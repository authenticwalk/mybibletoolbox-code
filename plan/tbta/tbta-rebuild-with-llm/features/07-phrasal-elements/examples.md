# Phrasal Elements: Detailed Examples

> **Parent Context:** Detailed examples with full prediction reasoning for identifying phrasal elements.

## Examples with Prediction Reasoning

### Example 1: "I am who I am" (Exodus 3:14)

**Source text:** אֶהְיֶה אֲשֶׁר אֶהְיֶה (Hebrew)

**Prediction reasoning:**
1. **Fixed collocation**: Unique philosophical construction not used elsewhere
2. **Divine name**: God's self-revelation—highest theological significance
3. **Translation patterns**: Most languages struggle with tautology, use explanatory phrases
4. **Non-compositional**: Literal "I will be that I will be" misses philosophical depth

**Prediction:** ✅ **Phrasal element** (divine identity statement)

**Expected output:**
```yaml
verse: EXO.003.014
phrasal_elements:
  - text: "I am who I am"
    type: "divine_name"
    function: "theological_statement"
    compositionality: "non-compositional"
    reason: "Philosophical statement of God's self-existence and eternality"
    translation_challenge: "Tautological structure difficult in many languages; requires theological interpretation"
```

### Example 2: "son of man" (Daniel 7:13, throughout Gospels)

**Source text:** בַּר־אֱנָשׁ (Aramaic), υἱὸς τοῦ ἀνθρώπου (Greek)

**Prediction reasoning:**
1. **Context-dependent**: Generic in some contexts ("human being"), messianic title in others
2. **Fixed collocation**: Appears 100+ times in consistent form
3. **Translation patterns**: Languages keep literal form even when odd (signals importance)
4. **Theological weight**: Jesus's preferred self-designation—theologically loaded

**Prediction:** ✅ **Phrasal element** (messianic title in Gospel contexts)

**Expected output:**
```yaml
verse: MAT.016.013
phrasal_elements:
  - text: "son of man"
    type: "messianic_title"
    function: "self_designation"
    compositionality: "context-dependent"
    reason: "Can be generic or messianic; Gospel usage is theologically significant title"
    translation_challenge: "Ambiguity between generic and messianic must be clear; gender implications vary by language"
```

### Example 3: "stiff-necked people" (Exodus 32:9)

**Source text:** עַם־קְשֵׁה־עֹרֶף (Hebrew, literally "people hard of neck")

**Prediction reasoning:**
1. **Body-part metaphor**: Physical neck → metaphorical stubbornness
2. **Translation patterns**: Most languages use functional equivalent ("stubborn", "rebellious")
3. **Cultural idiom**: Metaphor works in ancient Near East context, not universal
4. **Non-compositional**: Literal "hard neck" is meaningless/humorous in many languages

**Prediction:** ✅ **Phrasal element** (cultural idiom)

**Expected output:**
```yaml
verse: EXO.032.009
phrasal_elements:
  - text: "stiff-necked people"
    type: "cultural_idiom"
    function: "metaphor"
    compositionality: "non-compositional"
    reason: "Body-part metaphor for stubbornness; literal translation produces nonsense"
    translation_challenge: "Target cultures may use different body parts (hard heart, closed ears); need functional equivalent"
```

### Example 4: "born again" / "born from above" (John 3:3)

**Source text:** γεννηθῇ ἄνωθεν (Greek - deliberately ambiguous)

**Prediction reasoning:**
1. **Intentional wordplay**: ἄνωθεν means both "again" (temporal) and "from above" (spatial)
2. **Nicodemus's confusion**: John 3:4 shows he takes literal meaning—confirms non-compositional intent
3. **Translation patterns**: Languages force choice between meanings (losing wordplay)
4. **Theological depth**: Spiritual rebirth, not physical—meaning beyond literal words

**Prediction:** ✅ **Phrasal element** (theological expression with wordplay)

**Expected output:**
```yaml
verse: JHN.003.003
phrasal_elements:
  - text: "born again"
    type: "theological_expression"
    function: "wordplay"
    compositionality: "non-compositional"
    reason: "Greek ἄνωθεν has double meaning (again/from above); spiritual rebirth concept requires unified treatment"
    translation_challenge: "Target language may lose wordplay; consider footnote for alternate meaning"
```

### Example 5: "the big house" (Hypothetical - NOT phrasal)

**Source text:** ὁ μέγας οἶκος (Greek)

**Prediction reasoning:**
1. **Compositional**: "big" + "house" = big house (predictable meaning)
2. **Translation patterns**: All languages translate word-by-word without issue
3. **No idiom**: No cultural or theological special meaning
4. **No fixed collocation**: Words not specially bound together

**Prediction:** ❌ **NOT a phrasal element** (ordinary noun phrase)

This example shows what to reject—compositional phrases where meaning is predictable from parts.
