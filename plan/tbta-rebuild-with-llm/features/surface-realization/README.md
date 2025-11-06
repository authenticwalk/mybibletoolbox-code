# Surface Realization in Bible Translation Languages

## Executive Summary

Surface Realization describes how noun phrases appear in actual discourse - whether they manifest as full nouns, pronouns, null/dropped arguments (pro-drop), or clitics. This feature is critical for languages with null subject parameters, pro-drop constraints, and pronoun deletion rules. Understanding surface realization patterns is essential for accurate, natural-sounding translations across diverse linguistic systems.

The TBTA Surface Realization feature tracks four distinct realization types:
1. **Noun**: Full lexical noun appears
2. **Pronoun**: Pronoun appears (explicit reference)
3. **Zero**: Dropped/null (no surface form, but understood contextually)
4. **Clitic**: Reduced form attached to another word

**Translation Impact**: ⭐⭐⭐⭐⭐ CRITICAL for pro-drop languages (Spanish, Japanese, Greek, Hebrew, Mandarin), topic-prominent languages (Japanese, Korean), and ergative languages. Surface realization choices directly determine grammaticality and naturalness.

---

## Baseline Statistics

Expected distribution in Biblical narrative:

**English** (non-pro-drop):
- Noun: ~35% (full NPs for new/restaged participants)
- Pronoun: ~60% (routine continued reference)
- Zero: ~5% (ellipsis in coordinated structures)

**Biblical Hebrew** (pro-drop):
- Noun: ~30% (full NPs for new/restaged)
- Pronoun: ~20% (explicit emphasis/disambiguation)
- Zero: ~50% (routine continued reference in verb)

**Biblical Greek** (partial pro-drop):
- Noun: ~35% (full NPs)
- Pronoun: ~30% (moderate pro-drop)
- Zero: ~35% (subject in verb morphology)

**Genre variation**:
- Narrative: Higher noun usage (introducing characters)
- Dialogue: Higher pronoun usage (established participants)
- Teaching: More explicit nouns (clarity over conciseness)

**Key principle**: Surface realization correlates 95%+ with **Participant Tracking** state. First Mention → Noun, Routine → Pronoun/Zero, Restaging → Noun.

---

## Quick Translator Test

Answer these questions about your target language:

1. ☐ Is your language pro-drop (can omit subject pronouns)?
2. ☐ Does your language have rich verb agreement that identifies subjects?
3. ☐ Does your language require explicit pronouns for routine reference?
4. ☐ Does your language distinguish personal pronouns by formality (T-V distinction)?
5. ☐ When restaging participants, does your language require full NP or allow pronouns?

**Interpretation**:
- If YES to #1-2 (pro-drop): Surface realization annotation is CRITICAL for knowing when to use zero vs explicit forms
- If YES to #3 (non-pro-drop): You must use pronouns where source languages use zero
- If YES to #4 (formality): Surface realization interacts with Honorifics feature
- If YES to #5 (pronoun restaging): Your language has higher accessibility than English

**Pro-drop languages**: Spanish, Italian, Portuguese, Greek, Hebrew, Japanese, Chinese, Korean, Arabic, Turkish, Russian (partial)
**Non-pro-drop**: English, French, German, Dutch, Swedish

---

## What is Surface Realization?

Surface Realization refers to the phonologically realized form of a noun phrase in a sentence. The same semantic entity can appear in different ways depending on context, discourse, and language-specific rules.

### Example: English vs Spanish

**English (Non-pro-drop):**
```
Speaker: "John arrived at the market."
Response: "He bought fruits there."  ← Must use pronoun "he"
         NOT "Bought fruits there."   ← Ungrammatical without subject
```

**Spanish (Pro-drop):**
```
Hablante: "Juan llegó al mercado."
Response: "Compró frutas allí."      ← Pronoun can be dropped (zero)
         "Él compró frutas allí."    ← Or explicitly stated (pronoun)
```

The semantic meaning is identical, but Spanish allows zero realization while English requires overt pronouns for most persons/numbers.

