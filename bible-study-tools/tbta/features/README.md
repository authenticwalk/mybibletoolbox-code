# TBTA Features - Progress & Definitions

**Purpose**: Track implementation progress for linguistic features used in Bible translation. Each feature helps translators working in languages with grammatical distinctions not found in English/Greek/Hebrew.

**Methodology**: See [STAGES.md](STAGES.md) for 6-stage workflow • See [TEMPLATE.md](TEMPLATE.md) for feature development guide

---

## Noun Features (7)

### Person System (Clusivity)
**Status**: ✅ Complete (Stage 6)* • **Accuracy**: 98% (external validation)
**Definition**: Distinguishes inclusive "we" (speaker+listener) from exclusive "we" (speaker+others, not listener)
**Languages**: 200+ person-marking (Tagalog, Malay, Fijian, Vietnamese, many Native American)
**Source**: TBTA original
**Notes**: Also handles 1st-as-3rd, 2nd-as-3rd grammaticalizations. *Stage 6 has validation blockers - see [person-system/TODO.md](./person-system/TODO.md)

### Number System
**Status**: ✅ Stage 2 Complete (Language Study) • **Accuracy**: TBD
**Definition**: Beyond singular/plural - includes Dual (2), Trial (3), Quadrial (4), Paucal (few)
**Languages**: ~501+ languages across 5 families (Austronesian 176, Trans-New Guinea 129, Indo-European 135, Australian 36, Afro-Asiatic 25)
**Source**: TBTA original
**Notes**: ~220+ languages require dual (44%), ~20-30 require trial, ~50-70 require paucal. Genesis 1:26 "us" creates trial/plural ambiguity in some languages. See [number-system/](./number-system/) for complete analysis.

### Participant Tracking
**Status**: 🟨 Stage 4 (Refinement) • **Accuracy**: 90% (target: 95%)
**Definition**: Marks discourse status - First Mention, Routine, Exiting, Restaging, Frame Inferable
**Languages**: 200+ switch-reference (Papua New Guinea, Native American)
**Source**: TBTA original
**Notes**: Critical for pronoun clarity in ambiguous contexts (Genesis 4:8). Known issues: quoted speech boundaries, vision contexts, implicit role shifts. See [participant-tracking/](./participant-tracking/) for refinement plan.

### Proximity System
**Status**: 🟨 Stage 2 (Language Study) • **Accuracy**: TBD (expected 80-85%)
**Definition**: Demonstrative distinctions - 10-value system covering spatial/temporal/discourse dimensions (Near Speaker/Listener/Both, Remote Visible/Invisible, Temporal, Contextual)
**Languages**: 664+ across 6 families (Japanese 3-way, Korean 3-way, Spanish 3-way, Tagalog 3-way, Austronesian visibility, Trans-New Guinea elevation)
**Source**: TBTA original
**Notes**: Complex inference required for Hebrew unmarked זֶה. See [proximity-system/](./proximity-system/) for experiments and language mapping.

### Noun List Index
**Status**: ⬜ Not Started • **Accuracy**: TBD
**Definition**: Entity tracking across discourse (1-9, A-Z) for consistent reference
**Languages**: Navajo, Kiowa, PNG languages requiring explicit referent marking
**Source**: TBTA original

### Polarity (Noun)
**Status**: 🟨 Stage 2 (Training Data) • **Accuracy**: TBD
**Definition**: Affirmative vs Negative marking on noun phrases, including negative concord, NPIs, existentials
**Languages**: Turkish, Finnish, Russian (negative case marking), Slavic (negative concord), Greek (NPIs)
**Source**: TBTA original
**Notes**: Training set complete. Learnings documented on NC systems, NPIs, existentials. See [polarity/](./polarity/) for training data.

### Surface Realization
**Status**: 🟨 Stage 2 (Methodology) • **Accuracy**: TBD (95% correlation with Participant Tracking)
**Definition**: How referent appears - Noun, Pronoun, Zero (dropped), Clitic - with 5-level hierarchy from full NP to zero
**Languages**: 700+ analyzed (Spanish pro-drop, Japanese zero pronouns, Italian clitics, Arabic agreement)
**Source**: TBTA original
**Notes**: 95% predictable from Participant Tracking + language typology. See [surface-realization/](./surface-realization/) for complete methodology.

---

## Verb Features (10+)

### Mood
**Status**: ✅ Complete (Stage 5)* • **Accuracy**: 94.6% Indicative, 11 modal values
**Definition**: Indicative, Imperative, Subjunctive, Potential, Obligation (11 total mood values)
**Languages**: Turkish, Japanese, Greek (classical mood system), Arabic
**Source**: TBTA original
**Notes**: Gateway features (Greek imperative 99%, modal particles 85-95%). *Stage 6 validation needed - see [mood/TODO.md](./mood/TODO.md)

