# Validation Protocol: Blind Testing Procedure
## Number Systems TBTA Feature - Stage 6

**Created**: 2025-11-18
**Agent**: Tester Agent
**Purpose**: Define rigorous blind testing protocol for Stage 6 validation
**Prerequisites**: Train accuracy ≥95% AND Test accuracy ≥95%

---

## Protocol Overview

This protocol ensures **scientific integrity** through blind testing methodology where prediction agents NEVER see answer sheets until predictions are locked via git commit.

**Key Principle**: Predictions must be locked (git committed) BEFORE any scoring or comparison with answer sheets.

---

## Phase 1: Pre-Validation Verification

### Step 1.1: Verify Prerequisites

**Checklist** (ALL must be ✅):
- [ ] PROMPT2/PROMPT3 (or later) achieves ≥95% on train set
- [ ] PROMPT2/PROMPT3 (or later) achieves ≥95% on test set
- [ ] validate_questions.yaml has real translation data (not TO_BE_FETCHED)
- [ ] validate.yaml answer sheet exists (179 verses minimum)
- [ ] Best prompt file identified (PROMPT{N}.md)
- [ ] Git repository clean (no uncommitted changes)

**Verification Script**:
```bash
#!/bin/bash
# verify-prerequisites.sh

EXPERIMENTS_DIR="/workspace/bible-study-tools/tbta/features/number-systems-claude-flow/experiments"

# Check train accuracy
TRAIN_ACCURACY=$(grep "Overall Accuracy" "$EXPERIMENTS_DIR/PROMPT*-RESULTS.md" | tail -1 | grep -oP '\d+\.\d+')
if (( $(echo "$TRAIN_ACCURACY < 95" | bc -l) )); then
    echo "❌ Train accuracy ($TRAIN_ACCURACY%) below 95% threshold"
    exit 1
fi

# Check test accuracy
TEST_ACCURACY=$(grep "Test Accuracy" "$EXPERIMENTS_DIR/PROMPT*-RESULTS.md" | tail -1 | grep -oP '\d+\.\d+')
if (( $(echo "$TEST_ACCURACY < 95" | bc -l) )); then
    echo "❌ Test accuracy ($TEST_ACCURACY%) below 95% threshold"
    exit 1
fi

# Check translation data
if grep -q "TO_BE_FETCHED" "$EXPERIMENTS_DIR/validate_questions.yaml"; then
    echo "❌ Translation data not fetched in validate_questions.yaml"
    exit 1
fi

# Check answer sheet
if [ ! -f "$EXPERIMENTS_DIR/validate.yaml" ]; then
    echo "❌ Answer sheet validate.yaml not found"
    exit 1
fi

# Check git status
if ! git diff-index --quiet HEAD --; then
    echo "❌ Git repository has uncommitted changes"
    exit 1
fi

echo "✅ All prerequisites verified"
exit 0
```

**Action**: Run verification script before proceeding

### Step 1.2: Identify Best Prompt

**Determine which prompt achieved ≥95% on train+test**:

```bash
# Find best prompt file
cd /workspace/bible-study-tools/tbta/features/number-systems-claude-flow/experiments
ls -t PROMPT*-RESULTS.md | head -1
```

**Record**: Best prompt filename (e.g., PROMPT3.md)

### Step 1.3: Create Validation Session

**Create session directory**:
```bash
VALIDATION_SESSION="validation-session-$(date +%Y%m%d-%H%M%S)"
mkdir -p experiments/$VALIDATION_SESSION
```

**Record session ID**: Used for coordination and traceability

---

## Phase 2: Blind Prediction Generation

### Step 2.1: Spawn Prediction Agent (Isolated)

**CRITICAL**: This agent MUST NEVER see validate.yaml answer sheet

**Agent Configuration**:
```yaml
agent_type: coder
agent_name: "Validation Prediction Generator"
isolation_level: CRITICAL
working_directory: experiments/$VALIDATION_SESSION
accessible_files:
  - experiments/PROMPT{N}.md (best prompt)
  - experiments/validate_questions.yaml (questions ONLY)
  - src/predict_numbers.py (prediction script)
forbidden_files:
  - experiments/validate.yaml (ANSWER SHEET - FORBIDDEN)
  - experiments/validate_predictions.yaml (until locked)
```

