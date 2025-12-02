# TBTA Verse Column Reverse Engineering - Master Plan

> **Goal**: Reproduce TBTA's "Verse" column transformation from NIV to Controlled Natural Language (CNL)
> **Scope**: Genesis, Joshua, Ruth, 1-2 Samuel, Nehemiah, Esther, Daniel, Jonah, Nahum, Matthew, Mark, Acts, Titus, Philemon, 2 John

## Project Summary

TBTA creates a **language-neutral intermediary representation** that any language can generate from. This removes English idioms, implicit cultural assumptions, and ambiguous references.

**Data Source**: https://github.com/AllTheWord/tbta_db_export/blob/main/csv/Bible/

---

## Source Strategy

**Base**: Copy NIV text, **EXCEPT**:
- Pronouns → resolve to explicit nouns
- Compound sentences → segment (one predicate each)
- Idioms → decompose to explicit meaning
- Passives → convert to active where possible
- L2+ vocabulary → apply LDV substitution

**INCORPORATE FROM**:
- **Hebrew**: "Yahweh" for יהוה (NIV uses "LORD")
- **Greek/Hebrew**: Implicit cultural context via `(implicit-info)`
- **Scholarly sources**: Historical footnotes via `(footnote)`
- **Semantic analysis**: Clause boundaries, participant tracking

---

## Two Formats: He1 vs He2

| Feature | He1 (Phase 1) | He2 (Phase 2) |
|---------|---------------|---------------|
| Books | Ruth, Jonah, Genesis, most OT | Matthew (partial), some NT |
| "that" in patient clauses | Allowed for natural flow | Must omit |
| Brackets | Less strict | Required everywhere |
| Underscore markers | Fewer | Many (`_implicit`, `_implicitActiveAgent`) |
| Natural flow | Prioritized | Precise notation |

---

## Core Rules (12 total)

### 1. Coreference Resolution
Replace 3rd-person pronouns (he/she/it/they) with explicit referents.

```
he/she/it/they → [Name] or [that + noun]
```

**Supports**: Ruth 1:3, Ruth 1:4, Ruth 1:5, Jonah 1:3, Gen 1:28
**Contradicts**: [NEED TO VERIFY - search for any remaining pronouns]

---

### 2. Clause Segmentation
One predicate per sentence. Split at conjunctions.

```
"X and Y did Z" → "X did A. Y did B."
```

**Supports**: Ruth 1:1, Ruth 1:2, Gen 1:4, Gen 1:5, Jonah 1:3
**Contradicts**: [NEED TO VERIFY - search for compound predicates]

---

### 3. Explicit Relativization
Appositive → bracketed relative clause.

```
"X, the king" → "X, [who was the king]"
"Bethlehem in Judah" → "Bethlehem, [which was in Judah]"
```

**Supports**: Ruth 1:1, Ruth 1:2, Ruth 1:3, Ruth 2:1, Jonah 1:1
**Contradicts**: [NEED TO VERIFY]

---

### 4. Deixis Marking
Mark 1st/2nd person referents in parentheses.

```
I(Speaker), you(Addressee), my(Possessor's), we(Group) _incl/_excl
```

**Supports**: Ruth 1:8, Ruth 1:11, Ruth 1:16, Jonah 1:2, Ruth 2:2
**Contradicts**: [NEED TO VERIFY - any unmarked 1st/2nd person]

---

### 5. LDV Substitution (Longman Defining Vocabulary)

| Level | Color | Action |
|-------|-------|--------|
| L0-L1 | Blue/Cream | Use directly |
| L2 | Magenta | Pair: `simple/complex` |
| L3 | Green | Alternate: `(complex)...(simple)...` |
| L4 | Brown | Proper nouns, use directly |

**Common L2 pairings**: `family/clan`, `grain/barley`, `gather/harvest`, `buy/redeem`, `master/lord`, `wine/vinegar`

**Supports**: Ruth 1:2, Ruth 2:2, Ruth 2:3, Ruth 2:14, Ruth 4:1
**Contradicts**: [NEED TO VERIFY - unpaired L2 words]

---

### 6. Subordinate Bracketing
All non-main clauses in `[...]`:
- Relative: `[who/that/which...]`
- Patient: `knew [X happened]` (He1 allows `[that X...]`)
- Purpose: `[in order to...]`
- Conditional: `[if X then...]`

**Supports**: Ruth 1:1, Ruth 1:7, Ruth 1:16, Jonah 1:2, Gen 1:2
**Contradicts**: [NEED TO VERIFY]

---

### 7. Quote Framing
```
Speaker said, ["First sentence]. Continuation."
```
Nested: `["X said, ["inner quote"]"]`

**Supports**: Ruth 1:8, Ruth 1:11, Ruth 1:16, Jonah 1:2, Ruth 2:2
**Contradicts**: [NEED TO VERIFY - quotes without speaker intro]

---

### 8. Imperative Marking
```
You(Addressee) (imp) verb...
```

**Supports**: Ruth 1:8, Ruth 1:11, Ruth 1:15, Jonah 1:2, Ruth 2:8
**Contradicts**: [NEED TO VERIFY - imperatives without (imp)]

---

### 9. Hyphenated Verbs
Never inflect. Base form only.

```
run-away, sit-down, stand-up, go-up, pick-up (NOT ran-away, sat-down)
```

**Supports**: Jonah 1:1, Jonah 1:3, Matt 5:1
**Contradicts**: [NEED TO VERIFY - any inflected hyphenated verbs]

---

### 10. Modal Decomposition
```
"can X" → "is able [to X]"
"must X" → "has to [X]" / obligation marker
```

**Supports**: Ruth 1:11, Ruth 1:12, Ruth 4:6
**Contradicts**: [NEED TO VERIFY - any "can" remaining]

