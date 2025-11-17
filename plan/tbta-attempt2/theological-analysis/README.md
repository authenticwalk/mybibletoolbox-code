# Theological Analysis for TBTA Features

This directory contains the theological framework and analysis for distinguishing between arbitrary and non-arbitrary lexical choices in Bible translation features.

## Core Documents

### 1. [ARBITRARY-VS-NON-ARBITRARY.md](ARBITRARY-VS-NON-ARBITRARY.md)
The comprehensive framework for determining when lexical choices have theological ramifications versus when they are theologically neutral.

**Key Sections**:
- Theological criteria for non-arbitrary classification
- Feature-by-feature arbitrarity analysis
- Multi-answer output templates for non-arbitrary cases
- Integration with STAGES.md validation process

## Purpose

When predicting implicit linguistic features (number, person, aspect, etc.) for Bible translation, we must carefully distinguish between:

- **Arbitrary choices**: Theologically neutral decisions that don't affect doctrine or interpretation
- **Non-arbitrary choices**: Theologically significant decisions that impact doctrine, church practice, or salvation understanding

## Key Principles

1. **Prevent Eisegesis**: We must not introduce theological meanings that weren't in the original text
2. **Preserve Ambiguity**: Where the source text is ambiguous, maintain that ambiguity
3. **Present Options**: For non-arbitrary cases, provide multiple theological perspectives
4. **Respect Traditions**: Acknowledge legitimate theological diversity across denominations
5. **Flag Critical Issues**: Clearly mark choices that could enable false teaching

## Integration with TBTA Workflow

This theological framework integrates with the standard [STAGES.md](../../tbta-rebuild-with-llm/features/STAGES.md) workflow:

- **Stage 1**: Identify potential non-arbitrary contexts during research
- **Stage 4**: Include theological diversity in test set generation
- **Stage 5**: Develop multi-answer prompts for non-arbitrary cases
- **Stage 6**: Enhanced peer review including theological validation

## Feature-Specific Applications

### High-Impact Features (Many Non-Arbitrary Contexts)
- **Person Systems (Clusivity)**: Trinity, prayer, apostolic authority
- **Number Systems**: Trinity (trial vs plural), divine unity
- **Aspect**: Salvation (completed vs ongoing), prophecy
- **Mood**: Divine commands vs suggestions
- **Illocutionary Force**: Christ's authority, prophetic warnings

### Lower-Impact Features (Mostly Arbitrary)
- **Polarity**: Generally grammatical (except theological negations)
- **Deixis**: Spatial/temporal reference (except divine omnipresence)
- **Formality**: Social register (except divine address)

## Documentation Standards

For each feature with non-arbitrary contexts:

1. Create `experiments/THEOLOGICAL-ANALYSIS.md`
2. Document all non-arbitrary categories
3. Provide multi-answer YAML templates
4. List required safeguards and warnings
5. Include denominational perspectives

## Validation Requirements

Non-arbitrary cases require enhanced validation:

- **Theological Review**: Doctrinal soundness check
- **Cultural Review**: Cross-cultural sensitivity
- **Translation Practice**: Field testing with actual translators
- **Expert Consultation**: Domain experts for critical doctrines

## Contact & Contribution

This framework was developed through deep theological analysis using extended reasoning to ensure doctrinal accuracy while respecting theological diversity. Contributions and reviews from theological experts are welcome.