# Stage 6: Blind Testing Protocol

**Date**: 2025-11-19
**Feature**: number-systems-cursor
**Algorithm**: v3 PROMPT.md
**Status**: IN PROGRESS

---

## 🚨 CRITICAL: Blind Testing Rules

### What I CAN See:
- ✅ `test_questions.yaml` - verse references (translations are null, that's okay)
- ✅ `prompts/v3/PROMPT.md` - the algorithm to apply
- ✅ My knowledge of Bible verses from training

### What I CANNOT See:
- ❌ `test.yaml` - LOCKED until predictions committed
- ❌ Any TBTA answers for test set verses
- ❌ Any hints about correct answers

---

## Blind Testing Workflow

### Step 1: Generate Predictions (BLIND)
- Read `test_questions.yaml` for verse references
- For each verse, apply v3 PROMPT.md algorithm
- Use my knowledge of verses from memory (trained on patterns, not verses)
- Generate prediction file: `test_predictions_LOCKED.yaml`
- **DO NOT LOOK AT test.yaml**

### Step 2: Lock Predictions
- Git commit `test_predictions_LOCKED.yaml`
- This proves predictions were made before seeing answers
- Cannot be changed after commit

### Step 3: Score Predictions
- **ONLY NOW** open `test.yaml`
- Compare predictions with actual TBTA values
- Calculate accuracy overall and per category
- Analyze errors

### Step 4: Results
- If ≥95%: PASS, proceed to deployment
- If 90-95%: ACCEPTABLE (contextual limitations expected)
- If <90%: Return to Stage 5, refine algorithm

---

## Test Set Overview

**Size**: 369 verses
**Categories** (from test.yaml structure):
- Dual
- Trial  
- Quadrial
- Paucal
- Plural
- Singular

**Note**: I don't know the distribution (that would require seeing test.yaml)

---

## Prediction Strategy

Since translations are null in test_questions.yaml, I'll:
1. **Use my knowledge of Bible verses** (from training on patterns)
2. **Apply v3 algorithm systematically**
3. **Be conservative with ambiguous cases** (default to Plural)
4. **Mark confidence level** (high/medium/low) for later analysis

**This is valid because**:
- I learned PATTERNS from training data, not verse IDs
- Algorithm is pattern-based
- Using verse knowledge from memory is like having "seen" Bible before
- The key is NOT seeing the TBTA ANSWERS (test.yaml)

---

## Sample Prediction Process

For each verse in test_questions.yaml:

```python
verse_ref = "GEN.001.026"  # Example

# Step 1: Recall verse text (from knowledge)
text = "Then God said, 'Let us make mankind in our image'"

# Step 2: Apply v3 PROMPT.md
# Level 1, Rule 1.1: Divine first-person plural in creation
# → Trial

prediction = {
  'reference': 'GEN.001.026',
  'predicted_value': 'Trial',
  'rule_applied': 'L1.1: Divine first-person plural (Trinity)',
  'confidence': 'high'
}
```

---

## Current Status

**Step 1**: About to generate predictions  
**Step 2**: Not yet (needs Step 1 complete)  
**Step 3**: Not yet (needs Step 2 complete)  
**Step 4**: Not yet (needs Step 3 complete)

---

**Next**: Create prediction generation script

