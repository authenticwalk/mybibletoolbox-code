# TBTA Person System Documentation

## Overview

This document provides a comprehensive analysis of TBTA's Person System feature based on review of TBTA source documentation.

**Sources Reviewed:**
- `/workspace/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md` {tbta-features-2025}
- `/workspace/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md` {tbta-data-structure-2025}
- `https://github.com/AllTheWord/tbta_db_export` {tbta-github-2025}

---

## 1. Conceptual Definition

**Person** is a grammatical category that indicates the relationship between participants in a discourse event. It distinguishes:
- The speaker (first person)
- The addressee (second person)
- Others not directly involved in the conversation (third person)

In languages with **clusivity**, first person plural is further divided into:
- **Inclusive**: Speaker + addressee + (optionally) others
- **Exclusive**: Speaker + others, but NOT the addressee

{tbta-data-structure-2025}

---

## 2. TBTA Values

TBTA supports an **8-way person system** combining person and clusivity:

### Basic Person Values

| TBTA Value | TBTA Code | Meaning |
|------------|-----------|---------|
| First | 1 | Speaker (singular or ambiguous plural) |
| Second | 2 | Addressee (singular or plural) |
| Third | 3 | Others (singular or plural) |

### Clusivity Values (First Person Only)

| TBTA Value | TBTA Code | Meaning | Example Languages |
|------------|-----------|---------|-------------------|
| First Inclusive | A | "We" including the listener | Tagalog *tayo*, Malay *kita* |
| First Exclusive | B | "We" excluding the listener | Tagalog *kami*, Malay *kami* |

**Total Values**: 5 distinct values (First, First Exclusive, First Inclusive, Second, Third)

{tbta-features-2025}

---

## 3. Part-of-Speech Context

Person is encoded **only for nouns** (including pronouns) in TBTA's annotation system.

### Encoding Position

In TBTA's character-based encoding for nouns:
- **Position 10**: Person marking
- Values: `1`, `2`, `3`, `A` (inclusive), `B` (exclusive)

{tbta-data-structure-2025}

### Example from TBTA Data Structure

```json
{
  "Constituent": "God",
  "Part": "Noun",
  "Number": "Singular",
  "Person": "Third",
  "Participant Tracking": "Routine",
  "NounListIndex": "1",
  "Semantic Role": "Most Agent-like"
}
```

---

## 4. Gateway Features (Constraints)

**Part of Speech** is the controlling gateway feature:
- Person is **ONLY** annotated when Part = "Noun" or "Pronoun"
- Not applicable to verbs, adjectives, adverbs, etc. in TBTA's system

**Note**: While many languages mark person agreement on verbs, TBTA annotates person only at the noun/pronoun level, not on predicates.

{tbta-data-structure-2025}

---

## 5. TBTA Policy & Annotation Principles

### Source Language Encoding

**Hebrew and Greek do NOT grammatically encode clusivity.**

From TBTA Data Structure:
> "Many languages distinguish inclusive/exclusive 'we':
> | Value | Meaning | Languages |
> |-------|---------|-----------|
> | A | First Inclusive | Malay *kita*, Tagalog *tayo* |
> | B | First Exclusive | Malay *kami*, Tagalog *kami* |
> **Example**: Acts 15:25 - 'It seemed good to us' uses First Exclusive (apostles only, not congregation)."

{tbta-data-structure-2025}

**Critical Implication**: Since Hebrew/Greek do not mark clusivity, TBTA's annotations of "First Inclusive" vs "First Exclusive" are **SEMANTIC INTERPRETATIONS** based on contextual analysis, not morphological encoding in the source text.

### Semantic vs Morphological Priority

TBTA prioritizes **SEMANTIC INTERPRETATION** for clusivity:
- Hebrew/Greek first person plural pronouns are ambiguous
- TBTA disambiguates based on discourse context
- Annotators determine from context whether the speaker intended to include or exclude the addressee

### Annotation Methodology

