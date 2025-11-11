# Degree Feature: Random Test Predictions (LOCKED)

**Date**: 2025-11-09
**Algorithm**: v1.0 (commit d38b833)
**TBTA Access**: FORBIDDEN (predictions made WITHOUT checking TBTA)
**Prediction method**: Applied algorithm v1.0 to clearer cases
**Lock status**: LOCKED - DO NOT MODIFY AFTER COMMIT

---

## Prediction Summary

| # | Verse | Value Tested | Predicted | Confidence | Reasoning |
|---|-------|--------------|-----------|------------|-----------|
| 1 | Gen 1:1 | N (No Degree) | N | Very High | Training verse - RULE 5 |
| 2 | John 15:13 | C (Comparative) | C | High | Synthetic comparative morphology |
| 3 | 1 Cor 13:13 | S (Superlative) | S | High | Partitive superlative context |
| 4 | Mark 1:35 | I (Intensified) | I | Very High | Training verse - RULE 4 |
| 5 | 2 Cor 4:17 | E (Extremely Int) | E | Medium | Double hyperbole construction |
| 6 | [T searching] | T ('too') | N/A | N/A | No verse found |
| 7 | Heb 7:7 | L ('less') | C | Medium | No L distinction in algorithm |
| 8 | Matt 25:40 | l ('least') | S | Medium | No l distinction in algorithm |
| 9 | Phil 2:6 | q (Equative) | N | Low | No equative rule |
| 10 | Phil 1:23 | i (Intensified Comp) | C | Low | No i distinction in algorithm |
| 11 | [s searching] | s (Superlative of 2) | C | Very Low | No s distinction in algorithm |

**Overall confidence**: Medium-High (4 very high/high for training, 2 high for clear cases, 5 low-medium for rare values)

---

## Training Set Overlap Note

⚠️ **Warning**: GEN 1:1 and MRK 1:35 were in training set
- These should score 100% (already verified)
- Not ideal for independent testing
- Included per test set design, but flagged here

---

## Detailed Predictions

### 1. Genesis 1:1 - "In the Beginning" ⚠️ TRAINING VERSE

**Reference**: Genesis 1:1
**Status**: **TRAINING VERSE** (Phase 3 analysis)

**Training result**: No degree constituents found

#### Prediction

```yaml
# No adjectives/adverbs with degree in this verse
# If analyzed on verb "create":
Part: Verb
Adjective Degree: No Degree
```

**Confidence**: Very High (100%) - Training verse
**Reasoning**: RULE 5 verified in training

---

### 2. John 15:13 - "Greater Love"

**Reference**: John 15:13
**Greek**: μείζονα ταύτης ἀγάπην οὐδεὶς ἔχει
**English**: "Greater love has no one than this"
**Constituent**: "greater" (μείζονα)

#### Algorithm Application

**Step 1**: Part = Adjective ✓

**Step 2**: Morphology
- μείζονα (meizona) - **synthetic comparative**
- Irregular form (-ων pattern)
- Clear comparative morphology

**Step 3**: Semantic context
- "Greater love than this" - explicit comparative
- ἤ/than particle implied
- Morphology AND semantics align perfectly

**Step 4**: Apply rules
- **RULE 2**: Synthetic comparative + semantics agree
  - Morphology = Comparative ✓
  - Semantics = Comparative ✓
  - Perfect alignment

**Step 5**: Value = "Comparative"

#### Prediction

```yaml
Constituent: greater
Part: Adjective
Degree: Comparative
```

**Confidence**: High (95%)
**Reasoning**: Clear synthetic comparative (RULE 2), form = function
**Alternative**: None - this is textbook comparative

---

### 3. 1 Corinthians 13:13 - "Greatest of These Is Love"

**Reference**: 1 Corinthians 13:13
**Greek**: μείζων δὲ τούτων ἡ ἀγάπη
**English**: "The greatest of these is love"
**Constituent**: "greatest" (μείζων)

#### Algorithm Application

**Step 1**: Part = Adjective ✓

**Step 2**: Morphology
- μείζων (meizōn) - comparative form (not superlative)
- Same as John 15:13 morphologically

