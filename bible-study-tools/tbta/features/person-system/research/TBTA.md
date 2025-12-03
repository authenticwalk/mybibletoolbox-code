<<<<<<< HEAD
# Person System: TBTA Documentation Review

**Feature**: Person System
**TBTA Classification**: Tier A - Essential (affects 1000+ languages)
**Source**: TBTA Source Documentation (`/bible-study-tools/tbta/tbta-source/*`)
**Review Date**: 2025-11-26

## 1. Feature Definition

### 1.1 Concept

**What is Person System?**

{tbta-source/TBTA-FEATURES.md}: "Person System | 1st/2nd/3rd + Inclusive/Exclusive (8-way system) | Tagalog, Malay, Fijian, Vietnamese | ✅ Complete"

Person System refers to grammatical marking of the relationship between participants in discourse and the speech act itself. Beyond the basic 1st/2nd/3rd person distinctions found in English and Biblical source languages (Hebrew, Aramaic, Greek), many target languages require additional distinctions, particularly **clusivity** (inclusive vs. exclusive first person).

{tbta-source/README.md}: Listed as Tier A Essential feature - "Clusivity (1,000+ languages): Distinguish 'we including you' vs 'we excluding you'"

**Key Distinction - Clusivity**:
- **1st Person Inclusive ("we")**: Speaker + Listener(s) - "you and I/us"
- **1st Person Exclusive ("we")**: Speaker + Others, excluding Listener - "they and I, but not you"
- This distinction is **critical** for Bible translation accuracy in 1,000+ languages

### 1.2 TBTA Schema Location

**Where is it encoded?**

- **Noun/Pronoun feature**: Position 10 in 10-character encoding scheme
- **Applies to**: Pronouns (primarily), nouns with person reference
- **Source**: {tbta-source/DATA-STRUCTURE.md} - Character-based encoding

{tbta-source/DATA-STRUCTURE.md}: "| 10 | Person | 1, 2, 3, A (first inclusive), B (first exclusive) |"

