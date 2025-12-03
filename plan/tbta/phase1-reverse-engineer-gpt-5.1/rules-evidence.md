# TBTA Phase1 Verse Rules — Evidence by Rule

> Evidence strings under each rule in `RULES.md` are summarized and explained here. All examples are based on existing TBTA samples (especially in Ruth 1–2 and Genesis 22) plus internal knowledge of NIV and common translation patterns. They are hypotheses to be confirmed against the full TBTA corpus.

---

## 1. Coreference Resolution

- **References**: Ruth 1:3, Ruth 1:2, Jonah 1:3, Mark 4:38, Acts 9:1; NOT (no clear exceptions yet; see notes)
- **Pattern**:
  - Narrative verses like **Ruth 1:2–3** and **Jonah 1:3** are rich in 3rd person pronouns (`he`, `she`, `they`), which TBTA systematically replaces with explicit NPs (e.g., "Naomi", "that man, his wife, and his 2 sons", "Jonah").
  - Dialogue and miracle narratives such as **Mark 4:38** and conversion scenes like **Acts 9:1** similarly require repeated explicit reference to participants instead of stacked pronouns.
- **Notes**:
  - In all inspected and mentally simulated cases, 3rd person pronouns are fully resolved; apparent “exceptions” tend to be 1st/2nd person (handled by Deixis Marking) rather than violations of this rule.

---

## 2. Clause Segmentation

- **References**: Ruth 1:2, Ruth 1:3, Gen 22:2, Acts 1:8, Matt 28:19; NOT Matt 6:9–10
- **Pattern**:
  - **Ruth 1:2–3** (see `examples.md` and `TEST-RESULTS.md`) clearly show long NIV sentences being split into multiple TBTA sentences, each with a single main predicate.
  - **Genesis 22:2** ("Take your son ... and go...") is naturally split into a sequence of short imperatives.
  - Mission texts like **Acts 1:8** and **Matt 28:19** contain coordination (“receive power and be my witnesses”, “go and make disciples”) that TBTA treats as separate clauses or sentences.
- **Notes**:
  - The Lord’s Prayer (**Matt 6:9–10**) is a plausible edge case where idiomatic parallel petitions might occasionally be grouped more tightly; segmentation can be slightly looser for highly formulaic prayers.

---

## 3. Explicit Relativization

- **References**: Ruth 1:3, Ruth 2:1, Ruth 1:2, Gen 22:2, Acts 9:11; NOT 2 Sam 5:3
- **Pattern**:
  - **Ruth 1:3**: “Elimelek, Naomi’s husband” becomes `Elimelech [who was Naomi's husband]`.
  - **Ruth 1:2**: “Ephrathites from Bethlehem, Judah” is unpacked into `Ephrah's family/clan` plus `[which was in Judah]`.
  - **Ruth 2:1** and **Acts 9:11** similarly turn appositions ("relative", "street called Straight") into explicit relative clauses.
  - **Genesis 22:2** expands “your only son, whom you love—Isaac” into layered relatives `[who is your only son] [whom you love]` plus a naming sentence.
- **Notes**:
  - Royal or covenantal titles such as **2 Sam 5:3** (“King David made a covenant...”) may occasionally keep a bare apposition for brevity, but TBTA usually prefers the explicit `[who was the king]` style when it matters for participant tracking.

---

## 4. Deixis Marking

- **References**: Ruth 1:16, Ruth 2:4, Gen 22:2, Matt 6:9–10, Philem 1:4–5; NOT 2 John 1:5
- **Pattern**:
  - **Ruth 1:16** (classic loyalty speech) is full of 1st/2nd person pronouns that TBTA marks as `I(Ruth)`, `you(Naomi)`, `your(Naomi's)`, clarifying speaker/addressee throughout the quote.
  - **Ruth 2:4** uses `I(Boaz)` and `you(workers)` to disambiguate greetings and blessings.
  - **Gen 22:2** relies on consistent marking of `you(Abraham)` and `your(Abraham's)` to keep commands clear.
  - Prayers and epistolary formulas in **Matt 6:9–10** and **Philem 1:4–5** are especially sensitive to who is speaking to whom, which TBTA handles via systematic deixis marking.
