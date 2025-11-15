# Degree Feature: Methodology Status

**Current Phase**: Predictions Made → SPLIT NOW Before Checking TBTA
**Algorithm Version**: v0.9 (preliminary from LEARNINGS.md)
**Last Updated**: 2025-11-07

---

## CRITICAL: Perfect Timing to Do This Right! ⚠️

**Current status**: experiment-001.md has predictions but TBTA data NOT YET ACCESSED

**This is PERFECT timing!** We can fix the methodology BEFORE checking TBTA.

---

## The Plan: Split Before Checking

### Current Situation

From experiment-001.md, we have predictions for ~12 verses:
1. John 15:13 (μείζονα - comparative)
2. Matthew 22:36 & 22:38 (μεγάλη - superlative context)
3. Matthew 5:19 (ἐλάχιστος - downward superlative)
4. Romans 5:15 & 5:17 (πολλῷ μᾶλλον - intensified comparative)
5. Mark 1:35 (λίαν - intensified)
6. 2 Corinthians 4:17 (ὑπερβολή - extremely intensified)
7. Hebrews 7:7 (ἔλαττον/κρείττων - downward/upward comparative)
8. Matthew 10:25 (equative attempt)
9. Genesis 1:1 (no degree - Hebrew baseline)
10. Song of Solomon 1:2 (Hebrew comparative)
11. Song of Solomon 1:8 (Hebrew superlative)
12. Ephesians 3:20 (ὑπερεκπερισσοῦ - extremely intensified)

**Total**: ~12 verses with predictions

---

## Proper Split Strategy

### Option A: Training + Test Split (Recommended)

**Training set** (8 verses) - Check TBTA first, learn patterns:
1. John 15:13 (clear comparative)
2. Matthew 22:36 & 22:38 (semantic superlative)
3. Mark 1:35 (standard intensifier)
4. Hebrews 7:7 (upward vs downward comparison)
5. Song of Solomon 1:2 (Hebrew comparative)
6. Song of Solomon 1:8 (Hebrew superlative)

**Test set** (4 verses) - Predict BEFORE checking TBTA:
1. Matthew 5:19 (downward superlative)
2. Romans 5:15 & 5:17 (intensified comparative)
3. 2 Corinthians 4:17 (extreme intensification)
4. Ephesians 3:20 (extreme intensification)

**Rationale**:
- Training: Cover basic patterns (C, S, I/V, L/l)
- Test: Cover uncertain patterns (l vs S, i vs C, E threshold)
- Learning from training won't "leak" into test

---

### Option B: Full Adversarial Approach (Better)

**Training set** (8 verses) - Learn from TBTA freely:
- Same as Option A

**Lock algorithm v1.0** based on training

**Adversarial test** (5 verses) - Edge cases:
1. Matthew 5:19 (l vs S distinction)
2. Romans 5:15 (i vs C distinction)
3. 2 Cor 4:17 (E threshold - double hyperbole)
4. Ephesians 3:20 (E threshold - triple compound)
5. Matthew 10:25 (q - equative construction)

**Random test** (5 verses) - NEW verses not in experiment-001:
- Select 5 random verses with degree marking
- From different books
- Mix of C/S/I values
- Should be easier than adversarial

**Expected results**:
- Adversarial: 50-60% (very uncertain cases)
- Random: 75-85% (typical cases)

---

## Recommended Approach: Option B

**Advantages**:
- Follows standard adversarial methodology
- Includes random validation (not just hard cases)
- Tests on truly unseen data (random set)
- Can compare adversarial vs random accuracy
- More convincing validation

**Process**:

### Step 1: Lock the Training Split (TODAY)
```markdown
Training set (8 verses) - TBTA can be checked:
1. John 15:13 - μείζονα (comparative)
2. Matthew 22:36 - μεγάλη (semantic superlative)
3. Matthew 22:38 - μεγάλη (semantic superlative)
4. Mark 1:35 - λίαν (intensified)
5. Hebrews 7:7 - ἔλαττον/κρείττων (L vs C)
6. Song of Solomon 1:2 - Hebrew מִן construction (comparative)
7. Song of Solomon 1:8 - Hebrew article + partitive (superlative)
8. Genesis 1:1 - No degree (baseline)
```

Commit this split to git NOW before checking any TBTA data.

---

