# Linguistic Review: {Feature Name}

**Reviewer**: Linguistic Subagent
**Date**: YYYY-MM-DD
**Prompt Version**: PROMPT{N}.md
**Validation Accuracy**: {X}%

---

## Review Assumptions

I am reviewing this work assuming the author missed linguistic nuances:
- May not account for genre differences (narrative vs poetry vs epistle)
- May confuse grammar with semantics
- May not handle discourse complexity (quoted speech, multiple speakers)
- May miss register shifts (formal vs informal)
- May not distinguish narrative vs direct address

---

## Test Cases Evaluated

### Test 1: Genre Handling

**Narrative Verses**: {list 2-3}
**Poetry Verses**: {list 2-3}
**Epistle Verses**: {list 2-3}
**Prophetic Verses**: {list 2-3}

**Assessment**:
- [ ] Algorithm adapts to narrative discourse patterns
- [ ] Poetry parallelism recognized
- [ ] Epistolary argumentation structure understood
- [ ] Prophetic oracle patterns identified

**Issues Found**: {none / list issues}

### Test 2: Grammar vs Semantics Distinction

**Verses Tested**: {list 3-5 with grammatical/semantic ambiguity}

**Assessment**:
- [ ] Grammatical markers correctly identified
- [ ] Semantic interpretation doesn't overrule grammar
- [ ] Form-function relationships maintained

**Issues Found**: {none / list issues}

### Test 3: Discourse Complexity

**Quoted Speech**: {list 2-3 verses}
**Multiple Speakers**: {list 2-3 verses}
**Embedded Discourse**: {list 2-3 verses}

**Assessment**:
- [ ] Quoted speech boundaries recognized
- [ ] Speaker shifts identified
- [ ] Embedded discourse levels maintained
- [ ] Direct vs indirect discourse distinguished

**Issues Found**: {none / list issues}

### Test 4: Narrative vs Direct Address

**Narrative (3rd person)**: {list 2-3 verses}
**Direct Address (2nd person)**: {list 2-3 verses}

**Assessment**:
- [ ] Narrative voice recognized
- [ ] Direct address identified
- [ ] Distinction maintained consistently

**Issues Found**: {none / list issues}

---

## Critical Issues (Must Fix Before Production)

<!-- Only include if issues found -->

### Issue 1: {Description}

**Evidence**:
- Verse: {REF}
- Predicted: {value}
- Actual: {value}
- **Problem**: {linguistic error described}

**Impact**: Leads to {specific misunderstanding of linguistic structure}

**Recommendation**: {how to fix in prompt}

---

## Material Feedback (Should Address)

<!-- Only include if issues found -->

### Feedback 1: {Description}

**Evidence**: {examples}

**Impact**: Reduces linguistic precision

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

- **PASS**: No critical issues, non-material feedback only → Proceed to production
- **MATERIAL FEEDBACK**: Issues require prompt refinement → Return to Stage 5
- **FAIL**: Critical linguistic flaws → Major rework needed

**Recommendation**: {specific next steps}

---

## Linguistic Accuracy Score

Rate 1-5 in each category:

- **Genre Sensitivity**: {1-5}/5
- **Grammar-Semantics Balance**: {1-5}/5
- **Discourse Analysis**: {1-5}/5
- **Pragmatic Awareness**: {1-5}/5

**Overall Score**: {average}/5

**Approval for Production**: [YES / NO / CONDITIONAL]

**Conditions (if applicable)**: {list required changes}