**Step 3**: Semantic context
- "Greatest of these three" - **partitive superlative**
- Context: faith, hope, love (three items)
- Semantic superlative with comparative form

**Step 4**: Apply rules
- **RULE 1**: Semantic context overrides morphology
  - Context is superlative (greatest of three) ✓
  - Adjective semantically superlative ✓
  - → Superlative (even with comparative morphology)

**Step 5**: Value = "Superlative"

#### Prediction

```yaml
Constituent: greatest
Part: Adjective
Degree: Superlative
```

**Confidence**: High (90%)
**Reasoning**: Semantic superlative context overrides comparative morphology (RULE 1)
**Alternative**: C (if morphology prioritized), but semantic superlative context is clear
**Note**: Similar pattern to MAT 22:36 training verse

---

### 4. Mark 1:35 - "Very Early" ⚠️ TRAINING VERSE

**Reference**: Mark 1:35
**Status**: **TRAINING VERSE** (Phase 3 analysis)

**Training result**: "early" marked "Intensified" by TBTA

#### Prediction

```yaml
Constituent: early
Part: Adverb
Degree: Intensified
```

**Confidence**: Very High (100%) - Training verse
**Reasoning**: RULE 4 verified in training (λίαν → Intensified)

---

### 5. 2 Corinthians 4:17 - "Beyond All Comparison"

**Reference**: 2 Corinthians 4:17
**Greek**: καθ' ὑπερβολὴν εἰς ὑπερβολὴν
**English**: "Beyond all comparison" / "far more exceeding"
**Constituent**: Hyperbole construction

#### Algorithm Application

**Step 1**: Part = Adverb (modifying "eternal weight of glory")

**Step 2**: Morphology
- καθ' ὑπερβολὴν εἰς ὑπερβολὴν - **double hyperbole**
- ὑπερβολή = "excess, extreme, hyperbole"
- Double construction = maximum intensification
- More extreme than Eph 3:20 (triple compound)

**Step 3**: Semantic context
- "Beyond all comparison" = absolute extreme
- Not just "very" but "beyond measure"
- Maximum degree intensification

**Step 4**: Apply rules
- **RULE 4**: Extreme intensifier
  - Beyond standard λίαν
  - Double hyperbole construction
  - → "Extremely Intensified" (E)

**Step 5**: Value = "Extremely Intensified"

#### Prediction

```yaml
Constituent: [adverbial modifier]
Part: Adverb
Degree: Extremely Intensified
```

**Confidence**: Medium (75%)
**Reasoning**: Double hyperbole = maximum intensification (RULE 4 extreme case)
**Alternative**: I (if E threshold not met) or C (if comparative reading)
**Note**: If this isn't E, then E might not exist in TBTA

---

### 6. T ('too'/Excessive) - NO VERSE FOUND

**Status**: Test set indicates "[Searching]"

**Prediction**: N/A - No verse provided

---

### 7. Hebrews 7:7 - "The Inferior"

**Reference**: Hebrews 7:7
**Greek**: τὸ ἔλαττον ὑπὸ τοῦ κρείττονος
**English**: "The inferior is blessed by the superior"
**Constituent**: "inferior" (ἔλαττον)

#### Algorithm Application

**Step 1**: Part = Adjective ✓

**Step 2**: Morphology
- ἔλαττον (elatton) - **synthetic comparative**
- "Lesser, inferior" (downward comparative)

**Step 3**: Semantic context
- Comparative: inferior vs. superior
- Direction: Downward (less not more)

**Step 4**: Apply rules
- **RULE 2**: Synthetic comparative
  - Morphology = Comparative ✓
  - Semantics = Comparative ✓
  - → Comparative
- **L distinction**: Algorithm does NOT distinguish L from C
- → Default to C

**Step 5**: Value = "Comparative"

#### Prediction

```yaml
Constituent: inferior
Part: Adjective
Degree: Comparative
```

**Confidence**: Medium (75%)
**Reasoning**: Synthetic comparative (RULE 2). Algorithm has no L distinction.
**Alternative**: L (if TBTA distinguishes downward)
**Same as adversarial**: Identical verse, identical prediction