- **Notes**:
  - Very short address formulas like **2 John 1:5** ("Dear lady") may not always repeat full deictic markers on every pronoun; the core rule still holds for longer discourse segments.

---

## 5. LDV Substitution (Longman Defining Vocabulary)

- **References**: Ruth 2:1, Ruth 2:4, Matt 4:10, Acts 27:23, Titus 2:11–14; NOT (optional cases like Ruth 2:9)
- **Pattern**:
  - **Ruth 2:1**: “clan of Elimelek” → `family/clan`; “man of standing” → simple high-respect wording; implicit wealth marked via `(implicit-info)`.
  - **Ruth 2:4**: “harvesters” → `servants/workers`; “The LORD be with you” → prayer paraphrase with simple verbs.
  - Worship language in **Matt 4:10** and **Acts 27:23** naturally triggers `serve/worship` pairings.
  - Dense theological vocabulary in **Titus 2:11–14** (grace, salvation, redemption) is paraphrased into simpler LDV-compatible wording.
- **Notes**:
  - Some simple L0–L1 words like “grain” or “family” in verses such as **Ruth 2:9** may not require explicit pairings every time; pairing is driven by difficulty, not rigidly applied to every occurrence.

---

## 6. Subordinate Bracketing

- **References**: Ruth 1:2, Ruth 1:3, Gen 22:2, Ruth 2:4, Acts 1:8; NOT Matt 5:3
- **Pattern**:
  - **Ruth 1:2–3**: location and appositive details are consistently put in brackets: `Bethlehem [which was in Judah]`, `Elimelech [who was Naomi's husband]`.
  - **Gen 22:2**: multiple subordinates are bracketed: `[who is your only son]`, `[whom you love]`, `[in order to sacrifice him there]`.
  - **Ruth 2:4**: prayer clauses are bracketed as patient clauses of “pray”.
  - **Acts 1:8**: the condition is bracketed (`[when the Holy Spirit comes on you]`) distinct from the main future actions.
- **Notes**:
  - Compact beatitudes like **Matt 5:3** may be written in a flatter structure, where the “for” clause feels more like a parallel assertion than a clearly subordinate bracketed clause; TBTA can tolerate slightly looser bracketing in poetic lines.

---

## 7. Quote Framing

- **References**: Ruth 1:16, Gen 22:2, Ruth 2:4, Jonah 1:2, Acts 16:31; NOT Titus 1:4
- **Pattern**:
  - **Ruth 1:16** opens with a clear frame (“But Ruth replied”) followed by a multi-sentence quote that TBTA formats as `Ruth said to Naomi, ["First sentence]. Second sentence..."`.
  - **Gen 22:2** uses `God said, ["You(Abraham) (imp) take..."]`.
  - **Ruth 2:4** and **Jonah 1:2** exemplify greetings and commands introduced with `X said` / `the word of Yahweh came`, then bracketed quoted material.
  - Evangelistic speech in **Acts 16:31** fits the same pattern: `They said, ["Believe in the Lord Jesus..."]`.
- **Notes**:
  - Short epistolary greetings like **Titus 1:4** (“Grace and peace...”) sometimes appear without a full `X said` frame in natural English; TBTA still normalizes most narrative and dialogue quotes to the explicit pattern.

---

## 8. Imperative Marking

- **References**: Gen 22:2, Ruth 1:8, Josh 1:9, Matt 28:19, Acts 2:38; NOT Philem 1:8–10
- **Pattern**:
  - Commands in **Gen 22:2** and **Ruth 1:8** (“Go back, my daughters”) become `You(Abraham) (imp) take...` and `You(daughters-in-law) (imp) return...`.
  - Commissioning texts such as **Josh 1:9** and **Matt 28:19** are prototypical multi-clause imperatives that TBTA expresses via repeated `(imp)` markers.
  - **Acts 2:38** (“Repent and be baptized...”) naturally maps to `You(people) (imp) repent...`.
