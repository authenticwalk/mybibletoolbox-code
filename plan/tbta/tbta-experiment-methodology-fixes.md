# TBTA Experiment Methodology: Fixes and Best Practices

**Date**: 2025-11-07
**Purpose**: Provide concrete fixes for the experimental methodology while preserving the valuable reverse-engineering work

---

## The Core Principle: Train/Test Separation

**You CAN use TBTA data for validation** - that's the whole point. But you MUST separate:
- **Training data**: Where you learn patterns from TBTA (allowed to analyze)
- **Test data**: Where you validate your learned patterns (predict first, check later)

---

## Quick Fix: Minimal Changes to Current Work

### Option 1: Lock and Validate ⚡ (Easiest)

**What to do NOW with existing work:**

```markdown
Step 1: Acknowledge Current Status
- Experiment 001 (number-systems): This is now TRAINING DATA
- Original accuracy: 91.4% (before learning)
- Post-learning: 100% explainability (learned from these verses)
- Status: Algorithm development phase, not validation

Step 2: Document Learned Patterns
Create: plan/tbta-rebuild-with-llm/features/number/LEARNED-PATTERNS.md
- Pattern 1: Semantic over morphological (learned from Gen 1:1-2, Matt 5:3)
- Pattern 2: Trinity = Trial (learned from Gen 1:26)
- Pattern 3: Discourse role affects number (learned from John 3:2)
- Pattern 4: LXX/Vulgate provide semantic interpretation
- Pattern 5: Fossilized duals (shamayim, mayim) → singular

Step 3: Lock the Algorithm
Create: plan/tbta-rebuild-with-llm/features/number/ALGORITHM-V1.md
- Document EXACT decision rules based on learned patterns
- No more changes allowed after this point
- Version and date it: "Algorithm v1.0, locked 2025-11-07"

Step 4: Create Validation Set (NEW VERSES)
Select 30 verses NOT in experiment-001:
- Genesis 2:1-10 (10 verses)
- Matthew 6:1-10 (10 verses)
- John 4:1-10 (10 verses)

Step 5: Make Predictions WITHOUT Looking at TBTA
- Apply Algorithm v1.0 to all 30 validation verses
- Document predictions in writing (commit to git)
- Include reasoning for each prediction
- DO NOT check TBTA yet

Step 6: Lock Predictions
- Git commit with message: "Number feature validation predictions - DO NOT MODIFY"
- This proves predictions were made before seeing TBTA data

Step 7: Check TBTA and Calculate Accuracy
- Now retrieve TBTA annotations for the 30 verses
- Compare against locked predictions
- Calculate accuracy: matches/total
- This is your TRUE validation accuracy

Step 8: Report Honestly
- Training set (35 verses): 91.4% initial, 100% after learning
- Validation set (30 verses): X% accuracy (report actual number)
- If validation is 85%+, the patterns generalize well
- If validation is <70%, patterns overfit to training data
```

**Timeline**: 1-2 days
**Effort**: Low
**Validation strength**: Moderate (small test set, post-hoc separation)

---

### Option 2: Proper Experimental Design 🔬 (Better)

**Start fresh with rigorous methodology:**

```markdown
Phase 1: Sampling Strategy
Create stratified sample:
- Books: 5 OT books, 5 NT books (diverse genres)
- Features: Ensure all number values represented
- Difficulty: Mix of clear cases and edge cases

Total sample: 200 verses
- Training: 120 verses (60%)
- Validation: 40 verses (20%)
- Final test: 40 verses (20%)

Phase 2: Initial Split (BEFORE any analysis)
Randomly assign verses to sets:
- Document split in: data/splits/number-feature-split.yaml
- Commit to git with timestamp
- NEVER change assignments

Example split file:
```yaml
feature: number
split_date: 2025-11-07
random_seed: 42

training_set:
  - GEN.001.001
  - GEN.001.002
  - ...

validation_set:
  - GEN.002.001
  - GEN.002.002
  - ...

test_set:
  - GEN.003.001
  - GEN.003.002
  - ...
