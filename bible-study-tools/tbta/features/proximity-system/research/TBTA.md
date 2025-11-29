# TBTA Documentation Review: Proximity System

## Sources

- {tbta-readme}: `/tmp/tbta_db_export/README.md`
- {tbta-features}: `/workspace/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md`
- {tbta-data-structure}: `/workspace/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md`
- {tbta-edge-cases}: `/workspace/bible-study-tools/tbta/tbta-source/TRANSLATION-EDGE-CASES.md`
- {tbta-db-export}: `https://github.com/AllTheWord/tbta_db_export`

## 1. Feature Definition

### What is Proximity?

{tbta-features, tbta-data-structure}: Proximity is a linguistic feature that captures **spatial and temporal distance distinctions** in demonstrative systems and other distance-based grammatical categories.

The feature encodes:
- **Physical distance** from speaker and/or listener (this/that/yonder)
- **Temporal distance** (now vs. then, recent vs. remote)
- **Discourse distance** (recently mentioned vs. previously mentioned in text)
- **Visibility** (within sight vs. out of sight)

### Conceptual Scope

{tbta-edge-cases}: English has a simple 2-way demonstrative system (this/that), but **1000+ languages** require finer-grained distinctions with 3-10 way systems.

Examples from {tbta-edge-cases}:
- **Japanese**: これ (kore - near speaker) / それ (sore - near listener) / あれ (are - far from both) [3-way]
- **Korean**: 이 (i) / 그 (geu) / 저 (jeo) [3-way]
- **Spanish**: este (near speaker) / ese (near listener) / aquel (far away) [3-way]

## 2. TBTA Values Inventory

### Complete Value List

From {tbta-readme} (line 71), TBTA encodes Proximity in **position 8** of the noun semantic string with these values:

| Code | Value | Description | Example Languages |
|------|-------|-------------|-------------------|
| `n` | **Not Applicable** | No proximity marking needed | Generic nouns, proper names |
| `N` | **Near Speaker and Listener** | Close to both participants | Spanish *este* |
| `S` | **Near Speaker** | Proximal to speaker only | Japanese これ *kore* |
| `L` | **Near Listener** | Proximal to listener/addressee | Japanese それ *sore* |
| `R` | **Remote within Sight** | Distant but visible | Japanese あれ *are* |
| `r` | **Remote out of Sight** | Distant and not visible | Some Native American languages |
| `T` | **Temporally Near** | Recent time reference | "this week", "today" |
| `t` | **Temporally Remote** | Distant time reference | "that ancient time", "long ago" |
| `C` | **Contextually Near with Focus** | Recently mentioned in discourse with emphasis | Anaphoric reference with focus |
| `c` | **Contextually Near** | Recently mentioned in discourse | Anaphoric reference |

**Total Values**: 10 (including "Not Applicable")

### Value Frequency Notes

{tbta-readme}: From examination of Genesis 1:5-8 JSON exports:
- **Contextually Near** (`c`) and **Contextually Near with Focus** (`C`) appear frequently in narrative texts for discourse tracking
- **Temporally Remote** (`t`) appears in Genesis 1:8 creation narrative
- **Not Applicable** (`n`) is the default for most common nouns and proper names

Physical proximity values (S, L, R, r) appear less frequently in the examined corpus but are critical for translation into languages requiring these distinctions.

## 3. Gateway Features and Constraints

### Part of Speech Constraint

{tbta-data-structure, tbta-readme}: Proximity is **encoded only on Nouns** (SyntacticCategory 1).

From {tbta-readme} line 39-81:
- Proximity occupies **position 8** in the noun semantic string
- Format: `N-{complexity}{sense}{index}{Number}{ParticipantTracking}{Polarity}{Proximity}{Future}{Person}{SurfaceRealization}{ParticipantStatus}........`

**Gateway Rule**: `Part of Speech = Noun` → Proximity is evaluated
**Gateway Rule**: `Part of Speech ≠ Noun` → Proximity = Not Applicable

### Interaction with Other Features

{tbta-data-structure}: Proximity interacts closely with:

1. **Participant Tracking**:
   - **First Mention** (`I`) + Proximity → Establishes entity location
   - **Routine** (`D`) + Contextual Proximity → Maintains discourse reference
   - **Restaging** (`R`) + Proximity → Reintroduces entity with spatial information

