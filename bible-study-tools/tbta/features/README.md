# TBTA Features - Progress & Definitions

**Purpose**: Track implementation progress for linguistic features used in Bible translation. Each feature helps translators working in languages with grammatical distinctions not found in English/Greek/Hebrew.

**Methodology**: See [STAGES.md](STAGES.md) for 6-stage workflow • See [TEMPLATE.md](TEMPLATE.md) for feature development guide

---

## Noun Features (7)

### Person System (Clusivity)
**Status**: ✅ Complete (Stage 6) • **Accuracy**: 100%
**Definition**: Distinguishes inclusive "we" (speaker+listener) from exclusive "we" (speaker+others, not listener)
**Languages**: 1000+ (Tagalog, Malay, Fijian, Vietnamese, many Native American)
**Source**: TBTA original
**Notes**: Also handles 1st-as-3rd, 2nd-as-3rd grammaticalizations

### Number System
**Status**: 🟨 Stage 2 (Language Study) • **Accuracy**: TBD
**Definition**: Beyond singular/plural - includes Dual (2), Trial (3), Quadrial (4), Paucal (few)
**Languages**: 172 Austronesian/Polynesian (Hawaiian, Samoan, Slovenian dual)
**Source**: TBTA original
**Notes**: Genesis 1:26 "us" = Trial (Trinity reference)

### Participant Tracking
**Status**: 🟨 Stage 4 (Refinement) • **Accuracy**: 90%
**Definition**: Marks discourse status - First Mention, Routine, Exiting, Restaging, Frame Inferable
**Languages**: 200+ switch-reference (Papua New Guinea, Native American)
**Source**: TBTA original
**Notes**: Critical for pronoun clarity in ambiguous contexts (Genesis 4:8)

### Proximity System
**Status**: ⬜ Stage 1 (Research) • **Accuracy**: TBD
**Definition**: Demonstrative distinctions - Near Speaker/Listener/Both, Remote Visible/Invisible, Temporal (10-way)
**Languages**: 1000+ (Japanese 3-way, Korean 3-way, Spanish 3-way, Tagalog 3-way)
**Source**: TBTA original

### Noun List Index
**Status**: ⬜ Not Started • **Accuracy**: TBD
**Definition**: Entity tracking across discourse (1-9, A-Z) for consistent reference
**Languages**: Navajo, Kiowa, PNG languages requiring explicit referent marking
**Source**: TBTA original

### Polarity (Noun)
**Status**: ⬜ Not Started • **Accuracy**: TBD
**Definition**: Affirmative vs Negative marking on noun phrases
**Languages**: Turkish, Finnish, Russian (negative case marking)
**Source**: TBTA original

### Surface Realization
**Status**: ⬜ Not Started • **Accuracy**: TBD
**Definition**: How referent appears - Noun, Pronoun, Zero (dropped), Clitic
**Languages**: Spanish (pro-drop), Japanese (zero pronouns), Italian (clitics)
**Source**: TBTA original

---

## Verb Features (10+)

### Mood
**Status**: ✅ Complete (Stage 6) • **Accuracy**: 100% extraction
**Definition**: Indicative, Imperative, Subjunctive, Potential, Obligation
**Languages**: Turkish, Japanese, Greek (classical mood system)
**Source**: TBTA original
**Notes**: Explicit encoding discovered in source text

### Aspect
**Status**: 🟨 Stage 5 (Documentation) • **Accuracy**: 98.1%
**Definition**: Perfective, Imperfective, Progressive, Habitual, Inceptive, Completive
**Languages**: Russian, Polish, Mandarin, Arabic (required aspect marking)
**Source**: TBTA original
**Notes**: Multi-factor convergence pattern validated

### Time Granularity
**Status**: ⬜ Stage 1 (Research) • **Accuracy**: TBD
**Definition**: 20+ temporal distinctions - Immediate, Today, Yesterday, Last Week, Remote Past, Discourse Time
**Languages**: Tagalog (11 distinctions), Yagua (5 past tenses), ChiBemba (tense+aspect)
**Source**: TBTA original
**Notes**: Genesis narratives require precision for creation timeline

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
**Status**: ⬜ Stage 1 (Research) • **Accuracy**: TBD
**Definition**: Declarative, Interrogative, Imperative, Suggestive, Jussive
**Languages**: Japanese (sentence-final particles), Chinese, Korean
**Source**: TBTA original

### Speaker Demographics (6 sub-features)
**Status**: ⬜ Not Started • **Accuracy**: TBD
**Definition**: Age, Gender, Relationship, Attitude, Speech Style
**Languages**: Japanese (keigo), Korean (honorifics), Javanese (register), Thai
**Source**: TBTA original
**Notes**: Genesis 19:31 - daughters speaking shows age/relationship dynamics

### Discourse Genre
**Status**: ⬜ Stage 1 (Research) • **Accuracy**: TBD
**Definition**: Narrative, Expository, Poetic, Legal, Prophetic, Epistolary
**Languages**: All languages (affects feature distribution)
**Source**: TBTA original
**Notes**: Gateway feature - sets expectations for other features

### Topic NP
**Status**: ⬜ Not Started • **Accuracy**: TBD
**Definition**: Marks topic vs comment (Agent-like, Patient-like)
**Languages**: Japanese (wa/ga), Korean, Chinese, Tagalog
**Source**: TBTA original

*(4 more clause features - see TBTA-FEATURES.md)*

---

## Adjective Features (2)

### Degree
**Status**: ⬜ Not Started • **Accuracy**: TBD
**Definition**: Positive, Comparative, Superlative, Excessive
**Languages**: Most Indo-European, many others
**Source**: TBTA original

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

## Legend

- ✅ **Complete** (Stage 6): Production-ready with validation
- 🟨 **In Progress** (Stages 2-5): Active development
- ⬜ **Not Started** (Stage 1 or pending): Research phase or not yet prioritized

**Accuracy**: Prediction accuracy against TBTA annotations (when available)
**Source**: TBTA original / Redefined / NEW (our additions beyond TBTA's 59)

---

## Quick Stats

- **Total Features**: 59 TBTA + TBD new
- **Complete**: 2 (Person/Clusivity, Mood)
- **In Progress**: 2 (Aspect, Participant Tracking)
- **Pending**: 55+

**Tier A Priority** (19 features): Essential for 1000+ languages
**Tier B Priority** (20 features): Important, often inferable
**Tier C Priority** (20 features): Specialized, language-specific

See individual feature directories for detailed experiments, prompts, and validation results.

---

**Methodology**: [STAGES.md](STAGES.md) • **Learnings**: [../learnings/README.md](../learnings/README.md)
**Last Updated**: 2025-11-14
