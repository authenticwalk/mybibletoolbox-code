# TBTA Feature Reproduction Experiments

## Purpose

These experiments validate whether LLM-based analysis can accurately reproduce TBTA's linguistic annotations by testing predictions against actual TBTA data. The goal is to create prompts and methods that accurately predict translation-critical features for Bible translation work.

## Methodology Overview

Each experiment follows a systematic approach:

1. **Feature Isolation** - Test individual linguistic features in isolation
2. **Hypothesis Formation** - Create prediction frameworks based on linguistic principles
3. **Blind Testing** - Make predictions WITHOUT seeing the TBTA answer first
4. **Validation** - Compare predictions to actual TBTA annotations
5. **Refinement** - Improve methods based on error analysis
6. **Documentation** - Record patterns and learnings for future use

This approach ensures predictions are grounded in reproducible methods, not memorized patterns.

## Results Summary

### High Accuracy Features (95-100%)

#### Person/Clusivity Systems (100%)
**What it predicts**: Whether "we/us" includes or excludes the addressee
**Method**: 5-level hierarchical framework prioritizing theological and ontological factors
**Key Findings**:
- Divine vs human distinction dominates all other factors
- Divine speech → EXCLUSIVE (God speaking to angels)
- Prayer to God → EXCLUSIVE (God not in "we")
- Community statements → INCLUSIVE (shared identity)
- Tested on 10+ passages with perfect accuracy

**See**: [person-systems/experiment-001.md](person-systems/experiment-001.md), [person-systems/clusivity-framework.md](person-systems/clusivity-framework.md)

#### Mood Features (100%)
**What it predicts**: Verb mood (indicative, imperative, obligation, potential, conditional)
**Method**: Direct extraction from VP nodes with pattern-based rules
**Key Findings**:
- 94.6% of Biblical narrative uses Indicative mood
- Obligation moods correlate with authority relationships and time urgency
- Mood is explicitly marked in TBTA (minimal inference needed)
- Tested on 316 verbs from Matthew 24 with 100% extraction accuracy

**See**: [mood/experiment-001.md](mood/experiment-001.md), [mood/mood_identification_method.md](mood/mood_identification_method.md)

#### Aspect Features (98.1%)
**What it predicts**: Aspect marking (perfective, imperfective, inceptive, cessative, etc.)
**Method**: Pattern-based rules combining mood, time, and verb semantics
**Key Findings**:
- 90.7% of verbs are Unmarked (default/neutral aspect)
- Potential mood → Inceptive aspect (100% correlation in test data)
- Simple decision rules achieve 98.1% accuracy (53/54 correct)
- Genre affects aspect distribution (narrative vs teaching)

**See**: [aspect/experiment-001.md](aspect/experiment-001.md), [aspect/aspect_identification_method.md](aspect/aspect_identification_method.md), [aspect/aspect_raw_data.json](aspect/aspect_raw_data.json)

#### NounListIndex (100% validation)
**What it predicts**: Index values for entity tracking within verses
**Method**: Entity coreference tracking with per-verse scope
**Key Findings**:
- Indices reset per verse (not continuous across verses)
- All entity mentions tracked systematically within verse boundaries
- Critical for switch-reference languages
- Algorithmic approach (no ambiguity)

**See**: [noun-index/experiment-001.md](noun-index/experiment-001.md), [noun-index/summary-and-applications.md](noun-index/summary-and-applications.md)

### Medium Accuracy Features (80-95%)

#### Participant Tracking (High Confidence)
**What it predicts**: First Mention, Routine, Restaging, Exiting, Frame Inferable
**Method**: Three complementary approaches (narrative flow, surface realization, information structure)
**Key Findings**:
- All three methods achieved 100% agreement on test verses
- Pronouns → Routine (previously established entities)
- Possessives → Frame Inferable (implied relationships)
- First mention of new entities → First Mention
- Ensemble approach provides high confidence through triangulation

**See**: [participant-tracking/experiment-001.md](participant-tracking/experiment-001.md), [participant-tracking/PREDICTION-METHODS.md](participant-tracking/PREDICTION-METHODS.md)

