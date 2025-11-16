# Person Systems: Approach Analysis

**Feature**: Person Systems (Clusivity, Obviation)
**Status**: Methodology developed through iterative refinement
**Final Accuracy**: 73% adversarial test (meets 60-70% target), 50-60% random test (below 80-90% target)

---

## Summary

This document consolidates the various approaches analyzed for predicting person-system features (especially clusivity - inclusive vs exclusive first-person plural pronouns) in Biblical texts. The feature underwent multiple iterations, evolving from simple discourse analysis to a sophisticated hierarchical framework.

**Key Finding**: Theological and semantic factors are more determinative than grammatical analysis alone.

---

## Approaches Analyzed

### Approach 1: Basic Discourse Analysis (Experiment 001)

**Source**: `experiment-001.md`

**Framework**: 5-step identification method
1. Identify the Speaker (role/authority)
2. Identify the Addressee (presence/relationship)
3. Identify the Action/Content (participation capacity)
4. Apply Discourse Analysis (exclusive vs inclusive indicators)
5. Consider Theological Context (divine vs human, salvific vs creative)

**Strengths**:
- Simple, systematic approach
- Good foundation for theological reasoning
- Clear decision points

**Weaknesses**:
- No priority ordering (all steps weighted equally)
- Lacked explicit prompts for LLM
- No early termination strategy

**Outcome**: Established core principles but needed refinement

---

### Approach 2: Five-Level Hierarchical Framework

**Source**: `clusivity-framework.md`

**Framework**: Ontological priority with cascading checks
1. **Ontological Analysis** - Divine vs human nature (highest priority)
2. **Capability Analysis** - Can addressee participate?
3. **Group Identity Analysis** - Same vs different group membership
4. **Discourse Function Analysis** - Rhetorical purpose
5. **Grammatical Cues** - Explicit markers (lowest priority)

**Theological Patterns Identified**:
- Divine creative/judicial acts → EXCLUSIVE (Genesis 1:26, 3:22, 11:7)
- Prayer contexts → EXCLUSIVE (addressee is God, not included in "we")
- Apostolic eyewitness → EXCLUSIVE (non-apostles not witnesses)
- Community exhortation → INCLUSIVE (shared experience)

**Strengths**:
- Clear priority ordering (theology > discourse > grammar)
- Early termination (most cases resolved at levels 1-2)
- Validated patterns across verse categories

**Weaknesses**:
- Still conceptual, not yet LLM-executable prompts
- Lacked specific prompt engineering

**Accuracy**: 100% on 11 training verses (4 divine speech, 3 prayer, 2 apostolic, 2 community)

---

### Approach 3: Hierarchical Prompting Framework (Algorithm v1)

**Source**: `METHODOLOGY.md`, `training/ALGORITHM-v1.md`

**Framework**: LLM-executable prompts with priority ordering
1. **Theological/Semantic Prompts** (Level 1) - Ask LLM about meaning first
2. **Capability/Restriction Prompts** (Level 2) - Can participants perform action?
3. **Discourse Function Prompts** (Level 3) - Rhetorical purpose and speech act
4. **Grammatical Cue Prompts** (Level 4) - Explicit markers in text
5. **Baseline** (Level 5) - Default to most common value (65% exclusive)

**Key Innovation**: Converted conceptual framework into executable LLM prompts

**Theological Analysis Prompt** (Level 1 - most effective):
- Who is speaking? (Divine, Apostolic, Prophet, Believer)
- Who is addressed? (God, Believers, Unbelievers)
- Does this involve divine prerogative? (creation, omniscience, judgment → restricts participation)
- Does this describe salvific/shared experience? (justification, faith → shared participation)
- Is there authority structure? (apostolic witness, prophetic role → limited participation)
- Does this express community identity? (unity, worship → inclusive participation)

**Strengths**:
- Fully executable by LLM
- Leverages LLM strengths (theological/semantic analysis)
- Clear decision points at each level
- Documented reasoning output

**Weaknesses**:
- Initial prompts too verbose
- Missed edge cases in testing

**Accuracy**: 100% on 7 training verses, 73% on 11 adversarial test verses

---

### Approach 4: Refined Prompting (Algorithm v2)

**Source**: `training/ALGORITHM-v2.md`

**Changes from v1**:
- Simplified prompt language for clarity
- Added explicit edge case handling
- Refined theological categories
- Improved confidence scoring

