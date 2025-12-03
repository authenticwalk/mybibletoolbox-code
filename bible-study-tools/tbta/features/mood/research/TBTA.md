<<<<<<< HEAD
# TBTA Documentation Review: Mood Feature

**Feature**: Mood (Grammatical Modality)
**TBTA Tier**: A (Essential - affects 1000+ languages, cannot be easily inferred)
**Documentation Status**: Complete ✅
**Source Files Reviewed**:
- `/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md`
- `/bible-study-tools/tbta/features/features-archive/mood/README.md`
- `/bible-study-tools/tbta/features/features-archive/mood/DETAILED-RULES.md`
- `/bible-study-tools/tbta/features/features-archive/mood/LEARNINGS.md`

---

## 1. Conceptual Definition

**Mood** (also called **modality**) indicates the speaker's stance toward the reality or necessity of an action or state. It encompasses:

- **Epistemic modality**: Degree of certainty about an event (fact, possibility, probability)
- **Deontic modality**: Obligation, permission, prohibition
- **Dynamic modality**: Capability and volition

**TBTA's Approach**: TBTA extends traditional grammatical mood categories to include **semantic modality**, capturing not just morphological mood markers but the full spectrum of modal meanings expressed through:
- Morphological mood (Greek indicative, subjunctive, optative, imperative)
- Modal auxiliaries (δεῖ "must", δύναμαι "can", ἔξεστι "may")
- Syntactic constructions (conditional clauses, purpose clauses)
- Contextual semantics (speaker authority, genre conventions)

{tbta-features} Source: `/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md`

---

## 2. Value Inventory

TBTA encodes **11 distinct mood values** across three primary categories:

### 2.1 Indicative (Factual)

| Value | Description | Frequency | TBTA Code |
|-------|-------------|-----------|-----------|
| **Indicative** | Factual statements, assertions of reality | 94.62% | I |

**Identification**: Default mood; states actions as fact, reality, or certain prediction.
- Morphology: Greek indicative (οριστική), Hebrew qatal/wayyiqtol
- Context: Standard narrative, declarative statements
- No modal auxiliaries present

{mood-archive-readme} Source: `/bible-study-tools/tbta/features/features-archive/mood/README.md`
{mood-archive-detailed} Source: `/bible-study-tools/tbta/features/features-archive/mood/DETAILED-RULES.md` (lines 24-58)

### 2.2 Obligation Moods (Deontic Modality)

| Value | Description | Frequency | TBTA Code | Key Markers |
|-------|-------------|-----------|-----------|-------------|
| **'must' Obligation** | Strong necessity, mandates | 1.58% | f | δεῖ (dei) + infinitive |
| **'should' Obligation** | Moderate advice, recommendations | 0.32% | g | χρή (chre) + infinitive |
| **Forbidden Obligation** | Strong prohibition ("must not") | 0.63% | i | μή + aorist subjunctive |
| **'should not' Obligation** | Negative advice | 0.32% | h | μή + present imperative |
| **'may' (permissive)** | Permission granted | <0.1% | l | ἔξεστι (exesti) |

**Obligation Strength Continuum**:
```
Strong Positive: 'must' (δεῖ) → Moderate: 'should' (χρή) → Permission: 'may' (ἔξεστι)
Strong Negative: Forbidden (μή + aorist subj) → Moderate: 'should not' (μή + pres imp)
```

{mood-archive-detailed} Source: `/bible-study-tools/tbta/features/features-archive/mood/DETAILED-RULES.md` (lines 60-203)

### 2.3 Potential Moods (Epistemic Modality)

| Value | Description | Frequency | TBTA Code | Key Markers |
|-------|-------------|-----------|-----------|-------------|
| **Definite Potential** | Certain capability | <0.1% | a | Demonstrated ability |
| **Probable Potential** | Likely outcome | <0.1% | b | Evidence-based probability |
| **'might' Potential** | Possible but uncertain | 2.53% | c | δύναμαι, ἴσως, τάχα |
| **Unlikely Potential** | Doubtful | Rare | d | Greek optative (remote) |
| **Impossible Potential** | Cannot occur | Rare | e | Negated capability |
| **'might not' Potential** | Negative possibility | Rare | j | Negated 'might' |

**Epistemic Certainty Continuum**:
```
Definite (a) → Probable (b) → 'might' (c) → Unlikely (d) → Impossible (e)
```

{mood-archive-detailed} Source: `/bible-study-tools/tbta/features/features-archive/mood/DETAILED-RULES.md` (lines 205-265)
{mood-archive-learnings} Source: `/bible-study-tools/tbta/features/features-archive/mood/LEARNINGS.md` (lines 42-65)