**Spawn Command**:
```bash
# Using Claude Code Task tool (PRIMARY method)
Task(
  "Prediction Generator",
  "Apply PROMPT{N}.md to validate_questions.yaml.
   Generate predictions file.
   NEVER access validate.yaml.
   Lock predictions via git commit.
   Return ONLY file path.",
  "coder"
)
```

**Alternative - Using Claude Flow MCP**:
```bash
npx claude-flow@alpha hooks pre-task \
  --description "Blind validation prediction generation" \
  --isolation "critical" \
  --forbidden-files "validate.yaml"
```

### Step 2.2: Agent Instructions

**Provide to Prediction Agent**:

```markdown
# Blind Validation Prediction Task

You are generating predictions for the validation set. You MUST NOT access the answer sheet (validate.yaml).

## Your Task

1. Load the best prompt: experiments/PROMPT{N}.md
2. Load question sheet: experiments/validate_questions.yaml
3. Apply the prompt algorithm to each verse
4. Generate predictions in this format:

```yaml
feature: number-systems
dataset: validate_predictions
generated: <timestamp>
prompt_version: PROMPT{N}
commit_sha: <will be filled after commit>
total_verses: 179
predictions:
- reference: <BOOK.CCC.VVV>
  predicted_value: <Singular|Dual|Trial|Quadrial|Paucal|Plural>
  confidence: <Very Low|Low|Medium|High|Very High>
  rationale: <brief explanation>
  rule_applied: <Level X, Rule X.X>
```

5. Save predictions to: experiments/validation-session-{timestamp}/validate_predictions.yaml
6. LOCK PREDICTIONS: git add + git commit
7. Record commit SHA in predictions file
8. Return ONLY the file path (NOT the predictions themselves)

## FORBIDDEN

- ❌ DO NOT access experiments/validate.yaml
- ❌ DO NOT read any answer sheet
- ❌ DO NOT compare predictions to actual values
- ❌ DO NOT modify predictions after git commit

## Success Criteria

- File created with all 179 verses
- Git commit SHA recorded
- Predictions locked before any validation
```

### Step 2.3: Verify Blind Testing Integrity

**After agent completes, verify**:

```bash
# Check git commit exists
PREDICTION_COMMIT=$(git log --oneline -1 experiments/validation-session-*/validate_predictions.yaml)
if [ -z "$PREDICTION_COMMIT" ]; then
    echo "❌ Predictions not committed to git"
    exit 1
fi

# Check commit timestamp is BEFORE any scoring
COMMIT_TIME=$(git show -s --format=%ct HEAD)
CURRENT_TIME=$(date +%s)
if [ $COMMIT_TIME -gt $CURRENT_TIME ]; then
    echo "❌ Commit timestamp is in the future (impossible)"
    exit 1
fi

# Verify predictions file was not modified after commit
if ! git diff HEAD experiments/validation-session-*/validate_predictions.yaml | grep -q "^$"; then
    echo "❌ Predictions file was modified after commit"
    exit 1
fi

echo "✅ Blind testing integrity verified"
```

**Record**: Commit SHA and timestamp in session log

### Step 2.4: Lock Prediction File

**Create immutable copy**:
```bash
# Copy predictions to locked directory
cp experiments/validation-session-*/validate_predictions.yaml \
   experiments/validation-session-*/validate_predictions.LOCKED.yaml

# Make read-only
chmod 444 experiments/validation-session-*/validate_predictions.LOCKED.yaml

# Record SHA256 hash for verification
sha256sum experiments/validation-session-*/validate_predictions.LOCKED.yaml > \
  experiments/validation-session-*/predictions.sha256
```

**Purpose**: Ensure predictions cannot be altered after scoring begins

---

## Phase 3: Accuracy Scoring

### Step 3.1: Spawn Scoring Agent

**This agent CAN access both predictions and answers**

**Agent Configuration**:
```yaml
agent_type: analyst
agent_name: "Validation Accuracy Scorer"
isolation_level: MEDIUM
accessible_files:
  - experiments/validation-session-*/validate_predictions.LOCKED.yaml (predictions)
  - experiments/validate.yaml (answer sheet)
  - experiments/score_predictions.py (scoring script)
```