**Related features**:
- Number System (Feature #1) - person interacts with number (singular/plural/dual "we")
- Participant Tracking (Feature #3) - tracks discourse referents
- Honorifics/Register (Tier A) - social dimensions of person reference

## 2. Value Inventory

### 2.1 Complete Value List

{tbta-source/DATA-STRUCTURE.md} Position 10 encoding:

TBTA supports **5 person values**:

| Code | Value | Meaning | Source | Example Languages |
|------|-------|---------|--------|-------------------|
| 1 | First Person (ambiguous) | Speaker / "I, we" | {tbta-source/DATA-STRUCTURE.md} | English, Hebrew, Greek (no clusivity distinction) |
| 2 | Second Person | Listener / "you" | {tbta-source/DATA-STRUCTURE.md} | All languages |
| 3 | Third Person | Other / "he, she, it, they" | {tbta-source/DATA-STRUCTURE.md} | All languages |
| A | First Inclusive | Speaker + Listener(s) / "you and I" | {tbta-source/DATA-STRUCTURE.md} | Tagalog *tayo*, Malay *kita*, Fijian, 1,000+ languages |
| B | First Exclusive | Speaker + Others (not listener) / "they and I, not you" | {tbta-source/DATA-STRUCTURE.md} | Tagalog *kami*, Malay *kami*, Fijian, 1,000+ languages |

{tbta-source/DATA-STRUCTURE.md}:
- "| A | First Inclusive | Malay *kita*, Tagalog *tayo* |"
- "| B | First Exclusive | Malay *kami*, Tagalog *kami* |"
- "| 1 | First (ambiguous) | English 'we' |"

### 2.2 Value Documentation Status

**Fully Documented** (with examples from Scripture):

- **First Person** (1): Universal, used when clusivity is not distinguished
- **Second Person** (2): Universal, straightforward
- **Third Person** (3): Universal, most common
- **First Inclusive** (A): Documented with Genesis 1:26 example
- **First Exclusive** (B): Documented with Acts 15:25 example

{tbta-source/TRANSLATION-EDGE-CASES.md}:
- Genesis 1:26: "Person: 'First Inclusive' # 'us' including the listener"
- Acts 15:25: "Person: 'First Exclusive' # Apostles speaking, congregation listening"

### 2.3 Theoretical vs. Productive Values

**From TBTA documentation**:

| Value | Productive (Expected %) | Languages | Notes |
|-------|------------------------|-----------|-------|
| Third Person (3) | HIGH (60-70%) | All languages | Most common - narrative, references to God, Jesus, others |
| First Person (1) | MEDIUM (15-20%) | All languages | Ambiguous "we/I" in languages without clusivity |
| Second Person (2) | MEDIUM (10-15%) | All languages | Direct address, commands, letters |
| First Inclusive (A) | LOW-MEDIUM (5-10%) | 1,000+ languages | "We" including listener - prayers, inclusive exhortations |
| First Exclusive (B) | LOW (3-5%) | 1,000+ languages | "We" excluding listener - apostles vs. congregation |

**Note**: Values A and B only apply to languages with clusivity distinction. For languages without clusivity (English, Hebrew, Greek), value "1" is used. Actual frequencies to be validated in Stage 2 data analysis.

**Clusivity Scope**: {tbta-source/README.md} - "Clusivity (1,000+ languages)"

## 3. Gateway Features & Constraints

**Controlling Feature**: Part of Speech + Surface Realization

{tbta-source/DATA-STRUCTURE.md}: Person applies to:
- Pronouns (position 10 in encoding) - PRIMARY application
- Nouns with person reference (less common)
- Verbs (agreement in some languages - not directly encoded in TBTA)

**Dependency Rules**:

- Person is **valid** when Part = Pronoun, or when Surface Realization = Pronoun
- Person is **most relevant** for first person contexts (distinguishing inclusive/exclusive)
- Person is **straightforward** for second and third person (no clusivity distinction needed)

**Interaction with Number**:
- Person distinction applies across all number values
- First Inclusive/Exclusive most commonly appears with **plural** number
- Can also appear with **dual** or **trial** number in languages with those distinctions
  - Example: "we two" (dual + inclusive) vs. "we two" (dual + exclusive)

## 4. TBTA Labeling Policy

### 4.1 Semantic vs. Morphological Priority

**TBTA prioritizes SEMANTIC interpretation** for clusivity distinctions.

{tbta-source/TRANSLATION-EDGE-CASES.md}: Acts 15:25 example shows semantic analysis:
- Context: Apostles writing letter to congregation
- English: "It seemed good to us" (ambiguous)
- TBTA: "First Exclusive" (semantic determination based on discourse participants)
- Rationale: "us" = apostles only, not including the congregation being addressed

**Policy**: When source language (Hebrew/Greek) has ambiguous first person, TBTA determines inclusive vs. exclusive based on:
1. **Discourse context**: Who is speaking? Who is listening?
2. **Semantic participants**: Does "we" include the addressee or not?
3. **Theological precision**: Trinity contexts, prayer contexts, apostolic authority

### 4.2 Source Language Encoding

**CRITICAL**: Hebrew, Aramaic, and Greek **DO NOT** grammatically mark clusivity.

- Hebrew: אֲנַחְנוּ (*anachnu*) = "we" (ambiguous)
- Greek: ἡμεῖς (*hēmeis*) = "we" (ambiguous)
- English: "we" (ambiguous)

**Implication**: TBTA's inclusive/exclusive distinction is **INTERPRETIVE**, not morphologically explicit in source texts. This makes it a high-value annotation for translators working in clusivity-marking languages.

### 4.3 Second Person Honorifics

**Note**: TBTA does not encode honorific distinctions in the Person field itself. Honorific person systems (T/V distinction, formal/informal "you") are handled separately by:
- **Speaker Demographics** (Feature #13) - includes "Relationship" and "Attitude"
- **Honorifics/Register** (separate feature) - formal vs. informal address

Examples:
- Spanish: *tú* (informal) vs. *usted* (formal) - both = "2" (Second Person)
- Japanese: *anata* vs. *omae* vs. *kisama* - all = "2" but different registers
- Korean: multiple levels of honorific "you" - all = "2" + Speaker Demographics encoding

## 5. Past Learnings & Best Practices

### 5.1 Clusivity Determination Challenges

**From TBTA documentation review**:

{tbta-source/TRANSLATION-EDGE-CASES.md}: Key insight - "Using the wrong form would incorrectly imply the congregation participated in the apostolic decision-making."

**Challenge**: Determining inclusive vs. exclusive when source language is ambiguous requires:
1. **Exegetical analysis** - Who are the participants in context?
2. **Discourse tracking** - Who is speaker? Who is listener?
3. **Theological precision** - What does the passage intend to communicate?

**Best Practice**: Document reasoning for clusivity assignments, especially in:
- Epistolary literature (Paul's letters - "we" = Paul alone? Paul + co-authors? Paul + readers?)
- Prayer contexts ("Our Father" - inclusive of all believers? or exclusive to disciples present?)
- Apostolic pronouncements (Acts 15 - apostles speaking authoritatively to church)

### 5.2 Trinity Context

{tbta-source/DATA-STRUCTURE.md}: Genesis 1:26 example:
- "Number: 'Trial' # Exactly 3 persons"
- "Person: 'First Inclusive' # 'us' including the listener"

{tbta-source/TRANSLATION-EDGE-CASES.md}: "Maintains Trinity reference in translation."

**Learning**: Person System interacts with Number System in Trinitarian contexts:
- Genesis 1:26 "Let us make" = **Trial Number** + **First Inclusive Person**
- Trial = exactly 3 persons (Trinity)
- First Inclusive = "us" including the addressee (intra-Trinitarian dialogue)

**Question for Stage 2**: Should Trinity contexts be marked as "First Inclusive" (dialogue within Godhead) or treated differently? This requires theological review.

## 6. Edge Cases

### 6.1 Generic "You" (Second Person)

**Edge Case**: Generic second person (English "you know how it is")

- Hebrew: אַתָּה (*attah*) used generically
- Greek: σύ (*sy*) used generically
- Modern English: "you" = generic anyone

**TBTA Handling**: Mark as "2" (Second Person) even when semantically generic. No special encoding for generic vs. specific second person.

### 6.2 Royal "We" (Plural of Majesty)

**Edge Case**: First person plural used by single speaker for majesty/authority

- Example: Ezra 4:18 (Persian king's decree) - "We decree" (one king speaking)
- English royal "we"

**TBTA Handling**: Not explicitly documented. Likely marked as "1" (First Person ambiguous) with context note, OR "B" (First Exclusive) if interpreted as king + court.

**Requires clarification in Stage 2**.

### 6.3 "We" in Epistles (Paul's Letters)

**Edge Case**: Paul's "we" varies by context:
- Paul alone (authorial "we")
- Paul + co-authors (Silas, Timothy)
- Paul + readers (inclusive)
- Paul + other apostles (exclusive of readers)

**Examples**:
- 1 Thessalonians 1:2: "We always thank God" - Paul + co-authors? Or Paul + readers?
- 1 Corinthians 1:23: "We preach Christ crucified" - Paul + apostles (exclusive of Corinthians)
- Romans 8:15: "We cry 'Abba, Father'" - Paul + readers (inclusive)

**TBTA Handling**: Each instance requires contextual analysis. See Acts 15:25 as documented example of exclusive determination.

### 6.4 Prophetic "I" (God Speaking)

**Edge Case**: First person singular in prophetic oracles

- "I am the LORD" (Isaiah 45:5) - God speaking
- "I will make you fruitful" (Genesis 17:6) - God speaking to Abraham

**TBTA Handling**: Mark as "1" (First Person). No special encoding for divine vs. human first person. Context identifies speaker as God.

### 6.5 Zero Pronouns (Pro-drop Languages)

**Edge Case**: Languages with null subjects (Greek, Hebrew, Spanish, Italian)

- Greek: ἔρχομαι (*erchomai*) = "I come" (no explicit "I" pronoun)
- Hebrew: בָּאתִי (*ba'ti*) = "I came" (person marked on verb, no separate pronoun)

**TBTA Handling**: Person marked on verb morphology, not requiring explicit pronoun. Surface Realization would indicate "Zero" but person value still assigned.

## 7. Value Inventory Summary

### 7.1 Complete List of Attested Values

From {tbta-source/DATA-STRUCTURE.md} and {tbta-source/TBTA-FEATURES.md}:

**Primary Values** (Universal):
1. **First Person** (Code: 1) - "I, we" (ambiguous clusivity)
2. **Second Person** (Code: 2) - "you" (singular or plural)
3. **Third Person** (Code: 3) - "he, she, it, they"

**Clusivity Values** (1,000+ languages):
4. **First Inclusive** (Code: A) - "we including you"
5. **First Exclusive** (Code: B) - "we excluding you"

**Total**: 5 person values (3 universal + 2 clusivity)

**Note**: TBTA does not encode:
- Obviative/Proximate distinctions (Algonquian languages)
- Fourth person (Algonquian, Navajo)
- Logophoric pronouns (some African languages)
- Honorific person levels (handled by Speaker Demographics feature)

### 7.2 Rare Values Not in TBTA

**From linguistic literature** (not in TBTA encoding):

- **Obviative** (4th person): Algonquian languages distinguish "3rd person proximate" vs. "3rd person obviative" for disambiguation in narrative
- **Logophoric**: West African languages use special 3rd person for reported speech contexts
- **Clusivity in 2nd Person**: Some languages distinguish "you (including others)" vs. "you (alone)" - rare, not in TBTA

**Rationale for exclusion**: These are extremely rare or handled by other TBTA features (Participant Tracking for obviative function).

## 8. Mixed Annotations

**Can a constituent receive multiple person values simultaneously?**

**NO**. Person is a single-valued feature. A pronoun cannot be simultaneously "1st person" and "2nd person."

**However**, person **interacts** with other features:
- **Person + Number**: "we" (1st plural) vs. "I" (1st singular)
- **Person + Clusivity**: "we inclusive" vs. "we exclusive"
- **Person + Honorifics**: "you formal" vs. "you informal" (encoded via Speaker Demographics, not Person field)

**Clusivity is not a separate feature** - it's encoded within the Person field itself (codes A and B).

## 9. Theological Stakes

### 9.1 High-Stakes Contexts

**Trinity References**:
- Genesis 1:26, 3:22, 11:7: "Let us" - First person plural in divine speech
- Isaiah 6:8: "Who will go for us?" - Mixed singular/plural
- {tbta-source/DATA-STRUCTURE.md}: Genesis 1:26 marked as "First Inclusive"

**Clusivity in Prayer**:
- "Our Father" (Matthew 6:9) - Inclusive or exclusive?
  - If inclusive: "Our Father" = disciples + listeners (all believers)
  - If exclusive: "Our Father" = disciples only (Jesus teaching them)
  - **Likely inclusive** - prayer for all

**Apostolic Authority**:
- {tbta-source/TRANSLATION-EDGE-CASES.md}: Acts 15:25 - "First Exclusive"
- Epistles: Distinguishing Paul's authority claims (exclusive) vs. shared Christian experience (inclusive)

### 9.2 Translation Impact

**Critical**: Wrong clusivity = wrong theology

{tbta-source/TRANSLATION-EDGE-CASES.md}:
- Acts 15:25 example: "Using the wrong form would incorrectly imply the congregation participated in the apostolic decision-making."
- Genesis 1:26 example: "Maintains Trinity reference in translation."

**Affected languages**: Tagalog, Malay, Indonesian, Filipino languages, Austronesian, many Native American languages, Papua New Guinea languages

**Percentage of Bible affected**:
- {tbta-source/README.md}: "1,000+ languages" require clusivity distinction
- Estimated 5-15% of verses contain first person plural references requiring clusivity determination

## 10. Summary

**Person System in TBTA**:
- **Tier A Essential** feature (#2 of 59 total features)
- **5 values**: 1st, 2nd, 3rd, 1st Inclusive, 1st Exclusive
- **8-way system** reference in TBTA-FEATURES.md likely refers to: 1st/2nd/3rd × Singular/Plural + Clusivity distinction (not 8 separate person codes, but interaction with number)
- **Position 10** in noun/pronoun encoding
- **1,000+ languages** require clusivity marking
- **Interpretive feature**: Source languages (Hebrew/Greek) don't mark clusivity morphologically
- **High theological stakes**: Trinity contexts, prayer contexts, apostolic authority
- **Status**: ✅ Complete (TBTA has annotated this feature)

**Key Sources**:
- {tbta-source/TBTA-FEATURES.md} - Feature catalog and status
- {tbta-source/DATA-STRUCTURE.md} - Encoding scheme and examples
- {tbta-source/TRANSLATION-EDGE-CASES.md} - Genesis 1:26 and Acts 15:25 examples
- {tbta-source/README.md} - Clusivity scope (1,000+ languages)

**Next Steps** (Stage 2):
1. Validate clusivity assignments in key verses (Genesis 1:26, Acts 15:25, epistles)
2. Determine frequency distribution of person values in TBTA data
3. Create decision tree for inclusive vs. exclusive determination
4. Theological review of Trinity contexts (inclusive vs. other interpretation)
5. Compile list of all first-person plural verses requiring clusivity annotation
=======
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
>>>>>>> origin/feat/self-learning-tbta
