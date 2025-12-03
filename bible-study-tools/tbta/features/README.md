# TBTA Features

This directory contains all TBTA (Translation-Based Text Analysis) features for biblical text analysis. Each feature represents a grammatical, discourse, or linguistic characteristic that is important for Bible translation.

## Development Methodology

<<<<<<< HEAD
All features follow the authoritative **6-stage development methodology** documented in [STAGES.md](STAGES.md):

1. **Research TBTA Documentation** - Review official TBTA docs and existing analyses
2. **Language Study** - Identify which language families require this feature
3. **Scholarly and Internet Research** - Find latest research and web information
4. **Generate Test Set with Translation Data** - Create balanced datasets with real translation evidence
5. **Analyze Translations & Develop Algorithm** - Discover patterns from what translators actually did
6. **Test Against Validate Set & Peer Review** - Blind validation and critical peer reviews

See [TEMPLATE.md](TEMPLATE.md) for the feature development template and [STAGES.md](STAGES.md) for complete methodology details.
=======
All features follow the authoritative .instructions-to-build-feature

>>>>>>> origin/feat/self-learning-tbta

## Features Overview

### Grammatical Features

<<<<<<< HEAD
- **[aspect](aspect/)** - Grammatical aspect (perfective, imperfective, etc.)
- **[degree](degree/)** - Degree of comparison or intensity
- **[mood](mood/)** - Grammatical mood (indicative, subjunctive, imperative, etc.)
- **[number-system](number-system/)** - Grammatical number (singular, dual, plural)
- **[person-system](person-system/)** - Grammatical person (1st, 2nd, 3rd person)
- **[polarity](polarity/)** - Affirmation vs negation

### Discourse Features

- **[discourse-genre](discourse-genre/)** - Type of discourse (narrative, poetry, prophecy, etc.)
- **[honorifics-register](honorifics-register/)** - Social register and honorific language use
- **[illocutionary-force](illocutionary-force/)** - Speech act force (command, question, statement, etc.)
- **[participant-tracking](participant-tracking/)** - How participants are tracked across discourse
- **[topic-np](topic-np/)** - Topic-prominent vs subject-prominent language features

### Spatial & Temporal Features

- **[proximity-system](proximity-system/)** - Spatial/temporal proximity (near, far, etc.)
- **[time-granularity](time-granularity/)** - Temporal granularity and precision

### Surface Features

- **[surface-realization](surface-realization/)** - How semantic content is expressed on the surface

## Development Status

All 14 features have completed **Stage 1: Research & Definition**.

| Feature | Category | Description | Stage |
|---------|----------|-------------|-------|
| [aspect](aspect/) | Grammatical | Perfective/imperfective viewpoint | ✅ Stage 1 |
| [degree](degree/) | Grammatical | Comparison and intensity marking | ✅ Stage 1 |
| [mood](mood/) | Grammatical | Indicative, subjunctive, imperative, etc. | ✅ Stage 1 |
| [number-system](number-system/) | Grammatical | Singular, dual, trial, plural | ✅ Stage 1 |
| [person-system](person-system/) | Grammatical | 1st/2nd/3rd person, clusivity | ✅ Stage 1 |
| [polarity](polarity/) | Grammatical | Affirmation vs negation | ✅ Stage 1 |
| [discourse-genre](discourse-genre/) | Discourse | Narrative, poetry, prophecy, etc. | ✅ Stage 1 |
| [honorifics-register](honorifics-register/) | Discourse | Social register and politeness | ✅ Stage 1 |
| [illocutionary-force](illocutionary-force/) | Discourse | Speech act force (command, question) | ✅ Stage 1 |
| [participant-tracking](participant-tracking/) | Discourse | Reference tracking across discourse | ✅ Stage 1 |
| [topic-np](topic-np/) | Discourse | Topic-prominent information structure | ✅ Stage 1 |
| [proximity-system](proximity-system/) | Spatial/Temporal | Near/far deixis | ✅ Stage 1 |
| [time-granularity](time-granularity/) | Spatial/Temporal | Temporal remoteness | ✅ Stage 1 |
| [surface-realization](surface-realization/) | Surface | Voice and surface patterns | ✅ Stage 1 |

**Next**: Stage 2 (Generate Test Set) for all features.
=======
| Feature | Description | Stage | TBTA Data |
|---------|-------------|-------|-----------|
| [aspect](aspect/) | Perfective, imperfective, progressive, habitual | 2.1 ✅ | Yes |
| [degree](degree/) | Comparative, superlative, intensified | 2.1 ✅ | Yes |
| [mood](mood/) | Indicative, subjunctive, imperative, etc. | 2.1 ✅ | Yes |
| [number-systems](number-systems/) | Singular, dual, trial, plural | 2.1 ✅ | Yes |
| [person-system](person-system/) | 1st/2nd/3rd person + clusivity | 2.1 ✅ | Yes |
| [polarity](polarity/) | Affirmative vs negative | 2.1 ✅ | Yes |
| [reflexivity](reflexivity/) | Reflexive vs reciprocal | 2.1 ✅ | Yes (limited) |

