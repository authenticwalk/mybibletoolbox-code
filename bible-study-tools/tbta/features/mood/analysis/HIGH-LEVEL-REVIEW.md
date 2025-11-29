# Mood Feature: Baseline Analysis

**Date**: 2025-11-29
**Sample Size**: 100 verses (stratified from train.jsonl)

## 1. Accuracy Comparison

| Test | Accuracy | Notes |
|------|----------|-------|
| Haiku (no metadata) | 31.2% | Heavy Indicative bias (71/100 predicted) |
| Sonnet (no metadata) | 41.0% | Over-predicted Definite Potential (20!) |
| Sonnet (with metadata) | 45.0% | **Best overall** |
| Sonnet (guided) | 44.0% | Definitions didn't help (-1%) |
| **Improvement** | +13.8% | Haiku→Sonnet w/metadata |

**Key Finding**: Guidance HURT accuracy (-1%). The LLM's intuition with raw data is slightly better than explicit definitions.

## 2. Distribution Analysis

| Label | Ground Truth | Haiku | Sonnet | w/Metadata | Guided |
|-------|-------------|-------|--------|------------|--------|
| Indicative | 44 | 71 (+27) | 51 (+7) | 82 (+38) | 80 (+36) |
| 'should' Obligation | 16 | 4 (-12) | 3 (-13) | 2 (-14) | 0 (-16) |
| 'must' Obligation | 13 | 9 (-4) | 5 (-8) | 0 (-13) | 4 (-9) |
| Forbidden Obligation | 9 | 0 (-9) | 4 (-5) | 4 (-5) | 7 (-2) |
| 'might' Potential | 8 | 0 (-8) | 1 (-7) | 6 (-2) | 7 (-1) |
| 'may' (permissive) | 5 | 0 (-5) | 2 (-3) | 6 (+1) | 2 (-3) |
| 'should not' Obligation | 5 | 6 (+1) | 12 (+7) | 0 (-5) | 0 (-5) |
| Definite Potential | 0 | 5 (+5) | 20 (+20) | 0 | 0 |
| Probable Potential | 0 | 1 (+1) | 2 (+2) | 0 | 0 |

**Critical Finding**:
- ALL models massively OVER-predict Indicative
- ALL models massively UNDER-predict 'should' Obligation (worst: 0/16 in guided)
- 'Definite Potential' hallucinated (20 predictions, 0 in ground truth)

## 3. Error Pattern Analysis

### Pattern 1: 'should' Obligation Never Recognized (100% miss rate)
The guided model predicted 0/16 'should' Obligation cases.

**Root Cause**: TBTA's 'should' Obligation appears to be semantic modality that differs from what the LLM expects. When TBTA labels something 'should', it's often:
- Wisdom literature advice
- Implicit moral guidance
- NOT explicit "you should" phrasing

**Example Errors**:
- Verses with implicit advice (proverbs) labeled 'should' but predicted Indicative

### Pattern 2: 'must' Obligation vs Forbidden Confusion
The LLM struggles to distinguish strong positive obligation from prohibition.

**Root Cause**: Both involve strong modality but differ in polarity. The LLM may be seeing "obligation" features without capturing positive/negative distinction.

### Pattern 3: 'Definite Potential' Hallucination
Sonnet (no metadata) predicted 20 'Definite Potential' - ground truth has 0.

**Root Cause**: The LLM is inferring future/prophetic statements as "definite potential" but TBTA doesn't use this category in these contexts.

## 4. Where Guidance Helped

Few cases. When the zero-shot was wrong and guided was right:
- Some 'might' Potential cases (conditional constructions)
- Some Forbidden Obligation cases

## 5. Where Guidance Hurt

Many cases. When the zero-shot was right and guided was wrong:
- Guidance caused over-prediction of Indicative
- Guidance eliminated 'should' Obligation predictions entirely
- Definitions may have been TOO precise, causing the LLM to reject ambiguous cases

## 6. Persistent Errors (All Tests Wrong)

**High-frequency miss categories**:
1. 'should' Obligation - ALL models miss these systematically
2. 'must' Obligation in wisdom literature contexts
3. 'may' (permissive) - subtle permission constructions

**Likely Cause**: TBTA labeling follows translation theory conventions that differ from linguistic intuition.

## 7. LLM Internal Biases

1. **Indicative Bias**: All models over-predict Indicative (default to "statement of fact")
2. **Potential Confusion**: Sonnet hallucinates "Definite Potential" category
3. **Obligation Spectrum Blindness**: Can't distinguish must/should/forbidden reliably

## 8. Recommendations

### Immediate
1. **Stratify by error type**: Focus prompt engineering on 'should' Obligation specifically
2. **Remove rare categories**: Definite/Probable/Unlikely Potential may be too rare to learn
3. **Binary first**: Try "Indicative vs Non-Indicative" as first pass

### Investigation Needed
1. **Audit 'should' Obligation**: Are TBTA labels consistent? What's the pattern?
2. **Check training data balance**: 56% non-Indicative in sample but 97% Indicative in full data

### Alternative Approach
Consider outputting: `{dominant: "Indicative", confidence: 0.7, alternates: [{label: "'should' Obligation", reason: "wisdom context"}]}`

## Prompts Used

### Test A (No Metadata)
```
Label the **bolded** word in this verse with one of these Mood values:
Indicative, 'must' Obligation, 'should' Obligation, 'might' Potential,
'should not' Obligation, 'may' (permissive), Forbidden Obligation,
Definite Potential, Probable Potential, Unlikely Potential

Verse: {text}

Return ONLY the label, nothing else.
```

### Test C (Guided)
```
Grammatical mood encodes speaker stance toward an action...
[Full definitions for each value]
...
Label the **bolded** word. Return ONLY the label.
```

## Conclusion

**31-45% baseline accuracy** is low but expected for a semantically complex feature. The key insight is that **definitions don't help** - the problem is TBTA's semantic labeling conventions, not LLM linguistic knowledge.

**Next Steps**: Deep-dive into 'should' Obligation patterns to understand TBTA's labeling criteria.
