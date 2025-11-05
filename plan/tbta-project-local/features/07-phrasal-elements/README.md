# Phrasal Elements (TBTA Category 7)

Multi-word expressions encoded as single semantic units for accurate translation of idioms, fixed phrases, and compound expressions.

**Target Audience:** Bible translators working with languages that handle idioms and compound expressions differently from source languages.

**Primary Use Case:** When translating multi-word expressions like "I am who I am" or "son of man," translators need to know which word sequences function as indivisible semantic units. Without this feature, word-by-word translation destroys idiomatic meaning.

---

## Purpose

### What Are Phrasal Elements?

Phrasal elements identify sequences of words that must be treated as single semantic units rather than individual words. These include:

- **Idioms**: "I am who I am" (Exodus 3:14) - philosophical statement of divine identity
- **Fixed phrases**: "son of man" - theological/messianic title
- **Compound expressions**: Multi-word terms that lose meaning when separated
- **Cultural expressions**: Context-specific phrases requiring unified translation

### Why It Matters

**Translation Impact:**
- **Preserves idiomatic meaning**: Word-by-word translation often produces nonsense or theological error
- **Identifies cultural units**: Some expressions are culturally bound and need special handling
- **Prevents mistranslation**: Recognizing fixed phrases prevents breaking apart theological terms
- **Guides target language choices**: Helps translators choose equivalent idioms or explanatory phrases

**Error Types Prevented:**
- Breaking apart divine names/titles
- Translating idioms literally (producing nonsense)
- Missing theological significance of fixed expressions
- Creating grammatically correct but semantically wrong translations

### Which Language Families Need This?

**High Priority:**
1. **East Asian languages** (Chinese, Japanese, Korean) - Different idiom structures
2. **Austronesian languages** (Indonesian, Tagalog) - Different compounding patterns
3. **African languages** (Swahili, Yoruba) - Cultural-specific idioms
4. **Native American languages** - Different metaphorical systems

**Why:** These languages have:
- Different metaphorical systems (what's idiomatic in Greek/Hebrew isn't in target)
- Different compounding rules (some use single words for multi-word concepts)
- Cultural gaps (expressions requiring explanation vs. direct translation)

### When NOT to Use This Feature

- **Ordinary noun phrases**: "the big house" is not phrasal (compositional meaning)
- **Regular verb phrases**: "he walked quickly" is not phrasal (predictable construction)
- **Arbitrary word sequences**: Random adjacent words with independent meanings
- **Phrases with clear compositional meaning**: Where each word contributes predictably to the whole

---

## Methodology

### Phase 1: Data Extraction

**Location in TBTA Data:**

Phrasal elements appear in TBTA YAML with constituent marker `p` in the first position:

```python
def extract_phrasal_elements(verse_yaml):
    """
    Extract phrasal elements from TBTA YAML structure.

    Phrasal elements are marked with Part="p-..." structure:
    - Position 0: 'p' (phrasal category marker)
    - Position 1: '-' (separator)
    - Position 2: Semantic complexity level (e.g., '1')
    - Position 3: Lexical sense identifier (e.g., 'A')
    - Positions 4-9: Spare positions for future features
    """
    phrasal_elements = []

    def traverse(node, context=None):
        if isinstance(node, dict):
            # Check for phrasal marker
            part = node.get('Part', '')
            if part.startswith('p-'):
                phrasal_elements.append({
                    'semantic_code': part,
                    'text': node.get('Lu', ''),  # Language-universal text
                    'context': context,
                    'complexity': part[2] if len(part) > 2 else None,
                    'sense': part[3] if len(part) > 3 else None
                })

            # Recursively process children
            if 'children' in node:
                for child in node['children']:
                    traverse(child, context={**context, 'parent': part})

        elif isinstance(node, list):
            for item in node:
                traverse(item, context)

    traverse(verse_yaml, context={'verse': verse_yaml.get('verse', 'unknown')})
    return phrasal_elements
```

**Context Required:** Verse-level (phrasal elements are identified within single verses)

**Data Characteristics:**
- **Explicit encoding**: Phrasal elements are directly marked in TBTA data (not predicted)
- **Sparse feature**: Not every verse contains phrasal elements
- **Fixed structure**: `p-[complexity][sense][spares...]` where complexity/sense are currently hardcoded as `1A`