### 2.4 Traditional Grammatical Moods

| Value | Description | TBTA Mapping | Greek Morphology |
|-------|-------------|--------------|------------------|
| **Subjunctive** | Hypothetical, conditional, dependent | Often → c ('might') or context-dependent | υποτακτική |
| **Optative** | Wishes, prayers, remote possibilities | → d (Unlikely) or c ('might') | ευκτική (rare in Koine) |
| **Imperative** | Commands, requests | → f ('must') or g ('should') based on strength | προστακτική |

**Note**: TBTA does not preserve morphological mood categories directly, but maps them to semantic modal values based on contextual meaning.

{mood-archive-detailed} Source: `/bible-study-tools/tbta/features/features-archive/mood/DETAILED-RULES.md` (lines 267-329)

---

## 3. Gateway Features & Constraints

**Gateway Features**: Mood interacts with other TBTA features in a dependency hierarchy.

### 3.1 Controlling Features

**Part of Speech** → Mood
- Mood only applies to **verbs** (and verbal constructions)
- Nouns, adjectives, adverbs do not receive mood annotations

**Clause Type** → Mood Interpretation
- Independent clauses: Indicative, Imperative most common
- Subordinate clauses: Subjunctive, conditional more likely
- Purpose clauses (ἵνα + subj): Often → obligation or potential
- Conditional clauses: Determines factual vs. hypothetical interpretation

{mood-archive-detailed} Source: `/bible-study-tools/tbta/features/features-archive/mood/DETAILED-RULES.md` (lines 362-371)

### 3.2 Dependent Features

**Mood** → **Aspect**
- Some moods favor certain aspects
- Indicative: Compatible with all aspects (perfective, imperfective, progressive)
- Imperative/Obligation: Often imperfective (ongoing requirement)
- Potential: Often future-oriented aspects

**Mood** → **Time**
- Indicative: All time values possible (present, past, future)
- Obligation: Typically future-oriented (Immediate Future, Later Today)
- Potential: Future or hypothetical time frames

**Mood** + **Polarity** → Obligation Type
- Affirmative + 'must' = Strong positive obligation
- Negative + 'must' = Forbidden Obligation
- Affirmative + 'should' = Moderate advice
- Negative + 'should' = 'should not' Obligation

{mood-archive-detailed} Source: `/bible-study-tools/tbta/features/features-archive/mood/DETAILED-RULES.md` (lines 331-389)
{mood-archive-learnings} Source: `/bible-study-tools/tbta/features/features-archive/mood/LEARNINGS.md` (lines 84-94)

---

## 4. TBTA Labeling Policy

### 4.1 Semantic vs. Morphological Priority

**TBTA prioritizes semantic meaning over morphological form.**

**Example: Greek Subjunctive**
- **Morphology**: Subjunctive mood (υποτακτική)
- **Semantic Mapping**: Depends on construction
  - Conditional protasis (ἐάν + subj) → c ('might' Potential)
  - Purpose clause (ἵνα + subj) → Varies by strength (f, g, or c)
  - Prohibition (μή + aorist subj) → i (Forbidden Obligation)
  - Deliberative question (τί ποιήσω;) → c ('might' Potential)

**Rationale**: Target languages do not necessarily have subjunctive morphology, but they DO express the semantic distinctions (possibility, obligation, condition). Semantic annotation enables cross-linguistic transfer.

{mood-archive-learnings} Source: `/bible-study-tools/tbta/features/features-archive/mood/LEARNINGS.md` (lines 9-18, 23-39)

### 4.2 Multi-Level Analysis Process

TBTA uses a **four-stage annotation process** for mood:

**Stage 1: Source Language Morphology**
- Extract Greek/Hebrew mood markers
- Greek: Indicative, Subjunctive, Optative, Imperative
- Hebrew: Jussive, Cohortative, modal particles

**Stage 2: Semantic Mapping**
- Map morphology to semantic modal values
- Apply epistemic/deontic strength gradation
- Consider modal auxiliaries (δεῖ, χρή, δύναμαι)

**Stage 3: Contextual Refinement**
- Analyze discourse structure (genre, clause type)
- Speaker authority (divine command → stronger obligation)
- Pragmatic force (rhetorical questions, indirect commands)

**Stage 4: Target Language Validation**
- Verify annotation transfers to diverse target languages
- Test on mood-rich languages (Turkish, Japanese) and modal-verb languages (English, German)

{mood-archive-learnings} Source: `/bible-study-tools/tbta/features/features-archive/mood/LEARNINGS.md` (lines 22-80)

