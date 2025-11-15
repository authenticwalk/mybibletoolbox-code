# Polarity Feature - TODO

**Current Status**: 🟡 Training Set Complete, Algorithm Development Needed
**Last Updated**: 2025-11-15

## Summary

Polarity determines whether a constituent is affirmed or negated. **CRITICAL** for ~50% of languages with specialized negative systems including:
- Negative concord languages (Spanish, Russian, Greek, Turkish)
- Genitive of negation (Russian, Finnish)
- Special negative existentials (Hebrew אֵין, Russian нет, Turkish yok)

## Current Stage Status

### ✅ Complete
- README.md (complete feature specification)
- LEARNINGS.md (key insights on NC systems, NPIs, existentials)
- SUMMARY.md (overview and language family patterns)
- experiments/training/ - Training set prepared
- experiments/experiment-001.md - Experimental design

### ⏳ Next Steps Required

**Priority 1: Algorithm Development**
- [ ] Create 5-level decision tree (similar to degree feature)
- [ ] Handle negative concord detection
- [ ] Implement NPI (Negative Polarity Item) selection
- [ ] Add genitive/partitive case change rules
- [ ] Special existential construction detection

**Priority 2: Test Set Execution**
- [ ] Sample 100+ verses (50% negative constructions)
- [ ] Include NC languages (Spanish, Russian, Greek)
- [ ] Test existential negations (Hebrew אֵין patterns)
- [ ] Validate NPI licensing (English "any" vs "some")

**Priority 3: Language-Specific Validation**
- [ ] Russian: Verify genitive of negation
- [ ] Spanish: Check negative concord compliance
- [ ] Hebrew: Validate אֵין vs לֹא usage
- [ ] English: Test NPI selection accuracy

## Files Migrated

**Core Documentation:**
- README.md (6-level hierarchical template)
- LEARNINGS.md (core insights on polarity systems)
- SUMMARY.md (quick reference)

**Experiments:**
- experiments/training/ - Training set for algorithm development
- experiments/experiment-001.md - Initial experiment design

## Key Findings

**Three Major Language Types**:

1. **Negative Concord (NC)** Languages (strict):
   - Spanish, Russian, Turkish, Polish, many Romance
   - Multiple negatives strengthen (not cancel)
   - Must add negative elements not present in English

2. **NPI Languages** (Non-NC):
   - English, German, Dutch, Japanese
   - Special items restricted to negative contexts
   - Must select correct polarity-sensitive items

3. **Mixed/Special Systems**:
   - Finnish (negative auxiliary)
   - Hebrew (special existential אֵין)
   - Tagalog (existential distinction wala/may)

## Common Errors (Expected)

1. **Missing Negative Concord** (~40% in NC languages): Not marking all constituents
2. **Confusing Verbal vs Constituent Negation** (~25%): Scope ambiguity
3. **Missing Special Negative Existentials** (~20%): Using regular negation instead
4. **Incorrect NPI Selection** (~15%): "something" instead of "anything"
5. **Genitive/Partitive Case Errors** (~30% in Russian/Finnish): Not changing case under negation

## Next Actions Detail

### Stage 1: Algorithm Creation
- [ ] Level 1: Check for negation markers
- [ ] Level 2: Identify negation type (verbal/existential/constituent)
- [ ] Level 3: Determine scope of negation
- [ ] Level 4: Validate against source language
- [ ] Level 5: Check target language requirements

### Stage 2: Test Set Development
- [ ] Sample negative constructions across genres
- [ ] Include NC vs non-NC language examples
- [ ] Cover all negation types (verbal, existential, constituent)
- [ ] Test rhetorical negatives (negative interrogatives)

### Stage 3: Accuracy Testing
- [ ] Target: <5% error rate (binary feature, should be high accuracy)
- [ ] NC compliance check for NC languages
- [ ] Special existential validation
- [ ] NPI licensing accuracy

### Stage 4: Production Quality
- [ ] Achieve ≥95% accuracy
- [ ] Zero critical errors (ungrammatical negation)
- [ ] Language-specific rules documented

## Learnings for Other Features

**Binary features with complex interactions**: Polarity appears simple (Affirmative/Negative) but interacts with:
- Mood (negative imperatives)
- Aspect (perfective/imperfective under negation)
- Case (genitive of negation)
- Quantification (scope interactions)

## References

- Negative concord patterns: LEARNINGS.md § Error 1
- Special existentials: README.md § Hierarchical Prompt Level 2
- NPI licensing: LEARNINGS.md § Error 4

## Migration Notes

Migrated from: `/plan/tbta-rebuild-with-llm/features/polarity/`
Migration date: 2025-11-15
Status: Training set ready, algorithm development required
