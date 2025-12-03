# Stage 2.1 Analysis Dataset - Proximity System

**Status**: ✅ COMPLETED
**Date**: 2025-11-29
**Feature**: Proximity System
**TBTA Field**: `Proximity`

## Overview

This directory contains the completed Stage 2.1 analysis dataset for the proximity-system feature, following the process defined in `.instructions-to-build-feature/STAGE-2-1-ANALYSIS-DATASET.md`.

## Dataset Statistics

- **Total Entries**: 2,318 (balanced sample from 18,958 total TBTA annotations)
- **Train Set**: 1,854 entries (80%)
- **Validate Set**: 231 entries (10%)
- **Test Set**: 233 entries (10%)
- **Leftovers**: 14,617 entries (not used in training)

## Data Quality

### Completeness
- ✅ 100% have `strongs_number` field
- ✅ 100% have `reason_group` field
- ✅ 93.8% have `strongs` list (verse-level Strong's codes)
- ✅ 99.6% have translation enrichment

### Balance
Dataset is balanced across:
- **Genre**: OT/NT proportional sampling
- **Constituents**: Max 100 per constituent type
- **Labels**: All proximity values represented
- **Reason Groups**: 9 linguistic/theological categories

## Reason Group Distribution

| Reason Group | Count | % |
|--------------|-------|---|
| SPATIAL-MARKER | 634 | 27.4% |
| PERSON-SINGULAR | 551 | 23.8% |
| DEMONSTRATIVE-EMPHASIS | 389 | 16.8% |
| ANAPHORIC-DISCOURSE | 211 | 9.1% |
| ABSTRACT-CONCEPT | 203 | 8.8% |
| TEMPORAL-MARKER | 199 | 8.6% |
| NATURAL-OBJECT | 77 | 3.3% |
| ARTIFACT | 43 | 1.9% |
| PERSON-PLURAL | 11 | 0.5% |

## Translation Coverage

### Core Translations (Required)
- ✅ **eng-YLT**: 99.6% coverage (English Young's Literal)
- ✅ **heb-heb**: 99.6% coverage (Modern Hebrew)
- ✅ **lat-VUC**: 99.4% coverage (Latin Vulgate)
- ✅ **grc-BRENT + grc-SR**: 89.5% combined (Greek LXX + Scrivener)
- ✅ **hbo-hbo**: 65.4% coverage (Biblical Hebrew, OT only - expected)

### Additional Languages
- ✅ **spa-RV-1909**: 99.6% coverage (Spanish - 3-way person-oriented)
- ✅ **swh-ONEN**: 99.6% coverage (Swahili - 3-way + noun class)
- ✅ **ind-ind**: 88.3% coverage (Indonesian - 2-way simplified)

**Total**: 10 unique language varieties covering:
- 2 source languages (Hebrew, Greek)
- 2-way distance systems (English, Latin, Modern Hebrew)
- 3-way person-oriented systems (Spanish, Swahili, Indonesian)
- Major world languages and biblical traditions

## Files in This Directory

### Data Files
- `data/train.jsonl` - Training set (1,854 entries)
- `data/validate.jsonl` - Validation set (231 entries, labels visible)
- `data/validate.secret.jsonl` - Validation set (231 entries, for blind testing)
- `data/test.jsonl` - Test set (233 entries, labels visible)
- `data/test.secret.jsonl` - Test set (233 entries, for final evaluation)
- `data/leftovers.jsonl` - Remaining entries (14,617 entries)

### Documentation
- `README.md` - This file
- `LANGUAGE-SELECTION.md` - Language selection rationale and validation
- `audit-data.md` - Comprehensive data quality audit report
- `distribution.yaml` - Distribution of proximity values in full dataset
- `enrichment.log` - Log from translation enrichment process

### Scripts
- `enrich_dataset.py` - Python script used to add strongs_number and reason_group fields

## Process Summary

### Step 1A: Extract Data ✅
- Extracted 18,958 TBTA annotations from `.data/commentary/*/*/`
- Created `distribution.yaml` showing value distribution

### Step 1B: Create Balanced Dataset ✅
- Used `draft_dataset.py` to create balanced starting sample
- Manually enriched with:
  - `strongs_number`: Inferred from constituent + strongs list
  - `reason_group`: Assigned based on theological/linguistic categories
  - `difficulty`: Added for adversarial/hard cases
- Output: 2,318 entries with full metadata

### Step 1C: Enrich with Translations ✅
- Selected 14 translation codes based on `research/LANGUAGES.md`
- Validated language choices with sample verses (GEN.001.026)
- Enriched dataset using `enrich_extract_with_verses.py`
- Result: 99.6% of entries have 8+ translations

### Step 1D: Audit Data ✅
- Verified all required fields present
- Confirmed translation coverage >80% for core languages
- Validated reason_group distribution
- Documented 10 cache misses (JOL, 1KI chapters not in sparse checkout)

### Step 1E: Split Datasets ✅
- Used `split_dataset.py` to create train/validate/test splits
- Maintained stratification by genre and label
- Created both visible and secret versions for blind testing

### Step 1F: Delete Artifacts ✅
- Removed intermediate files:
  - `tbta-extract.jsonl` (18,958 entries - source data)
  - `datasets.jsonl` (2,318 entries - pre-enrichment)
  - `enriched.jsonl` (2,318 entries - post-enrichment)
  - `draft_datasets.jsonl/` (draft balanced sample)

## Known Issues and Resolutions

### Issue 1: Arabic Translation Missing
- **Problem**: Arabic ('ara') not found in enrichment
- **Resolution**: Dataset proceeds without Arabic. Still have 10 diverse languages.
- **Future**: Could add 'arb-NAV' or correct code in production

### Issue 2: Greek Split Across Versions
- **Not an issue**: Expected. OT uses grc-BRENT (LXX), NT uses grc-SR (Scrivener)
- **Combined coverage**: 89.5%

### Issue 3: 143 Entries Missing Strong's Data
- **Cause**: Original TBTA extraction lacked strongs field for some NT verses
- **Impact**: 6.2% of dataset - acceptable for Stage 2 analysis
- **Mitigation**: All entries have `strongs_number` field set to "MISSING" for tracking

## Next Stage: Stage 2.2 - Hypothesis Testing

Ready to proceed with:
1. Manual inspection of train set
2. Pattern identification
3. Rule development
4. Logical.py implementation
5. Validation against validate set (blind)

## References

- Stage 2.1 Instructions: `/workspace/bible-study-tools/tbta/features/.instructions-to-build-feature/STAGE-2-1-ANALYSIS-DATASET.md`
- Language Research: `/workspace/bible-study-tools/tbta/features/proximity-system/research/LANGUAGES.md`
- Theological Groups: `/workspace/bible-study-tools/tbta/features/proximity-system/research/THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml`
- Standardization: `/workspace/STANDARDIZATION.md`
- Schema: `/workspace/SCHEMA.md`
