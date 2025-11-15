# Participant Tracking v2.0 Test Strategy Analysis

**Date**: 2025-11-15
**Task**: Select NEW test set for Algorithm v2.0 validation
**Constraint**: Cannot use same 12 verses from v1.0 error analysis (introduces bias)

---

## Executive Summary

**RECOMMENDATION: Option B - Random Stratified Sample (12-15 verses)**

**Rationale**: Balances methodological rigor, resource efficiency, and genre coverage. Provides blind validation while avoiding adversarial test bias and cross-validation complexity.

**Key advantages**:
- ✅ Blind validation (no cherry-picking)
- ✅ Genre diversity ensures real-world applicability
- ✅ Achievable in 1-2 sessions
- ✅ Statistical validity with 12-15 samples
- ✅ Tests algorithm robustness across genres

---

## Three Options Evaluated

### Option A: Adversarial Test (10 verses from Stage 4 design)

**Description**: Use 10 verses specifically designed to test epistolary abstracts, nested quotes, and recognition frames.

**Pros**:
- ✅ **Targeted testing**: Directly tests v2.0's three fixes (epistolary abstracts, quantifier+definite, recognition frame)
- ✅ **Known edge cases**: Tests hardest scenarios (epistolary theology, complex recognition scenes)
- ✅ **Small sample size**: Only 10 verses (efficient)
- ✅ **Efficient resource use**: 1-2 sessions to complete

**Cons**:
- ❌ **Selection bias**: Verses chosen to test specific fixes, not representative of real usage
- ❌ **Over-optimistic results**: Algorithm designed for these exact patterns → inflated accuracy
- ❌ **No baseline comparison**: Can't compare to v1.0 (v1.0 wasn't tested on adversarial set)
- ❌ **Limited generalizability**: Strong on edge cases, unclear on typical cases
- ❌ **Missing verses**: TODO.md mentions adversarial search designed but not executed (verses may not exist yet)

**Validation concerns**:
- **Methodological integrity**: Testing on verses used to design the algorithm violates blind testing principles
- **Reproducibility**: Adversarial tests are inherently researcher-biased
- **Real-world applicability**: Edge cases ≠ typical usage

**Verdict**: ❌ **NOT RECOMMENDED**
- Violates blind validation principles
- High risk of bias (designed to pass these exact tests)
- Better suited for debugging specific edge cases, not production validation

---

### Option B: Random Stratified Sample (12-15 verses)

**Description**: Select NEW random sample with genre stratification:
- 50% Narrative (6-8 verses): Genesis, Gospels, Acts, OT narratives
- 30% Epistle (4-5 verses): Paul, general epistles (Ephesians, 2 John, etc.)
- 15% Poetry/Wisdom (2 verses): Psalms, Proverbs, Job
- 5% Prophecy (1 verse): Isaiah, Daniel, Revelation

**Pros**:
- ✅ **Blind validation**: Random selection eliminates researcher bias
- ✅ **Genre diversity**: Tests all 4 genres (v1.0 lacked epistolary coverage)
- ✅ **Comparable to v1.0**: Same sample size (12 verses), can compare accuracy
- ✅ **Production-representative**: Mimics real-world usage distribution
- ✅ **Statistical validity**: 12-15 samples sufficient for pattern detection
- ✅ **Methodologically rigorous**: Standard ML validation approach
- ✅ **Efficient**: 1-2 sessions (same as adversarial)

**Cons**:
- ⚠️ **May miss edge cases**: Random sampling might not hit epistolary abstracts or recognition frames
- ⚠️ **Requires genre tagging**: Need to classify all 215 TBTA verses by genre first
- ⚠️ **Variance risk**: Small sample may not fully represent genre complexity

**Implementation steps**:
1. **Genre classification**: Tag all 215 TBTA verses by genre (Narrative, Epistle, Poetry, Prophecy)
   - Use book codes from Algorithm v2.0 Rule 0 (EPH, PHP, etc. = Epistle)
   - Estimated: 30 minutes (automated via book code lookup)
2. **Stratified sampling**:
   - Narrative: Sample 6-8 verses from narrative books (excluding v1.0 test set)
   - Epistle: Sample 4-5 verses from epistles (ensuring Ephesians, 2 John included)
   - Poetry: Sample 2 verses from Psalms/Proverbs
   - Prophecy: Sample 1 verse from Isaiah/Daniel
3. **Blind prediction**:
   - Run Algorithm v2.0 WITHOUT accessing TBTA ground truth
   - Commit predictions to git BEFORE validation
4. **Accuracy calculation**:
   - Compare v2.0 predictions to TBTA ground truth
   - Calculate per-genre and overall accuracy
   - Compare to v1.0 baseline (60-70% random, 97% training)

