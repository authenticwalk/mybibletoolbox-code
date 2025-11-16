# Number System Feature - Handoff Document

**Feature**: number-system
**Date**: 2025-11-16
**Status**: Stages 1-3 COMPLETE | Ready for Stage 4
**Next Agent**: Test Set Generation Subagent (blind testing required)

---

## Quick Summary

✅ **COMPLETED**:
- Stage 1: TBTA Tier 0 encoding verified (Position 2 = Number)
- Stage 2: 501+ languages documented (5 families)
- Stage 3: 2024 scholarly research + translation sources identified

**CRITICAL DISCOVERY**: True trial languages = <10 (not 172). Most are paucal.

⏸️ **NEXT**: Stage 4 test set generation with subagent (blind testing)

---

## What the Next Agent Needs to Know

### 1. Tier 0 Encoding (CRITICAL)

**TBTA Position 2** of noun/pronoun codes = Number (S/D/T/p/P)

This is explicit source data. Algorithm Rule 1: **Always check Position 2 first**.

### 2. Trial vs. Paucal Distinction (CRITICAL CORRECTION)

- **Trial** (T): Exactly 3 entities - VERY RARE (<10 languages, mostly facultative)
- **Paucal** (p): Minimum of 3 (range 3-5 to 3-15) - ~50-70 languages
- **Fijian** uses PAUCAL, not trial (mission brief was incorrect)

### 3. Translation Sources for Stage 4

**5 Languages to Use**:
1. **Fijian** (paucal) - Nai Vola Tabu Vakavakadewa Vou
2. **Hawaiian** (dual) - Ka Baibala Hemolele (2018)
3. **Slovenian** (dual) - Dalmatinova Biblija (1583)
4. **Tok Pisin** (trial) - Nupela Testamen
5. **Samoan** (dual) - Dual pronouns

### 4. Common Error Patterns to Test

Include adversarial cases for these 6 error patterns:

1. Missing TBTA semantic expansions (~15%)
2. Paired body parts context override (~10%) - **Matthew 5:30 "RIGHT hand"**
3. Trinity trial subtle contexts (~5%, THEOLOGICALLY CRITICAL)
4. Generic vs specific plurals (~20%)
5. Hebrew morphological signals (~8%)
6. Paucal vs trial confusion (~10%, NEW)

### 5. Test Set Requirements

- **Sample size**: 100+ verses per value (S/D/T/p/P)
- **Split**: train (40%), test (30%), validate (30%)
- **Balance**: OT/NT, genre, difficulty
- **Adversarial**: Paired body parts, Trinity contexts, generic plurals
- **Format**: Answer sheets (TBTA) + question sheets (translations)

### 6. Trinity Contexts (100% Accuracy Required)

**MUST INCLUDE**:
- Genesis 1:26 "Let us make..." (paucal in Fijian, trial in Tok Pisin)
- Baptismal formulas (Matthew 28:19)
- Doxologies
- Any Father + Son + Spirit together

---

## Stage 4 Execution Plan

### Step 1: Extract TBTA Data (Subagent)

```bash
python src/ingest-data/tbta/extract_feature.py \
  --field "Number" \
  --position 2 \
  --max-per-value 2000 \
  --output features/number-system/experiments/raw_tbta_data.yaml
```

### Step 2: Sample Selection (Subagent)

**Stratification**:
- Testament: Proportional OT/NT
- Genre: Narrative, poetry, prophecy, epistle
- Difficulty: Typical + adversarial
- Book distribution: Avoid concentration

**Adversarial Priority**:
- Matthew 5:30 (paired body part, singular)
- Genesis 1:26 (Trinity/paucal)
- Matthew 18:20 "two or three" (paucal)
- Luke 24:13 "two of them" (dual)

### Step 3: Generate Question Sheets (Subagent)

For each verse in train/test/validate:
- Lookup translation texts from .data/commentary/
- Extract Fijian, Hawaiian, Slovenian, Tok Pisin, Samoan
- Create question YAML (translations only, NO TBTA values)

### Step 4: Output Files

**Generate**:
- `experiments/train.yaml` (answer sheet)
- `experiments/train_questions.yaml` (question sheet)
- `experiments/test.yaml`, `test_questions.yaml`
- `experiments/validate.yaml`, `validate_questions.yaml`
- `experiments/TRANSLATION-DATABASE.md`

---

## Stage 5 Hierarchical Algorithm

**Priority 1 - Tier 0 Check**:
```
IF TBTA data exists → RETURN Position 2 (S/D/T/p/P)
```

**Priority 2 - Translation Consensus**:
```
IF 80%+ translations agree → RETURN consensus value
```

**Priority 3 - Theological Level**:
```
IF Trinity context → Apply theological analysis (95%+ accuracy)
```

**Priority 4 - Contextual**:
```
Check Hebrew morphology, context overrides, generic vs specific
```

---

## Production Readiness Criteria

**Accuracy Targets**:
- ✅ Overall: ≥95% on validate set
- ✅ Stated values (n≥100): 100% accuracy
- ✅ Trinity contexts: 100% accuracy (non-negotiable)

**Validation**:
- ✅ Tier 0 check as Rule 1
- ✅ Translation consensus ≥90%
- ✅ 4 peer reviews passed
- ✅ TRANSLATOR-IMPACT.md created

---

## Key Documents

**Feature README**:
- `/workspace/bible-study-tools/tbta/features/number-system/README.md`

**Session Planning**:
- `/workspace/plan/tbta-number-system-2025-11-16/README.md`
- `/workspace/plan/tbta-number-system-2025-11-16/PRODUCTION-READINESS.md`
- `/workspace/plan/tbta-number-system-2025-11-16/SUMMARY.md`

**Archived Work**:
- `/workspace/bible-study-tools/tbta/features/features-archive/number-system/`

---

## Git Status

**Branch**: `feat-improve-tools-tbta-and-strongs`
**Latest Commits**:
- `db129b9`: Final session summary
- `3c9a88d`: Production readiness assessment
- `ba5a203`: Session plan
- `7986011`: README.md (Stages 1-3)

**Ready to Push**: Yes (4 commits local)

---

## Timeline

**Completed**: 1 day (Stages 1-3)
**Remaining**: 2-3 weeks (Stages 4-6)
- Stage 4: 3-5 days (test generation)
- Stage 5: 5-7 days (algorithm)
- Stage 6: 3-5 days (validation)

---

## Risks & Mitigations

**HIGH RISKS**:
1. **Blind testing required** (Stage 4) → Use subagent, never see TBTA answers
2. **Trinity 100% accuracy** (Stage 5-6) → Extra validation, theological review

**MEDIUM RISKS**:
1. **Translation data availability** → Fallback to 3 languages minimum
2. **TBTA coverage 29%** → Heavy reliance on translation consensus

---

## Contact & Coordination

**Session ID**: swarm-tbta-attempt2
**Memory Keys**: `swarm/number-system/stage1-3-complete`
**Hooks**: pre-task, post-edit, notify, post-task, session-end

---

**Handoff Date**: 2025-11-16
**From**: TBTA Number System Development Agent
**To**: Stage 4 Test Set Generation Subagent
**Status**: READY FOR STAGE 4
