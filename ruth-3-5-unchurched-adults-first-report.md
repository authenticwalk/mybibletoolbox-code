# Ruth 3:5 - UNCHURCHED-ADULTS-FIRST TBTA Phase 1 Encoding Report

**Date**: 2025-12-01
**Verse**: Ruth 3:5
**Approach**: Starting from Unchurched Adults target text and adapting to TBTA He1 encoding

---

## 1. Source Text: Unchurched Adults Version

**Retrieved from**: https://targets.tabitha.bible/English/Ruth/3/5

```
Then Ruth said to Naomi, 'I'll do all of those things that you said.'
```

This is the simplified English version designed for unchurched adults, using accessible vocabulary and clear structure.

---

## 2. Step-by-Step Transformation to He1 Encoding

### Step 1: Copy Unchurched Adults text exactly

```
Then Ruth said to Naomi, 'I'll do all of those things that you said.'
```

**Starting point**: Direct copy of the Unchurched Adults text.

---

### Step 2: Expand contractions to full forms

**Change**: `I'll` → `I will`

**Reason**: TBTA encoding uses full word forms, not contractions.

```
Then Ruth said to Naomi, 'I will do all of those things that you said.'
```

---

### Step 3: Normalize determiners

**Change**: `those things` → `the things`

**Reason**: "Those" is demonstrative and adds distance/specificity not needed in basic encoding. "The" is more neutral and standard.

```
Then Ruth said to Naomi, 'I will do all of the things that you said.'
```

---

### Step 4: Add pronoun resolution with brackets

**Changes**:
- `I` → `I(Ruth)` - resolve first-person pronoun to speaker
- `you` → `you(Naomi)` - resolve second-person pronoun to addressee

**Reason**: TBTA Phase 1 requires explicit resolution of pronouns to their antecedents for clarity in low-context languages.

```
Then Ruth said to Naomi, 'I(Ruth) will do all of the things that you(Naomi) said.'
```

---

### Step 5: Add quotation brackets

**Change**: Add `["..."]` brackets around the direct speech

**Reason**: TBTA uses brackets to mark quoted speech and subordinate clauses.

```
Then Ruth said to Naomi, ["I(Ruth) will do all of the things that you(Naomi) said"].
```

---

### Step 6: Add relative clause brackets

**Change**: Add brackets around `[that you(Naomi) said]`

**Reason**: Mark the relative clause modifying "things" to show syntactic dependency.

**Final He1 encoding**:
```
Then Ruth said to Naomi, ["I(Ruth) will do all of the things [that you(Naomi) said]"].
```

---

## 3. Validation Using TBTA Checker

### Initial Check

**URL**: https://editor.tabitha.bible/check?text={encoded_text}

**Status**: ✅ **VALID**

### Validation Results

#### ✅ Valid Elements
- **Main clause structure**: Properly tagged as main_clause
- **Verb case frame**: "said" (Sense A) has valid arguments with agent (Ruth) and patient (Naomi)
- **Quote clause**: Correctly nested as patient_clause_quote_begin
- **Relative clause**: Properly formed with relativizer "that" and gap-filling mechanism
- **Pronoun resolution**: Ruth tagged as "I" (first person singular); Naomi tagged as "you" (second person)

#### ⚠️ Minor Warnings (Non-blocking)
1. **Complexity ambiguity warnings**: Multiple word senses flagged for:
   - "then" (5 possible senses)
   - "Ruth" (2 senses)
   - "thing/things" (4 senses)
   - "all" (2 senses with different categorizations)

2. **Unchecked case frames**: Head nouns have unchecked case frames (standard for non-verbal elements)

3. **Ontology status**: All words present in ontology except GAP_REL (expected for gap markers)

#### Back-Translation
Generated: "Then Ruth said to Naomi, 'I will do all of the things that you said.'"

**Assessment**: Accurately reflects the syntactic structure and semantic relationships encoded.

### Validation Conclusion
**No blocking issues.** The encoding is suitable for analysis; ambiguity warnings are expected for natural language with multiple valid interpretations.

---

## 4. Comparison with Official Phase 1 Encoding

### Our Result (Unchurched Adults First approach)
```
Then Ruth said to Naomi, ["I(Ruth) will do all of the things [that you(Naomi) said]"].
```

### Official Phase 1 Encoding
**Retrieved from**: https://sources.tabitha.bible/Bible/Ruth/3/5

```
Then Ruth said to Naomi, ["I(Ruth) will do all of the things [that you(Naomi) said]"].
```

### Comparison Analysis

| Aspect | Match Status | Notes |
|--------|--------------|-------|
| Base text | ✅ Exact match | Identical wording |
| Pronoun resolution | ✅ Exact match | Both resolve I→Ruth, you→Naomi |
| Quotation brackets | ✅ Exact match | Both use `["..."]` for direct speech |
| Relative clause | ✅ Exact match | Both bracket `[that you(Naomi) said]` |
| Word choice | ✅ Exact match | "the things" not "those things" |
| Punctuation | ✅ Exact match | Period placement identical |

**Result**: 🎯 **100% MATCH** - Our encoding exactly matches the official phase_1_encoding.

---

## 5. Quality Assessment

### Strengths of the Unchurched Adults First Approach

1. **Natural starting point**: The Unchurched Adults text is already simplified and clear, requiring minimal transformation
2. **Explicit vocabulary**: Uses concrete, accessible words that align well with TBTA ontology requirements
3. **Clear structure**: Simple sentence structure with obvious clause boundaries
4. **Minimal pronoun chains**: Only two pronouns to resolve (I, you), both with clear antecedents
5. **No complex idioms**: Straightforward meaning without cultural metaphors

### Transformation Efficiency

- **Total steps**: 6 (from source to final encoding)
- **Major changes**: 3 (expand contraction, normalize determiner, add brackets)
- **Pronoun resolutions**: 2 (Ruth, Naomi)
- **Validation iterations**: 1 (passed first time)

### Key Insights

1. **Contraction expansion**: The only grammatical normalization needed was `I'll` → `I will`
2. **Determiner choice**: "Those" → "the" was the only lexical adjustment for neutrality
3. **Bracket addition**: All bracketing (quotes, relative clauses) was straightforward overlay
4. **No vocabulary issues**: All words already present in TBTA ontology
5. **No subordination issues**: Clear main clause with simple nesting

### Why This Approach Works Well for Ruth 3:5

- **Short response**: Ruth's reply is brief and direct
- **Single speech act**: One quotation with one embedded clause
- **Clear participants**: Only two people (Ruth, Naomi) referenced
- **Simple semantics**: "I will do what you said" is universally clear
- **No cultural load**: Statement of compliance needs no cultural translation

---

## 6. Conclusion

The UNCHURCHED-ADULTS-FIRST approach successfully produced a TBTA Phase 1 encoding that:
- ✅ Validates without errors
- ✅ Exactly matches the official encoding
- ✅ Required minimal transformation (6 clear steps)
- ✅ Maintains semantic clarity and syntactic precision

This demonstrates that starting from simplified, audience-appropriate English can be an efficient path to TBTA encoding, particularly for verses with:
- Simple syntax (one main clause, one or two subordinate)
- Clear participant reference
- Concrete vocabulary
- Direct speech acts

The approach reduces the cognitive load of starting from literal translations and working backward, instead building forward from already-simplified text that targets comprehension.

---

## Final He1 Encoding

```
Then Ruth said to Naomi, ["I(Ruth) will do all of the things [that you(Naomi) said]"].
```

**Status**: ✅ Validated and matches official encoding
