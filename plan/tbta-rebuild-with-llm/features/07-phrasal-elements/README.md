# Phrasal Elements (TBTA Category 7)

**Translation Impact:** Phrasal elements identify multi-word expressions where meaning is non-compositional (whole > sum of parts). Word-by-word translation of "stiff-necked people" or "son of man" produces nonsense or theological error in most languages. This feature prevents translation disasters by marking idioms, titles, and compound expressions requiring unified treatment, helping translators choose appropriate equivalents, functional descriptions, or cultural adaptations.

**Key principle**: Breaking apart phrasal elements destroys meaning or creates theological errors.

**Target Audience:** Bible translators working with languages that handle idioms and compound expressions differently from source languages.

---

## Complete Value Enumeration

| Type | Function | Compositionality | Example | Translation Strategy |
|------|----------|-----------------|---------|---------------------|
| **Divine Name** | theological_statement | non-compositional | "I am who I am" | Preserve philosophical depth; may require explanatory phrase |
| **Messianic Title** | self_designation | context-dependent | "Son of Man" | Maintain theological weight; clarify generic vs messianic |
| **Cultural Idiom** | metaphor | non-compositional | "stiff-necked people" | Use functional equivalent or cultural adaptation |
| **Compound Expression** | compound | partially-compositional | "give thanks" | May be single word in target; check compounding patterns |
| **Theological Expression** | wordplay | non-compositional | "born again/from above" | Preserve theological meaning; footnote for wordplay |
| **Formulaic Expression** | formula | non-compositional | "grace and peace to you" | Recognize as greeting formula; use cultural equivalent |
| **Body-Part Metaphor** | metaphor | non-compositional | "hardness of heart" | Replace with target culture metaphor for stubbornness |

---

## Baseline Statistics

Expected distribution in Biblical text:

**Overall occurrence**: ~5-8% of multi-word sequences are phrasal elements
- **Narrative**: ~4-6% (fewer idioms, some titles)
- **Prophetic/Poetic**: ~10-15% (extensive metaphors and cultural idioms)
- **Epistles**: ~6-8% (theological terms and formulaic expressions)
- **Gospels**: ~8-10% (messianic titles, Jesus's teaching idioms)

**By type**:
- Cultural Idiom: ~35% (body-part metaphors, cultural expressions)
- Theological Expression: ~25% (spiritual concepts, technical terms)
- Messianic Title: ~15% (Son of Man, Lord, Christ titles)
- Divine Name: ~10% (I AM, Lord of Hosts, etc.)
- Compound Expression: ~10% (fixed collocations)
- Formulaic Expression: ~5% (greetings, blessings)

**Prediction confidence**:
- High confidence (95%+): Divine names, well-known titles
- Medium confidence (80-90%): Common cultural idioms
- Lower confidence (70-80%): Context-dependent phrases

---

## Quick Translator Test

Answer these questions about your target language:

1. ☐ Does your language use the same body-part metaphors as Hebrew/Greek (e.g., "heart" for emotions, "neck" for stubbornness)?
2. ☐ Can your language translate "son of man" literally and preserve both generic and messianic meanings?
3. ☐ Does your language form compound verbs differently than Greek (e.g., "give thanks" = one word or two)?
4. ☐ Are divine names in your culture typically philosophical statements or simple titles?
5. ☐ Does your language require gender-specific forms for titles like "son of man"?

**Interpretation**:
- If NO to #1: You need cultural adaptation for body-part metaphors (high priority)
- If NO to #2: Mark "son of man" contexts carefully; may need different translations
- If YES to #3: Phrasal element analysis critical for compound expressions
- If NO to #4: "I am who I am" may need adaptation to cultural divine name patterns
- If YES to #5: Gender implications affect messianic title translation

**High Priority Languages**: East Asian (different metaphorical systems), Austronesian (different compounding patterns), African languages (different body-part metaphors)

---

## Examples

**Divine Name**: "I am who I am" (Exodus 3:14) - Philosophical statement; tautological structure difficult in many languages. **Messianic Title**: "Son of Man" - Context-dependent (generic vs messianic); gender implications vary. **Cultural Idiom**: "Stiff-necked people" - Body metaphor for stubbornness; meaningless literal. **Theological**: "Born again/from above" - Greek wordplay (ἄνωθεν = again/from above). **NOT phrasal**: "The big house" - Compositional (big + house = predictable).

[Read detailed examples with full reasoning →](examples.md)

---

## Hierarchical Prediction Method (3-Level Decision Tree)

**Level 1: Source Text Analysis** (30-second scan)
- Scan for: fixed collocations, divine names/titles, body-part metaphors, formulaic expressions
- Decision: Continue to Level 2 if candidates found

**Level 2: Translation Pattern Validation** (2-3 minutes)
- Check 3-5 translations: Do they treat as unit or word-by-word? Any functional equivalents?
- Decision: If 80%+ treat as unit or use functional equivalents → Continue to Level 3

**Level 3: Discourse Context & Final Prediction** (1-2 minutes)
- Consider: Genre, Speaker, Theological weight
- Is phrase non-compositional? What translation challenge does literal rendering create?
- **Output**: YES/NO/UNCERTAIN with type, confidence, reason, translation challenge

**Decision matrix**: High theological weight + fixed collocation + divine/theological = Phrasal (95%+). Word-by-word works + no theology = NOT phrasal.

[Read complete prediction methodology →](prediction-methodology.md)

---

## Gateway Features & Correlations

**Primary: Semantic Domains (90%+ correlation)**
- Phrasal elements cluster in specific domains: Divine names → Domain 12 (Supernatural), Body metaphors → Domain 26 (Psychological)
- Usage: Check semantic domain to validate phrasal element type

**Secondary: Discourse Genre (80%+)** - Prophetic/Poetic has 2-3x more phrasal elements than narrative

**Moderate: Speaker Identity (70%+)** - God as speaker → More divine names/formulaic expressions

**Weak: Participant Tracking (60%)** - Divine names often at First Mention; titles at Restaging

**Cross-validation**: If phrasal BUT generic semantic domain → Flag for review

---

## Common Prediction Errors

1. **Over-predicting theological significance** (Most common): Marking "eternal life" as phrasal when it's compositional. Solution: Apply strict compositionality test.

2. **Missing cultural idioms**: Not recognizing "uncircumcised ears" as Hebrew idiom. Solution: Study source culture metaphors; check translations.

3. **Context-insensitive**: Marking "son of man" same way in all contexts (generic vs messianic). Solution: Check genre, speaker, theological weight.

4. **Ignoring translation patterns**: Predicting based on theology alone. Solution: Always check 3-5 translations for functional equivalents.

5. **Confusing ellipsis with phrasal**: Marking "Jesus wept" as phrasal. Solution: Short ≠ idiomatic; test compositionality.

[Read detailed error patterns with examples →](prediction-methodology.md)

---

## Validation Approach

**Level 1: Automated (100% coverage)**
- Schema validation, value validation, citation validation
- Cross-reference against TBTA Part="p-..." encoding
- Target: 100% pass rate

**Level 2: Statistical (pattern-based)**
- Genre distribution (prophetic should have 2-3x narrative)
- Type distribution (Cultural ~35%, Theological ~25%, ±10% acceptable)
- Translation pattern consistency
- Target: 90%+ pass rate

**Level 3: Human Expert (sample-based)**
- Non-compositionality test, translation challenge validation
- Sample: 100% of divine names, 50% of cultural idioms, 20% of others
- Target: 85%+ precision, 80%+ recall, 90%+ agreement

**Validation against TBTA**: F1 Score targets - Initial: 85%+, Refined: 90%+, Production: 92%+

[Read detailed validation protocols →](validation.md)

---

## Output Schema

### Filename Format
```
{DATA_DIR}/commentary/{BOOK}/{chapter:03d}/{BOOK}-{chapter:03d}-{verse:03d}-phrasal-elements.yaml
```

### YAML Structure
```yaml
verse: BOOK.chapter.verse
phrasal_elements:
  - text: "I am who I am"
    type: "divine_name"  # divine_name|messianic_title|cultural_idiom|compound_construction|theological_expression|formulaic_expression
    function: "theological_statement"  # title|metaphor|idiom|formula|statement
    compositionality: "non-compositional"  # non-compositional|partially-compositional|context-dependent
    reason: "Philosophical statement of God's self-existence"
    translation_challenge: "Tautological structure difficult; may require explanatory phrase"
    source_language: "אֶהְיֶה אֲשֶׁר אֶהְיֶה"
    citations: "{llm-cs45}"
metadata:
  prediction_method: "llm_analysis"
  confidence: 0.95  # 0.0-1.0
  validation_status: "confirmed"  # confirmed|pending|uncertain
```

---

## Resources

**For translators**:
- [Detailed examples with reasoning](examples.md)
- [Complete prediction methodology](prediction-methodology.md)

**For reviewers**:
- [Validation protocols and metrics](validation.md)

**For tool developers**:
- [Prediction methodology](prediction-methodology.md)
- [Validation approach](validation.md)

---

**Summary**: Phrasal Elements (Category 7) are multi-word expressions requiring unified translation because meaning is non-compositional. Use 3-level prediction: (1) Identify candidates from source, (2) Validate with translation patterns, (3) Predict with context. Validate against TBTA after prediction. Expected accuracy: 85%+ F1 initial, 90%+ refined. Translator impact: Prevents nonsense translations and theological errors.
