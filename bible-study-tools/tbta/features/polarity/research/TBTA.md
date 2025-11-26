# TBTA Documentation: Polarity Feature

**Research Date**: 2025-11-26
**Feature Name**: Polarity
**TBTA Classification**: Tier A (Nouns), Tier B (Verbs)
**Source**: TBTA database export and internal documentation

---

## 1. Feature Definition

**Polarity** distinguishes between affirmative (positive) and negative statements or constituents. {TBTA-FEATURES.md}

**Conceptual Definition**: Not explicitly defined in TBTA documentation beyond the feature name and value labels. {TBTA-FEATURES.md}

The feature appears in two contexts:
- **Noun Polarity** (Tier A, Feature #6): Essential feature affecting 1000+ languages {TBTA-FEATURES.md}
- **Verb Polarity** (Tier B, Feature #29): Important but sometimes inferable from context {TBTA-FEATURES.md}

---

## 2. Supported Values

### 2.1 Noun Polarity Values

**Position 7 in 10-position Noun code** {DATA-STRUCTURE.md}

| Code | Value | Description |
|------|-------|-------------|
| A | Affirmative | Positive/non-negated noun {DATA-STRUCTURE.md} |
| N | Negative | Negated noun {DATA-STRUCTURE.md} |

**Example Languages**: Turkish, Finnish, Russian {TBTA-FEATURES.md}

### 2.2 Verb Polarity Values

**Position 4 in 9-position Verb code** {DATA-STRUCTURE.md}

| Code | Value | Description |
|------|-------|-------------|
| A | Affirmative | Positive/non-negated verb {DATA-STRUCTURE.md} |
| N | Negative | Negated verb {DATA-STRUCTURE.md} |
| E | Emphatic Affirmative | Emphatic positive (verbs only) {DATA-STRUCTURE.md} |

**Note**: Emphatic affirmative (E) is documented only for verbs, not nouns. {DATA-STRUCTURE.md}

---

## 3. Gateway Features

**Noun Polarity** is controlled by:
- **Part of Speech**: Must be a Noun (or noun-related constituent in NP) {DATA-STRUCTURE.md}
- Part of **Tier A Essential Features** (Category 1: Nouns) {TBTA-FEATURES.md}

**Verb Polarity** is controlled by:
- **Part of Speech**: Must be a Verb {DATA-STRUCTURE.md}
- Part of **Tier B Important Features** (Category 2: Verbs) {TBTA-FEATURES.md}

**No documented mood/aspect dependencies**: Unlike some features (e.g., Aspect requires Mood=Indicative), polarity does not appear to have documented gateway constraints beyond Part of Speech. {TBTA-FEATURES.md}

---

## 4. Labeling Policy

### 4.1 Semantic vs. Morphological Approach

**Not explicitly documented** in available TBTA source files. {All TBTA source files reviewed}

The documentation does not specify whether TBTA:
- Encodes morphological negation markers (e.g., Hebrew לא *lo*, Greek οὐ *ou*)
- Encodes semantic negation (meaning-level negation)
- Follows different rules for different negation types

### 4.2 Noun vs. Verb Policy Differences

**Documented difference**: Verbs have an additional "Emphatic Affirmative" (E) value not available for nouns. {DATA-STRUCTURE.md}

**No other policy differences documented** in available sources.

### 4.3 Affirmative vs. Unmarked

The documentation does not clarify whether:
- All non-negated constituents are marked "Affirmative" (A)
- "Affirmative" is reserved for emphatic or explicit positive polarity
- Default/unmarked polarity receives a specific code

---

## 5. TBTA Data Examples

### 5.1 Genesis 1:1 - Affirmative Verb Example

```json
{
  "Constituent": "create",
  "Part": "Verb",
  "Time": "Historic Past",
  "Aspect": "Inceptive",
  "Mood": "Indicative",
  "Polarity": "Affirmative"
}
```

**Source**: {DATA-STRUCTURE.md, Genesis 1:1 parsing example}

**Interpretation**: The verb "create" is marked as affirmative (non-negated). This is the only concrete polarity example provided in TBTA documentation.

### 5.2 Other Examples

**No negative polarity examples** are provided in the reviewed TBTA documentation. {All TBTA source files}

**No emphatic affirmative examples** are provided in the reviewed TBTA documentation. {All TBTA source files}

---

## 6. Edge Cases

### 6.1 Documented Edge Cases

**None found** in TBTA source documentation. {All TBTA source files reviewed}

Specific questions not addressed:
- How are rhetorical questions with implied negatives handled?
- How are double negatives (negative concord) encoded?
- How is negation scope handled across coordinated constituents?
- Are negative polarity items (NPIs like "anyone", "ever") marked?
- How are prohibitions vs. simple negations distinguished?

### 6.2 Potential Edge Cases (Inferred from Linguistic Literature)

The following edge cases are **not documented in TBTA** but are known challenges in negation annotation:

**Question Negation**: (not documented)
- Questions expecting negative answers (e.g., "Isn't God merciful?" expects "Yes")
- Questions expecting positive answers
- Rhetorical questions with implied negation

**Double Negatives**: (not documented)
- Negative concord (multiple negatives = single negation)
- Litotes (double negative = emphatic positive)

**Scope Ambiguity**: (not documented)
- "Not all disciples understood" (partial negation)
- "All disciples did not understand" (total negation)

**Prohibitions**: (not documented)
- Hebrew אַל (*al*) vs. לא (*lo*) negation
- Greek μή (*mē*) subjunctive prohibitions vs. οὐ (*ou*) indicative negations

---

## 7. Value Inventory

### 7.1 Theoretically Possible Values

Based on TBTA schema documentation:

**Nouns**: 2 values
- A (Affirmative)
- N (Negative)

**Verbs**: 3 values
- A (Affirmative)
- N (Negative)
- E (Emphatic Affirmative)

### 7.2 Attested vs. Rare Values

**No frequency data provided** in TBTA documentation. {All TBTA source files}

The CRITIQUE.md notes that TBTA includes some theoretical categories rarely used in practice (e.g., "Restaging" participant tracking has 0% usage despite being in schema). {CRITIQUE.md}

**Unknown whether**:
- Emphatic Affirmative (E) is productively used or rare
- Negative (N) appears frequently or primarily on specific constructions
- All verbs/nouns receive explicit polarity encoding or only non-default cases

### 7.3 Missing Values

Values **not in TBTA schema** but present in linguistic literature:
- Emphatic Negative (would parallel Emphatic Affirmative)
- Prohibitive (separate from simple negation)
- Interrogative Negative (questions with negation)
- Double Negative / Negative Concord (multiple negation markers)

---

## 8. Mixed Annotations

**Not documented** whether constituents can receive multiple polarity values simultaneously. {All TBTA source files}

The TBTA-FEATURES.md notes that some features (e.g., Degree) commonly use mixed annotations:
> "Note: Some features commonly use mixed annotations (20+ instances per 100 verses), not just edge cases" {TBTA-FEATURES.md}

**Polarity is not listed** among features that use mixed annotations. {TBTA-FEATURES.md}

**Likely**: Polarity is single-valued (Affirmative XOR Negative XOR Emphatic Affirmative), not multi-valued.

---

## 9. Character Encoding Technical Details

### 9.1 Noun Polarity Encoding

**Position 7 of 10** in noun character string {DATA-STRUCTURE.md}

Complete 10-position noun encoding:
```
Position 1: Gender (M/F/N/C)
Position 2: Number (S/D/T/P)
Position 3: Case (N/A/G/D)
Position 4: NounListIndex (1-9, A-Z, a-z)
Position 5: Participant Tracking (I/D/R)
Position 6: Proximity (S/L/R)
Position 7: Polarity (A/N)          ← POLARITY
Position 8: Participant Status (P/A/M)
Position 9: Surface Realization (N/p/P)
Position 10: Person (1/2/3/A/B)
```

**Source**: {DATA-STRUCTURE.md}

### 9.2 Verb Polarity Encoding

**Position 4 of 9** in verb character string {DATA-STRUCTURE.md}

Complete 9-position verb encoding:
```
Position 1: Time (P/D/h/E, etc.)
Position 2: Aspect (I/C/H/G)
Position 3: Mood (I/a-e/f-i)
Position 4: Polarity (A/N/E)        ← POLARITY
Position 5: Reflexivity (N/R/r)
Position 6: Degree (N/C/S/I)
Position 7-9: Target Features (Aspect/Mood/Tense)
```

**Source**: {DATA-STRUCTURE.md}

### 9.3 JSON Export Format

The TBTA database export expands character codes into readable field names:

```json
{
  "Polarity": "Affirmative"
}
```

or

```json
{
  "Polarity": "Negative"
}
```

**Source**: {DATA-STRUCTURE.md}

---

## 10. Known Limitations and Critiques

### 10.1 Validated Issues from CRITIQUE.md

The CRITIQUE.md document does **not identify any specific issues** with polarity annotation. {CRITIQUE.md}

Issues are documented for:
- Participant Tracking (presupposition conflation, unused "Restaging")
- Verb TAM (imperatives marked "Indicative", aspect overgeneralization)
- Number System (quadrial without evidence, morphological vs. semantic confusion)

**Polarity is not mentioned** in the validated issues list. {CRITIQUE.md}

### 10.2 General TBTA Limitations Affecting Polarity

**Methodological Limitations** that may affect polarity annotation: {CRITIQUE.md}

1. **Undocumented Decision Processes**: "Many annotation decisions lack explicit documentation or algorithms" {CRITIQUE.md}
   - Applies to polarity: No documented algorithm for identifying negative vs. affirmative vs. emphatic

2. **No Confidence Scoring**: "All annotations treated as equally certain" {CRITIQUE.md}
   - Applies to polarity: Semantic negation (implied negatives) may have lower confidence than morphological negation

3. **Single-Pass Annotation**: "No systematic cross-reference validation" {CRITIQUE.md}
   - Applies to polarity: Parallel passages may have inconsistent negation marking

---

## 11. Coverage and Completeness

### 11.1 Feature Status

**Noun Polarity** (Tier A, Feature #6):
- Status: ✅ Complete {TBTA-FEATURES.md}
- Priority: Highest - affects 1000+ languages {TBTA-FEATURES.md}

**Verb Polarity** (Tier B, Feature #29):
- Status: ✅ Complete {TBTA-FEATURES.md}
- Priority: Medium - common but sometimes inferable {TBTA-FEATURES.md}

### 11.2 Biblical Coverage

**11,649 verses** across 34 books (~37% of Bible) {README.md}

**Books included**: {README.md}
- **OT (20 books)**: Genesis, Exodus, Numbers, Deuteronomy, Joshua, Judges, Ruth, 1-2 Samuel, 1 Kings, Jonah, minor prophets
- **NT (14 books)**: Matthew, Mark, Luke, John, Acts, Romans, Galatians, Ephesians, Philippians, Colossians, 1 Thessalonians, Philemon, James, 1-2 Peter

**Focus**: Narrative and discourse-heavy texts where linguistic features matter most {README.md}

---

## 12. Integration Notes

### 12.1 Data Access

**TBTA Repository**: https://github.com/AllTheWord/tbta_db_export {README.md, DATA-STRUCTURE.md}

**File Format**: JSON export from Access database {DATA-STRUCTURE.md}

### 12.2 Old Testament vs. New Testament Structure

**Critical Difference**: {DATA-STRUCTURE.md}
- **OT**: Organized by pericopes (thematic units spanning multiple verses)
- **NT**: Organized by individual verses

**Implication**: OT polarity annotations may span multiple verses in a single pericope entry.

### 12.3 Schema Mapping for myBibleToolbox

Polarity should map to our commentary schema as:

| TBTA Field | myBibleToolbox Schema Section |
|------------|------------------------------|
| Polarity (Noun) | `grammar.morphology.polarity` |
| Polarity (Verb) | `grammar.morphology.polarity` or `grammar.semantics.polarity` |

**Open Question**: Is TBTA polarity morphological (negation markers) or semantic (negated meaning)? Documentation unclear. {All TBTA source files}

---

## 13. Past Learnings

### 13.1 Policy Changes

**No documented policy changes** for polarity feature found in TBTA source files. {All TBTA source files}

### 13.2 Best Practices

**No documented best practices** specific to polarity annotation found in TBTA source files. {All TBTA source files}

The CRITIQUE.md notes general improvements TBTA could make but does not single out polarity for special attention, suggesting the feature is relatively unproblematic in current implementation. {CRITIQUE.md}

---

## 14. Unanswered Questions

Based on this documentation review, the following questions about TBTA's polarity feature remain **unanswered**:

1. **Semantic vs. Morphological**: Does polarity encode surface negation morphemes or semantic negation meaning?

2. **Frequency Distribution**: How often is each polarity value used? Is Emphatic Affirmative (E) productive or rare?

3. **Annotation Protocol**: What algorithm or decision process identifies emphatic affirmative vs. simple affirmative?

4. **Negation Scope**: How is scope of negation handled when one negative marker affects multiple constituents?

5. **Double Negatives**: Are negative concord constructions (multiple negatives = single semantic negation) marked with multiple N values or treated differently?

6. **Prohibitions**: Are Hebrew אַל and Greek μή prohibitions distinguished from simple negations?

7. **Implied Negatives**: Are rhetorical questions with implied negative meaning marked as negative polarity?

8. **Cross-Linguistic Motivation**: Which specific target languages require explicit polarity marking? Why is noun polarity Tier A (essential) while verb polarity is Tier B (important but inferable)?

---

## 15. Summary

### 15.1 What We Know from TBTA Documentation

**Confirmed**:
- Polarity applies to both nouns (Tier A) and verbs (Tier B)
- Values: Affirmative (A), Negative (N), and Emphatic Affirmative (E, verbs only)
- Encoding: Position 7 (nouns), Position 4 (verbs)
- Status: Feature marked "Complete" in TBTA implementation
- Example: Genesis 1:1 "create" marked as "Affirmative"

### 15.2 What We Don't Know from TBTA Documentation

**Missing**:
- Conceptual definition of polarity
- Annotation decision algorithm
- Edge case handling
- Frequency of values in corpus
- Semantic vs. morphological encoding approach
- Justification for why noun polarity is Tier A vs. verb polarity Tier B
- Examples of negative or emphatic affirmative polarity
- Mixed annotation policies
- Cross-linguistic motivation (which languages need this?)

### 15.3 Next Steps for Research

To fully understand polarity for TBTA feature reproduction:

1. **Language Typology**: Research which language families require explicit polarity marking (Stage 1: LANGUAGES.md)
2. **Scholarly Sources**: Study negation typology, negative polarity items, Biblical Hebrew/Greek negation systems (Stage 1: SCHOLARLY.md)
3. **Theological Significance**: Identify non-arbitrary negation contexts (emphatic prohibitions, negated promises) (Stage 1: THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)
4. **Corpus Analysis**: Analyze TBTA database export to determine value frequencies and annotation patterns (Stage 2)
5. **Cross-Linguistic Study**: Build translation database showing how languages encode polarity (Stage 2)

---

**Document Lines**: 349
**Citation Discipline**: All claims cited to source documents
**Unanswered Questions**: 8 major questions requiring further research
**Assessment**: TBTA documentation provides minimal detail on polarity beyond schema structure. Feature is marked "Complete" but lacks conceptual definition, annotation protocol, and linguistic motivation in available documentation.
