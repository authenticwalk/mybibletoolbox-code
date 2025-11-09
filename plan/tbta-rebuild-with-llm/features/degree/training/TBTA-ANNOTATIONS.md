# Degree Feature: TBTA Training Annotations

**Purpose**: Document actual TBTA annotations for training set
**Date extracted**: 2025-11-09
**Verses analyzed**: 4 of 8 (partial dataset available)

---

## Data Availability

**Successfully extracted** (4 verses):
1. ✅ MAT 22:36 - Semantic superlative (question)
2. ✅ MAT 22:38 - Semantic superlative (answer)
3. ✅ MRK 1:35 - Intensified adverb
4. ✅ GEN 1:1 - No degree (baseline)

**Not available in TBTA export** (4 verses):
5. ❌ JHN 15:13 - Only John chapter 1 in dataset
6. ❌ HEB 7:7 - Book not in TBTA export
7. ❌ SNG 1:2 - Book not in TBTA export
8. ❌ SNG 1:8 - Book not in TBTA export

**Note**: TBTA export is incomplete (30 of 66 books). Training proceeds with available data.

---

## Verse 1: Matthew 22:36 - Semantic Superlative (Question)

**Reference**: MAT 22:36
**Greek**: Διδάσκαλε, ποία ἐντολὴ μεγάλη ἐν τῷ νόμῳ;
**English**: "Teacher, which is the great commandment in the Law?"

### TBTA Degree Annotations

```yaml
# Line 110
- Constituent: religious
  Part: Adjective
  Degree: No Degree

# Line 163
- Constituent: important
  Part: Adjective
  Degree: Superlative
```

### Analysis

1. **"important" marked as Superlative**
   - Greek uses μεγάλη (megalē) - **positive form**, not superlative μεγίστη
   - Question context: "which is the GREATEST?" → semantic superlative
   - **Pattern**: TBTA marks semantic meaning, not morphological form

2. **"religious" marked as No Degree**
   - Attributive adjective with no degree semantics
   - Baseline pattern confirmed

---

## Verse 2: Matthew 22:38 - Semantic Superlative (Answer)

**Reference**: MAT 22:38
**Greek**: αὕτη ἐστὶν ἡ μεγάλη καὶ πρώτη ἐντολή
**English**: "This is the great and first commandment"

### TBTA Degree Annotations

```yaml
# Line 43
- Constituent: great
  Part: Adjective
  Degree: Superlative

# Line 115
- Constituent: important
  Part: Adjective
  Degree: Superlative
```

### Analysis

1. **"great" marked as Superlative**
   - Greek uses μεγάλη (megalē) - positive form again
   - Answer to superlative question from v36
   - Combined with πρώτη "first" (ordinal superlative)
   - **Pattern**: Discourse context drives superlative marking

2. **"important" marked as Superlative**
   - Same constituent as v36, same superlative marking
   - Confirms consistency across related verses

---

## Verse 3: Mark 1:35 - Intensified Adverb

**Reference**: MRK 1:35
**Greek**: Καὶ πρωῒ ἔννυχα λίαν ἀναστὰς ἐξῆλθεν
**English**: "And rising very early in the morning, while it was still dark, he departed"

### TBTA Degree Annotations

```yaml
# Line 41
- Constituent: alone
  Part: Adverb
  Degree: No Degree

# Line 98
- Constituent: dark
  Part: Adjective
  Degree: No Degree

# Line 109
- Constituent: still
  Part: Adverb
  Degree: No Degree

# Line 176
- Constituent: early
  Part: Adverb
  Degree: Intensified

# Line 323
- Constituent: other
  Part: Adjective
  Degree: No Degree
```

### Analysis

1. **"early" marked as Intensified**
   - Greek λίαν (lian) - standard intensifier "very"
   - Modifies πρωῒ (prōi) "early in the morning"
   - **Pattern**: Intensifiers get "Intensified" value

2. **Multiple "No Degree" examples**
   - Confirms "No Degree" is default for non-degree constituents
   - Applies to both adjectives and adverbs

---

## Verse 4: Genesis 1:1 - No Degree (Baseline)

**Reference**: GEN 1:1
**Hebrew**: בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ
**English**: "In the beginning, God created the heavens and the earth"

### TBTA Degree Annotations

```yaml
# Line 27
- Constituent: create
  Part: Verb
  Adjective Degree: No Degree

# Line 125
- Constituent: create
  Part: Verb
  Adjective Degree: No Degree
```

### Analysis

1. **Verbs use different field name**
   - Field: "Adjective Degree: No Degree" (not just "Degree:")
   - Verbs can have degree in TBTA schema (intensification)
   - This verse has no degree marking (baseline)

2. **No adjectives or adverbs with degree**
   - Pure narrative, no comparison or intensification
   - Confirms "No Degree" baseline

---

## Cross-Verse Patterns

### Pattern 1: Semantic Over Morphological

**Evidence**:
- MAT 22:36: μεγάλη (positive) → "Superlative" (context-driven)
- MAT 22:38: μεγάλη (positive) → "Superlative" (discourse answer)

**Rule**: TBTA marks semantic degree meaning, not Greek morphology

### Pattern 2: Field Names by Part of Speech

| Part of Speech | Field Name | Values Seen |
|----------------|------------|-------------|
| Adjective | `Degree:` | No Degree, Superlative |
| Adverb | `Degree:` | No Degree, Intensified |
| Verb | `Adjective Degree:` | No Degree |

### Pattern 3: Value Encoding

TBTA uses **full words**, not single-letter codes:
- ✅ "No Degree" (not "N")
- ✅ "Superlative" (not "S")
- ✅ "Intensified" (not "I" or "V")

### Pattern 4: Discourse Context Matters

MAT 22:36-38 shows discourse-level degree assignment:
- Question (v36) establishes superlative context
- Answer (v38) maintains superlative marking
- Same Greek form, same semantic superlative across both verses

---

## Missing Data Impact

**Verses we don't have**:
1. **JHN 15:13** - Synthetic comparative (μείζονα)
   - Would show: Comparative morphology → "Comparative" value
2. **HEB 7:7** - Upward/downward comparison
   - Would show: ἔλαττον (lesser) and κρείττονος (better)
3. **SNG 1:2** - Hebrew comparative (מִן construction)
   - Would show: Hebrew comparative → "Comparative"
4. **SNG 1:8** - Hebrew superlative
   - Would show: Hebrew superlative patterns

**Workaround**: Use existing TBTA research and linguistic knowledge to infer patterns for missing verses.

---

## Key Findings Summary

1. **TBTA values**: "No Degree", "Superlative", "Intensified" (full words)
2. **Field names**: "Degree:" (adj/adv), "Adjective Degree:" (verbs)
3. **Semantic priority**: Context overrides morphology (positive → superlative)
4. **Intensifiers**: λίαν → "Intensified"
5. **Default**: "No Degree" for non-degree constituents

---

## Next Steps

1. ✅ TBTA annotations documented (4 verses)
2. ⏳ Infer patterns for missing verses from linguistic knowledge
3. ⏳ Create PATTERNS-LEARNED.md (comprehensive analysis)
4. ⏳ Create ALGORITHM-v1.md (decision rules)
5. ⏳ Lock algorithm with git commit

---

**Status**: Training data extraction complete (partial dataset)
**Coverage**: 4/8 verses (50%), but covers key patterns
**Ready for**: Pattern analysis phase
