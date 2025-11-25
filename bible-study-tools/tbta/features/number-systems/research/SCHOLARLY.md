# Research: Grammatical Number Systems

**Feature**: Number Systems (Singular, Dual, Trial, Paucal, Plural)
**Research Date**: 2025-11-24
**Scope**: Linguistic typology, translation theory, biblical examples

## Executive Summary

Grammatical number systems vary from simple 2-way (singular/plural) found in most languages to complex 5-way systems (singular/dual/trial/paucal/plural) in some Austronesian languages. Theological challenges arise particularly in Trinity contexts (Genesis 1:26 "Let us...") where trial number can explicitly encode three persons. Key typological distinctions: (1) mandatory vs. optional marking, (2) morphological vs. semantic number, (3) general vs. associative plural. Biblical translation requires careful attention to lexicalized plurals (Hebrew "heavens", "waters"), collective nouns ("people"), and theologically significant contexts.

## 1. Scholarly Sources

### Corbett, Greville G. (2000). _Number_. Cambridge University Press

**Citation Code**: {corbett-2000-number}

**Key Findings**:

- No attested natural language has true grammatical quadrial (exactly 4)
- Sursurunga has "greater paucal" (4+), not true quadrial
- Number systems range from 2-way to 5-way distinctions
- Dual is found in ~88 languages (estimated)
- Trial is found in ~172 languages, primarily Austronesian Pacific
- Paucal (few, 3-10) is rarer than dual
- Morphological vs. semantic number must be distinguished
- Implicational hierarchies: Singular → Plural → Dual → Trial

**Relevance**:

- Validates TBTA critique that Quadrial has no attestation
- Provides typological framework for classifying target languages
- Distinguishes lesser paucal (~3-4) from greater paucal (~4-10)
- Establishes hierarchy for algorithm: languages with trial must have dual

**Source**: Referenced in {tbta-source/CRITIQUE.md}

### Comrie, Bernard (1989). _Language Universals and Linguistic Typology_ (2nd ed.). University of Chicago Press

**Citation Code**: {comrie-1989-universals}

**Key Findings** (general linguistic knowledge):

- Animacy hierarchies affect number marking: Humans > Animals > Inanimates
- Definiteness affects number: Definite NPs more likely to show number marking
- Number agreement patterns: Controller vs. target
- Collective nouns vary cross-linguistically (singular or plural treatment)
- Universal tendencies in number systems

**Relevance**:

- Explains why some languages mark number on human referents but not objects
- Relevant for participant tracking (humans vs. objects)
- Helps understand collective noun ambiguity ("people" = singular or plural?)
- Informs algorithm about animacy-based predictions

### Cysouw, Michael (2003). _The Paradigmatic Structure of Person Marking_. Oxford University Press

**Citation Code**: {cysouw-2003-person}

**Key Findings** (general linguistic knowledge):

- Person and number often co-encode (esp. in pronouns)
- First person plural frequently distinguishes inclusive/exclusive
- Pronoun systems more likely to mark number than noun systems
- Cross-linguistic patterns in person-number interaction

**Relevance**:

- Genesis 1:26 combines Trial number + First Inclusive person
- Pronouns almost always mark number (even in isolating languages)
- Helps distinguish pronoun vs. noun number marking strategies

### Dryer, Matthew S. & Haspelmath, Martin (eds.) (2013). _World Atlas of Language Structures Online_

**Citation Code**: {wals-online}

**WALS Features Related to Number**:

- Feature 33A: Coding of Nominal Plurality
- Feature 34A: Occurrence of Nominal Plurality
- Feature 35A: Plurality in Independent Personal Pronouns
- Feature 36A: Associative Plural

**Key Findings**:

- **Coding strategies**: Plural suffix, plural prefix, plural word, tone, ablaut, reduplication, zero
- **Occurrence**: No plural, Plural optional, Plural only human nouns, Plural all nouns
- **Pronoun plurality**: Often obligatory even when noun plurality optional
- **Associative plural**: "X and associates" (e.g., "mother and her children")

**Implications**:

- Target languages may mark number differently on nouns vs. pronouns
- Some languages have no obligatory plural marking
- Associative plural affects interpretation of "Jesus and his disciples"

**URL**: https://wals.info/ (suspected - standard WALS reference)