---

### 11. Demonym → Description
```
"Moabite" → "[who was from Moab]"
"Ephrathite" → "[who was in Ephrah's family/clan]"
```

**Supports**: Ruth 1:4, Ruth 2:2, Ruth 2:21, Ruth 4:10
**Contradicts**: [NEED TO VERIFY]

---

### 12. Implicit Information
Add missing subactions, cultural context:

```
(implicit-info) Boaz walked to Ruth.
(footnote) At that time, judges ruled Israel.
```

Types: `(implicit-situational)`, `(implicit-background)`, `(implicit-subaction)`

**Supports**: Ruth 2:1, Ruth 2:7, Ruth 2:8, Ruth 3:7, Ruth 4:7
**Contradicts**: [NEED TO VERIFY]

---

## Special Notation

### Numbers
- **Digits** for quantities: `13 kilograms`, `10 old men`, `2 people`
- **Words** for: ordinals (`first day`), "one of" (`one of the men`), scene markers (`One day...`)

**Supports digits**: Ruth 2:17, Ruth 4:2, Ruth 4:4, Gen 1:28
**Supports words**: Ruth 1:2, Ruth 2:2, Ruth 3:1, Gen 1:5
**Inconsistencies**: Ruth 1:3 ("two sons"), Ruth 1:4 ("ten years")

---

### Divine Names
- Standard: "Yahweh" (from Hebrew יהוה)
- NIV's "LORD" → "Yahweh"
- Prayer pattern: `I(X) pray [that Yahweh will...]`

**Supports**: Ruth 1:8, Ruth 1:17, Ruth 2:4, Ruth 2:12, Jonah 1:2

---

### Titles and Sections
```
(title) Section heading here.
(paragraph) for paragraph breaks.
_paragraph in He2
```

**Supports**: Ruth 2:1, Matt 2:1, Matt 5:1, Jonah 1:1

---

### Advanced Markers (He2 primarily)

| Marker | Use | Example |
|--------|-----|---------|
| `_implicit` | Mark implicit word/phrase | `God _implicit` |
| `_implicitNecessary` | Grammatically required implicit | `said _implicitNecessary` |
| `_implicitActiveAgent` | Passive agent | `by God _implicitActiveAgent` |
| `_paragraph` | Paragraph break | `_paragraph` |
| `_descriptive` | Descriptive relative clause | `[_descriptive who was tall]` |
| `_frameInferable` | Inferable from context | `the king _frameInferable` |
| `_excl` / `_incl` | Exclusive/inclusive we | `we(Paul) _excl` |

**Found in Matthew**: 881x `_implicit`, 412x `_paragraph`, 253x `_implicitActiveAgent`

---

## Terminology Index

| Term | Meaning |
|------|---------|
| **CNL** | Controlled Natural Language |
| **LDV** | Longman Defining Vocabulary (2000 core words) |
| **Coreference** | Pronoun → explicit noun resolution |
| **Deixis** | Speaker/hearer reference marking |
| **Relativization** | Appositive → relative clause conversion |
| **L2 pairing** | simple/complex word pair for vocabulary |
| **He1/He2** | Phase 1 (natural) / Phase 2 (strict) format |

---

## Validation

### Linter Check
URL: `https://editor.tabitha.bible/check?text={urlencoded_output}`

### Compare to Reference
URL: `https://sources.tabitha.bible/Bible/{Book}/{ch}/{vs}`

### Self-Check Questions
1. Can this be translated word-for-word into any language?
2. Are all implicit cultural assumptions made explicit?
3. Would a non-English speaker understand who "he/she/they" refers to?
4. Is there exactly one action (verb) per sentence?

---

## Process (7 Steps)

```
1. COPY NIV base text
2. SEGMENT clauses (one predicate each)
3. RESOLVE coreference (pronouns → nouns)
4. RELATIVIZE appositives (→ bracketed clauses)
5. SUBSTITUTE L2/L3 vocabulary (LDV pairings)
6. MARK deixis, imperatives, quotes
7. ADD implicit context (from Greek/Hebrew/culture)
```

---

## Test Results (from Ruth analysis)

| Test | NIV Source | Accuracy |
|------|------------|----------|
| Ruth 1:3 | Narrative | 95% |
| Ruth 1:16 | Dialogue | 100% |
| Ruth 2:1 | Introduction | ~90% |

---

## TODO: Complete Reference Analysis

For each rule, need to search all 15 books for:
1. Up to 5 best supporting examples
2. Up to 3 contradicting examples (inconsistencies)

Books to analyze:
- [x] Genesis (1533 verses) - sampled
- [ ] Joshua
- [x] Ruth (85 verses) - fully analyzed
- [ ] 1 Samuel
- [ ] 2 Samuel
- [ ] Nehemiah
- [ ] Esther
- [ ] Daniel
- [x] Jonah (48 verses) - sampled
- [ ] Nahum
- [x] Matthew (1071 verses) - sampled for He2 patterns
- [ ] Mark
- [ ] Acts
- [ ] Titus
- [ ] Philemon
- [ ] 2 John

---

## Quick Reference Table

| NIV Pattern | TBTA Transform | Rule |
|-------------|----------------|------|
| "he went" | "John went" | Coreference |
| "X, the king" | "X, [who was king]" | Relativization |
| "harvest" | "gather/harvest" | LDV L2 |
| "Moabite" | "[from Moab]" | Demonym |
| "can do" | "is able [to do]" | Modal |
| "LORD" | "Yahweh" | Hebrew |
| Passive voice | Active voice | Restructure |
| "two sons" | "2 sons" | Numbers (mostly) |
| "I said" | "I(Naomi) said" | Deixis |
| Compound sentence | Split sentences | Segmentation |
