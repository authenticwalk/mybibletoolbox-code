# Number Systems Feature: Methodology Status

**Current Phase**: Training Complete → Adversarial Validation Next
**Algorithm Version**: v1.0 (locked from experiment-001)
**Last Updated**: 2025-11-07

---

## Methodology Acknowledgment

### What Experiment-001 Actually Was

**Original claim**: "Validation experiment achieving 100% accuracy"

**Actual status**: **Training phase / Pattern discovery**

The 35 verses in experiment-001.md were used to:
- ✅ Learn TBTA's annotation methodology
- ✅ Discover "semantic over morphological" pattern
- ✅ Identify theological contexts (Trinity = Trial)
- ✅ Document discourse role patterns
- ✅ Build algorithm v1.0

**Original prediction accuracy**: 91.4% (32/35 correct before learning)
**Post-learning explainability**: 100% (can explain all cases after analysis)

**This is valuable reverse-engineering work**, but NOT independent validation.

---

## Retrospective Classification

experiment-001.md should now be considered:
- **Training data**: Used to develop algorithm
- **Pattern discovery**: Identified TBTA methodology
- **Algorithm development**: Built v1.0 rules

**NOT validation** because:
- ❌ Algorithm was refined using these verses
- ❌ "100% accuracy" was retroactive after learning
- ❌ No held-out test set
- ❌ Data leakage (trained on test data)

---

## Algorithm v1.0: Locked Patterns

From experiment-001 training, these patterns were learned:

### Pattern 1: Semantic Over Morphological
```
Rule: Count entities semantically ("How many X?"), not morphologically

Examples:
- Hebrew שָׁמַיִם (dual form) → Singular (one sky)
- Hebrew מַיִם (dual form) → Singular (one body of water)
- Greek οὐρανῶν (plural) → Singular (one heaven)

Authority: LXX and Vulgate confirm semantic interpretation
```

### Pattern 2: Theological Context
```
Rule: Trinity contexts = Trial + First Inclusive

Examples:
- Genesis 1:26 "Let us make..." → Trial (3 persons of Trinity)

Authority: Christian doctrine of Trinity
```

### Pattern 3: Discourse Role Determines Number
```
Rule: Same entity gets different number based on discourse role

Examples:
- God as narrator → Singular Third
- God as speaker ("us") → Trial First Inclusive
- Nicodemus alone → Singular
- Nicodemus representing group ("we know") → Plural First Exclusive

Authority: Discourse pragmatics
```

### Pattern 4: Fossilized Forms
```
Rule: Certain Hebrew duals are lexicalized as singular

List:
- שָׁמַיִם (shamayim, "heavens") → always Singular
- מַיִם (mayim, "waters") → always Singular
- צָהֳרַיִם (tsohorayim, "noon") → always Singular

Exception: עֵינַיִם (enayim, "eyes") → context-dependent
```

### Pattern 5: Ancient Translations
```
Rule: When morphology conflicts with semantics, check LXX/Vulgate

Process:
1. If Hebrew dual/plural but semantically unclear
2. Check LXX translation (Greek number)
3. Check Vulgate translation (Latin number)
4. Ancient consensus = strong evidence for TBTA interpretation
```

**Algorithm v1.0 locked**: 2025-11-07 (see experiment-001.md)

---

## Next Phase: Adversarial Validation

Following methodology in: `../../METHODOLOGY-ADVERSARIAL.md`

### Phase 2a: Adversarial Test Set (10 verses)

**Goal**: Test algorithm v1.0 on challenging edge cases

**Selection criteria** - designed to break the algorithm:

1. **Theological edge cases** (3 verses)
   - Different Trinity contexts (not Gen 1:26)
   - Messianic prophecy with debated referents
   - Corporate solidarity (Israel as one/many)

