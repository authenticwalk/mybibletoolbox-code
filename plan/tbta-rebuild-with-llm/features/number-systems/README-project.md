# Grammatical Number Systems in TBTA

## Overview

TBTA encodes six distinct grammatical number values for biblical text annotation:

1. **Singular (S)** - One entity
2. **Dual (D)** - Exactly two entities
3. **Trial (T)** - Exactly three entities
4. **Quadrial (Q)** - Exactly four entities
5. **Paucal (p)** - A few entities (small, indefinite number, typically 3-10)
6. **Plural (P)** - Many entities (large or indefinite number)

These distinctions are critical for Bible translation into languages that grammatically mark number categories beyond the simple singular/plural distinction found in English and most Indo-European languages.

## Research Date
2025-11-05

## 1. SINGULAR (S)

### Definition
Refers to exactly one entity.

### Cross-linguistic Status
- **Universal**: Present in virtually all languages
- **Marking**: Often unmarked (zero morpheme) in most languages
- **Biblical Source Languages**: Both Biblical Hebrew and Koine Greek mark singular

### In Our Dataset
All 1009 languages distinguish singular from non-singular in some way.

---

## 2. DUAL (D)

### Definition
A grammatical number referring to precisely two entities, typically when they form a natural pair or act in unison.

### Language Families with Dual

#### Ancient Languages (Biblical Context)
**Biblical Hebrew** {bib-heb}
- **Status**: Productive dual system, especially for natural pairs
- **Morphology**: Suffix -ַיִם (-ayim) in absolute state, -ֵי (-ê) in construct state
- **Usage**:
  - Natural pairs: eyes (עֵינַיִם), ears, hands, feet
  - Time expressions: two days, two years
  - Numbers: 2, 12, 20, 200, etc.
- **Restriction**: Confined primarily to nouns that naturally occur in pairs
- **Citation**: {gesenius-1910}, {unfoldingword-uhg}

**Koine Greek** {grc-koine}
- **Status**: Virtually disappeared in New Testament Greek
- **Remnants**: Only survives in:
  - Genitive of δύο (two): δυοῖν (dyoīn)
  - Numeral ὀκτώ (eight) - from "two pairs of sharp points"
- **Classical Greek**: More common in Homer and Attic, but already declining
- **Citation**: {moulton-1908}, {blass-1961}

**Note**: Since Koine Greek has essentially lost the dual, TBTA dual annotations for NT Greek likely represent semantic interpretation rather than morphological marking.

#### Modern Indo-European Languages

**Slovene** {slv} ✓ IN DATASET
- **Status**: Fully productive dual across all inflected categories
- **Morphology**: Distinct dual forms for nouns, verbs, adjectives, pronouns
- **Obligatoriness**: Mandatory when referring to exactly two entities
- **Unique Status**: One of only two Slavic languages preserving productive dual
- **Citation**: {jakop-2016}, {britannica-dual}

**Sorbian** (Upper and Lower)
- **Status**: Fully productive dual
- **Geographic**: Germany (Lusatia region)
- **ISO 639-3**: hsb (Upper Sorbian), dsb (Lower Sorbian)
- **Not in our dataset** (no Bible translation)
- **Citation**: {britannica-dual}

**Lithuanian** {lit} ✓ IN DATASET
- **Status**: Remnant dual forms in fixed expressions
- **Usage**: Limited to certain nouns, especially natural pairs
- **Modern trend**: Declining use, being replaced by plural
- **Citation**: {linguistics-se-dual}

**Scottish Gaelic, Irish**
- **Status**: Archaic dual forms preserved in some contexts
- **Not systematically in our dataset**
- **Citation**: {wikipedia-dual}

#### Other Indo-European (Ancient)
- Sanskrit: Obligatory dual (Vedic Sanskrit)
- Old Church Slavonic: Obligatory dual
- Gothic, Old English: Had dual forms

### In Our Dataset
**Confirmed dual languages**:
- Slovene (slv) - productive
- Lithuanian (lit) - remnant