**Verdict**: ✅ **STRONGLY RECOMMENDED**
- Best balance of rigor, efficiency, and generalizability
- Tests v2.0 on realistic genre distribution
- Allows direct comparison to v1.0 (same sample size)
- Methodologically sound (blind random sampling)

---

### Option C: Cross-Validation (Split 215 TBTA verses into train/test)

**Description**: Divide original 215 TBTA verses into training set (e.g., 70% = 150 verses) and test set (30% = 65 verses). Train on 150, validate on 65.

**Pros**:
- ✅ **Largest sample size**: 65 test verses (vs. 12-15 random or 10 adversarial)
- ✅ **Statistical power**: High confidence in accuracy estimates
- ✅ **Standard ML practice**: Gold standard for algorithm validation
- ✅ **Train/test separation**: Guarantees no data leakage
- ✅ **Multiple iterations**: Can run k-fold cross-validation (e.g., 5-fold)

**Cons**:
- ❌ **High resource cost**: Testing on 65 verses = 5-10 sessions (vs. 1-2 for other options)
- ❌ **Methodological mismatch**: v1.0 was trained on 15 verses, not 150 (changes algorithm basis)
- ❌ **Over-complicates validation**: Algorithm is rule-based, not ML (doesn't require large train/test splits)
- ❌ **Genre imbalance**: 215 verses are narrative-heavy (Gospels, Acts) → test set may lack epistle coverage
- ❌ **Rare state problem**: With 65 test verses, still unlikely to find Restaging, Integration, Exiting (need 100+ verses)

**Implementation complexity**:
1. **Genre stratification**: Ensure train and test sets have proportional genre distribution
2. **Rare state allocation**: Manually ensure rare states (if any) are in test set
3. **k-fold cross-validation**: 5 iterations × 65 verses = 325 predictions → 10-20 sessions
4. **Result aggregation**: Average across folds, compute standard deviation

**Verdict**: ❌ **NOT RECOMMENDED**
- Excessive resource cost (5-10 sessions vs. 1-2)
- Methodological overkill for rule-based algorithm
- v2.0 is not data-driven ML (doesn't require large-scale training)
- Better suited for future research (if building ML participant tracker)

---

## Comparative Analysis

| Criterion | Option A (Adversarial) | Option B (Random Stratified) | Option C (Cross-Validation) |
|-----------|------------------------|------------------------------|----------------------------|
| **Methodological rigor** | ❌ Low (biased) | ✅ High (blind random) | ✅ Very High (train/test split) |
| **Resource efficiency** | ✅ 1-2 sessions | ✅ 1-2 sessions | ❌ 5-10 sessions |
| **Genre coverage** | ⚠️ Medium (edge cases) | ✅ High (stratified 4 genres) | ⚠️ Medium (narrative-heavy) |
| **Sample size** | 10 verses | 12-15 verses | 65 verses |
| **Bias risk** | ❌ High (designed for fixes) | ✅ Low (random) | ✅ Very Low (train/test) |
| **Comparable to v1.0** | ❌ No | ✅ Yes (same sample size) | ❌ No (different scale) |
| **Production applicability** | ❌ Low (edge cases) | ✅ High (realistic distribution) | ⚠️ Medium (large-scale) |
| **Epistolary coverage** | ✅ High (targeted) | ✅ Medium (30% stratified) | ⚠️ Low (narrative-heavy corpus) |

---

## Final Recommendation: Option B

### Why Option B is Best

1. **Balances rigor and efficiency**: Blind random sampling with stratification ensures validity without excessive resource cost
2. **Genre diversity**: 30% epistle allocation (4-5 verses) guarantees testing of v2.0's epistolary abstract fix
3. **Comparable to v1.0**: Same 12-verse scale allows direct accuracy comparison (v1.0: 60-70%, v2.0 target: 80%+)
4. **Production-ready validation**: Tests realistic usage distribution (narrative-heavy, but includes epistles, poetry, prophecy)
5. **Achievable timeline**: 1-2 sessions (vs. 5-10 for cross-validation)

### Refinements to Option B

**Enhanced stratification** (15 verses total):
- **Narrative (8 verses, 53%)**:
  - 3 Genesis (creation, family, patriarchs)
  - 3 Gospels/Acts (Jesus teaching, miracles, early church)
  - 2 OT narratives (Samuel, Kings, Esther)
- **Epistle (5 verses, 33%)**:
  - 2 Pauline epistles (Ephesians, Colossians, Romans)
  - 2 General epistles (2 John, 1 Peter, James)
  - 1 Hebrews (bridge genre: epistle + OT commentary)
- **Poetry/Wisdom (2 verses, 13%)**:
  - 1 Psalm (generic/timeless statements)
  - 1 Proverbs/Job (wisdom maxims)
- **Prophecy (1 verse, 7%)**:
  - 1 vision/oracle passage (Isaiah, Daniel, or Revelation)

**Sampling constraints**:
1. Exclude 12 verses from v1.0 test set (avoid contamination)
2. Prioritize verses with:
   - Theological abstracts in epistles (grace, mercy, peace) → tests Rule 2.3b
   - Universal quantifiers + definite article ("all the X") → tests Rule 2.1
   - Recognition scenes (if available) → tests Rule 3.2
3. Random selection within genre strata (use random seed for reproducibility)

**Implementation timeline**:
- **Session 1 (30 minutes)**: Genre classification of 215 TBTA verses
- **Session 1 (1 hour)**: Stratified random sampling (15 verses)
- **Session 2 (2-3 hours)**: Apply Algorithm v2.0 blindly (no TBTA access)
- **Session 2 (1 hour)**: Validate against TBTA, calculate accuracy
- **Total**: 2 sessions, 4.5-5.5 hours

---

## Risk Mitigation

### Risk 1: Random sample misses epistolary abstracts

**Mitigation**:
- Stratify epistle sampling by book (ensure Ephesians, 2 John, Colossians included)
- If first random draw lacks abstracts, re-sample within epistle stratum (documented in methodology)

### Risk 2: Small sample size (15 verses) → high variance

**Mitigation**:
- If v2.0 accuracy is borderline (78-82%), expand test set to 20-25 verses
- Use confidence intervals (binomial proportion CI) to assess statistical significance
- Example: 12/15 correct (80%) → 95% CI: [52%, 96%] (wide, but includes 80% threshold)

### Risk 3: No recognition frames in random sample

**Mitigation**:
- Recognition frames are rare (Acts 3:10 is primary example)
- If absent from random sample, note as "not tested" in validation report
- Defer recognition frame validation to adversarial test in future session (optional)

---

## Success Criteria

### Minimum Viable Validation (v2.0 production consideration)

- ✅ **Accuracy ≥80%** on NEW test set (12-15 verses)
- ✅ **Genre-stratified performance**:
  - Narrative: ≥75% (baseline comparison to v1.0)
  - Epistle: ≥80% (tests v2.0's key fix)
  - Poetry: ≥70% (generic-heavy, harder to predict)
  - Prophecy: ≥60% (vision frames, complex)
- ✅ **Error analysis**: Identify remaining systematic errors (if <80%)
- ✅ **Blind protocol maintained**: Predictions committed to git BEFORE accessing TBTA

### Production-Ready Validation (v2.0 gold standard)

- ✅ **Accuracy ≥85%** on NEW test set
- ✅ **All genres pass threshold**: Narrative ≥80%, Epistle ≥85%, Poetry ≥75%, Prophecy ≥70%
- ✅ **No systematic errors**: Errors are random, not patterned
- ✅ **Improvement over v1.0**: At least +10-15% accuracy gain (v1.0: 60-70%, v2.0: 75-85%)

---

## Implementation Plan (Option B)

### Step 1: Genre Classification (30 minutes)

**Task**: Tag all 215 TBTA verses by genre
**Method**: Use book codes from Algorithm v2.0 Rule 0
- Epistle: EPH, PHP, COL, 1TH, 2TH, 1TIM, 2TIM, TIT, PHM, HEB, JAS, 1PE, 2PE, 1JN, 2JN, 3JN, JUD, ROM, 1CO, 2CO, GAL
- Poetry/Wisdom: PSA, PRO, ECC, SNG, JOB, LAM
- Prophecy: ISA, JER, EZE, DAN, HOS, JOL, AMO, OBA, JON, MIC, NAH, HAB, ZEP, HAG, ZEC, MAL
- Narrative: All others (GEN, EXO, LEV, NUM, DEU, JOS, JDG, RUT, 1SA, 2SA, 1KI, 2KI, 1CH, 2CH, EZR, NEH, EST, MAT, MRK, LUK, JHN, ACT, REV)

**Output**: `test-set-genre-classification.yaml` (215 verses with genre tags)

---

### Step 2: Stratified Random Sampling (1 hour)

**Task**: Select 15 verses with genre stratification
**Method**:
1. Exclude 12 v1.0 test verses
2. Random sample within each stratum:
   - Narrative: 8 verses (random from 150+ narrative verses)
   - Epistle: 5 verses (random from 40+ epistle verses, ensure Ephesians, 2 John)
   - Poetry: 2 verses (random from 15+ poetry verses)
   - Prophecy: 1 verse (random from 10+ prophecy verses)
3. Use Python `random.seed(2025)` for reproducibility
4. Document sampling process in `test-set-sampling-methodology.md`

**Output**:
- `test-set-v2.0-sample.yaml` (15 verses with metadata: book, chapter, verse, genre)
- `test-set-sampling-methodology.md` (reproducible sampling steps)

---

### Step 3: Blind Prediction with Algorithm v2.0 (2-3 hours)

**Task**: Apply Algorithm v2.0 to 15 test verses WITHOUT accessing TBTA
**Method**:
1. For each verse:
   - Read verse text from Bible translation (NET, NIV)
   - Extract participants manually (text-based, not TBTA)
   - Apply Algorithm v2.0 rules (genre detection → interrogative → generic → frame inferable → first mention/routine)
   - Record predictions in `predictions-v2.0.yaml`
2. **NO TBTA ACCESS** during this phase
3. Commit predictions to git: `git commit -m "Blind predictions for v2.0 validation"`
4. Push to GitHub for timestamp verification: `git push`

**Output**:
- `predictions-v2.0.yaml` (verse, participant, predicted_state, justification)
- Git commit hash (proves predictions made before validation)

---

### Step 4: Validation and Accuracy Calculation (1 hour)

**Task**: Compare v2.0 predictions to TBTA ground truth
**Method**:
1. Load TBTA files for 15 test verses
2. Extract ground truth participant states
3. Compare prediction vs. ground truth for each participant
4. Calculate metrics:
   - Overall accuracy (correct predictions / total participants)
   - Per-genre accuracy (narrative, epistle, poetry, prophecy)
   - Per-state accuracy (Routine, Generic, Frame Inferable, First Mention, Interrogative)
   - Confusion matrix (which states confused with which)
5. Error analysis: Identify systematic patterns in errors

**Output**:
- `validation-results-v2.0.md` (accuracy metrics, confusion matrix, error analysis)
- `comparison-v1.0-vs-v2.0.md` (side-by-side comparison)

---

### Step 5: Decision Point (30 minutes)

**Based on v2.0 accuracy**:

- ✅ **If ≥85%**: Mark as PRODUCTION-READY
  - Proceed to Stage 6 (peer review)
  - Document in TODO.md: "v2.0 validated at X% accuracy, production-ready"

- ⚠️ **If 80-84%**: CONDITIONAL APPROVAL
  - Mark as "production consideration" (acceptable but monitor)
  - Identify top 2-3 error patterns for v2.1 refinement
  - Defer v2.1 to future session

- ❌ **If <80%**: REFINE TO v2.1 or v3.0
  - Conduct detailed error analysis
  - Identify which of the 3 fixes failed (epistolary abstracts, quantifier+definite, recognition frame)
  - Design v2.1 with targeted fixes
  - Re-test on same 15 verses (now becomes training set)

**Output**: `decision-v2.0-production.md` (production readiness assessment)

---

## Resources Needed

### Time Estimate
- **Total**: 2 sessions, 4.5-5.5 hours
- Session 1: Genre classification (30 min) + Stratified sampling (1 hour)
- Session 2: Blind prediction (2-3 hours) + Validation (1 hour) + Decision (30 min)

### Tools Required
- Python (for random sampling, genre classification)
- TBTA data access (for validation phase only)
- Git (for blind prediction commit)
- YAML parsing (for reading TBTA files)

### Data Requirements
- List of 215 TBTA verses (from existing TBTA corpus)
- Bible text (NET or NIV translation)
- TBTA ground truth files (commentary/BOOK/chapter/verse.yaml)

---

## Conclusion

**RECOMMENDED: Option B - Random Stratified Sample (15 verses)**

**Key justification**:
1. Methodologically rigorous (blind random sampling)
2. Genre-diverse (tests v2.0's epistolary fix + narrative baseline)
3. Resource-efficient (1-2 sessions, achievable)
4. Comparable to v1.0 (same scale, direct accuracy comparison)
5. Production-representative (realistic genre distribution)

**Next steps**:
1. Approve Option B strategy
2. Execute Step 1: Genre classification (30 min)
3. Execute Step 2: Stratified sampling (1 hour)
4. Execute Step 3: Blind prediction (2-3 hours)
5. Execute Step 4: Validation (1 hour)
6. Execute Step 5: Production decision (30 min)

**Timeline**: 2 sessions (4.5-5.5 hours total)

---

**Last updated**: 2025-11-15
**Status**: Strategy analysis complete, awaiting approval
**Next action**: User approval → Execute Step 1 (genre classification)
