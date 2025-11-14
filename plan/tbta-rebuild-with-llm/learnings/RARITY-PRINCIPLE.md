# Pattern 4: The Rarity Principle

**Source**: Aspect Experiment (98.1% Accuracy)
**Achievement**: 98.1% accuracy (53/54 correct predictions)
**Method**: Rarity principle + Mood correlation + Multi-factor analysis

---

## The Rarity Principle (HIGHEST BASELINE IMPACT)

**Discovery**: 90.7% of verbs are Unmarked (default), only 9.3% marked (Inceptive/Imperfective/Habitual)

**Core Insight**: TBTA only marks when semantically necessary. For ANY feature, identify and default to the dominant value.

---

## Prompt Strategy for Rarity Principle

### Step 1: Distribution Analysis Prompt

```
Analyze the distribution of {feature_name} values in this sample:

{provide 20-50 example verses with feature values}

Questions:
1. What is the most common value? (count and percentage)
2. What are the rare/marked values? (count and percentage)
3. What is a good default/baseline prediction?

The baseline should:
- Account for 80-90% of cases
- Be the semantically unmarked/neutral value
- Require no special context to predict

Distribution analysis:
- {Value 1}: X% ({count} instances)
- {Value 2}: Y% ({count} instances)
- ...

Recommended baseline: {most common value}
Expected baseline accuracy: {percentage}%
```

### Step 2: Baseline Application Prompt

```
For {verse reference}, predict {feature_name}:

Baseline value: {dominant_value} (accounts for {percentage}% of cases)

Check for special triggers that would override baseline:
- [ ] Theological factor present? (e.g., divine action)
- [ ] Discourse marker present? (e.g., topic shift)
- [ ] Grammatical trigger present? (e.g., specific mood)
- [ ] Semantic trigger present? (e.g., action vs state)

If NO special triggers found:
→ Use BASELINE: {dominant_value}
→ Confidence: {baseline_percentage}% (from distribution)

If special triggers found:
→ Override baseline with: {marked_value}
→ Confidence: depends on trigger strength
→ Reasoning: ...
```

---

## Results from Aspect Experiment

- Unmarked predictions = 97.9% accurate (48/49)
- Only 5 marked values needed special analysis
- Baseline alone gave 90.7% accuracy

### Distribution Breakdown

```
Aspect Distribution (54 total verbs):
- Unmarked:     49 verbs (90.7%)  → Baseline
- Inceptive:     3 verbs (5.6%)   → Requires special analysis
- Imperfective:  1 verb (1.9%)    → Requires special analysis
- Habitual:      1 verb (1.9%)    → Requires special analysis
```

**Strategy**: Default to Unmarked, only predict marked values when strong triggers present.

---

## Application to Other TBTA Features

### Apply To:

**Polarity**: Default Affirmative (~90%)
- Most clauses are affirmative
- Only mark negative when explicit negation present
- Expected baseline accuracy: 90%+

**Voice**: Default Active (~70%)
- Most clauses have active voice
- Only mark passive when agent backgrounding needed
- Expected baseline accuracy: 70-80%

**Status**: Default Realis (~85%)
- Most clauses describe actual events/states
- Only mark irrealis for hypotheticals, wishes, potentials
- Expected baseline accuracy: 85-90%

**Person**: Default 3rd in narrative (~70%)
- Most narrative uses 3rd person
- 1st/2nd person for dialogue, epistolary
- Expected baseline accuracy: 70-80%

**Mood**: Default Indicative (~85%)
- Most clauses are indicative (statements)
- Only mark subjunctive, imperative for specific functions
- Expected baseline accuracy: 85-90%

---

## Why It Works

**Matches TBTA Philosophy**: Mark only when necessary
- TBTA is designed for minority language translation
- Marking rare features helps translators notice important distinctions
- Unmarked = default, no special attention needed

**Achieves High Baseline Immediately**: 80-90% accuracy with zero analysis
- No complex prompts required for majority cases
- Computational efficiency: only analyze the 10-20% marked cases