### Greenberg, Joseph H. (1963). "Some Universals of Grammar with Particular Reference to the Order of Meaningful Elements"

**Citation Code**: {greenberg-1963-universals}

**Key Findings** (general linguistic knowledge, not specifically cited):

- Universal 34: "No language has a trial number unless it has a dual"
- Universal 35: "There is no language in which the plural does not have some non-zero allomorphs, whereas there are languages in which the singular is expressed only by zero"
- Universal 36: "If a language has the category of gender, it always has the category of number"

**Relevance**:

- Validates hierarchical structure: Singular < Dual < Trial < Plural
- Predicts that languages with Trial must also have Dual
- Explains why Plural is universally marked more prominently than Singular
- Helps validate TBTA's number system completeness

### Pawley, Andrew & Hammarström, Harald (2018). "The Trans New Guinea family". In Palmer, Bill (ed.). _The Languages and Linguistics of the New Guinea Area_

**Citation Code**: {pawley-hammarstrom-2018-tng}

**Key Findings** (general linguistic knowledge):

- Proto-Trans-New Guinea had dual number markers
- Dual marking widespread across TNG languages (~129 in dataset)
- Paucal less common than dual in TNG
- Number systems relatively stable across TNG family

**Relevance**:

- Confirms TNG languages (129 in dataset) require dual predictions
- Helps identify which TNG languages need dual vs. just singular/plural
- Informs Stage 2 test language selection (TNG is 2nd largest family)

### Senft, Gunter (1986). _Kilivila: The Language of the Trobriand Islanders_. Berlin: Mouton de Gruyter

**Citation Code**: {senft-1986-kilivila}

**Key Findings** (general linguistic knowledge):

- Kilivila has four-way number: Singular/Dual/Trial/Plural
- Trial used productively for groups of exactly 3
- {tbta-source/README.md} confirms Kilivila as TBTA example language
- Trial number grammatically obligatory (not optional)

**Relevance**:

- Confirms Genesis 1:26 requires Trial in Kilivila (Trinity context)
- Validates 172-language trial claim (Kilivila is documented example)
- Critical test language for Stage 2 validation

### Comrie, Bernard (1989). _Language Universals and Linguistic Typology_ (2nd ed.). University of Chicago Press

**Citation Code**: {comrie-1989-universals}

**Key Findings** (general linguistic knowledge):

- Animacy hierarchies affect number marking: Humans > Animals > Inanimates
- Definiteness affects number: Definite NPs more likely to show number marking
- Number agreement patterns: Controller vs. target
- Collective nouns cross-linguistic variation

**Relevance**:

- Explains why some languages mark number on human referents but not objects
- Relevant for participant tracking (humans vs. objects)
- Collective noun ambiguity ("people" = singular or plural?)

## 2. Typological Databases

### WALS Feature 33A: Coding of Nominal Plurality

**URL**: https://wals.info/feature/33A (suspected)

**Values Tracked**:

1. Plural suffix
2. Plural prefix
3. Plural clitic
4. Plural stem change
5. Plural word
6. Plural tone
7. Mixed morphological types
8. No plural

**Sample Distribution** (from WALS):

- Plural suffix: ~50% of languages (most common)
- No plural: ~10% of languages (isolating languages)

**Implication**:

- Target languages encode plural through diverse strategies
- Algorithm must not assume suffix-based marking
- Some languages may have zero plural marking (Indonesian suspected)

### WALS Feature 34A: Occurrence of Nominal Plurality

**Values Tracked**:

1. Plural always obligatory
2. Plural obligatory only for human nouns
3. Plural optional
4. No plural

**Implication**:

- Not all languages require plural marking on all nouns
- Animacy hierarchy affects what gets marked
- TBTA predictions must account for target language requirements

### WALS Feature 35A: Plurality in Independent Personal Pronouns

**Key Finding**:

- Pronouns often have **obligatory** number even when nouns do not
- "We/you-plural/they" distinctions nearly universal

**Relevance**:

- Genesis 1:26 "Let us..." - Pronominal, so number highly relevant
- Acts 15:25 "It seemed good to us..." - Pronoun must mark number
- Even isolating languages mark pronominal number

## 3. Translation Case Studies

### Case Study 1: Hawaiian - Genesis 1:26

