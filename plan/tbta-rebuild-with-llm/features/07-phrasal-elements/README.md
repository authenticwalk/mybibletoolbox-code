# Phrasal Elements (TBTA Category 7)

Predict multi-word expressions that function as single semantic units—idioms, fixed phrases, and compound expressions that cannot be translated word-by-word.

**Target Audience:** Bible translators working with languages that handle idioms and compound expressions differently from source languages.

**Primary Use Case:** When translating multi-word expressions like "I am who I am" or "son of man," translators need to know which word sequences function as indivisible semantic units. Without this feature, word-by-word translation destroys idiomatic meaning.

---

## What Are Phrasal Elements?

Phrasal elements are sequences of words where the meaning is **non-compositional**—the whole means more than the sum of its parts. These include:

- **Idioms**: "I am who I am" (Exodus 3:14) - philosophical statement beyond literal words
- **Fixed phrases**: "son of man" - theological/messianic title, not generic "human offspring"
- **Compound expressions**: "give thanks" - treated as unit in Greek, may be single word in target
- **Cultural expressions**: "stiff-necked people" - metaphor for stubbornness requiring special translation

**Key characteristic**: Breaking apart phrasal elements destroys meaning or creates theological errors.

---

## Why They Matter for Translation

**Translation Impact:**
- **Prevents nonsense**: Literal "stiff-necked" is meaningless in most languages
- **Preserves theology**: "Son of Man" as messianic title vs. generic human being
- **Guides target choices**: Use equivalent idiom, functional description, or explanatory phrase
- **Identifies cultural gaps**: Source culture metaphors may need replacement in target culture

**High Priority Languages:**
- **East Asian** (Chinese, Japanese, Korean) - different metaphorical systems
- **Austronesian** (Indonesian, Tagalog) - different compounding patterns
- **African** (Swahili, Yoruba) - different body-part metaphors ("hard heart" vs. "stiff neck")
- **Native American** - different cultural idiom structures

---

## Prediction Methodology

### Step 1: Identify Candidates from Source Text

**Indicators of phrasal elements in Greek/Hebrew:**

1. **Fixed collocations** - words that frequently appear together
   - Greek: εὐχαριστέω (give thanks), μετανοέω (change mind/repent)
   - Hebrew: בַּר־אֱנָשׁ (son of man), קְשֵׁה־עֹרֶף (stiff-necked)

2. **Divine names and titles** - theologically significant fixed expressions
   - אֶהְיֶה אֲשֶׁר אֶהְיֶה (I am who I am)
   - υἱὸς τοῦ ἀνθρώπου (Son of Man)
   - ἀμνὸς τοῦ θεοῦ (Lamb of God)

3. **Body-part metaphors** - culturally-specific idioms
   - Hebrew: "hardness of heart", "uncircumcised ears"
   - Greek: "bowels of mercy" (compassion)

4. **Formulaic expressions** - greetings, blessings, technical terms
   - χάρις ὑμῖν καὶ εἰρήνη (grace and peace to you)
   - βασιλεία τῶν οὐρανῶν (kingdom of heaven)

**LLM Prompt for Step 1:**
```
Analyze the Greek/Hebrew text for [VERSE]. Identify any:
1. Fixed collocations (words that regularly appear together)
2. Divine names, titles, or theological terms
3. Body-part metaphors or cultural idioms
4. Formulaic expressions or technical terms

For each candidate, explain why it might be non-compositional.
```

### Step 2: Validate with Translation Patterns

**Translation analysis reveals idiomatic status:**

1. **Check for unit translation** across languages
   - If 80%+ of translations treat phrase as unit → likely phrasal element
   - If translations vary widely → may be compositional

2. **Look for functional equivalents** in target languages
   - English "son of man" → Spanish "hijo del hombre" (literal)
   - English "hardness of heart" → Spanish "terquedad" (functional: stubbornness)
   - Presence of functional equivalents suggests non-compositional meaning

3. **Identify cultures without equivalent metaphor**
   - Languages that translate "stiff-necked" as "stubborn" → confirms idiom status
   - Languages that keep literal "stiff neck" → may miss idiomatic meaning

**LLM Prompt for Step 2:**
```
Compare translations of [PHRASE] across English, Spanish, French, German, Chinese, Arabic:

1. Do translators treat this as a unit or translate word-by-word?
2. Do some languages use different metaphors (functional equivalents)?
3. What does translation variation tell us about idiomatic status?

Conclusion: Is this a phrasal element? Why or why not?
```

### Step 3: LLM Prediction with Context

**Final prediction using discourse context:**

1. **Genre considerations**
   - Prophetic/poetic texts → more idioms and metaphors
   - Narrative texts → fewer but important theological titles
   - Epistles → technical theological terms

2. **Speaker identity**
   - Divine speaker → more fixed divine names/attributes
   - Jesus → more kingdom/messianic terminology
   - Prophets → more cultural metaphors