---

## Surface Realization Types in TBTA

### Type 1: Noun
Full lexical noun phrase appears in surface position.

**When to use:**
- First introduction of character/entity
- Emphasis or contrast
- Formal register
- Disambiguation needed

**Languages that prefer this:**
- Non-pro-drop languages (English, German, Dutch)
- When introducing new referents (first mention)
- In formal or emphatic contexts

### Type 2: Pronoun
Explicit pronoun (standalone or clitic-like) appears.

**When to use:**
- Established referent, no emphasis
- When zero would be ungrammatical
- Clarification contexts
- Certain syntactic positions (fronted objects, non-adjacent antecedents)

**Languages that commonly use pronouns:**
- Non-pro-drop languages (required for grammaticality)
- Pro-drop languages for emphasis or disambiguation

### Type 3: Zero (Pro-drop)
The argument is not realized phonologically but is understood from context.

**Conditions for zero realization:**
1. **Recoverability**: Antecedent must be clear from discourse
2. **Agreement morphology**: Verb must have rich enough agreement
3. **Language-specific rules**: Some languages restrict zero to certain persons
4. **Syntactic position**: Main clause subjects are most common
5. **Discourse status**: Established, salient, or generic referents

**When NOT to use zero:**
- First introduction of character
- Ambiguous antecedents
- Subject changes in non-switch-reference languages
- In non-pro-drop languages

### Type 4: Clitic
Reduced pronoun form attached to a host word (usually verb).

**Languages with systematic clitics:**
- Romance languages (Spanish, French, Italian, Portuguese)
- Slavic languages (some)
- Greek (Modern)
- Balkan languages (extensive system)

**Properties of clitics:**
- Phonologically dependent on host
- Typically follow special ordering rules
- May have limited case/number distinctions
- Can stack/double (multiple clitics per verb)

---

## Hierarchical Prediction Prompt Template

Surface realization is highly predictable using this 5-level decision process:

### Level 1 - Check Participant Tracking State
Surface realization correlates strongly with tracking (95%+ correlation):

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

## Gateway Features & Correlations

Surface realization is the OUTPUT of participant tracking. Check tracking state FIRST:

### Strong Correlation with Participant Tracking (95%+)

| Tracking State | Surface Form | Confidence | Notes |
|---------------|-------------|------------|-------|
| First Mention | **Noun** | 95%+ | Introducing new referent |
| Routine | **Pronoun** / **Zero** | 90%+ | Depends on pro-drop status |
| Restaging | **Noun** | 85%+ | Reintroducing after absence |
| Frame Inferable | **Noun** (definite) | 90%+ | "The priest" (role-based) |
| Generic | **Noun** (often bare) | 85%+ | "Water is essential" |
| Offstage | **Noun** (modifier) | 95%+ | "Peter's house" |

### Predicting from Source Language

**Greek/Hebrew explicit pronoun** → Unusual, signals:
- Emphasis (αὐτός = "HE himself")
- Contrast ("Not you, but HE")
- Disambiguation

**Greek/Hebrew zero** → Normal routine reference
- Cannot infer emphasis from absence
- Target language may require pronoun (if non-pro-drop)

**English always explicit** → Cannot infer emphasis
- English "he" could be routine or emphatic
- Check Greek/Hebrew source for emphasis signals

### Correlation with Person/Clusivity

Pro-drop languages with zero subjects:
- Person still encoded in verb morphology
- 1st plural zero → Check **Clusivity** feature separately
- Example: Spanish "Vamos" (go-1PL) = zero subject, but inclusive/exclusive distinction may matter

### Correlation with Number

Pronoun selection depends on number:
- Dual/trial/paucal languages → Special pronoun forms
- Greek/Hebrew encode number in verb morphology
- Affects pro-drop: "They" vs "The two of them" (dual)

---

## Common Prediction Errors

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

---

## Cross-Feature Interactions

### Surface Realization + Participant Tracking (PRIMARY - 95% correlation)
**Relationship**: Near-perfect correlation
- Tracking state predicts surface form reliably
- Use tracking as primary predictor