**Spawn Command**:
```bash
# Using Claude Code Task tool
Task(
  "Accuracy Scorer",
  "Score predictions against validate.yaml.
   Calculate overall and categorical accuracy.
   Generate error analysis file.
   Create VALIDATION-RESULTS.md report.",
  "analyst"
)
```

**Alternative - Using Claude Flow MCP**:
```bash
npx claude-flow@alpha hooks pre-task \
  --description "Validation accuracy scoring and analysis"
```

### Step 3.2: Scoring Script Execution

**Provide to Scoring Agent**:

```markdown
# Validation Scoring Task

Score the locked predictions against the answer sheet.

## Your Task

1. Load predictions: experiments/validation-session-{timestamp}/validate_predictions.LOCKED.yaml
2. Load answers: experiments/validate.yaml
3. Run scoring script: python experiments/score_predictions.py
4. Calculate accuracy metrics:
   - Overall accuracy
   - By number value (Singular, Dual, Trial, Quadrial, Paucal, Plural)
   - By arbitrarity (Non-arbitrary vs Arbitrary)
   - By confidence level
   - By genre
   - By testament
5. Generate error analysis file: validate_errors.yaml
6. Create VALIDATION-RESULTS.md report

## Output Format

```yaml
# validate_errors.yaml
feature: number-systems
dataset: validate_errors
generated: <timestamp>
prompt_version: PROMPT{N}
total_errors: <count>
overall_accuracy: <percentage>
errors:
- reference: <BOOK.CCC.VVV>
  predicted: <value>
  actual: <value>
  confidence: <level>
  rule_applied: <rule>
  error_type: <e.g., "Singular→Plural">
```

## Success Criteria

- All 179 verses scored
- Accuracy metrics calculated
- Error file generated
- Results report created
```

### Step 3.3: Generate Results Report

**Template for VALIDATION-RESULTS.md**:

```markdown
# Validation Results - PROMPT{N}

**Date**: <timestamp>
**Prompt Version**: PROMPT{N}
**Commit SHA**: <prediction commit SHA>
**Total Verses**: 179

---

## Overall Performance

**Validation Accuracy**: X.X% (Y/179 correct)
**Target**: 95%
**Status**: [✅ PASS / ❌ FAIL]

---

## Performance Breakdown

### By Number Value
- Singular: X.X% (Y/Z)
- Dual: X.X% (Y/Z)
- Trial: X.X% (Y/Z)
- Quadrial: X.X% (Y/Z)
- Paucal: X.X% (Y/Z)
- Plural: X.X% (Y/Z)

### By Arbitrarity
- Non-arbitrary: X.X% (Y/Z)
- Arbitrary: X.X% (Y/Z)

### By Confidence Level
- Very High: X.X% (Y/Z)
- High: X.X% (Y/Z)
- Medium: X.X% (Y/Z)
- Low: X.X% (Y/Z)
- Very Low: X.X% (Y/Z)

### By Genre
- Narrative: X.X% (Y/Z)
- Law: X.X% (Y/Z)
- Prophecy: X.X% (Y/Z)
- Wisdom: X.X% (Y/Z)
- Epistle: X.X% (Y/Z)

---

## Error Analysis Summary

**Total Errors**: X
**Error Rate**: X.X%

**Top 3 Error Patterns**:
1. [Pattern] (count, percentage)
2. [Pattern] (count, percentage)
3. [Pattern] (count, percentage)

---

## Decision

IF accuracy ≥95%:
  ✅ PROCEED TO PEER REVIEW (Phase 4)

ELSE IF accuracy ≥90%:
  ⚠️ ANALYZE ERRORS → Decide: Systematic issues? → Back to Stage 5 or proceed with limitations

ELSE:
  ❌ RETURN TO STAGE 5 (accuracy too low for production)
```

---

## Phase 4: Error Analysis (If Accuracy <95%)

### Step 4.1: Apply 6-Step Methodology

**For each error in validate_errors.yaml, apply**:

**6-Step Error Analysis Process** (from STAGES.md):

1. **Verify Data Accuracy**
   - Check TBTA annotation is correct
   - Look for transcription errors
   - Verify verse reference matches

2. **Re-analyze Source Text**
   - Examine Greek/Hebrew morphology
   - Check explicit number markers
   - Identify noun type (abstract vs collective)

