# Degree Feature: Adversarial Test Set

**Purpose**: Test algorithm v1.0 on challenging edge cases
**Expected accuracy**: 50-60% (adversarial cases are intentionally difficult)
**Selection date**: 2025-11-08
**TBTA Access**: FORBIDDEN until predictions locked
**Status**: LOCKED - Do not modify after this commit

---

## Test Set Overview

**Total verses**: 5
**Source**: Selected from experiment-001.md (excluded from training)
**Selection criteria**: Edge cases that challenge degree boundary decisions
**Training overlap**: None (explicitly excluded from 8-verse training set)

---

## Adversarial Test Verses

### 1. Matthew 5:19 - Downward Superlative Boundary

**Reference**: Matthew 5:19
**Greek**: ὃς ἐὰν οὖν λύσῃ μίαν τῶν ἐντολῶν τούτων τῶν ἐλαχίστων
**English (ESV)**: "Therefore whoever relaxes one of the least of these commandments"

**Challenge**:
- ἐλάχιστος (elachistos) - superlative form "least"
- Downward direction (smallest, least important)
- Does TBTA mark as:
  - l (lowercase L) - "least" specifically?
  - L (uppercase L) - general downward comparison?
  - S (Superlative) - treating as standard superlative?

**Why adversarial**: Tests directional superlative distinction (downward "least" vs. upward "greatest")

**Confidence**: Low (uncertain without training data on downward superlatives)

---

### 2. Romans 5:15 - Intensified Comparative Threshold

**Reference**: Romans 5:15
**Greek**: πολλῷ μᾶλλον ἡ χάρις τοῦ θεοῦ
**English (ESV)**: "much more the grace of God"

**Challenge**:
- πολλῷ μᾶλλον (pollō mallon) - "much more" (comparative + intensifier)
- Is this:
  - C (Comparative) - standard comparative?
  - i (Intensified Comparative) - if this code exists?
  - I/V (Intensified) - treating the intensifier separately?

**Why adversarial**: Tests boundary between comparative and intensified comparative

**Confidence**: Medium (depends on whether TBTA distinguishes intensified comparatives)

---

### 3. 2 Corinthians 4:17 - Extreme Intensification (Double Hyperbole)

**Reference**: 2 Corinthians 4:17
**Greek**: καθ' ὑπερβολὴν εἰς ὑπερβολὴν αἰώνιον βάρος δόξης
**English (ESV)**: "an eternal weight of glory beyond all comparison"

**Challenge**:
- καθ' ὑπερβολὴν εἰς ὑπερβολὴν - "beyond comparison to comparison" (double hyperbole)
- Extreme intensification through repetition
- Is this:
  - E (Extremely Intensified) - if this rare code exists?
  - I/V (Intensified) - treating as standard intensification?
  - S (Superlative) - semantic superlative ("most glorious")?

**Why adversarial**: Tests threshold for extreme intensification coding

**Confidence**: Low (rare construction, unclear TBTA policy)

---

### 4. Ephesians 3:20 - Triple Compound Intensifier

**Reference**: Ephesians 3:20
**Greek**: τῷ δὲ δυναμένῳ ὑπὲρ πάντα ποιῆσαι ὑπερεκπερισσοῦ
**English (ESV)**: "Now to him who is able to do far more abundantly than all that we ask or think"

**Challenge**:
- ὑπερεκπερισσοῦ (hyperekperissou) - triple compound: ὑπέρ (hyper-) + ἐκ (ek-) + περισσός (perissos)
- Morphologically extreme intensification
- But English translates as comparative: "far MORE abundantly"
- Does TBTA encode:
  - E (Extremely Intensified) - based on Greek morphology?
  - C (Comparative) - based on English translation "more"?
  - S (Superlative) - semantic maximum ("most abundantly possible")?

**Why adversarial**: Tests whether TBTA encodes source language (Greek) or target language (English) forms