---

### 8. Matthew 25:40 - "Least of These My Brothers"

**Reference**: Matthew 25:40
**Greek**: ἐλαχίστων τούτων τῶν ἀδελφῶν μου
**English**: "The least of these my brothers"
**Constituent**: "least" (ἐλαχίστων)

#### Algorithm Application

**Step 1**: Part = Adjective ✓

**Step 2**: Morphology
- ἐλαχίστων (elachistōn) - **superlative form**
- Genitive plural superlative "least"
- Synthetic superlative morphology (-ιστος)

**Step 3**: Semantic context
- Superlative: least among brothers
- Partitive construction ("of these")
- Direction: Downward (least not greatest)

**Step 4**: Apply rules
- **RULE 2**: Synthetic superlative
  - Morphology = Superlative ✓
  - Semantics = Superlative ✓
  - → Superlative
- **l distinction**: Algorithm does NOT distinguish l from S
- → Default to S

**Step 5**: Value = "Superlative"

#### Prediction

```yaml
Constituent: least
Part: Adjective
Degree: Superlative
```

**Confidence**: Medium (75%)
**Reasoning**: Synthetic superlative (RULE 2). Algorithm has no l distinction.
**Alternative**: l (if TBTA distinguishes downward superlative)

---

### 9. Philippians 2:6 - "Equal with God"

**Reference**: Philippians 2:6
**Greek**: ἴσα θεῷ (isa theō)
**English**: "Equal to/with God"
**Constituent**: "equal" (ἴσα)

#### Algorithm Application

**Step 1**: Part = Adjective ✓

**Step 2**: Morphology
- ἴσα (isa) - "equal" adjective
- No degree morphology (base form)
- Equative meaning ("equal to")

**Step 3**: Semantic context
- Equative: X equal to Y
- Not comparison (X > Y or X < Y)
- Equality relationship

**Step 4**: Apply rules
- **RULE 5**: Default
  - No degree morphology
  - No intensifier
  - No comparative/superlative context
  - → No Degree
- **q (Equative)**: Algorithm has NO rule for equative
  - Cannot predict q

**Step 5**: Value = "No Degree"

#### Prediction

```yaml
Constituent: equal
Part: Adjective
Degree: No Degree
```

**Confidence**: Low (60%)
**Reasoning**: No degree morphology (RULE 5). Algorithm cannot predict q.
**Alternative**: q (if TBTA treats equative as degree category)
**Key uncertainty**: Is equative a degree value in TBTA?

---

### 10. Philippians 1:23 - "Far Better"

**Reference**: Philippians 1:23
**Greek**: πολλῷ κρεῖσσον
**English**: "Far better" / "much better"
**Constituent**: "better" (κρεῖσσον) with intensifier πολλῷ

#### Algorithm Application

**Step 1**: Part = Adjective ✓

**Step 2**: Morphology
- κρεῖσσον (kreisson) - comparative "better"
- πολλῷ (pollō) - "much" (intensifier)
- Combined: intensified comparative

**Step 3**: Semantic context
- Comparative: "better to depart" (than to remain)
- Intensified: "much better" / "far better"

**Step 4**: Apply rules
- **RULE 2**: Comparative morphology
  - Head is κρεῖσσον (comparative)
  - → Comparative
- **i (Intensified Comparative)**: Algorithm does NOT have this category
- → Cannot predict i, default to C

**Step 5**: Value = "Comparative"

#### Prediction

```yaml
Constituent: better
Part: Adjective
Degree: Comparative
```

**Confidence**: Low (60%)
**Reasoning**: Comparative morphology (RULE 2). Algorithm has no i distinction.
**Alternative**: i (if TBTA has intensified comparative category)
**Same issue as adversarial ROM 5:15**

---

### 11. s (Superlative of 2) - NO CLEAR VERSE

**Status**: Test set indicates "[Searching]"

**Alternative analysis**: If testing John 2:10 "good wine"

**Reference**: John 2:10
**Greek**: τὸν καλὸν οἶνον
**English**: "The good wine" (comparing two servings)

#### Algorithm Application

