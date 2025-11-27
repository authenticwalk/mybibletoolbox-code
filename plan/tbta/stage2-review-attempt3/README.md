# Stage 2 Analysis Review - Mood Feature (Attempt 3)

**Date**: 2025-11-27
**Feature**: Mood (Grammatical Modality)
**Goal**: Execute and validate Stage 2 instructions on mood feature
**Status**: COMPLETE

## Overview

Successfully executed Stage 2 Analysis on the "mood" TBTA feature. This document records what worked, issues found, and recommendations.

## Status Tracker

| Step | Status | Notes |
|------|--------|-------|
| 1.1 Extract TBTA Data | ✅ | 72,089 annotations extracted |
| 1.2 Create Balanced Dataset | ✅ | 480 entries, stratified by mood |
| 1.3 Validate Language Selection | ✅ | eng,spa,fra,deu,por,rus,swh,tur,arb,jpn |
| 1.4 Enrich with Translations | ✅ | All languages enriched |
| 1.5 Split Datasets | ✅ | 283 train / 101 validate / 96 test |
| 2.1 Zero-shot Baseline | ✅ | 55% accuracy |
| 2.2 Guided Baseline | ✅ | 51% accuracy (WORSE!) |
| 2.3 HIGH-LEVEL-REVIEW.md | ✅ | Created |
| 3A EDGE-CASES.md | ✅ | Non-indicative patterns documented |
| 3B TBTA-QUALITY.md | ✅ | Data quality issues documented |
| 3C Strong's Analysis | ⏭️ SKIPPED | No Strong's numbers in data |
| 3D Translation Morphology | ✅ | word-analysis.jsonl created |
| 3E Reason Grouping | ✅ | grouped-by-reason.jsonl created |
| 7 Final Documentation | ✅ | README.md files updated |

## Issues Found

### 1. Strong's Numbers Missing

**Problem**: The `datasets.jsonl` and enriched data don't include Strong's numbers.

**Impact**: Can't run `group_by_strongs.py` properly - falls back to "ALL" grouping.

**Solution**: Stage 2 instructions should include a step to add Strong's numbers via LLM inference or lookup before enrichment.

### 2. Baseline Test Format Mismatch

**Problem**: The baseline TSV output format doesn't include constituent, making matching ambiguous when multiple entries have same verse.

**Current**: `VERSE\tLABEL` (e.g., `GEN.001.001\tIndicative`)
**Better**: `VERSE\tCONSTITUENT\tLABEL`

### 3. Guided Baseline Performed Worse

**Problem**: Providing definitions actually REDUCED accuracy from 55% to 51%.

**Implication**: TBTA mood labels use idiosyncratic criteria that don't match standard linguistic definitions. The Stage 2 instructions assume definitions help - this isn't true for mood.

### 4. Reason Groupings Not Mood-Specific

**Problem**: Default theological groupings (TRINITY, DIVINE_SPEECH, etc.) don't capture mood-relevant categories.

**Result**: 263/283 entries (93%) classified as "UNSET"

**Solution**: Create mood-specific groupings (LAW_CODE, CONDITIONAL, COMMAND, QUESTION, etc.)

### 5. Class Imbalance Extreme

**Problem**: 97.21% Indicative means a "always Indicative" classifier gets 97% accuracy.

**Impact**: Accuracy is misleading. Need F1-macro or per-class metrics.

## Script Audit Results

| Script | Works? | Issues |
|--------|--------|--------|
| `extract_feature.py` | ✅ | None |
| `enrich_extract_with_verses.py` | ✅ | Requires absolute paths |
| `split_dataset.py` | ✅ | Renames original files to .secret |
| `group_by_strongs.py` | ⚠️ | Needs strongs_number field |
| `group_by_reasons.py` | ⚠️ | Default groups not mood-relevant |

## Recommendations for Stage 2 Instructions

### High Priority

1. **Add Strong's enrichment step** between 1.2 and 1.4
2. **Create feature-specific reason groupings** for each feature
3. **Fix baseline format** to include constituent for unique matching
4. **Add F1-macro metric** alongside accuracy for imbalanced features

### Medium Priority

5. **Document when definitions help vs hurt** - mood showed definitions hurt
6. **Add data quality checkpoint** before proceeding
7. **Validate language availability** before enrichment to avoid errors

### Low Priority

8. Consider automating the balanced dataset creation
9. Add progress indicators to enrichment script
10. Create feature-specific baseline test templates

## Files Created

```
bible-study-tools/tbta/features/mood/analysis/
├── README.md
├── HIGH-LEVEL-REVIEW.md
├── EDGE-CASES.md
├── TBTA-QUALITY.md
├── WORD-ANALYSIS.md
├── datasets.jsonl
├── enriched.secret.jsonl
├── tbta-extract.secret.jsonl
├── word-analysis.jsonl
├── grouped-by-reason.jsonl
└── data/
    ├── train.jsonl (283 entries)
    ├── validate.jsonl (101 entries, no labels)
    ├── validate.secret.jsonl (with labels)
    ├── test.jsonl (96 entries, no labels)
    ├── test.secret.jsonl (with labels)
    ├── leftovers.jsonl (71,283 entries)
    ├── baseline_test_input.jsonl
    ├── baseline_test_answers.secret.jsonl
    ├── baseline_zero_shot.tsv
    └── baseline_guided.tsv
```

## Summary

Stage 2 Analysis completed successfully for the Mood feature. Main finding: TBTA mood labels use non-standard criteria, making linguistic definitions counterproductive. Future work should learn patterns empirically rather than relying on definitions.
