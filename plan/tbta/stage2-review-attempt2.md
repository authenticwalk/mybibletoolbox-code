# Stage 2 Analysis Review - Attempt 2

**Feature**: number-systems
**Date**: 2025-11-26
**Objective**: Execute Stage 2 Analysis instructions step-by-step, verifying scripts work and documenting issues

## Status - COMPLETE

- [x] Step 1: Create Dataset
  - [x] Extract TBTA data (171,876 annotations)
  - [x] Create balanced dataset (527 entries, LLM manual task)
  - [x] Enrich with 17 translations
  - [x] Split into train/validate/test/leftovers
- [x] Step 2: LLM Baseline Analysis (76% accuracy)
- [x] Step 3: Analyze Patterns (Parallel)
  - [x] 3A: Dominant Value Analysis - EDGE-CASES.md
  - [x] 3B: TBTA Label Quality - TBTA-QUALITY.md
  - [x] 3C: Strong's Word Patterns - STRONGS.md
  - [x] 3D: Word Patterns - WORD-ANALYSIS.md
  - [x] 3E: Logical Reason Analysis - reason-groupings-with-hints.jsonl
- [x] Step 7: Document Results - analysis/README.md

## Progress Log

### Step 1: Extract TBTA Data

**Completed**: 2025-11-26 23:11

- Extracted 171,876 annotations from 11,649 TBTA verse files
- Distribution:
  - Singular: 113,745 (66.2%)
  - Plural: 55,654 (32.4%)
  - Dual: 1,744 (1.0%)
  - Trial: 496 (0.3%)
  - Quadrial: 185 (0.1%) - SUSPICIOUS (no attested language)
  - Paucal: 52 (0.03%)

**Script tested**: `src/ingest_data/tbta/extract_feature.py` - WORKS correctly

### Step 1b: Create Balanced Dataset (LLM Task)

**Completed**: 2025-11-26 23:40

- Manually curated 527 entries with metadata
- Added: strongs_number, strongs_word, theological_group, literary_type, difficulty
- Balanced across labels, OT/NT, literary types

**Note**: Instructions correctly require LLM manual curation (not script) for adding enrichment fields

### Step 1c: Enrich with Translations

**Completed**: 2025-11-26 23:44

- Enriched with 17 languages: eng, heb, ara, spa, fra, deu, por, rus, ind, swh, meu, tgl, zho, tha, vie, tur, grc
- 527 entries processed, 1 error (timeout on GEN.009.019)
- 39 cache hits (verses appearing multiple times)

**Script tested**: `src/ingest_data/tbta/enrich_extract_with_verses.py` - WORKS correctly

### Step 1d: Split Datasets

**Completed**: 2025-11-26 23:44

- Train: 331 entries (labels visible)
- Validate: 100 entries (labels hidden in validate.secret.jsonl)
- Test: 96 entries (labels hidden in test.secret.jsonl)
- Leftovers: 171,260 entries

**Script tested**: `src/tools/predict/split_dataset.py` - WORKS correctly
- Properly renames source files to .secret.jsonl
- Correctly strips labels from validate/test public files

### Step 2: LLM Baseline Analysis

**Completed**: 2025-11-26 23:46

- Accuracy: 76/100 (76%)
- Major error: Paucal → Plural (41.7% of errors)
- LLM over-applies Trial to Trinity passages (but TBTA sometimes uses Plural!)

**Key Finding**: TBTA data quality issues - Trinity passages inconsistently labeled

### Step 3: Parallel Analyses

**Completed**: 2025-11-26 23:52

All analyses ran successfully in parallel via subagents:

1. **EDGE-CASES.md**: Documented when NOT Singular/Plural
2. **TBTA-QUALITY.md**: Critical review - found Trinity inconsistency, Quadrial issues
3. **STRONGS.md**: No Strong's reliably predicts number (context-dependent)
4. **WORD-ANALYSIS.md**: "two/four/few" are discriminative words

**Script tested**: `src/ingest_data/tbta/group_by_strongs.py` - WORKS correctly
**Script tested**: `src/ingest_data/tbta/group_by_reasons.py` - WORKS correctly

### Step 7: Document Results

**Completed**: 2025-11-26 23:55

- Created analysis/README.md with full summary
- Updated features/number-systems/README.md with Stage 2 results

## Issues Found with Instructions

1. **Line 53 clarification worked**: "LLM task" instruction was clear after update
2. **append_to_verses.py**: Script exists but wasn't needed for this feature (hints stored in JSONL)
3. **Parallel subagents**: Works well for Steps 3A-3D

## Script Audit Summary

| Script | Status | Notes |
|--------|--------|-------|
| extract_feature.py | ✅ WORKS | 171,876 annotations in 3 seconds |
| enrich_extract_with_verses.py | ✅ WORKS | 527 entries, 17 languages |
| split_dataset.py | ✅ WORKS | Proper secret file handling |
| group_by_strongs.py | ✅ WORKS | Outputs JSONL analysis |
| group_by_reasons.py | ✅ WORKS | Groups by theological reasons |
| append_to_verses.py | ⚠️ NOT TESTED | Exists but not needed for this run |

## Recommendations for Stage 2 Instructions

1. **Add validation step**: Check dataset sizes match targets before enrichment
2. **Parallel analysis**: Explicitly mention subagents can run 3A-3D in parallel
3. **LLM baseline**: Clarify that subagent should have NO memory of training labels