```

Phase 3: Training Phase
- Analyze TBTA annotations for training set ONLY
- Develop algorithm iteratively
- Test hypotheses, refine patterns
- Document all learnings
- No restrictions on training set analysis

Phase 4: Validation Phase (Checkpoint)
- Lock algorithm version: "Algorithm v1.0"
- Make predictions on validation set
- Commit predictions to git BEFORE checking TBTA
- Check TBTA and calculate accuracy
- If accuracy <80%, iterate on algorithm (back to Phase 3)
- If accuracy 80%+, proceed to final test

Phase 5: Final Test (One Shot)
- Lock algorithm version: "Algorithm v2.0" (or v1.0 if no iteration)
- Make predictions on test set
- Commit predictions to git BEFORE checking TBTA
- Check TBTA and calculate accuracy
- This is your reported accuracy
- NO iteration allowed after this point

Phase 6: Error Analysis (Post-test)
- Analyze test set errors
- Document learnings for next feature
- Update algorithm for v3.0
- But reported accuracy remains from Phase 5
```

**Timeline**: 1-2 weeks
**Effort**: Moderate
**Validation strength**: High (proper train/val/test split)

---

### Option 3: Cross-Validation Approach 🔄 (Most Rigorous)

**For when you have limited data:**

```markdown
Setup: 5-Fold Cross-Validation
Divide data into 5 equal folds (~40 verses each)
- Fold 1: Genesis 1-5
- Fold 2: Genesis 6-10
- Fold 3: Matthew 5-7
- Fold 4: Matthew 8-10
- Fold 5: John 1-5

Process:
Round 1: Train on Folds 2-5, Test on Fold 1
Round 2: Train on Folds 1,3,4,5, Test on Fold 2
Round 3: Train on Folds 1,2,4,5, Test on Fold 3
Round 4: Train on Folds 1,2,3,5, Test on Fold 4
Round 5: Train on Folds 1,2,3,4, Test on Fold 5

For each round:
1. Develop algorithm using training folds
2. Lock algorithm
3. Predict on test fold (without looking at TBTA)
4. Commit predictions
5. Check TBTA and calculate accuracy

Final accuracy: Average of 5 rounds

Benefits:
- Every verse gets tested exactly once
- 80% of data available for training in each round
- More robust accuracy estimate
- Shows if patterns generalize across different books

Challenges:
- 5x the work
- Need consistent algorithm across rounds
- More complex to manage
```

**Timeline**: 2-3 weeks
**Effort**: High
**Validation strength**: Very high (robust to sampling variation)

---

## Alternative Approaches

### Approach A: Dual-Purpose Design 🎯

**Separate reverse-engineering from validation:**

```markdown
Track 1: TBTA Methodology Analysis (Current work)
Goal: Understand how TBTA annotates
Method: Analyze TBTA data freely, document patterns
Output: "TBTA Annotation Methodology Guide"
Success: Can explain TBTA's decisions
No accuracy requirements - this is documentation

Track 2: Independent Algorithm Validation (New work)
Goal: Test if learned patterns generalize
Method: Proper train/test split on NEW data
Output: "Number Feature Algorithm Performance Report"
Success: 80%+ accuracy on held-out test set
Rigorous experimental standards

Benefits:
- Track 1 is already done and valuable
- Track 2 provides scientific validation
- No need to discard existing work
- Clear separation of purposes
```

**Example structure:**
```
plan/tbta-rebuild-with-llm/
├── methodology-analysis/          # Track 1
│   ├── number-systems/
│   │   ├── patterns-discovered.md  # What you learned from TBTA
│   │   ├── example-cases.md        # Analyzed examples
│   │   └── annotation-rules.md     # Documented TBTA rules
│   └── degree/
│       └── ...
└── algorithm-validation/          # Track 2
    ├── number-systems/
    │   ├── train-set.yaml          # Training verses
    │   ├── test-set.yaml           # Test verses (separate)
    │   ├── predictions.md          # Locked predictions
    │   └── results.md              # Accuracy report
    └── degree/
        └── ...
```

---

### Approach B: Progressive Validation 📊

**Build confidence gradually:**

