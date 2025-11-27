# Mood Feature - Stage 2 Analysis

**Feature**: Mood (Grammatical Modality)
**TBTA Field**: Mood
**Date**: 2025-11-27
**Status**: Stage 2 Complete

## Summary

Mood encodes the speaker's attitude toward an action: factual (Indicative), commanded (Obligation types), or possible (Potential types).

### Key Findings

| Metric | Value |
|--------|-------|
| Total TBTA annotations | 72,089 |
| Unique verses | 11,544 |
| Indicative dominance | 97.21% |
| Zero-shot accuracy | 55% |
| Guided accuracy | 51% |

**Main insight**: TBTA mood labels use idiosyncratic criteria that don't match standard linguistic definitions. The guided baseline performed *worse* than zero-shot, indicating definitions don't help.

## Distribution

| Label | Count | Percentage |
|-------|-------|------------|
| Indicative | 70,079 | 97.21% |
| 'must' Obligation | 633 | 0.88% |
| 'should' Obligation | 567 | 0.79% |
| 'might' Potential | 367 | 0.51% |
| 'should not' Obligation | 158 | 0.22% |
| 'may' (permissive) | 150 | 0.21% |
| Forbidden Obligation | 121 | 0.17% |
| Definite Potential | 8 | 0.01% |
| Probable Potential | 5 | 0.01% |
| Unlikely Potential | 1 | 0.001% |

## Files

### Data Files
- `data/train.jsonl` - 283 entries, balanced across moods
- `data/validate.jsonl` - 101 entries, labels hidden
- `data/validate.secret.jsonl` - Validation with labels
- `data/test.jsonl` - 96 entries, labels hidden
- `data/test.secret.jsonl` - Test with labels
- `data/leftovers.jsonl` - 71,283 remaining entries

### Analysis Files
- `HIGH-LEVEL-REVIEW.md` - Baseline comparison and insights
- `EDGE-CASES.md` - When NOT to use Indicative
- `TBTA-QUALITY.md` - Data quality issues
- `WORD-ANALYSIS.md` - Translation word patterns
- `word-analysis.jsonl` - Raw word pattern data
- `grouped-by-reason.jsonl` - Theological groupings

## Baseline Analysis

### Zero-Shot (55%)

LLM predicts mood without any guidance:

**Error patterns**:
- 'must' → 'should': 5 cases
- 'should not' → 'should': 4 cases
- Indicative ↔ 'might': 7 cases

### Guided (51%)

LLM predicts mood WITH definitions provided:

**Error patterns**:
- 'should not' → Indicative: 6 cases
- 'should' → Indicative: 6 cases
- 'may' → Indicative: 4 cases

**Conclusion**: Standard linguistic definitions actually hurt performance. TBTA has its own internal logic.

## Recommendations for Stage 3

1. **Two-stage classifier**: First Indicative vs Non-Indicative, then subtype
2. **Learn patterns empirically**: Don't rely on linguistic definitions
3. **Focus on context**: Law codes, conditionals, speech types
4. **Use source morphology**: Hebrew/Greek mood forms may help
5. **Add Strong's numbers**: Enable lexeme-based analysis

## Data Quality Issues

1. **Extreme class imbalance**: 97% Indicative
2. **Rare potential categories**: <15 examples total
3. **Overlapping obligations**: must/should/forbidden unclear
4. **Missing Strong's numbers**: Can't do lexeme analysis
5. **Inconsistent labeling**: Some questionable annotations

See `TBTA-QUALITY.md` for full details.

## Next Steps

1. Stage 3: Build empirical classifier
2. Request Strong's numbers from TBTA
3. Clarify obligation spectrum with TBTA team
4. Consider merging rare potential categories