**Potential investigation needed**:
- Other Slavic languages for dual remnants in two-word contexts
- 135 Indo-European languages total in dataset

---

## 3. TRIAL (T)

### Definition
A grammatical number referring to exactly three entities.

### Language Families with Trial

#### Austronesian (Oceanic subgroup)

Our dataset contains **176 Austronesian languages**, making this the largest family.

**Larike** {lar}
- **Status**: True trial (not paucal)
- **System**: Singular - Dual - Trial - Plural
- **Scope**: Free pronouns only (human referents)
- **Note**: "Larike trials are true trial forms representing the quantity three, not a vague notion of several" {laidig-1990}
- **Geographic**: Moluccas, Indonesia
- **Not in our dataset currently**

**Tolai/Kuanua** {ksd}
- **Status**: Full trial system
- **System**: Singular - Dual - Trial - Plural
- **Scope**: Pronouns (all persons)
- **Features**: Also marks inclusive/exclusive distinction
- **Geographic**: Papua New Guinea (East New Britain)
- **Check dataset**: Need to verify if in our 176 Austronesian languages

**Raga** {lml}
- **Status**: Trial pronouns
- **Geographic**: Vanuatu
- **Not confirmed in our dataset**

**Wamesa** {wad}
- **Status**: Remnant trial forms (very rare)
- **Note**: "Trial forms are remnants from old Austronesian influence, very rare, conjugate as plural with verbs"
- **Geographic**: Papua New Guinea
- **Not confirmed in our dataset**

#### Creole Languages (Melanesian Pidgin)

**Tok Pisin** {tpi} ✓ IN DATASET (2 translations, 78 books total)
- **Status**: Productive trial in pronouns
- **System**: Singular - Dual - Trial - Plural
- **Forms**:
  - 1st person exclusive: mitripela "the three of us (not you)"
  - 1st person inclusive: yumitripela "the three of us (including you)"
  - 2nd person: yutripela "you three"
  - 3rd person: ol tripela "the three of them"
- **Features**: Inclusive/exclusive distinction in 1st person
- **Citation**: {britannica-tokpisin}, {verhaar-1995}

**Bislama** {bis}
- **Status**: Trial pronouns (similar to Tok Pisin)
- **Geographic**: Vanuatu
- **Not in our dataset currently**

**Pijin** {pis}
- **Status**: Trial pronouns (Melanesian Pidgin)
- **Geographic**: Solomon Islands
- **Not in our dataset currently**

### Typological Status
According to Michael Cysouw {cysouw-2005}, most languages reported to have trials have mislabeled paucals. **True trials** (referring specifically to 3, not "a few") are extremely rare.

**Greenberg's Universal 34**: "No language has a trial number unless it has a dual."

### In Our Dataset
**Confirmed trial languages**:
- Tok Pisin (tpi) - ✓ verified, 2 translations

**Highly probable** (Austronesian languages in PNG/Solomon Islands/Vanuatu):
- Need to check our 176 Austronesian languages for Oceanic subgroup members

---

## 4. QUADRIAL (Q)

### Definition
A grammatical number referring to exactly four entities.

### Typological Controversy

**Greville Corbett's Analysis** {corbett-2000}:
> "By sometime in 2000, Greville Corbett found that no report of a 'quadral grammatical number' had been borne out."

Most proposed "quadrials" have been **reanalyzed as paucals** or "greater paucals."

### Previously Claimed Quadrial Languages (Now Disputed)

**Sursurunga** {sgz} ✓ IN DATASET
- **Previous claim**: Quadral
- **Reanalysis**: Greater paucal
- **Actual system**: Singular - Dual - Paucal (lesser paucal, ~3-4) - Greater Paucal (4+) - Plural
- **Example**:
  - singular: iau "I"
  - dual: giur "the two of us"
  - paucal: gimtul "the few of us" (~3-4)
  - greater paucal: gimhat "we" (4+)
  - plural: gim "we (many)"
