# TBTA Features

This directory contains all TBTA (Translation-Based Text Analysis) features for biblical text analysis. Each feature represents a grammatical, discourse, or linguistic characteristic that is important for Bible translation.

## Development Methodology

All features follow the authoritative **6-stage development methodology** documented in [STAGES.md](STAGES.md):

1. **Research TBTA Documentation** - Review official TBTA docs and existing analyses
2. **Language Study** - Identify which language families require this feature
3. **Scholarly and Internet Research** - Find latest research and web information
4. **Generate Test Set with Translation Data** - Create balanced datasets with real translation evidence
5. **Analyze Translations & Develop Algorithm** - Discover patterns from what translators actually did
6. **Test Against Validate Set & Peer Review** - Blind validation and critical peer reviews

See [TEMPLATE.md](TEMPLATE.md) for the feature development template and [STAGES.md](STAGES.md) for complete methodology details.

## Features Overview

### Grammatical Features

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

All features are currently at **Stage 0: Not yet started**. Previous work has been archived in [features-archive/](features-archive/) for reference.

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

## Archive

Previous feature implementations are available in [features-archive/](features-archive/) for reference. These contain valuable learnings but did not follow the complete 6-stage methodology.

## Cross-Feature Learnings

Transferable patterns and insights from feature development are documented in [../learnings/README.md](../learnings/README.md). These learnings help accelerate development of new features by applying proven approaches.

## Resources

- **[STAGES.md](STAGES.md)** - Complete 6-stage development methodology (authoritative)
- **[TEMPLATE.md](TEMPLATE.md)** - Feature development template with checklists
- **[../learnings/README.md](../learnings/README.md)** - Cross-feature learnings and patterns
- **[features-archive/](features-archive/)** - Previous feature implementations for reference

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
