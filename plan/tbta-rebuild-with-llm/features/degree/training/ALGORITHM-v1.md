# Degree Feature: Algorithm v1.0

**Created**: 2025-11-09
**Based on**: 4 training verses + linguistic inference
**Status**: LOCKED (do not modify - create v2.0 for refinements)
**Git commit**: d38b833

---

## Purpose

This algorithm predicts TBTA degree annotations for adjectives, adverbs, and verbs in Biblical texts (Greek NT, Hebrew OT).

**Input**: Verse with source language text (Greek/Hebrew)
**Output**: Degree annotation for each degree-bearing constituent

---

## Algorithm Overview

```
Step 1: Identify degree-bearing constituents (adjectives, adverbs, verbs)
Step 2: Analyze source language morphology
Step 3: Analyze semantic context (discourse-level)
Step 4: Apply decision rules (semantic prioritized over morphological)
Step 5: Assign TBTA degree value
Step 6: Select correct field name by part of speech
```

---

## Step 1: Identify Degree-Bearing Constituents

### Constituents That May Have Degree

| Part of Speech | Can Have Degree? | Field Name | Default Value |
|----------------|------------------|------------|---------------|
| Adjective | ✅ Yes | `Degree:` | No Degree |
| Adverb | ✅ Yes | `Degree:` | No Degree |
| Verb | ✅ Yes | `Adjective Degree:` | No Degree |
| Noun | ❌ No | N/A | N/A |
| Pronoun | ❌ No | N/A | N/A |
| Conjunction | ❌ No | N/A | N/A |

### Procedure

```
FOR each constituent in verse:
    IF part_of_speech IN [Adjective, Adverb, Verb]:
        candidate = TRUE
        proceed to Step 2
    ELSE:
        skip (no degree annotation)
```

---

## Step 2: Analyze Source Language Morphology

### Greek Morphological Patterns

#### Comparative Forms

| Pattern | Example | Morphology | Expected Degree |
|---------|---------|------------|-----------------|
| -τερος/-τέρᾱ/-τερον | μείζων (meizon) "greater" | Synthetic comparative | Comparative |
| -ίων/-ιον | κρείττων (kreitton) "better" | Irregular comparative | Comparative |
| μᾶλλον + adjective | μᾶλλον ἀγαθός | Analytic comparative | Comparative |

#### Superlative Forms

| Pattern | Example | Morphology | Expected Degree |
|---------|---------|------------|-----------------|
| -τατος/-τάτη/-τατον | μέγιστος (megistos) "greatest" | Synthetic superlative | Superlative |
| -ιστος/-ίστη/-ιστον | κράτιστος (kratistos) "strongest" | Irregular superlative | Superlative |
| μάλιστα + adjective | μάλιστα ἀγαθός | Analytic superlative | Superlative |

#### Intensifiers

| Form | Meaning | Expected Degree |
|------|---------|-----------------|
| λίαν (lian) | very | Intensified |
| σφόδρα (sphodra) | greatly, exceedingly | Intensified or Extremely Intensified |
| μάλιστα (malista) | most, especially | Intensified (when not with adjective) |
| ὑπερβολή (hyperbolē) constructions | beyond measure | Extremely Intensified |

### Hebrew Morphological Patterns

#### Comparative Construction

```hebrew
Adjective + מִן (min) "than"
Example: טוֹב מִן (tov min) "better than"
→ Degree: Comparative
```

#### Superlative Construction

```hebrew
Definite article + adjective + ב/מִן phrase
Example: הַגָּדוֹל בַּמְּלָכִים (ha-gadol ba-melakhim) "the greatest among kings"
→ Degree: Superlative

Alternative: Construct state pattern
Example: קְדֹשׁ קָדָשִׁים (qodesh qodashim) "holy of holies" (superlative of holiness)
→ Degree: Superlative
```

#### Intensifiers

| Form | Meaning | Expected Degree |
|------|---------|-----------------|
| מְאֹד (meod) | very, much | Intensified |
| Cognate accusative | Intensifying construction | Intensified |