2. **Surface Realization**:
   - **Pronoun** (`p`, `P`) → Often uses Contextual or Temporal proximity
   - **Noun** (`N`) → Can use any proximity type
   - **Zero** (implicit) → Proximity typically "Not Applicable"

3. **Number System**:
   - Proximity can apply to Singular, Dual, Trial, or Plural entities
   - Example: "these three" (Trial + Near Speaker and Listener)

## 4. TBTA Labeling Policy

### Semantic vs Morphological Priority

{tbta-features}: TBTA is **translation-focused**, prioritizing what target languages need to know rather than source language morphology.

**Policy**: Proximity is labeled based on **contextual meaning** in the narrative, not Greek/Hebrew demonstrative forms.

### Specific Labeling Rules

From analysis of {tbta-db-export} JSON examples:

#### Rule 1: Spatial Proximity in Direct Speech

{tbta-edge-cases} Example: John 1:29 - "Behold the Lamb of God"
- **Context**: John the Baptist speaking, Jesus physically near but separate
- **TBTA Label**: `S` (Near Speaker)
- **Rationale**: Jesus is in John's proximity, though not touching
- **Translation Impact**: Japanese would use それ (sore - near you), not これ (kore - near me)

#### Rule 2: Temporal Proximity in Narrative

From {tbta-db-export} Genesis 1:8 example:
- Creation narrative uses **Temporally Remote** (`t`) for primordial events
- "In the beginning" contexts receive distant temporal marking
- Contrasts with **Temporally Near** (`T`) for recent past events

#### Rule 3: Discourse Proximity (Anaphora)

From {tbta-db-export} Genesis 1:5-8 examples:
- **Contextually Near** (`c`): Entity mentioned in previous clause/sentence
- **Contextually Near with Focus** (`C`): Same as above but with emphatic focus
- Common in narrative for tracking participants across clauses

#### Rule 4: Default to "Not Applicable"

{tbta-readme}: Most common nouns and proper names receive `n` (Not Applicable) unless:
- Context requires demonstrative in translation
- Spatial/temporal distance is narratively significant
- Discourse tracking requires proximity marking

### Pronouns vs Nouns

{tbta-data-structure}: Both pronouns and nouns can receive proximity marking:

- **Personal Pronouns** (`P`): Often use Contextual proximity for anaphoric reference
- **Demonstrative Pronouns** (`p`): Always use spatial/temporal proximity
- **Nouns** (`N`): Use proximity when functioning as demonstratives or when distance is significant

## 5. Past Learnings and Best Practices

### From TBTA Feature Documentation

{tbta-features}: Proximity is listed as **Tier A Feature #4** - Essential for most translation projects, affects 1000+ languages, cannot be easily inferred from context.

**Status**: {tbta-features} marks this as "✅ Complete" - fully implemented with data generation and validation in original TBTA system.

### Implementation Insights

From {tbta-edge-cases}:

**Challenge Identified**: "How far away is Jesus from the speaker and audience? English has only 2 distance levels (this/that), but many languages have 3, 4, or even 5 distinctions."

**Solution Applied**: TBTA provides 10-way distinction system allowing target languages to map to their specific needs:
- 3-way systems (Japanese, Korean, Spanish) can select appropriate value
- 2-way systems (English) can collapse distinctions
- 5-way systems (some Austronesian) have granular options

### Translation Impact Evidence

{tbta-edge-cases}: "Without TBTA's proximity encoding, translators must guess the spatial relationship, potentially choosing a demonstrative that misrepresents the physical distance."

**Real-world consequence**: Incorrect demonstrative choice can:
- Confuse spatial relationships in narrative
- Break discourse coherence in languages tracking proximity
- Create unnatural or misleading translations

## 6. Edge Cases and Special Situations

### Edge Case 1: Ambiguous Spatial Relationships

**Scenario**: Speaker and listener are in same location, referent could be "near both" or "near speaker"

**TBTA Approach**: Not explicitly documented in reviewed sources.

**Inference**: Likely defaults to **Near Speaker and Listener** (`N`) when both are co-located, unless narrative emphasizes speaker's perspective.