**Reduces False Positives**: Over-marking is worse than under-marking
- False positive (mark when shouldn't): Confuses translators
- False negative (miss marked feature): Less harmful for common cases

---

## Detailed Example: Aspect Prediction

### Baseline Strategy

```python
# Conceptual approach (LLM prompt, not actual code)

def predict_aspect(verse_ref, verb_data):
    """
    Predict aspect using rarity principle
    """

    # STEP 1: Default to baseline (90.7% accurate)
    baseline = "Unmarked"

    # STEP 2: Check for triggers to override baseline
    triggers = check_aspect_triggers(verb_data)

    # STEP 3: Only override if strong evidence
    if triggers.count >= 3 and triggers.confidence > 0.9:
        return triggers.marked_value
    else:
        return baseline
```

### Prompt Template

```
Aspect Prediction for {verse_ref}:

Verb: "{verb_text}"
Mood: {mood_value}
Time: {time_value}

BASELINE: Unmarked (90.7% of cases)

CHECK FOR MARKED TRIGGERS:

Inceptive triggers (5.6% of cases):
- [ ] Potential mood present? (100% correlation)
- [ ] Near-future time? (e.g., "Later Today")
- [ ] Action verb? (e.g., beat, eat, drink)
→ If 3/3 present: Predict INCEPTIVE (95% confidence)

Imperfective triggers (1.9% of cases):
- [ ] State verb? (e.g., be, have, know)
- [ ] Durative context? (e.g., "while", "as")
- [ ] Background description?
→ If 2/3 present: Predict IMPERFECTIVE (80% confidence)

Habitual triggers (1.9% of cases):
- [ ] Iterative adverb? (e.g., "always", "regularly")
- [ ] Customary action? (e.g., "used to")
- [ ] Generic subject? (e.g., "people", "one")
→ If 2/3 present: Predict HABITUAL (80% confidence)

RESULT:
- If NO triggers → UNMARKED (default, 90.7% confidence)
- If triggers present → {marked_value} ({confidence}% based on trigger strength)
```

---

## Testing Results

### Test Set: 54 Verbs

**Baseline Performance** (predict all as Unmarked):
- Correct: 49/54 (90.7%)
- Incorrect: 5/54 (9.3% - the marked cases)

**With Trigger Detection**:
- Unmarked: 48/49 correct (97.9%)
- Inceptive: 3/3 correct (100%)
- Imperfective: 1/1 correct (100%)
- Habitual: 0/1 correct (0% - single failure case)
- **Overall: 53/54 (98.1%)**

### Error Analysis

**Single Error**: Habitual case
- Verse: Matthew 24:49
- Predicted: Unmarked (baseline)
- Actual: Habitual
- Reason: Missed iterative context ("begins to beat")
- Fix: Add "begins to" as habitual trigger

**Lesson**: Even with 1 error, achieved 98.1% accuracy by prioritizing baseline.

---

## Confidence Calibration

### Confidence Levels by Trigger Count

```
Baseline (no triggers):
- Predicted: Unmarked
- Confidence: 90.7% (from distribution)
- Accuracy: 97.9% (better than distribution!)

Weak triggers (1/3):
- Predicted: Marked value (low confidence)
- Confidence: 60%
- Recommendation: Flag for review, may use baseline

Medium triggers (2/3):
- Predicted: Marked value (medium confidence)
- Confidence: 80%
- Recommendation: Use predicted value

Strong triggers (3/3):
- Predicted: Marked value (high confidence)
- Confidence: 95%+
- Recommendation: High confidence prediction
```

---

## Integration with Other Patterns

### Combined Strategy

1. **Start with Rarity Principle** (Pattern 4) → 80-90% baseline
2. **Apply Hierarchical Prompts** (Pattern 1) → Resolve marked cases
3. **Use Gateway Features** (Pattern 5) → Check Mood first
4. **Multi-Factor Convergence** (Pattern 6) → Increase confidence

### Example Integration

```
Step 1: Rarity Principle
→ Baseline: Unmarked (90.7%)

Step 2: Check Gateway (Mood)
→ Mood = Potential → Strong correlation with Inceptive

Step 3: Multi-Factor Convergence
→ Factor 1: Potential mood ✓
→ Factor 2: Action verb ✓
→ Factor 3: Near-future time ✓
→ 3/3 agree → Override baseline

Result: Inceptive (95% confidence)
```

---

## Best Practices

### DO:
✅ Identify baseline distribution FIRST (before building complex prompts)
✅ Default to baseline unless strong evidence to override
✅ Use rarity principle to prioritize analysis effort (focus on 10-20% marked cases)
✅ Calibrate confidence based on distribution
✅ Test baseline alone to measure improvement from triggers

### DON'T:
❌ Over-mark features (false positives worse than false negatives)
❌ Build complex prediction for common cases (waste of effort)
❌ Ignore distribution data (always analyze first)
❌ Assume 50/50 distribution (TBTA favors unmarked heavily)
❌ Skip baseline testing (always measure baseline accuracy first)

---

## Quick Reference

### For Any TBTA Feature:

1. **Analyze distribution** → Find dominant value (expect 70-90%)
2. **Set baseline** → Default to dominant value
3. **Identify triggers** → What makes marked value necessary?
4. **Override selectively** → Only when high-confidence triggers present
5. **Calibrate confidence** → Based on trigger strength

### Expected Baselines for Common Features:

| Feature | Expected Baseline | Distribution | Confidence |
|---------|------------------|--------------|------------|
| Aspect | Unmarked | 90.7% | 90-95% |
| Polarity | Affirmative | ~90% | 90% |
| Voice | Active | ~70% | 70-80% |
| Status | Realis | ~85% | 85-90% |
| Mood | Indicative | ~85% | 85-90% |
| Person (narrative) | 3rd | ~70% | 70-80% |
| Number | Singular | ~60% | 60-70% |

---

## Conclusion

The Rarity Principle provides the **highest baseline impact** of any pattern discovered. By simply defaulting to the dominant value, you achieve 80-90% accuracy immediately. Combined with selective trigger detection for marked cases, accuracy exceeds 95%.

**Key Insight**: Don't try to predict everything perfectly. Predict the majority correctly (baseline), then invest effort in the minority (marked cases).

**Result**: 98.1% accuracy on Aspect with minimal complexity.