### Semantic Features

| Feature | Description | Stage | TBTA Data |
|---------|-------------|-------|-----------|
| [semantic-role](semantic-role/) | Agent, patient, source, destination, etc. | 2.1 ✅ | Yes |

### Discourse Features

| Feature | Description | Stage | TBTA Data |
|---------|-------------|-------|-----------|
| [discourse-genre](discourse-genre/) | Narrative, poetry, prophecy, epistolary | 2.1 ✅ | Yes |
| [illocutionary-force](illocutionary-force/) | Declarative, interrogative, imperative | 2.1 ✅ | Yes |
| [participant-tracking](participant-tracking/) | First mention, routine, exiting, restaging | 2.1 ✅ | Yes |
| [honorifics-register](honorifics-register/) | Social register and honorific language | - | No TBTA data |
| [topic-np](topic-np/) | Topic-prominent language features | - | No TBTA data |

### Spatial & Temporal Features

| Feature | Description | Stage | TBTA Data |
|---------|-------------|-------|-----------|
| [proximity-system](proximity-system/) | Near/far spatial and temporal deixis | 2.1 ✅ | Yes |
| [time-granularity](time-granularity/) | Temporal precision (today, yesterday, etc.) | 2.1 ✅ | Yes |

### Surface Features

| Feature | Description | Stage | TBTA Data |
|---------|-------------|-------|-----------|
| [surface-realization](surface-realization/) | Noun, pronoun, zero, clitic | 2.1 ✅ | Yes |

## Development Status

**14 features** with TBTA data have completed Stage 2.1 (Analysis Dataset).
**2 features** (honorifics-register, topic-np) have no TBTA data available.

Previous work archived in [.features-archive/](.features-archive/).
>>>>>>> origin/feat/self-learning-tbta

## Key Principles

### Translation-Informed Development

Every feature follows a **discovery-based approach**:

1. **"There is nothing new under the sun"** - With ~1000 Bible translations, someone has already dealt with your unique linguistic feature
2. **Discover, don't just validate** - Analyze what real translators chose to understand the correct answer
3. **Dual sources of truth**:
   - **TBTA annotations**: Discourse-level analysis (answer sheets)
   - **Real translations**: What translators actually did (question sheets)
4. **Translation consensus matters**: When 80%+ of marking-language translations agree, that's a strong signal
5. **Net benefit focus**: Measure mistakes avoided vs mistakes introduced

### Methodological Rigor

- **Sample size**: 100+ verses per value minimum (statistical power)
- **Balanced sampling**: OT/NT proportional, multiple genres, books, typical + adversarial cases
- **Blind testing**: Subagents prevent seeing answers during development
- **Locked predictions**: Git commits before checking TBTA (prevents unconscious bias)
- **6-step error analysis**: Every failure reveals a blind spot worth investigating
- **100% accuracy goal**: "The text is God's inerrant word - less than 100% means we're missing something"

### Production Readiness

Features are production-ready only when:

- ✅ Accuracy ≥ 100% on validate set (with ≥100 verses per value)
- ✅ All 4 peer reviews passed (theological, linguistic, methodological, translation practitioner)
- ✅ Translation practitioner testing shows net benefit (mistakes avoided > introduced)
- ✅ Real-world testing with both marking and non-marking languages
- ✅ Translation teams would recommend using this data

<<<<<<< HEAD
=======
## Archive

Previous feature implementations are available in [features-archive/](features-archive/) for reference. These contain valuable learnings but did not follow the complete 6-stage methodology.

>>>>>>> origin/feat/self-learning-tbta
## Cross-Feature Learnings

Transferable patterns and insights from feature development are documented in [../learnings/README.md](../learnings/README.md). These learnings help accelerate development of new features by applying proven approaches.

<<<<<<< HEAD
## Resources

- **[STAGES.md](STAGES.md)** - Complete 6-stage development methodology (authoritative)
- **[TEMPLATE.md](TEMPLATE.md)** - Feature development template with checklists
- **[../learnings/README.md](../learnings/README.md)** - Cross-feature learnings and patterns

## Getting Started

To develop a new feature:

1. Choose a feature directory (e.g., `aspect/`, `mood/`, etc.)
2. Read [STAGES.md](STAGES.md) for the complete methodology
3. Follow the stage checklist in the feature's README.md
4. Use [TEMPLATE.md](TEMPLATE.md) for file structure and naming conventions
5. Apply learnings from [../learnings/README.md](../learnings/README.md)
6. Remember: Discovery-based development using real translation evidence

---

**Need help?** Check [STAGES.md](STAGES.md) for methodology or [../learnings/README.md](../learnings/README.md) for patterns from other features.
=======
>>>>>>> origin/feat/self-learning-tbta
