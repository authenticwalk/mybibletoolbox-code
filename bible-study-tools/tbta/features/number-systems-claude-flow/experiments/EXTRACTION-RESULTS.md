# TBTA Number Systems Feature - Extraction Results

**Stage**: 4A (Data Extraction - Blind Testing Protocol)
**Date**: 2025-11-17T23:34:10Z
**Researcher**: Claude Sonnet 4.5 (Research Agent)
**TBTA Source**: AllTheWord/tbta_db_export (commit: 07797f2)

---

## Executive Summary

Successfully extracted TBTA Number field data from 11,649 verse files without viewing answer sheets (maintaining data hygiene for blind testing). Discovered 6 distinct number values with significant variation in frequency.

**Key Findings**:
- ✅ All expected values found (Singular, Dual, Trial, Paucal, Plural, Quadrial)
- ✅ Strong dataset for Dual (1,744 verses) and Trial (496 verses)
- ⚠️ Paucal is low frequency (52 verses total) - may need all verses + oversampling
- ✅ Quadrial present but rare (185 verses) - surprising discovery!
- ✅ Good OT/NT distribution for minority values

---

## Extraction Method

### Tool Used
**Script**: `src/ingest-data/tbta/extract_feature.py`

**Command**:
```bash
python src/ingest-data/tbta/extract_feature.py \
  --field "Number" \
  --max-per-value 2000 \
  --output bible-study-tools/tbta/features/number-systems-claude-flow/experiments/raw_tbta_data.yaml
```

### Data Source
- **Repository**: https://github.com/AllTheWord/tbta_db_export
- **Commit**: 07797f2 (shallow clone, latest as of 2025-11-17)
- **Files Processed**: 11,649 TBTA verse files (entire NT + portions of OT)
- **Format**: JSON clause trees with grammatical annotations

### Extraction Strategy
1. Clone fresh TBTA data from GitHub (ensures up-to-date annotations)
2. Recursively search clause trees for "Number" field
3. Filter out nullish values ("Not Applicable", "Unspecified", ".")
4. Track counts per value, OT/NT distribution, book distribution
5. Apply LRU cache (2000 max per value) to limit Singular/Plural datasets
6. Output to YAML with metadata

---

## Verse Counts per Value

| Number Value | Total Verses | Cached (Output) | OT Verses | NT Verses | OT % | NT % |
|--------------|--------------|-----------------|-----------|-----------|------|------|
| **Singular** | 113,745      | 2,000 ⚠️        | 78,708    | 35,037    | 69%  | 31%  |
| **Plural**   | 55,654       | 2,000 ⚠️        | 34,651    | 21,003    | 62%  | 38%  |
| **Dual**     | 1,744        | 1,744 ✅        | 1,269     | 475       | 73%  | 27%  |
| **Trial**    | 496          | 496 ✅          | 394       | 102       | 79%  | 21%  |
| **Quadrial** | 185          | 185 ✅          | 176       | 9         | 95%  | 5%   |
| **Paucal**   | 52           | 52 ✅           | 23        | 29        | 44%  | 56%  |

### Notes on Truncation
- **Singular & Plural**: LRU-capped at 2,000 verses each (showing first 2,000 chronologically)
  - These are extremely common (every noun, pronoun, verb subject)
  - Sampling strategy will select diverse representatives from full dataset
- **Dual, Trial, Quadrial, Paucal**: All verses included (no truncation)

---

## Distribution Analysis

### Testament Distribution (Overall)
- **OT-heavy values**: Quadrial (95% OT), Trial (79% OT), Dual (73% OT)
- **NT-heavy values**: Paucal (56% NT)
- **Balanced**: Singular (69% OT), Plural (62% OT)

**Interpretation**:
- Quadrial/Trial/Dual skew OT suggests Hebrew morphology (dual number in Hebrew nouns)
- Paucal skew NT may reflect Greek article usage or specific NT narrative contexts
- Aligns with expected ~77% OT / 23% NT biblical proportions for Dual/Trial

### Book Distribution (Top Contributors per Value)

#### Dual (1,744 verses total)
| Book | Count | % of Total | Testament |
|------|-------|------------|-----------|
| GEN  | 400   | 22.9%      | OT        |
| LUK  | 150   | 8.6%       | NT        |
| 1SA  | 142   | 8.1%       | OT        |
| MAT  | 140   | 8.0%       | NT        |
| JOS  | 127   | 7.3%       | OT        |
| MRK  | 124   | 7.1%       | NT        |
| EXO  | 119   | 6.8%       | OT        |
| JDG  | 113   | 6.5%       | OT        |

**Analysis**:
- Genesis dominates (22.9%) - many paired narratives (Adam/Eve, Cain/Abel, Jacob/Esau)
- Gospels strong (LUK 8.6%, MAT 8.0%, MRK 7.1%) - disciples sent "two by two"
- Good diversity: 25 different books represented