### Aspect
**Status**: 🟨 Stage 5 (Documentation) • **Accuracy**: 98.1%
**Definition**: Perfective, Imperfective, Progressive, Habitual, Inceptive, Completive
**Languages**: Russian, Polish, Mandarin, Arabic (required aspect marking)
**Source**: TBTA original
**Notes**: Multi-factor convergence pattern validated (5-factor model). Remaining 1.9% errors justify optimal accuracy threshold. See [aspect/](./aspect/) for complete methodology and external validation (94.7% agreement across languages).

### Time Granularity
**Status**: ✅ Stage 1 Complete (Research) • **Accuracy**: TBD
**Definition**: 20+ temporal distinctions - Immediate, Today, Yesterday, Last Week, Remote Past, Discourse Time
**Languages**: 150+ languages with grammatical temporal granularity. High: Tagalog (11), Yagua (5 past); Medium: ChiBemba (4+4 symmetrical), other Bantu; Aspect-based: Japanese, Korean, Mandarin
**Source**: TBTA original
**Notes**: Genesis narratives require precision for creation timeline. Hebrew temporal ambiguity creates translation challenges. See [time-granularity/](./time-granularity/) for complete 20-category analysis and translation impact examples.

### Voice System
**Status**: ⬜ Not Started • **Accuracy**: TBD
**Definition**: Active, Middle, Passive, Antipassive, Causative
**Languages**: Greek (middle voice), Ergative languages
**Source**: TBTA original

### Reflexivity
**Status**: ⬜ Not Started • **Accuracy**: TBD
**Definition**: Marks when subject and object are same entity
**Languages**: Romance languages (se constructions), Russian
**Source**: TBTA original

### Verb TAM (combined)
**Status**: ⬜ Not Started • **Accuracy**: TBD
**Definition**: Tense-Aspect-Mood as integrated system
**Languages**: Many languages encode these together, not separately
**Source**: TBTA original

*(4 more verb features - see individual feature directories)*

---

## Clause Features (8)

### Illocutionary Force
**Status**: 🟨 Stage 4 (Experiments) • **Accuracy**: 70-90% by category
**Definition**: Declarative, Interrogative, Imperative, Suggestive, Jussive - sentence-level speech act classification
**Languages**: Japanese (sentence-final particles), Chinese, Korean, Greek, Hebrew
**Source**: TBTA original
**Notes**: 10 critical discoveries documented. Register prediction needs improvement to 80%+. See [illocutionary-force/](./illocutionary-force/) for experiments.

### Speaker Demographics (6 sub-features)
**Status**: 🟨 Stage 5 (Production Documentation) • **Accuracy**: TBD
**Definition**: Age, Gender, Relationship, Attitude, Speech Style, Addressee Marking - 6-feature comprehensive speaker/addressee system
**Languages**: Japanese (keigo), Korean (honorifics), Javanese (register), Thai, Vietnamese, Hindi
**Source**: TBTA original
**Notes**: Production-ready documentation complete with 100+ Biblical character codes. Tool implementation needed. See [honorifics-register/](./honorifics-register/)

### Discourse Genre
**Status**: ✅ Stage 1 Complete (Research) • **Accuracy**: TBD (TBTA has 11% coverage - only Climactic Narrative observed)
**Definition**: Narrative, Expository, Poetic, Legal, Prophetic, Epistolary - 9 total genres (register-based classification)
**Languages**: All languages (affects feature distribution - genre determines grammaticality patterns)
**Source**: TBTA original
**Notes**: Gateway feature - sets expectations for other features. Tense systems vary dramatically by genre (90%+ correlation). See [discourse-genre/](./discourse-genre/) for patterns and training data.