**Confidence**: Low (critical test of TBTA's encoding philosophy)

---

### 5. Matthew 10:25 - Equative Construction

**Reference**: Matthew 10:25
**Greek**: ἀρκετὸν τῷ μαθητῇ ἵνα γένηται ὡς ὁ διδάσκαλος αὐτοῦ
**English (ESV)**: "It is enough for the disciple to be like his teacher"

**Challenge**:
- ὡς (hōs) - comparative particle "like, as"
- Equative construction: "X is AS Y" (not more or less, but equal)
- Does TBTA mark equative:
  - q (Equative) - if this code exists?
  - C (Comparative) - treating ὡς as general comparison?
  - N (No Degree) - not considering equative as degree?

**Why adversarial**: Tests whether TBTA distinguishes equative from comparative

**Confidence**: Low (equative is edge case, may not have dedicated code)

---

## Selection Rationale

These 5 verses were chosen from experiment-001.md because they represent:

1. **Boundary cases**: Where category distinctions are unclear
   - Downward vs. upward (Matt 5:19)
   - Comparative vs. intensified comparative (Rom 5:15)
   - Intensified vs. extremely intensified (2 Cor 4:17, Eph 3:20)
   - Comparative vs. equative (Matt 10:25)

2. **Rare constructions**: Not likely covered in training
   - Double hyperbole (2 Cor 4:17)
   - Triple compound (Eph 3:20)
   - Equative particle (Matt 10:25)

3. **Philosophy tests**: Source vs. target language encoding
   - Eph 3:20 specifically tests whether TBTA follows Greek morphology or English translation

---

## Expected Performance

**Realistic expectations**:
- **50-60% accuracy** (2-3 correct out of 5): Algorithm handles some edge cases
- **40-50% accuracy** (2 correct): Significant gaps but learning possible
- **<40% accuracy** (0-1 correct): Algorithm too simplistic for edge cases

**Specific predictions about likely errors**:
1. **Matt 5:19**: May mark 'S' instead of 'l' (expect error)
2. **Rom 5:15**: May mark 'C' instead of 'i' if 'i' exists (expect error)
3. **2 Cor 4:17**: May mark 'I' instead of 'E' if 'E' exists (expect error)
4. **Eph 3:20**: Critical test - may mark 'E' (Greek) but TBTA might mark 'C' (English)
5. **Matt 10:25**: May mark 'C' instead of 'q' if 'q' exists (expect error)

**Success benchmark**: 2-3 correct = 40-60% ✅

---

## Prediction Protocol

**CRITICAL**: Do NOT check TBTA for these verses until after predictions are locked!

### Step 1: Wait for Algorithm v1.0
- Training phase must complete first
- Algorithm v1.0 must be locked (git commit SHA)

### Step 2: Apply Algorithm to Test Set
- For each verse, apply algorithm v1.0 WITHOUT checking TBTA
- Document reasoning for each prediction
- Rate confidence: High/Medium/Low
- Note any gaps in algorithm that make prediction difficult

### Step 3: Lock Predictions
- Create `PREDICTIONS-locked.md` file
- Include all 5 predictions with reasoning
- Commit to git with timestamp
- Record commit SHA
- NO modifications allowed after this point

### Step 4: Check TBTA
- Only AFTER predictions are locked
- Retrieve TBTA annotations for these 5 verses
- Calculate accuracy
- Document in `RESULTS.md`

---

## Success Criteria

**Adversarial test successful if**:
- ✅ Predictions made BEFORE checking TBTA
- ✅ Predictions locked (git commit SHA recorded)
- ✅ Accuracy 40-60% (2-3 correct)
- ✅ Error analysis identifies specific algorithm gaps
- ✅ Learnings feed into algorithm v2.0

**Red flags**:
- ❌ Check TBTA before making predictions
- ❌ Modify predictions after seeing TBTA
- ❌ Accuracy <40% (algorithm fundamentally broken)
- ❌ Accuracy >70% (test set not adversarial enough)

---

## Comparison with Random Test

**Expected gap**: Random should beat adversarial by 20-35 points

**Example outcome**:
- Adversarial: 50% (2-3 correct)
- Random: 80% (4 correct)
- Gap: 30 points ✅

If gap <15 points, adversarial test not hard enough ❌

---

## Files to Create

After algorithm v1.0 locked:
1. ⏳ `PREDICTIONS-locked.md` - Predictions before checking TBTA (with commit SHA)
2. ⏳ `RESULTS.md` - Accuracy after checking TBTA
3. ⏳ `ERROR-ANALYSIS.md` - Detailed analysis of failures

---

**Status**: ✅ Test set locked
**Next action**: Wait for algorithm v1.0, then make predictions WITHOUT TBTA
**Target date**: 2025-11-10