3. **Theological significance**
   - Does phrase carry theological weight beyond literal words?
   - Is misunderstanding this phrase in early church dialogues (e.g., Nicodemus's confusion)?

**LLM Prompt for Step 3:**
```
For [VERSE], considering:
- Genre: [prophetic/narrative/epistle/etc.]
- Speaker: [God/Jesus/prophet/apostle/etc.]
- Context: [theological/cultural significance]

Is "[PHRASE]" a phrasal element that should be translated as a unit?

Answer with:
1. YES/NO/UNCERTAIN
2. Type: [idiom/title/compound/formula]
3. Reason: Why this phrase is/isn't non-compositional
4. Translation challenge: What happens if translated literally?
```

---

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

---

## Validation Against TBTA Data

**After prediction, validate against TBTA structure:**

### TBTA Encoding of Phrasal Elements

TBTA marks phrasal elements with `Part="p-..."` in YAML structure:
- Position 0: `p` (phrasal category marker)
- Position 1: `-` (separator)
- Positions 2+: Semantic codes (currently `1A` for all)

### Validation Process

1. **Check predictions against TBTA**
   - True Positives: Predicted phrasal, marked in TBTA ✅
   - False Positives: Predicted phrasal, NOT in TBTA ⚠️ (may be unmarked idiom)
   - False Negatives: Not predicted, but marked in TBTA ❌ (missed idiom)
   - True Negatives: Not predicted, not in TBTA ✅

2. **Accuracy metrics**
   - Precision: Of predicted phrasal elements, how many are correct?
   - Recall: Of actual phrasal elements (in TBTA), how many did we find?
   - F1 Score: Balance of precision and recall

3. **Learning from mismatches**
   - False Positives → refine prediction criteria (too broad?)
   - False Negatives → add overlooked indicators (too narrow?)

**Goal:** 85%+ F1 score on initial predictions, improving with iteration.

---

## Common Prediction Errors

### Error Type 1: Over-prediction (False Positives)

**Mistake:** Marking ordinary phrases as idiomatic

❌ Wrong: "the good shepherd" → phrasal element
✅ Right: Descriptive phrase, compositional (good + shepherd)

**Why it happens:** Theological significance ≠ non-compositional
**How to avoid:** Ask "Does literal word-by-word translation lose meaning?"

### Error Type 2: Under-prediction (False Negatives)

**Mistake:** Missing culturally-bound idioms

❌ Wrong: "uncircumcised ears" → not phrasal
✅ Right: Hebrew idiom for "stubborn to listen" (non-compositional)

**Why it happens:** Unfamiliarity with source culture metaphors
**How to avoid:** Study Hebrew/Greek idiom lexicons; check translation patterns

### Error Type 3: Context-insensitive

**Mistake:** Same phrase marked differently in different contexts

Example: "son of man"
- Generic context: "mere mortal" → NOT phrasal (compositional)
- Messianic context: "Son of Man" → phrasal (theological title)

**Why it happens:** Ignoring discourse context
**How to avoid:** Apply Step 3 prompts—genre, speaker, theological weight

### Error Type 4: Confusing theological importance with non-compositionality

**Mistake:** Marking theologically significant compositional phrases

❌ Wrong: "eternal life" → always phrasal
✅ Right: Usually compositional (eternal + life), unless culturally-loaded fixed term

**Why it happens:** Importance ≠ idiomatic
**How to avoid:** Focus on compositionality test: "Does word-by-word work?"

---

## Output Schema

### Filename Format

```
{DATA_DIR}/commentary/{BOOK}/{chapter:03d}/{BOOK}-{chapter:03d}-{verse:03d}-phrasal-elements.yaml
```

Example: `./data/commentary/EXO/003/014/EXO-003-014-phrasal-elements.yaml`

### YAML Structure

```yaml
verse: BOOK.chapter.verse
phrasal_elements:
  - text: "I am who I am"
    type: "divine_name"  # divine_name|messianic_title|cultural_idiom|compound_construction
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

### Field Descriptions

- **text**: The multi-word expression as it appears in English reference translation
- **type**: Classification (divine_name, messianic_title, cultural_idiom, compound_construction)
- **function**: Functional role (title, metaphor, idiom, formula, statement)
- **compositionality**: How meaning relates to parts (non-compositional, partially-compositional, context-dependent)
- **reason**: Explanation of why this is phrasal (for human reviewers)
- **translation_challenge**: Specific issues translators face
- **source_language**: Greek/Hebrew/Aramaic original text
- **citations**: Source of prediction (LLM inference should cite {llm-cs45})

---

## Summary

**Phrasal Elements (Category 7)** are multi-word expressions requiring unified translation because their meaning is non-compositional (whole > sum of parts).

**Prediction Strategy:**
1. ✅ Identify candidates from source text (fixed collocations, divine names, metaphors)
2. ✅ Validate with translation patterns (unit treatment, functional equivalents)
3. ✅ LLM prediction with context (genre, speaker, theological significance)
4. ✅ Validate against TBTA structure after prediction

**Key Principles:**
- Non-compositionality is the core test
- Context matters (same phrase may/may not be phrasal in different verses)
- Translation patterns reveal idiomatic status
- TBTA is validation source, NOT input for prediction

**Translator Impact:**
Accurate phrasal element prediction prevents translation disasters (literal idioms producing nonsense or theological error), helping preserve meaning across languages.

**Expected Accuracy:**
- Initial predictions: 85%+ F1 score
- With iterative refinement: 90%+ F1 score
- Some uncertainty is acceptable—reviewers can adjudicate borderline cases