```markdown
Level 1: Spot Check (Quick validation)
- Pick 10 random verses NOT in training
- Make predictions
- Check accuracy
- If 8/10 correct (80%), proceed to Level 2
- If <8/10, refine algorithm

Level 2: Representative Sample
- Pick 30 verses across different books/genres
- Ensure coverage of all number values
- Make predictions, commit, check
- If 24/30 correct (80%), proceed to Level 3
- If <24/30, analyze errors and refine

Level 3: Comprehensive Test
- 100 verses held-out test set
- Final locked algorithm
- One-shot prediction and validation
- Report accuracy as official result

Benefits:
- Catch major errors early (Level 1)
- Refine before final test (Level 2)
- Final test is rigorous (Level 3)
- Efficient use of time
```

---

### Approach C: Adversarial Testing 🥊

**Actively try to break your algorithm:**

```markdown
Phase 1: Learn Patterns (Training Set)
- Analyze TBTA on 60% of data
- Document patterns
- Create algorithm

Phase 2: Edge Case Hunting
Select test verses specifically designed to challenge:
- Theological edge cases (Trinity, incarnation)
- Rare values (trial, quadrial, paucal)
- Ambiguous cases (could go either way)
- Cross-linguistic challenges
- Morphological exceptions

Phase 3: Adversarial Prediction
- Predict on edge cases WITHOUT checking TBTA
- Expected: Lower accuracy than random sample
- If you still get 70%+, algorithm is robust

Phase 4: Random Test Set
- Also test on 40 random verses
- Should get higher accuracy than edge cases
- Proves algorithm works on typical cases

Report both:
- Random test accuracy: X%
- Adversarial test accuracy: Y%

Benefits:
- Tests robustness
- Identifies algorithm weaknesses
- More confidence in deployment
```

---

### Approach D: Incremental Disclosure 🔓

**Gradually reveal TBTA data:**

```markdown
Setup: Blind Prediction Challenge
Have a partner (or automated system) hold TBTA data

Round 1: No hints
- Make predictions on 10 verses
- Submit predictions
- Receive only: "X/10 correct" (no details)

Round 2: Minimal feedback
- Make predictions on 10 new verses
- Submit predictions
- Receive: "X/10 correct, errors on verses 3, 7, 9"
- Can refine algorithm but don't see TBTA answers yet

Round 3: Value-level feedback
- Make predictions on 10 new verses
- Submit predictions
- Receive: "8/10 correct, verse 3: expected S got N, verse 7: expected T got P"
- Can refine algorithm based on value types

Round 4: Full disclosure
- Make predictions on 10 new verses
- Submit predictions
- Receive full TBTA annotations
- Analyze thoroughly

Round 5: Final test
- Make predictions on 50 new verses
- Submit predictions (locked)
- Receive results
- This is reported accuracy

Benefits:
- Forces learning from minimal feedback
- Prevents overfitting to specific examples
- More realistic to real-world deployment
```

---

## Recommended Workflow for Future Features

### The Standard Protocol 📋

For each new TBTA feature (degree, person, proximity, etc.):

```markdown
Step 1: Sampling (Day 1)
- Collect 100-200 verses where feature applies
- Stratify by book, value type, difficulty
- Split: 60% train, 20% validation, 20% test
- Document split in YAML file
- Commit and lock split

Step 2: Training Phase (Days 2-7)
- Analyze TBTA on training set only
- Develop initial algorithm
- Document patterns and rules
- Test hypotheses freely
- Output: Algorithm v1.0

Step 3: Validation Checkpoint (Day 8)
- Lock algorithm v1.0
- Predict on validation set (commit predictions first)
- Check TBTA, calculate accuracy
- If <80%, iterate (back to Step 2 with v1.1, v1.2, etc.)
- If 80%+, proceed to final test

Step 4: Final Test (Day 9)
- Lock final algorithm version
- Predict on test set (commit predictions first)
- Check TBTA, calculate accuracy
- Report this as official accuracy
- No iteration after this point

Step 5: Documentation (Day 10)
- Write up methodology
- Document patterns learned
- Report accuracy with confidence intervals
- Identify edge cases and limitations
- Publish results

Step 6: Error Analysis (Post-publication)
- Analyze test errors
- Update algorithm for v2.0
- But don't retest on same data
- Use learnings for next feature
```

