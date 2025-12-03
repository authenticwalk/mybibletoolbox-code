# Step 1D: Data Audit Report

## Audit Date
2025-11-29

## Dataset Overview

- **Source**: `enriched.jsonl`
- **Total entries**: 240
- **Entries per label**: 30 (balanced)
- **Labels**: 8 (Addressee, Beneficiary, Destination, Instrument, Most Agent-like, Most Patient-like, Source, State)

## Audit Checklist

### ✅ Core Translations Present

Checked sample entries with translations (30 entries, 12.5% coverage):

- ✅ **eng-YLT**: Present in available entries
- ✅ **grc**: Present for NT verses (where available)
- ✅ **hbo**: Present for OT verses (where available)
- ✅ **heb-heb**: Present (where available)
- ✅ **lat-VUC**: Present (where available)
- ✅ **arb-NAV**: Present (where available)

**NOTE**: Translation coverage is 12.5% because most books/chapters are not in sparse checkout. To get full coverage:
```bash
cd /workspace/.data
git sparse-checkout add commentary
```

### ⚠️ Additional Languages (Partial)

- ⚠️ **rus**: Available in some entries
- ⚠️ **deu-1912**: Available in some entries
- ⚠️ **jpn**: Available in some entries (limited coverage)
- ⚠️ **ind-AYT**: Available in some entries
- ⚠️ **fra-LSG**: Available in some entries
- ⚠️ **spa-BES**: Available in some entries
- ⚠️ **tur**: Available in some entries (limited coverage)

### ❌ Strong's Numbers (Missing)

- ❌ **strongs_number**: NOT present in any entry
- ❌ **strongs**: NOT present (list of codes for verse)

**Reason**: The `strongs` and `strongs_number` fields were supposed to be added in Step 1B manual enrichment, which was not completed due to:
1. Missing macula data files (need to run macula processor)
2. Manual review required per instructions (cannot be scripted)

### ❌ Reason Groups (Missing)

- ❌ **reason_group**: NOT present in any entry

**Reason**: Manual assignment required per Step 1B instructions. Each entry needs human judgment to assign one of:
- Theological groups: TRINITY, CHRISTOLOGY-DUAL-NATURE, ATONEMENT, PRAYER-MEDIATION, SALVATION-SOVEREIGNTY
- Linguistic groups: PROPER-NAME, PRONOUN, COLLECTIVE, ABSTRACT, BODY-PART
- Verb frame groups: MOTION-VERB, TRANSFER-VERB, COMMUNICATION-VERB, MENTAL-VERB, CREATION-VERB
- Contextual groups: NARRATIVE-CLARITY, STYLISTIC, PASSIVE-VOICE, AMBIGUOUS-PREPOSITION

### ✅ Dataset Split Assignment

- ✅ All entries have `dataset.split` field
- ✅ Values: "train", "validate", "test"
- ✅ Distribution appears balanced across splits

### ✅ Testament Section

- ✅ All entries have `dataset.section` field
- ✅ Values: "OT" or "NT"

### ✅ Literary Type

- ✅ All entries have `dataset.literary_type` field
- ✅ Values appear to be assigned (though most are "other")

### ⚠️ Difficulty Marking (Optional)

- ⬜ **difficulty**: NOT checked (optional field)
- Expected values: blank (normal), "hard", "adversarial"
- Not critical for this stage

## Critical Issues Found

### Issue 1: Missing Strong's Data (BLOCKING)

**Severity**: HIGH
**Impact**: Cannot identify which specific word in the verse corresponds to the constituent
**Resolution Required**:
1. Generate macula data files: `python src/ingest_data/macula/macula_processor.py --all`
2. Manually add `strongs_number` to each entry based on macula word data
3. Add `strongs` field with full list of codes from verse

### Issue 2: Missing Reason Groups (BLOCKING)

**Severity**: HIGH
**Impact**: No logical grouping for analysis, cannot identify theological vs arbitrary cases
**Resolution Required**:
1. Manually review each of 240 entries
2. Assign `reason_group` from REASON-GROUPS.md taxonomy
3. Estimated time: 2-5 min per entry = 8-20 hours total

### Issue 3: Low Translation Coverage (NON-BLOCKING)

**Severity**: MEDIUM
**Impact**: Only 12.5% of entries have translation data
**Resolution**: Expand sparse checkout to include all books in dataset
**Command**:
```bash
cd /workspace/.data
git sparse-checkout add commentary
```

## Recommendations

### For Completing Stage 2.1

**Option A: Complete Full Dataset (Recommended for Production)**
1. Expand `.data` sparse checkout to all commentary
2. Generate macula data for all verses
3. Complete manual enrichment of all 240 entries with strongs_number and reason_group
4. Proceed to Step 1E (split datasets)

**Option B: Reduced Dataset (Pragmatic for Development)**
1. Filter enriched.jsonl to only entries WITH translations (30 entries)
2. Manually enrich those 30 entries with strongs_number and reason_group
3. Proceed with smaller but complete dataset
4. Expand later when ready for production

**Option C: Defer Manual Work (Current State)**
1. Document current state as "partial completion"
2. Proceed to Step 1E with incomplete data (will fail validation)
3. Return to complete Steps 1B-1C in future session

## Current Recommendation

Given time constraints and the instructions' emphasis on manual quality:

**Proceed with Option B (Reduced Dataset)**:
- 30 entries with translations is sufficient for initial analysis
- Quality > quantity for training data
- Can expand later once methodology proven
- Allows completion of Stage 2.1 workflow demonstration

## Next Steps

1. Filter to entries with translations
2. Manual enrichment session for strongs_number + reason_group (30 entries × 3 min = 1.5 hours)
3. Proceed to Step 1E (split)
4. Complete Stage 2.1

## Audit Summary

| Criterion | Status | Notes |
|-----------|--------|-------|
| Core translations present | ⚠️ PARTIAL | 12.5% coverage (30/240 entries) |
| 3+ additional languages | ⚠️ PARTIAL | Present where translations exist |
| strongs_number field | ❌ MISSING | Requires manual enrichment |
| strongs list field | ❌ MISSING | Requires manual enrichment |
| reason_group field | ❌ MISSING | Requires manual enrichment |
| dataset split assigned | ✅ PASS | All entries have split |
| section (OT/NT) assigned | ✅ PASS | All entries have section |

**Overall Status**: ⚠️ PARTIAL - Requires completion of Step 1B manual enrichment before proceeding to Step 1E
