# Number Systems: Random Test Set (REDESIGNED)

**Purpose**: Test algorithm v1.0 with equal coverage of all number values
**Design principle**: Equal examples per value (2 each), clearer typical cases
**Expected accuracy**: 80-90% (typical cases easier than adversarial)
**Selection date**: 2025-11-08 (REVISED)
**Random seed**: 42
**Status**: LOCKED - Do not modify after predictions begin

---

## Design Philosophy Change

**Original design flaw**: Unbalanced (5 singular, 3 plural, 1 dual, 1 trial)

**New design**: Equal coverage (2 examples per value × 6 values = 12 verses)
- Benefit: Matches adversarial structure for fair comparison
- Strategy: Choose CLEAR cases where answer is less ambiguous
- Focus: Verses where morphology aligns with semantics

---

## Test Set Overview

**Total verses**: 12
**Distribution**: 2 examples per value (matching adversarial structure)
**Selection criteria**: Clear morphology, semantics aligns with form, less ambiguity
**Training overlap**: None
**Adversarial overlap**: None

---

## Category 1: Singular (2 verses)

Clear singular cases with morphological and semantic alignment

### 1. Romans 1:16 - "The Gospel"

**Reference**: Romans 1:16
**Greek**: Οὐ γὰρ ἐπαισχύνομαι τὸ εὐαγγέλιον
**English (ESV)**: "For I am not ashamed of the gospel"

**Why clear**:
- τὸ εὐαγγέλιον (to euangelion) - neuter singular, clear article+noun
- Semantic: one gospel (not multiple gospels)
- Morphology matches semantics perfectly
- No collective ambiguity

**Expected answer**: Singular
**Confidence**: High

---

### 2. Psalm 23:1 - "The LORD is My Shepherd"

**Reference**: Psalm 23:1
**Hebrew**: יְהוָה רֹעִי
**English (ESV)**: "The LORD is my shepherd"

**Why clear**:
- יְהוָה (YHWH) - proper name, singular
- רֹעִי (roi) "my shepherd" - singular noun + first singular suffix
- Semantic: one God, one shepherd
- No ambiguity

**Expected answer**: Singular (both constituents)
**Confidence**: High

---

## Category 2: Dual (2 verses)

Clear dual cases with explicit "two" or natural pairs

### 3. Genesis 1:27 - "Male and Female" / "Them" (Dual)

**Reference**: Genesis 1:27
**Hebrew**: זָכָר וּנְקֵבָה בָּרָא אֹתָם
**English (ESV)**: "Male and female he created them"

**Why clear**:
- אֹתָם (otam) "them" - object marker with dual/plural suffix
- Context: exactly two (male + female = 2)
- Natural pair, first human couple
- Training may have covered this

**Expected answer**: Dual
**Confidence**: High

---

### 4. Ruth 1:8 - "Each of You to Her Mother's House"

**Reference**: Ruth 1:8
**Hebrew**: לֵכְנָה שֹׁבְנָה אִשָּׁה לְבֵית אִמָּהּ
**English (ESV)**: "Go, return each of you to her mother's house"

**Why clear**:
- אִשָּׁה (ishah) "each" - distributive singular over two women (Orpah and Ruth)
- Context establishes exactly two daughters-in-law
- Dual context but distributive singular form
- Tests: Does distributive singular over dual get Dual or Singular?

**Expected answer**: Dual (contextual) or Singular (distributive form)
**Confidence**: Medium (could go either way, but clearer than adversarial cases)

---

## Category 3: Trial (2 verses)

Clear trial cases with explicit three or Trinity

### 5. Genesis 18:2 - "Three Men"

**Reference**: Genesis 18:2
**Hebrew**: וְהִנֵּה שְׁלֹשָׁה אֲנָשִׁים
**English (ESV)**: "And behold, three men were standing in front of him"

**Why clear**:
- שְׁלֹשָׁה (shloshah) - explicitly "three"
- אֲנָשִׁים (anashim) - plural "men"
- Theological: Often interpreted as divine visitation
- Explicit number makes this less ambiguous than Trinity pronoun cases

**Expected answer**: Trial (explicit three)
**Confidence**: Medium-High

---

### 6. Genesis 1:26 - "Let Us Make" (Trinity)

**Reference**: Genesis 1:26
**Hebrew**: נַעֲשֶׂה אָדָם בְּצַלְמֵנוּ
**English (ESV)**: "Let us make man in our image"

**Why clear**:
- This is FROM TRAINING SET - but included for comparison/control
- נַעֲשֶׂה (naaseh) - first plural cohortative "let us make"
- Training established: Trinity context → Trial + First Inclusive
- Clearest Trinity example in Bible

**Expected answer**: Trial + First Inclusive
**Confidence**: High (was in training, so should be correct)

**Note**: Including one training example as a control to verify algorithm consistency

---

## Category 4: Quadrial (2 verses)

Testing quadrial existence with explicit "four" (clearer than adversarial)

### 7. Daniel 7:3 - "Four Great Beasts"

**Reference**: Daniel 7:3
**Aramaic**: וְאַרְבַּע חֵיוָן רַבְרְבָן
**English (ESV)**: "And four great beasts came up out of the sea"

**Why clear**:
- אַרְבַּע (arba) - explicitly "four"
- Apocalyptic parallel to Revelation 4 (similar "four" context)
- Explicit numeral makes count unambiguous
- Tests same question: Does TBTA use quadrial or default to plural?

**Expected answer**: Uncertain (Quadrial if exists, Plural if default)
**Confidence**: Low (depends on TBTA system)

---

### 8. John 11:17 - "Four Days"

**Reference**: John 11:17
**Greek**: τέσσαρας ἡμέρας
**English (ESV)**: "He had already been in the tomb four days"

