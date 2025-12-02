# TBTA Verse Transformation Rules

> **Goal**: NIV → Controlled Natural Language (CNL) for universal translation
> **Corpus**: 6,963 verses | **Format**: He1 (natural) / He2 (strict)

---

## Source Strategy

**Copy NIV EXCEPT**:
- Pronouns → explicit nouns (coreference resolution)
- Compound sentences → segmented clauses
- Complex vocabulary → LDV pairs (He2)

**INCORPORATE FROM**:
- Hebrew: "Yahweh" for יהוה
- Scholarly: implicit cultural context via markers

---

## 🟢 HIGH Confidence Rules (>95% consistent)

### 1. Coreference Resolution
**Coreference Resolution** (Gen 1:22, Gen 1:26, Gen 1:28, Gen 3:6, Gen 4:8; NOT Gen 1:2)

Replace 3rd-person pronouns with explicit referents:
```
he/she/it/they → [Name] or "that man/woman/person"
his/her/their → [Name's] or "that person's"
```

### 2. Clause Segmentation
**Clause Segmentation** (Gen 1:4, Gen 1:5, Gen 1:10, Gen 1:16, Gen 1:27)

One predicate per sentence. Split at conjunctions:
```
"X and Y did Z" → "X did A. Y did B."
```

### 3. Subordinate Bracketing
**Subordinate Bracketing** (Gen 1:6, Gen 1:9, Gen 1:11, Gen 1:17, Gen 1:18; NOT Gen 1:1)

All non-main clauses in `[...]`:
- Relative: `[that/who/which...]`
- Purpose: `[in-order-to...]`, `[so-that...]`
- Temporal: `[when...]`, `[after...]`, `[before...]`
- Conditional: `[if...]`
- Causal: `[because...]`
- Result: `[with-the-result-that...]`

### 4. Deixis Marking
**Deixis Marking** (Gen 1:26, Gen 1:28, Gen 1:29, Gen 3:9, Gen 3:11; NOT Gen 1:1)

Mark 1st/2nd person referents in parentheses:
```
I(Speaker), you(Addressee), my(Possessor's), we(Group)
```

**Prefer generic labels over specific groups**:
- ✓ `you(people)`, `you(person)` - generic
- ✗ `you(Disciples)`, `you(followers)` - too specific

He2 additions: `_incl` (inclusive we), `_excl` (exclusive we)

### 5. Quote Framing
**Quote Framing** (Gen 1:3, Gen 1:6, Gen 1:9, Gen 1:11, Gen 1:26; NOT Gen 1:1)

```
Speaker said, ["Quote text."]
```

Nested: `["X said, ['inner quote']"]`

### 6. Imperative Marking
**Imperative Marking** (Gen 1:22, Gen 1:28, Gen 3:3, Gen 3:14, Gen 4:7)

```
You(Addressee) (imp) verb...
```

### 7. Yahweh Substitution
**Yahweh Substitution** (Gen 2:4, Gen 2:5, Gen 2:7, Gen 2:8, Gen 2:9; NOT Daniel references)

```
LORD (NIV) → Yahweh (CNL)
```

OT only. Hebrew יהוה rendered as "Yahweh".

### 8. Explicit Relativization
**Explicit Relativization** (Gen 1:11, Gen 1:12, Gen 1:21, Gen 1:24, Gen 2:8; NOT Gen 1:1)

Appositive → bracketed relative clause:
```
"X, the king" → "X, [who was the king]"
"city in Y" → "city [which was in Y]"
```

---

## 🟡 MEDIUM Confidence Rules (Context-dependent)

### 9. LDV Substitution (He2 mainly, some He1)
**LDV Substitution** (Matt 4:10, Matt 6:10, Mark 4:10, Ruth 1:2; NOT Ruth 1:1)

L2 level words paired: `simple/complex`
```
people/disciples, stories/parables, spirits/demons
family/clan, grain/barley, gather/harvest
teaches/preach, happy/joyful, cry/mourn-B
```

He1: 9.2% of verses | He2: 47.6% of verses

**Note**: Common pairs like `family/clan` appear in He1 too (Ruth 1:2)

### 10. Hyphenated Verbs
**Hyphenated Verbs** (Gen 2:21, Gen 3:8, Gen 4:8, Mark 1:17, Mark 2:14; NOT Gen 1:1)

Phrasal verbs hyphenated, **ALWAYS BASE FORM** (never inflected):
```
go-up (not went-up), sit-down (not sat-down)
run-away, stand-up, come-out, throw-away
```

**CRITICAL**: Use infinitive form regardless of tense:
- "Jesus went up" → "Jesus go-up"
- "they sat down" → "they sit-down"

He2 adds sense suffixes: `teaching-B`, `things-C`, `kingdom-B`

### 11. Underscore Implicit Markers (He2)
**Underscore Implicit Markers** (Matt 12:45, Matt 22:4, Mark 14:28, Mark 6:7, Acts 15:33)

He2 format uses extensive underscore taxonomy:
```
_implicit, _implicitNecessary, _implicitActiveAgent
_paragraph, _descriptive, _frameInferable
_dual, _generic, _hyperbolic, _metonymy
_AdverbLDV, _Dimplicit, _distantPast
```