- **Notes**:
  - Persuasive appeals in **Philem 1:8–10** (“I could be bold and order you ..., yet I prefer to appeal to you”) represent edge cases where the strict `(imp)` marking may soften into more natural polite language while still being functionally imperative.

---

## 9. Hyphenated Verbs

- **References**: Jonah 1:3 (run away), Ruth 3:3, Mark 2:14, Acts 9:6; NOT Jonah 1:10
- **Pattern**:
  - **Jonah 1:3** (NIV “Jonah ran away from the LORD”) is archetypal for TBTA’s `run-away` base-form pattern, regardless of tense.
  - Movement and posture verbs in narrative commands (e.g., **Ruth 3:3**, **Mark 2:14**, **Acts 9:6**) map naturally to `go-down`, `stand-up`, `follow-me` style hyphenated bases.
- **Notes**:
  - Some narrative descriptions such as **Jonah 1:10** may occasionally be rendered with a simple past (“ran away”) in draft form; the rule still insists that finalized TBTA output normalize these to hyphenated base forms with separate tense/aspect marking if needed.

---

## 10. Modal Decomposition

- **References**: Matt 6:24, Acts 4:20, Titus 1:11, 2 John 1:7, Jonah 4:2; NOT (rare stylized uses like Matt 5:14–16)
- **Pattern**:
  - Ability statements in **Matt 6:24** (“cannot serve both God and money”) become `is not able [to serve both God and money]`.
  - In **Acts 4:20**, “we cannot help speaking” is decomposed to `we(Peter and John) _excl are not able [to stop speaking]`.
  - Obligation in **Titus 1:11** (“they must be silenced”) is rephrased as `people have to [stop them from speaking]`.
  - Emotionally loaded complaints and prayers (e.g., **Jonah 4:2**) also benefit from decomposed modals (`I(Jonah) was not able [to accept this]`, etc.).
- **Notes**:
  - Highly stylized light/metaphor passages in **Matt 5:14–16** (“cannot be hidden”) might keep a more idiomatic feel; even there, the underlying pattern is still “is not able [to be hidden]”.

---

## 11. Demonym → Description

- **References**: Ruth 1:2, Ruth 1:4, Esther 2:5, Acts 2:5–11, Nahum 1:1; NOT (title-like uses such as Nahum 1:1)
- **Pattern**:
  - **Ruth 1:4** (“Moabite women”) → `women [who were from Moab]`.
  - **Ruth 1:2** (“Ephrathites from Bethlehem, Judah”) → `people [who were in Ephrah's family/clan]` plus `[which was in Judah]`.
  - **Esther 2:5** and **Acts 2:5–11** contain classic demonyms (e.g., “a Jew of the tribe of Benjamin”, “Parthians, Medes...”) that TBTA systematically unpacks into origin/family clauses.
- **Notes**:
  - Superscription-style labels like **Nahum 1:1** (“an oracle concerning Nineveh. The book of the vision of Nahum the Elkoshite.”) may occasionally keep a bare demonym as a quasi-title; the rule is aimed primarily at in-verse participant descriptions.

---

## 12. Gap-filling (Implicit Information)

- **References**: Ruth 1:1–2, Ruth 2:1, Ruth 2:4, Acts 9:1–2, Neh 8:8; NOT (simple one-clause statements with no missing cultural steps)
- **Pattern**:
  - **Ruth 1:1–2**: TBTA adds background like “When judges were ruling Israel” and explicit famine context with `(implicit-info)` markers.
  - **Ruth 2:1**: Adds `(implicit-info)` about Boaz’s wealth and location beyond the bare NIV text.
  - **Ruth 2:4**: Blessing formulas (“The LORD be with you”) are treated as prayers (`I pray [that Yahweh will be with you]`), making implicit speech-act force explicit.
  - Persecution and mission contexts like **Acts 9:1–2** and explanatory reading scenes like **Neh 8:8** naturally encourage explicit bridging actions and background (`(implicit-background)`, `(implicit-subaction)`).
- **Notes**:
  - Many simple narrative clauses (e.g., “John went home”) do not need any gap-filling; the rule is applied where cultural, theological, or discourse-critical steps would otherwise be hidden from a literal reader or machine translator.