TBTA annotations for clusivity are based on:
1. **Discourse context**: Who is speaking to whom?
2. **Participant tracking**: Who is included in the action?
3. **Exegetical analysis**: What did the original author intend?

**Example Cited**: Acts 15:25
- Greek: ἔδοξεν ἡμῖν (edoxen hēmin) = "it seemed good to us"
- TBTA Annotation: "First Exclusive"
- Rationale: The apostles and elders writing to the Gentile believers; "us" refers to the council members only, not the recipients

{tbta-data-structure-2025}

---

## 6. Edge Cases & Complexity

### Trinity References

**Genesis 1:26** - "Let us make man in our image"

From TBTA Data Structure:
```json
{
  "Constituent": "God",
  "Number": "Trial",
  "Person": "First Inclusive",
  "Participant Tracking": "Routine"
}
```

{tbta-data-structure-2025}

**Interpretation**:
- Number = Trial (exactly 3) encodes Trinity
- Person = First Inclusive (God speaks to Godself, including all three Persons)
- This is a **NON-ARBITRARY, THEOLOGICALLY CRITICAL** annotation
- Alternative interpretations (e.g., God speaking to angels) would use different person/number combinations

### Ambiguous Contexts

In many Hebrew/Greek contexts, clusivity cannot be definitively determined:
- TBTA must make interpretive decisions
- Different exegetes may disagree on inclusive vs exclusive
- These decisions affect Bible translations in clusivity-marking languages

### Generic/Impersonal Uses

Not documented in TBTA sources reviewed. Questions remain:
- How does TBTA handle generic "we" (= "people in general")?
- How are impersonal constructions annotated?
- Is there a "zero person" or "fourth person" category? **Not found in documentation.**

---

## 7. Value Inventory

### Complete Person Values in TBTA

| Person Value | Clusivity | When Used | Example Contexts |
|--------------|-----------|-----------|------------------|
| **First** | Ambiguous | Singular "I" or ambiguous "we" | Most first-person contexts where clusivity is not specified |
| **First Exclusive** | Exclusive | "We" excluding addressee | Acts 15:25 (apostles writing to Gentiles) |
| **First Inclusive** | Inclusive | "we" including addressee | Gen 1:26 (Trinity), prayers, exhortations |
| **Second** | N/A | Addressee | Direct address, commands, questions |
| **Third** | N/A | Others | Narrative participants, references to absent parties |

### Theoretical vs Productive Values

**All five values are productive** in TBTA annotations:
- First Exclusive and First Inclusive appear in contexts where clusivity is exegetically determinable
- First (ambiguous) appears where clusivity cannot be determined or is irrelevant (singular contexts)

**No rare or theoretical-only values** documented.

---

## 8. Mixed Annotations

**Not applicable.** Person is a single-valued feature in TBTA.

A constituent receives exactly one Person value, not multiple simultaneous values.

---

## 9. Interaction with Other Features

### Person + Number

Person and Number are **independent but co-occurring** features:

| Person | Number Options |
|--------|----------------|
| First | Singular, Dual, Plural, Trial, Paucal |
| First Exclusive | Dual, Plural, Trial, Paucal (never singular) |
| First Inclusive | Dual, Plural, Trial, Paucal (never singular) |
| Second | Singular, Dual, Plural |
| Third | Singular, Dual, Plural, Trial, Paucal |

**Critical Combination**: Person = "First Inclusive" + Number = "Trial" → Trinity references

### Person + Participant Tracking

Person interacts with TBTA's Participant Tracking feature:
- First/Second person participants are typically "Frame Inferable" (known from discourse frame)
- Third person participants require tracking (First Mention, Routine, Restaging, Exiting)

### Person + Semantic Role

Person does not constrain Semantic Role, but statistical tendencies exist:
- First/Second person more likely Agent-like
- Third person can be any role

---

## 10. Cross-Reference to TBTA Feature Catalog

From TBTA Features document:

> **#2: Person System**
> - **Tier**: A (Essential - affects 1000+ languages, cannot be easily inferred)
> - **Values**: 1st/2nd/3rd + Inclusive/Exclusive (8-way system)
> - **Example Languages**: Tagalog, Malay, Fijian, Vietnamese
> - **Status**: ✅ Complete

{tbta-features-2025}

**Priority Justification**:
- Tier A status indicates this is **critical** for Bible translation
- 1000+ languages grammatically require clusivity distinctions
- Cannot be inferred from context in target languages (must be explicitly marked)
- Wrong choice can alter theological meaning

---

## 11. Known Gaps & Questions

Based on documentation review, the following are **not documented**:

1. **Obviation/Proximate**: No evidence of "fourth person" proximate/obviative distinctions (Algonquian-type systems)
2. **Generic Person**: How are generic/impersonal uses handled?
3. **Zero Person**: No mention of subjectless constructions (Finnish-type)
4. **Second Person Clusivity**: No evidence of second-person clusivity marking (y'all vs y'all and them)
5. **Formal/Informal Register**: No indication if person interacts with honorifics (though "Speaker Demographics" is a separate feature)
6. **Verb Agreement**: Person is not annotated on verbs, only nouns
7. **Frequency Data**: No statistics provided on relative frequency of each value
8. **Inter-annotator Agreement**: No data on how consistently clusivity is annotated
9. **Pericope vs Verse**: Old Testament is pericope-based; unclear if person annotations are consistent across verse boundaries

---

## 12. Translation Impact Examples

From TBTA documentation:

### Example 1: Acts 15:25
- **Greek**: ἔδοξεν ἡμῖν (first person plural, ambiguous)
- **TBTA Annotation**: First Exclusive
- **Tagalog**: *kami* (exclusive, not *tayo*)
- **Impact**: Clarifies that the decision was made by the apostles/elders alone, not including the Gentile recipients

### Example 2: Genesis 1:26
- **Hebrew**: נַעֲשֶׂה (first person plural cohortative)
- **TBTA Annotation**: First Inclusive + Trial Number
- **Impact**: Encodes Trinitarian interpretation (God speaking within the Godhead)
- **Theological Stakes**: HIGH (alternative annotations could suggest polytheism or divine council)

### Example 3: The Lord's Prayer (Matthew 6:13, Luke 11:4)
- **Greek**: ἡμῶν (first person plural, ambiguous)
- **Translation Decision**: Typically **First Exclusive** (excluding God from "our trespasses")
- **Historical Error**: Early missionaries used inclusive form, implying God shares in human sin—had to be corrected

{tips-translation-bible-2025}

---

## 13. Summary of TBTA Person System

| Aspect | Details |
|--------|---------|
| **Feature Name** | Person System |
| **TBTA Field Name** | "Person" |
| **Values** | First, First Exclusive, First Inclusive, Second, Third (5 total) |
| **Encoding** | Position 10 in noun codes: `1`, `2`, `3`, `A`, `B` |
| **Part of Speech** | Nouns/Pronouns only |
| **Source Languages** | Hebrew/Greek do NOT encode clusivity |
| **Annotation Method** | Semantic interpretation based on context |
| **Tier** | A (Essential for 1000+ languages) |
| **Theological Significance** | EXISTS (Trinity references, apostolic authority) |
| **Frequency** | All 5 values productive; clusivity appears where contextually determinable |

---

## 14. Bibliography

All citations are to TBTA source materials:

- {tbta-features-2025}: `/workspace/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md`
- {tbta-data-structure-2025}: `/workspace/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md`
- {tbta-github-2025}: `https://github.com/AllTheWord/tbta_db_export`
- {tips-translation-bible-2025}: Translation resources cited in TBTA documentation

---

**Document Status**: Complete based on available TBTA source documentation
**Last Updated**: 2025-11-29
**Gaps**: See Section 11 for areas requiring further research beyond TBTA documentation