**Validation rule**: If Tracking = First Mention but Surface = Zero → FLAG ERROR (except in rare contexts like diary style)

---

### Surface Realization + Person/Clusivity
**Relationship**: Clusivity applies even when subject is zero

**Example**:
- Spanish: "[∅] Vamos" = "We (inclusive/exclusive?) go"
- Surface = **Zero**, but person = 1PL, clusivity = TBD

**Important**: For pro-drop languages with zero subjects:
1. Zero surface form does NOT mean person is unspecified
2. Person/number encoded in verb morphology
3. Clusivity distinction still matters for translation
4. Must analyze verb agreement, not just surface form

---

### Surface Realization + Number
**Relationship**: Number affects pronoun selection

**Dual/trial/paucal languages**:
- "The two disciples" → If pronoun used, must be dual form
- Hebrew/Greek encode number in verb morphology
- Affects pro-drop: Number visible in verb even when subject is zero

**Example**:
- Greek: "ἦλθον" (elthon) = "came-3PL" (zero subject, plural)
- Target with dual: Must check if exactly 2 or more than 2
- Dual form required if exactly 2

---

### Surface Realization + Honorifics/Register
**Relationship**: Formality affects pronoun choice and noun usage

**T-V distinction languages** (French tu/vous, Spanish tú/usted):
- Pronoun selection depends on social distance
- Formal → May use title + name instead of pronoun
- Example: "The teacher said" (formal) vs "He said" (informal)

**Japanese/Korean honorific systems**:
- Pronoun choice dramatically affected by formality
- High-formality contexts may avoid pronouns entirely
- Use title/role noun instead: "The teacher" (not "he")

**Biblical application**:
- Prayers to God → High formality (many languages)
- May prefer nouns over pronouns even for routine reference
- Example: "The Lord" repeated instead of "He"

---

### Surface Realization + Switch-Reference
**Relationship**: Switch-reference systems interact with surface realization

**Languages with switch-reference** (many Papuan, some Mayan):
- Marking on verb indicates if subject is same or different from previous clause
- Same-subject (SS) marker → Often allows zero
- Different-subject (DS) marker → May require noun or pronoun

**Example** (Amele, Papua New Guinea):
- "John came-SS [∅] ate" → Same subject, zero OK
- "John came-DS Mary ate" → Different subject, must be explicit

**Validation**: If language has switch-reference, check consistency between switch-reference marking and surface realization

---

### Surface Realization + Proximity (Demonstratives)
**Relationship**: Demonstrative determiners affect noun phrase form

**When noun appears with demonstrative**:
- "This man" → Surface = **Noun**, Proximity = Near
- "That man" → Surface = **Noun**, Proximity = Far

**Cannot use zero/pronoun with demonstrative**:
- Must be full noun phrase
- Demonstrative + noun = single constituent

**Languages with demonstrative pronouns**:
- "This one" → Some analyses: Pronoun with demonstrative
- TBTA analysis: Treat as **Pronoun** (the head is pronominal)

---

## Languages from TSV with Pro-Drop Characteristics

**High Pro-Drop** (extensive null subject systems):
- East Asian: Mandarin, Japanese, Korean, Vietnamese, Thai, Burmese
- Romance: Spanish, Italian, Portuguese, Catalan
- Afro-Asiatic: Arabic, Hebrew
- Other: Greek, Turkish, Persian, Quechua

**Moderate Pro-Drop** (some contexts):
- Slavic: Russian (3rd person), Bulgarian, Serbian
- Trans-New Guinea: Many languages (chain clauses)
- Austronesian: Indonesian, Malay, Tagalog (varies)

**Non-Pro-Drop or Minimal**:
- Germanic: English, German, Dutch, Swedish
- Some Niger-Congo: Many Bantu languages

See LANGUAGES-IN-TSV.md for complete typological breakdown by language family.

---

## Discourse Factors Affecting Surface Realization

### 1. Givenness/Information Status
Based on Ariel's Accessibility Hierarchy:

