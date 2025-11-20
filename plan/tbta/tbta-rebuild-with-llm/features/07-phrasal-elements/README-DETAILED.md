# Phrasal Elements (TBTA Category 7)

**Translation Impact:** Phrasal elements identify multi-word expressions where meaning is non-compositional (whole > sum of parts). Word-by-word translation of "stiff-necked people" or "son of man" produces nonsense or theological error in most languages. This feature prevents translation disasters by marking idioms, titles, and compound expressions requiring unified treatment, helping translators choose appropriate equivalents, functional descriptions, or cultural adaptations.

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

**High Priority Languages**:
- East Asian (different metaphorical systems)
- Austronesian (different compounding patterns)
- African languages (different body-part metaphors)

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

## Hierarchical Prediction Prompt Template

Use this 3-level decision tree for systematic phrasal element identification:

### Level 1: Source Text Analysis (30-second scan)
**Prompt**: "Scan [VERSE] for fixed collocations, divine names/titles, body-part metaphors, or formulaic expressions. List all candidates."

**Decision criteria**:
- Fixed collocation (words regularly together)? → Continue to Level 2
- Divine name/title? → 95% likely phrasal (validate Level 3)
- Body-part in metaphorical context? → Continue to Level 2
- Greeting/blessing formula? → 90% likely phrasal (validate Level 3)
- None found? → Stop (no phrasal elements)

### Level 2: Translation Pattern Validation (2-3 minute check)
**Prompt**: "For [CANDIDATE PHRASE], check 3-5 translations in different language families. Do they treat this as a unit or translate word-by-word? Do any use functional equivalents (different metaphor with same meaning)?"

**Decision criteria**:
- 80%+ translations treat as unit? → Likely phrasal → Level 3
- Functional equivalents used? → Strong evidence → Level 3
- Word-by-word across all languages? → NOT phrasal (stop)
- Mixed/uncertain? → Continue to Level 3 for context check

### Level 3: Discourse Context & Final Prediction (1-2 minute analysis)
**Prompt**: "For [PHRASE] in [VERSE], consider: (1) Genre [narrative/prophetic/epistle], (2) Speaker [God/Jesus/prophet/etc.], (3) Theological weight [high/medium/low]. Is this phrase non-compositional (meaning beyond literal words)? What translation challenge does literal rendering create?"

**Final decision matrix**:

| Context | Fixed Collocation | Divine/Theological | Body Metaphor | Formula | Prediction |
|---------|------------------|-------------------|---------------|---------|------------|
| High theological weight | Yes | Yes | - | - | **Phrasal** (95%+) |
| Speaker = God/Jesus | Yes | - | - | Yes | **Phrasal** (90%+) |
| Prophetic genre | - | - | Yes | - | **Phrasal** (85%+) |
| Functional equiv. used | Yes | - | Yes | - | **Phrasal** (85%+) |
| Word-by-word works | - | No | - | - | **NOT phrasal** |
| Context-dependent | Yes | Maybe | - | - | Mark as "context-dependent" |

**Output template**:
```yaml
prediction: [YES/NO/UNCERTAIN]
type: [divine_name|messianic_title|cultural_idiom|compound_construction|theological_expression|formulaic_expression]
confidence: [0.70-1.00]
reason: [One sentence explaining non-compositionality]
translation_challenge: [What happens if translated literally?]
```

---

## Gateway Features & Correlations

Phrasal Elements interact with several other TBTA features:

### Primary Correlation: Semantic Domains (90%+ correlation)
- Phrasal elements cluster in specific semantic domains
- Divine names → Domain 12.1-12.48 (Supernatural beings)
- Body metaphors → Domain 26 (Psychological faculties) + others
- Cultural idioms → Domain-specific (agriculture, kinship, etc.)
- **Usage**: Check semantic domain to validate phrasal element type

### Secondary Correlation: Discourse Genre (80%+ correlation)
- Prophetic/Poetic → Higher phrasal element density (10-15%)
- Narrative → Lower density (4-6%), mostly titles
- Epistles → Medium density (6-8%), theological terms
- **Usage**: Adjust prediction threshold based on genre

### Moderate Correlation: Speaker Identity (70%+ correlation)
- God as speaker → More divine names, formulaic expressions
- Jesus as speaker → More messianic titles, teaching idioms
- Prophets → More cultural metaphors
- **Usage**: Speaker signals likely phrasal element types

### Weak Correlation: Participant Tracking (60% correlation)
- Divine names often appear at First Mention (introducing God)
- Titles may appear at Restaging (reintroducing participant)
- **Usage**: Participant state can confirm phrasal element function

### Cross-Feature Validation
- If phrase marked as phrasal BUT has generic semantic domain → Flag for review
- If prophetic genre BUT no metaphors found → May have missed idioms
- If speaker=Jesus BUT no titles found in passage → Check for implicit references

---

## Common Prediction Errors

### Error 1: Over-Predicting Theological Significance
**Mistake**: Marking theologically important compositional phrases as phrasal

❌ Wrong: "eternal life" → always phrasal element
✅ Right: "eternal life" is compositional (eternal + life = predictable meaning)

