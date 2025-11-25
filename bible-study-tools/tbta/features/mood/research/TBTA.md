# Mood: TBTA Documentation Review

**Feature**: Mood (Grammatical Modality)
**TBTA Classification**: Tier A - Essential (affects 1000+ languages)
**Source**: TBTA Source Documentation (`/bible-study-tools/tbta/tbta-source/*`)
**Review Date**: 2025-11-25

## 1. Feature Definition

### 1.1 Concept

**What is Mood?**

{tbta-source/TBTA-FEATURES.md}: "Mood | Indicative, Imperative, Subjunctive, Potential, Obligation | Turkish, Japanese, Greek | ✅ Complete"

Mood (also called modality) indicates the speaker's attitude toward an action - whether it's presented as factual (indicative), commanded (imperative), hypothetical (subjunctive), possible (potential), or necessary (obligation). {features-archive/mood/DETAILED-RULES.md}: "Mood indicates the speaker's stance toward the action."

{tbta-source/TBTA-FEATURES.md}: Listed as Tier A Essential feature #10 - "Cannot be easily inferred from context" in 1,000+ languages.

### 1.2 TBTA Schema Location

**Where is it encoded?**

{tbta-source/DATA-STRUCTURE.md}: Verb feature at Position 3 in 9-character verb encoding scheme:

```
Position 3: Mood | Example Values: I (indicative), a-e (potential levels), f-i (obligation levels)
```

{tbta-source/DATA-STRUCTURE.md}: "The JSON export expands these character codes into readable field names with descriptive values."

**Applies to**: Verbs only

**Gateway Feature**: Part = Verb

## 2. Value Inventory

### 2.1 Complete Value List

{features-archive/mood/README.md}: "Complete Value Enumeration - 11 distinct mood types"

TBTA supports **11 mood values** with semantic distinctions:

| Mood Value | Code | Frequency | Description | Example Languages |
|-----------|------|-----------|-------------|-------------------|
| **Indicative** | I | 94.62% | Factual statements, assertions of reality | All languages |
| **'might' Potential** | a | 2.53% | Possible but uncertain | Turkish, Japanese |
| **'must' Obligation** | f | 1.58% | Strong necessity | Greek δεῖ, Turkish |
| **Forbidden Obligation** | i | 0.63% | Strong prohibition ("must not") | Greek μή + subj |
| **'should' Obligation** | g | 0.32% | Moderate obligation/advice | Greek χρή |
| **'should not' Obligation** | h | 0.32% | Negative advice | Greek μή + pres imp |
| **'may' (permissive)** | - | <0.1% | Permission granted | Greek ἔξεστι |
| **Probable Potential** | b | <0.1% | Likely outcome | Epistemic modal |
| **Definite Potential** | c | <0.1% | Certain possibility | Strong capability |
| **Subjunctive** | S | Rare | Hypothetical, conditional | Greek subjunctive |
| **Optative** | O | Rare | Wishes, prayers | Greek optative |

{features-archive/mood/README.md}: "Test Data: Matthew 24 (316 verbs, 51 verses)"

### 2.2 Value Documentation Status

**Fully Documented** (with morphology/examples):
- Indicative (I): {features-archive/mood/DETAILED-RULES.md} Section 1 with Greek/Hebrew equivalents
- 'must' Obligation (f): {features-archive/mood/DETAILED-RULES.md} Section 2.1 with δεῖ constructions
- 'should' Obligation (g): {features-archive/mood/DETAILED-RULES.md} Section 2.2 with χρή constructions
- Forbidden Obligation (i): {features-archive/mood/DETAILED-RULES.md} Section 2.3 with μή + subjunctive
- 'might' Potential (a): {features-archive/mood/DETAILED-RULES.md} Section 3.1 with δύναμαι
- Subjunctive (S): {features-archive/mood/DETAILED-RULES.md} Section 4
- Optative (O): {features-archive/mood/DETAILED-RULES.md} Section 5

