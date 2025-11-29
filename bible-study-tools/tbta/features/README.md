# TBTA Features

This directory contains all TBTA (Translation-Based Text Analysis) features for biblical text analysis. Each feature represents a grammatical, discourse, or linguistic characteristic that is important for Bible translation.

## Development Methodology

All features follow the authoritative .instructions-to-build-feature


## Features Overview

### Grammatical Features

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

