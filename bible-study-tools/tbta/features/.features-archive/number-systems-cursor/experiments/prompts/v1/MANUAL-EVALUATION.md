# Manual Evaluation of Algorithm v1

**Date**: 2025-11-19
**Method**: Manual application of PROMPT.md v1 to sample verses
**Reason**: Automated fetching not available, using AI knowledge of verses

---

## Sample Verses from Training Set

### DUAL Category (Sample from train.yaml)

#### GEN.013.008 - "between you and me"
**Verse Text** (from memory): "So Abram said to Lot, 'Let's not have any quarreling between you and me, or between your herders and mine, for we are close relatives.'"

**Algorithm Application**:
- Level 1: No explicit "two"
- Level 2: No body parts
- Level 3: Not theological
- Level 4: Two names (Abram, Lot) → **Predicted: Dual**
- Also Rule 5.2: "between you and me" → **Predicted: Dual**

**Result**: ✅ **CORRECT** - True: Dual, Predicted: Dual

---

#### MAT.020.031 - "two blind men"
**Verse Text** (from memory): "The crowd rebuked them and told them to be quiet, but they shouted all the louder, 'Lord, Son of David, have mercy on us!'"

**Algorithm Application**:
- Level 1: Not explicitly in this verse (but context has "two")
- Level 5: "them" plural
- Would predict Plural without context

**Issue**: ❌ **INCORRECT** - True: Dual, Predicted: Plural
**Problem**: Need context from previous verses

---

#### JDG.014.006 - "bare hands"  
**Verse Text** (from memory): "The Spirit of the LORD came powerfully upon him so that he tore the lion apart with his bare hands"

**Algorithm Application**:
- Level 1: No explicit "two"
- Level 2: "hands" → **Predicted: Dual** (Rule 2.1)

**Result**: ✅ **CORRECT** - True: Dual, Predicted: Dual

---

### TRIAL Category

#### GEN.001.026 - Divine Plural (Trinity)
**Verse Text** (from memory): "Then God said, 'Let us make mankind in our image, in our likeness'"

**Algorithm Application**:
- Level 3: "Let us make" in creation context → **Predicted: Trial** (Rule 3.1 - Trinity)

**Result**: ✅ **CORRECT** - True: Trial, Predicted: Trial

---

#### GEN.036.021 - Three Named Individuals
**Verse Text** (from memory): "Dishon, Ezer and Dishan. These sons of Seir in Edom were Horite chiefs."

**Algorithm Application**:
- Level 1: No explicit "three"
- Level 4: Three names (Dishon, Ezer, Dishan) → **Predicted: Trial** (Rule 4.3)

**Result**: ✅ **CORRECT** - True: Trial, Predicted: Trial

---

#### 1SA.010.003 - Explicit "three men"
**Verse Text** (from memory): "...Three men going up to worship God at Bethel will meet you there..."

**Algorithm Application**:
- Level 1: "Three men" → **Predicted: Trial** (Rule 1.3)

**Result**: ✅ **CORRECT** - True: Trial, Predicted: Trial

---

### QUADRIAL Category

#### EXO.025.026 - "four gold rings"
**Verse Text** (from memory): "Make four gold rings for the table and fasten them to the four corners, where the four legs are."

**Algorithm Application**:
- Level 1: "four" mentioned multiple times → **Predicted: Quadrial** (Rule 1.4)

**Result**: ✅ **CORRECT** - True: Quadrial, Predicted: Quadrial

---

#### LUK.009.028 - Three names but marked Quadrial?
**Verse Text** (from memory): "About eight days after Jesus said this, he took Peter, John and James with him and went up onto a mountain to pray."

**Algorithm Application**:
- Level 1: "eight days" → Would predict **Paucal** (Rule 1.5)
- Level 4: Three names (Peter, John, James) → Would predict **Trial** (Rule 4.3)

**Issue**: ❌ **INCORRECT** - True: Quadrial, Predicted: Paucal or Trial
**Problem**: Why is this marked Quadrial? Possibly counting Jesus + 3 disciples = 4 total?

---

### PAUCAL Category

#### LUK.005.002 - "two boats"
**Verse Text** (from memory): "He saw at the water's edge two boats, left there by the fishermen"

**Algorithm Application**:
- Level 1: "two boats" → **Predicted: Dual** (Rule 1.2)

**Issue**: ❌ **INCORRECT** - True: Paucal, Predicted: Dual
**Problem**: Why is "two boats" Paucal not Dual?

---

