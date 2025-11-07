# Phrasal Elements: Validation Approach

> **Parent Context:** Three-level validation system for phrasal element predictions.

## Validation Approach

### Three-Level Validation System

**Level 1: Automated Checks (100% coverage)**
1. Schema validation: All required fields present
2. Value validation: Type/function/compositionality values from enumeration
3. Citation validation: Source must be {llm-cs45} or approved resource
4. Cross-reference: Check against TBTA Part="p-..." encoding
5. Duplicate detection: Same phrase marked multiple times in verse

**Metrics**:
- Pass: All checks pass
- Fail: Any required field missing or invalid value
- **Target**: 100% pass rate before human review

---

**Level 2: Pattern-Based Validation (statistical checks)**
1. **Genre distribution check**: Prophetic/poetic should have 2-3x more phrasal elements than narrative
2. **Type distribution check**: Cultural idiom ~35%, Theological ~25% (variance ±10% acceptable)
3. **Confidence calibration**: High-confidence predictions should correlate with divine names/well-known titles
4. **Translation pattern consistency**: If prediction=YES but all translations are word-by-word → Flag
5. **Context sensitivity**: Same phrase in different contexts should have context-dependent marking

**Metrics**:
- Pass: Within expected distribution ranges
- Warning: Outside ranges but explicable (e.g., Job has more metaphors)
- Fail: Major deviation without explanation
- **Target**: 90%+ pass rate

---

**Level 3: Human Expert Review (sample-based)**
1. **Non-compositionality test**: Do reviewers agree phrase meaning ≠ sum of parts?
2. **Translation challenge validation**: Does literal translation really cause problems?
3. **Type classification accuracy**: Is divine_name vs messianic_title vs cultural_idiom correct?
4. **Edge case adjudication**: For UNCERTAIN predictions, expert decides YES/NO

**Sample size**:
- 100% of divine names (high stakes)
- 50% of cultural idioms (high error rate)
- 20% of other types (spot check)

**Metrics**:
- Agreement rate: Expert agrees with prediction
- Precision: Of predicted phrasal, % actually non-compositional
- Recall: Of actual phrasal (per expert), % detected
- **Target**: 85%+ precision, 80%+ recall, 90%+ agreement

---

### Validation Against TBTA Encoding

TBTA marks phrasal elements with `Part="p-..."` codes. Use this for ground truth validation:

1. **True Positive**: Predicted phrasal, TBTA has p-code ✅
2. **False Positive**: Predicted phrasal, TBTA does NOT have p-code ⚠️
   - May be unmarked idiom in TBTA (acceptable)
   - May be over-prediction (error)
3. **False Negative**: Not predicted, TBTA has p-code ❌
   - Missed idiom (error)
4. **True Negative**: Not predicted, TBTA does NOT have p-code ✅

**F1 Score Targets**:
- Initial predictions: 85%+ F1
- After iterative refinement: 90%+ F1
- Production quality: 92%+ F1

**Iteration process**:
1. Analyze False Positives → Tighten prediction criteria
2. Analyze False Negatives → Add overlooked indicators
3. Re-run on sample → Measure improvement
4. Deploy updated model

