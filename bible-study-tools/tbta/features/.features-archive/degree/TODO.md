# Degree Feature - TODO

**Current Status**: 🟢 Stage 8 Complete - Algorithm v2.0 Validated
**Last Updated**: 2025-11-15

## Summary

Degree feature has completed Phases 1-8 of TBTA methodology with **71% expected accuracy** using Algorithm v2.0 (improved from 42.9% with v1.0). All training, testing, and error analysis complete.

**Key Achievement**: Discovered 4 critical universal principles:
1. Semantic over morphological analysis
2. Lexical vs syntactic distinction
3. Dual value encoding system
4. Gradability constraint

## Current Stage Status

### ✅ Stage 8: COMPLETE
- Algorithm v2.0 validated against adversarial test set
- 4 systematic errors analyzed (all algorithmic, not TBTA)
- Expected accuracy improvement: 42.9% → ~71%
- Universal principles documented in LEARNINGS.md

### Files Migrated

**Core Documentation:**
- README.md (complete feature specification)
- LEARNINGS.md (methodology thesis)

**Experiments Directory:**
- training/ - 4 training verses, 2 algorithm versions, pattern analysis
- adversarial-test/ - 7-verse validation, batch processing, V2 validation
- random-test/ - Test set with results
- COMPLETION-SUMMARY.md, VALIDATION-RESULTS.md, ERROR-ANALYSIS.md, etc.

## Next Actions

### Priority 1: Production Readiness (Stage 9)
- [ ] Run Algorithm v2.0 on full validate set (100+ verses)
- [ ] Achieve ≥95% accuracy threshold
- [ ] Document any remaining systematic errors

### Priority 2: Cross-Feature Integration
- [ ] Test degree + adjective interaction
- [ ] Validate with languages having degree-neutral systems (Motu, Fijian, Washo)
- [ ] Create language family quick-reference guides

### Priority 3: Tool Development
- [ ] Implement Algorithm v2.0 as automated tool
- [ ] Add gradability check as prerequisite
- [ ] Handle dual value encoding (standardized + literal)

## Open Questions

1. **Extremely Intensified (E)**: Does this value exist in TBTA? Not found in test verses
2. **Excessive (T)**: Rare in Biblical register; need more samples
3. **Less (L) vs least (l)**: Distinction needs validation (only found `'''least'''`)
4. **Non-existent values**: Confirmed q (equality), i (intensified comparative), s (superlative of 2) don't exist

## Learnings for Other Features

**Universal Principle 7** (NEW): Lexical vs Syntactic Distinction
- Only syntactic modification gets degree marking
- Lexical compounds (one word) = "No Degree"
- Syntactic (two words: modifier + modified) = marked degree

**Universal Principle 8** (NEW): Dual Value Encoding
- TBTA uses both standardized values AND literal quoted values
- Must handle both in validation (e.g., `'''least'''` not "l")

**Universal Principle 9** (NEW): Gradability Constraint
- Prerequisites check before any degree analysis
- Non-gradable words (justified, dead, perfect) always "No Degree"

## References

- Complete methodology: `/experiments/training/ALGORITHM-v2.md`
- Error analysis: `/experiments/ERROR-ANALYSIS.md` (6-step exhaustive debugging)
- Cross-feature learnings: See main `/features/learnings/` for principles 7-9

## Migration Notes

Migrated from: `/plan/tbta-rebuild-with-llm/features/degree/`
Migration date: 2025-11-15
All experimental work preserved in `/experiments/` subdirectory