- **Geographic**: Papua New Guinea (New Ireland Province)
- **Citation**: {hutchisson-1986}, {corbett-2000}

**Marshallese** {mah}
- **Previous claim**: Quadral pronouns
- **Reanalysis**: Better classified as paucal
- **Reason**: Can mean "exactly four" OR used rhetorically for larger groups with "individual intimacy"
- **Not in our dataset currently**
- **Citation**: {corbett-2000}

**Tok Pisin, Bislama, Pijin**
- **Previous claim**: Quadral possible (e.g., yupela fopela)
- **Status**: Grammatically possible but almost never used
- **Reality**: Speakers use plural instead
- **Citation**: {verhaar-1995}

**Sign Languages**
- **Estonian Sign Language**: Claimed to have quadral even for nouns
- **Status**: Exceptional if true
- **Not relevant to our dataset**

**Apinayé** {apn}
- **Claim**: Third person pronominal prefix meaning "they four"
- **Geographic**: Brazil (Macro-Gê family)
- **Status**: Needs verification
- **Not in our dataset currently**

### TBTA Usage of Quadrial

Despite scholarly consensus that true quadrials don't exist or are extremely rare, TBTA includes the category. This suggests:

1. **Semantic interpretation**: TBTA may mark semantic reference to "exactly four" even when not grammatically marked
2. **Target language provision**: Providing guidance for rare languages that might distinguish "four"
3. **Trinity + 1 contexts**: Biblical contexts referring to four specific entities

### In Our Dataset
**Claimed quadrial**: None confirmed

**Languages to investigate**:
- Sursurunga (sgz) - has greater paucal, might be what TBTA calls "quadrial"

---

## 5. PAUCAL (p)

### Definition
A grammatical number referring to a small, indefinite quantity - typically "a few" as opposed to "many." The exact range varies by language and noun class.

### Distinguishing Paucal from Trial
- **Trial**: Exactly three (precise)
- **Paucal**: A few, small group (imprecise, typically 3-10 but varies)

When dual and paucal coexist, paucal typically begins at 3.

### Language Families with Paucal

#### Austronesian (Complex Systems)

**Sursurunga** {sgz} ✓ IN DATASET
- **System**: Five-way distinction
  - Singular
  - Dual
  - **Lesser paucal** (labeled "trial" but means "a few", typically 3-4)
  - **Greater paucal** (mislabeled "quadral", means "several", minimum 4)
  - Plural (many)
- **Equivalents**: Lesser paucal = "a few", Greater paucal = "several"
- **Citation**: {hutchisson-1986}, {corbett-2000}

**Lihir** {lir}
- **System**: Five-way (similar to Sursurunga)
- **Geographic**: Papua New Guinea (New Ireland Province)
- **Not confirmed in our dataset**

#### Australian Aboriginal Languages

Our dataset contains **36 Australian Aboriginal languages**.

**Warlpiri** {wbp} ✓ IN DATASET (11,098 verses, 36 books)
- **Status**: Paucal number attested
- **Range**: Varies by noun class
- **Citation**: {hale-1983}

**Warndarrang**
- **Paucal range**: Up to about 5
- **Extinct language**
- **Citation**: {corbett-2000}

**Murrinh-Patha** {mwf} ✓ IN DATASET (4,374 verses, 12 books)
- **Paucal range**: About 10-15
- **Geographic**: Northern Territory, Australia
- **Citation**: {corbett-2000}

**General pattern**: Almost all Australian Aboriginal languages with paucal also have dual.

#### Afro-Asiatic

**Arabic** (Modern Standard, Classical) {ara, arb}
- **System**: Singular - Dual - Paucal - Plural
- **Paucal mechanism**: Specific broken plural templates
- **Paucal range**: 3-10
- **Usage**: Certain nouns have distinct "paucal plural" forms for small quantities
- **Example**: Specific morphological patterns (not just any plural with 3-10)
- **Note**: The dual (exactly 2) is separate; plural begins at 3
- **Citation**: {ryding-2005}, {holes-2004}

