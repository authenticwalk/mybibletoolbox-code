# Degree Feature: Random Test Set

**Purpose**: Test algorithm v1.0 on typical cases
**Expected accuracy**: 75-85% (typical cases should be easier than adversarial)
**Selection date**: 2025-11-08
**Random seed**: 42
**TBTA Access**: FORBIDDEN until predictions locked
**Status**: LOCKED - Do not modify after this commit

---

## Test Set Overview

**Total verses**: 5
**Source**: NEW verses not in experiment-001.md
**Selection method**: Random selection from diverse books with clear degree marking
**Training overlap**: None
**Adversarial overlap**: None

---

## Selection Strategy

**Books prioritized**: Different from training set
- Training includes: John 15, Matthew 22, Mark 1, Hebrews 7, Song of Solomon, Genesis 1
- Random test focuses on: Luke, James, Philippians, Psalms, Isaiah

**Typical cases** (avoid adversarial characteristics):
- Clear comparative/superlative morphology
- Standard intensification
- No extreme constructions (no triple compounds)
- No boundary cases (no equative, no directional ambiguity)
- Straightforward degree marking

---

## Random Test Verses

### 1. Luke 9:48 - Upward Superlative (Clear Morphology)

**Reference**: Luke 9:48
**Greek**: ὁ γὰρ μικρότερος ἐν πᾶσιν ὑμῖν ὑπάρχων οὗτός ἐστιν μέγας
**English (ESV)**: "For he who is least among you all is the one who is great"

**Morphology**: μικρότερος (mikroteros) - comparative form "lesser/younger"
**Context**: Standard comparative usage
**Expected**: C (Comparative) or possibly l/L (downward comparison)
**Confidence**: High (clear comparative morphology)

**Why typical**: Synthetic comparative with clear morphology, no ambiguity

---

### 2. James 3:4 - Intensified with Standard Adverb

**Reference**: James 3:4
**Greek**: ἰδοὺ καὶ τὰ πλοῖα τηλικαῦτα ὄντα καὶ ὑπὸ ἀνέμων σκληρῶν ἐλαυνόμενα
**English (ESV)**: "Look at the ships also: though they are so large and are driven by strong winds"

**Morphology**: τηλικαῦτα (tēlikauta) - "so large" (demonstrative intensifier)
**Context**: Intensification of size
**Expected**: I/V (Intensified/Very) or possibly S (if semantic superlative)
**Confidence**: Medium-High (standard intensification pattern)

**Why typical**: Common intensification pattern without extreme morphology

---

### 3. Philippians 1:23 - Synthetic Comparative (Clear Case)

**Reference**: Philippians 1:23
**Greek**: τὴν ἐπιθυμίαν ἔχων εἰς τὸ ἀναλῦσαι καὶ σὺν Χριστῷ εἶναι, πολλῷ γὰρ μᾶλλον κρεῖσσον
**English (ESV)**: "My desire is to depart and be with Christ, for that is far better"

**Morphology**: κρεῖσσον (kreisson) - comparative form "better"
**Intensifier**: πολλῷ μᾶλλον "far/much better"
**Expected**: C (Comparative) with possible intensification marking
**Confidence**: High (clear comparative, though intensified like Rom 5:15 in adversarial)

**Why typical**: Standard comparative construction, even if intensified

**Note**: Similar to Rom 5:15 (adversarial), but clearer comparative morphology

---

### 4. Psalm 19:10 - Hebrew Comparative (Min Construction)

**Reference**: Psalm 19:10
**Hebrew**: הַֽנֶּחֱמָדִים מִזָּהָב וּמִפַּז רָב
**English (ESV)**: "More to be desired are they than gold, even much fine gold"

**Morphology**: מִן (min) construction - "more desirable THAN gold"
**Context**: Standard Hebrew comparative
**Expected**: C (Comparative)
**Confidence**: High (standard Hebrew comparative like Song 1:2 in training)

**Why typical**: Straightforward Hebrew comparative construction

---

### 5. Isaiah 55:9 - Hebrew Comparative with Vertical Imagery

**Reference**: Isaiah 55:9
**Hebrew**: כִּֽי־גָבְהוּ שָׁמַיִם מֵאָרֶץ כֵּן גָּבְהוּ דְרָכַי מִדַּרְכֵיכֶם
**English (ESV)**: "For as the heavens are higher than the earth, so are my ways higher than your ways"

**Morphology**: מִן (min) construction - "higher THAN" (גָבְהוּ... מֵ)
**Context**: Comparative of elevation/superiority
**Expected**: C (Comparative)
**Confidence**: High (standard comparative, same structure as Psalm 19:10)

**Why typical**: Clear comparative construction with standard Hebrew morphology

---

## Stratification by Degree Type