3. **Re-analyze Context**
   - Read surrounding verses
   - Check discourse participants
   - Identify narrative/theological context

4. **Cross-Reference Sources**
   - Check multiple translations (8 languages)
   - Verify translation consensus
   - Check source language dictionaries

5. **Test Hypotheses**
   - Why did algorithm predict incorrectly?
   - What should it have noticed?
   - Is this a systematic error or edge case?

6. **Final Determination**
   - TBTA correct or algorithm correct?
   - Systematic issue or acceptable limitation?
   - Proposed fix or document as known limitation?

### Step 4.2: Categorize Errors

**Error Types**:
- **Systematic**: Algorithm rule is wrong (requires fix)
- **Edge Case**: Rare scenario (acceptable <5% failure rate)
- **Data Issue**: TBTA annotation questionable (requires review)
- **Ambiguous**: Multiple valid interpretations (non-arbitrary context)

**Action for Each Type**:
- Systematic → Back to Stage 5 for algorithm refinement
- Edge Case → Document in limitations section
- Data Issue → Flag for TBTA review, proceed if <2%
- Ambiguous → Add to multi-answer framework

### Step 4.3: Make Decision

**Decision Tree**:

```
IF overall_accuracy >= 95%:
    ├─> ✅ PROCEED TO PEER REVIEW (Phase 5)
    └─> Document any <5% errors as known limitations

ELSE IF overall_accuracy >= 90% AND systematic_errors < 3%:
    ├─> ⚠️ CONDITIONAL PROCEED
    ├─> Document limitations clearly
    ├─> Flag for post-production improvement
    └─> Proceed to peer review with caveats

ELSE IF overall_accuracy >= 90% AND systematic_errors >= 3%:
    ├─> ❌ RETURN TO STAGE 5
    ├─> Fix systematic issues
    ├─> Re-run PROMPT{N+1}
    └─> Repeat validation

ELSE (overall_accuracy < 90%):
    ├─> ❌ RETURN TO STAGE 5
    ├─> Major algorithm redesign needed
    └─> Re-evaluate approach
```

---

## Phase 5: Peer Review Coordination (If Accuracy ≥95%)

### Step 5.1: Prepare Review Packages

**Create 4 review packages** (one per reviewer type):

**Package 1: Theological Reviewer**
```
review-packages/theological/
├── VALIDATION-RESULTS.md
├── THEOLOGICAL-ANALYSIS.md (multi-answer framework)
├── ARBITRARITY-CLASSIFICATION.md
├── validate_predictions.LOCKED.yaml
├── validate.yaml
├── errors/ (filtered to non-arbitrary contexts only)
└── THEOLOGICAL-REVIEW-CHECKLIST.md
```

**Package 2: Linguistic Reviewer**
```
review-packages/linguistic/
├── VALIDATION-RESULTS.md
├── TRANSLATION-DATABASE.md
├── validate_questions.yaml (with translations)
├── validate_predictions.LOCKED.yaml
├── validate.yaml
├── errors/ (filtered to translation disagreements)
└── LINGUISTIC-REVIEW-CHECKLIST.md
```

**Package 3: Methodological Reviewer**
```
review-packages/methodological/
├── VALIDATION-RESULTS.md
├── PROMPT{N}.md (algorithm)
├── PROMPT{N}-RESULTS.md (train/test)
├── STAGES.md (process followed)
├── git log (prediction commits)
└── METHODOLOGICAL-REVIEW-CHECKLIST.md
```

**Package 4: Translation Practitioner**
```
review-packages/practitioner/
├── VALIDATION-RESULTS.md
├── TRANSLATOR-IMPACT.md
├── use-case-scenarios/ (real-world examples)
├── mistakes-avoided-analysis.md
├── mistakes-made-analysis.md
└── PRACTITIONER-REVIEW-CHECKLIST.md
```

### Step 5.2: Spawn Review Agents

**Spawn 4 agents in parallel** (using Claude Code Task tool):