**Accessibility Scale** (most to least):
1. Zero / Unstressed pronoun (highest accessibility)
2. Stressed pronoun
3. Demonstrative pronoun
4. Definite description
5. Indefinite description (lowest accessibility)

**Application**:
- New/Unknown → Noun (indefinite): "A rabbi came"
- Given/Known → Pronoun/Zero: "He taught" or "[∅] Taught"
- Accessible/Inferrable → Definite noun: "The rabbi"

### 2. Distance from Antecedent
- Adjacent (0-1 clauses): Zero most common (pro-drop languages)
- Nearby (2-3 clauses): Pronoun common
- Distant (4+ clauses): Noun preferred for clarity

**Language variation**:
- Japanese: Allows zero even at distance if salient
- English: Requires noun if 3+ clauses away
- Spanish: Intermediate (zero for salient topics at moderate distance)

### 3. Semantic Role and Saliency
- Agents: Pro-drop more likely
- Patients: May require more explicit marking
- Inanimate: More likely to require explicit marking
- Salient characters (Jesus, God): Pro-drop more likely even at distance

### 4. Register and Style
- Formal written: More nouns, more explicit
- Informal spoken: More pro-drop, more pronouns
- Narrative: Often high use of zero (pro-drop languages)
- Direct speech: More pronouns for clarity

---

## Bible Translation Implications

### Problem 1: The Holy Spirit Reference Problem
**Greek**: "To pneuma ho hagios" → Often understood with dropped pronouns in following clauses

**Translation choices**:
- English (non-pro-drop): "The Holy Spirit" (explicit noun) or "He" (pronoun)
- Spanish (pro-drop): "El Espíritu Santo" (noun), "Él" (pronoun), or "[∅]" (zero)
- Japanese (high pro-drop): Extensive zero use possible

### Problem 2: Theological Ambiguity
Some passages use zero subjects in source language, creating intentional ambiguity.

**Example - Romans 10:9** (Greek has ambiguous subject):
- Could be: God raised Jesus, OR God raised us, OR God raised the dead generally
- Pro-drop languages may preserve ambiguity
- Non-pro-drop languages must disambiguate (forced to choose referent)

### Problem 3: The Clitic Object Problem
**Spanish/Italian/Portuguese**: Objects often appear as clitics, changing word order

**Example**:
```
English: "He told them the story"
Spanish: "Les contó la historia" (to-them told the story) ← clitic "les"
         "Se la contó" (to-them it told) ← double clitics
```

Must choose:
- Full object NP: "a ellos" (to them)
- Clitic: "les"
- Zero: Only in limited contexts

### Problem 4: Switching Between Realization Types
Bible discourse switches between realization types naturally:

```
New character: "A woman came to the well"      [Noun - First Mention]
Continues: "She drank water"                   [Pronoun - Routine]
Later: "[∅] Returned to her home"              [Zero - Routine, pro-drop]
Topic shift: "Jesus asked the woman..."        [Noun - Restaging]
```

Translators must ensure consistency within target language constraints.

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

## Resources for Further Study

### Linguistic Background
- Ariel, Mira (1990). "Accessing Noun-Phrase Antecedents" - Accessibility Hierarchy
- Huang, C.-T. James (1984). "On the Distribution and Reference of Empty Pronouns" - Pro-drop theory
- Rizzi, Luigi (1986). "Null Objects in Italian and the Theory of pro" - Romance clitics

### For This Project
- LEARNINGS.md - Experimental findings and edge cases
- LANGUAGES-IN-TSV.md - Full typological breakdown by family
- QUICK-REFERENCE.md - Fast lookup for common translation scenarios
- INDEX.md - Cross-references to related features

---

## Notes for Tool Development

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

**Document Version**: 2.0 (TIER 1-2 Enhanced)
**Last Updated**: 2025-11-06
**See Also**:
- LEARNINGS.md (experimental findings)
- participant-tracking/README.md (gateway feature)
- FEATURE-IMPROVEMENT-CHECKLIST.md (quality framework)