2. **Rare values** (2 verses)
   - Trial contexts (outside Trinity)
   - Paucal contexts (if they exist)
   - Quadrial contexts (probably don't exist)

3. **Morphological exceptions** (3 verses)
   - More Hebrew dual forms (beyond shamayim/mayim)
   - Greek number mismatches
   - Suppletive forms

4. **Ambiguous cases** (2 verses)
   - Context-dependent resolution
   - Discourse boundary cases
   - Translation divergence

**Expected accuracy**: 60-70% (adversarial cases are hard!)

**Status**: NOT STARTED - verses to be selected

---

### Phase 2b: Random Validation Set (10 verses)

**Goal**: Test algorithm v1.0 on typical cases

**Selection criteria**:
```
Random sample from:
- Genesis 2-3 (not in training)
- Matthew 6-7 (not in training)
- John 4-5 (not in training)

Stratified by number value:
- Singular: 5 verses
- Plural: 3 verses
- Dual: 1 verse
- Trial: 1 verse (if possible)
```

**Expected accuracy**: 80-90% (should be higher than adversarial!)

**Status**: NOT STARTED - random seed to be chosen

---

## Validation Process

### Step 1: Design Test Sets
- [ ] Select 10 adversarial verses (document reasoning)
- [ ] Select 10 random verses (document random seed)
- [ ] Commit both lists to git BEFORE predictions
- [ ] Ensure no overlap with training (35 verses from experiment-001)

### Step 2: Make Predictions (WITHOUT checking TBTA)
- [ ] Apply algorithm v1.0 to adversarial set
- [ ] Apply algorithm v1.0 to random set
- [ ] Document reasoning for each prediction
- [ ] Rate confidence: High (90%+), Medium (70-90%), Low (<70%)
- [ ] Commit predictions to git with timestamp

### Step 3: Lock Predictions
- [ ] Git commit: "Number feature validation predictions - LOCKED"
- [ ] Record commit SHA
- [ ] NO modifications allowed after this point

### Step 4: Check TBTA
- [ ] Retrieve TBTA annotations for adversarial set
- [ ] Retrieve TBTA annotations for random set
- [ ] Calculate accuracy for each
- [ ] Compare: Random should beat adversarial by 15-25 points

### Step 5: Analyze Results
- [ ] Error analysis for failures
- [ ] Categorize: Algorithm gap vs. edge case vs. TBTA error
- [ ] Flag potential TBTA errors (expect 1-2 in 20 verses = 5-10%)
- [ ] Document learnings

### Step 6: Update Algorithm
- [ ] Create algorithm v2.0 based on learnings
- [ ] DO NOT retest on same 20 verses
- [ ] Save learnings for other features

---

## Success Criteria

### Adversarial Test
- ✅ Success: 60-70% accuracy
  - Algorithm handles edge cases reasonably
  - Ready for production with caveats
- ⚠️ Review: 50-60% accuracy
  - Algorithm has significant gaps
  - Needs refinement before production
- ❌ Fail: <50% accuracy
  - Algorithm too simplistic
  - Major misunderstanding of TBTA methodology

### Random Test
- ✅ Success: 80-90% accuracy
  - Patterns generalize well
  - Algorithm works on typical cases
- ⚠️ Review: 70-80% accuracy
  - Some overfitting to training
  - Acceptable but monitor
- ❌ Fail: <70% accuracy
  - Serious problems with generalization
  - Algorithm needs major revision

### Comparative Metric (CRITICAL!)
- ✅ Success: Random accuracy > Adversarial by 15-25 points
  - Example: Adversarial 65%, Random 85% = 20 point gap
  - Proves test sets properly designed
  - Algorithm performs as expected
- ⚠️ Review: Random > Adversarial by 5-15 points
  - Gap too small = adversarial test not hard enough
  - Redesign adversarial set with harder cases
- ❌ Fail: Random ≤ Adversarial
  - Test sets poorly designed
  - Start over with better selection

---

## Timeline

**Week of 2025-11-11**: Adversarial validation
- Monday-Tuesday: Design test sets, commit
- Wednesday: Make predictions, lock
- Thursday: Check TBTA, calculate accuracy
- Friday: Error analysis, update algorithm v2.0

**Estimated completion**: 2025-11-15

---

## Files to Create

```
plan/tbta-rebuild-with-llm/features/number-systems/
├── adversarial-test/
│   ├── TEST-SET.md                  # 10 challenging verses with justification
│   ├── PREDICTIONS-locked.md        # Predictions before checking TBTA (commit SHA)
│   ├── RESULTS.md                   # Accuracy: target 60-70%
│   └── ERROR-ANALYSIS.md            # Detailed analysis of failures
│
└── random-test/
    ├── TEST-SET.md                  # 10 random verses (random seed documented)
    ├── PREDICTIONS-locked.md        # Predictions before checking TBTA (commit SHA)
    └── RESULTS.md                   # Accuracy: target 80-90%
```

---

## Notes for Other Features

This retrofit applies to:
- ✅ number-systems (this feature)
- ✅ degree (in progress, not too late to fix)
- ⏳ All other features (use adversarial from start)

**Lesson learned**:
> Training data looks like validation if you don't hold out a test set.
> Always predict first, then check TBTA.

---

## Honest Reporting

**For publications/documentation:**

> "The number systems feature was validated using a two-phase approach:
>
> **Training phase**: 35 verses were analyzed to understand TBTA's annotation
> methodology, achieving 91.4% initial prediction accuracy. After analysis,
> all cases could be explained (100% explainability), leading to algorithm v1.0.
>
> **Validation phase**: Algorithm v1.0 was tested on 20 held-out verses:
> - Adversarial test (10 challenging edge cases): X% accuracy
> - Random test (10 typical cases): Y% accuracy
>
> Results demonstrate that learned patterns generalize to new data, with
> expected performance degradation on adversarial cases."

---

**Status**: Ready to proceed with adversarial validation
**Next action**: Design adversarial test set (10 verses)
**Owner**: [Assign to researcher]
**Target date**: 2025-11-15
