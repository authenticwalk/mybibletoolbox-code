# High-Level Baseline Review: Mood Feature

## Executive Summary

**Feature**: Mood (Grammatical Modality)
**Total TBTA annotations**: 72,089
**Test set size**: 100 entries (balanced sample)

### Baseline Performance

| Test | Accuracy | Notes |
|------|----------|-------|
| Zero-shot | 55% | Using LLM's baseline knowledge |
| Guided | 51% | With definitions provided |

**Verdict**: Poor baseline performance indicates TBTA uses idiosyncratic labeling system that differs from standard linguistic definitions.

## Distribution Analysis

### TBTA Label Distribution (Full Dataset)

| Label | Count | Percentage |
|-------|-------|------------|
| Indicative | 70,079 | 97.21% |
| 'must' Obligation | 633 | 0.88% |
| 'should' Obligation | 567 | 0.79% |
| 'might' Potential | 367 | 0.51% |
| 'should not' Obligation | 158 | 0.22% |
| 'may' (permissive) | 150 | 0.21% |
| Forbidden Obligation | 121 | 0.17% |
| Definite/Probable/Unlikely Potential | 14 | 0.02% |

**Key Insight**: Indicative dominates (97%+). The challenging cases are all non-indicative moods.

## Error Pattern Analysis

### Most Common Errors (Zero-shot)

| Actual → Predicted | Count | Analysis |
|--------------------|-------|----------|
| 'must' Obligation → 'should' Obligation | 5 | Difficulty distinguishing obligation strength |
| 'should not' → 'should' | 4 | Negative form misclassified |
| Indicative → 'might' Potential | 4 | Factual misread as potential |
| 'might' Potential → Indicative | 3 | Reverse confusion |

### Most Common Errors (Guided)

| Actual → Predicted | Count | Analysis |
|--------------------|-------|----------|
| 'should not' Obligation → Indicative | 6 | **CRITICAL**: Definitions don't help |
| 'should' Obligation → Indicative | 6 | Obligations confused with facts |
| 'may' (permissive) → Indicative | 4 | Permission confused with facts |
| 'might' Potential → Indicative | 4 | Speculation confused with facts |

## Key Findings

### 1. Definitions Made Things Worse

The guided baseline (51%) performed *worse* than zero-shot (55%). This suggests:
- Standard linguistic definitions don't match TBTA's internal logic
- TBTA may use context or clause-structure cues not captured in definitions
- Need to learn TBTA's specific patterns empirically

### 2. TBTA Labels Are Semantic, Not Morphological

Unlike source language mood (indicative, subjunctive, imperative forms), TBTA labels represent:
- **Speaker intent** (what should happen)
- **Epistemic status** (certainty vs possibility)
- **Deontic force** (obligation strength)

### 3. High Indicative Bias

With 97%+ of labels being Indicative, a naive "always predict Indicative" model would achieve 97% accuracy. This suggests:
- Accuracy alone is misleading
- Need F1-score by label or weighted metrics
- Focus analysis on non-indicative cases

### 4. Obligation Gradations Are Subtle

The 'must'/'should'/'should not'/Forbidden spectrum is difficult:
- 5 confusions between 'must' and 'should'
- 4 confusions between 'should not' and 'should'
- Context or verb-specific patterns likely determine these

## Recommendations for Stage 3

1. **Focus on non-indicative cases** - Build classifier for the 2,010 non-indicative entries
2. **Learn TBTA patterns empirically** - Don't rely on linguistic definitions
3. **Use translation patterns** - Mood-marking languages (Spanish subjunctive, German modal verbs) may help
4. **Analyze verb-specific patterns** - Some verbs may strongly predict certain moods
5. **Consider two-stage approach**:
   - Stage 1: Indicative vs Non-Indicative
   - Stage 2: Classify non-indicative into subtypes

## Questions for TBTA Team

1. What criteria determine 'must' vs 'should' obligation?
2. Why is "Forbidden Obligation" separate from "'should not' Obligation"?
3. Are moods assigned based on source language morphology or semantic intent?
4. Why are Definite/Probable/Unlikely Potential so rare (14 total)?
