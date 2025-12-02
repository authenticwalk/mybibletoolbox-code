# TBTA Verse Rules (Compressed)

> **Goal**: NIV → Controlled Natural Language for universal translation

## Source Strategy

**Base**: Copy NIV text, **except**:
- Pronouns (resolve to nouns)
- Compound sentences (segment)
- Idioms (decompose to meaning)
- Passives (convert to active where possible)
- Complex vocabulary (apply LDV substitution)

**Incorporate from**:
- **Hebrew**: "Yahweh" for יהוה (not NIV's "LORD")
- **Greek/Hebrew**: Implicit cultural context `(implicit-info)`
- **Scholarly sources**: Historical footnotes `(footnote)`
- **Semantic analysis**: Clause boundaries, participant tracking

---

## Core Transforms (5 rules)

### 1. Coreference Resolution
Replace 3rd-person pronouns with explicit referents.
```
he/she/it/they → [Name] or [that + noun]
```

### 2. Clause Segmentation
One predicate per sentence. Split at conjunctions.
```
"X and Y did Z" → "X did A. Y did B."
```

### 3. Explicit Relativization
Appositive → bracketed relative clause.
```
"X, the king" → "X, [who was the king]"
"city in Y" → "city [which was in Y]"
```

### 4. Deixis Marking
Mark 1st/2nd person referents in parentheses.
```
I(Speaker), you(Addressee), my(Possessor's), we(Group) _incl/_excl
```

### 5. LDV Substitution (Longman Defining Vocabulary)
| Level | Color | Action |
|-------|-------|--------|
| L0-L1 | Blue/Cream | Use directly |
| L2 | Magenta | Pair: `simple/complex` |
| L3 | Green | Alternate: `(complex)...(simple)...` |
| L4 | Brown | Proper nouns, use directly |

**Common L2 pairings**: `family/clan`, `grain/barley`, `gather/harvest`, `buy/redeem`

---

## Notation Patterns (3 rules)

### 6. Subordinate Bracketing
All non-main clauses in `[...]`:
- Relative: `[who/that/which...]`
- Patient: `knew [X happened]`
- Purpose: `[in order to...]`
- Conditional: `[if X then...]`

### 7. Quote Framing
```
Speaker said, ["First sentence]. Continuation."
```
Nested: `["X said, ["inner quote"]"]`

### 8. Imperative Marking
```
You(Addressee) (imp) verb...
```

---

## Lexical Rules (3 rules)

### 9. Hyphenated Verbs
Never inflect. Base form only.
```
run-away, sit-down, stand-up (not ran-away, sat-down)
```

### 10. Modal Decomposition
```
"can X" → "is able [to X]"
"must X" → "has to [X]" / obligation marker
```

### 11. Demonym → Description
```
"Moabite" → "[who was from Moab]"
"Ephrathite" → "[who was in Ephrah's family/clan]"
```

---

## Implicit Information

### 12. Gap-filling
Add missing subactions, cultural context:
```
(implicit-info) Boaz walked to Ruth.
(footnote) At that time, judges ruled Israel.
```

Types: `(implicit-situational)`, `(implicit-background)`, `(implicit-subaction)`

---

## Quick Reference

| NIV Pattern | TBTA Transform |
|-------------|----------------|
| "he went" | Coreference → "John went" |
| "X, the king" | Relativization → "X, [who was king]" |
| "harvest" | LDV L2 → "gather/harvest" |
| "Moabite" | Demonym → "[from Moab]" |
| "can do" | Modal → "is able [to do]" |
| "LORD" | Hebrew → "Yahweh" |
| Passive | Active voice where possible |

---

## Terminology Index

| Term | Meaning |
|------|---------|
| **CNL** | Controlled Natural Language |
| **LDV** | Longman Defining Vocabulary (2000 core words) |
| **Coreference** | Pronoun → explicit noun |
| **Deixis** | Speaker/hearer reference marking |
| **Relativization** | Appositive → relative clause |
| **L2 pairing** | simple/complex word pair |
| **He1/He2** | Phase 1 (natural) / Phase 2 (strict) |
