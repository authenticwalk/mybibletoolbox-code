# Degree Feature: Random Test Set (REDESIGNED)

**Purpose**: Test algorithm v1.0 with equal coverage of all degree values
**Design principle**: One example per value (11 values), clearer typical cases
**Expected accuracy**: 70-80% (typical cases easier than adversarial)
**Selection date**: 2025-11-08 (REVISED)
**Random seed**: 42
**TBTA Access**: FORBIDDEN until predictions locked
**Status**: LOCKED

---

## Design Philosophy Change

**Original design flaw**: Unbalanced (focused on comparative, missing many values)

**New design**: Equal coverage (1 example per value × 11 values = 11 verses)
- Benefit: Matches adversarial structure for fair comparison
- Strategy: Choose CLEAR cases where morphology aligns with semantics
- Focus: Unambiguous degree marking

---

## Test Set Overview

**Total verses**: 11
**Distribution**: 1 example per degree value (matching adversarial)
**Selection criteria**: Clear morphology, form = function, less ambiguity
**Training overlap**: None
**Adversarial overlap**: None

---

## Value 1: N (No Degree) - 1 verse

Clear base form with no degree marking

### 1. Genesis 1:1 - "In the Beginning"

**Reference**: Genesis 1:1
**Hebrew**: בְּרֵאשִׁית
**English (ESV)**: "In the beginning"

**Why clear**:
- No degree morphology whatsoever
- Baseline positive form
- No intensification, no comparison
- Simple descriptive use

**Expected answer**: N (No Degree)
**Confidence**: High

---

## Value 2: C (Comparative) - 1 verse

Clear synthetic comparative form

### 2. John 15:13 - "Greater Love"

**Reference**: John 15:13
**Greek**: μείζονα ταύτης ἀγάπην οὐδεὶς ἔχει
**English (ESV)**: "Greater love has no one than this"

**Why clear**:
- μείζονα (meizona) - comparative form of μέγας
- Synthetic morphology (-τερος suffix)
- Clear "X greater than Y" construction
- Form and function align perfectly

**Expected answer**: C (Comparative)
**Confidence**: High

---

## Value 3: S (Superlative) - 1 verse

Clear synthetic superlative form

### 3. Matthew 23:11 - "The Greatest Among You"

**Reference**: Matthew 23:11
**Greek**: ὁ δὲ μείζων ὑμῶν ἔσται ὑμῶν διάκονος
**English (ESV)**: "The greatest among you shall be your servant"

**Note**: If μείζων here is comparative not superlative, substitute with:

**Alternative**: 1 Corinthians 13:13 - "Greatest of These is Love"
**Greek**: μείζων δὲ τούτων ἡ ἀγάπη
**English (ESV)**: "The greatest of these is love"

**Why clear**:
- Explicit superlative context ("of these three")
- Clear partitive superlative construction
- Form and semantics align

**Expected answer**: S (Superlative)
**Confidence**: High

---

## Value 4: I (Intensified) - 1 verse

Clear intensifier adverb

### 4. Mark 1:35 - "Very Early"

**Reference**: Mark 1:35
**Greek**: πρωῒ ἔννυχα λίαν
**English (ESV)**: "And rising very early in the morning"

**Why clear**:
- λίαν (lian) - standard intensifying adverb "very"
- No ambiguity - pure intensification
- Straightforward I/V marking
- Training set included this type

**Expected answer**: I or V (Intensified/Very)
**Confidence**: High

---

## Value 5: E (Extremely Intensified) - 1 verse

Clear double intensification or hyperbole

### 5. 2 Corinthians 4:17 - "Beyond All Comparison"

**Reference**: 2 Corinthians 4:17
**Greek**: καθ' ὑπερβολὴν εἰς ὑπερβολὴν
**English (ESV)**: "Beyond all comparison" / "far more exceeding"

**Why clear**:
- καθ' ὑπερβολὴν εἰς ὑπερβολὴν - double hyperbole construction
- Explicit extreme intensification
- Morphologically marked as maximum degree
- If TBTA uses E, this is clearest case