**Target distribution**:
- Comparative (C): 3 verses (Luke 9:48, Phil 1:23, Psalm 19:10 or Isaiah 55:9)
- Superlative (S): 0 verses (harder to find clear typical cases)
- Intensified (I/V): 1 verse (James 3:4)
- Hebrew comparative: 2 verses (Psalm 19:10, Isaiah 55:9)

**Rationale**: Comparatives are most common degree type, so weighted accordingly

---

## Exclusions Confirmed

**Not in experiment-001**:
- John 15:13, Matthew 22:36, 22:38, 5:19, Romans 5:15, 5:17, Mark 1:35, 2 Corinthians 4:17, Hebrews 7:7, Matthew 10:25, Genesis 1:1, Song of Solomon 1:2, 1:8, Ephesians 3:20
- ✅ None of random test verses overlap

**Not in training set** (8 verses):
- ✅ None of random test verses overlap

**Not in adversarial set** (5 verses):
- ✅ None of random test verses overlap

---

## Expected Performance

**Target accuracy**: 75-85% (4 out of 5 correct, possibly all 5)

**High confidence predictions** (3 verses):
- Luke 9:48 (clear comparative)
- Psalm 19:10 (Hebrew min comparative)
- Isaiah 55:9 (Hebrew min comparative)

**Medium confidence predictions** (2 verses):
- James 3:4 (intensification - depends on TBTA intensifier policy)
- Phil 1:23 (comparative but intensified - similar to adversarial Rom 5:15)

**Likely correct** (4-5 verses):
- All Hebrew comparatives should work (learned in training)
- Clear Greek comparative should work (learned in training)
- Intensification might work (learned in training with Mark 1:35)

**Possible error candidate**:
- Phil 1:23 - If TBTA distinguishes intensified comparative, might miss this
  (But training will reveal this pattern, so maybe not an error)

**Success benchmark**: 4-5 correct = 80-100% ✅

---

## Comparison with Adversarial Set

**Design philosophy**:
- **Adversarial**: Boundary cases, extreme constructions, philosophical tests, rare values
- **Random**: Clear morphology, standard constructions, typical patterns, representative

**Expected gap**: Random should beat adversarial by 20-35 points

**Example outcome**:
- Adversarial: 50% (2-3 correct)
- Random: 80% (4 correct)
- Gap: 30 points ✅

**Success criteria**:
- ✅ Random > Adversarial by 15+ points
- ❌ Random ≤ Adversarial (test sets poorly designed)

---

## Prediction Protocol

**CRITICAL**: Do NOT check TBTA for these verses until after predictions are locked!

### Step 1: Wait for Algorithm v1.0
- Training phase must complete first
- Algorithm v1.0 must be locked (git commit SHA)

### Step 2: Apply Algorithm to Random Test
- For each verse, apply algorithm v1.0 WITHOUT checking TBTA
- Document reasoning
- Rate confidence: High/Medium/Low

### Step 3: Lock Predictions
- Create `PREDICTIONS-locked.md` file
- Include all 5 predictions with reasoning
- Commit to git with timestamp (AFTER adversarial predictions)
- Record commit SHA
- NO modifications allowed after this point

### Step 4: Check TBTA
- Only AFTER both test predictions are locked
- Retrieve TBTA annotations for these 5 verses
- Calculate accuracy
- Compare with adversarial accuracy
- Document in `RESULTS.md`

---

## Success Criteria

**Random test successful if**:
- ✅ Predictions made BEFORE checking TBTA
- ✅ Predictions locked (git commit SHA recorded)
- ✅ Accuracy 75-85% (4 out of 5 correct)
- ✅ Random accuracy > Adversarial accuracy by 15+ points
- ✅ Demonstrates algorithm generalization to typical cases

**Red flags**:
- ❌ Check TBTA before making predictions
- ❌ Modify predictions after seeing TBTA
- ❌ Accuracy <70% (algorithm doesn't generalize)
- ❌ Random ≤ Adversarial (test sets poorly designed)

---

## Random Seed Documentation

**Seed**: 42
**Selection process**:
1. Listed books not heavily used in experiment-001 or training
2. Used random seed 42 to select 5 diverse books
3. From each book, searched for clear degree marking (comparatives, intensifiers)
4. Selected verses with straightforward constructions (no edge cases)
5. Verified no overlap with training or adversarial sets

**Reproducibility**: Using seed 42, this selection process can be reproduced

---

## Files to Create

After algorithm v1.0 locked:
1. ⏳ `PREDICTIONS-locked.md` - Predictions before checking TBTA (with commit SHA)
2. ⏳ `RESULTS.md` - Accuracy after checking TBTA

---

**Status**: ✅ Test set locked
**Next action**: Wait for algorithm v1.0, then make predictions WITHOUT TBTA (after adversarial)
**Target date**: 2025-11-10