**Minimally Documented**:
- 'may' permissive: Mentioned but rare in test data
- Probable/Definite Potential: Listed but <0.1% frequency

### 2.3 Frequency Data

{features-archive/mood/README.md}: Complete frequency distribution from Matthew 24 test data:

```
Total Values: 11 distinct mood types
Test Data: Matthew 24 (316 verbs, 51 verses)
Source Languages: Greek (morphological mood) + Hebrew (modal semantics)

Distribution:
- Indicative: 94.62% (bulk of narrative)
- Modal meanings: 5.38% (crucial semantic distinctions)
- 11 distinct values capture semantic modality beyond traditional grammatical moods
```

## 3. Gateway Features & Constraints

**Controlling Feature**: Part of Speech = Verb

{tbta-source/DATA-STRUCTURE.md}: Mood is Position 3 in verb encoding, not present in noun/adjective/adverb encoding schemes.

**Dependency Rules**:
- Mood is **valid** when Part = Verb
- Mood is **not applicable** for Nouns, Adjectives, Adverbs, Adpositions, Conjunctions, Particles

**Related Features**:
- {tbta-source/DATA-STRUCTURE.md}: "Time Granularity (Position 1) provides temporal context"
- {tbta-source/DATA-STRUCTURE.md}: "Aspect (Position 2) modifies mood interpretation"
- {tbta-source/DATA-STRUCTURE.md}: "Polarity (Position 4) affects obligation strength"

## 4. TBTA Labeling Policy

### 4.1 Semantic vs Morphological Priority

{tbta-source/CRITIQUE.md}: "2.1 Greek Imperatives Marked as 'Indicative'"

**Evidence**:
```yaml
Matthew 5:44 - ἀγαπᾶτε (agapate)
Greek Form: Present Active Imperative 2nd Plural
TBTA Mood: Indicative  ← Incorrect
Expected: Imperative or Obligation
```

{tbta-source/CRITIQUE.md}: "Issue: Morphological imperative mood coded as semantic 'Indicative' mood."

**Impact**: {tbta-source/CRITIQUE.md}: "Affects ALL imperative clauses in NT (thousands of instances)"

**Root Cause**: {tbta-source/CRITIQUE.md}: "TBTA encoded propositional content (semantic) but lost morphological information critical for translation."

**Policy (inferred)**:
- TBTA prioritizes **semantic meaning** over morphological form
- Greek subjunctive in prohibition contexts → Forbidden Obligation (semantic)
- Greek imperative forms → sometimes coded as Indicative (semantic statement)
- **Problem**: {tbta-source/CRITIQUE.md}: "Creates confusion: Is it statement or command?"

### 4.2 Obligation Levels - Semantic Distinctions

{features-archive/mood/DETAILED-RULES.md}: Section 2 distinguishes obligation strength:

**Strong Obligation** ('must' - code f):
- Greek δεῖ + infinitive: "it is necessary to..."
- Strong imperative force
- Urgent commands, divine requirements

**Moderate Obligation** ('should' - code g):
- Greek χρή + infinitive: "it is fitting/proper to..."
- Advice or recommendation, not mandate

**Strong Prohibition** (Forbidden - code i):
- Greek μή + aorist subjunctive
- "Must not" - absolute prohibition

**Moderate Prohibition** ('should not' - code h):
- Greek μή + present imperative
- Negative advice - "shouldn't"

{features-archive/mood/DETAILED-RULES.md}: "Context and Greek auxiliary determine strength"

### 4.3 Potential Levels - Certainty Continuum

{features-archive/mood/DETAILED-RULES.md}: Section 3 distinguishes epistemic possibility:

- **'might' Potential** (code a): Possible but uncertain - δύναμαι "I am able"
- **Probable Potential** (code b): Likely outcome - stronger evidence
- **Definite Potential** (code c): Certain capability - demonstrated ability

{features-archive/mood/DETAILED-RULES.md}: "Potential moods indicate epistemic possibility along a certainty continuum."

## 5. Edge Cases & Special Patterns