### Phase 2: Analysis (Not Prediction)

Phrasal elements are **explicit** in TBTA data, not predicted. However, analysis can identify patterns:

**Pattern Recognition:**

1. **Theological Fixed Phrases** (95%+ reliability)
   - Divine names: "I AM", "Son of Man", "Son of God"
   - Messianic titles: "Lamb of God", "King of Kings"
   - Doctrinal expressions: "born again", "eternal life"

2. **Cultural Idioms** (90%+ reliability)
   - Hebrew idioms: "hardness of heart", "stiff-necked"
   - Greek idioms: "bowels of mercy", "gird up loins"
   - Cultural metaphors: "whitewashed tombs"

3. **Compound Constructions** (85%+ reliability)
   - Noun compounds: "high priest", "new covenant"
   - Verb compounds: "give thanks", "bear witness"
   - Prepositional compounds: "by means of", "on behalf of"

**Key Correlations:**
- **Discourse genre**: Prophetic/poetic genres have more idiomatic expressions
- **Speaker identity**: Divine speaker → more theological fixed phrases
- **Book-specific patterns**: Exodus/Revelation have more symbolic/idiomatic language

### Phase 3: Validation

**Extraction Accuracy:** 100% (explicit field, direct extraction)

**Critical Validation Rules:**
- [ ] All phrasal elements have valid `p-` prefix
- [ ] Text field (`Lu`) contains the multi-word expression
- [ ] Semantic code follows `p-[complexity][sense][spares...]` format
- [ ] Expression is genuinely non-compositional (meaning > sum of parts)

**Quality Checks:**
- Verify phrase boundaries (no truncated expressions)
- Confirm theological/cultural significance
- Check against standard Bible lexicons for recognized idioms
- Validate cross-translation consistency (same phrase = same marking)

---

## Output Schema

### Filename Format

```
{DATA_DIR}/commentary/{BOOK}/{chapter:03d}/{verse:03d}/{BOOK}-{chapter:03d}-{verse:03d}-phrasal-elements.yaml
```

Example: `./data/commentary/EXO/003/014/EXO-003-014-phrasal-elements.yaml`

### YAML Structure

```yaml
verse: BOOK.chapter.verse
phrasal_elements:
  - text: "I am who I am"
    semantic_code: "p-1A....."
    complexity: "1"
    sense: "A"
    type: "divine_identity"  # Optional: theological/cultural/compound
    function: "name"  # Optional: title/metaphor/idiom/name
    notes: "Hebrew: אֶהְיֶה אֲשֶׁר אֶהְיֶה - divine self-designation"
  - text: "son of man"
    semantic_code: "p-1A....."
    complexity: "1"
    sense: "A"
    type: "messianic_title"
    function: "title"
    notes: "Can mean 'human being' or messianic title depending on context"
metadata:
  source: "tbta"
  version: "1.0.0"
  extraction_method: "explicit"
  confidence: 1.0
```

### Field Descriptions

- **text**: The multi-word expression as it appears in the verse
- **semantic_code**: TBTA semantic string (format: `p-[complexity][sense][spares...]`)
- **complexity**: Semantic complexity level (currently hardcoded as `1`)
- **sense**: Lexical sense identifier (currently hardcoded as `A`)
- **type**: Optional classification (divine_identity, messianic_title, cultural_idiom, compound_construction)
- **function**: Optional functional role (name, title, metaphor, idiom)
- **notes**: Explanatory context (source language, theological significance, translation challenges)

### Examples

#### Example 1: Divine Identity Statement (Exodus 3:14)

```yaml
verse: EXO.003.014
phrasal_elements:
  - text: "I am who I am"
    semantic_code: "p-1A....."
    complexity: "1"
    sense: "A"
    type: "divine_identity"
    function: "name"
    notes: "Hebrew: אֶהְיֶה אֲשֶׁר אֶהְיֶה. Philosophical statement of God's self-existence. Must be translated as unified concept, not word-by-word."
    translation_challenges:
      - "Some languages lack copula ('to be' verb)"
      - "Tautological structure difficult in languages requiring distinct predicates"
      - "May require explanatory phrase: 'I exist as I exist' or 'I am the eternal one'"
metadata:
  source: "tbta"
  version: "1.0.0"
  extraction_method: "explicit"
  confidence: 1.0
```