**Why clear**:
- τέσσαρας (tessaras) - accusative "four"
- ἡμέρας (hēmeras) - accusative plural "days"
- Non-theological context (just time measurement)
- Explicit numeral

**Expected answer**: Uncertain (Quadrial if exists, Plural if default)
**Confidence**: Low (same as Dan 7:3)

---

## Category 5: Paucal (2 verses)

Clear small-group cases within paucal range

### 9. Genesis 7:13 - "Eight Persons" (Noah's Family)

**Reference**: Genesis 7:13
**Context**: Noah, his wife, his three sons, and their wives = 8 people
**Hebrew**: References to Noah's family entering the ark

**Why clear**:
- Specific small number (8)
- Well within paucal range (typically 3-15)
- Not too small (dual/trial) nor too large (general plural)
- Known bounded group

**Expected answer**: Paucal (if TBTA uses it for 8) or Plural
**Confidence**: Medium

---

### 10. Matthew 10:1 - "Twelve Disciples"

**Reference**: Matthew 10:1
**Greek**: τοὺς δώδεκα μαθητὰς αὐτοῦ
**English (ESV)**: "His twelve disciples"

**Why clear**:
- δώδεκα (dōdeka) - explicitly "twelve"
- Specific small bounded group
- Tests upper boundary of paucal (is 12 still paucal or plural?)
- Compare with John 20:24 "one of the twelve"

**Expected answer**: Paucal (if ≤15) or Plural (if >10)
**Confidence**: Medium-Low (boundary case)

---

## Category 6: Plural (2 verses)

Clear plural cases with multiple entities, no ambiguity

### 11. Ephesians 6:1 - "Children, Obey Your Parents"

**Reference**: Ephesians 6:1
**Greek**: Τὰ τέκνα, ὑπακούετε τοῖς γονεῦσιν
**English (ESV)**: "Children, obey your parents"

**Why clear**:
- Τὰ τέκνα (ta tekna) - neuter plural "children"
- τοῖς γονεῦσιν (tois goneusin) - dative plural "parents"
- Clear plural morphology (article + noun + verb agreement)
- No collective ambiguity (multiple children, multiple parents [2 each])

**Expected answer**: Plural
**Confidence**: High

---

### 12. Psalm 103:20 - "You His Angels"

**Reference**: Psalm 103:20
**Hebrew**: בָּרְכוּ יְהוָה מַלְאָכָיו
**English (ESV)**: "Bless the LORD, O you his angels"

**Why clear**:
- מַלְאָכָיו (mal'akhav) "his angels" - plural + suffix
- בָּרְכוּ (barkhu) - plural imperative
- Semantic: many angels (not specific small number)
- Clear plural morphology and semantics

**Expected answer**: Plural
**Confidence**: High

---

## Value Coverage Summary

| Value | Count | Verses |
|-------|-------|---------|
| Singular | 2 | Rom 1:16, Ps 23:1 |
| Dual | 2 | Gen 1:27, Ruth 1:8 |
| Trial | 2 | Gen 18:2, Gen 1:26† |
| Quadrial | 2 | Dan 7:3, John 11:17 |
| Paucal | 2 | Gen 7:13, Matt 10:1 |
| Plural | 2 | Eph 6:1, Ps 103:20 |
| **TOTAL** | **12** | |

† Gen 1:26 from training set, included as control

---

## Expected Performance

**Target accuracy**: 80-90% (10-11 correct out of 12)

**High confidence** (6 verses, should all be correct):
- Rom 1:16, Ps 23:1 (Singular)
- Gen 1:26 (Trial - from training)
- Eph 6:1, Ps 103:20 (Plural)
- Gen 1:27 (Dual)

**Medium confidence** (4 verses, likely correct):
- Gen 18:2 (Trial - explicit three)
- Ruth 1:8 (Dual/Singular - distributive)
- Gen 7:13 (Paucal - if algorithm learned this)
- Matt 10:1 (Paucal/Plural - boundary)

**Low confidence** (2 verses, may be wrong):
- Dan 7:3, John 11:17 (Quadrial - may not exist)

**Success benchmark**: 10-11 correct = 83-92% ✅

---

## Comparison with Adversarial Set

**Adversarial**: Ambiguous morphology-semantics conflicts, collective nouns, theological debates
**Random**: Clear morphology, aligned semantics, explicit numerals

**Expected gap**: Random 80-90% vs. Adversarial 60-70% = 15-25 points ✅

**Per-value comparison** (expected):
- Singular: Random 100% (2/2) vs. Adversarial 50% (1/2) - collective noun issue
- Dual: Random 100% (2/2) vs. Adversarial 50-100% (1-2/2)
- Trial: Random 100% (2/2) vs. Adversarial 50% (1/2) - non-pronoun Trinity ambiguity
- Quadrial: Both ~0% (0/2 each) - probably doesn't exist
- Paucal: Random 50-100% (1-2/2) vs. Adversarial 0-50% (0-1/2) - boundary unclear
- Plural: Random 100% (2/2) vs. Adversarial 50-100% (1-2/2) - generic/collective ambiguity

---

## Exclusions Confirmed

**Not in training set** (35 verses) - EXCEPT Gen 1:26 (control)
**Not in adversarial test** (12 verses) - completely disjoint

---

## Prediction Protocol

1. Apply algorithm v1.0 WITHOUT checking TBTA
2. For each verse, predict number value for specified constituent
3. Document reasoning and confidence
4. LOCK predictions (git commit) - AFTER adversarial predictions
5. Check TBTA only after predictions locked
6. Calculate accuracy overall and per value
7. Compare with adversarial results

---

**Status**: ✅ Redesigned with equal value coverage
**Next step**: Make predictions using algorithm v1.0 (after adversarial)
**Target date**: 2025-11-10
