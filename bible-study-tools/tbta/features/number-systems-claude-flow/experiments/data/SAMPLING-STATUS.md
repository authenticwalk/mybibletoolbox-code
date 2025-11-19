# Sampling Agent Status - Stage 4B

**Agent**: Analyst (Number Systems Hive Mind)
**Task**: Stratified sampling from TBTA data
**Date**: 2025-11-17
**Status**: WAITING FOR EXTRACTION

---

## Current State

**Waiting For**: EXTRACTION-RESULTS.md from researcher agent

**Ready When**:
- researcher completes TBTA data extraction
- raw_tbta_data.yaml is available
- Can begin stratified sampling

---

## Sampling Strategy (Pre-Planned)

### Target Distribution (640 total verses)

| Number Value | Train (40%) | Test (30%) | Validate (30%) | Total | Min Required |
|--------------|-------------|------------|----------------|-------|--------------|
| **Singular** | 60 | 45 | 45 | 150 | 100+ ✓ |
| **Dual** | 48 | 36 | 36 | 120 | 100+ ✓ |
| **Trial** | 40 | 30 | 30 | 100 | 100 ✓ |
| **Paucal** | 40 | 30 | 30 | 100 | 100 ✓ |
| **Plural** | 60 | 45 | 45 | 150 | 100+ ✓ |
| **Quadrial** | 2 | 4 | 4 | 10 | All available |
| **TOTAL** | 250 | 190 | 190 | 630 | |

### Stratification Dimensions

1. **Testament Balance**: 77% OT / 23% NT (±5%)
2. **Genre Distribution**: No single genre >40%
   - Narrative, Poetry, Prophecy, Epistle, Wisdom, Law
3. **Book Diversity**: ≥20 different books, no book >15%
4. **Difficulty Mix**:
   - Typical: 70%
   - Adversarial: 30% (concentrated in test set)

### Non-Arbitrary Verses (MANDATORY INCLUSION)

From ARBITRARITY-CLASSIFICATION.md:

**Trinity References (≥5 verses)**:
- GEN.001.026 (High stakes)
- GEN.003.022
- GEN.011.007
- ISA.006.008
- MAT.028.019 (Baptismal formula)
- 2CO.013.014 (Benediction)

**Dual Contexts (≥10 verses)**:
- LUK.024.013 (Two to Emmaus)
- ACT.013.002 (Barnabas and Saul)
- MAR.006.007 (Sent two by two)
- LUK.010.001 (Sent two by two)
- Additional paired disciple contexts (6+ more)

**Small Group Theology (≥2 verses)**:
- MAT.018.020 (Two or three gather)
- Small house church contexts

**Total Non-Arbitrary Target**: ~40+ verses (6% of dataset)

### Translation Languages Selected (from TEST-SET-PLAN.md)

**Trial-Marking** (for Genesis 1:26 validation):
1. Fijian (fij) - HIGH priority
2. Tok Pisin (tpi) - HIGH priority
3. Hawaiian (haw) - MEDIUM priority

**Dual-Marking** (for Luke 24:13, Mark 6:7):
4. Samoan (smo) - HIGH priority
5. Slovenian (slv) - MEDIUM priority

**Paucal-Marking** (for Matthew 18:20):
6. Warlpiri (wbp) - HIGH if available
7. Bislama (bis) - MEDIUM backup

**Control (Non-Marking)**:
8. Indonesian (ind) - HIGH priority
9. Spanish (spa) - MEDIUM priority

---

## Sampling Algorithm (Ready to Execute)

### Step 1: Load TBTA Data
```bash
# When available:
# - Load raw_tbta_data.yaml
# - Count verses per value
# - Identify available values (Singular, Dual, Trial, Paucal, Plural, Quadrial)
```

