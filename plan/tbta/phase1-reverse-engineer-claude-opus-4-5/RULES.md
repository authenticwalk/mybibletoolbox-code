# TBTA Verse Transformation Rules (Complete Evidence)

> **Goal**: NIV → Controlled Natural Language for universal translation  
> **Corpus**: 6,963 verses | **Model**: Claude Opus 4.5 | **Date**: 2024-12-02

---

## Source Strategy

**Base**: Copy NIV text, **except**:
- Pronouns → explicit nouns (coreference resolution)
- Compound sentences → segmented clauses
- Idioms → decomposed meaning
- Complex vocabulary → LDV substitution (L2 pairings)

**Incorporate from**:
- **Hebrew**: "Yahweh" for יהוה (not NIV's "LORD")
- **Greek/Hebrew**: Implicit cultural context via markers
- **Scholarly sources**: Historical footnotes
- **Semantic analysis**: Clause boundaries, participant tracking

---

## 🟢 Core Transforms (Highly Reliable)

### 1. Coreference Resolution
**Evidence**: (Esther 1:19, Esther 2:4, Esther 3:13, Esther 4:11, Esther 6:6; NOT Genesis 1:2, Acts 16:33, Matthew 22:17)  
**Stats**: 915 supporting, 6 contradicting (99.3% reliable)

Replace 3rd-person pronouns with explicit referents:
```
he/she/it/they → [Name] or "that + noun"
```

**Examples**:
- "They went to Moab" → "That family went to a country named Moab"
- "he said" → "Boaz said" or "that man said"
- "her husband" → "Naomi's husband" or "that woman's husband"

**Pattern**: Use "that man/woman/person/family/group" when antecedent is contextually clear.

---

### 2. Clause Segmentation
**Evidence**: (Esther 1:1, Esther 1:5, Esther 1:6, Esther 1:7, Esther 1:10)  
**Stats**: 3,014 supporting, 0 contradicting (100% reliable)

One predicate per sentence. Split at conjunctions:
```
"X and Y did Z" → "X did A. Y did B." (separate sentences)
```

**Examples**:
- "The man's name was Elimelek, his wife's name was Naomi, and the names of his two sons were Mahlon and Kilion."
- → "That man's name was Elimelech. And that man's wife's name was Naomi. One son's name was Mahlon. And the other son's name was Kilion."

---

### 3. Explicit Relativization
**Evidence**: (Esther 1:1, Esther 1:2, Esther 1:3, Esther 1:4, Esther 1:5; NOT Esther 6:4, Esther 7:5, Mark 5:1)  
**Stats**: 4,072 supporting, 67 contradicting (98.4% reliable)

Appositive → bracketed relative clause:
```
"X, the king" → "X, [who was the king]"
"city in Y" → "city [which was in Y]"
"a man named X" → "a man [whose name was X]" (or keep "named")
```

**Bracket openers** (frequency order):
1. `[that...]` - 4,537 occurrences
2. `[who...]` - 2,562 occurrences
3. `[to...]` - 1,429 occurrences
4. `[when...]` - 721 occurrences
5. `[because...]` - 562 occurrences

---

### 4. Deixis Marking
**Evidence**: (Esther 1:15, Esther 1:16, Esther 1:17, Esther 1:19, Esther 1:20; NOT Acts 20:16, Acts 20:17, Acts 21:13)  
**Stats**: 3,248 supporting, 3 contradicting (99.9% reliable)

Mark 1st/2nd person referents in parentheses:
```
I(Speaker), you(Addressee), my(Possessor's), we(Group)
```

**Examples**:
- "I(Xerxes) want [to punish the queen]"
- "You(king) should write a new law"
- "We(men) must tell all of the people"
- "your(king's) kingdom"

**He2 additions**: `_incl` (inclusive we) and `_excl` (exclusive we)

---

### 5. Subordinate Bracketing
**Evidence**: (Esther 1:3, Esther 1:7, Esther 1:10, Esther 1:12, Esther 1:13; NOT Mark 10:7, Acts 17:25, Matthew 8:15)  
**Stats**: 2,362 supporting, 4 contradicting (99.8% reliable)

All subordinate clauses in `[...]`:
- **Relative**: `[who/that/which...]`
- **Patient/Content**: `knew [X happened]`, `said [that...]`
- **Purpose**: `[in order to...]`, `[so that...]`
- **Temporal**: `[when...]`, `[after...]`, `[before...]`, `[while...]`, `[until...]`
- **Conditional**: `[if X then...]`
- **Causal**: `[because...]`
- **Comparative**: `[just-like...]`, `[like...]`

---

### 6. Quote Framing
**Evidence**: (Esther 6:3, Esther 6:4, Esther 6:5, Esther 6:11, Esther 7:6)  
**Stats**: 1,017 supporting, 0 contradicting (100% reliable)

```
Speaker said, ["First sentence. Second sentence."]
```

**Pattern**: `said, ["..."]` with brackets around the quoted content.

**Nested quotes**:
```
["X said, ["inner quote"]"]
```

**Common speech verbs**: said (627), answered (107), asked (38), thought (31)

---

### 7. Imperative Marking
**Evidence**: (Esther 2:10, Esther 3:11, Esther 4:13, Esther 4:16, Esther 5:5)  
**Stats**: 1,189 supporting, 0 contradicting (100% reliable)

```
You(Addressee) (imp) verb...
```

**Examples**:
- "You(Esther) (imp) do not tell people [that you(Esther) are a Jew]"
- "You(king) (imp) give a royal robe to that man"
- "You(Mordecai) (imp) call all the Jews"

---

### 8. Yahweh Substitution
**Evidence**: (Genesis 8:21, Genesis 11:5, Genesis 11:6, Genesis 11:7, Genesis 11:8; NOT Daniel 8:13)  
**Stats**: 914 supporting, 1 contradicting (99.9% reliable)

```
LORD (NIV) → Yahweh (CNL)
```

Hebrew יהוה rendered as "Yahweh" rather than NIV's small caps "LORD".

---

## 🟡 Notation Patterns (Context-Dependent)

### 9. LDV Substitution (Longman Defining Vocabulary)
**Evidence**: (Mark 4:10, Mark 5:1, Mark 5:2, Mark 6:2, Mark 7:1)  
**Stats**: 1,466 supporting, varies by format

| Level | Color | Action |
|-------|-------|--------|
| L0-L1 | Blue/Cream | Use directly |
| L2 | Magenta | Pair: `simple/complex` |
| L3 | Green | Alternate: `(complex)...(simple)...` |
| L4 | Brown | Proper nouns, use directly |

**Common L2 pairings**:
- `people/disciples`, `stories/parables`, `spirits/demons`
- `family/clan`, `grain/barley`, `gather/harvest`
- `buy/redeem`, `dirty/unclean`, `surprised/amazed`
- `holes/caves`, `laws/Law`, `followers/disciples`

**He1 format**: Uses L2 pairings 9.2% of verses  
**He2 format**: Uses L2 pairings 47.6% of verses

---

### 10. Hyphenated Verbs
**Evidence**: (Mark 5:2, Mark 6:2, Mark 7:1, Mark 7:4, Mark 9:1; NOT Matthew 7:25, Matthew 7:27, Matthew 28:4)  
**Stats**: 1,076 supporting, 4 contradicting

Never inflect. Base form only:
```
come-out, sit-down, stand-up, run-away, cry-out
```

**He2 additions**: `teaching-B`, `things-C`, `kingdom-B` (semantic disambiguation suffixes)

---

### 11. Gap-filling (Implicit Information)
**Evidence**: (Mark 4:7, Mark 4:10, Mark 6:3, Mark 6:5, Mark 7:4)  
**Stats**: 1,526 supporting, 0 contradicting

Add missing subactions, cultural context:
```
(implicit-info), (footnote), (implicit-situational), (implicit-background)
```

**He2 underscore markers** (frequency):
- `_implicit`: 1,511
- `_paragraph`: 418
- `_implicitActiveAgent`: 351
- `_implicitNecessary`: 340
- `_frameInferable`: 130
- `_descriptive`: 81
- `_metonymy`: 59
- `_hyperbolic`: 31

---

### 12. Demonym → Description
**Evidence**: (Mark 14:55, Mark 15:43, Mark 15:21, Mark 1:28, Mark 5:14; NOT Esther 2:5)  
**Stats**: 157 supporting, 126 contradicting (55% applied)

```
"Moabite" → "[who was from Moab]"
"Ephrathite" → "[who was in Ephrah's family/clan]"
"Cyrene" → "[who was from Cyrene]"
```

**Note**: Not all demonyms are converted. Some remain as-is (especially proper nouns like "Jew", "Greek").

---

### 13. Number Formatting
**Evidence**: (Esther 1:5, Esther 1:10, Esther 1:11, Esther 1:12; NOT Esther 1:3, Esther 2:6, Esther 2:15)  
**Stats**: 535 supporting, 507 contradicting (~50% applied)

**Pattern observed**:
- **Large numbers** → digits: 127, 180, 10000
- **Small numbers (1-12)** → sometimes words: "one", "two", "three"
- **7** → often digit in Esther (frequent ritual number)

**Most frequent digit usage**: 2 (288), 3 (153), 7 (134), 1 (113), 12 (89)  
**Word numbers retained**: one (338), two (128), three (83)

---

## 🔴 Aspirational Rules (Not Consistently Applied)

### 14. Modal Decomposition
**Evidence**: (Esther 4:11, Esther 8:12, Mark 5:4, Mark 6:2, Mark 14:7; NOT Esther 1:20, Esther 1:22, Esther 2:2)  
**Stats**: 133 supporting, 787 contradicting (14% applied)

**What IS converted**:
```
"can X" → "is able [to X]"
```

**What is NOT converted** (kept as-is):
```
must, should, could, would (obligation/epistemic modality)
```

**Explanation**: "can" expresses ability → decomposed. "must/should" express obligation/necessity → kept as modal.

---

### 15. Passive → Active Voice
**Evidence**: (N/A; NOT Mark 5:2, Mark 15:23, Mark 2:3)  
**Stats**: 0 supporting, 76 contradicting (0% applied)

**Rule is NOT applied in corpus**. Passive constructions remain passive:
- "was controlled by an unclean spirit" ✓ (kept)
- "was carried by 4 men" ✓ (kept)
- "was mixed by those soldiers" ✓ (kept)

**He2 marker**: `_implicitActiveAgent` marks the implied agent in passive constructions.

---

## Quick Reference

| NIV Pattern | TBTA Transform | Reliability |
|-------------|----------------|-------------|
| "he went" | "John went" / "that man went" | 🟢 99% |
| "X, the king" | "X, [who was king]" | 🟢 98% |
| "LORD" | "Yahweh" | 🟢 99% |
| "I said" | "I(Speaker) said" | 🟢 99% |
| subordinate clause | `[bracketed]` | 🟢 99% |
| command | "(imp) verb" | 🟢 100% |
| "harvest" | "gather/harvest" (He2) | 🟡 varies |
| "Moabite" | "[from Moab]" | 🟡 55% |
| "can do" | "is able [to do]" | 🟡 14% |
| Passive | Keep passive | 🔴 0% converted |

---

## He1 vs He2 Format Selection

| Use Case | Recommended Format |
|----------|-------------------|
| Natural-sounding translation | He1 (OT style) |
| Semantic precision for NLP | He2 (NT style) |
| Minimal post-processing | He1 |
| Machine translation input | He2 |

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
| **He1** | Phase 1 format (natural, OT) |
| **He2** | Phase 2 format (strict, NT) |

