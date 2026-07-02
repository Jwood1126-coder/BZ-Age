# The Opus Operating Manual — How to Use This Dossier

**Written:** July 2, 2026 (Fable). If you are the model reading this, you now hold the pen on a
project a temporary collaborator helped architect. This file is your boot sequence, your recipes,
and your guardrails. It assumes you have already read `CLAUDE.md` (the master editor contract)
and will follow the repo's Editorial DNA; this manual layers the dossier on top of that.

**The relationship, in one line:** the writer (Jake) decides; you execute, draft, and flag; the
dossier holds the taste and the architecture that were built while Fable was here. When a rubric
in this dossier and your own judgment conflict, **flag the conflict for the writer — never
resolve it silently in either direction.**

---

## Boot sequence (any session)

1. `00-INDEX.md` — what exists, current status.
2. `02-decision-log.md` — **settled positions. Do not reopen logged decisions silently.** If new
   evidence pushes against one, surface it; the writer decides.
3. `04-voice-bible.md` — read in full before writing ANY prose. It is the ear, codified.
4. Then only the files your task needs (map at the bottom).

## The five principles above everything

1. **Story first.** Every rule below is craft in service of storytelling; when a rule would kill
   a great beat, flag the collision for the writer (Hard Rule 0's spirit).
2. **THE QUESTION ENGINE — the series' main theme.** The writer's words (July 2, 2026): answer
   the questions a child would ask, *"because adults are often too afraid to look stupid or
   honestly don't even know they need to answer these basic questions to understand the story,
   especially when it is essential to understand the context."* For every beat you write or
   revise, ask: **what is the embarrassingly basic question here, and does the material answer
   it?** The question is asked BARE, in the narrator's voice ("Why does every first civilization
   sit on a river?") — never announced as basic. The phrase-family "a ten-year-old would ask /
   sounds naive / too simple to ask / nobody thinks to ask" is **banned from script copy**; it
   was the writer's instruction to his editors, not a device for air.
3. **One voice (D-002).** The narrator's single voice writes all finished narration. You may hold
   that pen for specced work; you may never fan prose out to subagents or import another
   register. Quotes from primary sources are narrator-read.
4. **Honesty engineering (Hard Rule 7).** Never invent a source, quote, date, or fact. New
   specifics carry `[VERIFY]` until fleet-verified. Hedges are about *claims*, never about the
   narrator's virtue. **Every specific number spoken aloud is a promise** — if the source can't
   cash it, say "hundreds," not "569." Where a consensus claim matters, gesture at *how it's
   known* in one clause (the isotopes, the tablet, the stratigraphy).
5. **The payoff economy.** Plants and detonations are contracts: each payoff detonates ONCE, at
   its contracted site, with one-line chords elsewhere. A part's top payoffs must be *absent*
   from the prior part — forward leans name that something is coming, never what. Check
   `06-cast-bible.md`'s registry and the continuity ledger before striking any chord.

## Recipes

### A. Executing an edit spec (e.g., `14-draft-04-execution-spec.md`)
Follow its own procedure exactly. The rules that generalize to ALL spec work: copy the prior
draft first, never edit it (D-001, append-only drafts); edit only what's itemized; anything else
you notice becomes `[FLAGGED, NOT FIXED]` in the revision notes; more-than-a-clause new prose
gets `[PILOT-NEW-PROSE]` flagging for review; run the verification greps; write honest headers
(prose words ÷ 140–155 wpm); append versioned revision notes.

### B. Writing a new beat (from `12-beat-menus.md` or the writer's request)
Pre-flight checklist, in order:
1. The question-engine check (principle 2).
2. `04-voice-bible.md` quick-reference (its final checklist section) — especially: no sentence
   pointing at the writing; announcements replaced by payloads; one bow per beat; read it aloud.
3. Cast: does the beat touch a recurring figure? Registry check (`06-cast-bible.md` Part I);
   two-cue callbacks; time-honest kinship; log any new plant in the registry the same day.
4. Contracts: does it brush a planted payoff? (The known tripwires: iron, Hurrian hymn = "we can
   hear their music," unfired tablets, Hittite rediscovery, Linear B literacy loss, Indus
   script, "before the flood.") Don't pre-spend.
5. Reception spine: if the beat is a ruins/memory moment, check the verb table
   (`08-reception-spine.md`) — one reception element per part, no verb repeats (D-010).
6. Glimpses: one per part maximum, must do named story-work, P7 gets none (`10-glimpse-bank.md`).
7. Snapshots name their **season** and what it means for the body in it.
8. Facts: only from the research digests, the fleet-verified ledger, or `[VERIFY]`-tagged with
   the CAUTIONS honored. Never from episode transcripts (auto-captions garble), never from a
   summary site, never from model memory presented as sourced.
9. Credit: if a framing (not a fact) came from another creator, apply the three-tier policy in
   `15-influences.md` — use-or-credit, never silently borrow.

### C. Adding or changing structure
Argue it in the open (master-prompt non-negotiable 5): write the case, name the trade-offs, put
it to the writer, log the decision. Never build a rival structure quietly. The pending structural
decisions already queued for the writer: D-005 (grow P9), D-006 (trim P2), D-007 (P4–P5 dread
chords + question restoration).

### D. Running verification fleets
Journaled `Workflow` tool ONLY — plain background agents die on session interruptions and leave
no journal; workflows resume via `resumeFromRunId` with completed agents cached. Token
discipline: diff-scoped review (only changed regions), grep-first dossiers, model tiering
(cheap models search, the main model judges), skip items already FLEET-VERIFIED. Findings go to
a persistent file in `04-Working-Notes/` immediately — nothing valuable lives only in chat.

### E. Maintenance duties (do these without being asked)
Update the cast registry when planting or striking chords · add recency flags (`13-…`) when a
source suggests the field moved · keep `00-INDEX.md` statuses current · append revision-log
entries per pass · convert relative dates to absolute in any note you write.

## The do-not list

- Do not reopen logged decisions silently (D-001 … D-010 and successors).
- Do not put "ten-year-old / naive / too-simple" framing in script copy. Ever.
- Do not add series self-references ("this series…") — budget ≤1 navigational per part, zero
  self-praise.
- Do not pattern-sweep drafts (em-dashes, bows, Not-X-Not-Y) without an itemized, writer-approved
  order — the Voice Bible governs *new* prose and *specced* recasts only.
- Do not pre-spend a contracted detonation, and do not multiply chords past their caps.
- Do not adopt figures from other creators' content or summaries (the Uruk-90k example); our
  numbers come from the digests or get `[VERIFY]`.
- Do not overwrite any draft file, ever (D-001).
- Do not frame food-origins through plant/crop science — storage, labor, logistics, tax, climate
  (D-004; a safety filter once derailed a session on the other framing).
- Do not attempt to run user-billed review products (e.g., /code-review ultra) yourself.

## Escalate to the writer (don't decide)

Structural changes; anything touching the protected sentences named in `07-bookends.md`; new
cast members beyond the approved menu; any use of tier-2 borrowed framings (credit lines);
resolving a `[FLAGGED, NOT FIXED]` item; killing a beat the writer has praised; anything where
two dossier documents genuinely conflict.

## File map (which document for which job)

| Job | File |
|---|---|
| Any prose at all | `04-voice-bible.md` |
| Is this decided already? | `02-decision-log.md` |
| P3–P9 draft-04 edits | `14-draft-04-execution-spec.md` |
| New beats / filling gaps | `12-beat-menus.md`, `09-why-here-and-first-city.md` |
| Cold opens | `11-cold-open-menus.md` (verdicts + taxonomy) |
| Recurring people, callbacks, peak beats | `06-cast-bible.md` |
| Ruins/memory/reception moments | `08-reception-spine.md` |
| World-beyond-the-Near-East | `10-glimpse-bank.md` |
| Prologue/finale | `07-bookends.md` (protected-sentence lists) |
| Arc-level judgment calls | `05-architecture-critique.md` |
| Is this claim still current? | `13-recency-flags.md` |
| Borrowing/crediting from other shows | `15-influences.md` |
| Fact packets | `04-Working-Notes/draft-04-research-digest.md`, `draft-03-fact-check-digest.md`, `miano-notes.md` |

*Last note from Fable: the writer's ambition is "one of the truly great works of history series
on YouTube." The dossier is scaffolding toward that — not a ceiling. Where you see past it,
say so, in the open, and let him choose. That's what I was asked to do, and it's what he'll ask
of you.*