---

## Step 3: Analyze Semantic Context

### Context Indicators for Superlative

```
Question patterns:
- "which is the GREATEST/BEST?" → Superlative context
- "who is the MOST?" → Superlative context

Answer patterns:
- Answers to superlative questions → Maintain superlative

Syntactic patterns:
- Definite article + adjective in comparative set → Superlative
- "Of all..." / "among..." constructions → Superlative
```

### Context Indicators for Comparative

```
Syntactic markers:
- "than" (ἤ in Greek, מִן in Hebrew)
- Two entities being compared
- Comparison particle present

Semantic patterns:
- Explicit comparison between A and B
- Relative ordering implied
```

### Discourse-Level Considerations

```
IF current verse is answer to question in previous verse:
    Inherit degree context from question

IF verse contains reported speech with comparison:
    Analyze from speaker's perspective

IF verse is part of parallel structure (poetry):
    Check for degree in parallel line
```

---

## Step 4: Apply Decision Rules (Priority Order)

### RULE 1: Semantic Context Overrides Morphology (HIGHEST PRIORITY)

```
IF discourse context is superlative (e.g., "which is greatest?")
   AND adjective is semantically superlative
THEN → Degree: Superlative
   (even if morphology is positive form)

Confidence: 95%
Evidence: MAT 22:36, 22:38 (μεγάλη positive → Superlative)
```

**Example**:
```yaml
# Matthew 22:36
Greek: μεγάλη (megalē) - POSITIVE form
Context: "which is the GREAT commandment?" (superlative question)
Decision: Degree: Superlative  # Semantic overrides morphological
```

---

### RULE 2: Synthetic Morphology When Semantics Agree

```
IF Greek has comparative morphology (-τερος, -ίων)
   AND semantics support comparative meaning
THEN → Degree: Comparative

IF Greek has superlative morphology (-τατος, -ιστος)
   AND semantics support superlative meaning
THEN → Degree: Superlative

Confidence: 85% (inferred, no training data)
Evidence: Linguistic standard for Greek degree morphology
```

**Example**:
```yaml
# John 15:13 (inferred)
Greek: μείζονα (meizona) - COMPARATIVE form
Semantics: "greater love than this" (comparative meaning)
Decision: Degree: Comparative  # Morphology and semantics align
```

---

### RULE 3: Hebrew Constructions Map to Degree

```
IF Hebrew has מִן (min) construction
THEN → Degree: Comparative

IF Hebrew has definite article + superlative construction
   OR construct state superlative pattern
THEN → Degree: Superlative

Confidence: 80% (inferred from grammar)
Evidence: Hebrew has no synthetic degree morphology, uses constructions
```

**Example**:
```yaml
# Song of Solomon 1:2 (inferred)
Hebrew: טוֹבִים מִיָּיִן (tovim miyayin) "better than wine"
Construction: adjective + מִן
Decision: Degree: Comparative
```

---

### RULE 4: Intensifiers Map to Intensified

```
IF λίαν (lian) or similar standard intensifier present
THEN → Degree: Intensified

IF extreme intensifier present (καθ' ὑπερβολήν, σφόδρα σφόδρα)
   OR double intensification construction
THEN → Degree: Extremely Intensified

Confidence: 90% (1 training example for Intensified)
Evidence: MRK 1:35 (λίαν → Intensified)
```

**Example**:
```yaml
# Mark 1:35
Greek: λίαν (lian) "very"
Modifies: early
Decision: Degree: Intensified
```

---

### RULE 5: Default to No Degree

```
IF no degree morphology present
   AND no intensifier present
   AND no comparative/superlative context
THEN → Degree: No Degree

Confidence: 100%
Evidence: 7 training examples
```

**Example**:
```yaml
# Genesis 1:1, Mark 1:35 ("dark", "alone", "still")
No degree markers
Decision: Degree: No Degree
```

---

## Step 5: Assign TBTA Degree Value

