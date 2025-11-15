# Mood Feature Learnings

**Source**: Migrated from `/plan/tbta-rebuild-with-llm/features/verb-tam/LEARNINGS.md`

This document consolidates learnings from the Verb TAM research that are specifically relevant to Mood prediction.

---

## Core Challenge: Language-Neutral Semantic Representation

Biblical source texts (Hebrew OT, Greek NT) must be annotated with mood features that:

1. **Capture source language semantics** accurately
2. **Enable transfer** to 7,000+ target languages with diverse modal systems
3. **Preserve discourse structure** and pragmatic meaning
4. **Is computationally tractable** for automatic generation

This requires creating a **language-neutral semantic representation** that abstracts from source morphology while preserving meaningful distinctions.

---

## Four-Stage Annotation Process (Mood-Specific)

### Stage 1: Source Language Analysis

**Input**: Raw Greek/Hebrew verb form in context

**Process**: Extract morphological mood markers

**Greek Morphology**:
- Indicative mood (οριστική) → I (Indicative) - assertion of fact
- Subjunctive (υποτακτική) → often epistemic potential (c 'might')
- Optative (ευκτική) → wishes, remote possibility (d Unlikely or c Might)
- Imperative (προστακτική) → commands (f 'must' or g 'should')

**Hebrew Equivalents**:
- Jussive/Cohortative → strong obligation (f or g)
- Modal particles (אָבָה, יָכֹל) → various modal strengths

### Stage 2: Semantic Mapping

**Epistemic Strength Gradation**:

| Context Clues | TBTA Code | Strength |
|---------------|-----------|----------|
| "Certainly, definitely, must be" | a | Definite Potential |
| "Probably, likely" | b | Probable Potential |
| "Perhaps, might, could" | c | 'might' Potential |
| "Might not, perhaps not" | j | 'might not' Potential |
| "Unlikely, doubtful" | d | Unlikely Potential |
| "Cannot, impossible" | e | Impossible Potential |

**Deontic Strength Gradation**:

| Context Clues | TBTA Code | Strength |
|---------------|-----------|----------|
| "Must, have to, required" | f | 'must' Obligation |
| "Should, ought to" | g | 'should' Obligation |
| "Should not, ought not" | h | 'should not' Obligation |
| "Must not, forbidden" | i | Forbidden Obligation |
| "May, allowed, permitted" | l | 'may' Permissive |

### Stage 3: Contextual Refinement

**Discourse Structure**:
- **Legal texts**: Deontic modality (obligations, prohibitions)
- **Prophetic texts**: Complex modal distinctions (certain vs. conditional futures)
- **Wisdom literature**: Extensive use of recommendations (g 'should')
- **Narrative**: Primarily indicative with occasional potential

**Genre Conventions**:
- Historical narrative: Favor Indicative
- Teaching: Mix of obligation and potential moods
- Apocalyptic: Strong epistemic distinctions

### Stage 4: Target Language Validation

**Test Cases**: Turkish, Japanese, Arabic (mood-rich), English, German (modal-verb)

---

## Key Principles for Mood Annotation

### Principle 1: Morphology + Context + Discourse

No single level determines annotation:
- **Morphological**: Greek/Hebrew mood forms
- **Lexical**: Modal auxiliaries (δεῖ, χρή, ἔξεστι, δύναμαι)
- **Syntactic**: Clause structure, negation patterns
- **Contextual**: Adverbs, speech acts, authority
- **Discourse**: Genre, narrative role

All must be considered together.

### Principle 2: Gateway Features Most Reliable

High-confidence triggers (in order):

1. **Greek Imperative morphology** → Imperative (99% confidence)
2. **Modal particles**:
   - δεῖ (dei) + infinitive → 'must' Obligation (95%)
   - χρή (chre) + infinitive → 'should' Obligation (90%)
   - ἔξεστι (exesti) → 'may' Permissive (95%)
   - δύναμαι (dunamai) → 'might' Potential (85%)
3. **Prohibition structures**:
   - μή + aorist subjunctive → Forbidden Obligation (95%)
   - μή + present imperative → 'should not' Obligation (90%)
4. **Indicative morphology** + no modals → Indicative (90%)

### Principle 3: Default to Indicative

- 94.62% of verbs are Indicative
- When ambiguous, predict Indicative (safest baseline)
- Only override with strong contextual evidence

### Principle 4: Obligation Strength Continuum

Context modulates strength:
- **Authority of speaker**: Divine command → stronger obligation
- **Urgency**: Life-or-death → 'must' not 'should'
- **Negation**: Affects strength and type (forbidden vs advised against)

---

## Common Errors and Solutions

### Error 1: Confused Potential Strength
**Symptom**: Predicted 'might' when actual was 'probable' (or vice versa)
**Cause**: Missed contextual likelihood markers
**Fix**: Check for adverbs (ἴσως "perhaps", τάχα "possibly")