#### Example 2: Messianic Title (Daniel 7:13)

```yaml
verse: DAN.007.013
phrasal_elements:
  - text: "son of man"
    semantic_code: "p-1A....."
    complexity: "1"
    sense: "A"
    type: "messianic_title"
    function: "title"
    notes: "Hebrew: בַּר־אֱנָשׁ. Can be generic 'human being' or specific messianic title. Context determines interpretation."
    translation_challenges:
      - "Ambiguity: generic vs. messianic must be clear in target"
      - "Languages with classifiers may need 'son' as kinship vs. metaphorical"
      - "Gender-specific: some languages require gender-neutral alternative"
metadata:
  source: "tbta"
  version: "1.0.0"
  extraction_method: "explicit"
  confidence: 1.0
```

#### Example 3: Cultural Idiom (Exodus 32:9)

```yaml
verse: EXO.032.009
phrasal_elements:
  - text: "stiff-necked people"
    semantic_code: "p-1A....."
    complexity: "1"
    sense: "A"
    type: "cultural_idiom"
    function: "metaphor"
    notes: "Hebrew idiom for stubbornness/rebellion. Literal translation meaningless in many languages."
    translation_challenges:
      - "Metaphor may not transfer: 'stiff neck' = stubbornness not universal"
      - "Some languages use different body part metaphors (hard heart, closed ears)"
      - "May require functional equivalent: 'rebellious people' or cultural idiom"
metadata:
  source: "tbta"
  version: "1.0.0"
  extraction_method: "explicit"
  confidence: 1.0
```

#### Example 4: Compound Construction (Matthew 26:26)

```yaml
verse: MAT.026.026
phrasal_elements:
  - text: "give thanks"
    semantic_code: "p-1A....."
    complexity: "1"
    sense: "A"
    type: "compound_construction"
    function: "idiom"
    notes: "Greek: εὐχαριστέω - compound verb 'to give thanks'. May be single word in target language."
    translation_challenges:
      - "Greek compound → may be single verb in target (e.g., 'thank')"
      - "Or may require descriptive phrase: 'express gratitude'"
      - "Register considerations: formal vs. informal gratitude expressions"
metadata:
  source: "tbta"
  version: "1.0.0"
  extraction_method: "explicit"
  confidence: 1.0
```

#### Example 5: Ambiguous Case (John 3:3)

```yaml
verse: JHN.003.003
phrasal_elements:
  - text: "born again"
    semantic_code: "p-1A....."
    complexity: "1"
    sense: "A"
    type: "theological_expression"
    function: "idiom"
    notes: "Greek: γεννηθῇ ἄνωθεν - can mean 'born again' or 'born from above'. Translation determines interpretation."
    translation_challenges:
      - "Double meaning: 'again' (temporal) vs. 'from above' (spatial/divine)"
      - "Nicodemus's confusion (John 3:4) hinges on ambiguity"
      - "Target language may force choice, losing wordplay"
      - "Possible strategies: use ambiguous term if available, or footnote alternate meaning"
metadata:
  source: "tbta"
  version: "1.0.0"
  extraction_method: "explicit"
  confidence: 1.0
```

---

## Related Features

### Integration with Other TBTA Categories

**Correlates with:**
- **Category 1 (Nouns)**: Phrasal elements often contain compound nouns ("son of man", "high priest")
- **Category 2 (Verbs)**: Some phrasal elements are verb compounds ("give thanks", "bear witness")
- **Category 105 (Clauses)**: Phrasal elements can span clause boundaries in rare cases
- **Lexical Sense fields**: Complexity/sense values may correlate with word-level semantic encoding

**Conflicts/Consistency Checks:**
- Ensure phrasal element boundaries align with phrase/clause boundaries
- Verify that words within phrasal elements don't have conflicting individual semantic annotations
- Check that phrasal elements marked in TBTA aren't redundantly annotated as separate words

### Integration with Macula Data

**Complementary Information:**
- **Macula provides**: Morphological analysis of individual words within phrases
- **TBTA provides**: Pragmatic/semantic identification of non-compositional units
- **Combined value**: Translators see both word-level grammar AND phrase-level meaning

