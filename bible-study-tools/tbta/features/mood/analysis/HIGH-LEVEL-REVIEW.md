# Mood Feature: Baseline Analysis

**Date**: 2025-11-29
**Sample Size**: 100 verses (stratified from train.jsonl)

## 1. Accuracy Comparison

| Test | Accuracy | Notes |
|------|----------|-------|
| Haiku (no metadata) | 41.1% | Direct LLM prediction |
| Sonnet (no metadata) | 48.5% | Direct LLM prediction |
| Sonnet (with metadata) | **50.0%** | Best overall |
| **Improvement** | +8.9% | Haiku→Sonnet w/metadata |

**Key Finding**: Metadata helps (+1.5% from sonnet to metadata). Sonnet significantly outperforms Haiku (+7.4%).

## 2. Error Pattern Analysis (from score_direct_metadata_sonnet.md)

### Most Confused Label Pairs

| Predicted | Actual | Count | Pattern |
|-----------|--------|-------|---------|
| Indicative | 'should' Obligation | 8 | Implicit moral guidance missed |
| Definite Potential | Indicative | 6 | Over-predicting future/prophecy |
| Definite Potential | 'might' Potential | 4 | Certainty vs uncertainty confused |
| 'must' Obligation | 'should' Obligation | 3 | Obligation strength confused |
| Forbidden Obligation | Indicative | 2 | Prohibitions over-detected |

### Sample Errors

| Line | Verse | Predicted | Actual | Analysis |
|------|-------|-----------|--------|----------|
| 18 | GEN-022-002 | 'must' Obligation | 'should' Obligation | Abraham **sacrifice** - LLM sees divine command as 'must', TBTA says 'should' |
| 23 | MRK-008-021 | Indicative | 'should' Obligation | Disciples **understand** - rhetorical question implies obligation |
| 24 | MAT-005-043 | 'must' Obligation | 'should' Obligation | Person **love** all - Jesus teaching, LLM says 'must', TBTA says 'should' |
| 30 | MRK-010-033 | Definite Potential | 'must' Obligation | Messiah **suffer** - prophecy but TBTA codes as obligation |

## 3. Distribution Comparison

| Label | Ground Truth | Direct Sonnet | Direct w/Metadata |
|-------|-------------|---------------|-------------------|
| Indicative | 44 | ~35 | 47 |
| 'should' Obligation | 16 | ~20 (mixed with 'must') | 7 |
| 'must' Obligation | 13 | ~20 | 15 |
| Forbidden Obligation | 9 | ~8 | 7 |
| 'might' Potential | 8 | ~5 | 0 |
| 'may' (permissive) | 5 | ~5 | 8 |
| 'should not' Obligation | 5 | ~2 | 1 |
| Definite Potential | 0 | ~5 | 14 |
| Probable Potential | 0 | ~0 | 1 |

**Key Issue**: LLM predicts "Definite Potential" (14 times) but ground truth has 0. This category may not exist in this sample or TBTA uses it differently.

## 4. 'should' vs 'must' Obligation Pattern

The LLM struggles to distinguish these. TBTA appears to use:
- **'must'**: Legal requirements, divine commands with no option
- **'should'**: Moral teaching, wisdom, exhortation (even divine teaching)

Examples where LLM predicted 'must' but TBTA says 'should':
- GEN-022-002: Abraham **sacrifice** Isaac - divine command but coded 'should'?
- MAT-005-043: **love** all people - Jesus's teaching coded 'should'

**Possible Issue**: TBTA may be coding based on target language translation choices, not source language semantics.

## 5. Recommendations

### Immediate Actions
1. **Audit 'should' vs 'must'**: Review TBTA criteria - is there a pattern?
2. **Remove Definite Potential**: Not in ground truth, causes false positives
3. **Focus on Indicative detection**: Get the 44% Indicative cases right first

### Prompt Engineering Ideas
1. Add: "Use 'should' for moral teaching and wisdom, 'must' only for legal requirements"
2. Add: "Definite Potential is rare - prefer 'might' for future events"
3. Genre-aware: "In wisdom literature, prefer 'should'"

### Data Investigation
1. Why does TBTA code divine commands as 'should'?
2. Is there translator variation in obligation strength?
3. Are 'should not' and Forbidden consistently applied?

## 6. Comparison: Word-Analysis vs Direct LLM

The subagents initially tried to write Python analysis scripts instead of direct prediction.

| Approach | Haiku | Sonnet | w/Metadata |
|----------|-------|--------|------------|
| Word-analysis (wrong) | 31.2% | 41.0% | 45.0% |
| Direct LLM (correct) | 41.1% | 48.5% | 50.0% |
| **Improvement** | +9.9% | +7.5% | +5.0% |

**Lesson**: Direct LLM prediction significantly outperforms rule-based analysis. The LLM's pre-training knowledge is valuable.

## Prompts Used

### Test A (No Metadata)
```
Read verses and write your mood predictions directly to a file.

INPUT: train-no-decoration.jsonl (verse + text only)
LABELS: Indicative, 'must' Obligation, 'should' Obligation, ...

For each of the 100 lines, decide what mood the **bolded** word represents.
One label per line, 100 lines total, in order.
NO PYTHON ANALYSIS - just read, predict, write.
```

### Test B (With Metadata)
Same as Test A but using train-no-labels.jsonl with full translations, Strong's numbers, genre.

## Conclusion

**50% baseline accuracy** is a reasonable starting point. Key issues:
1. 'should' vs 'must' distinction unclear in TBTA
2. "Definite Potential" over-predicted (need to understand when TBTA uses it)
3. Metadata helps modestly (+1.5%)

**Next Steps**: Investigate TBTA labeling criteria for obligation strength before prompt engineering.