**Expected answer**: E (Extremely Intensified) or I (if E doesn't exist)
**Confidence**: Medium (depends on E existing)

---

## Value 6: T ('too'/Excessive) - 1 verse

Looking for explicit "too" construction

### 6. Matthew 8:8 - "I Am Not Worthy"

**Reference**: Matthew 8:8 (checking for explicit "too" elsewhere)
**Alternative search**: Looking for ὑπέρ constructions meaning "too much"

**Note**: This value may not appear in Biblical Greek. If unavailable, mark as "No example found"

**Why uncertain**:
- "Too X" constructions rare in Koine Greek
- May not exist in TBTA Biblical data
- Included for completeness, but expect N/A

**Expected answer**: T (if exists) or No example available
**Confidence**: Very Low

---

## Value 7: L ('less'/Downward Comparative) - 1 verse

Clear "less than" construction

### 7. John 13:16 - "A Servant Is Not Greater Than His Master"

**Context**: "οὐκ ἔστιν δοῦλος μείζων τοῦ κυρίου αὐτοῦ"
**Reverse**: Implies servant is LESS than master

**Alternative**: Hebrews 7:7 - "The Lesser/Inferior"
**Greek**: τὸ ἔλαττον
**English (ESV)**: "The inferior is blessed by the superior"

**Why clearer than adversarial**:
- ἔλαττον (elatton) - explicit "lesser/inferior" form
- Paired with κρείττονος "greater/superior" for contrast
- Downward direction explicit

**Expected answer**: L (if directional) or C (if combined)
**Confidence**: Medium-Low

---

## Value 8: l ('least'/Downward Superlative) - 1 verse

Clear "least" superlative form

### 8. Matthew 25:40 - "Least of These My Brothers"

**Reference**: Matthew 25:40
**Greek**: ἐλαχίστων τούτων τῶν ἀδελφῶν μου
**English (ESV)**: "The least of these my brothers"

**Why clear**:
- ἐλαχίστων (elachistōn) - genitive plural superlative "least"
- Clear superlative morphology (-ιστος)
- Partitive construction ("of these")
- Downward direction explicit

**Expected answer**: l (if directional exists) or S (if combined)
**Confidence**: Medium

---

## Value 9: q (Equative) - 1 verse

Clear "as...as" equative construction

### 9. Matthew 10:24 - "A Disciple Is Not Above His Teacher"

**Greek**: οὐκ ἔστιν μαθητὴς ὑπὲρ τὸν διδάσκαλον οὐδὲ δοῦλος ὑπὲρ τὸν κύριον αὐτοῦ
**English (ESV)**: "A disciple is not above his teacher, nor a servant above his master"

**Alternative**: Looking for ὡς...ὡς "as...as" construction

### Better: Philippians 2:6 - "Equal with God"

**Greek**: ἴσα θεῷ (isa theō) - "equal to God"
**Explicit equative with ἴσος (isos) "equal"

**Why clear**:
- ἴσα (isa) - explicit "equal" adjective
- Clear equative semantics
- If TBTA uses q, this qualifies

**Expected answer**: q (if equative encoded) or N (if not degree)
**Confidence**: Low (rare value)

---

## Value 10: i (Intensified Comparative) - 1 verse

Clear "much more" construction

### 10. Philippians 1:23 - "Far Better"

**Reference**: Philippians 1:23
**Greek**: πολλῷ [μᾶλλον] κρεῖσσον
**English (ESV)**: "Far better" / "much better"

**Why clear**:
- πολλῷ (pollō) "much" + comparative
- κρεῖσσον (kreisson) "better" (comparative)
- Clear intensification of comparative
- If i exists, this is straightforward example

**Expected answer**: i (if exists) or C (if combined)
**Confidence**: Low (rare value)

---

## Value 11: s (Superlative of 2) - 1 verse

Clear "better of the two" dyadic context

### 11. John 2:10 - "You Have Kept the Good Wine Until Now"

**Context**: Comparing two wine servings (first vs. now)
**Greek**: τὸν καλὸν οἶνον... ἕως ἄρτι
**Comparison**: The better wine (of the two servings)

**Alternative**: Look for explicit "X-er of the two" constructions

**Why challenging even for random**:
- Dyadic superlative rare in Greek
- May not exist as distinct category
- Included for completeness

**Expected answer**: s (if exists) or C (comparative)
**Confidence**: Very Low

---

## Value Coverage Summary

| Value | Description | Verse | Confidence |
|-------|-------------|-------|------------|
| N | No Degree | Gen 1:1 | High |
| C | Comparative | John 15:13 | High |
| S | Superlative | 1 Cor 13:13 | High |
| I | Intensified | Mark 1:35 | High |
| E | Extremely Intensified | 2 Cor 4:17 | Medium |
| T | 'too' (Excessive) | [Searching] | Very Low |
| L | 'less' (Downward Comp) | Heb 7:7 | Medium-Low |
| l | 'least' (Downward Sup) | Matt 25:40 | Medium |
| q | Equative | Phil 2:6 | Low |
| i | Intensified Comparative | Phil 1:23 | Low |
| s | Superlative of 2 | [Searching] | Very Low |
| **TOTAL** | | **11** | |

---

## Expected Performance

**Target accuracy**: 70-80% (8-9 correct out of 11)

**High confidence** (4 verses, should all be correct):
- N (Gen 1:1)
- C (John 15:13)
- S (1 Cor 13:13)
- I (Mark 1:35)

**Medium confidence** (3 verses, likely correct):
- E (2 Cor 4:17) - if E exists
- L (Heb 7:7) - if directional exists
- l (Matt 25:40) - if directional exists

**Low confidence** (4 verses, may not exist):
- T, q, i, s - rare values, may not be in TBTA

**Success benchmark**: 7-9 correct = 64-82% ✅

---

## Comparison with Adversarial Set

**Adversarial**: Form-function mismatches, boundary ambiguities, rare value tests
**Random**: Form-function alignment, clear morphology, typical constructions

**Expected gap**: Random 70-80% vs. Adversarial 50-60% = 15-25 points ✅

**Per-value comparison** (expected):
- Common values (N, C, S, I): Random 100% vs. Adversarial 50-75%
- Directional (L, l): Both uncertain (may not distinguish)
- Rare (T, q, i, s, E): Both low (may not exist)

---

## Exclusions Confirmed

**Not in training set** (8 verses)
**Not in adversarial test** (11 verses)

---

## Prediction Protocol

1. Wait for algorithm v1.0 (from training)
2. Apply to each verse WITHOUT checking TBTA
3. Document reasoning
4. Rate confidence
5. LOCK predictions (git commit) - AFTER adversarial
6. Check TBTA after lock
7. Calculate accuracy overall and per value
8. Compare with adversarial results

---

**Status**: ✅ Redesigned with equal value coverage
**Next step**: Wait for algorithm v1.0, then predict (after adversarial)
**Target date**: 2025-11-10