**Example (Exodus 3:14 "I am who I am"):**
- Macula: Three separate verb forms (אֶהְיֶה - אֲשֶׁר - אֶהְיֶה), morphological parsing
- TBTA: Single phrasal element (p-1A.....), semantic unity marker
- Translation: Needs both - morphology shows grammatical construction, phrasal marking shows idiomatic meaning

### Translation Workflow Integration

**When to Consult This Feature:**
1. **Pre-translation phase**: Identify idioms/fixed phrases requiring special handling
2. **Drafting phase**: Check if word sequence is phrasal before translating word-by-word
3. **Review phase**: Verify phrasal elements preserved as semantic units
4. **Consultant check**: Flag phrasal elements for accuracy verification

**How to Present to Translators:**
- **Warning markers**: Highlight phrasal elements in draft text (don't translate literally!)
- **Suggested equivalents**: Provide target language idioms where available
- **Cultural notes**: Explain source culture context and significance
- **Alternative strategies**: List options (idiom, functional equivalent, explanatory phrase)

**Practical Example:**
```
Source text: "stiff-necked people" (EXO 32:9)
Phrasal marker: ⚠️ IDIOM - Do not translate literally
Meaning: Stubborn, rebellious, resistant to instruction
Target options:
  1. Use cultural equivalent idiom (if available)
  2. Use functional description: "rebellious people", "stubborn people"
  3. Use explanatory phrase: "people who refuse to listen"
Avoid: Literal "people with rigid necks" (meaningless or humorous in many languages)
```

---

## Implementation Notes

### Current Limitations

1. **Sparse annotations**: Not all idiomatic expressions are marked (TBTA is incomplete)
2. **Hardcoded values**: Complexity and sense currently locked at `1A` (not semantically differentiated)
3. **No subcategories**: All phrasal elements treated uniformly (no distinction between idioms, compounds, titles)
4. **Boundary ambiguity**: Some phrasal elements may have fuzzy boundaries
5. **Context-dependent**: Same phrase may be phrasal in one context, compositional in another

### Future Enhancements

1. **Semantic differentiation**: Expand complexity/sense fields to distinguish:
   - Theological terms (divine names, messianic titles)
   - Cultural idioms (metaphorical expressions)
   - Compound constructions (fixed collocations)
   - Grammatical idioms (fixed syntactic patterns)

2. **Prediction models**: Develop ML models to identify unmarked phrasal elements:
   - Train on known idioms from Bible lexicons
   - Use discourse context to identify fixed expressions
   - Cross-reference translation equivalents across languages

3. **Translation database**: Build phrasal element database with:
   - Source language text
   - Literal meaning
   - Idiomatic meaning
   - Target language equivalents by language family
   - Translation strategies by context

4. **Quality metrics**: Establish accuracy measures:
   - Precision: How many marked phrases are truly non-compositional?
   - Recall: How many actual idioms are unmarked?
   - Cross-translation consistency: Same phrase marked consistently?

### Research Questions

1. **Coverage**: What percentage of actual biblical idioms are marked in TBTA?
2. **Accuracy**: Are all marked phrasal elements genuinely non-compositional?
3. **Granularity**: Should sub-types be encoded (idiom vs. compound vs. title)?
4. **Boundaries**: How to handle nested phrasal elements or overlapping structures?
5. **Context**: When does context change a phrase from compositional to idiomatic?

---

## Summary

**Phrasal Elements (Category 7)** identify multi-word expressions that function as semantic units, critical for accurate translation of idioms, fixed phrases, and compound expressions.

**Key Takeaways:**
- ✅ Explicit in TBTA data (direct extraction, 100% accuracy)
- ✅ Essential for 50+ language families with different idiom systems
- ✅ Prevents translation errors (breaking apart fixed expressions)
- ⚠️ Currently limited: Hardcoded complexity/sense, sparse annotations
- 🔮 Future work: Expand subcategories, build translation database, develop prediction models

**Translator Impact:**
Phrasal element marking saves translators from common errors like literal translation of idioms, helping preserve theological significance and cultural meaning in target languages.

**Next Steps:**
1. Extract all phrasal elements from TBTA data
2. Categorize by type (theological, cultural, compound)
3. Build translation equivalent database by language family
4. Develop prediction model for unmarked phrasal elements
5. Create translator reference guide with examples and strategies
