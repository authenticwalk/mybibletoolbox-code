# Methodological Review: {Feature Name}

**Reviewer**: Methodological Subagent
**Date**: YYYY-MM-DD
**Prompt Version**: PROMPT{N}.md
**Validation Accuracy**: {X}%

---

## Review Assumptions

I am reviewing this work assuming the author cut corners:
- May have insufficient sample size (< 100 per value)
- May have unbalanced sampling (OT/NT, genres)
- May not have followed 6-step error analysis
- May not have locked predictions (git discipline)
- May have skipped external validation (if applicable)

---

## Sample Size Verification

### Dataset Statistics

**Train Set**:
- Total verses: {count}
- Verses per value: {breakdown}
- Minimum per value: {min}

**Test Set**:
- Total verses: {count}
- Verses per value: {breakdown}
- Minimum per value: {min}

**Validate Set**:
- Total verses: {count}
- Verses per value: {breakdown}
- Minimum per value: {min}

**Assessment**:
- [ ] All values have ≥100 verses in each set
- [ ] Total sample size adequate for statistical power
- [ ] No single value dominates (balanced)

**Issues Found**: {none / list issues}

---

## Balanced Sampling Verification

### Testament Distribution

**Old Testament**: {count} verses ({percentage}%)
**New Testament**: {count} verses ({percentage}%)

**Assessment**:
- [ ] Proportional to biblical corpus
- [ ] Both testaments represented
- [ ] No extreme imbalance

**Issues Found**: {none / list issues}

### Genre Distribution

**Narrative**: {count} verses
**Poetry**: {count} verses
**Prophecy**: {count} verses
**Epistle**: {count} verses
**Other**: {count} verses

**Assessment**:
- [ ] Multiple genres represented
- [ ] Distribution matches feature relevance
- [ ] No single genre dominance

**Issues Found**: {none / list issues}

### Book Distribution

**Most represented book**: {book} ({count} verses)
**Least represented book**: {book} ({count} verses)

**Assessment**:
- [ ] Multiple books represented
- [ ] No excessive concentration in single book
- [ ] Distribution reasonable for feature

**Issues Found**: {none / list issues}

### Adversarial Selection

**Typical cases**: {count}
**Adversarial cases**: {count}

**Assessment**:
- [ ] Adversarial cases included (edge cases)
- [ ] Challenging contexts represented
- [ ] Not just "easy" verses

**Issues Found**: {none / list issues}

---

## Error Analysis Rigor

### 6-Step Process Verification

Review LEARNINGS.md for each error:

**Step 1: Data Verification**
- [ ] TBTA annotation accuracy checked
- [ ] Verse reference verified

**Step 2: Source Text Re-analysis**
- [ ] Greek/Hebrew consulted
- [ ] Multiple translations checked

**Step 3: Context Re-analysis**
- [ ] Surrounding verses reviewed
- [ ] Chapter context considered

**Step 4: Cross-References**
- [ ] 3+ translations consulted
- [ ] Commentaries referenced (if available)

**Step 5: Hypothesis Testing**
- [ ] Error cause identified
- [ ] Alternative approaches considered

**Step 6: Final Determination**
- [ ] TBTA correctness confirmed
- [ ] Algorithmic fix proposed

**Assessment**:
- [ ] All errors have 6-step analysis documented
- [ ] Analysis depth sufficient
- [ ] Learnings translated to prompt improvements

**Issues Found**: {none / list issues}

---

## Locked Predictions Discipline

### Git Commit Verification

Check `experiments/predictions/commit-shas.yaml`:

**PROMPT1 predictions locked**: [YES / NO]
- Commit SHA: {sha or "MISSING"}

**PROMPT2 predictions locked**: [YES / NO]
- Commit SHA: {sha or "MISSING"}

**PROMPT{N} predictions locked**: [YES / NO]
- Commit SHA: {sha or "MISSING"}

**Assessment**:
- [ ] All prompt predictions committed BEFORE seeing answers
- [ ] Git history shows proper discipline
- [ ] No evidence of answer contamination

**Issues Found**: {none / list issues}

---

## External Validation (If Applicable)

**Feature has observable translation differences**: [YES / NO / UNCERTAIN]

If YES:

### Marking Languages Identified

**Languages**: {list}
**Language Families**: {list}

### Translation Validation Conducted

**Translations Checked**: {list}
**Agreement Rate**: {percentage}%

**Assessment**:
- [ ] External validation attempted
- [ ] Agreement rate ≥95%
- [ ] Divergences documented and explained

**Issues Found**: {none / list issues}

If NO or UNCERTAIN:

**Rationale for skipping**: {explanation}

---

## Iteration Quality

### Prompt Evolution

**Total prompts created**: {count}
**Accuracy progression**:
- PROMPT1: {X}%
- PROMPT2: {X}%
- PROMPT{N}: {X}%

**Assessment**:
- [ ] Multiple approaches tried (not just refinement)
- [ ] Clear progression in accuracy
- [ ] Iterations driven by error analysis
- [ ] Stopped when diminishing returns

**Issues Found**: {none / list issues}

---

## Critical Issues (Must Fix Before Production)

<!-- Only include if issues found -->

### Issue 1: {Description}

**Evidence**: {specific data}

**Impact**: Methodological unsoundness undermines results

**Recommendation**: {how to fix}

---

## Material Feedback (Should Address)

<!-- Only include if issues found -->

### Feedback 1: {Description}

**Evidence**: {examples}

**Impact**: Reduces methodological rigor

**Recommendation**: {improvement suggestion}

---

## Non-Material Observations

<!-- Minor points for consideration -->

- {Observation 1}
- {Observation 2}

---

## Overall Assessment

**Critical Issues Found**: {count}
**Material Feedback Items**: {count}
**Non-Material Observations**: {count}

**Status**: [PASS / MATERIAL FEEDBACK / FAIL]

- **PASS**: Methodology sound, proceed to production
- **MATERIAL FEEDBACK**: Methodological gaps require attention
- **FAIL**: Methodological flaws require restart

**Recommendation**: {specific next steps}

---

## Methodological Rigor Score

Rate 1-5 in each category:

- **Sample Size Adequacy**: {1-5}/5
- **Balanced Sampling**: {1-5}/5
- **Error Analysis Depth**: {1-5}/5
- **Git Discipline**: {1-5}/5
- **Iteration Quality**: {1-5}/5

**Overall Score**: {average}/5

**Approval for Production**: [YES / NO / CONDITIONAL]

**Conditions (if applicable)**: {list required changes}