### Error 2: Missed Obligation in Embedded Clause
**Symptom**: Predicted Indicative, actual was 'must' Obligation
**Cause**: Obligation expressed through parent clause modal auxiliary
**Fix**: Check parent clause for δεῖ even when analyzing embedded infinitives

### Error 3: Wrong Obligation Strength
**Symptom**: Predicted 'must' when actual was 'should'
**Cause**: Misidentified strength of modal auxiliary
**Fix**: δεῖ = strong ('must'), χρή = weak ('should')

### Error 4: Prohibition vs Negation
**Symptom**: Predicted Indicative with negation, actual was Forbidden
**Cause**: Did not recognize μή + subjunctive as prohibition
**Fix**: μή (not οὐ) + subjunctive = prohibition structure

---

## Decision Trees

### Mood Feature Decision Tree

```
What is the source mood?
├─ Indicative
│  └─ → I (Indicative)
├─ Subjunctive
│  ├─ In conditional protasis? → c ('might' Potential)
│  ├─ Deliberative question? → c ('might' Potential)
│  ├─ Hortatory ("let us")? → g ('should' Obligation)
│  └─ Purpose clause? → depends on strength
├─ Optative
│  ├─ Wish? → d (Unlikely) or c ('might')
│  └─ Potential? → c or d
└─ Imperative
   ├─ Strong command? → f ('must' Obligation)
   ├─ Moderate command? → g ('should' Obligation)
   ├─ Prohibition? → h ('should not') or i (Forbidden)
   └─ Permission? → l ('may' Permissive)

Also check:
- Modal verbs/particles in clause
- Authority of speaker (divine → stronger)
- Context (legal → deontic, reasoning → epistemic)
- Negation (affects strength and type)
```

---

## Statistical Summary (Matthew 24)

From analysis of Matthew 24 TBTA data (316 verbs, 51 verses):

| Mood Type | Count | % | Confidence |
|-----------|-------|---|------------|
| Indicative | 299 | 94.62% | HIGH (90%+) |
| 'must' Obligation | 5 | 1.58% | MEDIUM (75-90%) |
| 'might' Potential | 8 | 2.53% | MEDIUM (75-90%) |
| 'should' Obligation | 1 | 0.32% | LOW (<75%) |
| 'should not' Obligation | 1 | 0.32% | LOW (<75%) |
| Forbidden Obligation | 2 | 0.63% | HIGH (90%+) |

**Key Finding**: Indicative dominates Biblical narrative. Other moods rare and context-specific.

---

## Resources Needed for Mood Reproduction

### Linguistic Databases

1. **Morphologically parsed texts**:
   - OpenText.org (Greek NT)
   - ETCBC database (Hebrew Bible)

2. **Lexicons with modal semantics**:
   - BDAG (Greek) - modal verb entries
   - BDB, HALOT (Hebrew) - modal particles
   - Augment with modal strength ratings

3. **Discourse-annotated corpora**:
   - Genre labels (narrative, prophecy, law, wisdom)
   - Speech act annotations
   - Authority/participant tracking

---

## Open Questions

### Question 1: Modal Strength Gradation

**Issue**: How to consistently assign 6 levels of potential and 4 levels of obligation?

**Hypothesis**: Requires:
- Lexical strength ratings for modal expressions
- Contextual modulation (negation, conditional embedding)
- Genre conventions (prophetic certainty vs wisdom probability)

**Test**: Inter-annotator agreement on modal strength; correlation with translations

### Question 2: Subjunctive vs Indicative in Conditionals

**Issue**: Greek uses both in conditional clauses

**Hypothesis**:
- First-class conditions (εἰ + indicative) → Indicative (factual)
- Third-class conditions (ἐάν + subjunctive) → Subjunctive/Potential (hypothetical)

**Test**: Annotate conditional clauses; validate with target language conditionals

---

## Validation Metrics

To evaluate mood annotation quality:

1. **Inter-annotator agreement**: Cohen's kappa, Krippendorff's alpha
2. **Consistency**: Same construction → same mood code
3. **Coverage**: All verbs annotated
4. **Transfer adequacy**: Translations rated by native speakers
5. **Typological validity**: Codes align with cross-linguistic modal patterns

---

## Next Steps

1. **Expand test corpus**: Beyond Matthew 24 to full Gospels
2. **Test across genres**: Legal (Leviticus), Wisdom (Proverbs), Epistles (Romans)
3. **Build confidence models**: Quantitative confidence per mood type
4. **Create transfer matrices**: Target language mapping guides
5. **Validate with real translators**: 2-3 languages per modal system type

---

**Document Source**: Combined from verb-tam/LEARNINGS.md (mood-specific sections)
**Last Updated**: 2025-11-15
**Status**: Migrated to mood feature directory
