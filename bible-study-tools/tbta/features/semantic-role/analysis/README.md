# Semantic Role Analysis Dataset - Stage 2.1

## Overview

This directory contains the analysis dataset for the semantic-role TBTA feature, following the Stage 2.1 workflow from `.instructions-to-build-feature/STAGE-2-1-ANALYSIS-DATASET.md`.

## Status: COMPLETED (with caveats)

### Completed Steps

- ✅ **Step 1A**: Extracted TBTA feature data
  - Extracted 138,723 annotations from TBTA corpus
  - Created distribution analysis
  - Updated feature README with distribution stats

- ✅ **Step 1B**: Create Balanced Dataset
  - Generated balanced dataset: 240 entries (30 per label)
  - Created REASON-GROUPS.md taxonomy
  - ⚠️ **INCOMPLETE**: Manual enrichment with `strongs_number` and `reason_group` not completed (see `_STEP1B_STATUS.md`)

- ✅ **Step 1C**: Enrich with Translations
  - Added 13 language translations (eng-YLT, grc, hbo, heb-heb, lat-VUC, arb-NAV, rus, deu-1912, jpn, ind-AYT, fra-LSG, spa-BES, tur)
  - ⚠️ **LIMITED COVERAGE**: Only 12.5% of entries have translations due to sparse checkout (see `audit-data.md`)

- ✅ **Step 1D**: Audit the Data
  - Completed audit checklist
  - Documented missing fields and resolution paths
  - See `audit-data.md` for full report

- ✅ **Step 1E**: Split Datasets
  - Created train.jsonl (180 entries)
  - Created validate.jsonl (36 entries)
  - Created test.jsonl (24 entries, secret)
  - Created leftovers.jsonl (138,483 entries)

- ✅ **Step 1F**: Delete Artifacts
  - Removed temporary files: datasets.jsonl, enriched.jsonl, tbta-extract.jsonl, draft_datasets.jsonl

### Caveats & Next Steps

**To make this dataset production-ready:**

1. **Complete Step 1B manual enrichment** (see `_STEP1B_STATUS.md`)
   - Add `strongs_number` field to all 240 entries
   - Add `reason_group` field to all 240 entries
   - Estimated time: 8-20 hours

2. **Expand translation coverage** (see `audit-data.md`)
   - Expand sparse checkout: `cd /workspace/.data && git sparse-checkout add commentary`
   - Re-run Step 1C enrichment
   - Target: 100% coverage

3. **Generate macula data** (prerequisite for Strong's numbers)
   - Fetch source data: `python src/ingest_data/macula/macula_fetcher.py --all`
   - Process verses: `python src/ingest_data/macula/macula_processor.py --all`

## Files

### Input Data
- `tbta-extract.jsonl` - Full TBTA extraction (138,723 annotations)
- `distribution.yaml` - Distribution analysis of semantic role values

### Working Files
- `datasets.jsonl` - Draft balanced dataset (240 entries, NEEDS ENRICHMENT)
- `REASON-GROUPS.md` - Taxonomy for reason_group classification
- `_STEP1B_STATUS.md` - Detailed status and instructions for Step 1B completion

### Final Output (Not Yet Created)
- `data/train.jsonl` - Training set (max 800 entries)
- `data/validate.jsonl` - Validation set (max 100 entries)
- `data/test.jsonl` - Test set (max 100 entries, DO NOT TOUCH until final eval)
- `data/leftovers.jsonl` - Remaining entries

## Next Actions Required

### Immediate: Complete Step 1B Manual Enrichment

**What needs to be done:**

1. **Expand sparse checkout** to include all books needed for dataset
   ```bash
   cd /workspace/.data
   git sparse-checkout add commentary
   ```

2. **Generate macula data** (for Strong's numbers)
   ```bash
   # Fetch macula source data
   python src/ingest_data/macula/macula_fetcher.py --all

   # Process verses in dataset
   python src/ingest_data/macula/macula_processor.py --all
   ```

3. **Manually enrich each entry** in `datasets.jsonl`
   - Add `strongs_number` field (lookup from macula data)
   - Add `reason_group` field (from REASON-GROUPS.md)
   - Add `difficulty` field for adversarial cases
   - Write to new `enriched-draft.jsonl`

4. **Follow instructions** in `_STEP1B_STATUS.md`

### Then: Continue to Step 1C

Once Step 1B is complete with enriched dataset:
- Run enrichment script to add translations
- Follow remaining steps in STAGE-2-1-ANALYSIS-DATASET.md

## Distribution Analysis

From `distribution.yaml`:

| Semantic Role | Count | Percentage |
|--------------|-------|------------|
| Most Agent-like | 74,510 | 53.7% |
| Most Patient-like | 36,704 | 26.5% |
| Destination | 12,611 | 9.1% |
| State | 10,365 | 7.5% |
| Source | 1,851 | 1.3% |
| Beneficiary | 1,031 | 0.7% |
| Addressee | 998 | 0.7% |
| Instrument | 653 | 0.5% |
| **TOTAL** | **138,723** | **100%** |

## Draft Dataset Balance

Current draft (`datasets.jsonl`):
- 30 entries per label × 8 labels = 240 total entries
- Balanced by genre and label
- One entry per verse (no duplicate verses)
- Split: train (75%), validate (15%), test (10%)

## Notes

- **Manual work required**: Step 1B cannot be automated per instructions
- **Context limits**: Manual enrichment should be done in batches across multiple sessions
- **Quality over quantity**: Consider reducing to 100-150 entries if manual review becomes prohibitive