### Step 2: Classify Each Verse
For each verse, determine:
- **Testament**: OT or NT (from book code)
- **Genre**: Narrative/Poetry/Prophecy/Epistle/Wisdom/Law
  - Narrative: GEN, EXO, JOS, JDG, RUT, 1SA, 2SA, 1KI, 2KI, 1CH, 2CH, EZR, NEH, EST, MAT, MAR, LUK, JHN, ACT
  - Poetry: PSA, SNG, LAM
  - Prophecy: ISA, JER, EZE, DAN, HOS, JOL, AMO, OBA, JON, MIC, NAM, HAB, ZEP, HAG, ZEC, MAL, REV
  - Epistle: ROM, 1CO, 2CO, GAL, EPH, PHP, COL, 1TH, 2TH, 1TI, 2TI, TIT, PHM, HEB, JAS, 1PE, 2PE, 1JN, 2JN, 3JN, JUD
  - Wisdom: JOB, PRO, ECC
  - Law: LEV, NUM, DEU
- **Difficulty**: Typical or Adversarial (see criteria below)
- **Arbitrarity**: Check against ARBITRARITY-CLASSIFICATION.md

### Step 3: Adversarial Selection Criteria

**Adversarial if**:
- **Category 1**: Ambiguous count ("a few", "some", collective singular)
- **Category 2**: Genre boundaries (quoted speech in narrative, vision contexts)
- **Category 3**: Theological edge cases (Trinity, small group theology)
- **Category 4**: Translation-divergent (check if trial languages split)
- **Category 5**: Rare discourse (vocative, imperative to groups)

**Typical if**: Clear, unambiguous number context

### Step 4: Stratified Sampling

**For each value** (Singular, Dual, Trial, Paucal, Plural):

1. **Mandatory Non-Arbitrary Inclusion**:
   - Add ALL non-arbitrary verses for this value
   - Mark with `arbitrarity: non-arbitrary` and `reason_group`

2. **Testament Proportional Sampling**:
   - Target: 77% OT, 23% NT
   - Sample from remaining verses after non-arbitrary added

3. **Genre Balancing**:
   - No genre >40% of value's sample
   - Prioritize diverse genres

4. **Book Diversity**:
   - ≥20 different books in total dataset
   - No book >15% of total

5. **Difficulty Balancing**:
   - Typical: 70% overall
   - Adversarial: 30% overall (concentrated in test set 50%)

### Step 5: Split into Train/Test/Validate

**Split Ratios**: 40% / 30% / 30%

**Non-Arbitrary Distribution**:
- Train: 40% of non-arbitrary verses
- Test: 30% of non-arbitrary verses
- Validate: 30% of non-arbitrary verses

**Adversarial Distribution** (weighted toward test):
- Train: 20% adversarial (lower for clean training)
- Test: 50% adversarial (stress test algorithm)
- Validate: 30% adversarial (final blind test)

### Step 6: Generate Output Files

**Answer Sheets** (with TBTA values - for scoring only):
- `train.yaml` (250 verses)
- `test.yaml` (190 verses)
- `validate.yaml` (190 verses)

**Question Sheets** (without TBTA values - for prediction):
- `train_questions.yaml`
- `test_questions.yaml`
- `validate_questions.yaml`

---

## Deliverables Checklist

- [ ] `train.yaml` - Answer sheet with TBTA values
- [ ] `train_questions.yaml` - Question sheet WITHOUT values
- [ ] `test.yaml` - Answer sheet
- [ ] `test_questions.yaml` - Question sheet
- [ ] `validate.yaml` - Answer sheet
- [ ] `validate_questions.yaml` - Question sheet
- [ ] `SAMPLING-REPORT.md` - Statistics and methodology

---

## Coordination Protocol

```bash
# Pre-task (DONE)
npx claude-flow@alpha hooks pre-task --description "Stage 4B: Stratified sampling"

# During sampling
npx claude-flow@alpha hooks post-edit --file "{file}" --memory-key "swarm/analyst/sampling"

# Post-task
npx claude-flow@alpha hooks post-task --task-id "number-systems-stage4b-sample"
npx claude-flow@alpha hooks notify --message "Sampling complete: {stats}"
```

---

## Next Actions

**Immediate**: WAIT for EXTRACTION-RESULTS.md
**Then**: Execute sampling algorithm
**Finally**: Return ONLY question sheet paths (NOT answer sheets)

**Status**: READY AND WAITING
