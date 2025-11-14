# TBTA Discourse-Level Context Strategy - Overview

**Date**: 2025-11-05
**Status**: Proposed
**Priority**: HIGH - Affects multiple core features

---

## Executive Summary

Current TBTA implementation processes verses in isolation, but multiple critical features require **discourse-level context** beyond single verse boundaries. This overview compares three approaches to address this limitation.

**Recommendation**: Start with **Approach 1 (LLM Memory)** for immediate implementation, with **Approach 2 (Expanded Context Window)** as fallback for accuracy-critical features.

---

## The Problem: Verse-Level Scope Limitation

### Current Limitation

```python
# Current approach
for verse_ref in chapter:
    verse_data = load_verse(verse_ref)
    features = extract_features(verse_data)  # ❌ No context from other verses
    save_features(verse_ref, features)
```

**Impact**: Features requiring discourse history **cannot be accurately predicted** without context.

---

## Features Requiring Discourse Context

### Critical Dependencies (HIGH Priority)

1. **Participant Tracking** (9 states)
   - **Problem**: Cannot distinguish "First Mention" vs "Routine" without tracking prior appearances
   - **Example**: Matthew 24:46 - "servant" continues from 24:45, not a new entity
   - **Impact**: 100% error rate on state classification without context

2. **NounListIndex**
   - **Problem**: Cannot assign consistent indices across verses
   - **Example**: Same entity needs same index throughout discourse unit
   - **Impact**: Pronouns cannot inherit indices from antecedents

3. **Surface Realization**
   - **Problem**: Zero anaphora requires discourse history to resolve
   - **Example**: "Ø went home" - who went? Need prior context
   - **Impact**: Cannot determine what is elided

4. **Topic/Focus Tracking**
   - **Problem**: Topic continuity requires tracking across boundaries
   - **Example**: Topic shift detection requires knowing previous topic
   - **Impact**: Cannot identify thematic structure

### Medium Dependencies

5. **Notional Structure** - Discourse structure spans multiple clauses/verses
6. **Coreference Resolution** - Pronouns reference entities mentioned earlier
7. **Definiteness** - First mention vs subsequent mention distinction

---

## Concrete Failure Example

**Without Context** (WRONG):
```yaml
MAT.024.046:
  entities:
    - text: "servant"
      participant_tracking: "First Mention"  # ❌ Wrong!
      noun_index: 7                          # ❌ Inconsistent!
    - text: "lord"
      participant_tracking: "First Mention"  # ❌ Wrong!
      noun_index: 8                          # ❌ Inconsistent!
```

**With Chapter Context** (CORRECT):
```yaml
# Context from MAT.024.045:
#   - "master" introduced (index 5)
#   - "servant" introduced (index 6)

MAT.024.046:
  entities:
    - text: "servant"
      participant_tracking: "Routine"        # ✓ Continues from 24:45
      noun_index: 6                          # ✓ Inherits from first mention
      antecedent: "MAT.024.045:servant"
    - text: "lord"
      participant_tracking: "Routine"        # ✓ Same as "master"
      noun_index: 5                          # ✓ Coreference with master
      antecedent: "MAT.024.045:master"
```

**Accuracy Impact**: 0% → 100% with proper context

---

## Three Proposed Solutions

### Approach 1: LLM Memory (Recommended First)

**Concept**: Leverage LLM's existing knowledge of Bible content from training data.

**Pros**:
- ✅ Zero infrastructure changes
- ✅ Immediate implementation (2 weeks)
- ✅ Leverages existing knowledge
- ✅ Cost-effective

**Cons**:
- ⚠️ Accuracy uncertainty
- ⚠️ Less well-known books may have sparse coverage

**Expected Accuracy**: 80-90% for well-known books
**Implementation Time**: 2 weeks

**Details**: See [APPROACH-1-LLM-MEMORY.md](APPROACH-1-LLM-MEMORY.md)

---

### Approach 2: Expanded Context Window (Fallback/Hybrid)

**Concept**: Load and process full chapters, maintaining entity registry across verse boundaries.

**Pros**:
- ✅ 100% accuracy potential
- ✅ Explicit tracking
- ✅ Systematic and debuggable

**Cons**:
- ⚠️ Infrastructure changes required
- ⚠️ Memory overhead
- ⚠️ Higher token costs

**Expected Accuracy**: 95-100%
**Implementation Time**: 5 weeks

**Details**: See [APPROACH-2-EXPANDED-CONTEXT.md](APPROACH-2-EXPANDED-CONTEXT.md)

---

### Approach 3: Two-Pass Processing (Comprehensive)

**Concept**: First pass extracts chapter-level discourse structure, second pass uses that structure for verse-level feature prediction.

**Pros**:
- ✅ Best accuracy potential
- ✅ Separation of concerns
- ✅ Reusable structure
- ✅ Human reviewable

**Cons**:
- ⚠️ Most complex
- ⚠️ Highest cost
- ⚠️ Error propagation from Pass 1 to Pass 2

**Expected Accuracy**: 95-100%
**Implementation Time**: 8 weeks

**Details**: See [APPROACH-3-TWO-PASS.md](APPROACH-3-TWO-PASS.md)

---

## Comparison Matrix

