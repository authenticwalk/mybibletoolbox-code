# Participant Tracking - Analysis Dataset

## Overview

This directory contains the analysis dataset for the Participant Tracking feature, created following the Stage 2.1 process defined in `.instructions-to-build-feature/STAGE-2-1-ANALYSIS-DATASET.md`.

## Dataset Statistics

### Source Data
- **Total TBTA annotations extracted**: 171,876
- **Source**: TBTA Database export
- **Extraction date**: 2025-11-29

### Value Distribution (from TBTA)
| Label | Count | Percentage |
|-------|-------|------------|
| Routine | 125,543 | 73.04% |
| Generic | 23,856 | 13.88% |
| Frame Inferable | 12,815 | 7.46% |
| First Mention | 9,267 | 5.39% |
| Interrogative | 394 | 0.23% |
| Offstage | 1 | 0.00% |

### Balanced Dataset
- **Total entries after balancing**: 4,153
- **Balancing strategy**: Genre-balanced, one per verse, sampled by constituent
- **Label caps**: Max 1,000 per major label (Interrogative: 152, Offstage: 1)

### Dataset Splits
- **Training set**: 3,322 entries (80%)
- **Validation set**: 415 entries (10%)
- **Test set**: 416 entries (10%)
- **Leftovers**: 160,755 entries (not included in train/val/test)

### Enrichment

#### Strong's Numbers
- **Entries with strongs_number**: 3,873 (93.26%)
- **Missing strongs_number**: 280 (6.74%, primarily NT verses)

#### Reason Groups
15 categories identified:
1. KINSHIP (14.11%) - Family relationships
2. OTHER (13.53%) - Unclassified
3. ANIMATE (11.05%) - Living beings
4. TITLE-ROLE (9.75%) - Titles and roles
5. DEITY (9.25%) - References to God
6. PLACE (9.25%) - Location references
7. GENERIC-REF (7.54%) - Generic references
8. OBJECT (7.42%) - Objects and things
9. TIME (4.55%) - Temporal references
10. ABSTRACT (3.73%) - Abstract concepts
11. PROPER-NAME (3.08%) - Proper names
12. COLLECTIVE (2.43%) - Groups/collectives
13. BODY-PART (2.14%) - Body parts
14. FRAME-PARTICIPANT (1.61%) - Frame-inferable participants
15. INTERROGATIVE (0.55%) - Interrogative references

#### Translations
**Core translations** (required):
- eng-YLT (English - Young's Literal Translation)
- grc (Greek source text prefix)
- hbo (Hebrew source text prefix)
- heb-heb (Modern Hebrew)
- lat-VUC (Latin Vulgate Clementina)
- arb-NAV (Arabic Van Dyck)

**Additional translations** (linguistic diversity):
- spa-BES (Spanish)
- fra-LSG (French)
- deu-1912 (German)
- ind-AYT (Indonesian)

**MANDATORY Participant Tracking Languages** (from LANGUAGES.md research):
- swh-ONEN (Swahili) - Bantu noun class agreement system
- qub-qub (Quechua) - Topic marker -qa system
- tgl-ULB (Tagalog) - Voice/focus system with definiteness

**Total**: 13 translation versions covering diverse language families and participant tracking systems

**Note**: Japanese (jpn) and Korean (kor) were identified as MANDATORY but are not available in the eBible corpus used for enrichment.

## Directory Structure

```
analysis/
├── README.md                      # This file
├── distribution.yaml              # Value distribution summary
├── LANGUAGE-SELECTION.md          # Translation selection rationale
├── audit-data.md                  # Data quality audit report
├── enriched.secret.jsonl          # Full enriched dataset (secret)
├── tbta-extract.secret.jsonl      # Original TBTA extraction (secret)
└── data/
    ├── train.jsonl                # Training set (3,322 entries)
    ├── validate.jsonl             # Validation set - no labels (415 entries)
    ├── validate.secret.jsonl      # Validation set - with labels (415 entries)
    ├── test.jsonl                 # Test set - no labels (416 entries)
    ├── test.secret.jsonl          # Test set - with labels (416 entries)
    └── leftovers.jsonl            # Remaining TBTA data (160,755 entries)
```

## Data Fields

Each entry in the dataset contains:

### Core Fields
- `verse`: Verse reference (e.g., "GEN-001-001")
- `label`: TBTA participant tracking label
- `constituent`: The word/phrase being tracked
- `part`: Part of speech
- `text`: Simplified text with constituent highlighted (**constituent**)
- `strongs`: Space-separated list of Strong's codes for the verse
- `strongs_number`: Strong's code for the specific constituent

### Metadata (`dataset` object)
- `split`: "train", "validate", or "test"
- `section`: "OT" or "NT"
- `literary_type`: Genre classification
- `reason_group`: Logical/theological grouping
- `difficulty`: "adversarial" or "hard" for challenging cases (optional)

### Translations (`translations` object)
- Dictionary mapping translation codes to verse text
- Example: `{"eng-YLT": "In the beginning...", "grc-BRENT": "Ἐν ἀρχῇ..."}`

## Usage Notes

### Secret Files
Files marked `.secret.jsonl` contain the full data including labels and should NOT be accessed during algorithm development to prevent bias. These are:
- `enriched.secret.jsonl` - Full enriched dataset
- `tbta-extract.secret.jsonl` - Original TBTA extraction
- `validate.secret.jsonl` - Validation set with labels
- `test.secret.jsonl` - Test set with labels

### Non-Secret Files
- `train.jsonl` - Use for algorithm development and training
- `validate.jsonl` - Use for blind validation (labels removed)
- `test.jsonl` - Reserved for final evaluation (labels removed)
- `leftovers.jsonl` - Additional TBTA data not in main splits

## Quality Assurance

See `audit-data.md` for complete data quality audit report.

**Summary**: Dataset PASSED all critical requirements with 93% strongs_number coverage and complete translation enrichment across 13 languages (including 3 MANDATORY participant tracking languages).

## Next Steps

1. Proceed to Stage 2.2: Translation analysis and pattern discovery
2. Use `train.jsonl` to analyze what translators actually did
3. Develop hypothesis and create initial prompt
4. Test against `validate.jsonl` (blind validation)
5. Reserve `test.secret.jsonl` for final evaluation only

## Files Generated

| File | Purpose | Status |
|------|---------|--------|
| distribution.yaml | Value distribution summary | ✓ Complete |
| LANGUAGE-SELECTION.md | Translation selection rationale | ✓ Complete |
| audit-data.md | Data quality audit | ✓ Complete |
| data/train.jsonl | Training dataset | ✓ Complete |
| data/validate.jsonl | Validation dataset (no labels) | ✓ Complete |
| data/test.jsonl | Test dataset (no labels) | ✓ Complete |
| data/leftovers.jsonl | Additional TBTA data | ✓ Complete |

---

**Created**: 2025-11-29
**Stage**: 2.1 - Analysis Dataset Creation
**Status**: Complete ✓