### 4.3 Edge Case Handling

#### Case 1: Interrogative Indicative
**Pattern**: Questions with indicative mood
**Example**: "Do you not see all these things?" (οὐ βλέπετε ταῦτα πάντα;)
- IlLocutionary Force: Interrogative
- Mood: **Indicative** (asking about factual observation)
- **Key Insight**: IlLocutionary Force and Mood are separate dimensions

{mood-archive-detailed} Source: `/bible-study-tools/tbta/features/features-archive/mood/DETAILED-RULES.md` (lines 407-420)

#### Case 2: Embedded Moods
**Pattern**: Infinitive clauses inheriting mood from parent verb
**Example**: δεῖ ἀκοῦσαι "it is necessary to hear"
- Parent: δεῖ (modal auxiliary → 'must')
- Embedded: ἀκοῦσαι (infinitive "to hear")
- **Result**: 'must' Obligation applies to "hear"

{mood-archive-detailed} Source: `/bible-study-tools/tbta/features/features-archive/mood/DETAILED-RULES.md` (lines 436-442)

#### Case 3: Rhetorical Questions
**Pattern**: Interrogative form with imperatival force
**Example**: "Should we not obey God?"
- Syntactic: Question
- Pragmatic: Functions as obligation (expects "yes")
- **Resolution**: Analyze rhetorical function, not just syntax

{mood-archive-detailed} Source: `/bible-study-tools/tbta/features/features-archive/mood/DETAILED-RULES.md` (lines 431-434)

#### Case 4: Indirect Commands
**Pattern**: Indicative form with imperatival force
**Example**: "You will go to Jerusalem" (prediction OR command)
- Check IlLocutionary Force
- Speaker authority (prophet, divine voice → command more likely)
- **Resolution**: Context determines interpretation

{mood-archive-detailed} Source: `/bible-study-tools/tbta/features/features-archive/mood/DETAILED-RULES.md` (lines 425-429)

---

## 5. Past Learnings & Best Practices

### 5.1 Core Principles

**Principle 1: Morphology + Context + Discourse**
- No single level determines mood annotation
- Must consider: morphological form, lexical auxiliaries, syntactic structure, contextual adverbs, discourse genre
- All levels analyzed together

**Principle 2: Gateway Features Most Reliable**
High-confidence triggers (with confidence levels):
1. Greek Imperative morphology → Imperative (99%)
2. δεῖ (dei) + infinitive → 'must' Obligation (95%)
3. χρή (chre) + infinitive → 'should' Obligation (90%)
4. ἔξεστι (exesti) → 'may' Permissive (95%)
5. δύναμαι (dunamai) → 'might' Potential (85%)
6. μή + aorist subjunctive → Forbidden Obligation (95%)
7. Indicative morphology + no modals → Indicative (90%)

**Principle 3: Default to Indicative**
- 94.62% of verbs are Indicative (based on Matthew 24 test data)
- When ambiguous, predict Indicative (safest baseline)
- Only override with strong contextual evidence

**Principle 4: Obligation Strength Continuum**
Context modulates strength:
- **Authority of speaker**: Divine command → stronger obligation
- **Urgency**: Life-or-death situations → 'must' not 'should'
- **Negation**: Affects strength and type

{mood-archive-learnings} Source: `/bible-study-tools/tbta/features/features-archive/mood/LEARNINGS.md` (lines 82-122)

### 5.2 Common Annotation Errors

**Error 1: Confused Potential Strength**
- Symptom: Predicted 'might' when actual was 'probable' (or vice versa)
- Cause: Missed contextual likelihood markers
- Fix: Check for adverbs (ἴσως "perhaps", τάχα "possibly")

**Error 2: Missed Obligation in Embedded Clause**
- Symptom: Predicted Indicative, actual was 'must' Obligation
- Cause: Obligation expressed through parent clause modal
- Fix: Check parent clause for δεῖ even when analyzing embedded infinitives

**Error 3: Wrong Obligation Strength**
- Symptom: Predicted 'must' when actual was 'should'
- Cause: Misidentified strength of modal auxiliary
- Fix: δεῖ = strong ('must'), χρή = weak ('should')

**Error 4: Prohibition vs Negation**
- Symptom: Predicted Indicative with negation, actual was Forbidden
- Cause: Did not recognize μή + subjunctive as prohibition
- Fix: μή (not οὐ) + subjunctive = prohibition structure

{mood-archive-learnings} Source: `/bible-study-tools/tbta/features/features-archive/mood/LEARNINGS.md` (lines 124-146)

---