### Topic NP
**Status**: 🟨 Stage 2 (Documentation) • **Accuracy**: TBD
**Definition**: Marks topic vs comment (Agent-like, Patient-like) with Li & Thompson typology
**Languages**: Japanese (wa/ga), Korean (eun/neun), Chinese, Tagalog, topic-prominent languages (25% of world's languages)
**Source**: TBTA original
**Notes**: TIER 1-2 documentation complete. Translation validation needed for Japanese wa/ga, Korean eun/neun. See [topic-np/](./topic-np/)

*(4 more clause features - see TBTA-FEATURES.md)*

---

## Adjective Features (2)

### Degree
**Status**: 🟨 Stage 8 (Algorithm Validation) • **Accuracy**: 71% (Algorithm v2.0)
**Definition**: Positive, Comparative, Superlative, Excessive, Equative - 5-value system with 3 NEW universal principles discovered
**Languages**: Most Indo-European, many others
**Source**: TBTA original
**Notes**: Algorithm v2.0 tested (71% on adversarial). Full validation needed to reach ≥95%. See [degree/](./degree/) for complete training and error analysis.

### Usage (Attributive/Predicative)
**Status**: ⬜ Not Started • **Accuracy**: TBD
**Definition**: Whether adjective modifies noun directly or through copula
**Languages**: Many languages restrict which adjectives can be attributive
**Source**: TBTA original

---

## Additional Categories

See [../tbta-source/TBTA-FEATURES.md](../tbta-source/TBTA-FEATURES.md) for complete catalog:
- **Adverb Features** (2)
- **Adposition Features** (3)
- **Conjunction Features** (2)
- **Particle Features** (1)
- **Phrasal Features** (8)
- **Paragraph/Episode Markers** (2)

---

## NEW Features (Beyond TBTA's 59)

**Status**: 🔵 Proposed (23 extensions documented) • See [../tbta-source/IMPROVEMENTS.md](../tbta-source/IMPROVEMENTS.md) for full details

### Aktionsart (Lexical Aspect)
**Status**: ⬜ Proposed • **Definition**: Inherent temporal structure (State/Activity/Accomplishment/Achievement/Semelfactive)
**Languages**: Slavic, Niger-Congo, Austronesian (aspect-prominent languages)
**Source**: NEW • **Priority**: Tier A

### Evidentiality
**Status**: ⬜ Proposed • **Definition**: Information source (witnessed/reported/inferred/assumptive)
**Languages**: 250+ require evidentials (Quechuan, Tucanoan, Turkish, Korean)
**Source**: NEW • **Priority**: Tier A

### Switch-Reference
**Status**: ⬜ Proposed • **Definition**: Same-subject vs different-subject marking in clause chains
**Languages**: 80+ TNG languages, many Papuan, some Native American
**Source**: NEW • **Priority**: Tier B

### Mirativity
**Status**: ⬜ Proposed • **Definition**: New/surprising information to speaker
**Languages**: Albanian, Korean, Tibeto-Burman
**Source**: NEW • **Priority**: Tier B

### Honorifics/Social Register (Expanded)
**Status**: ⬜ Proposed • **Definition**: Plain/polite/humble/exalted register marking
**Languages**: Japanese, Korean, Javanese, many Southeast Asian
**Source**: NEW (TBTA has limited "Speaker's Attitude") • **Priority**: Tier A

**Additional Extensions** (18 more): Morphological Mood Layer, Phasal Marking, Deontic Strength Gradation, Presupposed Entities, Collective Reference, Vocative Addressing, Lesser/Greater Paucal, Morphological Number Layer, Collective Number, Emphatic Affirmative, Negation Scope, Elevation-Based Proximity, Across-Water Proximity, Excessive vs Intensification, Attenuative/Diminutive, Information Structure, Split Referent Tracking, Impersonal Agent

---

## Legend

- ✅ **Complete** (Stage 6): Production-ready with validation
- 🟨 **In Progress** (Stages 2-5): Active development
- ⬜ **Not Started** (Stage 1 or pending): Research phase or not yet prioritized
- 🔵 **Proposed** (NEW features): Documented extensions beyond TBTA's original 59

**Accuracy**: Prediction accuracy against TBTA annotations (when available)
**Source**: TBTA original / Redefined / NEW (our additions beyond TBTA's 59)

---

## Quick Stats

- **Total Features**: 59 TBTA + 23 NEW = 82 total
- **Feature Directories Created**: 14 (Person System, Mood, Aspect, Participant Tracking, Number System, Time Granularity, Proximity System, Discourse Genre, Degree, Surface Realization, Honorifics/Register, Polarity, Topic NP, Illocutionary Force)
- **Complete**: 2 (Person/Clusivity Stage 6*, Mood Stage 6*)
- **Stage Progress**: 10 features with experimental work migrated
- **In Progress**: 4 (Aspect Stage 5🟨, Participant Stage 4🟨, Number Stage 2✅, Time Granularity Stage 1✅)
- **Pending**: 45 TBTA + 23 NEW = 68

*Note: Person System and Mood marked complete but have validation blockers documented in TODO.md

**Tier A Priority** (19 TBTA + 5 NEW): Essential for 1000+ languages
**Tier B Priority** (20 TBTA + 8 NEW): Important, often inferable
**Tier C Priority** (20 TBTA + 10 NEW): Specialized, language-specific

See individual feature directories for detailed experiments, prompts, and validation results.

---

**Methodology**: [STAGES.md](STAGES.md) • **Learnings**: [../learnings/README.md](../learnings/README.md) • **Extensions**: [../tbta-source/IMPROVEMENTS.md](../tbta-source/IMPROVEMENTS.md)
**Last Updated**: 2025-11-15 (Migration complete: 14 features with experimental work from /plan/tbta-rebuild-with-llm/features/)