**Dialectal Arabic**
- Some dialects use dual morpheme -e:n for paucal meanings
- **Citation**: {al-harahsheh-2023}

#### Indo-European

**Kurmanji/Northern Kurdish** {kmr}
- **Status**: One of few Indo-European languages with paucal
- **Not confirmed in our dataset** (need to check Kurdish translations)

**Slavic remnants**
- **Russian**: Singular, Paucal (2-4), Plural (5+)
  - This is often analyzed as genitive singular (2-4) vs. genitive plural (5+)
  - один пёс (1 dog-NOM.SG)
  - два/три/четыре пса (2/3/4 dogs-GEN.SG - paucal interpretation)
  - пять псов (5 dogs-GEN.PL)
- **Polish**: Similar pattern
- **Not true paucal**: These are often reanalyzed as genitive case rather than paucal number
- **Citation**: {corbett-2000}

### In Our Dataset

**Confirmed paucal languages**:
- Sursurunga (sgz) - lesser + greater paucal
- Warlpiri (wbp) - paucal
- Murrinh-Patha (mwf) - paucal (range ~10-15)

**Potential paucal languages** (need investigation):
- Other Australian Aboriginal languages (36 total)
- Other Austronesian Oceanic languages (176 total)
- Arabic translations (if any in dataset)

---

## 6. PLURAL (P)

### Definition
Refers to multiple entities - either definitively more than the highest precise number category in a language, or an indefinite large quantity.

### Cross-linguistic Variation

**In languages with only singular/plural**:
- Plural = 2 or more

**In languages with dual**:
- Plural = 3 or more (dual covers 2)

**In languages with dual + trial**:
- Plural = 4 or more (trial covers 3)

**In languages with paucal**:
- Plural = "many" as opposed to paucal "few"
- Boundary varies by language and noun type

### Marking Strategies (WALS Feature 33A)

From our research of 1009 languages:

**Most common** (513 languages globally):
- Plural suffix (e.g., English -s, Hebrew -ים)

**Other strategies**:
- Plural prefix (126 languages)
- Plural word/particle (170 languages)
- Plural clitic (81 languages)
- Mixed morphological plural (60 languages)
- **No plural marking** (98 languages) - common in East/Southeast Asia, New Guinea
- Plural reduplication (8 languages)
- Plural stem change (6 languages)
- Plural tone (4 languages)

### Biblical Source Languages

**Biblical Hebrew**:
- Masculine plural: -ים (-im)
- Feminine plural: -ות (-ot)
- Dual vs. plural distinction maintained

**Koine Greek**:
- Full plural declension system
- No productive dual (only remnants)

### In Our Dataset
All 1009 languages have some mechanism to express plurality, though strategies vary widely.

---

## Cross-Linguistic Typology Summary

### Number Hierarchy (Corbett 2000)

Corbett proposes a hierarchy rather than simple linear progression:

```
Singular ← most basic
   ↓
Plural ← most common
   ↓
Dual ← less common
   ↓
Trial ← rare
   ↓
Paucal ← alternative to trial/quadrial
```

**Implicational universals**:
- If a language has trial, it has dual (Greenberg Universal 34)
- If a language has dual, it has singular and plural
- Paucal typically coexists with dual

### Geographic Distribution

**Dual number**:
- Scattered: Slavic (Slovene, Sorbian), remnants in other Indo-European
- Some Austronesian
- Some Australian Aboriginal

**Trial number**:
- **Concentrated**: Oceanic Austronesian (Papua New Guinea, Solomon Islands, Vanuatu)
- **Creoles**: Melanesian Pidgins (Tok Pisin, Bislama, Pijin)
- **Rare elsewhere**

**Paucal number**:
- **Australian Aboriginal languages** (common)
- **Austronesian Oceanic** (especially complex systems like Sursurunga)
- **Arabic** (broken plural patterns)
- **Scattered**: Some Native American languages

