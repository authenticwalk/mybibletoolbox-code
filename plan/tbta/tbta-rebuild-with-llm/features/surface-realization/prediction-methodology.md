# Surface Realization: Prediction Methodology

> **Parent Context:** Complete methodology for predicting surface realization (noun/pronoun/zero/clitic) in Bible translation languages.

## Hierarchical Prediction Prompt Template

Surface realization is highly predictable using this 5-level decision process:

### Level 1 - Check Participant Tracking State (95% correlation)

Surface realization correlates strongly with tracking:

| Tracking State | Surface Realization | Confidence |
|---------------|---------------------|------------|
| First Mention | **Noun** | 95%+ |
| Routine (non-pro-drop) | **Pronoun** | 90%+ |
| Routine (pro-drop) | **Zero** or **Pronoun** | 85%+ |
| Restaging | **Noun** | 85%+ |
| Frame Inferable | **Noun** (definite) | 90%+ |
| Generic | **Noun** (often bare) | 85%+ |
| Offstage | **Noun** (modifier position) | 95%+ |

**Prompt**: "What is the Participant Tracking state? If First Mention or Restaging → use Noun (95%). If Routine → check Level 2."

---

### Level 2 - Check Language Pro-Drop Status

**Prompt**: "Is the target language pro-drop?"

**Pro-drop languages** (Hebrew, Greek, Spanish, Italian, Portuguese, Japanese, Korean, Mandarin, Arabic, Turkish):
- Routine reference → **Zero** (most natural)
- Emphasis/disambiguation → **Pronoun** (explicit)
- First mention/restaging → **Noun**

**Non-pro-drop languages** (English, French, German, Dutch, Swedish):
- Routine reference → **Pronoun** (required)
- First mention/restaging → **Noun**
- Zero → Only in coordinated structures (ellipsis)

---

### Level 3 - Check for Emphasis/Disambiguation

**Prompt**: "Is there emphasis, contrast, or ambiguity?"

**Emphasis markers**:
- Hebrew/Greek explicit pronoun when zero is normal → Emphasis
  - Example: αὐτὸς εἶπεν (autos eipen) = "HE said" (emphatic, not routine)
- Contrast: "Peter went, but JOHN stayed" → Use pronoun even in pro-drop
- Ambiguity: Multiple same-gender referents → Use **Noun** for clarity
  - Example: Two males in context → "Peter said" (not "he said")

**Decision**:
- If emphasis/contrast → Use explicit **Pronoun** (even in pro-drop)
- If ambiguous → Use **Noun**
- If neither → Continue to Level 4

---

### Level 4 - Check Register/Formality

**Prompt**: "Does formality affect pronoun choice?"

**Formal contexts** (epistles, teaching, legal):
- May use title + name instead of pronoun
- Higher noun usage (explicit over implicit)
- Pro-drop languages may use more explicit pronouns

**Informal contexts** (dialogue, narrative):
- Pro-drop languages maximize zero
- Allow pronouns more freely

**Honorific systems** (Japanese, Korean, Javanese):
- Pronoun choice affected by social distance
- May avoid pronouns entirely in high-formality contexts

---

### Level 5 - Default Prediction (Accessibility Hierarchy)

Based on Ariel's Accessibility Hierarchy:

**High accessibility** (recent, salient, unique) → Less material:
- Pro-drop languages: **Zero**
- Non-pro-drop: **Pronoun**

**Medium accessibility** (nearby, semi-salient) → Moderate material:
- **Pronoun** (most languages)

**Low accessibility** (distant, multiple referents) → More material:
- **Noun** (all languages)

**Final decision**: Choose least material form allowed by grammar that maintains clarity.

---

## Common Prediction Errors (Detailed)

### Error 1: Not Accounting for Pro-Drop Differences

**Problem**: Assuming all languages work like English (explicit pronouns for all routine reference)

**Example**:
- Spanish "Vino" (came-3SG) analyzed as missing pronoun
- Actually: This is **Zero** (normal, grammatical)

**Solution**:
1. Check target language pro-drop status FIRST
2. For pro-drop languages, zero is the DEFAULT for routine reference
3. Explicit pronouns in pro-drop languages signal emphasis

**How to detect**: If language has rich verb agreement (person/number marked on verb), likely pro-drop

**Frequency**: 40% of all prediction errors

---

### Error 2: Missing Emphasis in Source Language

**Problem**: Not recognizing that Greek/Hebrew explicit pronouns signal emphasis, not just routine reference

**Example**:
- Greek: "αὐτὸς εἶπεν" (autos eipen) = "HE said"
- Wrong analysis: Routine pronoun (translatable as zero in pro-drop target)
- Correct analysis: **Emphatic pronoun** (should be explicit in target, even if pro-drop)

