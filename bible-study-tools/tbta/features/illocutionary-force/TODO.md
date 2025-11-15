# Illocutionary Force Feature - TODO

**Current Status**: 🟡 Experiment Complete, Validation Needed
**Last Updated**: 2025-11-15

## Summary

Illocutionary force determines HOW a clause functions communicatively—whether asserting, questioning, commanding, or exhorting. **CRITICAL** for East Asian languages (Japanese, Mandarin, Korean) which require sentence-final particles for every clause type.

**Key Discovery**: Imperative register choices encode speaker-hearer relationships with theological significance (Jesus commanding demons vs teaching disciples).

## Current Stage Status

### ✅ Complete
- README.md (complete feature specification with 6 force types)
- LEARNINGS.md (10 critical discoveries about force in translation)
- experiments/experiment-001.md (validation complete: 70-90% accuracy by category)

**Findings from Experiment 001**:
- Declarative prediction: 90%+ accuracy
- Interrogative (yes/no vs wh-): 85%+ accuracy
- Imperative register prediction: 70%+ accuracy (highly language-dependent)
- Rhetorical question identification: ~75% accuracy

### ⏳ Next Steps Required

**Priority 1: Blind Validation**
- [ ] Create validate set (100+ verses, never seen by algorithm)
- [ ] Test on new verses without answers visible
- [ ] Measure accuracy on unseen data
- [ ] Refine based on error patterns

**Priority 2: Register Refinement**
- [ ] Improve imperative register accuracy (currently 70%)
- [ ] Document speaker-hearer relationship patterns
- [ ] Create register selection guidelines per language family
- [ ] Test with Japanese keigo, Korean speech levels

**Priority 3: Rhetorical Question Handling**
- [ ] Improve rhetorical detection (currently 75%)
- [ ] Document patterns (negative comparative = superlative assertion)
- [ ] Test genre variation (prophetic vs epistolary)

## Files Migrated

**Core Documentation:**
- README.md (6 force types with examples, hierarchical template)
- LEARNINGS.md (10 critical discoveries)

**Experiments:**
- experiments/experiment-001.md (complete with test cases, accuracy results)

## Complete Value Enumeration

| Value | Definition | Bible Context | Accuracy |
|-------|-----------|---------------|----------|
| **Declarative** | Statement of fact | "Jesus healed the sick", "God is love" | 90%+ |
| **Yes-No Interrogative** | Polar question | "Do you believe in Jesus?" | 85%+ |
| **Wh-Interrogative** | Content question | "Who is Jesus?", "When will He come?" | 85%+ |
| **Imperative** | Command | "Repent!", "Follow me" | 95% (form), 70% (register) |
| **Hortative** | First-person plural | "Let us love one another" | 95%+ |
| **Exclamative** | Strong emotion | "How great is God!", "O the depths!" | 80%+ |

## Gateway Features (Quick Prediction Rules)

| Condition | Predicted Force | Confidence |
|-----------|----------------|------------|
| Imperative verb form | **Imperative** | 95%+ |
| Interrogative pronoun (who, what, why) | **Interrogative** | 90%+ (unless rhetorical) |
| Question particle (Gk: ἆρα, οὐ, μή) | **Interrogative** | 95%+ |
| Optative mood (Greek) | **Optative/Hortative** | 95%+ |
| Standard indicative statement | **Declarative** | 85%+ (default) |

## Common Errors (From Experiment 001)

1. **Confusing Grammatical Mood with Force**: Assuming indicative = declarative always
2. **Missing Indirect Speech Acts**: Polite questions functioning as commands
3. **Confusing Rhetorical vs Genuine Questions**: Both use interrogative form
4. **Not Recognizing Hortatives**: Treating "let us" as second-person imperative
5. **Missing Register Distinctions**: Using same imperative for all contexts

## Next Actions Detail

### Stage 1: Blind Validation Set
- [ ] Sample 100+ verses across all 6 force types
- [ ] Ensure genre balance (narrative, teaching, prophecy, law)
- [ ] Include rhetorical questions (20-30% of questions)
- [ ] Lock predictions BEFORE checking TBTA

### Stage 2: Error Analysis
- [ ] For every error: 6-step systematic analysis
- [ ] Identify patterns (genre-specific? language-specific?)
- [ ] Refine algorithm based on learnings
- [ ] Document edge cases

### Stage 3: Language-Specific Testing
- [ ] Japanese: Test particle suggestions (か, よ, ね, な)
- [ ] Mandarin: Test particle usage (吗, 吧, 呢, 了)
- [ ] Korean: Test speech level selection
- [ ] Spanish: Test imperative mood conjugations

### Stage 4: Production Quality
- [ ] Achieve ≥95% force category accuracy
- [ ] Improve register prediction to 80%+
- [ ] Rhetorical question detection to 85%+
- [ ] Zero critical errors (wrong force type)

## Key Findings from LEARNINGS.md

**Discovery 1**: Particle Systems as Effective as Inflectional Systems
- East Asian languages (Japanese, Mandarin, Korean) mark force as explicitly as inflected languages
- English underutilizes force marking (relies on context/intonation)

**Discovery 2**: Imperative Register is Theologically Significant
- Jesus to crowds vs disciples vs demons requires different registers
- Wrong register choice carries unintended theological baggage

**Discovery 3**: Rhetorical Questions Are Systematic (~20-30% of biblical questions)
- Expressing awe, asserting negation, challenging assumptions
- Must be marked separately from genuine information-seeking

**Discovery 4**: Hortative/Imperative Distinction Affects Community Theology
- "Let us" (reciprocal action) vs "You must" (imposed command)
- Loss of hortative changes theological emphasis

**Discovery 5**: Politeness Can Override Grammatical Categories
- Korean/Japanese: Imperatives restructured as interrogatives for politeness
- Grammar and pragmatics not neatly separated

## Learnings for Other Features

**Multi-Level Interaction Pattern**: Illocutionary force interacts with:
- Mood (grammatical mood)
- Honorifics (speaker-hearer relationship)
- Register (formal vs informal)
- Evidentiality (source of information)

This multi-level pattern likely exists for other feature clusters.

## References

- Experiment results: experiments/experiment-001.md
- Critical discoveries: LEARNINGS.md
- Hierarchical prompt template: README.md

## Migration Notes

Migrated from: `/plan/tbta-rebuild-with-llm/features/illocutionary-force/`
Migration date: 2025-11-15
Status: Experiment complete, blind validation required
