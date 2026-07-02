# Draft-04 Execution Spec — Parts 3–9 (The Opus Pilot)

**Written:** July 2, 2026 (Fable), compiled from `04-Working-Notes/draft-04-fleet-findings.md` and
`04-Working-Notes/draft-04-research-digest.md`. Every fix below is fleet-confirmed; nothing here is
speculative. This document is the pilot test of the Fable-plans/Opus-executes model (decision D-003).

**Who executes this:** Opus 4.8, in a fresh session with this file, the Voice Bible
(`04-voice-bible.md`), and `CLAUDE.md` loaded.

---

## Procedure (per part, in order P3 → P9)

1. `cp 02-Parts/Part-N-<name>/draft-03.md 02-Parts/Part-N-<name>/draft-04.md` — **never edit
   draft-03; never skip the copy.** Draft-03 is the permanent record (decision D-001).
2. Read the new draft-04 file in full before editing.
3. Apply the part's itemized edits below, in the order given.
4. Update the header: `## FOURTH DRAFT — v0.4`, today's date, status line naming this spec, and an
   **honest audio estimate** (count prose words only — exclude headers/notes — and divide by 140–155
   wpm; state the word count).
5. Append a `## Revision notes — v0.4` section listing what changed, in the style of
   `Part-1-Before-Bronze/draft-04.md`. Flag every `[PILOT-NEW-PROSE]` item there explicitly.
6. Run the verification greps (below). Fix any failures before moving to the next part.

### Rules of engagement

- **Edit only what this spec itemizes.** No freelance improvements, no additional de-AI sweeps, no
  em-dash cleanup beyond listed items — pattern-level voice work is a separate Fable/writer pass.
  If you see something that looks wrong but isn't listed, note it in the revision notes as
  `[FLAGGED, NOT FIXED]` and leave the prose alone.
- **`[PILOT-NEW-PROSE]` items** (more than a clause of new prose) must match the Voice Bible and be
  flagged for Fable review. There are four: the P8 cold-open rewrite, the P3 music-and-games beat,
  the P7 harbor disambiguation, and the P6 rower-desk recast.
- **Example sentences in this spec show shape and register — you may use them verbatim or vary them
  minimally.** Do not invent new facts. Every fact you need is in this spec or the research digest;
  if a fix seems to require a fact not provided, stop and flag it.
- When cutting a sentence, read the seam aloud in your head: the paragraph must still hand off. If a
  cut orphans a transition, repair with the smallest possible stitch, not a new sentence of ideas.

### Verification greps (run per part on the new draft-04)

```
grep -c "this series" FILE                     # target: ≤1 (P6 and P7 keepers specified below)
grep -nE "ten-year-old|sounds naive|too simple to ask|nobody thinks to ask" FILE   # target: 0
grep -nE "And that matters|This matters because|the part that matters" FILE        # target: 0
grep -nE "Hold on to th|Hold that" FILE        # only the keepers listed per part
grep -n "Indo-European" FILE                   # P3, P4: 0. P9: unchanged.
diff Part-N/draft-03.md Part-N/draft-04.md     # confirm ONLY intended regions changed
```

---

## Part 3 — First Empires (`Part-3-First-Empires/`)

1. **L130 series self-billing.** "It's one of the best answers in this entire series, and I'm not
   going to give it to you yet" → keep the withholding, cut the billing: *"And I'm not going to give
   you the answer yet."* The withheld iron answer detonates in Part 5; the device is protected, the
   self-praise is not.
2. **L132 stacked hold.** Cut "Hold that idea too. The entire back half of this series lives inside
   it." entirely. The tin-question plant earlier ("Hold the question. Let it bother you a little")
   is the earned keeper and stays.
3. **Naive-question meta-frame.** "it's one of those questions that sounds naive and is actually the
   whole game" → cut that clause; keep the in-voice half. Result shape: *"And here a question should
   be forming, because it formed for me: iron ore is everywhere..."* ("the whole game" phrasing is
   reserved — it must not appear in P3.)
4. **KEEP (do not touch):** P3:144 "Not posthumously deified. Not symbolically divine. A god, during
   his own lifetime." This is the earned version of the Not-X-Not-Y move — precise escalation doing
   real work.
5. **Strip "Indo-European" from the Hittite mention.** "the Hittites — the Indo-European-speaking
   kingdom that has been consolidating the high plateau" → *"the Hittites — newcomers who have been
   consolidating the high plateau"*. This protects Part 9's decipherment thunderclap ("The Hittite
   language is Indo-European."), which currently lands pre-spent.
