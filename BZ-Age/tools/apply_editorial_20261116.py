#!/usr/bin/env python3
"""Apply the authorized November 16 editorial pass, or verify its outputs.

All chapter blobs and edit anchors are checked before any file is written.
This is a one-time migration from ef7b943, not an ongoing unattended editor.
No network access, external packages, or credentials are used by this script.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import pathlib
import re
import runpy
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE_COMMIT = 'ef7b94391ea80b9bba260c4e00725f1960238992'
FILES = {
0: ('02-Parts/Part-00-Prologue/cold-open-draft-07.md', 'efccf02b2f845d3ef171edcff0d1d29aae019a41'),
1: ('02-Parts/Part-1-Before-Bronze/draft-07.md', '63ba7ecba867699b13b485836d68e7ddc1bb9e75'),
2: ('02-Parts/Part-2-First-Cities/draft-07.md', 'ae69a442ebd51c8770391f8ac3a5f435ffe5b80a'),
3: ('02-Parts/Part-3-First-Empires/draft-07.md', 'c1736e415c20e8fc95b9d657af4311c91aba31d2'),
4: ('02-Parts/Part-4-Middle-Bronze/draft-07.md', '095ff19f71e3838313504d8482fc00599d32fbfe'),
5: ('02-Parts/Part-5-Cosmopolitan-Age/draft-07.md', '29226100b8d705152f2c742d61e181f6921ffe52'),
6: ('02-Parts/Part-6-Crisis-Builds/draft-07.md', '93f0f3735c2b9e1022c68e3f1382d8c5f8c953d3'),
7: ('02-Parts/Part-7-Collapse/draft-07.md', '9d8abe0b316304ccb9dc000d7970f5003225be0a'),
8: ('02-Parts/Part-8-Long-Aftermath/draft-07.md', '243131da1a5ea6a98f99cda940f5cab11917916a'),
9: ('02-Parts/Part-9-Inheritance-Memory/draft-07.md', '7e059f78eda7f790bbd5c40d295a93901aa27994'),
}
BRIEF = '04-Working-Notes/draft-07-brief.md'
BUILDER = 'tools/assemble_draft07.py'
EXTRA_HASHES = {BRIEF: '30db72020e239f23a580ff999e0f8805d47433da', BUILDER: 'd25cf2c79202937ab69cb6519b67beb17bd9b6eb'}
DATA = runpy.run_path(str(ROOT / 'tools/editorial_20261116_changes.py'))
PATCHES = DATA['PATCHES']
SOURCES = DATA['SOURCES']
REPORT = ROOT / '04-Working-Notes/draft-07-v0.7.3-applied.md'


def blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def split_chapter(text: str) -> tuple[str, str, str]:
    if text.count('## The Draft') != 1 or text.count('## Revision notes') != 1:
        raise ValueError('Expected exactly one narration and revision-notes boundary')
    head, rest = text.split('## The Draft', 1)
    body, notes = rest.split('## Revision notes', 1)
    return head, body, notes


def apply_one(body: str, edit: dict) -> str:
    anchor, replacement = edit['anchor'], edit['text']
    count = body.count(anchor)
    if count != 1:
        raise ValueError(f"{edit['issue']}: anchor occurs {count} times: {anchor!r}")
    start = body.index(anchor)
    mode = edit['mode']
    if mode == 'replace':
        return body.replace(anchor, replacement, 1)
    if start and body[start - 1] != '\n':
        raise ValueError(f"{edit['issue']}: paragraph/span does not start on a line boundary")
    if mode == 'span':
        end_anchor = edit['end']
        if body.count(end_anchor) != 1:
            raise ValueError(f"{edit['issue']}: end anchor not unique")
        end = body.index(end_anchor, start + len(anchor))
        return body[:start] + replacement.rstrip() + '\n\n' + body[end:]
    end = body.find('\n\n', start)
    if end < 0:
        end = len(body)
    if mode == 'paragraph':
        return body[:start] + replacement.rstrip() + body[end:]
    if mode == 'after':
        return body[:end] + '\n\n' + replacement.rstrip() + body[end:]
    raise ValueError(f'Unknown edit mode: {mode}')


def clean_narration(body: str) -> str:
    kept = [line for line in body.splitlines()
            if line.strip() != '---' and not line.strip().startswith('[VISUAL:')]
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(kept)).strip()


def apply() -> None:
    staged = {}
    errors = []
    original = {}
    for part, (rel, expected) in FILES.items():
        raw = (ROOT / rel).read_bytes()
        if blob_sha(raw) != expected:
            errors.append(f'Stale source: {rel}; expected {expected}, got {blob_sha(raw)}')
        original[part] = raw.decode('utf-8')
    for rel, expected in EXTRA_HASHES.items():
        raw = (ROOT / rel).read_bytes()
        if blob_sha(raw) != expected:
            errors.append(f'Stale supporting file: {rel}')
    if errors:
        raise SystemExit('\n'.join(errors))
    ids = [e['issue'] for e in PATCHES]
    if len(ids) != len(set(ids)):
        raise SystemExit('Duplicate change IDs')
    counts = {}
    for part, (rel, _) in FILES.items():
        head, body, notes = split_chapter(original[part])
        edits = [e for e in PATCHES if e['part'] == part]
        counts[part] = len(edits)
        for edit in edits:
            try:
                body = apply_one(body, edit)
            except (ValueError, KeyError) as exc:
                errors.append(f'Part {part}: {exc}')
        if not edits:
            errors.append(f'No edits supplied for part {part}')
        if len(clean_narration(body).split()) < (700 if part == 0 else 1800):
            errors.append(f'Unexpectedly short narration: {rel}')
        head = re.sub(r'^## SEVENTH DRAFT[^\n]*', '## SEVENTH DRAFT — v0.7.3', head, flags=re.M)
        head = re.sub(r'^\*\*Status:\*\*[^\n]*', '**Status:** ChatGPT implementation of the editorial review and Jacob\'s selective scene-setting direction. Source version ef7b943; changed passages and continuity corrected. Not a final recording clearance or an exhaustive fact check.', head, flags=re.M)
        old_notes = notes.split('\n', 1)[1] if '\n' in notes else notes
        revision = ('## Revision notes — v0.7.3\n\n'
                    '- Applied by ChatGPT under Jacob\'s instruction to make edits directly; Claude/Fable is an advisor and second reader, not a blocking approver.\n'
                    '- Selective physical reconstruction stays marked in the narration. Solid claims are stated plainly; uncertain documentary sequences and causal inferences are narrowed.\n'
                    '- Changes in this section: ' + ', '.join(e['issue'] for e in edits) + '.\n'
                    '- See `04-Working-Notes/draft-07-v0.7.3-applied.md` for scope, sources, remaining checks, and validation.\n\n'
                    '### Source and review references for this pass\n\n' + ''.join('- ' + x + '\n' for x in SOURCES.get(str(part), [])) + '\n'
                    '### Earlier revision record — historical, not current verification\n\n'
                    'The following notes document the earlier draft. Any claim contradicted by the v0.7.3 narration is superseded; an old `[sure]` label is not recording clearance.\n\n' + old_notes.lstrip())
        staged[rel] = head + '## The Draft' + body + revision
    if errors:
        raise SystemExit('No chapter files written. Validation failed:\n' + '\n'.join(errors))
    brief = (ROOT / BRIEF).read_text(encoding='utf-8')
    policy = '''## Current implementation authority and scene-setting — v0.7.3\n\nJacob has assigned ChatGPT responsibility for making and verifying edits. Claude/Fable advises, challenges, and reviews the diff; a missing response does not block routine corrections. Alfred, Jacob's ChatGPT dot, is the intended continuation owner after the handoff. This records Jacob's direction, not acceptance or activity by either advisor.\n\nWrite for a curious adult with no Bronze Age background. Establish relative time, physical place, relationships, immediate stakes, and the reason a scene follows. Add description selectively where it resolves a listener's question. Ask what a place or object looked like, how it worked, what could survive, and what the source actually lets us see. Clearly marked plausible reconstruction and enjoyable what-ifs are welcome. Do not turn a conjecture into eyewitness testimony, give an imagined person an invented statistic, or pad every paragraph with scenery. There is no word target. Video production remains deferred.\n\nThe household represents five kinds of work, not a real multigenerational bloodline or a universal model of social evolution. Preserve the revised thirty-year-old protagonist and grandmother near seventy. Later societies are not automatically freer, completely self-sufficient, or without kings. Different kinds of destruction and survival must shape the conclusions.\n\nThis implementation is separate from the earlier bounded critique window. It creates no new recurring task or automatic Claude restart. The detailed original reviews remain an audit trail, not a list of issues all certified as fixed.\n\n'''
    brief = brief.replace('## What the writer asked for', policy + '## What the writer asked for', 1)
    brief = brief.replace('Five people live in it and all of them do a bit of everything.', 'Six people belong to the illustrative household; five are present while the trading brother is away. Their work overlaps.')
    brief = brief.replace('Assyria the merchant city; Mitanni the horse kingdom; Alashiya the copper island', 'Assur the merchant city; Assyria the northern Iraqi kingdom; Mitanni the horse kingdom; Alashiya on Cyprus')
    brief = brief.replace('The first house holds six people.', 'Six people belong to the first household, with the brother away at the opening.')
    old_argument = 'The cast is the argument. One household splits into specialists who live in different countries and cannot eat without each other. That is the wealth of the Bronze Age and it is also why it fell. After the collapse the lines come back under one roof.'
    brief = brief.replace(old_argument, 'The cast makes changes in work and dependence intelligible. It does not prove a universal progression or a single cause of collapse. Some work stays local; some crosses regions. The aftermath contains continuing trade, states, and specialists as well as smaller communities.')
    staged[BRIEF] = brief
    builder = (ROOT / BUILDER).read_text(encoding='utf-8')
    if builder.count('v0.7.2') != 2:
        raise SystemExit('Unexpected assembler version layout; no files written')
    staged[BUILDER] = builder.replace('v0.7.2', 'v0.7.3')
    timestamp = datetime.now(timezone.utc).isoformat(timespec='seconds')
    lines = [
        '# Draft-07 v0.7.3 — applied editorial pass', '',
        f'Applied at {timestamp}. Baseline: `{BASE_COMMIT}`.',
        'Repository: `Jwood1126-coder/BZ-Age`; working branch: `claude/zealous-goldberg-6vhirf`.',
        'Original preserved at `archive/draft07-v0.7.2-before-chatgpt-edit`.', '',
        '## Actual scope', '',
        f'{len(PATCHES)} anchored edits across the prologue and Parts 1–9. The edits implement priority factual/continuity repairs and selective explanatory scene-setting; they are not a fresh rewrite of every paragraph or a certification of every claim.',
        'The source chapter files are authoritative. The narration and cue sheet are rebuilt with `python3 tools/assemble_draft07.py`; never edit the assembly instead of a chapter.', '',
        '## Roles and editorial contract', '',
        'Jacob retains final creative authority. ChatGPT makes and checks edits. Claude/Fable is an advisor and second reader. Alfred is the requested continuation owner; creating a handoff does not start another assistant or transfer an active session.',
        'Assume no prior Bronze Age knowledge. Context before unfamiliar names; accurate physical context when useful; locally marked reconstructions and what-ifs; no repetitive caveats around secure facts; no imposed length target; video work deferred.', '',
        '## Applied changes by section', '']
    for part, (rel, _) in FILES.items():
        label = 'Prologue' if part == 0 else f'Part {part}'
        lines += [f'### {label} — {counts[part]} edits', '', f'`{rel}`', '']
        lines += ['- ' + e['issue'] + ': ' + e['anchor'] for e in PATCHES if e['part'] == part]
        lines += ['', 'Source/review references:'] + ['- ' + x for x in SOURCES.get(str(part), [])] + ['']
    lines += ['## What remains open before recording', '',
        '- A source-by-source quotation ledger, including translator/edition and exact wording. Some inherited quotations and statistics remain to be checked.',
        '- Earlier-part claims not targeted by this pass: agricultural/labor numbers, exact early-city population and institutional reconstructions, specific Royal Tombs at Ur details, and detailed metallurgy attributions.',
        '- Exact sequencing and dates of Ugarit correspondence; particular destruction/hoard contexts; contested emergency interpretations at Pylos; attribution of Egyptian battle and settlement narratives.',
        '- Archaeological and textual dates should remain approximate where the evidence is approximate. A surviving inscription or archive does not date the last living reader.',
        '- A cold-listener read-through of all revised transitions, especially Parts 6–9, plus repetition and voice polish. Existing review issue IDs should be closed only after the complete issue, not merely one anchor, is rechecked.',
        '- New and old visual cues are retained for later planning, not newly researched production assets. Some inherited cues still require an accuracy pass before video work.', '',
        '## Validation', '',
        'Input chapter blobs and supporting-file hashes were checked before writing. Every edit anchor is unique and validated; failures abort all chapter writes. The one-time build regenerates narration/cues, independently checks assembly content, compiles the patch script, and runs `git diff --check` before committing. Consult the actual Actions result for success; this file alone is not proof the remote commit completed.', '',
        '## Review room', '',
        '- Master: https://app.notion.com/p/41ae5852471e81b69971e5fe89c3edb0',
        '- Exchange: https://app.notion.com/p/41ae5852471e81038c0dd73d87ae81c8',
        '- Round 3: https://app.notion.com/p/41ae5852471e8182b652e2e2456c81ad',
        '- Coverage ledger: https://app.notion.com/p/41ae5852471e81b0b921d325aa6535c4',
        '']
    staged[str(REPORT.relative_to(ROOT))] = '\n'.join(lines)
    # All preconditions have succeeded. Only now replace the selected files.
    for rel, text in staged.items():
        (ROOT / rel).write_text(text.rstrip() + '\n', encoding='utf-8')
    print(json.dumps({'status': 'applied_locally', 'anchored_edits': len(PATCHES), 'per_section': counts, 'files_written': list(staged)}, indent=2))


def verify() -> None:
    assembly = (ROOT / 'BZ-Age-draft07-audiobook.md').read_text(encoding='utf-8')
    if not assembly.startswith('# BZ-Age — Draft-07 Narration (v0.7.3)'):
        raise SystemExit('Wrong assembly version')
    expected_sections = []
    total = 0
    for part, (rel, _) in FILES.items():
        text = (ROOT / rel).read_text(encoding='utf-8')
        head, body, _ = split_chapter(text)
        if '## SEVENTH DRAFT — v0.7.3' not in head:
            raise SystemExit(f'Wrong chapter version: {rel}')
        title = text.splitlines()[0].lstrip('# ').strip()
        clean = clean_narration(body)
        total += len(clean.split())
        expected_sections.append(f'# {title}\n\n{clean}\n')
        for edit in (x for x in PATCHES if x['part'] == part):
            if edit['text'].strip() not in body:
                raise SystemExit(f"Applied text missing for {edit['issue']}")
    header, actual = assembly.split('# Series Cold Open / Prologue', 1)
    actual = '# Series Cold Open / Prologue' + actual
    expected = '\n\n'.join(expected_sections)
    if actual != expected:
        raise SystemExit('Narration assembly does not match all ten source chapters exactly')
    if '[VISUAL:' in assembly or '## Revision notes' in assembly:
        raise SystemExit('Editorial material leaked into narration')
    print(json.dumps({'status': 'verified', 'sections': 10, 'anchored_edits': len(PATCHES), 'spoken_words': total}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    verify() if args.verify else apply()
