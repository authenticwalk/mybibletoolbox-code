# Phrasal Elements: Complete Prediction Methodology

> **Parent Context:** Step-by-step methodology for predicting phrasal elements using LLM analysis and translation patterns.

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

