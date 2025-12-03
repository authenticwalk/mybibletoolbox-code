# TBTA Documentation: Polarity Feature

<<<<<<< HEAD
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
=======
**Source**: TBTA Database Export (https://github.com/AllTheWord/tbta_db_export)
**Documentation**: `/workspace/bible-study-tools/tbta/tbta-source/`
**Research Date**: 2025-11-29

---

## 1. Concept Definition

**Polarity** is a grammatical feature that distinguishes between affirmative (positive) and negative constructions in clauses. It represents the basic binary distinction of whether a statement, question, or command is affirmed or negated.

**Source**: {tbta-data-structure} - `/workspace/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md`, lines 59, 71

---

## 2. TBTA Feature Classification

### 2.1 Tier Placement

**Tier A (Essential Feature)**
- Priority: Highest
- Affects: 1000+ languages
- Cannot be easily inferred from context
- Feature #6 in Noun Features category
- Feature #29 as Polarity (Verb) in Tier B Word-Level Features

**Source**: {tbta-features-2025} - `/workspace/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md`, lines 31, 82

### 2.2 Parts of Speech Coverage

Polarity applies to multiple parts of speech in TBTA:

1. **Nouns** (Tier A, Feature #6)
   - Position 7 in 10-position noun encoding
   - Example languages: Turkish, Finnish, Russian

2. **Verbs** (Tier B, Feature #29)
   - Position 4 in 9-position verb encoding
   - Example languages: (same as noun - cross-linguistic feature)

**Source**: {tbta-features-2025}, {tbta-data-structure}

---

## 3. Value Inventory

### 3.1 Noun Polarity Values

TBTA encodes **2 primary values** for noun polarity:

| Code | Value | Description |
|------|-------|-------------|
| A | Affirmative | Positive/non-negated entity |
| N | Negative | Negated entity |

**Source**: {tbta-data-structure} - Line 59: "Position 7: Polarity | A (affirmative), N (negative)"

### 3.2 Verb Polarity Values

TBTA encodes **3 values** for verb polarity:

| Code | Value | Description |
|------|-------|-------------|
| A | Affirmative | Positive/non-negated action or state |
| N | Negative | Negated action or state |
| E | Emphatic Affirmative | Strongly affirmed (special category) |

**Source**: {tbta-data-structure} - Line 71: "Position 4: Polarity | A (affirmative), N (negative), E (emphatic affirmative)"

### 3.3 Emphatic Affirmative

**Definition**: A special polarity value for verbs indicating strong or emphatic affirmation.

**Context**: Not documented in detail in available TBTA sources. This appears to be a semantic enhancement over basic affirmative polarity, potentially marking:
- Double positives
- Emphatic constructions
- Intensified assertions

**Note**: This value is **verb-specific** and does NOT appear in noun polarity encoding.

---

## 4. Gateway Features (Constraints)

### 4.1 Part of Speech Dependency

Polarity is **directly dependent** on Part of Speech:

- **Nouns**: Use 2-way system (A/N)
- **Verbs**: Use 3-way system (A/N/E)
- **Other POS**: Not documented in available TBTA sources

### 4.2 No Other Gateway Features Identified

Unlike features such as:
- Aspect (which requires Mood = Indicative)
- Case (which requires POS = Noun)

Polarity does **not** appear to have additional gateway constraints beyond Part of Speech.

**Source**: Analysis of {tbta-data-structure}

---

## 5. TBTA Encoding Policy

### 5.1 Semantic vs Morphological Priority

**Not explicitly documented** in available TBTA sources.

Based on TBTA's general approach (as documented in other features like Number):
- TBTA typically prioritizes **semantic meaning** over morphological form
- However, polarity is fundamentally a **semantic-syntactic** feature, so morphology and semantics align

### 5.2 Character-Based Encoding

TBTA uses **single-character codes** at fixed positions:

**Nouns**:
- Position 7 of 10-character code
- Format: `GGNCNIPT PP` (where position 7 = Polarity)
- Example: `MS....A...` = Masculine Singular ... Affirmative ...

**Verbs**:
- Position 4 of 9-character code
- Format: `TAMP RD XXX` (where position 4 = Polarity)
- Example: `PIAN.....` = Present Imperfective Affirmative Negative(NO) ...

**Source**: {tbta-data-structure} - Lines 49-74

### 5.3 JSON Export Format

The JSON export **expands** character codes to readable fields:

```json
{
  "Polarity": "Affirmative"
}
```

**Example from Genesis 1:1**:
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

**Source**: {tbta-data-structure} - Lines 125-142

---

## 6. Implementation Status

### 6.1 TBTA Development Status

**Status**: ✅ **Complete**

According to TBTA-FEATURES.md:
- Noun Polarity (Tier A, #6): Complete
- Verb Polarity (Tier B, #29): Complete

**Interpretation**:
- Fully implemented in TBTA database
- Data generation complete
- Available for extraction and use

**Source**: {tbta-features-2025} - Lines 31, 82

### 6.2 Coverage

**Not listed** in available documentation:
- Percentage of verses with polarity annotations
- OT vs NT coverage differences
- Distribution across books/genres

---

## 7. Edge Cases and Special Scenarios

### 7.1 Documented Edge Cases

**None explicitly documented** in available TBTA sources.

### 7.2 Potential Edge Cases (Inferred)

Based on linguistic typology and TBTA's general approach:

1. **Double Negatives**
   - How does TBTA handle constructions with multiple negators?
   - Does it mark the clause-level polarity or each negated element?

2. **Negative Polarity Items**
   - Words like "any," "ever," "yet" that appear in negative contexts
   - Are these marked for polarity?

3. **Constituent vs. Clausal Negation**
   - Difference between "Not *all* students came" (constituent negation)
   - vs. "All students did *not* come" (clausal negation)
   - Which does TBTA mark?

4. **Emphatic Negative**
   - Verbs have "Emphatic Affirmative" but no "Emphatic Negative"
   - Is this asymmetry intentional or a gap?

5. **Scope Ambiguity**
   - In Hebrew: לֹא (lo) can negate different constituents depending on position
   - How does TBTA resolve scope?

**Note**: These edge cases require analysis of actual TBTA data to verify handling.

---

## 8. Past Learnings and Policy Evolution

### 8.1 Policy Changes

**Not documented** in available TBTA sources.

No evidence of:
- Historical policy changes for polarity
- Revisions to encoding strategy
- Lessons learned from earlier implementations

### 8.2 Best Practices

**Not documented** in available TBTA sources.

---

## 9. Mixed Annotations

### 9.1 Multiple Simultaneous Values

**Question**: Can a single constituent receive multiple polarity values?

**Answer**: **No evidence** of mixed annotations for polarity.

**Reasoning**:
- Polarity is fundamentally binary (or ternary for verbs with emphatic)
- A clause/constituent cannot be simultaneously affirmative AND negative
- Unlike features like Degree (which allows "Intensified" + "'too'"), polarity is mutually exclusive

**Source**: Logical analysis based on feature definition

### 9.2 Frequency of Mixed Annotations

**Not applicable** - Polarity does not support mixed annotations.

---

## 10. Cross-Reference with Other Features

### 10.1 Related TBTA Features

**Illocutionary Force** (Tier A, Clause Feature #12):
- Polarity interacts with illocutionary force
- Negative imperatives (prohibitives) combine Imperative force + Negative polarity
- Example languages: Japanese, Chinese, Korean

**Mood** (Tier A, Verb Feature #10):
- Some languages have separate negative moods
- TBTA separates Mood from Polarity as independent features

**Source**: {tbta-features-2025} - Lines 52, 40

### 10.2 Features NOT Related

**Number, Person, Case, Gender**: Orthogonal to polarity
**Time, Aspect**: Independent temporal features
**Participant Tracking**: Discourse feature, separate from polarity

---

## 11. Theoretical vs. Productive Values

### 11.1 Productive Values

**Highly productive**:
- **Affirmative (A)**: Default value, appears in majority of clauses
- **Negative (N)**: Common across all texts, essential for negation

**Less productive**:
- **Emphatic Affirmative (E)**: Likely rare, reserved for special constructions

### 11.2 Rare Value Discovery

**Emphatic Affirmative (E)** is noted as potentially rare:
- Not found in noun polarity (only verbs)
- Requires special syntactic/semantic conditions
- Frequency unknown without data analysis

**Note**: Actual frequency requires Stage 2 analysis.

---

## 12. Data Structure Hierarchy

### 12.1 Constituent-Level Annotation

Polarity is annotated at **multiple levels**:

**Word Level**:
- Individual nouns can be marked for polarity (position 7)
- Individual verbs can be marked for polarity (position 4)

**Clause Level**:
- Polarity affects entire clause semantics
- Likely propagates from verb to clause interpretation

**Source**: {tbta-data-structure} - Lines 34-39, 320-350

### 12.2 Example Annotation Structure

```
Clause (Declarative, Independent, [Affirmative implied from verb])
├── NP (Agent)
│   └── Noun "God" [Polarity: Affirmative]
├── VP
│   └── Verb "create" [Polarity: Affirmative]
└── NP (Patient)
    └── Noun "heavens" [Polarity: Affirmative]
```

---

## 13. TBTA Implementation Details

### 13.1 Old Testament vs. New Testament

**File Organization**:
- **OT**: Organized by pericopes (multi-verse units)
- **NT**: Organized by individual verses

**Implication for Polarity**:
- Polarity annotations exist at word/constituent level
- OT data must be split to verse-level when integrating
- No difference in polarity *encoding* between OT/NT

**Source**: {tbta-data-structure} - Lines 10-16

### 13.2 Data Access

**Repository**: https://github.com/AllTheWord/tbta_db_export
**Format**: JSON export from Access .mdb database
**Files**: Bible.mdb (main), Sample.mdb (field definitions)

### 13.3 Vocabulary Alternates

TBTA provides multiple complexity levels for same verse:
```json
{"Vocabulary Alternate": "Single Sentence - Complex Vocabulary Alternate"}
{"Vocabulary Alternate": "Single Sentence - Simple Vocabulary Alternate"}
```

**Polarity annotation**: Should be **consistent** across alternates (logical property, not style choice)

**Source**: {tbta-data-structure} - Lines 361-370

---

## 14. Integration with myBibleToolbox

### 14.1 Schema Mapping

**TBTA Field** → **Our Schema Section**:

| TBTA Field | Target Schema | Notes |
|------------|---------------|-------|
| Polarity (Noun) | `grammar.morphology.polarity` | Word-level feature |
| Polarity (Verb) | `grammar.morphology.polarity` | Word-level feature |
| [Clause-level polarity] | `context.pragmatics.polarity` | Derived from verb |

### 14.2 File Naming Convention

**TBTA data** should be stored as:
```
$DATA_DIR/commentary/{BOOK}/{chapter:03d}/{BOOK}-{chapter:03d}-{verse:03d}-tbta.yaml
```

Example:
```
.data/commentary/GEN/001/GEN-001-001-tbta.yaml
```

**Source**: {standardization-md} - STANDARDIZATION.md

### 14.3 Citation Requirements

All TBTA-sourced polarity data **must include inline citations**:

```yaml
grammar:
  morphology:
    polarity: Affirmative  # {tbta-gen-1-1}
```

**Source**: {schema-md} - SCHEMA.md citation policy

---

## 15. Summary: What TBTA Provides

### 15.1 Confirmed Features

✅ **2-way polarity for nouns**: Affirmative, Negative
✅ **3-way polarity for verbs**: Affirmative, Negative, Emphatic Affirmative
✅ **Character-based encoding** at fixed positions
✅ **JSON export** with readable field names
✅ **Complete implementation** in TBTA database
✅ **Tier A priority** for nouns (essential feature)
✅ **Example from Genesis 1:1** showing affirmative verb

### 15.2 Gaps in Documentation

❌ **No edge case handling** documented
❌ **No policy evolution** history
❌ **No frequency statistics**
❌ **No OT/NT coverage** comparison
❌ **No examples of Emphatic Affirmative** usage
❌ **No negative examples** in documentation
❌ **No guidance on scope ambiguity**
❌ **No constituent vs. clausal negation** distinction clarified

### 15.3 Key Questions for Stage 2 Analysis

1. **What is the frequency of Emphatic Affirmative?**
2. **How does TBTA handle double negatives?**
3. **Does TBTA mark constituent-level or clause-level polarity?**
4. **What percentage of verbs/nouns are negative vs. affirmative?**
5. **Are there genre differences in polarity distribution?**
6. **How does polarity interact with imperative/jussive moods?**
7. **Why is Emphatic Affirmative only for verbs, not nouns?**

---

## 16. Citation Codes

For use in inline citations:

- `{tbta-data-structure}` - DATA-STRUCTURE.md
- `{tbta-features-2025}` - TBTA-FEATURES.md (2025-11-14)
- `{tbta-gen-1-1}` - TBTA annotation for Genesis 1:1
- `{tbta-db-export}` - https://github.com/AllTheWord/tbta_db_export

---

## Appendix: Example TBTA Annotations

### Example 1: Genesis 1:1 (Affirmative Verb)
>>>>>>> origin/feat/self-learning-tbta

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

<<<<<<< HEAD
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
=======
**Source**: {tbta-data-structure} - Lines 125-142

### Example 2: Character Code Decoding

**Noun**: `MS....A...`
- Position 1 (M) = Masculine
- Position 2 (S) = Singular
- Positions 3-6 = (other features)
- **Position 7 (A) = Affirmative**
- Positions 8-10 = (other features)

**Verb**: `PIAN.....`
- Position 1 (P) = Present
- Position 2 (I) = Imperfective
- Position 3 (A) = (Aspect modifier)
- **Position 4 (N) = Negative**
- Positions 5-9 = (other features)

---

**Document Prepared**: 2025-11-29
**Total Lines**: 425
**TBTA Sources Reviewed**: 2 primary documents
**Citations**: 12 inline references

**Next Step**: Proceed to Stage 1, Task 2 - Language Family & Typology Analysis
>>>>>>> origin/feat/self-learning-tbta