6. **`[PILOT-NEW-PROSE]` Music-and-games fabric beat (~200–280 words),** placed with the Royal
   Cemetery of Ur / Woolley material (the Lyres of Ur come from those very graves — that's the hook:
   the same pits that hold the death-ranks hold the band). Facts available, all digest-verified:
   - The Lyres of Ur, c. 2550–2450 BCE — bull-headed, lapis and gold, found crushed in the Royal
     Cemetery; among the world's oldest surviving stringed instruments.
   - The Royal Game of Ur — twenty-square race game from the same cemetery; people played it for
     ~2,000+ years; a Babylonian tablet let Irving Finkel reconstruct plausible rules (**hedge
     required:** the rules are a scholar's reconstruction from a much later tablet, not a certainty).
   - Dice and knucklebones existed; gaming was ordinary, not elite-only.
   - A plaque/imagery of wrestlers and boxers with musicians — sport with a live band.
   - Beer drunk through long straws from shared vessels (filters the mash).
   - **CAUTION:** do not claim any specific melody survives from this period; do not call any object
     a "toy" flatly (toys-vs-votive is unresolved — hedge or avoid).
   Register example (shape, not script): *"The same pits that hold the soldiers and the serving
   women hold a lyre — a bull's head in gold and lapis on the sound-box, strings long rotted, the
   wood long gone, the shape pressed into the soil. Somebody in that procession walked down playing
   it."* Write the beat, mark it `[PILOT-NEW-PROSE]` in the revision notes.

---

## Part 4 — Middle Bronze (`Part-4-Middle-Bronze/`)

1. **Question meta-frame.** "here is another of those questions nobody thinks to ask: what did a
   loan look like before banks?" → ask it bare: *"What did a loan look like before banks? It looked
   remarkably like a loan."* (The answer's first line is already the hook. "another" would dangle
   after the P1 cuts anyway.)
2. **L82 series-as-moral-agent.** "this series made a commitment in the first cities and this is
   where it comes due again" → cut the frame; open on the slavery material itself. If a bridge is
   needed: *"We looked at this squarely in the first cities. Here it is again."*
3. **L84.** "this series is not going to resolve the discomfort of holding them together, because
   the discomfort is accurate" → first person: *"I'm not going to resolve the discomfort of holding
   them together, because the discomfort is accurate."*
4. **Hammurabi stele "found, intact".** Digest-verified correction, and the honest version is
   better: the Elamite king who carried it to Susa **scraped off a band of Hammurabi's text to make
   room for his own inscription — and never wrote it.** The erased provisions survive from later
   manuscript copies. Rewrite the clause to that reality; drop "intact."
5. **"Great-great-great-grandmother" spanning 3,200 years.** Replace the kin-label with a
   time-honest formula that keeps the lineage feel: *"a hundred grandmothers back"* or *"the woman
   we started with, three thousand years before this letter."*
6. **Strip "Indo-European" from the Hittite reference** (same fix as P3 item 5; same reason).
7. **KEEP:** P4:24 "Not kings proclaiming victories. Not temple scribes counting rations. The first
   private voices." — earned. **FLATTEN:** P4:177 "Not perfectly. Not in the form a modern
   listener..." → ordinary syntax (e.g., *"imperfectly, and not in a form a modern listener would
   recognize"* — vary to fit the sentence).

---

## Part 5 — Cosmopolitan Age (`Part-5-Cosmopolitan-Age/`)

1. **THE DATE FIX (do this first — other fixes depend on it).** The Ugarit harbor snapshot header
   reads "approximately 1350 BCE" but its dread line says "They have forty or fifty more years."
   Ugarit burns ~1190–1185. **Re-date the snapshot header to "approximately 1230 BCE."** The dread
   line then becomes exact and stays. Then scan the snapshot body for anything Amarna-specific
   (pharaoh names, letter references, anything that only works at 1350): do NOT silently rewrite
   such cues — list each under `[FLAGGED, NOT FIXED]` for Fable review. Also add one line to
   `04-Working-Notes/archetypes.md` noting the dockworker anchor moved 1350 → ~1230.
