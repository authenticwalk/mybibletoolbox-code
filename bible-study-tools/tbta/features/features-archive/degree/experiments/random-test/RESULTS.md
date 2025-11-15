# Degree Feature: Random Test Results

**Date**: 2025-11-09
**Algorithm**: v1.0 (commit d38b833)
**Predictions locked**: commit 70a4460
**TBTA data coverage**: 3 of 11 verses (27%) - **INSUFFICIENT DATA**

---

## Overall Results

**Accuracy**: 3/3 = **100%** (with caveats)

**Available vs. Missing TBTA Data**:
- ✅ Available (3): GEN 1:1 (training), MRK 1:35 (training), PHP 2:6
- ❌ Not in TBTA export (8): JHN 15:13, 1CO 13:13, 2CO 4:17, HEB 7:7, MAT 25:40, PHP 1:23, JHN 2:10, [T and s verses]

**WARNING**: Only 3 verses testable, 2 are training verses → NOT a valid independent test

---

## Detailed Results

### ✅ CORRECT (3/3)

#### 1. Genesis 1:1 - No Degree ⚠️ TRAINING VERSE
**Predicted**: N (No Degree)
**TBTA Actual**: No Degree
**Result**: ✓ CORRECT (expected - training verse)

**Constituent**: Verb "create"
**TBTA annotation**: `Adjective Degree: No Degree`
**Analysis**: Training verse from Phase 3. 100% expected to match.
**Value**: Confirms algorithm but NOT independent validation.

---

#### 2. Mark 1:35 - Intensified ⚠️ TRAINING VERSE
**Predicted**: I (Intensified)
**TBTA Actual**: Intensified
**Result**: ✓ CORRECT (expected - training verse)

**Constituent**: "early" (λίαν πρωῒ)
**TBTA annotation**: `Degree: Intensified`
**Analysis**: Training verse from Phase 3. λίαν → Intensified pattern verified in training.
**Value**: Confirms RULE 4 but NOT independent validation.

---

#### 3. Philippians 2:6 - No Degree (Equative Context)
**Predicted**: N (No Degree)
**TBTA Actual**: No Degree
**Result**: ✓ CORRECT

**Constituent**: "equal" (ἴσα) in "equal with God"
**TBTA annotation**: `Degree: No Degree`
**Analysis**: Equative construction gets "No Degree". Algorithm RULE 5 correct.

**Key finding**: TBTA does NOT use 'q' (Equative) as a degree value. Equatives are marked "No Degree".

**Value**: INDEPENDENT validation - confirms algorithm RULE 5 and confirms q (Equative) does NOT exist in TBTA.

---

## Missing Data Impact

**Critical verses missing** (8 of 11):
1. **JHN 15:13** (C - Comparative) - Would test synthetic comparative
2. **1CO 13:13** (S - Superlative) - Would test semantic superlative context
3. **2CO 4:17** (E - Extremely Intensified) - Would test double hyperbole
4. **HEB 7:7** (L - 'less') - Would test downward comparative
5. **MAT 25:40** (l - 'least') - Would test downward superlative
6. **PHP 1:23** (i - Intensified Comparative) - Would test πολλῷ μᾶλλον
7. **JHN 2:10** (s - Superlative of 2) - Would test dyadic superlative
8. **[T and s verses]** - Never identified in test set design

**Impact on validation**:
- Cannot test comparative accuracy (JHN 15:13 missing)
- Cannot test superlative accuracy beyond training (1CO 13:13 missing)
- Cannot test rare values (E, L, l, i, s, T) - all missing
- Cannot compare adversarial vs. random (insufficient overlap)

---

## Summary Statistics

### By Prediction vs. Actual

| Predicted | Actual | Count | Notes |
|-----------|--------|-------|-------|
| N | N | 2 | 1 training, 1 independent |
| I | I | 1 | Training verse |
| **TOTAL** | | 3 | 2 training, 1 independent |

**Independent accuracy**: 1/1 = 100% (but only 1 verse!)

---

## Comparison with Adversarial Test

**Cannot perform meaningful comparison** due to insufficient data.

**Adversarial**: 7 verses tested, 42.9% accuracy
**Random**: 3 verses tested (2 training), 100% accuracy (misleading)

**Expected gap**: ~20 percentage points (random should be easier)
**Actual gap**: Cannot calculate (training verses inflate random accuracy)

---

## Critical Finding: Equative is NOT a Degree Category

**PHP 2:6 finding**:
- Equative "equal with God" (ἴσα θεῷ)
- TBTA: "No Degree"
- Algorithm: Predicted "No Degree" ✓

**Conclusion**: TBTA does NOT use 'q' (Equative) as a degree value.
- Equatives are treated as non-gradable
- "Equal" is not on a scale (not "more equal" or "most equal")
- Confirms algorithm's RULE 5 (default to No Degree)

**Cross-validation with adversarial**:
- MAT 10:25 (adversarial) also tested equative → TBTA: "No Degree"
- 2/2 equative contexts marked "No Degree"
- **Confirmed**: q does NOT exist in TBTA

---

## Data Coverage Assessment

**Random test design**: 11 verses (1 per value)
**TBTA availability**: 3 verses (27%)
**Training overlap**: 2 verses (67% of available data!)

**Validity of results**:
- ❌ NOT a valid random test (too few verses)
- ❌ Training contamination (2/3 are training verses)
- ✓ Confirms one independent finding (q doesn't exist)

**Recommendation**:
- Cannot use this data for accuracy calculation
- Can only extract specific findings (q doesn't exist)
- Need alternative verses from available TBTA books

---

## Revised Test Set Needed

**To properly test random set with available TBTA data**:

Available books: Genesis, Exodus, Matthew, Mark, Luke, John (ch 1 only), Philippians, etc.

**Proposed substitute verses** (from available data):
1. N (No Degree) - Any baseline verse
2. C (Comparative) - Need to find in Matthew/Mark/Luke
3. S (Superlative) - Need to find in Matthew/Mark/Luke
4. I (Intensified) - MRK 1:35 (training, but only option)
5-11. Rare values - Likely don't exist or unavailable

**Challenge**: Most clear comparative/superlative examples are in epistles (not available in TBTA export)

---

## Expected vs. Actual Accuracy

**Original expectation**: 64-73% (7-8 correct out of 11)
**Actual**: Cannot calculate (insufficient independent data)

**If counting only independent verse**:
- 1/1 = 100% (but statistically meaningless)

**If including training verses**:
- 3/3 = 100% (misleading - training contamination)

---

## Next Steps

**Option A: Accept limited data**
- Document that random test could not be completed
- Use adversarial test as primary validation
- Note equative finding as key discovery

**Option B: Design new random test from available data**
- Search Matthew, Mark, Luke for clear comparative/superlative cases
- Focus on available books
- Accept that rare values cannot be tested

**Recommendation**: Option A - Proceed to error analysis with adversarial data only.

---

**Status**: Phase 7 complete for random test (INSUFFICIENT DATA)
**Accuracy**: Cannot calculate (only 1 independent verse)
**Key finding**: Equative (q) does NOT exist in TBTA
**Next**: Error analysis based on adversarial test results