### Step 2: Check TBTA for Training Set ONLY
- Access TBTA for the 8 training verses
- Analyze patterns:
  - Does semantic superlative get marked S?
  - Is L/l distinguished from C/S?
  - How is Hebrew מִן marked?
  - Hebrew article + partitive → S?
- Document patterns learned
- Build algorithm v1.0

---

### Step 3: Lock Algorithm v1.0
Based on training set analysis, document decision rules:

```markdown
Algorithm v1.0: Degree Feature

Rule 1: Synthetic Morphology (High confidence)
- Greek -τερος/-ίων forms → C
- Greek -τατος/-ιστος forms → S
- Hebrew מִן construction → C

Rule 2: Semantic Interpretation (From training)
- Positive form + superlative context → [S or N - learn from training]
- Analytic μᾶλλον/μάλιστα → [C/S - learn from training]

Rule 3: Intensification (From training)
- Standard intensifiers (λίαν, μְאֹד) → [I/V - learn from training]
- Compound intensifiers → [I or E - learn from training]

Rule 4: Downward Comparison (From training)
- ἔλαττον "lesser" → [L or C - learn from training]
- ἐλάχιστος "least" → [l or S - learn from training]

Rule 5: Hebrew Constructions (From training)
- Article + partitive → [S or N - learn from training]
```

Commit algorithm v1.0 with git SHA.

---