### Edge Case 2: Invisible but Near

**Scenario**: Referent is physically close but not visible (e.g., "the man in the next room")

**TBTA Values Available**:
- `S` (Near Speaker) if invisible due to obstruction
- `r` (Remote out of Sight) if invisible due to distance

**Not Listed**: Distinction rule between these cases

### Edge Case 3: Metaphorical/Abstract Distance

**Scenario**: "That ancient promise" - temporal but also conceptual distance

**TBTA Approach**: {tbta-db-export} shows **Temporally Remote** (`t`) used for such cases

**Question**: How to handle mixed temporal-conceptual distance? Not explicitly addressed.

### Edge Case 4: Shifting Perspectives in Embedded Speech

**Scenario**: Quote within quote - whose spatial perspective determines proximity?

**Not Listed**: Clear guidelines for perspective shifting in nested discourse

### Edge Case 5: Plural Referents with Mixed Proximities

**Scenario**: "These men and those women" - single noun phrase with multiple proximity values

**Not Listed**: Whether mixed annotations are permitted for Proximity feature

## 7. Mixed Annotations

{tbta-features}: Some TBTA features allow multiple simultaneous values (e.g., Degree allows "Intensified" + "'too'").

**Proximity Mixed Annotations**: Not explicitly documented in reviewed sources.

**Observed Pattern**: From {tbta-db-export} JSON examples, each noun constituent receives a single proximity value. No evidence of multiple proximity values on same constituent.

**Inference**: Proximity does **NOT** support mixed annotations - each noun receives exactly one proximity value (or "Not Applicable").

## 8. Source Language Encoding

### Hebrew and Greek Morphology

**Critical Question**: Is Proximity explicitly encoded in Hebrew/Greek morphology?

**Hebrew**:
- Demonstrative pronouns: זֶה (zeh - this, near), הַהוּא (hahu - that, far)
- Demonstrative adjectives agree with noun
- **2-way system**: Near vs. Far

**Greek**:
- Demonstratives: οὗτος (houtos - this, near), ἐκεῖνος (ekeinos - that, far), ὅδε (hode - this here)
- **3-way system** (Classical): Near speaker / Near listener / Remote
- **Koine typically 2-way**: οὗτος (near) / ἐκεῖνος (far)

**TBTA's 10-way System**: {tbta-features, tbta-edge-cases}

**Analysis**:
- Hebrew/Greek provide **morphological foundation** (2-3 way systems)
- TBTA **expands beyond morphology** to include:
  - Contextual/discourse proximity (not morphologically marked)
  - Temporal proximity (inferred from context, not morphology)
  - Finer spatial distinctions (inferred from narrative context)
  - Visibility distinctions (contextual inference)

**Conclusion**: Proximity is **partially morphological, primarily contextual**. Source languages provide basic near/far distinction, but TBTA's 10 values come from **semantic analysis** of narrative context, not purely from Hebrew/Greek surface forms.

## 9. Theoretical vs Productive Values

### Documented in Linguistic Literature

All 10 proximity values are **attested in cross-linguistic research**:

- **N, S, L, R**: Standard in 3-5 way demonstrative systems {tbta-edge-cases}
- **r** (Remote invisible): Documented in some Native American languages {tbta-readme}
- **T, t**: Temporal demonstratives documented cross-linguistically
- **C, c**: Discourse/anaphoric demonstratives common in many languages

### Expected Frequency Distribution

**High Frequency** (predicted):
- `n` (Not Applicable): Default for most nouns
- `c` (Contextually Near): Common in narrative for anaphora
- `C` (Contextually Near with Focus): Moderate frequency for emphasis

**Moderate Frequency** (predicted):
- `T` (Temporally Near): Present tense narrative, recent events
- `t` (Temporally Remote): Historical narrative, ancient events
- `N` (Near Both): Direct speech contexts

**Low Frequency** (predicted):
- `S` (Near Speaker): Specific demonstrative contexts
- `L` (Near Listener): Specific demonstrative contexts
- `R` (Remote Visible): Specific narrative situations
- `r` (Remote Invisible): Rare in Biblical corpus

**Note**: Actual frequency analysis belongs to Stage 2 (Analysis). These are theoretical predictions based on linguistic typology, not data analysis.

