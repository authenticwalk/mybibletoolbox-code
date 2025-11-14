# TBTA Features Directory

This directory contains 59 TBTA linguistic features organized by subdirectory, plus cross-feature documentation.

---

## Quick Reference

**Feature Summary**: [FEATURE-SUMMARY.md](FEATURE-SUMMARY.md) - All 59 features organized by tier and translation priority

**Feature Status**: [FEATURE-STATUS-SUMMARY.md](FEATURE-STATUS-SUMMARY.md) - Current implementation status and completion tracking

**Cross-Feature Patterns**: [CROSS-FEATURE-LEARNINGS.md](CROSS-FEATURE-LEARNINGS.md) - Universal patterns discovered across multiple feature experiments

---

## Tier A Features (Critical - 12 features)

Essential features affecting most languages. Highest translation priority.

**Person Systems** - [person-systems/](person-systems/)
Clusivity (inclusive/exclusive "we"), theological context (Trinity = trial number), participant tracking

**Number Systems** - [number-systems/](number-systems/)
Singular, dual, trial, paucal, plural distinctions beyond English binary system

**Gender** - [gender/](gender/)
Grammatical gender systems, natural vs grammatical gender, agreement patterns

**Tense/Aspect/Mood** - [verb-tam/](verb-tam/)
Verb temporal, aspectual, and modal systems for accurate translation

**Clause Types** - [105-clauses/](105-clauses/)
Declarative, interrogative, imperative, exclamatory clause structures

**Illocutionary Force** - [illocutionary-force/](illocutionary-force/)
Speech act classification (commands, requests, assertions, questions)

**Polarity** - [polarity/](polarity/)
Affirmative vs negative, scope of negation, double negatives

**Participant Reference** - [participant-tracking/](participant-tracking/)
Tracking referents across discourse (introduced, routine, exiting, restaging)

**Discourse Genre** - [discourse-genre/](discourse-genre/)
Narrative, dialogue, poetry, prophecy, legal, etc.

**Register/Honorifics** - [honorifics-register/](honorifics-register/)
Formality levels, respectful vs casual speech, social distance marking

---

## Tier B Features (Important - 20 features)

Significant for many languages, moderate translation impact.

**Proximity/Deixis** - [proximity/](proximity/)
Demonstrative distinctions (near/far), spatial/temporal/discourse domains

**Evidentiality** - [evidentiality/](evidentiality/)
Information source marking (witnessed, reported, inferred)

**Reflexivity** - [reflexivity/](reflexivity/)
Reflexive pronouns, reciprocal constructions, middle voice

**Time Granularity** - [time-granularity/](time-granularity/)
Temporal precision (specific time, general time, eternal)

**Lexical Sense** - [lexical-sense/](lexical-sense/)
Word sense disambiguation for polysemous terms

**Surface Realization** - [surface-realization/](surface-realization/)
Overt vs implicit arguments, zero anaphora, pro-drop

---

## Tier C Features (Enhanced - 27 features)

Specialized features for specific languages, lower priority.

**Degree** - [degree/](degree/)
Comparative, superlative, equative, excessive marking

**Noun Classifier** - [noun-classifier/](noun-classifier/)
Numeral classifier systems (East Asian, Austronesian languages)

**Directionals** - [directionals/](directionals/)
Motion towards/away, elevation marking, oriented motion

**Distributivity** - [distributivity/](distributivity/)
Collective vs distributive interpretation of plurals

**Associated Motion** - [associated-motion/](associated-motion/)
Motion combined with main verb (go-and-do, come-and-do patterns)

**Additional Features**: See subdirectories for complete list

---

## Feature Subdirectories

Each feature subdirectory contains:
- `README.md` - Feature overview (≤200 lines)
- `experiments/` - Validation experiments and results
- Topic files - Detailed analysis (≤400 lines each)

**Total features**: 59 subdirectories

---

## Cross-Feature Documentation

**Universal Patterns**: [CROSS-FEATURE-LEARNINGS.md](CROSS-FEATURE-LEARNINGS.md)
Transferable patterns discovered from experiments:
- Semantic encoding over morphological form
- Theological context improves predictions
- Discourse role determines feature values
- Ancient translations guide interpretation
- Rare values often absent in Biblical text

**Related**: See [../learnings/](../learnings/) for methodology patterns (hierarchical prompts, rarity principle, multi-factor convergence)

---

## Archive

Historical analysis documents archived at: [../archive/features-analysis/](../archive/features-analysis/)
- 100% accuracy achievement reports
- Completed improvement summaries
- Integration opportunity analyses
- Implementation pattern studies

---

**Navigation**: Use FEATURE-SUMMARY.md for quick lookup, subdirectories for detailed specifications.