| Criterion | Approach 1: LLM Memory | Approach 2: Expanded Context | Approach 3: Two-Pass |
|-----------|----------------------|---------------------------|---------------------|
| **Implementation Time** | 2 weeks | 5 weeks | 8 weeks |
| **Accuracy (est.)** | 80-90% | 95-100% | 95-100% |
| **Infrastructure Change** | None | Moderate | Significant |
| **Token Cost** | Low (verse-level) | Medium (chapter context) | High (2x passes) |
| **Debuggability** | Low (LLM black box) | High (explicit registry) | High (structured output) |
| **Scalability** | Excellent | Good | Good |
| **Failure Handling** | Graceful degradation | Deterministic | Intermediate caching |
| **Human Review** | Hard to verify | Registry inspectable | Pass 1 reviewable |
| **Best For** | Rapid deployment | Accuracy-critical | Long-term comprehensive |

---

## Recommended Strategy: Hybrid Approach

**Start with Approach 1 (LLM Memory)**, then **selectively apply Approach 2** for accuracy-critical features.

### Rationale

1. **Immediate value** - Approach 1 can be deployed in 2 weeks
2. **Low risk** - No pipeline changes, easy to test and iterate
3. **Validates need** - Proves discourse context improves accuracy
4. **Identifies gaps** - Testing reveals which books/features need explicit tracking
5. **Incremental investment** - Only build Approach 2 where Approach 1 fails

### Implementation Sequence

**Milestone 1: LLM Memory Baseline** (Weeks 1-2)
- Implement discourse-aware prompts
- Test on Participant Tracking (highest priority)
- Measure accuracy on 50 test verses
- **Go/No-Go Decision**: If >85% accuracy → Deploy broadly, If <85% → Add Approach 2

**Milestone 2: Selective Expansion** (Weeks 3-4)
- For books with <85% accuracy → Implement Approach 2 (chapter context)
- Likely candidates: Minor prophets, Numbers, Chronicles
- Build hybrid system: LLM Memory for most books, Explicit Context for difficult ones

**Milestone 3: Feature Rollout** (Weeks 5-8)
- Apply to NounListIndex (second priority)
- Apply to Surface Realization
- Apply to Topic/Focus Tracking

**Milestone 4: Optimization** (Weeks 9-12)
- Refine prompts based on error analysis
- Add Approach 2 where needed
- Build confidence calibration (by book/genre)
- Consider Approach 3 for future enhancement

---

## Decision Criteria

**When to use Approach 1 (LLM Memory)**:
- ✓ Well-known books (Gospels, Genesis, Psalms, Romans)
- ✓ Features with clear discourse patterns (Participant Tracking)
- ✓ Development speed is priority
- ✓ Acceptable accuracy: 80-90%

**When to use Approach 2 (Expanded Context)**:
- ✓ Accuracy-critical features (NounListIndex consistency)
- ✓ Features with complex state (coreference chains)
- ✓ Obscure books where LLM memory uncertain
- ✓ Required accuracy: 95-100%

**When to use Approach 3 (Two-Pass)**:
- ✓ Long-term comprehensive solution
- ✓ Multiple features benefit from same discourse analysis
- ✓ Human review of discourse structure desired
- ✓ Computational cost acceptable

---

## Success Metrics

### Phase 1 Success (Approach 1 validation)
- ✓ 50 test cases evaluated
- ✓ Participant Tracking accuracy ≥85%
- ✓ Clear understanding of where LLM memory succeeds/fails
- ✓ Decision made: Deploy broadly OR add Approach 2

### Phase 2 Success (Production deployment)
- ✓ Participant Tracking deployed for all books
- ✓ NounListIndex implemented with consistent indices
- ✓ Surface Realization updated with discourse context
- ✓ Overall feature accuracy ≥90%

### Phase 3 Success (Comprehensive)
- ✓ All discourse-dependent features implemented
- ✓ Hybrid system optimized (Approach 1 + selective Approach 2)
- ✓ Documentation updated
- ✓ Ready for Approach 3 evaluation

---

## Next Steps

**Week 1: Validation**
1. Design test corpus (50 verses across 3 dimensions)
2. Manually annotate ground truth for Participant Tracking
3. Implement Approach 1 prototype for Participant Tracking
4. Run validation tests

**Week 2: Analysis**
1. Analyze results by book/genre/feature
2. Categorize errors (4 types)
3. Calculate accuracy metrics
4. Make go/no-go decision

**Week 3-4: Implementation** (if validation succeeds)
1. Refine prompts based on error analysis
2. Implement for NounListIndex (Approach 2 required)
3. Build hybrid system
4. Deploy to production

---

## Conclusion

### Key Insights

1. **Discourse context is essential** for 7+ TBTA features (high priority)
2. **Verse-level processing is fundamentally insufficient** for Participant Tracking, NounListIndex, Surface Realization
3. **Three viable approaches** exist with different trade-offs
4. **Hybrid strategy recommended**: Start with LLM Memory (fast), add Explicit Context (accurate) where needed

### Strategic Recommendation

**Implement Approach 1 (LLM Memory) immediately** to:
- Prove discourse context value in 2 weeks
- Deploy Participant Tracking improvements quickly
- Identify books/features needing Approach 2

**Reserve Approach 2 (Expanded Context)** for:
- NounListIndex (consistency requirement)
- Books where LLM memory insufficient
- Features requiring 95%+ accuracy

**Consider Approach 3 (Two-Pass)** for:
- Long-term comprehensive solution
- After Approach 1+2 hybrid proves value
- When multiple features benefit from shared discourse analysis

---

**Document Status**: READY FOR REVIEW
**Next Action**: Validate Approach 1 with 50-verse test corpus
**Timeline**: Start validation in Week 1

---

For detailed implementation of each approach, see the individual approach documents.
