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
