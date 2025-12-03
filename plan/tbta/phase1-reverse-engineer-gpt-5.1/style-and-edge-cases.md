# TBTA Phase1 Styles and Edge Cases (He1 vs He2)

> This file captures style differences between He1 and He2 usage, plus key edge-case patterns and mental validation scenarios for the 12 compressed TBTA Verse rules.

---

## 1. He1 vs He2 Styles

### He1 (Phase 1 — “Natural but Marked”)

- **Representative books**: Ruth, Genesis, Jonah (with spillover into other narrative books).
- **Characteristics**:
  - Allows **“that”** in patient clauses more freely: `know [that Ruth is good]`.
  - Bracketing is **present but slightly looser** in simple cases.
  - Fewer underscore markers (`_implicit`, `_paragraph`, etc.).
  - Prioritizes **natural English flow** while still enforcing core rules (no 3rd person pronouns, basic clause segmentation, explicit relativization).

### He2 (Phase 2 — “Strict Notational”)

- **Representative books**: Matthew (especially later chapters), Mark, Acts (in many sections), and some epistolary material (Titus, 2 John).
- **Characteristics**:
  - Strong pressure to **omit “that”** in patient clauses: `knew [Mary was there]` instead of `knew [that Mary was there]`.
  - Bracketing is **comprehensive and nested**, especially in teaching sections and complex discourse.
  - Heavy use of underscore markers (e.g., `_implicitActiveAgent`, `_paragraph`, `_excl/_incl`, `_frameInferable`).
  - Prioritizes **formal, machine-readable structure** even at the cost of slightly stiffer English.

### Style Continuum

- He1 and He2 are best understood as **ends of a continuum**, not hard categories:
  - Ruth and Genesis lean clearly He1 but still utilize most notation patterns.
  - Matthew shows mixed behaviour: more He2 in the teaching blocks (Sermon on the Mount, parables), more He1 in some narrative transitions.
  - Acts is often very close to He2, especially where discourse structure is dense (sermons, trials).

---

## 2. Rule-Level Style Nuances

### Coreference Resolution & Clause Segmentation (Rules 1–2)

- **Both He1 and He2** apply these aggressively:
  - In all styles, narrative and didactic texts avoid 3rd person pronouns and long, tangled sentences.
  - Differences are mainly in how **finely** clauses are split:
    - He1 may occasionally keep mild coordination (“X went and saw Y”) if both verbs share the same simple subject.
    - He2 prefers a **single predicate per sentence** approach almost everywhere.

### Explicit Relativization & Subordinate Bracketing (Rules 3 & 6)

- **He1**:
  - Likely to relativize appositions that affect participant tracking (e.g., “Naomi’s husband”, “from Moab”) but may leave some short location phrases as simple PPs when unambiguous.
  - Bracketing is consistent for complex or ambiguous clauses, but trivial subordinate relations (e.g., very short time phrases) may be left linear.
- **He2**:
  - Strong tendency to **convert all appositions** into `[who/that/which]` relatives.
  - **All** subordinate clauses (relative, causal, conditional, temporal) are expected to be enclosed in `[...]`, even if short or idiomatic.

### Deixis & Imperatives (Rules 4 & 8)

- **He1**:
  - Deixis marking for 1st/2nd person is present but occasionally lighter in obvious contexts (e.g., when the same speaker dominates a long paragraph).
  - Imperatives may sometimes be realized as natural English commands without explicit `(imp)` after every verb, especially in short exchanges.
- **He2**:
  - Near-blanket enforcement of `I(X)`, `you(Y)`, `my(Z's)`, plus `_incl/_excl` for `we/us`.
  - Imperative marking is treated almost like a **syntactic label**, especially in teaching and command-heavy passages (Matt 5–7; 28:18–20; Acts 2:38).

### LDV Substitution & Demonyms (Rules 5 & 11)

- **LDV Substitution**:
  - He1 tends to substitute where **comprehension** is clearly at risk (idioms, rare terms) but may tolerate some higher-level vocabulary if context is simple.
  - He2 is much more **systematic**, pairing or explicating almost every L2/L3 word, especially in doctrinal or dense theological material (Titus).
- **Demonyms → Descriptions**:
  - In He1, demonyms that drive narrative identity (e.g., "Moabite" in Ruth) are consistently unpacked.
  - He2 extends this pattern even to compact superscriptions and title-like phrases where possible, although a few heading lines may still keep demonyms as quasi-titles.