Common uses:
- `_implicitActiveAgent` - agent in passive: "blessed by God _implicitActiveAgent"
- `_AdverbLDV` - adverb from LDV: "similarly _AdverbLDV"
- `_distantPast` - past tense marker: "were told _distantPast"

### 12. Dual Representations (He2)
**Dual Representations** (Matt 6:10, Matt 16:18, Matt 27:45, Mark 4:19, Acts 2:1)

Alternative translations provided:
```
(literal)/(dynamic) - Translation style
(complex)/(simple) - Accessibility
(literalunits)/(modernunits) - Time/measurement
```

### 13. Rhetorical Question Handling (He2)
**Rhetorical Question Handling** (Matt 16:10, Matt 23:11, Mark 2:7, Mark 7:18, Matt 5:47)

Questions marked by expected answer + statement form:
```
(norhetorical) Did you remember...?
(statement) You should remember...

(yesrhetorical) - Expected "yes"
(rhetorical) - General rhetorical
```

### 14. Named Entity Introduction
**Named Entity Introduction** (Gen 2:8, Gen 2:11, Gen 2:13, Gen 4:17, Gen 4:25; NOT Gen 1:1)

Consistent "named X" pattern:
```
a man named Adam
a city named Enoch
a country named Moab
```

### 15. Structural Markers (He1 & He2)
**Structural Markers** (Ruth 1:1, Matt 5:1, Matt 5:13, Matt 5:17, Acts 3:1)

Section organization:
```
(title), -Title - Section headers
(paragraph), _paragraph - Breaks
(footnote), -Footnote - Notes
```

**CRITICAL**: Titles describe ACTION, not traditional names:
- ✗ "(title) The Sermon on the Mount"
- ✓ "(title) Jesus teaches/preach about God's laws to people on a mountain"
- ✓ "(title) Elimelech and Naomi move from Bethlehem to Moab"

Both He1 and He2 use `(title)` markers at section starts.

---

## 🔴 LOW Confidence Rules (<50% consistent)

### 16. Demonym → Description
**Demonym → Description** (Ruth 1:2, Ruth 1:4, Esther 2:5, Mark 15:21; NOT Ruth 1:1, Esther 2:5)

**55% applied** - Inconsistent:
```
"Moabite" → "[who was from Moab]" (sometimes)
"Ephrathite" → "[who was in Ephrah's family/clan]" (sometimes)
```

Note: Some demonyms kept as-is (Jew, Greek).

### 17. Modal Decomposition
**Modal Decomposition** (Gen 1:25, Esther 4:11, Mark 5:4, Mark 6:2; NOT Gen 3:3, Esther 1:20)

**14% applied** - Only "can" converted:
```
"can X" → "is able [to X]" ✓
"must X" → kept as "must" ✗
"should X" → kept as "should" ✗
```

### 18. Number Formatting
**Number Formatting** (Gen 1:28, Gen 5:5, Esther 1:5; NOT Gen 1:5, Gen 1:8)

**~50% applied** - Inconsistent:
- Large numbers → digits: 127, 180, 10000
- Small numbers (1-12) → sometimes words
- "2" often written as digit

### 19. Passive Voice
**Passive Voice** (N/A; NOT Mark 2:3, Mark 5:2, Mark 15:23)

**0% converted** - Passives remain passive:
```
"was controlled by" - kept
"was carried by" - kept
```

He2 marks agent: `_implicitActiveAgent`

---

## Quick Reference

| Pattern | Transform | Confidence |
|---------|-----------|------------|
| pronouns | → explicit nouns | 🟢 HIGH |
| compound sentence | → multiple sentences | 🟢 HIGH |
| subordinate clause | → `[bracketed]` | 🟢 HIGH |
| I/you/we | → `I(Name)`, `you(Name)` | 🟢 HIGH |
| direct speech | → `said, ["..."]` | 🟢 HIGH |
| command | → `(imp) verb` | 🟢 HIGH |
| LORD | → Yahweh | 🟢 HIGH |
| complex word (He2) | → `simple/complex` | 🟡 MEDIUM |
| phrasal verb | → `run-away` | 🟡 MEDIUM |
| demonym | → `[from X]` | 🔴 LOW |
| "can" | → `is able [to]` | 🔴 LOW |
| passive | → keep passive | 🔴 N/A |

---

## He1 vs He2 Format

| Feature | He1 (OT style) | He2 (NT style) |
|---------|----------------|----------------|
| Underscore markers | Rare (0.6%) | Common (64%) |
| L2 word pairings | 9.2% | 47.6% |
| Sense suffixes | No | Yes (-A, -B, -C) |
| Dual translations | No | Yes |
| Use case | Natural reading | NLP/MT input |

---

## Terminology

| Term | Meaning |
|------|---------|
| **CNL** | Controlled Natural Language |
| **LDV** | Longman Defining Vocabulary |
| **Coreference** | Pronoun → explicit noun |
| **Deixis** | Speaker/hearer marking |
| **Relativization** | Appositive → relative clause |
| **He1/He2** | Phase 1 (natural) / Phase 2 (strict) |
