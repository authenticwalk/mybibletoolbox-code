# Topic NP Feature - TODO

**Current Status**: 🟡 Documentation Complete, Testing Required
**Last Updated**: 2025-11-15

## Summary

Topic NP identifies which noun phrase serves as the discourse topic (what the clause is "about"), distinct from grammatical subject. **CRITICAL** for ~25% of world's languages that are topic-prominent (Japanese, Korean, Mandarin, Tagalog, Indonesian).

**Key Insight**: Topic ≠ Subject. Patients and objects can be topics. Discourse context determines topic, not just syntax.

## Current Stage Status

### ✅ Complete
- README.md (TIER 1 overview with complete value enumeration)
- TOPIC-VS-SUBJECT.md (theoretical distinction, Li & Thompson typology)
- TOPIC-PROMINENT-LANGUAGES.md (language-specific patterns)
- DETAILED-METHODOLOGY.md (TIER 2 hierarchical prompt, gateway features, common errors)
- DOCUMENTATION-SUMMARY.md (overview of documentation structure)

### ⏳ Next Steps Required

**Priority 1: Validation Against Translations**
- [ ] Compare TBTA values with Japanese wa/ga usage
- [ ] Test Korean eun/neun vs i/ga particle selection
- [ ] Verify Mandarin topic-comment structures
- [ ] Check Tagalog focus marking

**Priority 2: Correlation Testing**
- [ ] Validate 95% correlation with Participant Tracking
- [ ] Test accuracy of gateway features
  - Restaging → Topic (70% confidence)
  - Semantic Role A + sentence-initial → Topic A (80%)
  - Surface Realization Zero + Previous Topic → continued (75%)

**Priority 3: Test Set Execution**
- [ ] Sample 100 clauses (50 narrative, 25 teaching, 25 poetry)
- [ ] Measure against topic-prominent language translations
- [ ] Target: 75-85% accuracy (discourse features are challenging)

## Files Migrated

**Core Documentation** (TIER 1-2 complete):
- README.md (quick translator test, concrete examples, gateway features)
- DETAILED-METHODOLOGY.md (hierarchical prediction, error patterns)
- TOPIC-VS-SUBJECT.md (theoretical foundation)
- TOPIC-PROMINENT-LANGUAGES.md (Japanese, Korean, Mandarin, Tagalog)
- DOCUMENTATION-SUMMARY.md (navigation guide)

## Complete Value Enumeration

| Value | Meaning | Frequency | Example |
|-------|---------|-----------|---------|
| **A** | Agent-like Topic | ~15-20% | "Jesus (TOPIC) said to them..." |
| **P** | Patient-like Topic | ~10-15% | "That stone (TOPIC), the builders rejected" |
| **N** | No explicit topic | ~70% | "God created the heavens" (subject-predicate) |

**Note**: Values borrowed from semantic role system to indicate whether topic is agent-like or patient-like.

## Gateway Features (Strong Correlations)

| If Feature X = Value | Then Topic NP | Confidence |
|---------------------|---------------|------------|
| Participant Tracking = Restaging | = A or P | 70% |
| Semantic Role = A + Sentence-initial | = A | 80% |
| Surface Realization = Zero (pro-drop) + Previous Topic | = (continued) | 75% |
| Salience Band = Foreground | More likely topic | 60% |

**Validation Rule**: If Japanese wa appears → TBTA should not be N (mismatch indicates error)

## Validation Approach

**Test Set**: 100 clauses
- 50 from narrative (Gospels)
- 25 from teaching (Epistles)
- 25 from poetry (Psalms)

**Validation Method**:
Compare TBTA Topic NP values with Japanese/Korean/Mandarin translations:
- **Japanese**: wa (topic) vs ga (subject) particle usage
- **Korean**: eun/neun (topic) vs i/ga (subject) particle usage
- **Mandarin**: Topic-comment structure vs subject-predicate

**Expected Accuracy**: 75-85%
- Higher in narrative (topic continuity)
- Lower in poetry (complex structures)

## Next Actions Detail

### Stage 1: Translation Comparison
- [ ] Collect Japanese Bible translation (新共同訳 or 新改訳)
- [ ] Collect Korean Bible translation (개역개정 or 새번역)
- [ ] Collect Mandarin translation (和合本)
- [ ] Parse particle usage for test verses

### Stage 2: Correlation Testing
- [ ] Cross-reference with Participant Tracking feature data
- [ ] Measure actual correlation percentage
- [ ] Identify systematic exceptions
- [ ] Refine confidence scores

### Stage 3: Accuracy Testing
- [ ] Run TBTA predictions on test set
- [ ] Compare with translation particle usage
- [ ] Document divergences (error vs valid variation)
- [ ] Refine methodology based on results

### Stage 4: Production Quality
- [ ] Achieve 75-85% target accuracy
- [ ] Document language-specific variation
- [ ] Create quick-reference for translators

## Common Prediction Errors (Expected)

1. **Topic vs Subject Confusion** (30%): Not recognizing patient/object topics
2. **Missing Discourse Context** (25%): Ignoring narrative flow, restaging
3. **Genre Variation** (20%): Poetry uses more complex topic structures
4. **Pro-Drop Interaction** (15%): Zero subjects can still be topics
5. **Definiteness Correlation** (10%): Indefinite NPs unlikely to be topics

## Learnings for Other Features

**Discourse Feature Pattern**: Topic NP demonstrates how discourse features (topic, participant tracking) require multi-clause context for accurate prediction. Single-verse analysis insufficient.

**Language Typology Importance**: Topic-prominence vs subject-prominence is fundamental typological distinction. Other features may have similar typological splits.

## References

- Li & Thompson typology: TOPIC-VS-SUBJECT.md
- Language-specific patterns: TOPIC-PROMINENT-LANGUAGES.md
- Prediction methodology: DETAILED-METHODOLOGY.md

## Migration Notes

Migrated from: `/plan/tbta-rebuild-with-llm/features/topic-np/`
Migration date: 2025-11-15
Status: Documentation complete, validation testing required