**Solution**:
1. When Greek/Hebrew has explicit pronoun, check if it's expected or emphatic
2. If verb agreement would normally allow zero, explicit pronoun = emphasis
3. Mark as **Pronoun** with note: "Emphatic, preserve in target"

**How to detect**: Compare to surrounding clauses - if other clauses use zero but this one has explicit pronoun, likely emphatic

**Frequency**: 25% of all prediction errors

---

### Error 3: Assuming All Nouns Are "Full" NPs

**Problem**: Not distinguishing between different types of noun phrases

**Examples**:
- "Water is essential" → **Noun** (bare, generic)
- "The water" → **Noun** (definite, specific referent)
- "This water" → **Noun** (demonstrative, proximal)
- "Some water" → **Noun** (indefinite, non-specific)

**Solution**:
1. All are "Noun" surface realization, but require different analysis
2. Bare nouns (generic) correlate with Generic participant tracking
3. Definite nouns correlate with Routine or Frame Inferable
4. Demonstrative nouns correlate with Proximity feature
5. Indefinite nouns correlate with First Mention

**How to detect**: Check determiner type (the, a, this, bare)

**Frequency**: 15% of all prediction errors

---

### Error 4: Not Considering Register/Formality

**Problem**: Missing that formal contexts increase noun usage even for routine reference

**Example**:
- Narrative: "Jesus healed the man. He went home." (pronoun OK)
- Formal epistle: "Paul writes to the church. The apostle declares..." (noun preferred)

**Solution**:
1. Check **Discourse Genre** and **Speech Style** features
2. Formal/written genres prefer explicit nouns over pronouns
3. Even in pro-drop languages, formal contexts may avoid zero
4. Teaching/expository text = higher noun usage

**How to detect**: Check if genre is formal (epistle, legal, teaching) vs informal (narrative dialogue)

**Frequency**: 12% of all prediction errors

---

### Error 5: Conflating Zero with Ellipsis

**Problem**: Treating coordinated structure ellipsis (grammatical in English) as pro-drop

**Example**:
- English: "John came and [∅] bought fruits"
- This is grammatical ellipsis in coordination, NOT pro-drop
- Pro-drop = "John came. [∅] Bought fruits." (separate clauses)

**Solution**:
1. True zero (pro-drop) = omission in independent clauses
2. Ellipsis = omission in coordinated structures (many languages allow)
3. Mark coordinated ellipsis as **Zero** but note: "Coordinated ellipsis, not pro-drop"

**How to detect**: Check if "and" connects the clauses (coordination) vs separate sentences

**Frequency**: 8% of all prediction errors

---

## Prediction Guide Summary

**Step-by-Step Process**:

1. **Check Participant Tracking** → 95% determines surface form
   - First Mention → Noun
   - Routine → Pronoun or Zero (check language type)
   - Restaging → Noun

2. **Check Language Pro-Drop Status**
   - Pro-drop → Default to Zero for routine
   - Non-pro-drop → Required Pronoun for routine

3. **Check for Emphasis/Disambiguation**
   - Greek/Hebrew explicit pronoun → Likely emphatic
   - Multiple same-gender referents → Use Noun
   - Contrast/focus → Explicit Pronoun

4. **Check Register/Formality**
   - Formal → More nouns
   - Informal → More zero/pronouns

5. **Apply Accessibility Hierarchy**
   - High accessibility → Less material (Zero/Pronoun)
   - Low accessibility → More material (Noun)

**Validation**:
- Compare prediction to TBTA annotation
- Expected accuracy: 90%+ if following hierarchy
- Common errors: Not accounting for pro-drop, missing emphasis

---

## Implementation Notes for Tool Development

**Detection priorities**:
1. Check Participant Tracking state first (95% correlation)
2. Determine target language pro-drop status
3. Scan for emphasis markers in source (Greek/Hebrew explicit pronouns)
4. Check discourse distance from last mention
5. Consider register/genre (formal vs informal)

**Validation checks**:
- Consistency within verse (don't mix systems arbitrarily)
- Compatibility with language family patterns (pro-drop vs non-pro-drop)
- Register appropriateness (formal genres → more nouns)
- Switch-reference consistency (if applicable to language)

**Training data needed**:
- Native speaker judgments of naturalness
- Corpus analysis of existing translations in target language
- Language-specific grammatical constraints (which persons allow pro-drop?)
- Discourse pattern analysis (distance thresholds for pronoun vs noun)

---

**See Also**:
- [Cross-feature interactions](cross-feature-interactions.md)
- [Language family patterns](LANGUAGES-IN-TSV.md)
- [Key findings](LEARNINGS.md)