## 6. Mixed Annotations

**Mixed annotations**: Can constituents receive multiple mood values simultaneously?

**Answer**: **Generally NO** for mood feature.

Unlike features like Degree (which allows "Intensified" + "'too'" combined), mood is typically a **single-valued feature**. A verb receives one primary mood annotation.

**Exception**: Ambiguous constructions where multiple interpretations are valid may be annotated with the primary interpretation and secondary possibilities noted in alternative analysis fields.

{stage-1-instructions} Source: `/bible-study-tools/tbta/features/.instructions-to-build-feature/STAGE-1-RESEARCH.md` (lines 54-55)
{mood-archive-readme} Note: Matthew 24 test data shows no instances of mixed mood annotations

---

## 7. Statistical Profile (Test Data)

**Test Corpus**: Matthew 24 (51 verses, 316 verbs)

| Mood Type | Count | Percentage | Confidence Level |
|-----------|-------|------------|------------------|
| Indicative | 299 | 94.62% | HIGH (90%+) |
| 'might' Potential | 8 | 2.53% | MEDIUM (75-90%) |
| 'must' Obligation | 5 | 1.58% | MEDIUM (75-90%) |
| Forbidden Obligation | 2 | 0.63% | HIGH (90%+) |
| 'should' Obligation | 1 | 0.32% | LOW (<75%) |
| 'should not' Obligation | 1 | 0.32% | LOW (<75%) |
| **TOTAL** | **316** | **100%** | - |

**Key Findings**:
- Indicative dominates Biblical narrative (94.62%)
- Modal meanings constitute only 5.38% of verbs
- Within modal verbs: Potential (2.53%) slightly exceeds Obligation (2.85%)
- Rare values (<0.1%): 'may' Permissive, Probable Potential, Definite Potential

**Implications**:
- Indicative is the safe default prediction
- Modal distinctions are rare but **critically important** when present
- Obligation and potential moods carry significant semantic weight despite low frequency

{mood-archive-readme} Source: `/bible-study-tools/tbta/features/features-archive/mood/README.md` (lines 18-37)
{mood-archive-learnings} Source: `/bible-study-tools/tbta/features/features-archive/mood/LEARNINGS.md` (lines 178-193)

---

## 8. Theoretical vs. Productive Values

### 8.1 Productive Values (Attested in Data)

**High frequency** (>1%):
- Indicative (94.62%)
- 'might' Potential (2.53%)
- 'must' Obligation (1.58%)

**Low frequency** (<1%):
- Forbidden Obligation (0.63%)
- 'should' Obligation (0.32%)
- 'should not' Obligation (0.32%)

**Rare** (<0.1%, attested but uncommon):
- 'may' Permissive
- Probable Potential
- Definite Potential

### 8.2 Theoretically Possible but Rare

**Greek Optative**: Rare in Koine Greek (common in Classical)
- Wishes: γένοιτο "may it be"
- Remote possibility
- Maps to: d (Unlikely Potential) or c ('might')

**Complex Modal Stacks**: Multiple modals in sequence
- Example: "might be able to" (epistemic + dynamic)
- TBTA would encode the dominant semantic force

{mood-archive-detailed} Source: `/bible-study-tools/tbta/features/features-archive/mood/DETAILED-RULES.md` (lines 287-304)

---

## 9. Source Language Encoding

### 9.1 Greek Morphology

**Explicitly Encoded in Morphology**: YES

Greek verbs have distinct morphological forms for mood:

| Greek Mood | Name | Markers | TBTA Mapping |
|------------|------|---------|--------------|
| Indicative | οριστική | Specific endings per tense | → I (Indicative) |
| Subjunctive | υποτακτική | Vowel lengthening (ω, η) | → Context-dependent (c, f, i) |
| Optative | ευκτική | -οιμι, -οις, -οι endings | → d or c |
| Imperative | προστακτική | Distinct imperative endings | → f or g (by strength) |

**Modal Auxiliaries** (lexical, not morphological):
- δεῖ (dei) "it is necessary" → f ('must')
- χρή (chre) "it is fitting" → g ('should')
- ἔξεστι (exesti) "it is permitted" → l ('may')
- δύναμαι (dunamai) "I am able" → c ('might')

{mood-archive-detailed} Source: `/bible-study-tools/tbta/features/features-archive/mood/DETAILED-RULES.md` (lines 30-42, 66-106)
{mood-archive-learnings} Source: `/bible-study-tools/tbta/features/features-archive/mood/LEARNINGS.md` (lines 30-35)

### 9.2 Hebrew Equivalents

**Partially Encoded in Morphology**