**Success criteria:**
- ✅ Train/test separation maintained
- ✅ Predictions committed before checking TBTA
- ✅ Accuracy reported on truly held-out data
- ✅ Process documented and reproducible
- ✅ Limitations acknowledged

---

## Specific Fixes for Current Experiments

### Fix for Number Systems (Completed Experiment)

```markdown
Current status: 35 verses analyzed, patterns learned, 91.4% → 100% claimed

Recommendation: Reframe as methodology analysis
1. Rename experiment-001.md → methodology-analysis-001.md
2. Change header:
   FROM: "Experiment 001: Number Annotation Reproduction Test"
   TO: "Methodology Analysis 001: Understanding TBTA Number Annotations"
3. Update accuracy claims:
   FROM: "100% accuracy achieved"
   TO: "91.4% prediction accuracy, 100% explainability after analysis"
4. Add validation section:
   "This analysis identified patterns from 35 verses.
    Validation on independent test set required to confirm generalization.
    See validation-001.md for held-out test results."

Then create validation-001.md:
1. Select 30 NEW verses (not in the 35)
2. Apply learned patterns
3. Make predictions (commit to git first)
4. Check TBTA
5. Report accuracy
6. This is your validation accuracy
```

### Fix for Degree Experiment (Not Yet Tested)

```markdown
Current status: Predictions made, awaiting TBTA data

This is actually PERFECT timing! You can do it right:

Step 1: Split the Verses BEFORE Checking TBTA
Current verse list in experiment-001.md:
- Training set: Verses 1-8 (develop algorithm)
- Test set: Verses 9-12 (validate algorithm)

Step 2: Check TBTA for Training Set ONLY
- Access TBTA for verses 1-8
- Analyze patterns
- Refine hypotheses
- Update predictions if needed

Step 3: Lock Algorithm
- Document decision rules
- Commit to git
- No more changes

Step 4: Apply to Test Set
- Use locked algorithm on verses 9-12
- Make predictions WITHOUT checking TBTA
- Commit predictions

Step 5: Check TBTA for Test Set
- Retrieve annotations
- Calculate accuracy
- Report honestly

This gives you:
- 8 verses for learning (training)
- 4 verses for validation (test)
- Proper methodology from the start
```

---

## Statistical Best Practices

### Sample Size Recommendations

```markdown
Minimum viable:
- Training: 20 verses
- Validation: 10 verses
- Test: 10 verses
- Total: 40 verses minimum

Recommended:
- Training: 60 verses
- Validation: 20 verses
- Test: 20 verses
- Total: 100 verses

Ideal:
- Training: 120 verses
- Validation: 40 verses
- Test: 40 verses
- Total: 200 verses

Note: Depends on feature complexity and value distribution
```

### Confidence Intervals

```markdown
Report accuracy with confidence intervals:

Example:
"Number feature algorithm achieved 85% accuracy
(95% CI: 76%-92%) on held-out test set of 40 verses"

Calculation (Wilson score interval):
- For 34/40 correct (85%)
- 95% CI: 76%-92%
- Shows uncertainty due to small sample size

Don't claim: "85% accuracy, proven to work"
Do claim: "85% accuracy (76%-92% CI), suggests patterns generalize"
```

### When to Flag Potential TBTA Errors

```markdown
Criteria for flagging (all must be met):
1. Algorithm confidence: 90%+ certain of prediction
2. Multiple independent sources agree with prediction
3. Exhaustive debugging completed (6 steps)
4. No plausible alternative explanation
5. Pattern is consistent across similar cases

Then and only then: Flag as potential TBTA error

Expected rate: 1-5% of test cases
If you find 0%: Methodology problem (too lenient)
If you find >10%: Methodology problem (too strict) or algorithm issue
```

---

## Tools and Automation

### Suggested Scripts

```bash
# scripts/create-split.py
# Creates train/val/test split and locks it

python scripts/create-split.py \
  --feature number \
  --total-verses 100 \
  --train-ratio 0.6 \
  --val-ratio 0.2 \
  --test-ratio 0.2 \
  --random-seed 42 \
  --output data/splits/number-split.yaml

# Outputs:
# - YAML file with verse assignments
# - Commits to git with timestamp
# - Prevents future modification
```