```bash
# Theological review
Task(
  "Theological Reviewer",
  "Review number-systems feature for theological soundness.
   Focus on Trinity contexts, multi-answer framework, denominational considerations.
   Complete THEOLOGICAL-REVIEW-CHECKLIST.md.",
  "reviewer"
)

# Linguistic review
Task(
  "Linguistic Reviewer",
  "Review number-systems feature for linguistic accuracy.
   Verify translation database, cross-language agreement, typological soundness.
   Complete LINGUISTIC-REVIEW-CHECKLIST.md.",
  "reviewer"
)

# Methodological review
Task(
  "Methodological Reviewer",
  "Review number-systems feature for scientific rigor.
   Verify STAGES.md compliance, blind testing integrity, error analysis quality.
   Complete METHODOLOGICAL-REVIEW-CHECKLIST.md.",
  "reviewer"
)

# Practitioner review
Task(
  "Translation Practitioner",
  "Review number-systems feature for practical utility.
   Assess real-world scenarios, net benefit, workflow integration.
   Complete PRACTITIONER-REVIEW-CHECKLIST.md.",
  "reviewer"
)
```

**Coordination**:
```bash
npx claude-flow@alpha hooks pre-task --description "Peer review coordination - 4 parallel reviews"
```

### Step 5.3: Collect Review Results

**Wait for all 4 reviews to complete**

**Aggregate results**:
```yaml
# peer-review-results.yaml
feature: number-systems
review_date: <timestamp>
validation_accuracy: X.X%

theological_review:
  status: [APPROVED / CONDITIONAL / REJECTED]
  reviewer: <agent name>
  concerns: [list]
  recommendations: [list]

linguistic_review:
  status: [APPROVED / CONDITIONAL / REJECTED]
  reviewer: <agent name>
  concerns: [list]
  recommendations: [list]

methodological_review:
  status: [APPROVED / CONDITIONAL / REJECTED]
  reviewer: <agent name>
  concerns: [list]
  recommendations: [list]

practitioner_review:
  status: [APPROVED / CONDITIONAL / REJECTED]
  reviewer: <agent name>
  concerns: [list]
  recommendations: [list]

overall_decision:
  status: [APPROVED / CONDITIONAL / REJECTED]
  conditions: [list if conditional]
  blocking_issues: [list if rejected]
```

### Step 5.4: Make Final Decision

**Approval Criteria**:
- ALL 4 reviews: APPROVED or CONDITIONAL (no REJECTED)
- Validation accuracy ≥95%
- No blocking theological issues
- No blocking methodological issues

**Decision**:
- **APPROVED**: Proceed to production deployment
- **CONDITIONAL**: Proceed with documented limitations and conditions
- **REJECTED**: Return to Stage 5 for major revisions

---

## Phase 6: Production Readiness Certification

### Step 6.1: Generate Production Certification

**Create PRODUCTION-CERTIFICATION.md**:

```markdown
# Production Readiness Certification
## Number Systems TBTA Feature

**Certification Date**: <timestamp>
**Certifying Agent**: Tester Agent
**Status**: [✅ CERTIFIED / ⚠️ CONDITIONAL / ❌ NOT CERTIFIED]

---

## Certification Criteria

### Stage 5 Completion
- [x] Train accuracy ≥95%: X.X%
- [x] Test accuracy ≥95%: X.X%
- [x] Algorithm documented: PROMPT{N}.md
- [x] Error analysis completed: PROMPT{N}-RESULTS.md

### Stage 6 Validation
- [x] Blind testing protocol followed
- [x] Validation accuracy ≥95%: X.X%
- [x] Error analysis completed (if <95%)
- [x] Predictions locked via git commit

### Peer Review
- [x] Theological review: [APPROVED / CONDITIONAL / REJECTED]
- [x] Linguistic review: [APPROVED / CONDITIONAL / REJECTED]
- [x] Methodological review: [APPROVED / CONDITIONAL / REJECTED]
- [x] Practitioner review: [APPROVED / CONDITIONAL / REJECTED]

### Documentation
- [x] THEOLOGICAL-ANALYSIS.md complete
- [x] TRANSLATION-DATABASE.md complete
- [x] TRANSLATOR-IMPACT.md complete
- [x] VALIDATION-RESULTS.md complete
- [x] LEARNINGS.md complete

---

## Known Limitations

[Document any <5% error patterns or edge cases]

---

## Conditions (If Conditional Certification)

[List any conditions or caveats for production use]

---

## Certification Statement

I certify that the number-systems TBTA feature has completed Stages 1-6 of the TBTA development methodology and is [READY / CONDITIONALLY READY / NOT READY] for production deployment.

**Signature**: Tester Agent
**Date**: <timestamp>
```