### Hyphenated Verbs & Modals (Rules 9 & 10)

- Hyphenated movement/posture verbs (`run-away`, `stand-up`, `sit-down`) are **expected** in both styles, but:
  - He1 may tolerate the occasional simple-past form in narrative if the tense is clear from context.
  - He2 prefers strict base-form hyphenation with separate aspect/tense marking when needed.
- Modal decomposition is more rigid in He2:
  - He1 might leave an occasional “can” or “must” in very short or familiar phrases.
  - He2 consistently decomposes them into `is able [to ...]` / `has to [ ... ]`.

### Gap-filling (Rule 12)

- **He1**:
  - Uses `(implicit-info)` and related markers sparingly, usually to fill key cultural or situational gaps (e.g., who judges are, why famine matters).
  - Reads more like a **good explanatory translation** for humans.
- **He2**:
  - Treats implicit markers as an explicit **semantic layer**, often breaking out subactions and background that would otherwise remain implicit.
  - Optimized for machine translation and automatic reasoning about events.

---

## 3. Edge-Case Patterns by Genre

### Genealogies & Lists

- Long genealogies (e.g., in Genesis, 1–2 Samuel) and name lists:
  - **Coreference Resolution** and **Demonym → Description** still apply, but:
    - Clause segmentation may allow slightly **longer list-style sentences** for readability.
    - LDV substitution focuses on relational terms (“son of”, “in family/clan”) rather than every lexical item.

### Beatitudes and Poetic Lines (e.g., Matt 5)

- Parallel structures (“Blessed are X, for Y”) behave more like poetic lines than prose:
  - Bracketing of “for”-clauses can be slightly looser, especially in He1.
  - Modal decomposition and LDV substitution should still occur, but the overall line shape is often preserved to maintain rhythm.

### Rhetorical Questions & Parables

- Rhetorical questions (e.g., Romans 8 in examples, or Jesus’ questions in Matthew/Mark):
  - Often get both a **question version** and a **(statement)** paraphrase in TBTA to support logic-based reasoning.
  - Deixis and modal decomposition are crucial; clause segmentation may keep a tighter connection between the rhetorical question and its paraphrase.
- Parables:
  - Strong emphasis on **participant tracking** (Coreference Resolution, Demonym → Description) and **Bracketed Subordinates**.
  - He2 will often treat nested speech and explanatory asides with especially careful bracketing and quote framing.

### Prayers, Blessings, and Epistolary Openings

- Prayers and blessings (Ruth 2, Jonah 2, Matt 6, epistolary greetings):
  - Use a **pray/hope** paraphrase pattern (`I(X) pray [that Yahweh will ...]`).
  - Deixis and LDV substitution are heavily used; clause segmentation may keep tightly related clauses together when they form a single speech act.

---

## 4. Mental Validation Scenarios (Summary)

To sanity-check the 12 rules plus the RULES+SKILL process without external data, a series of “mental held-out” scenarios were considered:

- **Complex narrative scene** (e.g., David and Goliath in 1 Sam 17):
  - Rules 1–3 and 6–8 successfully predict a TBTA-style output that keeps participants clear and clauses short, but over-aggressive splitting can risk choppy flow if not balanced by He1-style smoothing.
- **Dense teaching block** (e.g., Sermon on the Mount in Matt 5–7):
  - He2-style application of bracketing, modals, and imperatives creates a very structured but sometimes stiff output; the rules appear sufficient but must be applied with attention to poetic parallelism.
- **Doctrinal summary** (e.g., Titus 2:11–14):
  - LDV substitution and modal decomposition are central; mental application of the rules suggests TBTA will heavily paraphrase key terms while preserving the logical skeleton.
- **Short epistle** (Philemon, 2 John):
  - Highlights tension between strict imperative marking and polite appeals; rules 4, 8, and 10 need flexibility to avoid over-marking every softened request as `(imp)`.

Overall, the mental validation suggests:

- The **12-rule compressed set is sufficient** to recreate the major TBTA behaviours observed in Ruth/Genesis/Matthew/Acts.
- The largest risks are:
  - **Over-application** of segmentation and bracketing in poetic/parallel material.
  - **Overly strict** modal decomposition and imperative marking in polite or rhetorical contexts.

These risks are flagged here so future corpus-based refinement can tune the balance between He1 naturalness and He2 strictness without changing the core rule set.


