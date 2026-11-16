#!/usr/bin/env python3
"""One-time, version-pinned finishing pass after the 198-edit v0.7.3 build.

Use --verify only after running assemble_draft07.py. All source checks and
edit anchors are validated before chapter writes. No network access is used.
"""
from __future__ import annotations
import argparse
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO = ROOT.parent
BASE = '8a11d6ab721cb41d9cda8341daa7c2952c50dea9'
REPORT = ROOT / '04-Working-Notes/draft-07-v0.7.4-applied.md'
P3 = '02-Parts/Part-3-First-Empires/draft-07.md'
P4 = '02-Parts/Part-4-Middle-Bronze/draft-07.md'
P5 = '02-Parts/Part-5-Cosmopolitan-Age/draft-07.md'
EDITS = [
(P3, 'P3-EGYPT-EVIDENCE', 'Now put Egypt next to Akkad, because the dates are the point.',
 "Now put Egypt beside Akkad. Late in the third millennium BCE, the kingdom that had built the great pyramids broke into competing regional powers. Poor Nile floods may have added to its troubles. One provincial governor boasted in his tomb that he had kept his district fed while other people starved. That is a ruler telling posterity why he deserves to be remembered, not a survey of the whole country. But it tells us what he wanted credit for: keeping food available when other authorities could not.", 'paragraph'),
(P3, 'P3-EGYPT-SYNCHRONY', 'The first empire in Iraq and the oldest kingdom on the Nile came apart within a few decades of each other.',
 "The Egyptian and Iraqi disruptions belong to the same broad period. Some chronologies bring them close together, but the dates do not give us two synchronized disasters. I think the comparison is worth making anyway. Environmental pressure could make it harder for either government to hold its provinces together. Whether the same climatic change helped weaken both remains an open question.", 'paragraph'),
(P3, 'P3-EGYPT-RETURN', 'Egypt put itself back together after about a century. Back to Iraq.',
 "Egypt eventually reunited. For now, come back to Iraq.", 'replace'),
(P4, 'P4-OPENING-LETTERS', "He's seven hundred miles away. He's been away for years.",
 "He's far away, doing business in another country. The cloth she makes travels out to him with the caravans; complaints come back. The pieces are too small. The quality isn't right. She has some answers for him.", 'paragraph'),
(P4, 'P4-SEPARATE-REPLIES', 'Her answer survives. In effect,',
 "Her replies survive. In one letter she discusses the size of the pieces and how much wool she has put into them. In another, she wants to know who is in his house finding fault with her cloth. These are separate letters, but the frustration runs through them. She is managing the work at home, and the man abroad keeps sending instructions.", 'paragraph'),
(P4, 'P4-TIN-QUANTITY', "There's a little tin in their mountains, but nowhere near enough for what they want to make.",
 "There is evidence for local tin production in Anatolia too. But imported tin was central to this trading business.", 'replace'),
(P4, 'P4-PRIVATE-LITERACY', "That would make this the earliest place we can watch reading and writing get loose from the temple and the palace.",
 "The letters give us an unusually vivid view of writing used inside trading households, far beyond royal proclamations.", 'replace'),
(P4, 'P4-MINERS-PREMISE', "Between Egypt and the land of Canaan there's a desert peninsula called the Sinai,",
 "Between Egypt and Canaan lies the Sinai Peninsula, where Egyptians mined turquoise. People from Canaan joined the expeditions, bringing a language related to later Hebrew into a landscape covered with Egyptian inscriptions. Somewhere in this wider world of contact, people began experimenting with a different way to write.", 'paragraph'),
(P4, 'P4-ALPHABET-PROPOSAL', "Here's the best current guess about what happened next.",
 "One influential explanation places an important part of that experiment among the people working around those mines. Take a picture and use it for the first sound of the word in your own language. The word for ox was something like alef, so an ox's head could stand for its opening sound. The word for house was bet. A little picture of a house could stand for B. You no longer needed a separate sign for every thing you wanted to name.", 'paragraph'),
(P4, 'P4-WORKER-STATUS', "The letters don't say which, because to the people writing them it wasn't an interesting difference.",
 "The letters do not always give us enough information to recover each worker's legal position.", 'replace'),
(P4, 'P4-FAMILY-END', 'And what became of Lamassi and Pushu-ken?',
 "And what became of Lamassi and Pushu-ken? The record doesn't give us a neat last scene with the couple together. Later letters concern their children and the division of family property, including their sister's claim to a share. The business outlived the correspondence we have been listening to. I would rather leave the end of the marriage open than invent the homecoming their letters make us hope for.", 'paragraph'),
(P5, 'P5-KHAEMWASET-MONUMENT', "One of Ramses' sons spent those peaceful years on something unusual.",
 "One of Ramses' sons spent those peaceful years looking much further back. His name was Khaemwaset, and he was high priest at Memphis, Egypt's old capital near the pyramids. On one old pyramid, an inscription credits him with preserving the name of the king who built it. By then that king had been dead for more than a thousand years. So here is an Egyptian prince looking at monuments already ancient to him, and making sure an earlier ruler's name stays attached to the stone. He made sure his own name was there too.", 'paragraph'),
]
SOURCES = {
P3: [
 'Erdil et al. (2025), Resolution of the High versus Low debate for Old and Middle Kingdom Egypt: https://doi.org/10.1371/journal.pone.0314612',
 'Round 3 review, regional environmental evidence and chronology limits: https://app.notion.com/p/41ae5852471e8182b652e2e2456c81ad'],
P4: [
 'Cecile Michel, Women of Assur and Kanesh (2020), texts 164-165 (BIN 4, 10; BIN 6, 11); letter boundaries checked in Round 3: https://app.notion.com/p/41ae5852471e8182b652e2e2456c81ad',
 'Michel, Taram-Kubi, Assyrian housewife and businesswoman: https://www.csmc.uni-hamburg.de/publications/mesopotamia/2020-10-31.html',
 'Part 4 review and remaining verification: https://app.notion.com/p/41ae5852471e816b8ad0e7f456845932'],
P5: [
 'Campbell Price (2022), The Legacy of Prince Khaemwaset at Saqqara, section 4 and the Unas pyramid inscription: https://www.mdpi.com/2571-9408/5/3/115']}