**Quadrial**:
- **Consensus**: Doesn't exist as true grammatical category
- **Reanalysis**: Claimed quadrials are better analyzed as greater paucals

---

## Determining Number for Target Languages

### Step 1: Identify Language Family

Use language family as initial predictor:

**High probability of dual**:
- Slavic (check: Slovene, Sorbian, Kashubian)
- Some Austronesian

**High probability of trial**:
- Oceanic Austronesian (Papua New Guinea, Solomon Islands, Vanuatu, Indonesia)
- Melanesian Pidgins

**High probability of paucal**:
- Australian Aboriginal
- Austronesian Oceanic
- Arabic

### Step 2: Consult Reference Grammars

**Resources**:
1. **Glottolog** (glottolog.org): Links to grammars and descriptive materials
2. **WALS** (wals.info): Typological features, including nominal plurality
3. **Ethnologue** (ethnologue.com): Basic information, speaker numbers
4. **Grammar libraries**: University digital repositories

**What to look for in grammars**:
- Pronoun paradigms (number distinctions often clearest here)
- Noun morphology sections
- Number agreement patterns
- Example sentences with quantities

### Step 3: Examine Pronoun Systems

Number distinctions are typically most visible in **pronouns**:

**Questions to ask**:
1. How many distinct forms for "we"?
   - 1 form → probably singular/plural only
   - 2 forms → check for dual or inclusive/exclusive
   - 3+ forms → likely dual/trial or paucal distinctions

2. Is there inclusive/exclusive distinction?
   - Common in languages with dual/trial
   - Helps identify complex number systems

3. Do nouns also mark number, or only pronouns?
   - Pronoun-only systems are common
   - Noun number marking indicates more pervasive system

### Step 4: Test Elicitation Questions

When working with native speakers or analyzing texts:

**For dual**:
- How do you say "two eyes" vs. "three eyes" vs. "many eyes"?
- Is the form for "two" different from "three or more"?

**For trial**:
- How do you say "we three people" vs. "we four people"?
- Is there a special form only used for exactly three?

**For paucal**:
- How do you say "a few dogs" vs. "many dogs"?
- What's the boundary? (test with 3, 4, 5, 10, 20)

**Obligatoriness test** {cable-2010}:
- If a form **must** be used when referring to a specific number, it's grammaticalized
- If it's optional or can be replaced by numeral, it may not be true grammatical number

### Step 5: Check Our Dataset

Our 1009 languages by family:
- **176 Austronesian** → check for Oceanic subgroup (trial likely)
- **141 Trans-New Guinea** → variable, check individually
- **135 Indo-European** → check for Slavic (dual possible)
- **89 Niger-Congo** → typically singular/plural
- **36 Australian** → paucal highly likely
- **25 Afro-Asiatic** → check for Arabic (paucal)
- **15 Creole** → check for Melanesian Pidgins (trial)

---

## Mapping from Biblical Source Languages

### Biblical Hebrew → Target Language

**Hebrew has**: Singular, Dual (limited), Plural

**Mapping rules**:

| Hebrew | English | Target (Dual) | Target (Trial) | Target (Paucal) |
|--------|---------|---------------|----------------|-----------------|
| Singular | Singular | Singular | Singular | Singular |
| Dual | Plural (two) | **Dual** | Plural | Paucal or Plural |
| Plural (3-10) | Plural | Plural | **Trial** (if 3) | **Paucal** |
| Plural (11+) | Plural | Plural | Plural | **Plural** |

**Challenge**: Hebrew dual is mostly lexicalized (body parts, time), not productive for all "exactly two" contexts.

### Koine Greek → Target Language

**Greek has**: Singular, Plural (dual essentially absent)

**Mapping rules**:

| Greek | Context | Target (Dual) | Target (Trial) | Target (Paucal) |
|-------|---------|---------------|----------------|-----------------|
| Singular | One | Singular | Singular | Singular |
| Plural | Two (from context) | **Dual** | Plural | Paucal |
| Plural | Three (from context) | Plural | **Trial** | Paucal |
| Plural | Few (from context) | Plural | Plural | **Paucal** |
| Plural | Many | Plural | Plural | Plural |

**Challenge**: Greek plural is underspecified for exact number. Must rely on:
1. **Context**: Discourse participants mentioned
2. **Numerals**: Explicit numbers in the text
3. **Semantic knowledge**: Cultural/theological interpretation

**Example - Genesis 1:26** (LXX):
- Greek: ποιήσωμεν "let us make" (1st person plural)
- **Theological interpretation**: Trinity (three persons)
- Hebrew: נַעֲשֶׂה "let us make" (1st person plural)
- **TBTA encoding**: Trial + First Person Inclusive
- **Justification**: Trinitarian theology → exactly three divine persons

---

## Methodology for Reproducing TBTA Number Decisions

### Phase 1: Identify All Participants

For each verse:
1. Extract all noun phrases and pronouns
2. Identify referents (who/what is being discussed)
3. Track participant indices (TBTA uses 1-9, A-Z, a-z for same-entity tracking)

### Phase 2: Determine Semantic Number

**From source text morphology**:
- Hebrew: Check for dual suffix (-ayim/-ê)
- Hebrew: Singular vs. plural morphology
- Greek: Singular vs. plural (no dual)

**From context**:
- Explicit numerals (two angels, three men, etc.)
- Discourse tracking (how many participants in the scene?)
- Prior mentions (established as pair, trio, group?)

**From theology/culture** (use cautiously):
- Trinity passages → trial?
- Angels appearing in pairs → dual?
- Requires scholarly commentary consultation

### Phase 3: Apply Target Language Constraints

For languages with number distinctions beyond singular/plural:

**If target has dual**:
- Any "exactly two" entities → dual
- Any plural → stay plural

**If target has trial**:
- Any "exactly three" entities → trial
- Especially: Trinity references, three angels, three visitors

**If target has paucal**:
- Small groups (3-10 typically) → paucal
- Large crowds, nations, armies → plural
- **Boundary varies by language** - consult grammar

**If target has quadrial** (disputed):
- Extremely rare, likely don't use unless target language clearly attests it
- Sursurunga "greater paucal" might be closest real equivalent

### Phase 4: Validation

**Check consistency**:
- Same referent across verse should have same number
- Participant tracking should align with number
- Discourse flow should make sense

**Check against reference translations**:
- Consult existing translations in target language
- If available, check how translators handled number

**Check theological implications**:
- Does the number choice affect meaning?
- Trinity passages especially sensitive

---

## Sources Consulted

### Academic Books
- {corbett-2000}: Corbett, Greville G. 2000. *Number*. Cambridge Textbooks in Linguistics. Cambridge: Cambridge University Press.
- {ryding-2005}: Ryding, Karin C. 2005. *A Reference Grammar of Modern Standard Arabic*. Cambridge: Cambridge University Press.
- {holes-2004}: Holes, Clive. 2004. *Modern Arabic: Structures, Functions, and Varieties*. Georgetown University Press.

### Biblical Languages
- {gesenius-1910}: Gesenius, Wilhelm. 1910. *Gesenius' Hebrew Grammar*. Edited by E. Kautzsch. Oxford: Clarendon Press.
- {unfoldingword-uhg}: *unfoldingWord® Hebrew Grammar*. https://uhg.readthedocs.io/
- {moulton-1908}: Moulton, James Hope. 1908. *A Grammar of New Testament Greek*. Edinburgh: T&T Clark.
- {blass-1961}: Blass, F. and A. Debrunner. 1961. *A Greek Grammar of the New Testament and Other Early Christian Literature*. Chicago: University of Chicago Press.

