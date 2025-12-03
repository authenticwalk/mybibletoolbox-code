# TBTA Stage 2 Analysis Review - Complete

**Status**: ✅ Complete
**Started**: 2025-11-26
**Goal**: Address all [NOTE]s and [QUESTION]s, update STAGE-2-ANALYSIS.md

## Summary of Changes Made

### STAGE-2-ANALYSIS.md - Complete Rewrite

Key improvements based on your notes:

| Your Note | How Addressed |
|-----------|---------------|
| LLM baseline first (line 73) | Added **Step 2: LLM Baseline** - test before complex analysis |
| Dataset too big (line 77) | Reduced: train ≤300, validate ≤100, test ≤100 |
| Focus on edge cases (line 71) | Added **5A: Dominant Value Analysis** - when is it NOT the dominant value |
| Reconstruct verse with word (line 87) | Added `reconstructed_verse` field with **bolded target word** |
| Strongs went to ALL (line 90-91) | Added strongs_number inference in Step 3 (LLM task during dataset creation) |
| Language-version codes (line 92) | Changed to use `eng-NIV` format, not just `eng` |
| 7% edge cases (line 79) | Added **5D: Edge Case Investigation** |
| Three-tier approach (line 83) | Documented: prompt rules vs code lists vs strongs hints |
| Leftovers output (line 77) | Added `leftovers.jsonl` for entries not in any split |
| Overfitting warning (line 81-82) | Added to Anti-Patterns section |

### Investigation Answers

| Question/Note | Finding |
|---------------|---------|
| **ml_exploration.py results?** | 36.5% accuracy (vs 22% baseline). Top predictors: body parts→Dual, proper names→Singular |
| **Quadrial suspicious?** | ✅ Valid but misleading. SEMANTIC annotation (groups of 4), NOT grammatical. Recommend reclassify. |
| **Strongs grouped to ALL?** | Root cause: `--no-strongs` flag used because train.jsonl lacks strongs_number field. Fixed by adding inference in Step 3. |
| **~10% cache coverage?** | Root cause: Versification mismatch (54.7% of files). Directory `018/` contains file `*-000-*.yaml`. Documented as known issue. |
| **Env var MYBIBLE_DATA_DIR?** | Correct per config.py. Auto-detects `.data/` in project root. |

## Files Modified

- `bible-study-tools/tbta/features/.instructions-to-build-feature/STAGE-2-ANALYSIS.md` - Complete rewrite

## Files Created

- `plan/tbta-stage2-review/PLAN.md` - Investigation plan with all findings

## Remaining Work (Future Sessions)

1. **Test updated instructions** - Run Stage 2 on a new feature
2. **Script improvements** (optional):
   - Add `--cache-only` flag to main enrich script
   - Create `/src/tools/predict/split_datasets.py`
3. **Quadrial reclassification** - Decision for TBTA data team

## Original Distribution (for reference)

- Singular: 113,745 (66.2%) - dominant, focus on when NOT singular
- Plural: 55,654 (32.4%) - secondary dominant
- Dual: 1,744 (1.0%) - body parts pattern
- Trial: 496 (0.3%) - semantic (groups of 3)
- Quadrial: 185 (0.1%) - semantic (groups of 4), NOT grammatical
- Paucal: 52 (0.03%) - small quantities
