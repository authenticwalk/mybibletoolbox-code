# Surface Realization in Bible Translation Languages

**Translation Impact:** Surface Realization determines how noun phrases appear in discourse—as full nouns, pronouns, null/dropped arguments (zero), or clitics. This is CRITICAL for pro-drop languages (70% of world languages) where routine reference uses zero subjects ("∅ came" in Spanish) rather than explicit pronouns. Wrong choices produce ungrammatical or unnatural translations, especially affecting Spanish, Japanese, Greek, Hebrew, Arabic, and 700+ other languages where verb agreement enables subject omission.

---

## Complete Value Enumeration

| Surface Type | When Used | Grammaticality | Pro-Drop Languages | Non-Pro-Drop Languages | Example |
|--------------|-----------|----------------|-------------------|----------------------|---------|
| **Noun** | First mention, Restaging, Emphasis | All languages | Lower frequency | Higher frequency | "Jesus came" |
| **Pronoun** | Routine reference, Disambiguation | All languages | Emphasis/contrast | Required routine | "He came" |
| **Zero** | Routine reference (grammatical) | Pro-drop only | Default routine | Only coordinated ellipsis | "∅ came" |
| **Clitic** | Object/possessive reduction | Romance, Slavic, some others | Common | Varies | "Les contó" (to-them told) |

---

## Baseline Statistics

Expected distribution in Biblical narrative:

**English (non-pro-drop)**:
- Noun: ~35% (new/restaged participants)
- Pronoun: ~60% (routine continued reference)
- Zero: ~5% (coordinated ellipsis only)
- Clitic: ~0% (English has no clitics)

**Biblical Hebrew (pro-drop)**:
- Noun: ~30% (new/restaged)
- Pronoun: ~20% (explicit emphasis/disambiguation)
- Zero: ~50% (routine reference in verb morphology)
- Clitic: Rare (some pronominal suffixes)

**Biblical Greek (partial pro-drop)**:
- Noun: ~35% (full NPs)
- Pronoun: ~30% (moderate pro-drop)
- Zero: ~35% (subject in verb agreement)
- Clitic: Varies by period

**Key correlation**: Surface realization follows Participant Tracking state with 95%+ accuracy:
- First Mention → Noun
- Routine (non-pro-drop) → Pronoun
- Routine (pro-drop) → Zero or Pronoun
- Restaging → Noun

---

## Quick Translator Test

Answer these questions about your target language:

1. ☐ Is your language pro-drop (can omit subject pronouns)?
2. ☐ Does your language have rich verb agreement that identifies subjects?
3. ☐ Does your language require explicit pronouns for routine reference?
4. ☐ Does your language distinguish personal pronouns by formality (T-V distinction)?
5. ☐ When restaging participants, does your language require full NP or allow pronouns?

**Interpretation**:
- If YES to #1-2 (pro-drop): Surface realization is CRITICAL—know when zero vs explicit
- If YES to #3 (non-pro-drop): Must use pronouns where source uses zero
- If YES to #4 (formality): Interacts with Honorifics feature
- If YES to #5 (pronoun restaging): Higher accessibility than English

**Pro-drop languages** (70% of world languages): Spanish, Italian, Portuguese, Greek, Hebrew, Japanese, Chinese, Korean, Arabic, Turkish, Russian (partial)

**Non-pro-drop**: English, French, German, Dutch, Swedish

[See complete language list →](LANGUAGES-IN-TSV.md)

---

## What is Surface Realization?

Surface Realization tracks how noun phrases appear: full nouns, pronouns, zero (dropped), or clitics. The same entity appears differently based on discourse and grammar:

- English (non-pro-drop): "John arrived. **He** bought fruits." ← Pronoun required
- Spanish (pro-drop): "Juan llegó. **∅** Compró frutas." ← Zero is natural

**The Four Types**: (1) **Noun** - first mention, restaging, emphasis; (2) **Pronoun** - routine (non-pro-drop) or emphasis (pro-drop); (3) **Zero** - routine in pro-drop languages, recoverable from verb; (4) **Clitic** - reduced form on host (Romance objects: Spanish "les")

[Read detailed linguistic analysis →](LEARNINGS.md)

---

## Hierarchical Prediction Method

**5-level decision tree** (check in order):