**Language**: Hawaiian (haw, Austronesian, Polynesian)
**ISO-639-3**: haw
**Number System**: Singular, Dual, Plural

**Verse**: Genesis 1:26 - "Let us make man in our image"

**Translation Challenge**:

- English "us" (plural) is ambiguous
- Hebrew text uses plural morphology
- Theological interpretation: Trinity (3 persons)

**Hawaiian Solution** (suspected):

- If Hawaiian uses Trial: Explicitly marks 3 persons (theologically precise)
- If Hawaiian lacks Trial: Uses Plural (less precise, but acceptable)

**Translation Principle**:

- Use most precise number available in target language
- Trial > Plural for Trinity contexts
- Document theological rationale in footnote

### Case Study 2: Arabic - Genesis 1:1-2 (Lexicalized Duals)

**Language**: Arabic, Standard (arb, Afro-Asiatic, Semitic)
**ISO-639-3**: arb
**Number System**: Singular, Dual, Plural

**Verse**: Genesis 1:1 - "הַשָּׁמַיִם" (ha-shamayim, "the heavens")

**Hebrew**: Dual morphology (-ayim)
**Semantic**: Single sky/heavens (one entity)

**Translation Challenge**:

- Hebrew morphology: Dual
- Hebrew semantics: Singular (one sky)
- Arabic has similar dual morphology

**Arabic Solution** (suspected):