### Step 6.2: Update Feature Status

**Update number-systems-claude-flow/README.md**:
```markdown
## Status: ✅ PRODUCTION READY

**Validation Accuracy**: X.X%
**Peer Review**: 4/4 APPROVED
**Certification Date**: <date>
**Production Deployment**: APPROVED
```

### Step 6.3: Deploy to Production

**Final steps**:
1. Merge feature branch to main
2. Tag production release: `git tag v1.0.0-number-systems`
3. Update TBTA feature registry
4. Notify stakeholders
5. Close Stage 6 in tracking system

---

## Coordination Hooks

### Pre-Validation
```bash
npx claude-flow@alpha hooks pre-task \
  --description "Stage 6 blind validation testing" \
  --task-id "number-systems-validation"

npx claude-flow@alpha hooks session-restore \
  --session-id "swarm-number-systems"
```

### Post-Prediction
```bash
npx claude-flow@alpha hooks post-task \
  --task-id "validation-predictions-locked" \
  --memory-key "swarm/tester/predictions-commit-sha"
```

### Post-Scoring
```bash
npx claude-flow@alpha hooks post-task \
  --task-id "validation-scoring-complete" \
  --memory-key "swarm/tester/validation-accuracy"
```

### Post-Review
```bash
npx claude-flow@alpha hooks post-task \
  --task-id "peer-review-complete" \
  --memory-key "swarm/tester/peer-review-results"

npx claude-flow@alpha hooks session-end \
  --export-metrics true
```

---

## Quality Assurance Checks

### Blind Testing Integrity
- [ ] Prediction agent never accessed validate.yaml
- [ ] Predictions committed before scoring
- [ ] Git commit SHA recorded in predictions file
- [ ] No modifications to predictions after commit
- [ ] SHA256 hash verification passed

### Scoring Accuracy
- [ ] All 179 verses scored
- [ ] No missing predictions
- [ ] Accuracy metrics calculated correctly
- [ ] Error analysis file generated
- [ ] Results report complete

### Peer Review Completeness
- [ ] All 4 review types completed
- [ ] Each review has checklist filled
- [ ] Concerns documented
- [ ] Recommendations recorded
- [ ] Overall decision clear

### Documentation Completeness
- [ ] VALIDATION-RESULTS.md exists
- [ ] THEOLOGICAL-ANALYSIS.md exists
- [ ] TRANSLATOR-IMPACT.md exists
- [ ] PRODUCTION-CERTIFICATION.md exists
- [ ] All files committed to git

---

## Troubleshooting

### Issue: Prediction agent accessed validate.yaml
**Solution**: ABORT and restart. Scientific integrity compromised.

### Issue: Predictions modified after commit
**Solution**: ABORT and restart. Use .LOCKED.yaml copy only.

### Issue: Validation accuracy <95% but no systematic errors
**Solution**: Document limitations, proceed to peer review with caveats.

### Issue: One peer review REJECTED
**Solution**: Address blocking issues, re-submit for review.

### Issue: Translation data still TO_BE_FETCHED
**Solution**: Fetch translations before validation (see VALIDATION-READINESS.md).

---

## Success Criteria Summary

**Minimum Requirements for Production Certification**:
1. ✅ Validation accuracy ≥95%
2. ✅ Blind testing protocol followed (no integrity violations)
3. ✅ 4/4 peer reviews APPROVED or CONDITIONAL (no REJECTED)
4. ✅ All required documentation complete
5. ✅ Known limitations documented (if any)
6. ✅ Git commits present for all locked predictions

**Conditional Certification Allowed If**:
- Accuracy ≥90% with <5% systematic errors
- Peer reviews CONDITIONAL with clear mitigation plan
- Known limitations clearly documented
- Net benefit positive for translators

**Rejection Criteria**:
- Accuracy <90%
- Any peer review REJECTED on blocking issue
- Blind testing integrity compromised
- Systematic errors >5%

---

**Protocol Version**: 1.0
**Created**: 2025-11-18T01:51:40Z
**Last Updated**: 2025-11-18T01:51:40Z
**Status**: READY FOR EXECUTION (pending PROMPT2/PROMPT3 completion)
