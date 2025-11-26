# TBTA Stage 2 Analysis Review - Number Systems Feature

**Status**: Complete
**Started**: 2025-11-26
**Goal**: Validate and audit Stage 2 instructions before scaling to other features

## Execution Summary

| Step | Status | Notes |
|------|--------|-------|
| 1. Extract TBTA Data | DONE | 171,876 annotations extracted |
| 2. Verse Enrichment | DONE | Created fast cache-based script |
| 3. Dataset Split | DONE | 1339 train / 446 validate / 448 test |
| 4. Strong's Analysis | DONE | Word patterns found but limited utility |
| 5. Reason Grouping | DONE | 7 theological groups identified |
| 6. Quick Solution | DONE | 26% accuracy - not a quick win |
| 7. AgentDB ML | IN PROGRESS | Exploring vector search approach |
| 8. Documentation | PENDING | |

## Data Distribution

Full TBTA extraction:
- Singular: 113,745 (66.2%)
- Plural: 55,654 (32.4%)
- Dual: 1,744 (1.0%)
- Trial: 496 (0.3%)
- **Quadrial: 185 (0.1%) - SUSPICIOUS (no language has true quadrial)**
- Paucal: 52 (0.03%)

## Issues Found

### 1. CRITICAL: Environment Variable Required
- **Issue**: `group_by_strongs.py` and `group_by_reasons.py` fail without `MYBIBLE_DATA_DIR`
- **Fix**: Set `export MYBIBLE_DATA_DIR=/workspace/.data` before running scripts
- **Recommendation**: Add env var check at script start with helpful error message

### 2. Script: enrich_extract_with_verses.py Too Slow
- **Issue**: Uses BibleHub network calls (~30 seconds per 100 entries)
- **Fix**: Created `enrich_from_cache.py` that uses local cache only (~9 sec for 2233 entries)
- **Recommendation**: Update Stage 2 instructions to use cache script, or add --cache-only flag

### 3. YAML Schema Mismatch: group_by_reasons.py
- **Issue**: Script expects `{group: {patterns: [], keywords: []}}` format
- **Reality**: `THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml` uses different structure (`non_arbitrary_contexts` list with `verse_pattern`)
- **Fix**: Used default groups instead. Custom groups need format conversion.
- **Recommendation**: Either fix script to handle new format OR fix YAML to match expected format

### 4. Logical Classifier Limited Utility
- **Issue**: On balanced test set, simple rules achieve only 26% (baseline 17%)
- **Analysis**: Rules work for body parts (Dual) but miss Trial/Quadrial patterns
- **Insight**: Need embedding-based approach for these edge cases

### 5. Cache Coverage Gap
- **Issue**: Only ~10% of verses have cached translations
- **Impact**: Most entries enriched without verse text
- **Recommendation**: Either run full eBible clone OR accept sparse enrichment for now

## Scripts Created/Modified

1. `/workspace/src/ingest_data/tbta/enrich_from_cache.py` - Fast cache-only enrichment
2. `/workspace/bible-study-tools/tbta/features/number-systems/analysis/logical.py` - Rule-based classifier

## Recommendations for Stage 2 Instructions

1. Add prerequisite: `export MYBIBLE_DATA_DIR=/workspace/.data`
2. Use cache-based enrichment by default (much faster)
3. Fix YAML schema mismatch between groups file and script
4. Add note about Quadrial being suspicious data (should be 0)
5. Clarify that balanced sample != full distribution accuracy