#### Trial (496 verses total)
| Book | Count | % of Total | Testament |
|------|-------|------------|-----------|
| GEN  | 107   | 21.6%      | OT        |
| EXO  | 63    | 12.7%      | OT        |
| JOS  | 27    | 5.4%       | OT        |
| 1SA  | 26    | 5.2%       | OT        |
| NUM  | 25    | 5.0%       | OT        |
| DEU  | 24    | 4.8%       | OT        |
| MAT  | 23    | 4.6%       | NT        |
| LUK  | 20    | 4.0%       | NT        |

**Analysis**:
- Genesis 21.6% (likely Gen 1:26 Trinity + narrative triples)
- Torah heavy (GEN, EXO, NUM, DEU = 44.2%) - expected for Hebrew morphology
- NT representation modest (21% total) but present in key theological texts

#### Paucal (52 verses total - CRITICAL LOW FREQUENCY)
| Book | Count | % of Total | Testament |
|------|-------|------------|-----------|
| LUK  | 8     | 15.4%      | NT        |
| JHN  | 7     | 13.5%      | NT        |
| MAT  | 6     | 11.5%      | NT        |
| GEN  | 6     | 11.5%      | OT        |
| ACT  | 4     | 7.7%       | NT        |
| ROM  | 4     | 7.7%       | NT        |

**Analysis**:
- ⚠️ **CRITICAL**: Only 52 verses total across entire Bible
- NT-heavy (56%) - unexpected, may reflect Greek contexts for small groups
- Concentration in Gospels (LUK+JHN+MAT = 40.4%) - small disciple groups?
- **Sampling Impact**: Will need ALL 52 verses + careful stratification

#### Quadrial (185 verses total - UNEXPECTED DISCOVERY)
| Book | Count | % of Total | Testament |
|------|-------|------------|-----------|
| GEN  | 44    | 23.8%      | OT        |
| EXO  | 26    | 14.1%      | OT        |
| NUM  | 19    | 10.3%      | OT        |
| JOS  | 15    | 8.1%       | OT        |
| 1SA  | 10    | 5.4%       | OT        |
| DEU  | 9     | 4.9%       | OT        |

**Analysis**:
- ⚠️ **SURPRISE**: 185 Quadrial verses (TEST-SET-PLAN.md predicted 0-5)
- 95% OT (176/185) - strongly Hebrew-specific
- Genesis 23.8%, Exodus 14.1% - Pentateuch = 53.0%
- **Action Required**: Investigate what triggers Quadrial annotation
  - Possible: Four-element lists (cardinal directions, Gospels, cherubim faces?)
  - May be linguistically contested (see ARBITRARITY-CLASSIFICATION.md)

---

## Data Quality Observations

### Strengths
1. ✅ **Dual & Trial**: Strong datasets (1,744 and 496 verses respectively)
   - Exceeds Stage 4 minimum requirements (≥100 per value)
   - Sufficient for robust train/test/validate splits
   - Good book diversity (25+ books for Dual, 20+ for Trial)

2. ✅ **Quadrial Discovery**: Unexpected 185 verses
   - Provides opportunity for rare feature validation
   - May reveal interesting TBTA annotation patterns

3. ✅ **Testament Balance**: Most values align with biblical proportions
   - Dual: 73% OT (target ~77%)
   - Trial: 79% OT (target ~77%)

### Challenges
1. ⚠️ **Paucal Scarcity**: Only 52 verses total
   - **Impact**: Cannot meet 100-verse minimum from TEST-SET-PLAN.md
   - **Mitigation Options**:
     - Use ALL 52 verses with note in validation
     - Oversample with replacement for statistical power
     - Acknowledge limitation in Stage 6 results
   - **Distribution**: Must carefully balance 52 across train/test/validate
     - Suggested: 21 train / 16 test / 15 validate (40%/30%/30% rounded)

2. ⚠️ **Singular/Plural Truncation**: LRU capped at 2,000 each
   - **Impact**: Cannot see full 113k Singular / 55k Plural datasets
   - **Mitigation**: Stratified sampling from truncated dataset still valid
     - 2,000 verses provides ample diversity for representative sampling
     - Can re-extract specific verses if needed for adversarial selection

3. ⚠️ **Quadrial Investigation Needed**: Status unclear
   - **Action**: Subagent should spot-check Quadrial verses
     - Verify linguistic basis (four-element lists? Hebrew dual pairs?)
     - Check if controversial (may be arbitrarily classified)
     - Decide if include in test set or exclude as contested

---

## Next Steps for Subagent (Stage 4B)

### Immediate Actions
1. **Investigate Quadrial**:
   - Read sample verses (GEN.001.020, EXO.014.007, etc.)
   - Determine linguistic basis
   - Assess if stable enough for test set inclusion

