# Feature Audit Template

Use this template to audit existing TBTA features against the STAGES.md workflow.

## Feature: {feature-name}

**Audit Date**: {YYYY-MM-DD}
**Auditor**: {agent or human name}

---

## Stage Completion Status

### Stage 1: Research TBTA Documentation ✅/⚠️/❌

**Status**: {completed | partial | not-done}

**Evidence**:
- [ ] Feature README.md exists and describes the feature
- [ ] README includes feature definition from TBTA docs
- [ ] README includes theological/linguistic context
- [ ] README references CROSS-FEATURE-LEARNINGS.md

**Files Found**:
- `README.md` - {brief assessment}
- Other docs: {list}

**Gaps/Issues**:
- {list any missing elements or problems}

---

### Stage 2: Language Study ✅/⚠️/❌

**Status**: {completed | partial | not-done}

**Evidence**:
- [ ] README includes language family analysis
- [ ] Lists which languages grammatically encode this feature
- [ ] Provides target translation scenarios

**Files Found**:
- {relevant sections in README or separate docs}

**Gaps/Issues**:
- {list any missing elements or problems}

---

### Stage 3: Scholarly and Internet Research ✅/⚠️/❌

**Status**: {completed | partial | not-done}

**Evidence**:
- [ ] README includes latest research findings
- [ ] References scholarly articles or linguistic papers
- [ ] Incorporates web research on the topic

**Files Found**:
- {relevant sections or references}

**Gaps/Issues**:
- {list any missing elements or problems}

---

### Stage 4: Generate Proper Test Set ✅/⚠️/❌

**Status**: {completed | partial | not-done}

**Evidence**:
- [ ] `train.yaml` exists (40% of data)
- [ ] `test.yaml` exists (30% of data)
- [ ] `validate.yaml` exists (30% of data)
- [ ] Each file contains 100 verses per value (or documented reason for different size)
- [ ] Files include TBTA values for verification
- [ ] Balanced sampling across books/genres

**Files Found**:
- `experiments/train.yaml` - {size, structure}
- `experiments/test.yaml` - {size, structure}
- `experiments/validate.yaml` - {size, structure}

**Alternative Approaches Used** (if not YAML):
- {describe what was done instead, e.g., adversarial-test/random-test folders}

**Gaps/Issues**:
- {list any missing elements or problems}

---

### Stage 5: Propose Hypothesis and First Prompt ✅/⚠️/❌

**Status**: {completed | partial | not-done}

**Evidence**:
- [ ] `ANALYSIS.md` exists with multiple approaches (target: 12)
- [ ] Iterative prompts exist (PROMPT1.md, PROMPT2.md, ...)
- [ ] `LEARNINGS.md` documents debugging and refinement
- [ ] Achieved 100% accuracy on stated values
- [ ] Achieved 95% accuracy on dominant values
- [ ] Final algorithm/prompt is minimal and refined

**Files Found**:
- `experiments/ANALYSIS.md` - {number of approaches}
- `experiments/PROMPT*.md` - {how many iterations}
- `experiments/LEARNINGS.md` - {quality assessment}
- `training/ALGORITHM-v*.md` - {which versions exist}

**Accuracy Results**:
- Stated values: {percentage}% ({X} correct out of {Y} total)
- Dominant values: {percentage}% ({X} correct out of {Y} total)

**Gaps/Issues**:
- {list any missing elements or problems}

---

### Stage 6: Test Against Validate Set ✅/⚠️/❌

**Status**: {completed | partial | not-done}

**Evidence**:
- [ ] Validation was done using subagent (to prevent cheating)
- [ ] `VALIDATION-RESULTS.md` exists with final accuracy
- [ ] Peer review was conducted (3+ reviewers)
- [ ] Peer review feedback was documented
- [ ] Issues from peer review were addressed

**Files Found**:
- `experiments/VALIDATION-RESULTS.md` - {summary}
- `PEER-REVIEW.md` - {reviewer count, feedback quality}
- Evidence of subagent usage: {yes/no, details}

**Final Accuracy**:
- Overall: {percentage}%
- Per-value breakdown: {if available}

**Gaps/Issues**:
- {list any missing elements or problems}

---

## Overall Assessment

**Completion Summary**:
- Stages completed: {X} / 6
- Stages partial: {Y} / 6
- Stages not done: {Z} / 6

**Overall Status**: {fully-complete | mostly-complete | partially-complete | needs-major-work}

**Complies with STAGES.md?**: {yes | mostly | partially | no}

---

## Recommendations

**Priority 1 (Critical gaps)**:
1. {most important thing to fix}
2. {next most important}

**Priority 2 (Important improvements)**:
1. {nice to have improvements}
2. {additional enhancements}

**Priority 3 (Nice to have)**:
1. {optional improvements}

---

## Notes

### What This Feature Did Well
- {list strengths}

### What Deviates from STAGES.md
- {list differences, with rationale if available}

### Historical Context
- This feature was built using: {previous methodology description}
- Valuable learnings preserved: {what should be kept}
- Migration path: {how to align with STAGES.md if needed}

---

**Audit Complete**: {yes/no}
**Requires Follow-up**: {yes/no, with details}