def source_paths():
    paths = sorted(ROOT.glob('02-Parts/*/*draft-07.md'))
    if len(paths) != 10:
        raise ValueError(f'Expected 10 chapter files, found {len(paths)}')
    return paths


def parts(text):
    head, rest = text.split('## The Draft', 1)
    body, notes = rest.split('## Revision notes', 1)
    return head, body, notes


def clean(body):
    lines = [x for x in body.splitlines() if x.strip() != '---' and not x.strip().startswith('[VISUAL:')]
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(lines)).strip()


def apply():
    paths = source_paths()
    staged = {}
    for path in paths + [ROOT / 'tools/assemble_draft07.py']:
        rel = path.relative_to(REPO).as_posix()
        expected = subprocess.check_output(['git', 'show', BASE + ':' + rel], cwd=REPO)
        actual = path.read_bytes()
        if expected != actual:
            raise SystemExit('Source changed since v0.7.3; refusing stale edit: ' + rel)
        staged[path] = actual.decode('utf-8')
    for rel, ident, anchor, replacement, mode in EDITS:
        path = ROOT / rel
        head, body, notes = parts(staged[path])
        if body.count(anchor) != 1:
            raise SystemExit(f'Nonunique or missing anchor {ident}; no chapter files written')
        start = body.index(anchor)
        if mode == 'replace':
            body = body.replace(anchor, replacement, 1)
        else:
            if start and body[start-1] != '\n':
                raise SystemExit('Paragraph anchor must begin at line boundary: ' + ident)
            end = body.find('\n\n', start)
            if end < 0:
                raise SystemExit('Missing paragraph boundary: ' + ident)
            body = body[:start] + replacement + body[end:]
        staged[path] = head + '## The Draft' + body + '## Revision notes' + notes
    for path in paths:
        text = staged[path]
        text = text.replace('## SEVENTH DRAFT — v0.7.3', '## SEVENTH DRAFT — v0.7.4', 1)
        rel = path.relative_to(ROOT).as_posix()
        applied = [x[1] for x in EDITS if x[0] == rel]
        note = ('## Revision notes — v0.7.4\n\n'
                '- Finishing pass after v0.7.3: ' + (', '.join(applied) if applied else 'version and assembly synchronization; no new narration changes in this section') + '.\n'
                '- See `04-Working-Notes/draft-07-v0.7.4-applied.md`. Prior verification limits remain; this is not a final recording clearance.\n')
        if rel in SOURCES:
            note += '\n' + ''.join('- ' + src + '\n' for src in SOURCES[rel])
        text = text.replace('## Revision notes — v0.7.3\n', note + '\n### Earlier v0.7.3 implementation record\n', 1)
        staged[path] = text
    builder = ROOT / 'tools/assemble_draft07.py'
    if staged[builder].count('v0.7.3') != 2:
        raise SystemExit('Unexpected builder version layout; no files written')
    staged[builder] = staged[builder].replace('v0.7.3', 'v0.7.4')
    report = [
        '# Draft-07 v0.7.4 — finishing check and handoff state', '',
        'Baseline: `8a11d6ab721cb41d9cda8341daa7c2952c50dea9` (v0.7.3).',
        'Original v0.7.2 preserved at `archive/draft07-v0.7.2-before-chatgpt-edit`.', '',
        '## What actually changed', '',
        f'{len(EDITS)} additional anchored repairs in Parts 3, 4, and 5, following the 198-edit v0.7.3 pass. All ten chapter headers and the narration/cue-sheet build are synchronized to v0.7.4. The combined total of 210 is an edit-operation count, not 210 independent historical issues certified as resolved.', '',
        'These repairs remove the remaining synchronized Egypt/Akkad claim, distinguish Lamassi\'s separate letters, narrow unsupported tin and private-literacy superlatives, make the Sinai origin proposal consistently provisional, remove an invented motive for silence about worker status, avoid unverified precise household death dates, and replace the blanket pyramid-restoration story with a specific attributed inscription.', '',
        '## Additional changes', '']
    report += [f'- {ident} (`{rel}`): {anchor}' for rel, ident, anchor, _, _ in EDITS]
    report += ['', '## Source and review references', '']
    for rel, srcs in SOURCES.items():
        report += [f'### {rel}', ''] + ['- ' + s for s in srcs] + ['']
    report += ['## Current division of work', '',
        'Jacob is the final creative authority. ChatGPT implements edits. Claude/Fable provides advice and second-reader critique without blocking routine corrections. Alfred, Jacob\'s ChatGPT dot, is the requested continuation owner after the Notion handoff. No agent was automatically started by this build.', '',
        '## Not finished / next work', '',
        'This is a substantial correction pass, not certification of all historic detail. Retain the original review pages as evidence trails, but recheck current text before applying an old finding. A whole-series cold-listener and read-aloud pass remains. The quotation ledger must identify each text, translator, edition, exact wording, and treatment as quote/paraphrase/reconstruction. Remaining factual checks include inherited numerical claims in Parts 1-5, precise Ugarit letter sequencing/findspots, Pylos interpretations, and archaeological dates. Earlier revision notes marked [sure] are not a substitute for verification.', '',
        'Selective physical context belongs in the narration when it answers a listener\'s likely question; it is not a direction to add scenery everywhere. Preserve humor, narrative energy, useful analogies, and clearly announced imagined scenes. Video production remains deferred.', '',
        '## Build verification', '',
        'VERIFICATION_PENDING', '',
        '## Files and rebuild', '',
        'Edit the individual draft-07 chapters under `BZ-Age/02-Parts`, then run `python3 tools/assemble_draft07.py` from `BZ-Age/`. The generated narration is `BZ-Age/BZ-Age-draft07-audiobook.md`.',
        'The two migration scripts are historical, version-pinned one-time edits, not normal build commands. Do not rerun them in apply mode on later drafts. Their workflows trigger only when those migration files change; they are not recurring schedules. Use the assembler for future edits.', '',
        'The v0.7.3 `--verify` command is version-specific and is superseded for this version by `python3 tools/finish_editorial_20261116.py --verify`. A later substantive revision needs a newly appropriate verification check.', '']
    staged[REPORT] = '\n'.join(report)
    for path, text in staged.items():
        path.write_text(text.rstrip() + '\n', encoding='utf-8')
    print(json.dumps({'status': 'applied', 'additional_edits': len(EDITS)}, indent=2))


