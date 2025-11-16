# Subagent Task: Test Algorithm v2.2 on Test Set

**Task ID**: test-v2.2-algorithm
**Duration**: 2 hours
**Priority**: High (blocks all other phases)

## Objective

Apply PROMPT4.md (Algorithm v2.2) to the 21-verse test set and validate the claimed 81% accuracy.

## Input Files

All files located in `/workspace/bible-study-tools/tbta/features/person-system/experiments/`:

1. **PROMPT4.md** - Algorithm v2.2 (hierarchical decision framework)
2. **test.yaml** - 21 verses with TBTA clusivity values (11 adversarial + 10 random)

## Task Instructions

### Step 1: Read Algorithm (10 min)
- Read `experiments/PROMPT4.md` thoroughly
- Understand the hierarchical decision framework:
  - Level 1: Structural analysis (identify speaker, addressee, God-reference type)
  - Level 2: Primary rules (2.1-2.7, apply first match)
  - Level 3: Secondary rules (3.1-3.3, if no primary match)
  - Level 4-5: Genre defaults (last resort)
- **Key v2.2 change**: Rule 2.1 now ONLY triggers on direct address (2nd person/vocative), NOT 3rd person

### Step 2: Read Test Data (10 min)
- Read `experiments/test.yaml`
- Note the 21 verses with their TBTA clusivity values
- Understand adversarial vs random split

### Step 3: Apply Algorithm to Each Verse (60 min)

For each of the 21 verses in test.yaml:

1. **Structural Analysis** (Level 1):
   - Speaker: Who is speaking?
   - Addressee: Who is being addressed?
   - Action: What action/state is referenced?
   - Genre: What is the discourse context?
   - God-reference: How is God referenced (2nd person/vocative vs 3rd person)?
   - Quoted speech: Is this nested?

2. **Apply Rules in Order**:
   - **FIRST**: Check strict Rule 2.1 (Direct address TO deity)
     - Verify 2nd person/vocative (not 3rd person)
     - Verify actual prayer (not quoted/hypothetical)
   - Then: Rules 2.2-2.7
   - Then: Rules 3.1-3.3
   - Stop at first match

3. **Make Prediction**:
   - Predicted value: INCLUSIVE or EXCLUSIVE
   - Rule applied: Which rule triggered?
   - Confidence: HIGH/MEDIUM/LOW (from PROMPT4.md calibration)
   - Rationale: Brief explanation

4. **Document Analysis**:
   ```yaml
   - reference: "{BOOK} {chapter}:{verse}"
     tbta_value: "{inclusive|exclusive}"
     predicted_value: "{inclusive|exclusive}"
     rule_applied: "Rule {number}"
     confidence: "{high|medium|low}"
     correct: "{yes|no}"
     rationale: |
       {Brief explanation of decision}
   ```

### Step 4: Calculate Accuracy (20 min)

**Overall Accuracy**:
- Correct predictions / 21 total
- Compare with v2.2 target (81% = 17/21)

**By Subset**:
- Adversarial subset (11 verses): {X}/11 = {Y}%
- Random subset (10 verses): {X}/10 = {Y}%

**By Value**:
- Inclusive verses: {X}/{total inclusive} = {Y}%
- Exclusive verses: {X}/{total exclusive} = {Y}%

**Error Analysis**:
- List failed verses with brief explanation
- Identify common error patterns

### Step 5: Document Results (20 min)

Create `/workspace/plan/person-system-completion/v2.2-test-results.md`:

```markdown
# Algorithm v2.2 Test Results

**Date**: 2025-11-16
**Algorithm**: PROMPT4.md (v2.2)
**Test Set**: 21 verses (11 adversarial + 10 random)

## Overall Results

- **Accuracy**: {X}/21 = {Y}%
- **vs. Claimed**: 81% (17/21)
- **Result**: {PASS ✅ / FAIL ❌}

## Breakdown

| Subset | Correct | Total | Accuracy |
|--------|---------|-------|----------|
| Adversarial | {X} | 11 | {Y}% |
| Random | {X} | 10 | {Y}% |
| **Total** | **{X}** | **21** | **{Y}%** |

| Value | Correct | Total | Accuracy |
|-------|---------|-------|----------|
| Inclusive | {X} | {N} | {Y}% |
| Exclusive | {X} | {N} | {Y}% |

## Predictions

{Include YAML with all 21 verse predictions}

## Error Analysis

### Failed Verses

{List each failed verse with:}
- Reference
- TBTA value vs Predicted value
- Rule that was applied
- Why the prediction was wrong
- What should have triggered instead

### Error Patterns

{Identify common patterns across failures}

## Comparison with Prior Versions

| Version | Test Accuracy | Notes |
|---------|---------------|-------|
| v1.0 | 62% (13/21) | Baseline |
| v2.1 | 71.4% (15/21) | Rule 2.1 over-trigger issue |
| v2.2 | {Y}% ({X}/21) | Strict Rule 2.1 trigger |

## Recommendation

{PASS ≥80%}: Proceed to Phase 2 (generate validate.yaml)
{FAIL <80%}: Iterate to v2.3 with identified fixes
```

## Success Criteria

- ✅ All 21 verses analyzed with documented rationale
- ✅ Accuracy calculated (overall, by subset, by value)
- ✅ Results documented in v2.2-test-results.md
- ✅ Clear recommendation (proceed or iterate)

## Expected Outcome

**If v2.2 achieves ≥80%**: Proceed to Phase 2 (validate.yaml generation)
**If v2.2 achieves <80%**: Error analysis reveals what needs fixing for v2.3

## Key v2.2 Predictions to Verify

According to PROMPT4.md, v2.2 should fix these specific errors:

| Verse | v2.1 Result | v2.2 Expected | Reason |
|-------|-------------|---------------|--------|
| Psalm 44:1 | ✅ EXCLUSIVE | ✅ EXCLUSIVE | Vocative "O God" |
| Psalm 66:6 | ❌ EXCLUSIVE | ✅ INCLUSIVE | 3rd person "in him" doesn't trigger Rule 2.1 |
| Ezekiel 33:10 | ❌ EXCLUSIVE | ✅ INCLUSIVE | Quoted lament, not direct prayer |
| Jonah 1:14 | ✅ EXCLUSIVE | ✅ EXCLUSIVE | Vocative "O LORD" |

**Critical Test**: Did v2.2 fix Psalm 66:6 and Ezekiel 33:10 without breaking others?

## Deliverables

1. `/workspace/plan/person-system-completion/v2.2-test-results.md` - Complete test results
2. Clear recommendation to main agent: proceed or iterate

---

**Subagent**: You are a rigorous tester. Apply the algorithm exactly as specified in PROMPT4.md. Do not deviate. Document every decision transparently.