**Strengths**:
- More concise prompts
- Better edge case coverage

**Accuracy**: Projected 70-75% (not fully validated)

---

### Approach 5: Production Algorithm (Algorithm v2.1)

**Source**: `training/ALGORITHM-v2.1-PRODUCTION.md`

**Changes from v2**:
- Incorporated error analysis from failed test cases
- Enhanced capability detection
- Refined discourse function analysis
- Added context sensitivity for ambiguous cases

**Status**: ⚠️ UNTESTED
- Projected accuracy: 75-80%
- Not yet validated on test set
- Cannot claim "production ready" without validation

---

## External Validation Approach

**Source**: `TRANSLATION-VALIDATION.md`, `clusivity/` directory

**Innovation**: Validate predictions against real Bible translations (not just TBTA)

**Languages Used** (9 translations with grammatical clusivity):
- Austronesian family
- Oceanic languages
- Languages that grammatically mark inclusive/exclusive distinction

**Method**:
1. Predict clusivity using hierarchical framework
2. Check actual translation in person-marking languages
3. Verify 100% agreement

**Results**: 7/7 verses validated (100% agreement with real translations)

**Value**: Proves real-world applicability beyond TBTA alignment

---

## Cross-Cutting Patterns Discovered

### Divine Speech Pattern (100% consistent)
- Genesis 1:26 "Let us make man" → EXCLUSIVE (only God creates)
- Genesis 3:22 "Like one of us" → EXCLUSIVE (divine knowledge)
- Genesis 11:7 "Let us go down" → EXCLUSIVE (divine judgment)

**Rule**: Divine creative/judicial acts always exclude human participation

### Prayer Context Pattern
- When addressing God → EXCLUSIVE (God not included in "our")
- Teaching prayer → May be INCLUSIVE (all believers learn)
- Intercessory prayer → Context determines

### Apostolic Authority Pattern
- Eyewitness testimony → EXCLUSIVE (non-witnesses excluded)
- Apostolic "we" → Initially EXCLUSIVE (unique role)
- General teaching → May shift to INCLUSIVE (shared faith)

### Community Identity Pattern
- Unity, worship, shared faith → INCLUSIVE
- Ethnic/religious distinctions → EXCLUSIVE
- Exhortation to action → Typically INCLUSIVE

---

## What Worked Best

1. **Theological analysis first** - 70%+ of cases resolved by theological factors alone
2. **Capability checking second** - Most remaining cases resolved here
3. **Early termination** - Avoid over-analyzing simple cases
4. **LLM-friendly prompts** - Natural language questions work better than formal logic
5. **External validation** - Real translations confirm theoretical predictions

---

## What Didn't Work

1. **Grammar-first approaches** - Too many ambiguous cases
2. **Single-factor analysis** - No one factor sufficient
3. **Overly complex prompts** - LLM performs worse with verbose instructions
4. **Small test sets** - 20 verses insufficient for statistical confidence
5. **Ignoring edge cases** - Generic prompts miss contextual nuances

---

## Lessons for Future Features

1. **Start with meaning, not form** - Semantic/theological factors trump grammatical cues
2. **Use hierarchical prompting** - Priority ordering with early termination
3. **Validate externally when possible** - Real translations confirm predictions
4. **Iterate based on failures** - Systematic error analysis drives improvement
5. **Lock predictions** - Git commit before checking TBTA (prevents cheating)
6. **Document reasoning** - Each prompt should output rationale, not just answer

---

## Remaining Gaps

1. **Untested algorithm** - v2.1 needs validation on test set
2. **Random test failure** - 50-60% vs 80-90% target suggests overfitting or blind spots
3. **Small validation set** - Only 2 verses checked against actual TBTA
4. **Documentation bloat** - 57 files excessive for feature documentation

---

## Recommended Next Steps

Per MIGRATION-PLAN.md:
1. Test algorithm v2.1 on existing test set (21 verses)
2. Investigate random test failure (analyze the 5 failed cases)
3. Generate proper validate.yaml with 100 verses per value (use subagent)
4. Complete Stage 6 peer review with multiple critical reviewers
5. Document actual accuracy, not projected

---

**Conclusion**: The hierarchical prompting framework represents significant innovation, but requires completion of validation to confirm production readiness. The external validation approach (checking real translations) is a unique contribution worth preserving.
