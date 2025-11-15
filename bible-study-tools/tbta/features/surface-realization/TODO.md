# Surface Realization - TODO

**Current Status**: 🟡 Research Complete, Experimentation Needed
**Last Updated**: 2025-11-15

## Summary

Surface Realization feature determines how noun phrases appear in discourse (full nouns, pronouns, zero/dropped, or clitics). **CRITICAL** for pro-drop languages (70% of world languages) including Spanish, Japanese, Greek, Hebrew, Arabic, and 700+ others.

**Key Discovery**: Surface realization is OUTPUT of Participant Tracking state with 95% correlation. Must coordinate with tracking state FIRST before predicting surface form.

## Current Stage Status

### ✅ Complete
- Comprehensive linguistic analysis (LEARNINGS.md)
- Language family patterns documented (LANGUAGES-IN-TSV.md)
- Prediction methodology (5-level hierarchy)
- Cross-feature interactions (95% correlation with Participant Tracking)
- Bible translation guide with practical implications

### ⏳ Next Steps Required

**Priority 1: Validation**
- [ ] Create proper test set (100+ verses across genres)
- [ ] Validate 95% correlation with Participant Tracking
- [ ] Test pro-drop vs non-pro-drop predictions
- [ ] Check emphasis detection accuracy

**Priority 2: Experiment Execution**
- [ ] Run experiment-001 (currently only documented, not executed)
- [ ] Test with Spanish, Greek, Hebrew samples
- [ ] Validate clitic detection for Romance languages
- [ ] Measure error rates by pattern type

**Priority 3: Tool Development**
- [ ] Implement 5-level decision tree
- [ ] Add pro-drop language detection
- [ ] Create emphasis marker detection
- [ ] Handle register variations (formal vs informal)

## Files Migrated

**Core Documentation:**
- README.md (TIER 1-2 complete with progressive disclosure)
- LEARNINGS.md (12 critical discoveries)
- prediction-methodology.md (5-level hierarchy)
- cross-feature-interactions.md (correlations)
- bible-translation-guide.md (practical translation scenarios)

**Reference Materials:**
- QUICK-REFERENCE.md (decision tree + lookup tables)
- LANGUAGES-IN-TSV.md (700+ language patterns)

**Experiments:**
- experiments/experiment-001.md (planned, not yet executed)

## Key Findings

**Pro-Drop is Default for 70% of Languages**:
- East Asian (Japanese, Chinese, Korean): Near-complete pro-drop
- Romance (Spanish, Portuguese, Italian): Subject pro-drop required
- Slavic: Limited to 3rd person or specific contexts
- Germanic (English, German): Essentially no pro-drop

**95% Correlation with Participant Tracking**:
- First Mention → Noun
- Routine (non-pro-drop) → Pronoun
- Routine (pro-drop) → Zero or Pronoun
- Restaging → Noun

**Validation Rule**: If Tracking=First Mention BUT Surface=Zero → FLAG ERROR

## Common Prediction Errors (Expected)

1. **Not accounting for pro-drop** (40%): Spanish "Vino" is Zero (grammatical), not missing pronoun
2. **Missing emphasis** (25%): Greek explicit pronoun (when zero expected) = Emphatic
3. **Assuming all nouns equal** (15%): Bare vs definite nouns correlate with tracking states
4. **Ignoring register** (12%): Formal contexts use more nouns than dialogue
5. **Conflating zero with ellipsis** (8%): Coordination vs independent clauses

## Next Actions Detail

### Stage 1: Test Set Creation
- [ ] Sample 100+ verses across genres (narrative, epistle, poetry, law)
- [ ] Ensure coverage of all 4 surface types (noun, pronoun, zero, clitic)
- [ ] Include pro-drop languages (Spanish, Greek, Hebrew)
- [ ] Include non-pro-drop (English) for contrast
- [ ] Stratify by Participant Tracking states

### Stage 2: Correlation Validation
- [ ] Cross-reference with existing Participant Tracking data
- [ ] Measure 95% correlation claim
- [ ] Identify systematic exceptions

### Stage 3: Accuracy Testing
- [ ] Run prediction methodology on test set
- [ ] Target: 90%+ initial accuracy (following hierarchy)
- [ ] Identify high-error patterns
- [ ] Refine methodology based on results

### Stage 4: Production Quality
- [ ] Achieve 95%+ accuracy
- [ ] Critical errors (ungrammatical) < 1%
- [ ] Document language-specific variation

## Learnings for Other Features

**Gateway Feature Pattern**: Surface Realization demonstrates how one feature can be 95% predictable from another (Participant Tracking). This pattern should be tested for other feature pairs.

**Pro-Drop Typology**: Methodology for detecting pro-drop vs non-pro-drop languages applicable to other morphological typologies.

## References

- Participant Tracking correlation: See cross-feature-interactions.md
- Pro-drop patterns by language family: LANGUAGES-IN-TSV.md
- Translation scenarios: bible-translation-guide.md

## Migration Notes

Migrated from: `/plan/tbta-rebuild-with-llm/features/surface-realization/`
Migration date: 2025-11-15
Status: Research complete, experimentation phase required
