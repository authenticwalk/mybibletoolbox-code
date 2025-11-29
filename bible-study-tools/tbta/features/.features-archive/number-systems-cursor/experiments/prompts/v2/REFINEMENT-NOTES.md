# Algorithm v2 - Refinement Notes

**Date**: 2025-11-19
**Based on**: v1 manual evaluation results
**Key Changes**: Fix Paucal boundary, implicit counting, improve context awareness

---

## v1 Problems Summary

### Problem 1: Paucal vs Dual/Trial/Quadrial Boundary

**Observation from training data**:
- LUK.005.002 "two boats" → marked Paucal (appears 4x in training)
- MAT.015.034 "seven loaves" → marked Paucal
- But GEN.013.008 "you and me" → marked Dual

**Hypothesis**: The distinction is about **SEMANTIC FOCUS** vs **GRAMMATICAL NUMBER**

#### When to use EXACT numbers (Dual/Trial/Quadrial):
1. **Entities are the MAIN FOCUS** of the verse
   - "between you and me" - the two people ARE the point
   - "three men going up" - the three men ARE the actors
   - "four gold rings" - the four rings ARE what's being described

2. **Theologically significant** (non-arbitrary)
   - Trinity references → always Trial
   - Natural pairs (hands, eyes) → always Dual
   - Symbolic numbers → Quadrial (four corners, four creatures)

3. **Named individuals**
   - "Dishon, Ezer and Dishan" → Trial (specific people)
   - "Peter and John" → Dual (specific pair)

#### When to use Paucal:
1. **Small number mentioned but NOT the focus**
   - "two boats at the water's edge" - verse is about the scene, not the boats specifically
   - "a few small fish" - mentioned incidentally
   
2. **Small group as collective**
   - "I and all those with me" - small military band
   - Context suggests countable but emphasis on group, not exact count

3. **Numbers 5-10 range mentioned** (unless theologically significant)
   - "seven loaves" - incidental detail
   - "eight days later" - time reference, not main actors

**KEY INSIGHT**: Paucal is for "small numbers mentioned incidentally" vs "exact numbers that are the point"

---

### Problem 2: Implicit Participant Counting

**Example**: LUK.009.028 marked as Quadrial
- Verse: "he took Peter, John and James with him"
- Named: Peter, John, James (3 names)
- But "he" = Jesus
- Total: Jesus + 3 disciples = **4 people** = Quadrial ✅

**Rule Needed**: Count ALL participants, not just named individuals
- "he took X, Y, Z" = he + X + Y + Z = 4 total
- "we and them" = count both groups
- "sent them two by two" = focus is on the pairs (Dual), not total sent

---

### Problem 3: Contextual References

**Example**: MAT.020.031 
- Verse text: "they shouted"
- Context (v30): "two blind men"
- Should be Dual, but verse alone says "they" (would predict Plural)

**Solution Options**:
1. **Accept as limitation** - note that some verses need context
2. **Add contextual rules** - if pronouns without antecedent, mark as uncertain
3. **Trust TBTA workflow** - assume data includes contextual understanding

**Decision for v2**: Accept as known limitation, document it
- Algorithm works on verse in isolation
- Some verses require broader context
- This is expected and okay

---

## v2 Algorithm Changes

### Change 1: Refine Level 1 (Explicit Numbers)

**OLD v1 Rules**:
- "two" → Dual
- "three" → Trial  
- "four" → Quadrial
- "5-10" → Paucal

**NEW v2 Rules**:
- "two" → Check if FOCUS is on the two things
  - If main actors/focus → Dual
  - If incidental mention → Paucal
- "three" → Check if FOCUS or theological
  - If main actors/Trinity → Trial
  - If incidental → Paucal
- "four" → Check if symbolic/focus
  - If symbolic (corners, creatures) or main focus → Quadrial
  - If incidental → Paucal
- "5-10" → Paucal (unless extremely important to verse)

**How to determine FOCUS**:
- Are they the subject of the main verb?
- Are they being specifically described/acted upon?
- Does the verse lose meaning without the exact number?
- YES → Use exact number (D/T/Q)
- NO → Use Paucal

---

### Change 2: Add Implicit Participant Counting (Level 4)

**NEW Rule 4.6**: Count ALL participants mentioned
- "he took X, Y, Z" = Count "he" + 3 names = 4 total
- "we went with X and Y" = Count "we" (at least 1) + 2 names = 3+ total
- Look for subject + objects when counting

**Examples**:
- "Jesus took Peter, James, and John" = 1 + 3 = 4 → Quadrial
- "Moses, Aaron, and Hur" = 3 → Trial
- "Paul and Silas" = 2 → Dual

---

### Change 3: Refine Natural Pairs (Level 2)

**Keep existing** but clarify:
- Body parts that come in pairs → **ALWAYS Dual**
- This is universal and non-arbitrary
- Examples: hands, eyes, feet, ears, arms, legs

**Rationale**: Natural pairs are inherently dual across all languages

---

### Change 4: Keep Theological Rules Strong (Level 3)

**No changes needed** - these worked well in v1:
- Divine first-person plural in creation/judgment → Trial (Trinity)
- Explicit Trinity formula → Trial
- Monotheism emphasis → Singular

These are **non-arbitrary** and theologically grounded.

---

### Change 5: Refine Plural Default (Level 7)

**Clarify when to use Plural**:
- Large indefinite groups ("people", "nations", "crowds")
- Generic plurals ("those who believe", "everyone")
- Plural pronouns without specific count
- **Ambiguous small groups** (if can't determine if Paucal or specific number)

**Conservative approach**: When in doubt between Paucal and Plural → choose Plural

---

## Expected v2 Improvements

### Should Fix:
1. ✅ Paucal boundary clearer (focus vs incidental)
2. ✅ Implicit counting (count all participants)
3. ✅ Better distinction between exact numbers and small groups

### Still Limited:
1. ⚠️ Contextual references (need surrounding verses)
   - Accept as limitation
   - Document in algorithm notes
2. ⚠️ Ambiguous cases
   - Default to Plural (conservative)

### Target Accuracy:
- v1 estimated: 70-80%
- v2 target: 85-90%
- Still aiming for 95%+ (may need v3, v4...)

---

## Testing Strategy

1. **Manual test on same v1 sample**
   - Should fix LUK.005.002 (Paucal)
   - Should fix LUK.009.028 (Quadrial)
   - Should maintain good performance on others

2. **Test on additional Paucal examples**
   - Verify the "focus vs incidental" distinction works
   - Check boundary cases

3. **Test on Quadrial implicit counting**
   - Verify counting all participants works

4. **If accuracy ≥85%**: Continue to v3 refinement
5. **If accuracy <85%**: Debug and revise v2

---

**Status**: ✅ v2 refinement plan complete
**Next**: Implement PROMPT.md v2 with these changes
**Goal**: 85-90% manual accuracy on training samples

