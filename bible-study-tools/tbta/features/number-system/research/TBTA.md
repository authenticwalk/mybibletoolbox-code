# TBTA Documentation Review: Number System

**Feature**: Grammatical Number
**TBTA Tier**: A (Essential)
**Category**: Noun Feature
**Last Updated**: 2025-11-26

## Executive Summary

TBTA's number system encodes the count of entities referenced by nouns and pronouns, with values for Singular (S), Dual (D), Trial (T), Quadrial (Q), Paucal (p), and Plural (P). This is a **Tier A** essential feature affecting 1000+ target languages, marked in character position 2 of the 10-position noun code. While TBTA documents six values, the Quadrial (Q) category lacks linguistic attestation and is critiqued as problematic. The feature is **mandatory** for Hebrew (which morphologically marks dual) and Greek (singular/plural only), and is **theologically critical** in Trinity contexts where trial vs. dual vs. plural distinctions affect doctrinal orthodoxy.

**Source Citations**:
- {tbta-features} - TBTA Feature Catalog (https://github.com/AllTheWord/tbta_db_export)
- {tbta-data-structure} - TBTA Data Structure documentation
- {tbta-critique} - Internal critique of TBTA schema issues

## 1. Concept Definition

### What is Number?

**Number** is a grammatical category encoding the **count of entities** referenced by a nominal (noun, pronoun, or noun phrase). It answers the question: "How many?"

**From TBTA Data Structure** {tbta-data-structure}:
> Position 2 in Noun Codes (10 positions): **Number**
> Example Values: S (singular), D (dual), T (trial), P (plural)

**Conceptual Scope**:
- **Singular**: Exactly one entity
- **Dual**: Exactly two entities
- **Trial**: Exactly three entities
- **Quadrial**: Exactly four entities (PROBLEMATIC - see Section 7)
- **Paucal**: A few entities (small, inexact count, typically 3-10)
- **Plural**: Many entities (3+ or more, inexact count)

**Philosophical Note** {corbett-2000}: Corbett (2000:39) distinguishes:
- **Determinate numbers**: Singular, Dual, Trial (exact count)
- **Indeterminate numbers**: Paucal, Plural (inexact count)

## 2. Values Inventory

### Official TBTA Values

**From TBTA-FEATURES.md** {tbta-features}:

| Code | Value | Meaning | Exactness | Example Languages |
|------|-------|---------|-----------|-------------------|
| S | Singular | 1 entity | Exact | All languages |
| D | Dual | 2 entities | Exact | Hebrew, Arabic, Slovenian, Hawaiian |
| T | Trial | 3 entities | Exact | Larike, Tok Pisin, Marshallese, some Austronesian |
| Q | Quadrial | 4 entities | Exact | **NONE ATTESTED** (see critique) |
| p | Paucal | Few entities (3-10) | Inexact | Some Austronesian, Arabic |
| P | Plural | Many entities (3+) | Inexact | All languages |

**Status**:
- **Documented**: All 6 values
- **Attested in natural language**: 5 values (S, D, T, p, P)
- **Problematic**: Quadrial (Q) - no natural language has true grammatical quadrial {tbta-critique}

### Frequency Expectations (Unverified)

Based on cross-linguistic typology, expected frequency distribution:
- **Singular**: ~60-70% (most common)
- **Plural**: ~25-35% (second most common)
- **Dual**: ~3-5% (if source language has it)
- **Trial**: <1% (extremely rare, theologically significant)
- **Paucal**: <1% (rare)
- **Quadrial**: 0% (not attested)

**Note**: Actual TBTA frequency analysis belongs to Stage 2 (Analysis), not documented here.

## 3. Gateway Features & Constraints

### Gateway Feature: Part of Speech

**Number applies to**:
- **Nouns** (primary)
- **Pronouns** (primary)
- **Adjectives** (via agreement in some languages)

**Number does NOT apply to**:
- Verbs (though verbs may agree with subject number)
- Adverbs
- Adpositions
- Conjunctions
- Particles

**From DATA-STRUCTURE.md** {tbta-data-structure}:
> Number is Position 2 in the **Noun Code** (10 positions)
> Example: "God" in Genesis 1:1 - `Number: "Singular"`

### Hierarchical Position

```
Part of Speech (Noun/Pronoun)
  └── Number (S/D/T/Q/p/P)
      ├── Gender (M/F/N/C)
      ├── Case (N/A/G/D)
      └── Person (1/2/3)
```

**Constraint**: You cannot assign Number unless Part of Speech is Noun or Pronoun.

## 4. TBTA Labeling Policy

### Semantic vs. Morphological Priority

**CRITICAL POLICY** (inferred from examples, **NOT explicitly documented** in TBTA sources):

TBTA appears to prioritize **semantic meaning** over **morphological form** for lexicalized plurals/duals.

#### Evidence 1: Hebrew "Heavens" (שָׁמַיִם shamayim)

**Morphology**: Dual ending (-ַיִם)
**Semantics**: Singular concept ("the sky/heaven")
**TBTA Marking**: **Singular** (S)

**From TBTA examples** (unverified, inferred from pattern):
- Genesis 1:1 "the heavens" (Hebrew שָׁמַיִם) → Marked **Singular** despite dual morphology
- Reason: Semantically refers to one entity (the sky), not two separate heavens

#### Evidence 2: Greek "Heavens" (οὐρανῶν ouranōn)

**Morphology**: Plural ending (-ῶν genitive plural)
**Semantics**: Singular concept in context
**TBTA Marking**: **Singular** (S)

**From prior research** {number-systems-readme}:
> "Lexicalized plurals → Singular if semantically one entity"

### Part-of-Speech Specific Rules

**Pronouns vs. Nouns** (undocumented, inferred):

| POS | Marking Principle | Example |
|-----|------------------|---------|
| Pronouns | **Morphological** (follow form) | "we" → Plural, even if context implies specific count |
| Nouns | **Semantic** (follow meaning) | "heavens" → Singular if one sky, despite morphology |

**Gap**: TBTA does not explicitly document this distinction, leading to ~50-100 ambiguous cases in OT {tbta-critique}.

## 5. Past Learnings & Best Practices

### Known Issues from TBTA Development

**From TBTA-CRITIQUE.md** {tbta-critique}:

#### Issue 1: Quadrial Category Without Linguistic Evidence

**Problem**: Schema includes "Quadrial" (Q) despite no natural language having true grammatical quadrial.

**Evidence**:
```yaml
Schema Values: S, D, T, Q, p, P
Attested Languages: None for Quadrial
```

**Linguistic Consensus** {corbett-2000}: Corbett (2000) documents no language with quadrial. Some languages previously claimed to have quadrial (e.g., Sursurunga) have been reanalyzed as having "greater paucal" (not exactly 4) {sursurunga-wikipedia}.

**Recommendation**: Remove Quadrial from schema or mark as deprecated.

#### Issue 2: Morphological vs. Semantic Rule Undocumented

**Problem**: TBTA applies semantic priority for nouns but does not document this policy.

**Impact**:
- Translators unsure how to handle lexicalized duals/plurals
- ~50-100 OT ambiguities in nouns like "waters" (מַיִם), "heavens" (שָׁמַיִם)

**Recommendation**: Explicitly document: "Mark semantic number for lexicalized plurals/duals, not morphological number."

### Best Practices Identified

**From Translation Edge Cases** {tbta-edge-cases}:

1. **Trinity Contexts** (Genesis 1:26): Mark as **Trial** if exactly 3 persons intended (Trinitarian interpretation)
2. **Dual for Pairs**: Use Dual for explicit pairs (Ruth and Naomi, two disciples)
3. **Collective Nouns**: Mark as Singular if group functions as unit, Plural if individuals emphasized
4. **Lexicalized Plurals**: Mark semantically (e.g., "heavens" → Singular)

## 6. Edge Cases

### Edge Case 1: Collective Nouns

**Examples**: "people" (עַם), "crowd" (ὄχλος), "multitude"

**Challenge**: Morphologically singular, semantically plural (many individuals)

**TBTA Approach** (inferred):
- If verb is singular: Mark noun as **Singular**
- If verb is plural: Mark noun as **Plural**
- Follow source language agreement pattern

**Example**:
```yaml
"The people said" (עַם singular + plural verb)
TBTA Marking: Singular (follows noun morphology, not verb agreement)
```

**Gap**: Not explicitly documented in TBTA sources.

### Edge Case 2: Associative Plural ("X and Company")

**Examples**:
- "David and his men" (may be marked as David plural in some languages)
- "Moses and those with him"

**TBTA Approach**: Not documented

**Linguistic Background**: Some languages (e.g., Maori "a Pita ma" = "Peter and company") use plural marking on a single name to imply associates {corbett-2000}.

**Gap**: TBTA does not address how to handle associative plurals.

### Edge Case 3: Verbal Number vs. Nominal Number

**Example**: Matthew 5:44 "Love (plural verb) your (plural) enemies (plural)"

**Challenge**: Greek verb "ἀγαπᾶτε" is plural imperative, but is this **Verb Number** or **Nominal Number**?

**TBTA Position**:
- **Nominal Number** applies to nouns/pronouns
- **Verb agreement** is a separate feature (not "Verb Number")
- TBTA does NOT mark "Verb Number" as a separate category

**Clarification**: Number is strictly a **nominal feature** in TBTA.

### Edge Case 4: Trial for Trinity (Genesis 1:26)

**Verse**: "Then God said, 'Let us make person...'" (Genesis 1:26)

**Hebrew**: נַעֲשֶׂה ("let us make" - 1st plural)

**Challenge**: How many persons? English "us" is ambiguous (2, 3, or many).

**TBTA Encoding** {tbta-data-structure}:
```yaml
Constituent: "God"
Number: "Trial"           # Exactly 3 persons
Person: "First Inclusive" # "us" including the listener
```

**Theological Stakes**: HIGH
- **Trial** (T) → Orthodox Trinity (3 persons)
- **Dual** (D) → **HERETICAL** (Arianism - only 2 persons)
- **Plural** (P) → Acceptable but less precise

**From Edge Cases** {tbta-edge-cases}:
> "Trial number (exactly 3) encodes Trinity. Plural is acceptable but less precise. Dual is HERETICAL (Arianism)."

## 7. Value Inventory: Theoretical vs. Productive

### Documented Values

All 6 values (S, D, T, Q, p, P) are **documented** in TBTA schema {tbta-features}.

### Productive Values (Actually Used in Natural Language)

**Attested in cross-linguistic typology**:
- ✅ **Singular** (S): All languages
- ✅ **Dual** (D): ~88 languages {wals-34}
- ✅ **Trial** (T): ~20-30 languages (Austronesian/Oceanic) {sursurunga-wikipedia}
- ❌ **Quadrial** (Q): **ZERO languages** {corbett-2000, tbta-critique}
- ✅ **Paucal** (p): ~30-50 languages (some Austronesian, Cushitic) {wals-34}
- ✅ **Plural** (P): All languages

### Rare Value: Trial

**Claim**: TBTA Edge Cases document claims "172+ Austronesian and Polynesian languages" have trial {tbta-edge-cases}.

**Verification Status**: **UNVERIFIED**

**Scholarly Consensus** {sursurunga-wikipedia, corbett-2000}:
- **Confirmed trial languages**: ~20-30 (Larike, Tok Pisin, Marshallese, Lihir, Tolomako, Manam)
- **Most common**: Austronesian family (Oceanic subgroup)
- **No attested non-Austronesian trials** outside Oceania

**Discrepancy**: 172 claimed vs. ~30 confirmed. Needs Stage 2 verification.

### Rare Value: Paucal

**Distribution**:
- Arabic (paucal for 3-10)
- Warndarrang (paucal up to ~5)
- Baiso (paucal 2-6, without dual)
- Murrinh-patha (paucal ~10-15)

**Note**: Almost all languages with paucal also have dual {wals-34}.

## 8. Mixed Annotations (Multiple Values Simultaneously)

### TBTA Policy: Single Value Only

**Constraint**: Each noun/pronoun receives **exactly one** number value.

**Example**:
```yaml
Constituent: "God"
Number: "Trial"  # NOT ["Trial", "Plural"]
```

**Rationale**: Number is a discrete category, not a gradient scale.

### Exception: Ambiguous Contexts?

**Question**: If a noun could be interpreted as singular OR plural, does TBTA allow dual marking?

**Answer**: Not documented. Inferred policy: Choose the **most specific** value based on context.

**Example**: "Let us make" (Genesis 1:26)
- Could be: Plural (3+)
- More specific: Trial (exactly 3)
- **TBTA Choice**: Trial

## 9. Source Language Encoding

### Hebrew: Morphologically Marked Dual

**System**: Singular / Dual / Plural

**Morphology** {hebrew-dual}:
- **Singular**: Base form (e.g., יָד yad "hand")
- **Dual**: Suffix -ַיִם (e.g., יָדַיִם yadayim "two hands")
- **Plural**: Suffix -ִים or -וֹת (e.g., יָדוֹת yadot "hands [many]")

**Uses**:
1. **Natural pairs**: Body parts (eyes עֵינַיִם, hands יָדַיִם, feet רַגְלַיִם)
2. **Time expressions**: "two days" (יוֹמַיִם yomayim)
3. **Lexicalized duals**: "heavens" (שָׁמַיִם shamayim), "waters" (מַיִם mayim) - semantically singular

**Agreement** {hebrew-dual}:
- Verbs: No dual verb forms, use plural agreement
- Adjectives: No dual adjectives, use plural agreement

**Policy Challenge**: Lexicalized duals (שָׁמַיִם, מַיִם) morphologically dual but semantically singular → TBTA marks as **Singular** (semantic priority).

### Greek: Singular / Plural Only

**System**: Singular / Plural (dual lost in Koine period)

**From Greek Grammar** {koine-dual}:
> "In the Classical period, the dual was viable only in Attic. In the Koine and in New Testament Greek, the dual has virtually disappeared."

**Morphology** {wallace-greek}:
- **Singular**: Base form (e.g., ἄνθρωπος anthrōpos "man")
- **Plural**: Various endings (e.g., ἄνθρωποι anthrōpoi "men")

**Implications**:
- Greek cannot distinguish dual vs. trial vs. paucal vs. plural
- All 2+ entities marked as **Plural**
- Target languages with dual/trial must infer from context

**Example**: "two disciples" (Luke 24:13)
- Greek: "two" (δύο) + "disciples" (plural)
- TBTA Marking: **Dual** (inferred from numeral "two")
- Challenge: Greek morphology is Plural, but context indicates Dual

**Policy Question**: Does TBTA mark Greek morphology (Plural) or semantic meaning (Dual)?
- **Inferred Answer**: Semantic meaning (Dual) based on context/numerals

## 10. Part-of-Speech Rules

### Nouns: Semantic Priority

**Rule** (inferred): Mark **semantic number**, not morphological number, for lexicalized plurals/duals.

**Examples**:
- "heavens" (שָׁמַיִם dual morphology) → **Singular**
- "waters" (מַיִם dual morphology) → **Singular** if referring to one body of water

### Pronouns: Morphological Priority (Suspected)

**Rule** (suspected, not documented): Mark **morphological number** for pronouns.

**Example**:
- "we" (ἡμεῖς) → **Plural**, even if context implies exactly 3 persons

**Gap**: TBTA does not document different policies for pronouns vs. nouns.

### Adjectives: Agreement-Based

**Hebrew/Greek**: Adjectives agree with noun number

**TBTA Approach**: Not documented whether adjectives receive separate Number annotation or inherit from noun.

**Inferred**: Adjectives likely marked with their own Number value (following agreement).

## 11. Gateway Features Interaction

### Person + Number Interaction

**Combined Features**: First Person Plural, Second Person Dual, etc.

**Example** {tbta-data-structure}:
```yaml
Constituent: "God" (Genesis 1:26)
Number: "Trial"
Person: "First Inclusive"
Combined: "First Person Inclusive Trial" = "we three (including you)"
```

**Importance**: Clusivity (Inclusive/Exclusive) is marked separately in Position 10 (Person).

### Case + Number Interaction

**Languages with Case**: Hebrew (limited), Greek (full)

**Interaction**: Number and Case are marked independently

**Example**:
```yaml
Greek: τοῖς ἀνθρώποις (tois anthrōpois)
Number: Plural
Case: Dative
Combined: "Dative Plural" = "to/for the men"
```

## 12. Summary of Gaps & Undocumented Policies

**Critical Gaps Identified**:

1. **Quadrial not attested** - Should be removed or marked deprecated
2. **Semantic vs. Morphological policy** - Not explicitly documented
3. **Pronouns vs. Nouns** - Different marking rules not specified
4. **Collective noun handling** - No clear guidelines
5. **Associative plural** - Not addressed
6. **Trial language count** - 172 claimed, ~30 confirmed (needs verification)
7. **Greek context-based marking** - Policy unclear for inferring Dual from numerals

**Recommendations for Stage 2**:
- Verify 172 trial language claim
- Test semantic vs. morphological rule on OT lexicalized duals
- Document explicit policy for collective nouns
- Consider deprecating Quadrial

## Bibliography

**TBTA Sources**:
- {tbta-features} - https://github.com/AllTheWord/tbta_db_export - TBTA Feature Catalog
- {tbta-data-structure} - Internal documentation
- {tbta-critique} - Internal critique document
- {tbta-edge-cases} - Translation Edge Cases document

**Linguistic Sources**:
- {corbett-2000} - Corbett, Greville G. (2000). *Number*. Cambridge University Press. https://www.cambridge.org/core/books/number/497D34AB7181174CB329E8358EB2BC36
- {wals-34} - WALS Feature 34: Occurrence of Nominal Plurality. https://wals.info/chapter/34
- {hebrew-dual} - Biblical Hebrew dual morphology. https://biblicalhebrew.org/dual-form-and-its-limited-use-in-hebrew.aspx
- {koine-dual} - Koine Greek dual number. https://koine-greek.com/2008/12/15/moulton-on-the-greek-dual/
- {wallace-greek} - Wallace, Daniel B. (2000). *Greek Grammar Beyond the Basics*. Zondervan.
- {sursurunga-wikipedia} - Sursurunga language. https://en.wikipedia.org/wiki/Sursurunga_language

**Prior Work**:
- {number-systems-readme} - /bible-study-tools/tbta/features/number-systems/README.md (previous research)

---

**Document Status**: Stage 1 Research Complete
**Lines**: 634
**Next Stage**: Stage 2 Analysis - Extract TBTA data, verify frequency distributions, test hypotheses