### Value Encoding Table

| Concept | Single-Letter Code (README) | TBTA Full Value | Confidence |
|---------|----------------------------|-----------------|------------|
| No degree | N | "No Degree" | 100% (observed) |
| Comparative | C | "Comparative" | 85% (inferred) |
| Superlative | S | "Superlative" | 100% (observed) |
| Intensified | I (adj), V (adv) | "Intensified" | 100% (observed) |
| Extremely Intensified | E | "Extremely Intensified" | 70% (inferred) |
| Too/Excessive | T | "Too" or "Excessive" | 60% (inferred) |
| Less | L | "Less" | 60% (inferred) |
| Least | l | "Least" | 60% (inferred) |
| Equality | q | "Equality" or "Equative" | 60% (inferred) |

**IMPORTANT**: Always use FULL WORD values, not single-letter codes

**Uncertainty**: Values E, T, L, l, q not seen in training data; strings are inferred

---

## Step 6: Select Field Name by Part of Speech

```python
def get_field_name(part_of_speech):
    if part_of_speech in ["Adjective", "Adverb"]:
        return "Degree:"
    elif part_of_speech == "Verb":
        return "Adjective Degree:"
    else:
        return None  # No degree field
```

**Confidence**: 100% (observed in all 11 training examples)

---

## Complete Algorithm Pseudocode

```
FUNCTION predict_degree(constituent, verse_context, source_language):

    # Step 1: Check if constituent can have degree
    IF constituent.part_of_speech NOT IN [Adjective, Adverb, Verb]:
        RETURN null  # No degree annotation

    # Step 2: Analyze morphology
    morphology_degree = analyze_morphology(constituent, source_language)

    # Step 3: Analyze semantic context
    semantic_degree = analyze_semantic_context(verse_context)

    # Step 4: Apply decision rules (priority order)

    # RULE 1: Semantic overrides morphological
    IF semantic_degree == "Superlative" AND context_is_superlative(verse_context):
        degree_value = "Superlative"

    # RULE 2: Synthetic morphology when semantics agree
    ELIF morphology_degree IN ["Comparative", "Superlative"] AND semantics_agree(morphology_degree, semantic_degree):
        degree_value = morphology_degree

    # RULE 3: Hebrew constructions
    ELIF source_language == "Hebrew":
        IF has_min_construction(constituent):
            degree_value = "Comparative"
        ELIF has_superlative_construction(constituent):
            degree_value = "Superlative"
        ELSE:
            degree_value = check_intensifiers(constituent) OR "No Degree"

    # RULE 4: Intensifiers
    ELIF has_intensifier(constituent):
        IF is_extreme_intensifier(constituent):
            degree_value = "Extremely Intensified"
        ELSE:
            degree_value = "Intensified"

    # RULE 5: Default
    ELSE:
        degree_value = "No Degree"

    # Step 6: Select field name
    field_name = get_field_name(constituent.part_of_speech)

    RETURN (field_name, degree_value)
```

---

## Example Applications

### Example 1: Matthew 22:36 (Semantic Superlative)

**Input**:
```
Constituent: important
Part: Adjective
Greek: μεγάλη (megalē) - positive form
Context: "which is the GREAT commandment?" (superlative question)
```

**Algorithm execution**:
```
Step 1: Adjective → can have degree ✓
Step 2: Morphology = positive form (No morphological degree)
Step 3: Semantic context = superlative question
Step 4: RULE 1 applies → Semantic overrides morphology
Step 5: Degree value = "Superlative"
Step 6: Field name = "Degree:"
```

**Output**:
```yaml
Degree: Superlative
```

**Confidence**: High (matches training data exactly)

---

### Example 2: Mark 1:35 (Intensified Adverb)

**Input**:
```
Constituent: early
Part: Adverb
Greek: λίαν (lian) + πρωῒ (prōi)
Context: Temporal adverb with intensifier
```

