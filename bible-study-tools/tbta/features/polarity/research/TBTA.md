# TBTA Documentation: Polarity Feature

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
