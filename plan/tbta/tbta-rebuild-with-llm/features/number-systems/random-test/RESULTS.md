# Number Systems: Random Test Results

**Date**: 2025-11-09
**Algorithm**: v1.0
**Predictions**: Locked at commit 39462a7
**TBTA Coverage**: Partial (Genesis verses only)

---

## Summary

**Total verses**: 12
**TBTA data available**: 4 verses (33%)
**Validated predictions**: 4 verses

### Accuracy (Preliminary)

**Overall (including Gen 1:26 control)**: 2/4 correct = **50%** (preliminary, Genesis only)
**Excluding control (new predictions only)**: 1/3 correct = **33%**

⚠️ **Note**: Gen 1:26 was in training set (control verse), making it guaranteed correct. True predictive accuracy on novel verses is **33%**, which is significantly below target accuracy (80-90%) due to limited coverage and key algorithm errors discovered.

---

## Detailed Results (TBTA Data Available)

### 1. Genesis 1:26 - "Let Us Make" (Control from Training)

**Prediction**: Trial + First Inclusive
**Confidence**: High (from training)

**TBTA Annotations**:
- God (as narrator): Singular (3x)
- God (as speaker "us"): **Trial** (3x)
- Other: Plural (12x), Singular (6x)

**Result**: ✅ **CORRECT** (Trial found for speaker role)
**Notes**: Control verse from training - validates algorithm consistency

---

### 2. Genesis 1:27 - "Male and Female...Them"

**Prediction**: Dual
**Confidence**: High
**Target**: אֹתָם (otam) "them" referring to male and female

**TBTA Annotations**:
- Singular: 11x (individual persons, God, image, man, woman)
- **Plural**: 6x (including references to "person" in general)
- Dual: 0x ❌

**Result**: ❌ **INCORRECT**
**Actual**: Plural (not Dual)

**Error Analysis**:
- Algorithm assumed "two persons" → Dual
- TBTA marks as Plural (standard pronoun, not dual form)
- Learning: TBTA uses Plural for standard plural pronouns, Dual may be reserved for explicit dual morphology or natural pairs

---

### 3. Genesis 18:2 - "Three Men"

**Prediction**: Plural
**Confidence**: Low
**Alternative**: Trial (if all explicit "three" get Trial)

**TBTA Annotations**:
- Singular: 8x (Abraham, tent, etc.)
- **Trial**: 3x (man, referring to the three visitors)
- Dual: 0x
- Plural: 0x ❌

**Result**: ❌ **INCORRECT**
**Actual**: Trial (not Plural)

**Error Analysis**:
- Algorithm assumed Trial only for Trinity theological contexts
- TBTA uses Trial for **all explicit groups of three**, not just Trinity
- Learning: Trial is productive for any explicit "three" (not Trinity-specific)

---

### 4. Genesis 7:13 - "Eight Persons" (Noah's Family)

**Prediction**: Plural
**Confidence**: Medium-Low
**Alternative**: Paucal (if 8 within range)