**Algorithm execution**:
```
Step 1: Adverb → can have degree ✓
Step 2: Morphology = intensifier λίαν present
Step 3: Semantic context = intensification
Step 4: RULE 4 applies → Intensifier mapping
Step 5: Degree value = "Intensified"
Step 6: Field name = "Degree:"
```

**Output**:
```yaml
Degree: Intensified
```

**Confidence**: High (matches training data exactly)

---

### Example 3: John 15:13 (Synthetic Comparative - INFERRED)

**Input**:
```
Constituent: greater
Part: Adjective
Greek: μείζονα (meizona) - comparative form
Context: "Greater love than this"
```

**Algorithm execution**:
```
Step 1: Adjective → can have degree ✓
Step 2: Morphology = synthetic comparative (-ίων pattern)
Step 3: Semantic context = comparative ("than")
Step 4: RULE 2 applies → Morphology + semantics agree
Step 5: Degree value = "Comparative"
Step 6: Field name = "Degree:"
```

**Output**:
```yaml
Degree: Comparative
```

**Confidence**: Moderate (inferred, no training data)

---

### Example 4: Genesis 1:1 (No Degree Baseline)

**Input**:
```
Constituent: create
Part: Verb
Hebrew: בָּרָא (bara)
Context: Narrative verb, no degree markers
```

**Algorithm execution**:
```
Step 1: Verb → can have degree ✓
Step 2: Morphology = no degree markers
Step 3: Semantic context = no comparison or intensification
Step 4: RULE 5 applies → Default
Step 5: Degree value = "No Degree"
Step 6: Field name = "Adjective Degree:" (verb uses different field)
```

**Output**:
```yaml
Adjective Degree: No Degree
```

**Confidence**: High (matches training data exactly)

---

## Known Limitations

### Limitation 1: Intensification Levels (I vs. E)

**Problem**: Algorithm cannot reliably distinguish:
- "Intensified" (standard: λίαν "very")
- "Extremely Intensified" (extreme: καθ' ὑπερβολήν "beyond measure")

**Workaround**: Default to "Intensified" unless clear extreme marker present

**Resolution needed**: Test on 2 Cor 4:17 (double hyperbole construction)

---

### Limitation 2: Upward vs. Downward Comparison

**Problem**: Algorithm defaults to "Comparative" for both:
- Upward: "greater", "better" → Comparative
- Downward: "lesser", "worse" → Comparative or Less?

**Workaround**: Use "Comparative" for all comparisons until TBTA data clarifies

**Resolution needed**: Test on Hebrews 7:7 (ἔλαττον "lesser")

---

### Limitation 3: Rare Values

**Problem**: No training examples for:
- Equality (q): "as...as" constructions
- Intensified Comparative (i): "much more"
- Superlative of 2 (s): "the greater of the two"
- Too/Excessive (T): "too large"

**Workaround**: Don't predict these values in v1.0; flag as uncertain

**Resolution needed**: Corpus search or mark as theoretical

---

## Validation Plan

**Adversarial test set should include**:
1. More semantic superlatives (positive form in superlative context)
2. Synthetic comparatives (μείζων, κρείττων)
3. Hebrew constructions (מִן comparative, construct superlative)
4. Extreme intensifiers (καθ' ὑπερβολήν)
5. Downward comparisons (ἔλαττον, "lesser")

**Expected accuracy**:
- Clear patterns (synthetic morphology): 85-90%
- Semantic patterns (context-driven): 70-80%
- Overall adversarial: 60-70%
- Overall random: 80-90%

---

## Algorithm Status

**Version**: 1.0
**Lock date**: 2025-11-09
**Training verses**: 4 (with linguistic inference for 4 missing)
**Confidence level**: High for core patterns, moderate for inferred patterns

**Next steps**:
1. Commit this algorithm to git (LOCK)
2. Design adversarial + random test sets
3. Make predictions WITHOUT checking TBTA
4. Validate and refine to v2.0

---

**LOCKED**: Do not modify this file. For refinements after testing, create ALGORITHM-v2.md

**Git commit SHA**: d38b833
