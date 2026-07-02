# BZ-Age

A long-form, multi-part podcast series on the Bronze Age, built in the spirit of Dan Carlin's *Hardcore History*.

**Current phase:** Drafting, deep in (July 2026).
**Current status:** Full drafts exist for all ten parts. Draft-04 for the Prologue and Parts 1–2; draft-03 for Parts 3–9, with the draft-04 pass fully specced and ready to execute (`08-Fable-Dossier/14-draft-04-execution-spec.md`). A 16-file architecture/craft dossier (`08-Fable-Dossier/`) governs voice, cast, structure, and process. A narration-only full-series assembly exists (`BZ-Age-draft03-audiobook.md`). Drafts are append-only — every prior draft is preserved.

---

## Reading order for a new visitor

If you're new to the project (or returning after a gap), read in this order:

1. **[CLAUDE.md](./CLAUDE.md)** — the master prompt and editorial DNA. The single most important file in the repo. Load this into any AI session before doing anything else.
2. **[08-Fable-Dossier/00-INDEX.md](./08-Fable-Dossier/00-INDEX.md)** — the July 2026 architecture and craft layer: voice bible, decision log, cast bible, execution spec, operating manual. If you're an AI holding the pen, `01-opus-operating-manual.md` in that folder is your manual.
3. **[02-Parts/](./02-Parts/)** — the drafts themselves. Read the highest-numbered draft in each part folder; earlier drafts are the preserved record.
4. **[00-Editorial-DNA/](./00-Editorial-DNA/)** — voice, hard rules, posture, north star, the State of the World discipline. The values of the project.
5. **[01-Macro-Structure/](./01-Macro-Structure/)** — the nine-part-plus-coda arc, with defenses and alternatives considered.
6. **[06-Throughlines/](./06-Throughlines/)** — the running obsessions that thread through every part (note: #9 and #10 are now merged and promoted into `08-Fable-Dossier/08-reception-spine.md`).
7. **[04-Working-Notes/](./04-Working-Notes/)** — revision logs, fact-check digests, fleet findings, research digests; the *why* behind decisions.
8. **[05-Open-Questions/](./05-Open-Questions/)** — the still-genuinely-open questions (title, runtime, release cadence, and a few content items); most Phase One questions were resolved by the drafts.
9. **[03-Source-Map/](./03-Source-Map/)** — bibliography scaffolding. Honest status: sourcing currently lives inline in the drafts and in the fact-check digests; backfilling this folder from the finished drafts is queued work.
10. **[09-Archive/](./09-Archive/)** — superseded material, preserved but not live (including the early `07-Scripts` fork and the rev1 compile). See its README.

---

## The North Star

**Great storytelling.** Everything in this repo serves that goal. The rules, the throughlines, the contrarian-honest posture, the ground-level discipline — all of it exists to make the storytelling work harder. None of it is the goal itself. If a rule, applied rigidly, would kill a great story beat, the rule gives way.

The insight the series will (we hope) deliver — that people across the chasm of four thousand years were so different and yet so much the same — is an *outcome* of great storytelling about ancient humans. Not the goal of it. Backed into, not aimed at.

---

## How to work in this repo

This is a writing-and-research project organized using software-development tools. The mental model:

- The repo is the codebase.
- The Markdown files are the source files.
- `CLAUDE.md` is the project-level prompt that loads into any AI session.
- GitHub gives version control, history, branching for alternate drafts, and the issue tracker (which we use for open research questions).

The recommended client is **Obsidian** with one of the Claude plugins (claudian, Marx's Obsidian-AI, or the basic AI Assistant). Obsidian renders the Markdown beautifully and treats the folder as a knowledge vault with backlinks and search. Open the repo folder as an Obsidian vault and everything works.

You can also work in any Markdown editor — VS Code, Typora, plain text. The files are portable.

---

## Conventions

- **Markdown for everything.** Word documents get converted to MD when they land here.
- **kebab-case filenames.** No spaces.
- **One concept per file.** Long monolithic documents get broken up.
- **Revision log entries** on every substantive change. See `04-Working-Notes/Revision-Log.md`.
- **Open questions** live in `05-Open-Questions/` with the part they relate to and when they were raised.

---

## What this project is not

- Not a book. The deliverable is audio.
- Not an academic project. The deliverable is for general audiences.
- Not a news show. There is no urgency. Depth is the point.
- Not a lecture series. Story is primary, exposition serves story.
- Not a pop-history greatest-hits package. The pitch is "the Bronze Age you didn't know was there," not "the Bronze Age you've heard of."

---

## Version

- **2026-07-02 — v1.0.** Repo audit and reorganization. Phase status corrected everywhere (drafting is deep in progress, not "not yet started"); `08-Fable-Dossier/` added (16 files: voice bible, architecture critique, cast bible, bookends, reception spine, glimpse bank, beat menus, cold-open menus, recency flags, influences, draft-04 execution spec, Opus operating manual, decision log); superseded material moved to `09-Archive/` (the `07-Scripts` v0.1 fork, `BZ-Age-rev1.md`, three finished working-notes docs); first full push to GitHub; `HOW-TO-PUSH.md` rewritten for the live-repo workflow. Reading order updated.
- **2026-05-27 — v0.14.** Sequential v0.1 opening script drafts created for Parts 1–9 in `07-Scripts/`. Each draft is source-flagged and limited to an opening movement / first script section, not a complete episode script. Added `07-Scripts/README.md` as a script index and drafting note. `CLAUDE.md` restored to prior wording and should not be edited for script-drafting metadata.
- **2026-05-27 — v0.6.** First provisional script copy begun at user request. New file `07-Scripts/part-1-before-bronze-v0.1.md` drafts the opening movement for Part 1, using the full current project library as framing and carrying explicit source-check flags because the source maps remain placeholders. README updated so future sessions know source-flagged script copy now exists.
- **2026-05-27 — v0.5.** Added Rule 11 (Turning Points and their human consequence) as a recurring discipline. New file `00-Editorial-DNA/08-turning-points.md`. New `04-Working-Notes/archetypes.md` tracking the recurring vantage figures the series can call back to across parts (the Neolithic farmer, the Sumerian scribe, the Old Assyrian merchant's wife, the Late Bronze Age dockworker, etc.). Turning Points sections added to all nine part outlines — full content for Parts 1–5; seeds for Parts 6–9. CLAUDE.md updated with Rule 11, Move H (Draft a Turning Point Beat), turning-point-specific failure modes, and updated standard per-part outline structure. Final structural addition before handoff to GitHub.
- **2026-05-27 — v0.4.** Added Rule 10 (State of the World snapshots) as a recurring discipline. New file `00-Editorial-DNA/07-state-of-the-world.md`. State of the World snapshot sections added to all nine part outlines — Parts 1, 2, 3, 5 with full sketches; Parts 4, 6, 7, 8, 9 with seeds. Editorial DNA file numbering cleaned up.
- **2026-05-27 — v0.3.** CLAUDE.md refined as an operating toolkit (master-editor for Carlin-style podcast format) with explicit operational moves and decision heuristics. Open Questions directory populated with per-part files. Push instructions and .gitignore added.
- **2026-05-26 — v0.2.** Initial repo structure created. Editorial DNA locked. Parts 1–5 outlined; 6–9 sketched. Source map skeleton seeded. Hard Rule 9 (Anticipated Questions) added. CLAUDE.md master prompt created. North star refined to put storytelling primary, with so-different-yet-so-same as outcome rather than goal.

See `04-Working-Notes/Revision-Log.md` for full history.