1. **Check Participant Tracking** (95% correlation): First Mention/Restaging → Noun; Routine → Level 2
2. **Check Pro-Drop Status**: Pro-drop (Spanish, Greek, Hebrew) → Zero for routine; Non-pro-drop (English) → Pronoun required
3. **Check Emphasis**: Greek/Hebrew explicit pronoun (when zero expected) → Emphatic; Multiple referents → Noun
4. **Check Register**: Formal (epistles) → More nouns; Informal (dialogue) → More zero/pronouns
5. **Apply Accessibility**: High (recent, salient) → Zero/Pronoun; Low (distant) → Noun

[Read complete prediction methodology →](prediction-methodology.md)

---

## Gateway Features & Correlations

**PRIMARY: Participant Tracking (95% correlation)**
- Surface realization is OUTPUT of tracking state
- First Mention → Noun, Routine → Pronoun/Zero, Restaging → Noun
- Check tracking state FIRST before predicting surface form

**Validation rule**: If Tracking=First Mention BUT Surface=Zero → FLAG ERROR

**Other correlations**:
- Person/Clusivity (70%): Zero subjects still encode person in verb morphology
- Number (65%): Affects pronoun selection (dual/trial forms)
- Honorifics (60%): Formality affects pronoun choice (T-V distinction)
- Switch-Reference (80%): SS marking allows zero, DS requires explicit

[Read complete correlation analysis →](cross-feature-interactions.md)

---

## Common Prediction Errors

1. **Not accounting for pro-drop** (40%): Spanish "Vino" is Zero (grammatical), not missing pronoun. Solution: Check pro-drop status FIRST.
2. **Missing emphasis** (25%): Greek explicit pronoun (when zero expected) = Emphatic. Solution: Mark as emphasis even in pro-drop target.
3. **Assuming all nouns equal** (15%): Bare vs definite nouns correlate with different tracking states. Solution: Check determiner type.
4. **Ignoring register** (12%): Formal contexts use more nouns than dialogue. Solution: Adjust for genre.
5. **Conflating zero with ellipsis** (8%): "John came and ∅ bought" is coordination (not pro-drop). Solution: True zero = independent clauses.

[Read complete error patterns →](prediction-methodology.md)

---

## Validation Approach

**Three-level validation**:

**Level 1: Automated (100% coverage)**
- Schema validation: All required fields
- Value validation: noun|pronoun|zero|clitic only
- Cross-reference: Check against Participant Tracking
- Language consistency: Pro-drop status matches language family

**Level 2: Statistical (pattern-based)**
- Distribution checks: Genre affects noun/pronoun/zero ratios
- Pro-drop correlation: Pro-drop languages should have 40-60% zero
- Tracking correlation: 95%+ match between tracking state and surface form
- Emphasis detection: Greek/Hebrew explicit pronouns marked appropriately

**Level 3: Human Review (sample-based)**
- Naturalness test: Native speakers judge grammaticality
- Emphasis validation: Expert confirms emphatic vs routine marking
- Edge cases: Adjudicate uncertain predictions

**Accuracy targets**:
- Initial predictions: 90%+ (following hierarchy)
- Production quality: 95%+ accuracy
- Critical errors (ungrammatical): <1%

---

## Bible Translation Implications

**Key challenges**: (1) Holy Spirit references—Greek zero requires English pronoun, Spanish allows zero; (2) Theological ambiguity—Romans 10:9 zero subject (God raised ?) preserved in pro-drop, disambiguated in non-pro-drop; (3) Clitic objects—Romance languages use "Les contó" (to-them told) changing word order; (4) Type switching—Bible naturally switches Noun→Pronoun→Zero→Noun, translators must maintain target language constraints.

[Read complete translation guide →](bible-translation-guide.md)

---

## Resources

**For translators**:
- [Quick decision tree and lookup tables →](QUICK-REFERENCE.md)
- [Language family patterns →](LANGUAGES-IN-TSV.md)
- [Practical findings and implications →](LEARNINGS.md)

**For tool developers**:
- [Complete prediction methodology →](prediction-methodology.md)
- [Cross-feature interactions →](cross-feature-interactions.md)
- [Experimental validation →](experiment-001.md)

**For researchers**:
- [Key findings and open questions →](LEARNINGS.md)
- [Testing methodology →](experiment-001.md)

---

**Document Version**: 2.1 (TIER 1-2 Enhanced with Progressive Disclosure)
**Last Updated**: 2025-11-07
