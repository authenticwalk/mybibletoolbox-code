# TBTA Feature Validation: Standard Methodology (Adversarial Approach)

**Version**: 1.0
**Date**: 2025-11-07
**Status**: APPROVED - Use this for all feature experiments until full merge

---

## Philosophy: Adversarial Testing at Early Phase

**Why adversarial at this stage?**
- We're learning TBTA's methodology (reverse-engineering)
- Need to find edge cases and limitations quickly
- Small focused tests more valuable than large random samples
- Can iterate rapidly on specific challenges
- Builds robust patterns that handle hard cases

**Later phase (post-feature-merge):**
- Switch to large representative samples (200+ verses)
- Comprehensive cross-validation
- Statistical rigor for publication

---

## The Adversarial Validation Protocol

### Phase 1: Pattern Discovery (Training Set)

**Size**: 15-20 verses (small, focused)

**Selection criteria:**
```
Pick verses that cover:
✅ All possible feature values (ensure complete coverage)
✅ Clear, unambiguous cases (build confidence)
✅ 1-2 theological contexts (Trinity, incarnation, etc.)
✅ Morphological diversity (Hebrew and Greek)
✅ Different discourse contexts (narrative, poetry, epistles)
```

**Process:**
1. Select training verses and commit list to git
2. Analyze TBTA annotations freely (no restrictions)
3. Document patterns discovered
4. Build initial algorithm
5. Iterate until 90%+ accuracy on training set
6. Lock algorithm with version number

**Output:**
- `features/[feature]/TRAINING-SET.md` - List of training verses
- `features/[feature]/PATTERNS-LEARNED.md` - Documented patterns
- `features/[feature]/ALGORITHM-v1.md` - Locked algorithm

---

### Phase 2: Adversarial Testing (Test Set)

**Size**: 10-15 verses (small but challenging)

**Selection criteria - ACTIVELY HUNT FOR EDGE CASES:**
```
Pick verses specifically designed to break your algorithm:

🎯 Theological edge cases (25%)
   - Trinity contexts (Gen 1:26, Matt 28:19)
   - Incarnation contexts (John 1:14)
   - Messianic prophecies
   - Corporate solidarity (Israel as one/many)

🎯 Rare feature values (25%)
   - Values that appeared 0-1 times in training
   - Theoretical values (quadrial, excessive degree, etc.)
   - Boundary cases (dual vs. plural, comparative vs. superlative)

🎯 Morphological exceptions (25%)
   - Semantic ≠ morphological cases
   - Fossilized forms (shamayim, mayim)
   - Analytic vs synthetic constructions
   - Suppletive forms (irregular morphology)

🎯 Ambiguous cases (25%)
   - Multiple valid interpretations
   - Translation divergence (versions disagree)
   - Context-dependent resolution
   - Discourse boundary cases
```

**Process:**
1. Design adversarial test set (commit list to git)
2. Make predictions WITHOUT checking TBTA
3. Document reasoning for each prediction
4. Rate confidence: High (90%+), Medium (70-90%), Low (<70%)
5. Commit predictions to git with timestamp
6. Lock predictions (no modifications allowed)
7. Check TBTA and calculate accuracy
8. Analyze failures in detail