#### Number Systems (73-85%)
**What it predicts**: Singular, dual, trial, paucal, plural number marking
**Method**: Surface analysis combined with semantic expansion detection
**Key Findings**:
- TBTA adds implicit concepts not in surface text ("things" for actions, "house" for locations)
- Generic substances → Singular; Specific groups → Plural
- Collective nouns → Plural when referring to members
- Accuracy improved after accounting for semantic expansions

**See**: [number-systems/experiment-001.md](number-systems/experiment-001.md)

### Framework Stage (Awaiting Validation)

#### Proximity/Demonstratives
**What it predicts**: Proximal vs distal demonstrative marking
**Method**: Context-based rules for spatial, temporal, and emotional distance
**Key Findings**:
- Discourse deixis differs from physical deixis
- Emotional distance affects proximity marking
- Visibility matters in some language systems
- Framework created but needs validation against TBTA data

**See**: [proximity/experiment-001.md](proximity/experiment-001.md)

#### Time Granularity
**What it predicts**: Time precision (immediate, later today, remote past, etc.)
**Method**: Context and genre-based prediction rules
**Key Findings**:
- Genre strongly influences time marking (narrative past vs teaching present)
- Prophetic texts need special handling
- Evidentiality overlaps with time in some languages
- Framework ready for testing

**See**: [time/experiment-001.md](time/experiment-001.md)

## Key Methodological Insights

### 1. Theological/Semantic Factors Override Grammar
Divine vs human speakers determine clusivity regardless of grammatical structure. Generic vs specific semantics determine number beyond surface forms.

### 2. TBTA Adds Semantic Depth
TBTA doesn't just annotate surface text - it makes implicit information explicit. This requires LLMs to reason about frame semantics and cultural context.

### 3. Simple Rules Often Suffice
Pattern matching achieves 98% accuracy on aspect. Hierarchical decision trees work perfectly for clusivity. Not all features require complex models.

### 4. Multiple Methods Provide Validation
When three different approaches to participant tracking agree 100%, it validates our understanding. Ensemble methods increase confidence.

### 5. Per-Verse Scope is Critical
NounListIndex and other features reset at verse boundaries. Understanding TBTA's scope decisions is essential for accurate reproduction.

## Reproducibility Assessment

### Highly Reproducible (Can automate)
- NounListIndex assignment
- Mood extraction
- Aspect prediction
- Basic participant tracking

### Semi-Reproducible (Needs refinement)
- Number systems (semantic expansions)
- Clusivity (theological knowledge required)
- Proximity (context-dependent)

### Requires Human Review
- Ambiguous theological interpretations
- Cultural/historical context
- Rare grammatical constructions

## Recommendations for Combined System

1. **Layer predictions by confidence** - Start with high-confidence features, add medium-confidence with fallbacks
2. **Use ensemble methods** - Implement redundant approaches and compare results
3. **Context is crucial** - Genre affects aspect/mood; discourse position affects tracking; theology affects person systems
4. **Maintain per-verse scope** - Reset indices each verse as TBTA does
5. **Build learning loops** - Compare predictions to TBTA data, identify error patterns, refine rules

## Cross-Feature Patterns

- **Mood × Aspect**: Potential mood strongly correlates with Inceptive aspect
- **Person × Theology**: Divine identity determines clusivity more than grammar
- **Tracking × Surface**: Pronoun use reliably indicates Routine tracking status
- **Number × Semantics**: Implicit expansions add entities not in surface text
- **Time × Genre**: Narrative and teaching genres show distinct time patterns

## Next Steps

1. Validate framework-stage features (proximity, time) against actual TBTA data
2. Test combined feature prediction on broader verse samples
3. Measure cross-feature interaction effects
4. Create production-ready prediction prompts
5. Document edge cases and exceptions systematically

## File Organization

- `FRAMEWORK.md` - Overall experimental methodology
- `RESULTS-ANALYSIS.md` - Comprehensive results across all features
- `{feature}/experiment-001.md` - Initial experiment for each feature
- `{feature}/*_analysis.md` - Detailed analysis files
- `{feature}/*.json` - Raw data extracts for validation

## References

- See [FRAMEWORK.md](FRAMEWORK.md) for detailed experimental methodology
- See [RESULTS-ANALYSIS.md](RESULTS-ANALYSIS.md) for complete statistical analysis
- Individual experiment files contain verse-by-verse predictions and validations