### 5.1 Greek Imperatives Coded as Indicative (Critical Issue)

{tbta-source/CRITIQUE.md}: "2.1 Greek Imperatives Marked as 'Indicative'"

**Problem**:
```yaml
Matthew 5:44 - ἀγαπᾶτε (agapate) "love!"
Greek Morphology: Present Active Imperative 2nd Plural
TBTA Mood: Indicative  ← Error
Expected: Imperative or Obligation (f/g)
```

**Frequency**: {tbta-source/CRITIQUE.md}: "Affects ALL imperative clauses in NT (thousands of instances)"

**Impact**:
- {tbta-source/CRITIQUE.md}: "Target languages with distinct imperative morphology need source mood information"
- {tbta-source/CRITIQUE.md}: "Languages using modal particles need obligation strength"
- Semantic priority loses critical grammatical information

### 5.2 Aspect Overgeneralization to "Unmarked"

{tbta-source/CRITIQUE.md}: "2.2 Overgeneralization of 'Unmarked' Aspect"

**Evidence**:
```yaml
Matthew 5:6 - χορτασθήσονται (chortasthēsontai, "will be filled")
Verb Class: Accomplishment (telic - has completion point)
Context: Hunger → Satisfaction (clear endpoint)
TBTA Aspect: Unmarked  ← Too coarse
Expected: Completive (based on Aktionsart + morphology)
```

**Impact**: {tbta-source/CRITIQUE.md}: "Aspect-prominent languages (Slavic, Niger-Congo, Austronesian) need this information"

**Related to Mood**: {features-archive/mood/DETAILED-RULES.md}: "Aspect modifies mood interpretation"

**Methodology Gap**: {tbta-source/CRITIQUE.md}: "No systematic Aktionsart classification in TBTA approach"

### 5.3 Interrogative Force with Indicative Mood

{features-archive/mood/DETAILED-RULES.md}: Section 1 "Common Confusion":

**Pattern**: Questions can use indicative mood for factual queries

**Example**: "Do you **see** all these things?" (Matthew 24:2)
- IlLocutionary Force: Interrogative (yes-no question)
- Mood: Indicative (question about fact, not command)

{features-archive/mood/DETAILED-RULES.md}: "Key Insight: IlLocutionary Force and Mood are separate dimensions"

### 5.4 Rhetorical Questions - Mood vs Force

{features-archive/mood/DETAILED-RULES.md}: "Case 2: Rhetorical Questions"

**Pattern**: Interrogative form with statement/command force

**Example**: "Should we not obey God?" (expects yes, functions as obligation)

{features-archive/mood/DETAILED-RULES.md}: "Resolution: Analyze rhetorical function, not just syntax"

**Not explicitly addressed**: How TBTA codes rhetorical questions - as Indicative or Obligation?

### 5.5 Embedded Moods - Infinitive Clauses

{features-archive/mood/DETAILED-RULES.md}: "Case 3: Embedded Moods"

**Pattern**: Infinitive clauses inheriting mood from parent verb

**Example**: δεῖ ἀκοῦσαι "it is necessary to hear"
- Parent: δεῖ (modal auxiliary - 'must')
- Embedded: ἀκοῦσαι (infinitive "to hear")
- Result: 'must' Obligation applies to "hear"

**TBTA Handling**: Not explicitly documented whether infinitive inherits mood or has separate coding.

## 6. Past Learnings & Policy Evolution

### 6.1 Matthew 24 Test Data Analysis

{features-archive/mood/README.md}: "Test Data: Matthew 24 (316 verbs, 51 verses)"

**Key Findings**:
- 94.62% of verbs are Indicative (factual narrative)
- 5.38% use modal meanings (crucial semantic distinctions)
- 11 distinct mood values needed to capture semantic modality
- Even 2-mood target languages benefit (guides modal verb choice)

{features-archive/mood/README.md}: "TBTA helps decide when to add modal verbs ('must,' 'should,' 'might')"