**Step 1**: Part = Adjective ✓

**Step 2**: Morphology
- καλὸν (kalon) - positive form "good"
- No comparative or superlative morphology

**Step 3**: Semantic context
- Context: two wine servings (first vs. now)
- "Better wine of the two" (dyadic comparison)
- But morphology is positive

**Step 4**: Apply rules
- **RULE 5**: Default
  - No degree morphology
  - → No Degree (or possibly comparative in context)
- **s (Superlative of 2)**: Algorithm does NOT have this category

**Step 5**: Value = "No Degree" or "Comparative" (uncertain)

#### Prediction

```yaml
Constituent: good
Part: Adjective
Degree: No Degree
```

**Confidence**: Very Low (40%)
**Reasoning**: Positive form, no clear degree (RULE 5)
**Alternative**: C (comparative of two) or s (if dyadic superlative exists)

---

## Prediction Summary Statistics

### By Confidence Level

| Confidence | Count | Verses |
|------------|-------|--------|
| Very High (100%) | 2 | Gen 1:1, Mark 1:35 (training) |
| High (90-95%) | 2 | John 15:13, 1 Cor 13:13 |
| Medium (70-80%) | 4 | 2 Cor 4:17, Heb 7:7, Matt 25:40, (partial Phil 2:6/1:23) |
| Low (60-69%) | 2 | Phil 2:6, Phil 1:23 |
| Very Low (<50%) | 1 | John 2:10 (if s test) |
| N/A | 2 | T and s (no verses) |

### By Predicted Value

| Predicted Value | Count | Verses |
|-----------------|-------|--------|
| No Degree (N) | 2 (3 with training) | Gen 1:1*, Phil 2:6, (John 2:10) |
| Comparative (C) | 3 | John 15:13, Heb 7:7, Phil 1:23 |
| Superlative (S) | 2 | 1 Cor 13:13, Matt 25:40 |
| Intensified (I) | 1 | Mark 1:35* |
| Extremely Intensified (E) | 1 | 2 Cor 4:17 |
| **Rare values not predicted**: T, L, l, q, i, s | 0 | Algorithm cannot predict |

*Training verse

### Comparison with Adversarial Predictions

| Value | Adversarial Pred | Random Pred | Note |
|-------|------------------|-------------|------|
| N | 3 | 3 | Same algorithm |
| C | 5 | 3 | Fewer in random |
| S | 2 | 2 | Same |
| I | 0 (adv) | 1* | Training verse |
| E | 1 | 1 | Both uncertain |
| Rare (T,L,l,q,i,s) | 0 | 0 | Algorithm gaps |

---

## Expected Performance

**Conservative estimate**: 7-8 correct (64-73%)
- Training verses (2): 100% correct
- High confidence clear cases (2): 90% likely (1-2 correct)
- Medium (4): 75% likely (3 correct)
- Low (2): 50% likely (1 correct)
- Very low/N/A (1+2): 0 likely

**Optimistic estimate**: 8-9 correct (73-82%)
- All clear cases correct
- Some rare value luck

**Gap from adversarial**: Random should be 15-25 points higher
- Adversarial expected: 45-55%
- Random expected: 64-73%
- Gap: ~20 points ✓

---

## Key Differences from Adversarial

1. **Training overlap**: GEN 1:1, MRK 1:35 in both training and random test (not ideal)
2. **Clearer morphology**: John 15:13 (clear C), 1 Cor 13:13 (clear S context)
3. **Same rare value gaps**: T, L, l, q, i, s still cannot be predicted
4. **Same verses**: Heb 7:7 in both adversarial and random

**Net effect**: Higher confidence on 4 verses (2 training + 2 clear), rest similar to adversarial

---

## Lock Information

**Status**: LOCKED
**Date locked**: 2025-11-09
**Algorithm version**: v1.0 (commit d38b833)
**Training overlap**: 2 verses (flagged)
**Next step**: Commit this file, then check TBTA for both test sets
**Git commit**: 70a4460

**DO NOT MODIFY THIS FILE AFTER COMMIT**
**All changes after validation go in RESULTS.md and ERROR-ANALYSIS.md**