def verify():
    expected = []
    total = 0
    table = []
    for path in source_paths():
        text = path.read_text(encoding='utf-8')
        head, body, _ = parts(text)
        if '## SEVENTH DRAFT — v0.7.4' not in head:
            raise SystemExit('Wrong source version: ' + str(path))
        title = text.splitlines()[0].lstrip('# ').strip()
        cleaned = clean(body)
        words = len(cleaned.split())
        total += words
        table.append((title, words))
        expected.append(f'# {title}\n\n{cleaned}\n')
    assembly = (ROOT / 'BZ-Age-draft07-audiobook.md').read_text(encoding='utf-8')
    if not assembly.startswith('# BZ-Age — Draft-07 Narration (v0.7.4)'):
        raise SystemExit('Wrong assembly version')
    _, actual = assembly.split('# Series Cold Open / Prologue', 1)
    actual = '# Series Cold Open / Prologue' + actual
    if actual != '\n\n'.join(expected):
        raise SystemExit('Assembly/source mismatch')
    if '[VISUAL:' in assembly or '## Revision notes' in assembly:
        raise SystemExit('Editorial notes leaked into narration')
    for rel, ident, _, replacement, _ in EDITS:
        if replacement not in parts((ROOT / rel).read_text(encoding='utf-8'))[1]:
            raise SystemExit('Applied edit missing: ' + ident)
    verified = ('All ten assembled narration sections exactly match their source chapter narration after the documented cue/note filtering. '
                f'{total:,} spoken words. At an assumed 150 words/minute, approximately {total/150/60:.1f} hours; no audio was generated. '
                'All 12 finishing replacements are present. Script compilation and git diff --check are separate workflow gates.\n\n'
                '| Section | Words |\n| --- | --- |\n' + '\n'.join(f'| {t} | {w:,} |' for t, w in table))
    report = REPORT.read_text(encoding='utf-8')
    if 'VERIFICATION_PENDING' in report:
        REPORT.write_text(report.replace('VERIFICATION_PENDING', verified), encoding='utf-8')
    print(json.dumps({'status': 'verified', 'sections': 10, 'additional_edits': len(EDITS), 'spoken_words': total}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    verify() if args.verify else apply()