### Language-Specific
- {jakop-2016}: Jakop, Tjaša. 2016. "Use of dual in standard Slovene, colloquial Slovene and Slovene dialects."
- {laidig-1990}: Laidig, Wyn D. 1990. "Insights from Larike Possessive Constructions." *Oceanic Linguistics* 29(2).
- {hutchisson-1986}: Hutchisson, Don. 1986. "Sursurunga Pronouns and the Special Uses of Quadral Number." In *VICAL 1: Oceanic Languages, Papers from the Fifth International Conference on Austronesian Linguistics*.
- {verhaar-1995}: Verhaar, John W.M. (ed). 1995. *Melanesian Pidgin and Tok Pisin*. Amsterdam: John Benjamins.
- {hale-1983}: Hale, Ken. 1983. "Warlpiri and the grammar of non-configurational languages." *Natural Language & Linguistic Theory* 1(1).

### Typological Resources
- {cable-2010}: Cable, Seth. 2010. "Number: Beyond the Plural." UMass Ling 720 Proseminar.
- {cysouw-2005}: Cysouw, Michael. 2005. "Syncretisms involving clusivity." In *Clusivity: Typology and case studies of inclusive-exclusive distinction*.
- {al-harahsheh-2023}: Al-Harahsheh, Ahmad M. 2023. "When a Dual Marker Acts as a Paucal Marker: The Case of the Dual -e:n in Northern Rural Jordanian Arabic." *Languages* 8(3).

### Online Databases
- WALS Online: https://wals.info/ (World Atlas of Language Structures)
- Glottolog: https://glottolog.org/
- Ethnologue: https://ethnologue.com/

### Bible Translation Resources
- TIPs (Translation Insights and Perspectives): https://tips.translation.bible/
  - Multiple articles on inclusive/exclusive pronouns in Bible translation

---

## Appendix A: Languages in Our Dataset by Number System

### Confirmed Dual
1. Slovene (slv) - Indo-European, productive dual
2. Lithuanian (lit) - Indo-European, remnant dual

### Confirmed Trial
1. Tok Pisin (tpi) - Creole, 2 translations, productive trial in pronouns

### Confirmed Paucal
1. Sursurunga (sgz) - Austronesian, lesser + greater paucal
2. Warlpiri (wbp) - Australian, paucal
3. Murrinh-Patha (mwf) - Australian, paucal (range ~10-15)

### High Probability for Further Investigation

**Austronesian (176 total)** - check for Oceanic subgroup:
- Papua New Guinea (PNG) Austronesian languages → likely trial
- Solomon Islands Austronesian → likely trial
- Vanuatu Austronesian → likely trial
- Indonesia Austronesian (eastern regions) → possible trial
- Philippines Austronesian → less likely (western Austronesian)

**Australian Aboriginal (36 total)** - most likely have paucal:
- Arrernte, Eastern (aer)
- Alyawarr (aly)
- Anindilyakwa (aoi)
- [See full list in languages.tsv]

**Indo-European (135 total)** - check for Slavic with dual remnants:
- Need to identify which Slavic languages
- Check for other Baltic languages besides Lithuanian

---

## Appendix B: Quick Reference for Annotators

When annotating biblical text for target language number:

**Ask these questions**:
1. **How many entities are being referenced?**
   - Count from context, numerals, discourse tracking

2. **Does the target language have dual?**
   - If yes, and entities = 2 → use Dual (D)
   - Check: Slovene, Lithuanian, some Austronesian

3. **Does the target language have trial?**
   - If yes, and entities = 3 → use Trial (T)
   - Check: Tok Pisin, Oceanic Austronesian languages

4. **Does the target language have paucal?**
   - If yes, and entities = small group (3-10 typically) → use Paucal (p)
   - Check: Australian Aboriginal, Sursurunga, Arabic

5. **Is it exactly 4?**
   - Be cautious: true Quadrial (Q) is disputed
   - Consider using Paucal instead
   - Only use if target language clearly attests it

6. **Otherwise**:
   - Singular (S) for one
   - Plural (P) for many or default

**Priority**: Target language grammar determines the number marking, not source language morphology alone.