#### MAT.015.034 - "seven loaves"
**Verse Text** (from memory): "'How many loaves do you have?' Jesus asked. 'Seven,' they replied, 'and a few small fish.'"

**Algorithm Application**:
- Level 1: "seven" → **Predicted: Paucal** (Rule 1.5)
- Also "a few" → **Predicted: Paucal** (Rule 1.6)

**Result**: ✅ **CORRECT** - True: Paucal, Predicted: Paucal

---

### PLURAL Category

#### 1TH.005.014 - "brothers and sisters"
**Verse Text** (from memory): "And we urge you, brothers and sisters, warn those who are idle and disruptive, encourage the disheartened, help the weak"

**Algorithm Application**:
- Level 6: "brothers and sisters" → large group → **Predicted: Plural** (Rule 6.2)

**Result**: ✅ **CORRECT** - True: Plural, Predicted: Plural

---

#### TIT.001.011 - "whole households"
**Verse Text** (from memory): "They must be silenced, because they are disrupting whole households by teaching things they ought not to teach"

**Algorithm Application**:
- Level 6: "households" → **Predicted: Plural** (Rule 6.2)

**Result**: ✅ **CORRECT** - True: Plural, Predicted: Plural

---

### SINGULAR Category

#### TIT.002.001 - "You"
**Verse Text** (from memory): "You, however, must teach what is appropriate to sound doctrine."

**Algorithm Application**:
- Level 4: One person (Titus addressed) → **Predicted: Singular** (Rule 4.1)
- Level 5: Singular "you" → **Predicted: Singular** (Rule 5.1)

**Result**: ✅ **CORRECT** - True: Singular, Predicted: Singular

---

## Pattern Analysis

### High Confidence Rules (Working Well) ✅

1. **Explicit cardinal numbers** (Level 1)
   - "three men" → Trial ✅
   - "four gold rings" → Quadrial ✅
   - "seven loaves" → Paucal ✅

2. **Natural pairs** (Level 2)
   - "bare hands" → Dual ✅

3. **Divine plural** (Level 3)
   - "Let us make" → Trial (Trinity) ✅

4. **Named individuals** (Level 4)
   - Three names → Trial ✅
   - One name → Singular ✅

5. **Large groups** (Level 6)
   - "brothers and sisters" → Plural ✅
   - "households" → Plural ✅

---

### Problems Identified ❌

#### Problem 1: Contextual References
**Example**: MAT.020.031 - verse says "them" but context establishes "two blind men"
**Issue**: Algorithm working on verse in isolation misses context
**Solution Needed**: Either:
- Allow looking at surrounding verses
- Trust that TBTA data includes contextual understanding
- Document as known limitation

---

#### Problem 2: Paucal Boundary Unclear
**Example**: LUK.005.002 - "two boats" marked as Paucal not Dual
**Issue**: When does a specific small number become Paucal vs exact count?
**Hypothesis**: Maybe it's about the **focus** of the verse?
- If verse is ABOUT two specific things → Dual
- If verse mentions two things incidentally → Paucal?
**Solution Needed**: Understand the distinction better

---

#### Problem 3: Implicit Counting
**Example**: LUK.009.028 - Three names but marked Quadrial
**Issue**: Possibly counting Jesus + 3 disciples = 4 total (implicit)
**Solution Needed**: Count all people involved, not just named

---

## Initial Assessment

**Estimated Accuracy**: ~70-80% on high-confidence categories
- Strong on: Explicit numbers, natural pairs, divine plural, simple cases
- Weak on: Contextual references, Paucal boundary, implicit counting

---

## Refinement Priorities for v2

### Priority 1: Fix Paucal Boundary
Need to understand when "two boats" is Paucal vs Dual
- Research the linguistic definition more carefully
- Look at more Paucal examples from training data
- May need to consider semantic focus of the verse

### Priority 2: Handle Implicit Participants
Count ALL people involved, not just named
- Example: "Jesus took Peter, John and James" = 4 people total (Quadrial)
- Need rule: "if taking/bringing + N names → count speaker + names"

### Priority 3: Contextual References
Document that some verses require context
- May need to note this as a limitation
- Or add rule about looking back to previous verses

---

## Next Steps

1. Analyze MORE Paucal examples to understand boundary
2. Look at Quadrial examples to confirm implicit counting hypothesis
3. Create v2 with refined rules
4. Test v2 on same sample
5. Iterate until patterns clear

---

**Status**: ✅ v1 Manual evaluation complete
**Estimated Training Accuracy**: 70-80%
**Key Insight**: Paucal category needs clarification
**Next**: Analyze more training examples, create v2