2. **Ledger series-ref (brief's named cut target).** "The series has shown you this ledger three
   times now, in three civilizations, and it is the same ledger every time." → in-world recast that
   also fixes the fuzzy count: *"You have seen this ledger before — in Uruk, in Kanesh, on a ship's
   manifest. It is the same ledger every time."*
3. **L140.** "His lesson for this series is specific" → *"His lesson is specific"*. **KEEP L144**
   ("because late in this series, everything that happens to his world is going to be measured
   against this one ordinary morning") as the part's single allowed series reference.
4. **Instruction density.** KEEP: "Remember him. Remember the shelf." and the Mitanni hold. CUT or
   declarativize: L156 "Hold that. It will matter more than almost anything else in this hour." and
   L228 "Hold on to that through everything that's coming."
5. **L216.** Cut "Here's where the story goes somewhere unexpected." — spring the surprise, don't
   announce it.
6. **"Two things" scaffold used twice** (L152, L186). Convert L152's into flowing prose (the
   "First:/And second:" structure beneath it survives without the headline); L186 may stand.
7. **Mitanni topic-justification.** Cut "I want to flag this one specifically" and the
   "gets almost no airtime in popular tellings" clause; keep the hold/plant; soften "They matter."
   (the plant itself signals importance).
8. **Uluburun tin.** "The tin came from somewhere very far to the east" presupposes the contested
   side. Digest-verified reshape including the near option: *"where these particular ingots came
   from is a live fight in the laboratories — the Taurus Mountains a few weeks' walk from this
   coast, or mountains in Central Asia three thousand kilometers east; the isotopes are still
   arguing."*
9. **CUT (unverified fact):** "Cargo lists from this age elsewhere include human beings among the
   goods, entered in the same column-logic as the copper." No digest backing. The surrounding beat
   ("Part of what it cost was paid by people who never chose to be in the chain") already carries
   the weight. Cut the sentence; do not replace it.
10. **"Sixteen years later"** → *"Fifteen years later"* (Kadesh 1274, treaty 1259 — the series'
    own dates).
11. **Dockworker grounding (one clause).** The P7/P9 callbacks call this snapshot's "you" a
    dockworker, but the snapshot never puts the body in harbor labor. Add one clause that does both
    jobs — labor + the Part 2 echo. Shape: *"...the ache across your shoulder where the rope rides —
    the same shoulder the barge-pullers of Uruk wore raw two thousand years before you."*
12. **Pylos tricolon un-hedges the hedge.** "Bought, captured, or born into it, the figs are counted
    out the same." forecloses the digest's "refugees" possibility one sentence after the hedge
    honors it. Fix: *"Walked in desperate, bought, captured, or born into it — the figs are counted
    out the same."* (or cut the tricolon and let "the tablets say the rations" close the beat).
13. **Administrator chronology (option A — adopted).** Date the "ordinary morning at the peak" at
    Pylos explicitly late with one cue — shape: *"a long lifetime before the end"* — so P7/P8's
    "same man" callbacks hold. (P6's contradicting hedge is cut in P6 item 9.)
14. **Weaving-halls formula (cap: once outside P2).** P5:48 "what we've seen since the weaving
    halls of Uruk" → rephrase without the named formula: *"since the first ration lists in Sumer"*.
    P6's instance is the keeper.

---

## Part 6 — Crisis Builds (`Part-6-Crisis-Builds/`)

1. **Lamassi arithmetic (appears once, flagged thrice).** "unchanged from the form Lamassi would
   have recognized two centuries earlier" → *"nearly six centuries earlier"*. (P4 anchors her
   ~1800 BCE; the warehouse scene is ~1230 BCE. Six centuries strengthens the longevity point.)
2. **Pylos pre-detonation (protect Part 7's payoff).** Cut "Pylos will be destroyed thoroughly, and
   the Linear B tablets baked in the destruction fire are the most complete palace archive we have
   from Mycenaean Greece" — all of it. The rowers appear as an ominous plant only; the fire, the
   baking, and the archive's fate belong to Part 7 ("Remember the shelf" is the contract).
3. **`[PILOT-NEW-PROSE]` Rower-desk chord recast (2–3 sentences).** Current version claims rowers
   are new at the desk; P5's plant already had "rowers owed by the coastal towns" in the peak
   ledger. Recast as routine-vs-emergency, not absent-vs-present. Shape: *"The desk always counted
   rowers — owed by the coastal towns, annual, boilerplate. Now it counts rowers begged for,
   urgently, by name."*
4. **Medinet Habu → forward lean.** P6 currently describes the Ramses III inscription in full and
   P7 describes it again as if new. Reduce P6's version to a lean: the inscriptions exist, they name
   the groups, the battle itself belongs to the next part. (P7's full version then stands.)
5. **L32 billing trim.** "is one of the best stories this series has, and I am saving it,
   deliberately, for the very end" → keep the protected saving-device, cut the billing: *"...and I
   am saving it, deliberately, for the very end."*
6. **L94.** "feeding people this series hasn't told you about yet" → *"feeding people I haven't
   told you about yet"*.
7. **Imperative beat-openers → start in scene.** "Stay with what that actually means, in one body,
   on one farm on the plateau." → open on the body: *"A farmer in his forties has been measuring
   the same facts his whole life."* Same treatment for "Read that the way a Bronze Age listener
   would have" — give the Bronze Age reading directly.
8. **Aphorism bows (one per beat).** KEEP: "We don't find a prophet. We find an accountant." (hinge
   into the warehouse snapshot) and "Not screaming — boilerplate." CUT or demote the stacked
   runners-up around them, including the triple-bow run in could-they-see-it-coming (keep at most
   "You cannot diagnose the failure of a thing you do not know you are standing inside of" — the
   other two paragraph-final bows in that run flatten into their paragraphs).
9. **Chronology hedge (pairs with P5 item 13).** Delete "or his successor, a generation or two on"
   from the rower-requisition line — P5 now dates the peak morning late, so it's the same man.
10. **Buffer paragraph compression.** L126 re-argues the cold open at full length. Compress to two
    sentences that lean on it. Shape: *"I told you this disaster begins in sunshine. This is why —
    a well-buffered system looks fine until it is almost finished."* (~25% cut to the beat.)
11. **Transportees coda.** End the beat at "you can guess where it falls hardest." Cut "is a
    question the next part will have to face" — Part 7's owned-people beat detonates unannounced.
12. **"Thirty-two centuries"** → *"more than three thousand years"* (the walk-back is ~31
    centuries; don't overshoot).
13. **Told-importance.** "Now, here is the part that matters for everything that follows. The
    system *absorbed* it." → delete the announcement; lead with *"The system absorbed it."*
14. **Series-ref budget check:** after edits, P6's one reference is the L32 saving-device. Verify.

---

## Part 7 — Collapse (`Part-7-Collapse/`)

1. **Sea Peoples attribution (contradicts P6's own correction; two sites).** L74 "Ramses III fought
   off what his inscriptions call the Sea Peoples invasion" → *"what we now call the Sea Peoples
   invasion"*. L46 the companion phrase → *"the inscription from which modern scholars drew the
   name"*. The term stays modern everywhere; P6 teaches exactly that.
2. **Coast-watcher number (unsourced "569").** The precise figure appears twice plus a body-beat
   ("One of those five hundred and sixty-nine names"). The o-ka tablets' commonly cited total is
   ~800 and they name officers, not every man. Recast to the defensible shape: *"hundreds of men,
   counted by unit, the officers named"* — and the body-beat becomes *"One of those men"*. Do not
   assert any specific total.
3. **Em-dash trick + triple silence.** "the way a sentence stops when the speaker—" is typographic;
   it doesn't exist on audio. Replace with the speakable version: *"the way a sentence stops when
   the speaker stops mid-word."* Then trim the paragraph's three statements of unknowability to one.
4. **Series self-praise (zero tolerance).** Cut both sentences: "This series has been telling you
   since the first hour that the gaps and corrections are part of the story. Here is the practice
   of that, at the worst..." The paragraph ends on "nameless." — which is the stronger ending.
5. **Triple-tell pivot.** "Here is what did not get corrected. Hold on to this, because it's the
   part that matters." → delete both sentences. The next line — "The letter is real." — IS the
   pivot, and lands harder bare.
6. **L56.** "Every fact you have heard in this series about the rations..." → delete "in this
   series" (the sourcing-transparency work survives).
7. **L48.** "what scribes in this series have done since the first tablets in Sumer" → *"what
   scribes had done since the first tablets in Sumer"*.
8. **L68.** "the divine households this series walked you through in Uruk" → *"the divine
   households we walked through in Uruk"*.
9. **L146.** "The silence is total, and it is not the kind of silence this series gets to fill." →
   *"...and it is not a silence anyone gets to fill."* **KEEP L148** ("If this series has a debt it
   cannot pay, it is this one.") verbatim — it is the part's one allowed reference and it's earned.
10. **Emar/Carchemish seam.** "Emar leaves us something rarer than arrowheads, though, before it
    goes" reaches back across the ~250-word Carchemish paragraph; on audio the antecedent is lost.
    Lowest-risk fix (preferred): re-anchor the transition explicitly — *"Back at Emar — before the
    city goes — the scribes leave us something rarer than arrowheads."* (Alternative, only if the
    seam still reads broken: move the year-of-distress material to directly follow Emar's
    introduction and let Carchemish trail as the exception.)
11. **Hattusa-inside dedup.** L68 re-walks L66's evacuation (seals/gods taken; destination never
    found stated twice more). Cut L68 to ~250 words: keep "You do not leave the gods" and "The
    state took its future and abandoned its memory"; the unknown destination is stated once, in
    closing position.
12. **`[PILOT-NEW-PROSE]` Empty-harbor disambiguation (2–3 sentences).** The 1180 BCE coastal
    snapshot reads as Ugarit, but Ugarit burned five years earlier in this same part. Add a beat
    near the snapshot's top making the non-identity the point. Shape: *"This is not Ugarit — Ugarit
    is ash five years now. This is a harbor the fires missed. The silence reached it anyway."*
13. **Iron chord trim (contract: P8 owns the iron beat).** In the new smith beat, drop the hillside
    specifics ("dug from hillsides a day's walk from home — no fleet, no treaty..."). Keep the
    forward lean: *"That story belongs to the next part. The crucible of scrap is where it starts."*
    (P8's hillside image then lands fresh.)
14. **Imperative beat-openers → start in scene.** "Put one body on that shoreline." / "Slow down
    inside that." / "Here is the question that matters..." — cut the imperative frames; open each
    beat inside the scene or the fact it announces.
15. **Dockworker callback sanity check (after P5's re-date).** With the snapshot at ~1230, the man
    at the 1185 destruction would be very old. If the callback text asserts he personally watched
    the burning, soften with one clause (shape: *"an old man by then, if he lived to see it"*) and
    flag `[PILOT-NEW-PROSE]`-adjacent for review; if it only invokes "his harbor," leave it.

---

## Part 8 — Long Aftermath (`Part-8-Long-Aftermath/`)

1. **`[PILOT-NEW-PROSE]` — THE COLD-OPEN REWRITE (the most important fix in this spec).** The cold
   open describes the grandfather as a Mesopotamian cuneiform scribe; line 28 identifies him as
   "the man from the archive room — the administrator we watched at Pylos." Pylos wrote **Linear B**.
   Rewrite the scribal details to match the planted root. The facts (digest-verified):
   - Linear B: ~87 syllabic signs plus ideograms — not "hundreds of signs," and not cuneiform.
   - Medium: palm-sized clay tablets, day-records — figs, bronze, linen, rations, rowers.
   - **No literature**: Linear B preserves zero hymns, prayers, or stories — administration only.
     (If the current text has him learning hymns or classics, that goes.)
   - Training: palace scribal apprenticeship — NOT the Mesopotamian edubba; the "homework and
     beatings" color belongs to the edubba texts and must come out.
   - Keep: the emotional architecture (a literate man; a grandson who will never learn; the skill
     dying in one lifetime) — every beat of that survives, re-grounded in Linear B reality.
   This will run 150–300 words of rewritten prose. Match the Voice Bible. Flag prominently for
   Fable review.
2. **L34.** Cut both sentences: "the aftermath contains something the whole series has been building
   toward. Something counterintuitive, and worth taking seriously." The Lefkandi/highlands material
   earns attention without a trailer.
3. **Production-notes leak.** "a line you'll find in this series' own earlier notes and in plenty of
   modern books" → attribute only to *"plenty of modern books"*. (The self-correction beat itself —
   polis-as-response-to-palace being a modern reading — stays intact.)
4. **L175.** "it is the question the whole series..." → recast without the series-as-subject (e.g.,
   *"it is the question everything since the first storehouse has been asking"* — vary to fit).
5. **L179 closing self-billing.** "That's the last part. It's the best one." → cut "It's the best
   one." End on *"That's the last part."* — the withholding does the selling.
6. **Highlands snapshot unplanted callbacks.** "smaller than the palace weaver's room in Mycenae" →
   *"smaller than the weaving women's quarters at Pylos"* (that's the rendered plant). "smaller than
   the barge-puller's tenement in Uruk" → generalize (*"smaller than the rooms the barge-pullers
   slept in at Uruk"*) — the tenement was never rendered.
7. **Iron "one sentence" promise.** P8:125 announces "One sentence, and we..." then runs a
   paragraph. Cut the announcement; keep the paragraph (with P7's hillside now trimmed, P8's
   "iron needs a hillside, and the hillsides were everywhere" is the sole, fresh instance).
8. **Series-ref budget:** P8 currently carries six — worst in the series. After items 2–5, verify
   ≤1 navigational reference remains.

---

## Part 9 — Inheritance & Memory (`Part-9-Inheritance-Memory/`)

1. **Ventris contradiction.** "what he found was Greek. Not archaic Greek. Not proto-Greek." is
   contradicted two sentences later by Ventris's own quoted "a difficult and archaic Greek."
   Rewrite so the surprise is that it was Greek *at all*: shape — *"what he found was Greek — not a
   cousin of Greek, not some lost language wearing Greek's clothes: Greek, five centuries before
   Homer."* The quote then lands in agreement.
2. **Roll-call kiln revival.** "The scribe in Ugarit, pressing his warning into clay while the city
   burned around him." revives the exact legend P7's cold open spends ~500 words retiring. Recast
   to the corrected reality P7 built: *"The scribe in Ugarit, filing the king's plea in perfect
   diplomatic form while the world it was addressed to stopped existing."*
3. **Hattusa tablet count.** P6 promises "tens of thousands"; P9 delivers "ten thousand." Reconcile
   in P9: *"ten thousand clay tablets in the first seasons alone — the first of the tens of
   thousands we now hold."*
4. **Throughline jargon leak.** "That is the literacy-as-losable lesson of this entire series, paid
   forward." → cut the sentence; the adjacent "Writing survives when something keeps it readable"
   already does the work.
5. **L160.** "But in the way that matters for the purposes of this series:" → *"But in the way that
   matters:"*.
6. **P9:16 superlative self-billing** ("one of the most important and least...") → recast without
   the self-rating; state what the thing is and let it be important.
7. **DO NOT TOUCH:** P9:48 "The Hittite language is Indo-European." — the thunderclap now lands
   clean because P3/P4 stripped the label. P9:108's one-line internal chord also stands.
8. **Second kiln-adjacent image (clay coda, ~L124).** "A scribe at Ugarit, pressing a warning into
   riverbank mud, wrote on something that could survive the end of his world." Softer than the
   roll-call instance but uses the same retired vocabulary: P7 establishes the letter as a *plea*
   (probably a file copy of one dispatched), not a warning pressed in extremis. Align: *"A scribe
   at Ugarit, filing a plea for help in riverbank mud, wrote on something that could survive the
   end of his world."* The point of the sentence (medium outlives world) is untouched.

---

## After all seven parts pass verification

1. **Audiobook reassembly.** Regenerate `BZ-Age-draft03-audiobook.md`'s successor as
   `BZ-Age-draft04-audiobook.md` (do not overwrite the draft-03 assembly): same assembly pattern —
   prologue + Parts 1–9 in order, prose sections only (strip headers, revision notes, and editorial
   apparatus), part-title separators between parts. Source each part from `draft-04.md`
   (all ten should exist by then; error out loudly if any is missing rather than falling back).
2. **Revision-Log v1.3 entry** in `04-Working-Notes/Revision-Log.md`: date, scope (draft-04 P3–P9
   per this spec), the four `[PILOT-NEW-PROSE]` items flagged for Fable review, per-part word
   counts, and any `[FLAGGED, NOT FIXED]` items collected along the way.
3. **Report back** with: per-part grep results, the diff summaries, and the flagged-items list.
   Fable reviews the four new-prose sites plus a sample of the mechanical edits (decision D-003).

## Part 2 residuals (one small check, not a full pass)

Part 2 draft-04 is done, but verify one fleet item that may have been missed: the sentence "The
tablets record people dedicated to the temple, people handed over to settle debts, people captured
in raids on other cities and put to work." asserts three ownership routes unverified for the
earliest period. If still present verbatim, loosen the period claim (shape: *"The early tablets
record..."* → *"The records of these early centuries come to include..."*) or flag it. Also grep P2
for "Think about what that says" (instruction-to-listener) — if present, declarativize.