Hebrew has fewer morphological mood distinctions than Greek:

| Hebrew Form | Function | TBTA Mapping |
|-------------|----------|--------------|
| Qatal (Perfect) | Completed/factual actions | → I (Indicative) |
| Wayyiqtol | Narrative past sequence | → I (Indicative) |
| Yiqtol | Context-dependent (future, modal) | → Varies (I or modal) |
| Imperative | Commands (2nd person) | → f or g |
| Jussive | Exhortations (3rd person) | → f or g |
| Cohortative | 1st person exhortations | → g ('should') |

**Modal Particles** (lexical):
- אָבָה (abah) "be willing" → volition
- יָכֹל (yakhol) "be able" → capability → c ('might')
- לֹא (lo) + imperfect → strong prohibition → i (Forbidden)

**Note**: Hebrew modality is more context-dependent and less morphologically explicit than Greek.

{mood-archive-detailed} Source: `/bible-study-tools/tbta/features/features-archive/mood/DETAILED-RULES.md` (lines 39-42, 76-83, 140-143)
{mood-archive-learnings} Source: `/bible-study-tools/tbta/features/features-archive/mood/LEARNINGS.md` (lines 36-38)

---

## 10. Discrepancies & Open Questions

### 10.1 Morphology vs. Semantics

**Discrepancy**: Greek subjunctive morphology does not map to a single TBTA mood value.
- Conditional subjunctive → c ('might' Potential)
- Prohibition subjunctive → i (Forbidden Obligation)
- Hortatory subjunctive → g ('should' Obligation)
- Purpose subjunctive → Varies by context

**Resolution**: TBTA prioritizes **semantic function** over **morphological form**. This is intentional to enable cross-linguistic transfer.

### 10.2 Modal Strength Gradation

**Open Question**: How to consistently assign 6 levels of epistemic potential and 4 levels of deontic obligation?

**Current Approach**:
- Lexical strength ratings for modal expressions (δεῖ vs. χρή)
- Contextual modulation (negation, conditional embedding)
- Genre conventions (prophetic certainty vs. wisdom probability)

**Challenge**: Inter-annotator agreement on fine-grained distinctions (e.g., Probable vs. 'might')

**Future Work**: Quantitative confidence models, expanded test corpus beyond Matthew 24

{mood-archive-learnings} Source: `/bible-study-tools/tbta/features/features-archive/mood/LEARNINGS.md` (lines 217-228)

### 10.3 Subjunctive vs. Indicative in Conditionals

**Open Question**: How to handle Greek conditional constructions?

**Hypothesis**:
- First-class conditions (εἰ + indicative) → Indicative (factual assumption)
- Third-class conditions (ἐάν + subjunctive) → Subjunctive/Potential (hypothetical)

**Future Validation**: Annotate conditional clauses across full corpus; validate with target language conditional forms

{mood-archive-learnings} Source: `/bible-study-tools/tbta/features/features-archive/mood/LEARNINGS.md` (lines 230-237)

---

## 11. Summary

**Mood** is a **Tier A essential feature** in TBTA, affecting translation into 1000+ languages. TBTA encodes **11 distinct mood values** spanning:
- **Factual** (Indicative, 94.62%)
- **Deontic** (5 obligation/permission types, 2.85%)
- **Epistemic** (6 potential/certainty types, 2.53%)

**Key Characteristics**:
- **Semantic priority**: Annotation reflects meaning, not just morphology
- **Multi-level analysis**: Morphology, lexicon, syntax, context, discourse all considered
- **Default to Indicative**: Safe baseline given 94.62% frequency
- **Modal auxiliaries**: Primary triggers for obligation/potential (δεῖ, χρή, ἔξεστι, δύναμαι)
- **Prohibition structures**: μή + aorist subjunctive → Forbidden; μή + present imperative → 'should not'

**Source Language Encoding**:
- **Greek**: Explicitly morphological (4 mood forms) + lexical modal auxiliaries
- **Hebrew**: Partially morphological (imperative, jussive, cohortative) + context-dependent

**Data Quality**: High confidence (90%+) for Indicative, Forbidden, and strong modals; medium confidence (75-90%) for strength gradations.

**Documentation Sources**: Fully documented in archived feature files with test data from Matthew 24 (316 verbs, 51 verses).

---

**Document Status**: Complete
**Primary Sources**: TBTA archived mood documentation, TBTA-FEATURES.md
**Test Data**: Matthew 24 (316 verbs, 51 verses)
**Last Updated**: 2025-11-26
=======
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
>>>>>>> origin/feat/self-learning-tbta