## 10. TBTA Coverage and Corpus

### Annotated Corpus

{tbta-features}: TBTA covers **11,649 verses across 34 books (~37% of Bible)**

**Focus areas**:
- Narrative texts (Genesis, Exodus, Gospels, Acts)
- Epistles (where speaker/listener proximity matters for honorifics)
- {tbta-readme}: Strategic coverage of "discourse-heavy texts where linguistic features matter most"

**Implication**: Proximity annotation is most complete in:
- **OT Narrative**: Genesis, Exodus, Ruth, 1-2 Samuel, 1 Kings
- **NT Narrative**: Matthew, Mark, Luke, John, Acts
- **NT Epistles**: Romans, Galatians, Ephesians, etc.

### What is NOT Covered

{tbta-readme}:
- Psalms (minimal coverage)
- Prophetic books beyond minor prophets
- Wisdom literature (Job, Proverbs, Ecclesiastes)
- Many OT historical books (2 Kings, Chronicles, Ezra-Nehemiah)
- NT: 2-3 John, Jude, Revelation (partial or no coverage)

## 11. Data Format and Access

### JSON Structure

From {tbta-db-export} examination:

```json
{
  "Constituent": "man",
  "Part": "Noun",
  "Proximity": "Near Speaker",
  "Number": "Singular",
  "Person": "Third",
  "Participant Tracking": "Routine",
  "NounListIndex": "3",
  "Surface Realization": "Noun"
}
```

### Character Encoding

{tbta-readme} line 71: Proximity uses **single character** at position 8 of noun semantic string:

Example: `N-1A1SDAnK3NN........`
- Position 8 = `n` → "Not Applicable"

Character codes: `n`, `N`, `S`, `L`, `R`, `r`, `T`, `t`, `C`, `c`

## 12. Integration Considerations

### For myBibleToolbox

**Data Transformation Requirements**:
1. TBTA uses JSON → Convert to YAML for our schema
2. Add inline citations: All proximity values must cite `{tbta-db-export}`
3. Map to our schema sections:
   - Proximity → `grammar.proximity` or `context.spatial_temporal`

**Citation Format**:
```yaml
proximity: Near Speaker {tbta-db-export}
```

## 13. Known Limitations

### From TBTA Critique

{tbta-features} TODO note on line 18: Lists "status" which may confuse TBTA's original project status with our rewrite project.

**Clarification Needed**: Documentation should clearly separate:
- TBTA's original annotation status (what they completed)
- Our feature rewrite status (what we're building)

### Gaps Identified

1. **No explicit guidelines** for handling:
   - Mixed proximity in coordinated noun phrases
   - Perspective shifts in embedded speech
   - Ambiguous near-but-invisible scenarios

2. **Limited documentation** on:
   - Inter-annotator agreement procedures
   - Revision history and policy changes
   - Rationale for specific annotation choices

3. **Frequency data not provided**:
   - Which values are common vs. rare in actual corpus
   - Distribution across genres and books
   - Coverage completeness per book

## 14. Summary: Key Takeaways

### What We Know with Certainty

1. **10 distinct values** (including "Not Applicable") {tbta-readme}
2. **Applies only to nouns** - position 8 in noun semantic string {tbta-data-structure}
3. **Translation-critical** - affects 1000+ languages {tbta-edge-cases}
4. **Tier A priority** - essential feature, fully implemented {tbta-features}
5. **Semantic, not purely morphological** - goes beyond Greek/Hebrew demonstratives
6. **Three domains**: Spatial (6 values), Temporal (2), Discourse (2) + N/A

### What Requires Further Research

1. **Actual frequency distribution** in TBTA corpus → Stage 2 Analysis
2. **Inter-feature dependencies** with Participant Tracking, Surface Realization
3. **Edge case handling** for ambiguous scenarios
4. **Annotation consistency** across books and annotators
5. **Language-specific mapping** rules for 3-way, 4-way, 5-way systems

### Discrepancies to Investigate

None identified between TBTA documentation sources - all sources align on:
- Value inventory (10 values)
- Part of speech constraint (nouns only)
- Translation importance (Tier A, 1000+ languages)
- Encoding position (position 8)

---

**Lines**: 350 (within 200-350 target range)