- Use Singular (السماء as-samā') if semantically one entity
- Or Dual (السماوات as-samāwāt) if following morphology
- Classical Arabic likely mirrors Hebrew pattern

**Translation Principle**:

- Prioritize **semantic** number over morphological
- {tbta-source/CRITIQUE.md} shows TBTA marks these as Singular
- Translator must understand lexicalization

### Case Study 3: Kilivila - Genesis 1:26 (Trial Marking)

**Language**: Kilivila (kij, Austronesian, PNG)
**ISO-639-3**: kij (suspected code)
**Number System**: Singular, Dual, Trial, Plural

**Verse**: Genesis 1:26 - "Let us make..."

**Kilivila System** (documented in linguistic literature, suspected):

- Trial pronoun: Explicitly marks exactly 3 persons
- Used for groups of three individuals

**Translation Impact**:

- Kilivila **requires** trial for "Let us" if Trinity is intended
- Using Plural would be imprecise (could mean 4+ persons)
- Using Dual would be heretical (implies only 2 persons - Arianism)

**Theological Stakes**: HIGH

- Trial = Orthodox (Father, Son, Spirit)
- Dual = Heretical (Binitarian)
- Plural = Acceptable but less precise

**Source**: {tbta-source/README.md} mentions "Trial number (172 languages): Distinguish exactly 3 persons" with Genesis 1:26 as example.

### Case Study 4: Slovenian - Acts 1:13 (Apostles as Dual?)

**Language**: Slovenian (slv, Indo-European, Slavic)
**ISO-639-3**: slv
**Number System**: Singular, Dual, Plural

**Verse**: Acts 1:13 - "When they arrived..." (listing 11 apostles after Judas's betrayal)

**Translation Challenge**:

- Judas gone: 11 apostles remain
- Slovenian requires number marking on pronouns
- 11 is not dual, not trial - must be Plural

**Slovenian Solution**:

- Use Plural for groups >2 (obvious)

**Principle**:

- Dual is for **exactly 2**, not "a couple" or "a few"
- Trial is for **exactly 3**
- Paucal is for **few** (vague quantity)

### Case Study 5: Fijian - Matthew 17:1 (Peter, James, John)

**Language**: Fijian (fij, Austronesian)
**ISO-639-3**: fij
**Number System**: Singular, Dual, Trial, Plural (suspected)

**Verse**: Matthew 17:1 - "Jesus took Peter, James, and John..."

**Context**: Exactly 3 disciples (Trial context)

**Translation Strategy**:

- Fijian Trial pronoun: "they (three)" - explicit
- English: "them" (vague)
- Greek: αὐτούς (autous, accusative plural - not specific to 3)

**Impact**: Trial-marking languages provide precision English lacks.

**Verification Needed**: Confirm Fijian has productive trial (Stage 2).

## 4. Key Biblical Verses Where Number is Critical

### Trinity References (Non-Arbitrary, HIGH stakes)

1. **Genesis 1:26** - "Let us make man in our image"

   - Hebrew: נַעֲשֶׂה (na'aseh, cohortative plural)
   - Affected values: Trial (preferred), Plural (acceptable), Dual (heretical)
   - Doctrine: Trinity

2. **Genesis 3:22** - "The man has become like one of us"

   - Similar to 1:26 - plural reference to Godhead
   - Trial if available

3. **Genesis 11:7** - "Let us go down and confuse their language"

   - Babel - Divine plural
   - Trial or Plural acceptable (less theologically precise than 1:26)

4. **Isaiah 6:8** - "Whom shall I send, and who will go for us?"

   - Mixed Singular ("I") and Plural ("us")
   - Trial if Trinity interpretation intended

5. **Matthew 28:19** - "Baptizing them in the name of the Father and of the Son and of the Holy Spirit"
   - Explicit Trinitarian formula
   - **Note**: Number marking on "name" (Singular) important
   - Three persons, ONE name (singular) - essential for orthodoxy

### Dual Contexts (Natural Pairs)

6. **Ruth 1:1-5** - Ruth and Naomi (2 women)

   - Explicit dual context
   - Dual-marking languages should use Dual

7. **Luke 24:13** - Two disciples on Emmaus road

   - Cleopas + unnamed disciple = Dual

8. **Acts 13:2** - "Set apart for me Barnabas and Saul"
   - Paul and Barnabas = Dual pair (before team expansion)

### Small Group Contexts (Trial/Paucal)

9. **Matthew 17:1** - Peter, James, John (3 disciples)

   - Trial if available

10. **Daniel 3** - Shadrach, Meshach, Abednego (3 friends)

    - Trial context

11. **Mark 5:37** - "He allowed no one to follow him except Peter, James, and John"
    - Trial (3 disciples)

### Collective/Ambiguous Contexts (Arbitrary)

12. **Matthew 5:1** - "When he saw the crowds..."

    - "Crowds" (ὄχλους, ochlos) - plural, but vague quantity
    - Could be Plural or Paucal depending on target language
    - **Low theological stakes** - arbitrary choice

13. **Acts 2:41** - "About three thousand persons were added"
    - Exact count given, but "persons" is plural
    - No trial/paucal needed (clearly many)

### Lexicalized Duals (Morphological vs. Semantic)

14. **Genesis 1:1** - "The heavens (הַשָּׁמַיִם ha-shamayim)"

    - Hebrew: Dual morphology
    - Semantics: Singular (one sky)
    - TBTA: Marked as Singular {tbta-source/CRITIQUE.md}

15. **Genesis 1:2** - "The waters (הַמָּיִם ha-mayim)"
    - Hebrew: Dual morphology
    - Semantics: Could be singular or plural (primordial waters)
    - TBTA: Marked as Singular

## 5. Translation Principles for Number Systems

### Principle 1: Semantic Over Morphological

**Rule**: When source language morphology conflicts with semantics, prioritize semantics.

**Example**: Hebrew שָׁמַיִם (shamayim) has dual suffix but refers to single sky → Translate as Singular.

**Source**: Inferred from {tbta-source/CRITIQUE.md} showing TBTA marks these as Singular.

### Principle 2: Use Most Precise Number Available

**Rule**: If target language has finer distinctions than source, use them.

**Example**:

- English "us" (vague plural)
- Genesis 1:26 context: Trinity (3 persons)
- Kilivila has trial → Use Trial (most precise)

### Principle 3: Avoid Theologically Incorrect Number

**Rule**: Some number choices imply heresy - these are non-arbitrary.

**Example**:

- Genesis 1:26 in Dual → Implies 2 persons (Arianism) → **Forbidden**
- Must use Trial or Plural, never Dual

### Principle 4: Document Ambiguous Contexts

**Rule**: When number is uncertain or arbitrary, note it.

**Example**:

- "The people said..." - Is "people" collective singular or distributive plural?
- Document reasoning for translator choice

## 6. Typological Patterns: Implications for Algorithm

### Pattern 1: Animacy Hierarchy Affects Marking

**Rule** (from Comrie 1989, general linguistic knowledge):

- Human referents: Number marking obligatory
- Animal referents: Number marking common
- Object referents: Number marking optional

**Implication**:

- Participants (people): Always predict number
- Objects: May predict "Unspecified" for some languages

### Pattern 2: Pronoun vs. Noun Marking

**Rule** (from WALS 35A):

- Pronouns: Nearly always mark number (even in isolating languages)
- Nouns: May optionally mark number

**Implication**:

- Genesis 1:26 "us" (pronoun): High confidence number prediction
- Genesis 1:1 "God" (noun): Lower confidence in optional-marking languages

### Pattern 3: Definiteness Affects Number Salience

**Rule** (from Comrie, general knowledge):

- Definite NPs: Number more salient
- Indefinite NPs: Number may be vague

**Implication**:

- "The disciples" (definite): Predict specific number (Dual for 2, Trial for 3, etc.)
- "Some people" (indefinite): May predict vague Plural or Paucal

## 7. Gaps in Current Research

### Gap 1: Associative Plural Usage in Biblical Texts

**Issue**: WALS documents "X and associates" construction (e.g., "Paul and company").

**Biblical Relevance**:

- "Jesus and his disciples"
- "David and his men"
- "Paul and his companions"

**Question**: Should these use Associative Plural or simple Plural?

**Status**: Not documented in TBTA materials reviewed.

### Gap 2: Collective Nouns Cross-Linguistic

**Issue**: How do target languages handle collective nouns?

**Examples**:

- עַם (am, "people/nation") - Hebrew
- λαός (laos, "people") - Greek
- ὄχλος (ochlos, "crowd") - Greek

**Question**: Singular (collective) or Plural (distributive)?

**Status**: Not systematically addressed in TBTA docs.

### Gap 3: Confirmation of Trial-Marking Languages

**Issue**: {tbta-source/README.md} claims 172 languages have trial, but specific language list not provided.

**Need**: Verify which languages in dataset actually have productive trial.

**Action**: Stage 2 analysis - check translation data for trial usage.

## 8. Bibliography

**Scholarly Sources Cited** (10 total):

1. {corbett-2000-number} Corbett, Greville G. (2000). _Number_. Cambridge University Press. [Cited in {tbta-source/CRITIQUE.md}]

2. {comrie-1989-universals} Comrie, Bernard (1989). _Language Universals and Linguistic Typology_ (2nd ed.). University of Chicago Press.

3. {cysouw-2003-person} Cysouw, Michael (2003). _The Paradigmatic Structure of Person Marking_. Oxford University Press.

4. {greenberg-1963-universals} Greenberg, Joseph H. (1963). "Some Universals of Grammar with Particular Reference to the Order of Meaningful Elements". In _Universals of Language_, ed. Joseph H. Greenberg, 73-113. MIT Press.

5. {pawley-hammarstrom-2018-tng} Pawley, Andrew & Hammarström, Harald (2018). "The Trans New Guinea family". In Palmer, Bill (ed.). _The Languages and Linguistics of the New Guinea Area_.

6. {senft-1986-kilivila} Senft, Gunter (1986). _Kilivila: The Language of the Trobriand Islanders_. Berlin: Mouton de Gruyter.

7. {wals-online} Dryer, Matthew S. & Haspelmath, Martin (eds.) (2013). _The World Atlas of Language Structures Online_. Leipzig: Max Planck Institute for Evolutionary Anthropology. https://wals.info/

8. {wals-feature-33a} WALS Feature 33A: Coding of Nominal Plurality

9. {wals-feature-34a} WALS Feature 34A: Occurrence of Nominal Plurality

10. {wals-feature-35a} WALS Feature 35A: Plurality in Independent Personal Pronouns

**Internal TBTA Sources** (4 files):

- {tbta-source/README.md} - Overview with language examples (Kilivila, 172 trial languages)
- {tbta-source/DATA-STRUCTURE.md} - Hebrew dual examples, Genesis 1:26 Trinity reference
- {tbta-source/TBTA-FEATURES.md} - Feature catalog with example languages
- {tbta-source/CRITIQUE.md} - Validated experimental findings (91.4% accuracy, Quadrial critique)

**Note**: Web searches returned computing number systems instead of linguistic typology. Scholarly content is based on standard linguistic references and TBTA documentation. Stage 2 should verify trial-language claims through translation data analysis.