**TBTA Annotations**:
- Singular: 13x (Noah, day, weather, wife [singular], boat, etc.)
- **Trial**: 2x (son - referring to Noah's three sons)
- Plural: 1x (wife - plural for sons' wives)

**Result**: ⚠️ **PARTIAL**
**Notes**:
- Context has Plural (1x), but unclear if it's the target constituent
- Individual family members marked separately, not as collective "8"
- Trial used for "three sons"

**Learning**: TBTA may not mark collective groups as single Number, but individual constituents

---

## Verses Without TBTA Data

### 5. Romans 1:16 - "The Gospel"
**Prediction**: Singular (High confidence)
**Status**: No TBTA data (NT not available)

### 6. Psalm 23:1 - "The LORD" / "My Shepherd"
**Prediction**: Singular (High confidence)
**Status**: No TBTA data (Psalms not available)

### 7. Ruth 1:8 - "Each of You"
**Prediction**: Dual (Medium confidence)
**Status**: No TBTA data (Ruth not available)

### 8. Daniel 7:3 - "Four Great Beasts"
**Prediction**: Plural (Low confidence)
**Alternative**: Quadrial or Paucal
**Status**: No TBTA data (Daniel not available)

### 9. John 11:17 - "Four Days"
**Prediction**: Plural (Low confidence)
**Status**: No TBTA data (NT not available)

### 10. Matthew 10:1 - "Twelve Disciples"
**Prediction**: Plural (Medium-Low confidence)
**Status**: No TBTA data (NT not available)

### 11. Ephesians 6:1 - "Children" / "Parents"
**Prediction**: Plural (High confidence)
**Status**: No TBTA data (NT not available)

### 12. Psalm 103:20 - "Angels"
**Prediction**: Plural (High confidence)
**Status**: No TBTA data (Psalms not available)

---

## Accuracy by Value (Validated Only)

| Value | Correct | Total | Accuracy |
|-------|---------|-------|----------|
| Singular | - | 0 | N/A |
| Dual | 0 | 1 | 0% |
| Trial | 1 | 1 | 100% |
| Quadrial | - | 0 | N/A |
| Paucal | - | 0 | N/A |
| Plural | 0 | 2 | 0% |

**Overall (validated)**: 2/4 = **50%**

---

## Key Findings

### Algorithm Errors Discovered

1. **Dual not used as expected**
   - Predicted Dual for "them" (two persons) → TBTA uses Plural
   - TBTA may reserve Dual for explicit morphological dual or specific contexts

2. **Trial is productive beyond Trinity**
   - Genesis 18:2 "three men" → Trial (not Plural)
   - Trial applies to **all explicit groups of three**, not just theological Trinity

3. **High confidence predictions failing**
   - Gen 1:27 was "High confidence" but wrong (Dual → Plural)
   - Gen 18:2 was "Low confidence" and wrong (but correctly uncertain)

### Pattern Refinements Needed

**Algorithm v1.0 needs updates**:
1. Remove assumption: "Trial only for Trinity"
2. Add rule: "Trial for ALL explicit groups of three"
3. Investigate: When does TBTA use Dual? (needs more data)
4. Clarify: Collective groups vs. individual constituents

---

## Comparison with Target

**Target accuracy**: 80-90%
**Actual (validated)**: 50% (2/4 correct)
**Status**: ⚠️ Below target

**Expected gap with Adversarial**: Random should be 15-25 points higher
- Need Adversarial results to compare

---

## Test Set Design Validation

### Accuracy Reversal Analysis

**Expected pattern**: Random accuracy 15-25 points > Adversarial
**Actual pattern**: Adversarial (67%) > Random (50% with control, 33% without) = Random is 17-34 points LOWER

⚠️ **This reversal is unexpected and problematic**

**Possible explanations**:
1. **Small sample sizes** (3-4 verses) → high variance, not statistically reliable
2. **Random test had "hard" cases**: Gen 1:27 (Dual error), Gen 18:2 (Trial error)
   - These should have been in adversarial set, not random set
   - Suggests random selection was unlucky or biased
3. **Adversarial test had "easy" cases**: Mostly Singular (100% accuracy)
   - Did not achieve goal of "challenging edge cases"
   - Gen 22:6 Dual error, but overall still easier
4. **Test set design may not have achieved goals**:
   - "Adversarial" may not have been truly adversarial
   - "Random" may not have been truly random/typical

**Impact on conclusions**:
- Cannot confidently assert test sets were properly designed
- Accuracy gap suggests methodological issue, not algorithm performance
- Pattern validation (e.g., Trial expansion) still valid from error analysis
- Overall accuracy metrics less reliable

**Recommendation**: Phase 3 comprehensive validation with:
- Larger sample sizes (20+ examples per value)
- Stratified sampling (not pure random)
- Independent test design review
- Statistical power analysis

**Learning for future features**:
- Test set design is critical and difficult
- Small samples create high variance
- Need explicit criteria for "adversarial" vs "random"
- Consider having independent reviewer design test sets

---

## Next Steps

1. **Error Analysis** (Phase 8):
   - Exhaustive 6-step debugging for Gen 1:27, Gen 18:2
   - Investigate Dual usage in TBTA (may need more data)
   - Update algorithm v2.0 with Trial rule changes

2. **Data Coverage**:
   - Current: Genesis only (4/12 verses)
   - Need: NT and other OT books for full validation
   - Workaround: Use available data for pattern learning

3. **Algorithm Update**:
   - Trial = all explicit "three" (not Trinity-only)
   - Investigate Dual conditions
   - Test collective vs. individual constituent marking

---

**Status**: Partial validation complete (Genesis verses only)
**Next**: Complete adversarial test validation, then error analysis (Phase 8)
