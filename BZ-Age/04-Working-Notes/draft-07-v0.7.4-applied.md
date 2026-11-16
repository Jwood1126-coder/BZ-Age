# Draft-07 v0.7.4 — finishing check and handoff state

Baseline: `8a11d6ab721cb41d9cda8341daa7c2952c50dea9` (v0.7.3).
Original v0.7.2 preserved at `archive/draft07-v0.7.2-before-chatgpt-edit`.

## What actually changed

12 additional anchored repairs in Parts 3, 4, and 5, following the 198-edit v0.7.3 pass. All ten chapter headers and the narration/cue-sheet build are synchronized to v0.7.4. The combined total of 210 is an edit-operation count, not 210 independent historical issues certified as resolved.

These repairs remove the remaining synchronized Egypt/Akkad claim, distinguish Lamassi's separate letters, narrow unsupported tin and private-literacy superlatives, make the Sinai origin proposal consistently provisional, remove an invented motive for silence about worker status, avoid unverified precise household death dates, and replace the blanket pyramid-restoration story with a specific attributed inscription.

## Additional changes

- P3-EGYPT-EVIDENCE (`02-Parts/Part-3-First-Empires/draft-07.md`): Now put Egypt next to Akkad, because the dates are the point.
- P3-EGYPT-SYNCHRONY (`02-Parts/Part-3-First-Empires/draft-07.md`): The first empire in Iraq and the oldest kingdom on the Nile came apart within a few decades of each other.
- P3-EGYPT-RETURN (`02-Parts/Part-3-First-Empires/draft-07.md`): Egypt put itself back together after about a century. Back to Iraq.
- P4-OPENING-LETTERS (`02-Parts/Part-4-Middle-Bronze/draft-07.md`): He's seven hundred miles away. He's been away for years.
- P4-SEPARATE-REPLIES (`02-Parts/Part-4-Middle-Bronze/draft-07.md`): Her answer survives. In effect,
- P4-TIN-QUANTITY (`02-Parts/Part-4-Middle-Bronze/draft-07.md`): There's a little tin in their mountains, but nowhere near enough for what they want to make.
- P4-PRIVATE-LITERACY (`02-Parts/Part-4-Middle-Bronze/draft-07.md`): That would make this the earliest place we can watch reading and writing get loose from the temple and the palace.
- P4-MINERS-PREMISE (`02-Parts/Part-4-Middle-Bronze/draft-07.md`): Between Egypt and the land of Canaan there's a desert peninsula called the Sinai,
- P4-ALPHABET-PROPOSAL (`02-Parts/Part-4-Middle-Bronze/draft-07.md`): Here's the best current guess about what happened next.
- P4-WORKER-STATUS (`02-Parts/Part-4-Middle-Bronze/draft-07.md`): The letters don't say which, because to the people writing them it wasn't an interesting difference.
- P4-FAMILY-END (`02-Parts/Part-4-Middle-Bronze/draft-07.md`): And what became of Lamassi and Pushu-ken?
- P5-KHAEMWASET-MONUMENT (`02-Parts/Part-5-Cosmopolitan-Age/draft-07.md`): One of Ramses' sons spent those peaceful years on something unusual.

## Source and review references

### 02-Parts/Part-3-First-Empires/draft-07.md

- Erdil et al. (2025), Resolution of the High versus Low debate for Old and Middle Kingdom Egypt: https://doi.org/10.1371/journal.pone.0314612
- Round 3 review, regional environmental evidence and chronology limits: https://app.notion.com/p/41ae5852471e8182b652e2e2456c81ad

### 02-Parts/Part-4-Middle-Bronze/draft-07.md

- Cecile Michel, Women of Assur and Kanesh (2020), texts 164-165 (BIN 4, 10; BIN 6, 11); letter boundaries checked in Round 3: https://app.notion.com/p/41ae5852471e8182b652e2e2456c81ad
- Michel, Taram-Kubi, Assyrian housewife and businesswoman: https://www.csmc.uni-hamburg.de/publications/mesopotamia/2020-10-31.html
- Part 4 review and remaining verification: https://app.notion.com/p/41ae5852471e816b8ad0e7f456845932

### 02-Parts/Part-5-Cosmopolitan-Age/draft-07.md

- Campbell Price (2022), The Legacy of Prince Khaemwaset at Saqqara, section 4 and the Unas pyramid inscription: https://www.mdpi.com/2571-9408/5/3/115

## Current division of work

Jacob is the final creative authority. ChatGPT implements edits. Claude/Fable provides advice and second-reader critique without blocking routine corrections. Alfred, Jacob's ChatGPT dot, is the requested continuation owner after the Notion handoff. No agent was automatically started by this build.

## Not finished / next work

This is a substantial correction pass, not certification of all historic detail. Retain the original review pages as evidence trails, but recheck current text before applying an old finding. A whole-series cold-listener and read-aloud pass remains. The quotation ledger must identify each text, translator, edition, exact wording, and treatment as quote/paraphrase/reconstruction. Remaining factual checks include inherited numerical claims in Parts 1-5, precise Ugarit letter sequencing/findspots, Pylos interpretations, and archaeological dates. Earlier revision notes marked [sure] are not a substitute for verification.

Selective physical context belongs in the narration when it answers a listener's likely question; it is not a direction to add scenery everywhere. Preserve humor, narrative energy, useful analogies, and clearly announced imagined scenes. Video production remains deferred.

## Build verification

All ten assembled narration sections exactly match their source chapter narration after the documented cue/note filtering. 40,585 spoken words. At an assumed 150 words/minute, approximately 4.5 hours; no audio was generated. All 12 finishing replacements are present. Script compilation and git diff --check are separate workflow gates.

| Section | Words |
| --- | --- |
| Series Cold Open / Prologue | 1,594 |
| Part 1 — Before Bronze | 4,380 |
| Part 2 — The First Cities | 4,978 |
| Part 3 — The First Empires | 4,296 |
| Part 4 — The Merchants and the Lawgiver | 4,829 |
| Part 5 — The Brotherhood of Kings | 5,272 |
| Part 6 — The Slow Part | 3,833 |
| Part 7 — The Collapse | 3,386 |
| Part 8 — After | 3,653 |
| Part 9 — What Survived | 4,364 |

## Files and rebuild

Edit the individual draft-07 chapters under `BZ-Age/02-Parts`, then run `python3 tools/assemble_draft07.py` from `BZ-Age/`. The generated narration is `BZ-Age/BZ-Age-draft07-audiobook.md`.
The two migration scripts are historical, version-pinned one-time edits, not normal build commands. Do not rerun them in apply mode on later drafts. Their workflows trigger only when those migration files change; they are not recurring schedules. Use the assembler for future edits.

The v0.7.3 `--verify` command is version-specific and is superseded for this version by `python3 tools/finish_editorial_20261116.py --verify`. A later substantive revision needs a newly appropriate verification check.