### 6.2 Morphology + Semantics + Discourse Context

{features-archive/mood/README.md}: "Methodology: Morphology + Semantics + Discourse Context"

**Three-Layer Approach**:
1. Greek/Hebrew morphological mood (indicative, subjunctive, optative, imperative)
2. Semantic modality (obligation strength, possibility level)
3. Discourse context (illocutionary force, speaker authority)

{features-archive/mood/DETAILED-RULES.md}: Multiple sections document morphology-semantics mapping

### 6.3 Validated Experiment Results

{tbta-source/CRITIQUE.md}: "6.2 Verb TAM Experiment"

**Accuracy**: 96.3% reproduction

**Issues Found**:
- {tbta-source/CRITIQUE.md}: "All imperatives marked 'Indicative' mood"
- {tbta-source/CRITIQUE.md}: "All tested verbs marked 'Unmarked' aspect"
- {tbta-source/CRITIQUE.md}: "No Aktionsart information used"

**Interpretation**: Core mood algorithm is very accurate (96.3%), but systematic policy issues affect imperatives.

### 6.4 Polarity Interaction with Obligation

{features-archive/mood/DETAILED-RULES.md}: "Polarity Interaction" section:

| Construction | Mood | Interpretation |
|-------------|------|----------------|
| Affirmative + 'must' | Strong positive obligation | "You must go" |
| Negative + 'must' | Forbidden Obligation | "You must not go" |
| Affirmative + 'should' | Moderate advice | "You should go" |
| Negative + 'should' | 'should not' Obligation | "You shouldn't go" |

{features-archive/mood/DETAILED-RULES.md}: "Polarity (affirmative/negative) modifies obligation strength"

## 7. Mixed Annotations

**Not mentioned** in TBTA documentation for Mood feature.

**Assessment**: Mood is typically a **single value** feature - a verb is either Indicative, Subjunctive, Optative, Imperative, Potential, or Obligation, not multiple simultaneously.

**Possible exception**: Not listed in reviewed documentation.

{features-archive/mood/README.md}: Each verb in Matthew 24 test data has exactly one mood value (no mixed annotations shown).

**Status**: Does not appear to use mixed annotations (unlike features that allow multiple simultaneous values).

## 8. Translation Impact

{features-archive/mood/README.md}: "Impact Level: VERY HIGH ⭐⭐⭐⭐⭐ (5/5 stars)"

### 8.1 Why This Matters for Translation

{features-archive/mood/README.md}: "Mood determines whether an action is presented as fact, possibility, necessity, or command—fundamentally shaping reader understanding."

**Examples of Misidentification**:
- Commands → suggestions: "you should go" vs "you must go"
- Facts → possibilities: "he is here" vs "he might be here"
- Permissions → obligations

### 8.2 Cross-Linguistic Variation

{features-archive/mood/README.md}: "Languages vary enormously in mood encoding"

**Encoding Strategies**:
- Grammatical morphology: Greek subjunctive, Turkish evidentials
- Modal verbs: English must/should/might
- Context alone: Some languages rely on pragmatic inference

{tbta-source/TBTA-FEATURES.md}: Example languages needing mood annotation: Turkish, Japanese, Greek

### 8.3 Coverage for Different Language Types

{features-archive/mood/README.md}: "Even 2-mood languages benefit: TBTA helps decide when to add modal verbs"

**Language Types**:
- **Rich mood morphology** (Greek, Turkish): Need to map source → target mood accurately
- **Modal verb languages** (English, Germanic): Need to choose appropriate modal (must/should/might)
- **Context-dependent** (Chinese, many isolating): Need guidance on when modality is semantically present

## 9. Time Field Correlation

{features-archive/mood/DETAILED-RULES.md}: "Time Field Correlation" section:

| Time | Mood Type | Interpretation |
|------|-----------|----------------|
| Present | Indicative | Current state of affairs |
| Immediate Future | Obligation/Indicative | Imminent action (factual or required) |
| Later Today | Potential/'should' | Near-term possibility/recommendation |
| Discourse | Indicative | Narrative/timeless present |
| Historic Past | Indicative | Historical fact |
| Remote Future | Potential | Distant possibility |