### Step 4: Make Adversarial Test Predictions
For the 5 adversarial verses (from experiment-001):
1. Matthew 5:19 (ἐλάχιστος)
2. Romans 5:15 (πολλῷ μᾶλλον)
3. 2 Cor 4:17 (καθ' ὑπερβολὴν εἰς ὑπερβολὴν)
4. Eph 3:20 (ὑπερεκπερισσοῦ)
5. Matthew 10:25 (ὡς - equative)

Apply algorithm v1.0 WITHOUT checking TBTA.
Document predictions with reasoning.
Rate confidence for each.
Commit predictions with timestamp.

---

### Step 5: Select Random Test Set (NEW VERSES)
Choose 5 verses NOT in experiment-001:

**Random seed**: 42 (for reproducibility)

**Selection criteria**:
- From books not heavily represented in training
- Mix of Greek and Hebrew
- Include clear C, S, and I/V cases
- Typical cases, not edge cases

**Suggested verses** (can change based on random selection):
- John 3:16 (οὕτως... ὥστε - possible intensification)
- Matthew 7:11 (πολλῷ μᾶλλον - "how much more")
- Luke 18:14 (comparative righteousness context)
- Psalm 19:10 (Hebrew comparative - "sweeter than")
- Isaiah 55:9 (Hebrew comparative - "higher than")

Commit this list to git.

---

### Step 6: Make Random Test Predictions
Apply algorithm v1.0 to the 5 random verses.
WITHOUT checking TBTA.
Document predictions.
Commit with timestamp.

---

### Step 7: Lock All Predictions
Git commit: "Degree feature test predictions - LOCKED"
Record commit SHA.
NO modifications after this point.

---

### Step 8: Check TBTA for Test Sets
Now retrieve TBTA data for:
- 5 adversarial verses
- 5 random verses

Calculate accuracy for each set.

---

### Step 9: Analyze Results

**Expected outcomes**:

Scenario A (Success):
- Adversarial: 50-60% (hard cases)
- Random: 75-85% (typical cases)
- Gap: 20-30 points ✅

Scenario B (Acceptable):
- Adversarial: 60-70% (not as hard as expected)
- Random: 80-90% (good generalization)
- Gap: 15-25 points ✅

Scenario C (Problem):
- Adversarial: 40% (algorithm too simplistic)
- Random: 50% (doesn't generalize)
- Need major algorithm revision ❌

Scenario D (Wrong test design):
- Adversarial: 80%
- Random: 75%
- Random should beat adversarial ❌

---

## Alternative: Minimal Approach (If time constrained)

If full adversarial + random is too much work:

**Simplified process**:
1. Designate 8 verses as training (check TBTA, learn patterns)
2. Designate 4 verses as test (predict first, then check)
3. Report test accuracy honestly
4. Acknowledge small sample size

**But this is less rigorous** - no comparison between hard and typical cases.

---

## File Structure

```
plan/tbta-rebuild-with-llm/features/degree/
├── METHODOLOGY-STATUS.md (this file)
│
├── training/
│   ├── TRAINING-SET.md              # 8 verses from experiment-001
│   ├── TBTA-ANNOTATIONS.md          # TBTA data for training
│   ├── PATTERNS-LEARNED.md          # Insights from training
│   └── ALGORITHM-v1.md              # Locked decision rules
│
├── adversarial-test/
│   ├── TEST-SET.md                  # 5 hard verses from experiment-001
│   ├── PREDICTIONS-locked.md        # Before checking TBTA (commit SHA)
│   ├── TBTA-ANNOTATIONS.md          # TBTA data after prediction
│   └── RESULTS.md                   # Accuracy: target 50-60%
│
└── random-test/
    ├── TEST-SET.md                  # 5 new verses (random seed 42)
    ├── PREDICTIONS-locked.md        # Before checking TBTA (commit SHA)
    ├── TBTA-ANNOTATIONS.md          # TBTA data after prediction
    └── RESULTS.md                   # Accuracy: target 75-85%
```

---

## Timeline

**This week** (2025-11-07 to 2025-11-11):

**Day 1 (Today)**: Split decision
- [ ] Commit training split (8 verses)
- [ ] Commit adversarial split (5 verses)
- [ ] Select random test set (5 verses)
- [ ] Commit random split

**Day 2**: Training phase
- [ ] Access TBTA for training set ONLY
- [ ] Analyze patterns
- [ ] Document learnings
- [ ] Build algorithm v1.0

**Day 3**: Lock and predict
- [ ] Lock algorithm v1.0 (git commit)
- [ ] Make adversarial predictions (no TBTA)
- [ ] Make random predictions (no TBTA)
- [ ] Commit predictions with SHA

**Day 4**: Validation
- [ ] Access TBTA for test sets
- [ ] Calculate accuracy
- [ ] Compare adversarial vs random

**Day 5**: Analysis
- [ ] Error analysis
- [ ] Update algorithm v2.0
- [ ] Document learnings for other features

---

## Key Decisions Needed

### Decision 1: Which split option?
- [ ] Option A: Simple train/test (faster, less rigorous)
- [x] Option B: Full adversarial (recommended, follows methodology)

### Decision 2: Random test verses
- [ ] Use suggested verses above
- [ ] Different random selection (specify seed)
- [ ] Skip random test (not recommended)

### Decision 3: When to access TBTA?
- [ ] TODAY for training set (can start learning)
- [ ] Wait until algorithm v1.0 locked
- [ ] Wait until predictions locked

---

## Success Criteria

**Validation successful if**:
- ✅ Training/test split documented before TBTA access
- ✅ Predictions locked before checking test TBTA
- ✅ Adversarial accuracy: 50-60%
- ✅ Random accuracy: 75-85%
- ✅ Random > Adversarial by 15-30 points
- ✅ Error analysis completed
- ✅ Learnings documented

**Red flags**:
- ❌ Check TBTA before locking split
- ❌ Modify predictions after seeing TBTA
- ❌ Random accuracy ≤ Adversarial accuracy
- ❌ Both accuracy rates <50%

---

## Honest Reporting Template

For documentation/publication:

> "The degree feature validation used a split approach with 8 training verses
> and 10 held-out test verses (5 adversarial, 5 random).
>
> **Training phase**: Analysis of 8 verses identified patterns for [list patterns].
> Algorithm v1.0 was locked with these decision rules.
>
> **Adversarial test**: 5 challenging edge cases (intensified comparative,
> extreme intensification threshold, downward comparison distinction) achieved
> X% accuracy, demonstrating algorithm performance on difficult cases.
>
> **Random test**: 5 typical cases achieved Y% accuracy, showing pattern
> generalization to unseen data.
>
> The Z-point gap between random and adversarial accuracy indicates [interpretation]."

---

## Action Items

**Immediate (before checking ANY TBTA data)**:
1. [ ] Review split options
2. [ ] Decide on Option A or B
3. [ ] Commit training split to git
4. [ ] Commit adversarial split to git
5. [ ] Select and commit random split (if Option B)

**Next**:
6. [ ] Access TBTA for training set only
7. [ ] Follow the process above

**DO NOT**:
- ❌ Check TBTA for test verses before prediction
- ❌ Modify splits after seeing TBTA
- ❌ Skip the random validation (if doing Option B)

---

**Status**: DECISION POINT - Choose split option and lock splits before TBTA access
**Next action**: Commit training/test splits to git
**Owner**: [Assign to researcher]
**Target date**: 2025-11-07 (TODAY before checking TBTA!)
