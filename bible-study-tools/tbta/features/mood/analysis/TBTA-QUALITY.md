# TBTA Data Quality Assessment: Mood Feature

## Overview

This document identifies data quality issues in the TBTA Mood annotations that may affect model training and accuracy.

## Quality Issues Identified

### Issue 1: Extreme Class Imbalance

| Label | Count | Percentage |
|-------|-------|------------|
| Indicative | 70,079 | 97.21% |
| All other moods | 2,010 | 2.79% |

**Impact**: Any classifier can achieve 97%+ accuracy by always predicting Indicative. Need balanced evaluation metrics.

**Recommendation**: Use F1-score per class or macro-averaged F1 for evaluation.

### Issue 2: Rare "Potential" Categories

Three potential categories have almost no examples:
- Definite Potential: 8 cases (0.01%)
- Probable Potential: 5 cases (0.01%)
- Unlikely Potential: 1 case (0.001%)

**Impact**: Cannot reliably train or evaluate these categories.

**Recommendation**: Consider merging into single "Potential" category or removing these labels entirely.

### Issue 3: Overlapping Obligation Categories

The distinction between obligation types is unclear:
- 'must' Obligation (633 cases)
- 'should' Obligation (567 cases)
- 'should not' Obligation (158 cases)
- Forbidden Obligation (121 cases)

**Evidence from baseline tests**:
- 5 confusions between 'must' and 'should'
- 4 confusions between 'should not' and 'should'
- 2 confusions between Forbidden and 'should'

**Questions for TBTA team**:
1. What distinguishes 'must' from 'should' obligation?
2. Why separate "Forbidden" from "'should not'"?
3. Is this based on source language morphology or semantic intent?

### Issue 4: Semantic vs Morphological Basis Unclear

TBTA mood labels appear to encode:
- Speaker intent (what should happen)
- Epistemic status (certainty)
- Deontic force (obligation strength)

But source language moods (Hebrew waw-consecutive, Greek subjunctive) have morphological bases.

**Example confusion**:
- GEN.020.11 "they might kill me" - TBTA: 'might' Potential
  - But in Hebrew this may be a simple narrative form

**Recommendation**: Document whether TBTA mood is based on:
- Source language morphology
- Target language semantic rendering
- Or a hybrid approach

### Issue 5: Missing Strong's Numbers

The TBTA extract does not include Strong's numbers for words. This prevents:
- Lexeme-based pattern analysis
- Cross-referencing with source language morphology
- Building lexicon-based hints

**Recommendation**: Add Strong's numbers via enrichment or request from TBTA.

### Issue 6: Inconsistent Label Application

Some examples suggest inconsistent labeling:

| Verse | TBTA Label | Expected | Issue |
|-------|------------|----------|-------|
| JHN.002.04 | 'should not' | Indicative? | Mary's action is past tense |
| 1KI.018.09 | 'may' (permissive) | 'might' Potential? | Obadiah fears Ahab "may kill" him |

**Recommendation**: Review edge cases with theological advisors.

## Recommendations Summary

1. **Merge rare categories**: Combine Definite/Probable/Unlikely Potential
2. **Clarify obligation spectrum**: Document criteria for must/should/forbidden
3. **Add Strong's numbers**: Enable lexeme-based analysis
4. **Create annotation guidelines**: Help future labelers be consistent
5. **Review ambiguous cases**: Flag uncertain labels for expert review

## Questions for TBTA Team

1. What determines 'must' vs 'should' obligation in TBTA annotation guidelines?
2. Should "Forbidden Obligation" and "'should not' Obligation" be merged?
3. Are the Definite/Probable/Unlikely Potential categories used consistently?
4. Is mood assigned based on source morphology or semantic intent?
5. Can Strong's numbers be added to future exports?