{features-archive/mood/DETAILED-RULES.md}: "The Time field provides additional semantic information about mood"

## 10. Aspect Correlation

{features-archive/mood/DETAILED-RULES.md}: "Aspect Correlation" section:

| Aspect | Mood | Combined Meaning |
|--------|------|------------------|
| Perfective | Indicative | Completed fact |
| Imperfective | Obligation | Ongoing requirement |
| Progressive | Imperative | Action in progress requested |
| Habitual | Indicative | Regular factual pattern |
| Inceptive | Obligation | Beginning requirement |

{features-archive/mood/DETAILED-RULES.md}: "Aspect modifies mood interpretation"

## 11. Summary

**Feature**: Mood (grammatical modality indicating speaker's attitude toward action)

**Values**: 11 distinct types - Indicative (94.62%), 5 obligation levels (2.85%), 3 potential levels (2.53%), Subjunctive/Optative (rare)

**Encoding**: {tbta-source/DATA-STRUCTURE.md}: Position 3 in 9-character verb code

**Gateway**: Part = Verb only

**Policy**:
- Semantic priority over morphology (undocumented but evident)
- {tbta-source/CRITIQUE.md}: Greek imperatives → Indicative (semantic statement)
- Obligation/Potential levels capture semantic nuance beyond traditional mood
- {features-archive/mood/DETAILED-RULES.md}: Morphology + Semantics + Discourse Context methodology

**Critical Issues**:
- {tbta-source/CRITIQUE.md}: ALL Greek imperatives marked as Indicative (thousands of instances)
- {tbta-source/CRITIQUE.md}: Aspect overgeneralized to "Unmarked" (loses semantic information)
- {tbta-source/CRITIQUE.md}: No Aktionsart classification (verb lexical aspect)
- Embedded mood inheritance not documented

**Strengths**:
- {features-archive/mood/README.md}: 11-value system captures semantic modality comprehensively
- {tbta-source/CRITIQUE.md}: 96.3% reproduction accuracy (high reliability)
- {features-archive/mood/DETAILED-RULES.md}: Detailed Greek/Hebrew morphology mappings
- {features-archive/mood/README.md}: "Impact Level: VERY HIGH" - affects all target languages

**Status**: TBTA Tier A - Essential feature, marked as "Complete" {tbta-source/TBTA-FEATURES.md}

**Test Coverage**: Matthew 24 (316 verbs, 51 verses) - {features-archive/mood/README.md}

**Accuracy**: 96.3% reproduction in experiments - {tbta-source/CRITIQUE.md}

**Key Languages**: Greek (rich morphological mood in NT), Hebrew (modal semantics in OT), Target languages with diverse mood systems (Turkish, Japanese)

## Bibliography

All sources from TBTA documentation:

**TBTA Source Files**:
- {tbta-source/TBTA-FEATURES.md} - Feature catalog listing Mood as Tier A #10
- {tbta-source/DATA-STRUCTURE.md} - Technical encoding (Position 3 in verb code)
- {tbta-source/CRITIQUE.md} - Validated issues from experiments (imperatives as indicative, aspect overgeneralization)

**Features Archive**:
- {features-archive/mood/README.md} - Quick reference with 11-value enumeration and frequency data
- {features-archive/mood/DETAILED-RULES.md} - Comprehensive interpretation rules for each mood type

**Web Sources**:
- AllTheWord.org TBTA materials (general background, no specific mood documentation found)

**Note**: GitHub repository search for "AllTheWord/tbta_db_export" did not yield specific mood documentation beyond what's already in archived files.

---

**Document Status**: TBTA research complete
**Lines**: 335 (within 200-350 target)
**Citations**: All facts cited with {source-file} format
**Coverage**: Feature definition, values, constraints, policy, edge cases, learnings, mixed annotations, summary
