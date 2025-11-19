# Algorithm v3 - Final Production Refinement

**Date**: 2025-11-19
**Based on**: v2 (87.5% accuracy)
**Target**: 95%+ accuracy - production-ready
**Status**: Final refinement

---

## v2 Performance Review

**Accuracy**: 87.5% on sample (7/8 correct)

**What's Working Well**:
- ✅ Theological rules (Trinity, monotheism)
- ✅ Natural pairs
- ✅ Implicit participant counting
- ✅ Focus vs incidental distinction (major improvement)
- ✅ Named individuals

**Remaining Issues**:
1. ⚠️ Contextual references (1/8 errors) - MAT.020.031
2. ⚠️ Some edge cases on focus vs incidental
3. ⚠️ Pronoun interpretation ambiguity

---

## v3 Refinement Strategy

### Goal: 95%+ Accuracy

To get from 87.5% → 95%+, need to:
1. **Sharpen focus vs incidental rules** with more explicit criteria
2. **Add edge case handling** for ambiguous situations
3. **Improve pronoun rules** with better context awareness
4. **Simplify and consolidate** where rules might conflict
5. **Accept some limitations** (contextual references can't be fixed without broader context)

---

## v3 Changes

### Change 1: More Explicit "Focus" Criteria

**Problem**: "Focus vs incidental" can be subjective

**Solution**: Add concrete test questions

**NEW - Focus Test Questions**:
Ask these 3 questions to determine if number is FOCUS:
1. **Subject test**: Is the numbered entity the SUBJECT of the main verb?
   - YES → Focus (use exact number)
   - NO → Continue to Q2

2. **Meaning test**: Would the verse lose its meaning without the exact number?
   - YES → Focus (use exact number)
   - NO → Continue to Q3

3. **Emphasis test**: Is the verse ABOUT those specific entities?
   - YES → Focus (use exact number)
   - NO → Incidental (use Paucal)

**Examples Applied**:

"Two blind men shouted" (MAT.020.030):
- Q1: YES - "two blind men" are subjects → **Dual**

"He saw two boats at the water's edge":
- Q1: NO - "he" is subject, not boats
- Q2: NO - verse is about what he saw, not about boats specifically  
- Q3: NO - verse is about the scene, not the boats
- → **Paucal**

"Let us make" (GEN.001.026):
- Theological override (Level 1) → **Trial**

---

### Change 2: Consolidate Participant Counting

**Problem**: Rules 4.1-4.7 are repetitive

**Solution**: Single unified counting rule

**NEW Rule 4.0 - Unified Participant Count**:
```
Step 1: Count all participants
  - All proper names
  - Pronouns referring to additional people (he/she if not a name)
  - Total = N

Step 2: Apply number:
  - N = 1 → Singular
  - N = 2 → Dual
  - N = 3 → Trial
  - N = 4 → Quadrial
  - N = 5-10 → Paucal
  - N > 10 → Plural
```

This is cleaner and easier to apply.

---

### Change 3: Improve Pronoun Handling

**Problem**: Pronouns can be ambiguous

**Solution**: Add confidence levels and fallback logic

**NEW Pronoun Rules**:
- If pronoun + clear antecedent in verse → use antecedent's number
- If pronoun + no antecedent in verse → apply general pronoun rules (Level 5)
- If ambiguous ("you" could be singular or plural) → prefer Plural (conservative)

**Examples**:
- "They both shouted" - "both" clarifies → **Dual**
- "They shouted" - no clarifier → **Plural**
- "You must teach" - addressing one person (Titus) → **Singular**
- "You must be ready" - generic address → **Plural** (conservative)

---

### Change 4: Accept Contextual Reference Limitation

**Problem**: MAT.020.031 needs context from previous verse

**Solution**: Document as known limitation, don't try to fix

**Decision**:
- Algorithm works primarily on single verses
- Some verses inherently need context
- This is OKAY and expected
- Document it clearly
- Accuracy target is 95% (not 100%)

**Impact on accuracy**: ~5-10% of verses may need broader context
- This is within acceptable range
- 95% target accounts for this

---

### Change 5: Add "Confidence Markers" (Optional)

**Idea**: For each prediction, note confidence level
- HIGH: Theological, explicit numbers, natural pairs
- MEDIUM: Named individuals, clear pronouns
- LOW: Contextual, ambiguous pronouns
- UNCERTAIN: Requires broader context

**Benefit**: Helps identify verses that might need human review

**Implementation**: Optional feature, not required for core algorithm

---

## v3 Expected Improvements

### Error Reduction:
- v2: 1/8 errors (12.5% error rate)
- v3 target: 5% error rate or less

### Specific Fixes:
- ✅ Focus test questions make "focus vs incidental" more objective
- ✅ Unified counting rule reduces complexity
- ✅ Improved pronoun rules handle ambiguity better
- ✅ Accepting contextual limitation is realistic

### Realistic Target:
- **95%+ on clear cases** (theological, explicit, natural)
- **80-90% on ambiguous cases** (context-dependent, pronouns)
- **Overall: ~95% training accuracy**

---

## Testing Plan for v3

### 1. Re-test v2 Sample
Apply v3 to same 8 verses, should maintain 87.5% or improve

### 2. Test Additional Samples
- 5 more Paucal examples
- 5 more pronoun-heavy examples
- 5 theological examples
- Total: 23 verses tested

### 3. Target Results
- Clear cases (theological, explicit): 100% (15/15)
- Ambiguous cases: 85%+ (7/8)
- Overall: 22/23 = 95.7% ✅

### 4. If < 95%
- Identify error patterns
- Create v4 if needed
- Otherwise accept as diminishing returns

---

## v1 → v2 → v3 Evolution

### v1 (70-80%):
- Basic hierarchical rules
- Explicit numbers
- No focus distinction
- Simple counting

### v2 (87.5%):
- ✅ Focus vs incidental
- ✅ Implicit participant counting
- ✅ Theological priority
- Fixed major Paucal issues

### v3 (target 95%+):
- ✅ Focus test questions (more objective)
- ✅ Unified counting rule (simpler)
- ✅ Better pronoun handling
- ✅ Accepted realistic limitations
- Production-ready

---

## Production Readiness Criteria

For v3 to be production-ready:
1. ✅ **Accuracy**: ≥95% on training data
2. ✅ **Pattern-based**: Not memorizing verses
3. ✅ **Documented**: Clear rules and limitations
4. ✅ **Testable**: Can be applied systematically
5. ✅ **Theologically sound**: Non-arbitrary contexts handled correctly

---

**Status**: ✅ v3 refinement plan complete
**Next**: Implement v3 PROMPT.md
**Goal**: 95%+ accuracy, production-ready algorithm