**Expected accuracy:**
- High confidence predictions: 85%+ (if lower, algorithm has problems)
- Medium confidence: 60-75% (acceptable for edge cases)
- Low confidence: 40-60% (expected for ambiguous cases)
- Overall: 60-70% (if higher, test wasn't adversarial enough!)

**Output:**
- `features/[feature]/ADVERSARIAL-TEST-SET.md` - Challenging verses
- `features/[feature]/PREDICTIONS-v1-locked.md` - Locked predictions (commit SHA)
- `features/[feature]/RESULTS-adversarial.md` - Accuracy and analysis

---

### Phase 3: Random Validation (Baseline Test)

**Size**: 10-15 verses (random sample)

**Selection criteria:**
```
Random sample from:
✅ Different books (not in training or adversarial)
✅ Stratified by feature value (representative distribution)
✅ Mix of OT and NT
✅ No special selection bias
```

**Process:**
1. Random selection (commit with random seed)
2. Make predictions WITHOUT checking TBTA
3. Commit predictions to git
4. Lock predictions
5. Check TBTA and calculate accuracy

**Expected accuracy:**
- Should be HIGHER than adversarial test (80-90%)
- If lower than adversarial, algorithm has serious issues
- If same as adversarial, test sets not properly designed

**Output:**
- `features/[feature]/RANDOM-TEST-SET.md` - Random verses
- `features/[feature]/PREDICTIONS-v1-random.md` - Locked predictions
- `features/[feature]/RESULTS-random.md` - Accuracy comparison

---

### Phase 4: Error Analysis & Algorithm Refinement

**Process:**
1. Analyze adversarial test failures
2. Categorize errors:
   - Algorithm limitation (need new rule)
   - Edge case (document as translator choice point)
   - Potential TBTA error (flag for review)
   - Ambiguous (genuinely uncertain)
3. Document learnings
4. Update algorithm to v2.0
5. DO NOT retest on same verses
6. Save learnings for next feature

**Criteria for flagging TBTA errors:**
```
Flag as potential TBTA error ONLY if:
✅ High confidence prediction (90%+)
✅ 3+ independent sources support prediction
✅ Exhaustive debugging completed (6-step process)
✅ No plausible alternative explanation
✅ Pattern is consistent across similar cases

Expected: 1-5% of adversarial test cases
If 0%: Being too lenient (confirmation bias)
If >10%: Being too strict or algorithm is wrong
```

**Output:**
- `features/[feature]/ERROR-ANALYSIS-v1.md` - Detailed error breakdown
- `features/[feature]/ALGORITHM-v2.md` - Updated algorithm
- `features/[feature]/LEARNINGS.md` - Insights for other features

---

## File Structure Template

```
plan/tbta-rebuild-with-llm/features/[feature]/
├── README.md                          # Feature overview, TBTA values, plan status
├── METHODOLOGY-STATUS.md              # Current phase, next steps
│
├── training/
│   ├── TRAINING-SET.md                # List of 15-20 training verses
│   ├── PATTERNS-LEARNED.md            # Documented patterns from TBTA
│   └── ALGORITHM-v1.md                # Locked algorithm (git SHA)
│
├── adversarial-test/
│   ├── ADVERSARIAL-TEST-SET.md        # 10-15 challenging verses
│   ├── PREDICTIONS-v1-locked.md       # Predictions (git SHA)
│   ├── RESULTS-adversarial.md         # Accuracy: 60-70% expected
│   └── ERROR-ANALYSIS-v1.md           # Detailed failure analysis
│
├── random-test/
│   ├── RANDOM-TEST-SET.md             # 10-15 random verses
│   ├── PREDICTIONS-v1-random.md       # Predictions (git SHA)
│   └── RESULTS-random.md              # Accuracy: 80-90% expected
│
└── potential-errors/
    └── [case-by-case-files].md        # Flagged TBTA errors (1-5%)
```

---

## Validation Checklist

Before claiming success for any feature:

### Data Integrity
- [ ] Training set selected and committed before analysis
- [ ] Adversarial test set designed with edge cases
- [ ] Random test set selected with random seed
- [ ] No overlap between training and test sets
- [ ] All sets committed to git before predictions

### Prediction Integrity
- [ ] Predictions made WITHOUT seeing TBTA test data
- [ ] Predictions committed with timestamp (SHA recorded)
- [ ] Confidence ratings documented
- [ ] Reasoning provided for each prediction
- [ ] No modifications after checking TBTA

### Algorithm Integrity
- [ ] Algorithm version locked before testing
- [ ] Decision rules explicitly documented
- [ ] Git commit SHA recorded
- [ ] No changes to algorithm after test predictions

### Analysis Integrity
- [ ] Adversarial accuracy: 60-70% (if higher, test not hard enough)
- [ ] Random accuracy: 80-90% (should exceed adversarial)
- [ ] Error analysis completed for failures
- [ ] Potential TBTA errors flagged with justification (1-5%)
- [ ] Learnings documented for future features

### Reporting Integrity
- [ ] Methodology clearly described
- [ ] Sample sizes and selection criteria reported
- [ ] Both adversarial and random accuracy reported
- [ ] Confidence calibration checked
- [ ] Limitations acknowledged
- [ ] No retroactive accuracy claims

---

## Success Metrics by Phase

### Training Phase (Pattern Discovery)
- ✅ Success: 90%+ accuracy on training set
- ⚠️ Review: 70-90% accuracy (need more patterns)
- ❌ Fail: <70% accuracy (fundamental misunderstanding)

### Adversarial Test
- ✅ Success: 60-70% accuracy (robust to edge cases)
- ⚠️ Review: 50-60% accuracy (algorithm has gaps)
- ❌ Fail: <50% accuracy (algorithm too simplistic)

### Random Test
- ✅ Success: 80-90% accuracy (patterns generalize)
- ⚠️ Review: 70-80% accuracy (some overfitting)
- ❌ Fail: <70% accuracy (serious problems)

### Comparative Metric (Critical!)
- ✅ Success: Random > Adversarial by 15-25 percentage points
- ⚠️ Review: Random > Adversarial by 5-15 points (test design issue)
- ❌ Fail: Random ≤ Adversarial (test sets not properly designed)

---

## Example: Number Systems Feature (Retrofitted)

### Current Status
- Training phase: 35 verses analyzed → 91.4% initial accuracy
- Patterns learned: Semantic over morphological, Trinity=Trial, discourse role
- Algorithm locked: v1.0 (documented in PATTERNS-LEARNED.md)

### Next Steps
1. Design adversarial test (10 verses):
   - 3 theological edge cases (Trinity variants)
   - 2 rare values (trial, paucal contexts)
   - 3 morphological exceptions (more dual forms)
   - 2 ambiguous cases (corporate solidarity)

2. Design random test (10 verses):
   - Random selection from Genesis 2-3, Matthew 6-7, John 4-5
   - Stratified by number value

3. Predict both sets (commit before checking TBTA)

4. Expected results:
   - Adversarial: ~65% (challenging cases)
   - Random: ~85% (patterns should generalize)

---

## Timeline for Each Feature

**Week 1: Training Phase**
- Days 1-2: Select training verses, commit
- Days 3-5: Analyze TBTA, document patterns
- Days 6-7: Build algorithm, test on training set

**Week 2: Testing Phase**
- Day 8: Design adversarial + random test sets
- Day 9: Make predictions, commit and lock
- Day 10: Check TBTA, calculate accuracy
- Days 11-12: Error analysis, document learnings
- Days 13-14: Update algorithm v2.0

**Total per feature: 2 weeks**

With 17 features identified, estimated completion: 34 weeks (8 months)
Can parallelize some features to reduce timeline.

---

## When to Switch to Large-Scale Validation

**Trigger for switching approaches:**
```
After completing adversarial validation for ALL features:
✅ All 17 features have algorithm v2.0+
✅ Common patterns identified across features
✅ Ready for comprehensive validation
✅ Preparing for publication/release

Then switch to:
- 200+ verse sample per feature
- Proper train/val/test split (60/20/20)
- Cross-validation approach
- Statistical rigor
- Confidence intervals
- Inter-rater reliability studies
```

---

## Integration with CROSS-FEATURE-LEARNINGS.md

After each feature completion:

1. **Update cross-feature learnings**
   - Add patterns that apply to multiple features
   - Document exceptions to universal principles
   - Note feature-specific edge cases

2. **Propagate learnings**
   - Review older features with new insights
   - Update algorithms if pattern applies broadly
   - Retest if major pattern discovered

3. **Build knowledge base**
   - Common error types across features
   - Theological contexts requiring special handling
   - Morphological vs semantic conflicts
   - Rare values that never appear

---

## Automation Recommendations

### Script: adversarial-test-generator.py
```python
# Suggests adversarial test cases for a feature
# Based on training set analysis and known edge case types

python scripts/adversarial-test-generator.py \
  --feature number \
  --training-results training/PATTERNS-LEARNED.md \
  --suggest-count 10

# Output: Suggested verses that challenge the algorithm
```

### Script: validate-methodology.py
```python
# Checks that methodology was followed correctly

python scripts/validate-methodology.py \
  --feature number \
  --check-all

# Validates:
# - Training/test separation
# - Predictions locked before TBTA access
# - No retroactive modifications
# - Proper git commit history
```

---

## Summary: The Adversarial Advantage

**Why this approach works for early phase:**

1. **Fast iteration**: 15-20 training + 10 adversarial + 10 random = 35-40 verses total
2. **High signal**: Edge cases reveal algorithm weaknesses quickly
3. **Robust patterns**: If it handles adversarial cases, it'll handle normal cases
4. **Clear metrics**: Random should beat adversarial by 15-25 points
5. **Honest validation**: Adversarial accuracy of 60-70% is realistic, not inflated

**Comparison to naive approach:**
- ❌ Large random sample → Hides weaknesses, expensive, slow
- ❌ All easy cases → Inflated accuracy, false confidence
- ✅ Adversarial + random → Reveals limitations, builds robust algorithm

**The key insight:**
> If your algorithm gets 65% on adversarial cases and 85% on random cases,
> it's MUCH more trustworthy than 90% on an easy random sample.

---

**Status**: APPROVED for all TBTA feature experiments
**Next**: Apply to number-systems (retrofit), degree (new), and all remaining features