```bash
# scripts/lock-predictions.py
# Commits predictions before checking TBTA

python scripts/lock-predictions.py \
  --feature number \
  --split test \
  --predictions-file predictions.md

# Outputs:
# - Git commit with message: "LOCKED: Number feature test predictions"
# - SHA hash for verification
# - Prevents modification
```

```bash
# scripts/calculate-accuracy.py
# Compares locked predictions with TBTA

python scripts/calculate-accuracy.py \
  --feature number \
  --predictions predictions.md \
  --tbta-data tbta-annotations.yaml \
  --output results.md

# Outputs:
# - Accuracy percentage
# - Confidence interval
# - Confusion matrix
# - Error analysis
```

### Validation Checklist

```markdown
Before claiming validation success:

Data integrity:
- [ ] Train/test split documented and committed before analysis
- [ ] Split ratios appropriate (at least 20% for test)
- [ ] No data leakage between sets
- [ ] Stratified sampling for balanced representation

Prediction integrity:
- [ ] Predictions made without seeing TBTA test data
- [ ] Predictions committed to git with timestamp
- [ ] No modifications after TBTA data accessed
- [ ] Reasoning documented for each prediction

Analysis integrity:
- [ ] Accuracy calculated on held-out test set
- [ ] Confidence intervals reported
- [ ] Error analysis completed
- [ ] Limitations acknowledged

Reporting integrity:
- [ ] Methodology clearly described
- [ ] Sample sizes reported
- [ ] Distinction between training and test accuracy
- [ ] No retroactive claims of accuracy
```

---

## Template Documents

### Template: Validation Report

```markdown
# [Feature] Feature Validation Report

**Date**: YYYY-MM-DD
**Algorithm Version**: v1.0
**Test Set**: [Description]

## Methodology

### Data Split
- Training set: [N] verses from [books/chapters]
- Validation set: [N] verses from [books/chapters]
- Test set: [N] verses from [books/chapters]
- Split committed: [git SHA]

### Algorithm Development
- Patterns learned: [List key patterns]
- Training accuracy: [X]%
- Validation accuracy: [Y]%
- Algorithm locked: [date and git SHA]

## Test Results

### Predictions
- Predictions committed: [git SHA]
- Date: [YYYY-MM-DD]
- [Link to predictions file]

### Accuracy
- Test set accuracy: [Z]% ([CI_low]%-[CI_high]% 95% CI)
- Breakdown by value:
  - Value N: [accuracy]
  - Value C: [accuracy]
  - etc.

### Error Analysis
[Detailed analysis of errors]

### Limitations
[Honest assessment of limitations]

## Conclusion
[Summary and interpretation]
```

---

## Summary: What to Do Right Now

### Immediate Actions (Next 24 hours):

1. **Reframe existing work**
   - Change "100% accuracy" to "100% explainability after analysis"
   - Label as "methodology analysis" not "validation"
   - Acknowledge this was algorithm development

2. **Set up proper validation for number feature**
   - Select 30 new verses (not in the original 35)
   - Commit the list to git
   - Make predictions using learned patterns
   - Lock predictions (git commit)
   - Then check TBTA and report accuracy

3. **Fix degree experiment before it's too late**
   - Split existing verses into train/test BEFORE checking TBTA
   - Check TBTA for training set only
   - Lock algorithm
   - Predict on test set
   - Then check TBTA for test set

### Medium-term (Next week):

4. **Create standard protocol**
   - Write up the methodology for all future features
   - Create train/val/test split template
   - Build validation checklist

5. **Implement for one feature end-to-end**
   - Choose a new feature (not number or degree)
   - Follow the protocol exactly
   - Document everything
   - Report results honestly
   - Use as template for others

### Long-term (Next month):

6. **Validate all features properly**
   - Work through each TBTA feature
   - Proper methodology for each
   - Build confidence in the approach
   - Create comprehensive validation suite

---

## Bottom Line

You absolutely CAN use TBTA data for validation - that's the point! The fix is simple:

**BEFORE you check TBTA for a verse:**
1. Make your prediction
2. Write it down
3. Commit it to git
4. THEN check TBTA

**Do this for test data only. Training data can be analyzed freely.**

This single change fixes everything. The rest is about being systematic and honest about it.