2. **Stratified Sampling**:
   - **Dual**: Sample 120 verses (from 1,744 available)
   - **Trial**: Sample 100 verses (from 496 available)
   - **Paucal**: Use ALL 52 verses (no sampling)
   - **Plural**: Sample 150 verses (from 2,000 cached)
   - **Singular**: Sample 150 verses (from 2,000 cached)
   - **Quadrial**: Sample 10-20 verses (IF linguistically valid)

3. **Classification Dimensions**:
   For each verse, annotate:
   - Testament (OT/NT) - already tracked
   - Genre (Narrative/Poetry/Prophecy/Epistle/Wisdom/Law)
   - Difficulty (Typical/Adversarial)
   - Arbitrarity (Arbitrary/Non-Arbitrary with reason group)
   - Book diversity (track per TEST-SET-PLAN.md ≥20 books target)

4. **Non-Arbitrary Verse Selection**:
   Ensure mandatory verses included:
   - **Trinity**: GEN.001.026, GEN.001.027, GEN.011.007 (Trial)
   - **Apostolic Authority**: Acts 15:25, 15:28 (Plural)
   - **Paired Disciples**: LUK.024.013, ACT.013.002, MRK.006.007 (Dual)
   - **Small Groups**: MAT.018.020, MAT.026.026 (Paucal - if available)

5. **Translation Availability Check**:
   - Use /quote-bible skill to verify selected languages available
   - Adjust language selection if needed (per TEST-SET-PLAN.md §5)

6. **Generate Outputs**:
   - `train.yaml` (answer sheet with TBTA values)
   - `train_questions.yaml` (translations only, NO TBTA values)
   - `test.yaml`, `test_questions.yaml`
   - `validate.yaml`, `validate_questions.yaml`

---

## Success Metrics (Stage 4 Validation)

### Achieved ✅
- [x] Extraction script executed successfully
- [x] All 6 number values discovered
- [x] Testament distribution tracked
- [x] Book distribution documented
- [x] Data output in YAML format
- [x] Blind testing protocol maintained (no answer viewing)

### Pending (Subagent Stage 4B)
- [ ] Sample size ≥100 per value (EXCEPT Paucal: use all 52)
- [ ] Testament balance 77% OT / 23% NT (±5%)
- [ ] Genre diversity: No single genre >40%
- [ ] Book diversity: ≥20 different books
- [ ] Adversarial cases: 30% of test set
- [ ] Non-arbitrary verses: All 5 reason groups represented (≥2 each)
- [ ] Translation availability: 100% of selected languages verified

---

## File Outputs

### Created
- ✅ `raw_tbta_data.yaml` (6,655 lines, 6,477 total verses cached)

### Pending (Subagent)
- [ ] `train.yaml` (answer sheet, ~250 verses)
- [ ] `train_questions.yaml` (question sheet, translations only)
- [ ] `test.yaml` (answer sheet, ~190 verses)
- [ ] `test_questions.yaml` (question sheet)
- [ ] `validate.yaml` (answer sheet, ~190 verses)
- [ ] `validate_questions.yaml` (question sheet)
- [ ] `TRANSLATION-DATABASE.md` (language selection documentation)

---

## Issues Encountered

### Issue 1: PyYAML Not Installed
**Problem**: Script requires PyYAML but not in environment
**Resolution**: `pip install pyyaml` (successful)
**Impact**: None (resolved immediately)

### Issue 2: Paucal Low Frequency
**Problem**: Only 52 verses (expected ≥100 per TEST-SET-PLAN.md)
**Resolution**: Document limitation, use all 52 + oversampling if needed
**Impact**: May affect statistical power claims in Stage 6

### Issue 3: Quadrial Unexpected Presence
**Problem**: 185 verses found (plan predicted 0-5 as "highly contested")
**Resolution**: Investigation required by subagent
**Impact**: Opportunity or noise? Depends on linguistic validity

---

## Coordination Status

**Task ID**: task-1763422403326-bnsca3j3t
**Status**: Stage 4A Complete
**Next Agent**: Subagent (Stage 4B Stratified Sampling & Classification)
**Hand-off**: raw_tbta_data.yaml ready for sampling

---

## Appendix: Sample Data Structure

```yaml
feature: number
extracted: '2025-11-17T23:34:10.977068Z'
tbta_commit: 07797f2
max_per_value: 2000
value:
- specific_value: Dual
  total_verses: 1744
  distribution:
    OT: 1269
    NT: 475
    Books:
      GEN: 400
      EXO: 119
      JOS: 127
      # ... (25 books total)
  verses:
  - GEN.001.006
  - GEN.001.016
  - GEN.001.028
  # ... (1,744 total)
```

**Key Fields**:
- `specific_value`: TBTA annotation (Singular, Dual, Trial, Paucal, Plural, Quadrial)
- `total_verses`: Full count before LRU truncation
- `distribution.OT/NT`: Testament counts
- `distribution.Books`: Per-book counts
- `verses`: List of verse references (USFM format: BOOK.chapter.verse)

---

**Status**: Extraction Complete ✅
**Next Action**: Spawn subagent for Stage 4B (Stratified Sampling)