**Why it happens**: Confusing theological importance with non-compositionality
**How to avoid**: Apply strict compositionality test: "Does word-by-word translation lose meaning or just theological weight?"
**Warning signs**: Phrase is theologically significant BUT literal translation works in multiple languages

---

### Error 2: Missing Cultural Idioms
**Mistake**: Not recognizing culture-specific body-part metaphors

❌ Wrong: "uncircumcised ears" (Jeremiah 6:10) → not phrasal
✅ Right: Hebrew idiom for "stubborn to listen" (non-compositional)

**Why it happens**: Unfamiliarity with source culture metaphorical systems
**How to avoid**: Study Hebrew/Greek idiom lexicons; check for functional equivalents in translations
**Warning signs**: Body part + abstract concept; translations use completely different words

---

### Error 3: Context-Insensitive Prediction
**Mistake**: Marking same phrase differently without considering context

**Example**: "son of man"
- Ezekiel 2:1 (generic) → "mere mortal" = NOT phrasal (compositional)
- Matthew 16:13 (messianic) → "Son of Man" = phrasal (theological title)

**Why it happens**: Ignoring discourse context (genre, speaker, theological significance)
**How to avoid**: Always apply Level 3 prompts—check genre, speaker, and theological weight
**Warning signs**: Same phrase gets different treatment in different verses without explanation

---

### Error 4: Ignoring Translation Patterns
**Mistake**: Predicting phrasal status without checking how languages actually translate it

❌ Wrong: "the good shepherd" → phrasal (because theologically important)
✅ Right: NOT phrasal (all languages translate word-by-word: good + shepherd)

**Why it happens**: Skipping Level 2 validation (translation pattern check)
**How to avoid**: Always check 3-5 translations in different families; look for functional equivalents
**Warning signs**: Prediction based solely on English or theological significance

---

### Error 5: Confusing Ellipsis with Phrasal Elements
**Mistake**: Treating grammatical ellipsis as phrasal elements

❌ Wrong: "Jesus wept" (John 11:35) → phrasal element
✅ Right: Minimal sentence, NOT phrasal (Jesus + wept = compositional)

**Why it happens**: Confusing brevity/impact with non-compositionality
**How to avoid**: Short phrases can still be compositional; test if meaning = sum of parts
**Warning signs**: Two-word sentences, grammatically complete, predictable meaning

---

## Validation Approach

### Three-Level Validation System

**Level 1: Automated Checks (100% coverage)**
1. Schema validation: All required fields present
2. Value validation: Type/function/compositionality values from enumeration
3. Citation validation: Source must be {llm-cs45} or approved resource
4. Cross-reference: Check against TBTA Part="p-..." encoding
5. Duplicate detection: Same phrase marked multiple times in verse

**Metrics**:
- Pass: All checks pass
- Fail: Any required field missing or invalid value
- **Target**: 100% pass rate before human review

---

**Level 2: Pattern-Based Validation (statistical checks)**
1. **Genre distribution check**: Prophetic/poetic should have 2-3x more phrasal elements than narrative
2. **Type distribution check**: Cultural idiom ~35%, Theological ~25% (variance ±10% acceptable)
3. **Confidence calibration**: High-confidence predictions should correlate with divine names/well-known titles
4. **Translation pattern consistency**: If prediction=YES but all translations are word-by-word → Flag
5. **Context sensitivity**: Same phrase in different contexts should have context-dependent marking

**Metrics**:
- Pass: Within expected distribution ranges
- Warning: Outside ranges but explicable (e.g., Job has more metaphors)
- Fail: Major deviation without explanation
- **Target**: 90%+ pass rate

---

**Level 3: Human Expert Review (sample-based)**
1. **Non-compositionality test**: Do reviewers agree phrase meaning ≠ sum of parts?
2. **Translation challenge validation**: Does literal translation really cause problems?
3. **Type classification accuracy**: Is divine_name vs messianic_title vs cultural_idiom correct?
4. **Edge case adjudication**: For UNCERTAIN predictions, expert decides YES/NO

**Sample size**:
- 100% of divine names (high stakes)
- 50% of cultural idioms (high error rate)
- 20% of other types (spot check)

**Metrics**:
- Agreement rate: Expert agrees with prediction
- Precision: Of predicted phrasal, % actually non-compositional
- Recall: Of actual phrasal (per expert), % detected
- **Target**: 85%+ precision, 80%+ recall, 90%+ agreement

---

### Validation Against TBTA Encoding

TBTA marks phrasal elements with `Part="p-..."` codes. Use this for ground truth validation:

1. **True Positive**: Predicted phrasal, TBTA has p-code ✅
2. **False Positive**: Predicted phrasal, TBTA does NOT have p-code ⚠️
   - May be unmarked idiom in TBTA (acceptable)
   - May be over-prediction (error)
3. **False Negative**: Not predicted, TBTA has p-code ❌
   - Missed idiom (error)
4. **True Negative**: Not predicted, TBTA does NOT have p-code ✅

**F1 Score Targets**:
- Initial predictions: 85%+ F1
- After iterative refinement: 90%+ F1
- Production quality: 92%+ F1

**Iteration process**:
1. Analyze False Positives → Tighten prediction criteria
2. Analyze False Negatives → Add overlooked indicators
3. Re-run on sample → Measure improvement
4. Deploy updated model

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
