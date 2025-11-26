# Language Family & Typology Analysis: Number System

**Feature**: Grammatical Number
**Dataset**: 1,008 languages across 30+ families
**Source**: `/src/constants/languages.tsv`
**Last Updated**: 2025-11-26

## Executive Summary

Analysis of 1,008 Bible translation languages reveals **Austronesian** (176 languages) as the most complex number system family, with documented dual, trial, and paucal categories. Hebrew and Arabic explicitly encode dual morphologically, while Koine Greek lost the dual by the Hellenistic period. Most Indo-European languages (135 in dataset) use simple singular/plural distinction. Classifier languages (Indonesian, Chinese) often have optional or no number marking. **Theological impact**: ~20-30 Austronesian/Oceanic languages can explicitly mark trial (exactly 3) for Trinity contexts; all other languages must use less precise plural or rely on context.

**Key Findings**:
- **Source Languages**: Hebrew has productive dual, Greek has singular/plural only
- **Most Complex**: Austronesian family (trial, dual, paucal in some languages)
- **Simplest**: Isolating languages (Chinese, Vietnamese) with optional/no marking
- **Root Languages**: English, Spanish, French, German have simple S/P; Arabic has dual/paucal; Hawaiian/Tongan have dual (pronouns)
- **Trinity-capable**: ~20-30 languages with trial can explicitly encode "exactly 3 persons"

## 1. Source Language Encoding

### 1.1 Hebrew: Morphologically Marked Dual

**System**: Singular / Dual / Plural

**Evidence** {hebrew-dual}:
- **Morphology**: Dual suffix -ַיִם (-ayim) for pairs
- **Distribution**: Mandatory for natural pairs (body parts, time expressions)
- **Frozen duals**: שָׁמַיִם (shamayim "heavens"), מַיִם (mayim "waters") - morphologically dual, semantically singular

**From Biblical Hebrew Grammar** (https://biblicalhebrew.org/dual-form-and-its-limited-use-in-hebrew.aspx):
> "The dual form in Biblical Hebrew is a morphologically distinct number category, marked by the suffix -ַיִם in absolute state and -ֵי in construct, used primarily for natural pairs like body parts (e.g., עֵינַיִם 'two eyes') and time expressions (e.g., יוֹמַיִם 'two days')."

**Examples**:
- יָדַיִם (yadayim) "two hands" - natural pair
- שְׁנָתַיִם (shenatayim) "two years" - time expression
- מִצְרַיִם (mitsrayim) "Egypt" - frozen dual (place name)

**Verb Agreement**: No dual verb forms exist; dual nouns take plural verb agreement {hebrew-dual}.

**Theological Significance**: Hebrew dual morphology creates translation challenges in Genesis 1:26 ("Let us..."), where target languages with trial can be more theologically precise than Hebrew itself.

### 1.2 Koine Greek: Dual Lost, Singular/Plural Only

**System**: Singular / Plural

**Evidence** {koine-dual}:
> "In the Classical period, the dual was viable only in Attic. In the Koine and in New Testament Greek, the dual has virtually disappeared."

**From Moulton on Greek Dual** (https://koine-greek.com/2008/12/15/moulton-on-the-greek-dual/):
> "The dual number, which denoted pairs in Classical Greek, was entirely lost in Koine, with plural forms substituting for it across nouns, adjectives, and verbs."

**Implications for Translation**:
- Greek cannot distinguish dual (2) vs. trial (3) vs. paucal (few) vs. plural (many)
- Translators must infer from context (e.g., "two disciples" Luke 24:13)
- Target languages with finer number distinctions require contextual analysis

**Example**:
```
Luke 24:13: δύο ἐξ αὐτῶν (duo ex autōn)
Greek: "two" (numeral) + "of them" (plural pronoun)
Target with dual: Mark pronoun as DUAL (inferred from numeral)
Target without dual: Mark as PLURAL (follow Greek morphology)
```

## 2. Language Family Distribution

### Dataset Overview

**Total Languages**: 1,008 (from `/src/constants/languages.tsv`)
**Unique Families**: 30+

**Top 10 Families by Count**:

| Rank | Family | Count | % of Dataset | Number System Complexity |
|------|--------|-------|--------------|--------------------------|
| 1 | Austronesian | 176 | 17.5% | **HIGH** (dual, trial, paucal in some) |
| 2 | Trans-New Guinea | 141 | 14.0% | **MEDIUM** (varies by language) |
| 3 | Indo-European | 135 | 13.4% | **LOW** (mostly singular/plural, except Slovenian dual) |
| 4 | Niger-Congo | 89 | 8.8% | **LOW** (mostly singular/plural) |
| 5 | Otomanguean | 69 | 6.9% | **LOW** (singular/plural) |
| 6 | Mayan | 41 | 4.1% | **LOW** (singular/plural) |
| 7 | Australian | 36 | 3.6% | **MEDIUM** (some have dual/trial) |
| 8 | Afro-Asiatic | 25 | 2.5% | **MEDIUM** (Arabic has dual/paucal) |
| 9 | Uto-Aztecan | 21 | 2.1% | **LOW** (singular/plural) |
| 10 | Maipurean | 20 | 2.0% | **LOW** (singular/plural) |

**Other Notable**:
- Sino-Tibetan: 18 (Chinese - optional number)
- Creole: 15 (varies by substrate)
- Language isolate: 10 (varies)

## 3. Typological Classification by Number System

### 3.1 Mandatory Number Marking

**Definition**: Language **must** mark number on nouns/pronouns grammatically.

**Languages in Dataset** (selected examples):

| ISO-639-3 | Language | Family | System | Mandatory/Optional | Notes |
|-----------|----------|--------|--------|-------------------|-------|
| arb | Arabic (Standard) | Afro-Asiatic | S/D/P/Paucal | Mandatory | Dual for pairs, paucal for 3-10 {wals-34} |
| haw | Hawaiian | Austronesian (Polynesian) | S/D/P | Mandatory | Dual confirmed in pronouns {hawaiian-dual-wiki} |
| ton | Tongan | Austronesian (Polynesian) | S/D/P | Mandatory | Dual confirmed in pronouns {tongan-dual-wiki} |
| deu | German | Indo-European (Germanic) | S/P | Mandatory | Mandatory singular/plural |
| eng | English | Indo-European (Germanic) | S/P | Mandatory | Mandatory singular/plural |
| spa | Spanish | Indo-European (Romance) | S/P | Mandatory | Mandatory singular/plural |
| rus | Russian | Indo-European (Slavic) | S/P | Mandatory | Lost dual (except Slovenian) |

**Note**: Slovenian (slv) has productive dual **but is NOT in our dataset** {slovenian-dual-gap}.

### 3.2 Optional Number Marking

**Definition**: Number marking is optional or restricted by animacy hierarchy.

**Languages in Dataset** (selected examples):

| ISO-639-3 | Language | Family | System | Mandatory/Optional | Notes |
|-----------|----------|--------|--------|-------------------|-------|
| ind | Indonesian | Austronesian (Malayo-Polynesian) | General Number | Optional | Plural via reduplication (optional) {indonesian-number} |
| zlm | Malay | Austronesian (Malayo-Polynesian) | General Number | Optional | Classifiers optional {malay-classifiers} |
| cmn | Mandarin Chinese | Sino-Tibetan | General Number | Optional | No plural morphology, classifiers required |
| jpn | Japanese | Japonic | General Number | Optional | Optional plural suffix -たち (-tachi) for animates |
| vie | Vietnamese | Austroasiatic | General Number | Optional | Classifiers, no plural morphology |

**From Indonesian Number Research** (https://www.researchgate.net/publication/239568420_Plural_Semantics_Reduplication_and_Numeral_Modification_in_Indonesian):
> "In Indonesian, plural marking as both reduplication and classifiers in numeral modification constructions are optional, and bare (non-reduplicated) Indonesian nouns are best analyzed as exhibiting 'general number.'"

### 3.3 Complex Number Systems (Dual, Trial, Paucal)

#### Languages with Dual

**Documented in Literature**:
- **Slavic**: Slovenian (NOT in dataset), Sorbian
- **Semitic**: Hebrew, Classical Arabic, Maltese
- **Polynesian**: Hawaiian, Samoan, Tongan, Maori
- **Other Austronesian**: Many Philippine languages

**In Our Dataset**:
- arb (Arabic, Standard) - **confirmed dual**
- haw (Hawaiian) - **confirmed dual** (pronouns only) {hawaiian-dual-wiki}
- ton (Tongan) - **confirmed dual** (pronouns only) {tongan-dual-wiki}

#### Languages with Trial

**Documented in Scholarly Sources** {sursurunga-trial, corbett-2000}:

**Confirmed Trial Languages** (~20-30 total):
- **Austronesian/Oceanic**: Larike, Tok Pisin, Marshallese, Lihir, Tolomako, Manam, Sursurunga, Mussau
- **Suspected but not confirmed**: Fijian, some other Oceanic languages

**From Sursurunga Research** (https://en.wikipedia.org/wiki/Sursurunga_language):
> "Sursurunga is famous for having a five-way grammatical number distinction... The Larike trial is a genuine trial: 'it should be stated explicitly that Larike trials are true trial forms. In other words, they represent the quantity three, and are not used to refer to the more vague notion of several, as is a paucal or limited plural.'"

**Critical Note**: TBTA Edge Cases claim "172+ Austronesian and Polynesian languages" have trial {tbta-edge-cases}, but scholarly consensus is ~20-30 {corbett-2000}. **Discrepancy requires Stage 2 verification**.

**In Our Dataset**:
- **NONE confirmed** - No Larike, Marshallese, Sursurunga, or other documented trial languages in current dataset
- **Gap**: Lack of trial languages limits theological precision for Trinity contexts

#### Languages with Paucal

**Documented Examples** {wals-34}:
- Arabic (paucal for 3-10)
- Warndarrang (paucal up to ~5)
- Baiso (paucal 2-6, without dual)
- Murrinh-patha (paucal ~10-15)
- Sursurunga (lesser/greater paucal, not true trial)

**In Our Dataset**:
- arb (Arabic, Standard) - **confirmed paucal** (3-10 range)

## 4. Root Languages Analysis

### Definition of Root Languages

**Root languages** are major translation source languages that translators often consult when translating from Hebrew/Greek into minority languages. These include historical biblical languages and modern lingua francas.

### Root Language Number Systems

| Language | ISO-639-3 | Family | In Dataset? | Number System | Theological Impact |
|----------|-----------|--------|-------------|---------------|-------------------|
| **Hebrew** | heb | Afro-Asiatic | ✅ (source) | S/D/P | Dual for pairs, but not trial for Trinity |
| **Greek** | grc | Indo-European | ✅ (source) | S/P | No dual (lost in Koine), cannot distinguish 2 vs. 3 |
| **Latin** | lat | Indo-European | ❌ | S/P | Simple system |
| **English** | eng | Indo-European | ✅ (33 versions) | S/P | Simple system, "us" ambiguous for Trinity |
| **Spanish** | spa | Indo-European | ✅ (multiple) | S/P | Simple system |
| **French** | fra | Indo-European | ✅ (suspected) | S/P | Simple system |
| **German** | deu | Indo-European | ✅ (4 versions) | S/P | Simple system |
| **Arabic** | arb | Afro-Asiatic | ✅ (2 versions) | S/D/P/Paucal | Complex system, dual for pairs |
| **Indonesian** | ind | Austronesian | ✅ (2 versions) | General Number | Optional marking, isolating tendencies |
| **Swahili** | swh | Niger-Congo | ✅ (suspected) | Noun Classes | Number via noun class prefixes |
| **Portuguese** | por | Indo-European | ✅ (suspected) | S/P | Simple system |
| **Russian** | rus | Indo-European | ✅ (suspected) | S/P | Lost dual (unlike Slovenian) |
| **Mandarin** | cmn | Sino-Tibetan | ✅ (3 versions) | General Number | Classifier language, no plural morphology |

**Key Observations**:
1. **Most root languages** (English, Spanish, French, German, Portuguese, Russian) have simple S/P systems
2. **Arabic** is the most complex root language (dual + paucal)
3. **Hebrew** has dual but not trial (cannot explicitly encode Trinity as "exactly 3")
4. **Isolating languages** (Indonesian, Chinese) have optional/no number marking
5. **No trial in any root language** - Trinity contexts require plural or context

## 5. Typological Distinctions

### 5.1 Animacy Hierarchy Effects

**Principle** {animacy-hierarchy}: Number marking may be **obligatory** for animates (especially humans) but **optional** for inanimates.

**From Animacy Hierarchy Research** (https://hal.science/hal-01874511v1/document):
> "In Kannada, a Dravidian language, number marking is obligatory at the top of the extended Animacy Hierarchy, down to nouns that denote humans, but optional for all those denoting non-humans."

**Examples**:
- **Kannada**: Obligatory for humans, optional for animals/objects
- **Muna**: Verb agreement obligatory for human plurals, optional for animates, impossible for inanimates
- **Guaraní, Tiwi, Slave**: Restrict number marking above certain animacy cut-off

**Hierarchy**: Human > Animate > Inanimate

**Impact on Bible Translation**:
- God, Jesus, disciples → Likely **mandatory** number marking (high animacy)
- Animals, objects → May be **optional** (low animacy)
- Abstract concepts (sin, grace) → May **lack** number marking

### 5.2 Greenberg's Universal 34

**From Grammatical Number Wikipedia** (https://en.wikipedia.org/wiki/Grammatical_number):
> "Joseph Greenberg has proposed a number category hierarchy as a linguistic universal: 'No language has a trial number unless it has a dual. No language has a dual unless it has a plural.'"

**Implicational Hierarchy**:
```
Singular < Plural < Dual < Trial < Quadrial (not attested)
```

**Interpretation**:
- If a language has **Trial**, it must also have **Dual** and **Plural**
- If a language has **Dual**, it must also have **Plural**
- All languages have **Singular** and **Plural**

**Verification**: Larike, Marshallese, Tok Pisin (trial languages) all have dual + plural ✅

**Exception**: Baiso (Cushitic) has paucal (2-6) without dual {corbett-2000} - violates Universal 34, disputed.

### 5.3 Pronoun vs. Noun Number

**Key Finding**: Many languages mark number on **pronouns** but not **nouns**.

**From Trial Number Research** (https://en-academic.com/dic.nsf/enwiki/26937):
> "Several Austronesian or Austronesian-based languages such as Tolomako, Lihir, Manam, Bislama, and some registers of Tok Pisin have trial number in their pronouns; **no language is known with trial number in its nouns**."

**Implication**:
- Genesis 1:26 "Let **us** make" (pronoun) → Can be marked Trial in trial languages
- "God" (noun) → May only support Singular/Plural, not Trial

**TBTA Challenge**: Does TBTA mark pronouns and nouns differently for trial?
- **Suspected**: Pronouns can be Trial, nouns cannot
- **Status**: Undocumented in TBTA sources

## 6. Proposed Test Languages for Stage 2 Analysis

### Selection Criteria

1. **Diversity**: Mix of families, number systems
2. **Root language representation**: Major translation sources
3. **Complexity range**: Simple (S/P) to complex (S/D/T/P/Paucal)
4. **Theological significance**: Include languages with dual/trial for Trinity contexts
5. **Dataset availability**: Languages present in `/src/constants/languages.tsv`

### Proposed 10 Test Languages

| # | ISO-639-3 | Language | Family | System | Mandatory/Optional | Rationale |
|---|-----------|----------|--------|--------|-------------------|-----------|
| 1 | **eng** | English | Indo-European | S/P | Mandatory | Root language, simple system, baseline |
| 2 | **spa** | Spanish | Indo-European | S/P | Mandatory | Root language (Romance), mandatory marking |
| 3 | **arb** | Arabic (Standard) | Afro-Asiatic | S/D/P/Paucal | Mandatory | Complex system, dual + paucal, root language |
| 4 | **ind** | Indonesian | Austronesian | General Number | Optional | Optional marking, isolating tendencies |
| 5 | **haw** | Hawaiian | Austronesian (Polynesian) | S/D/P | Mandatory | Dual confirmed (pronouns), Polynesian representative |
| 6 | **cmn** | Mandarin Chinese | Sino-Tibetan | General Number | Optional | Classifier language, no plural morphology |
| 7 | **deu** | German | Indo-European (Germanic) | S/P | Mandatory | Root language, mandatory marking |
| 8 | **swh** | Swahili | Niger-Congo | Noun Classes | Mandatory | Bantu noun class system |
| 9 | **rus** | Russian | Indo-European (Slavic) | S/P | Mandatory | Slavic without dual (contrast with Slovenian) |
| 10 | **ton** | Tongan | Austronesian (Polynesian) | S/D/P | Mandatory | Dual confirmed (pronouns), compare with Hawaiian |

**Backup Candidates** (if above not available):
- **zlm** (Malay) - Austronesian, optional marking, classifier language
- **fra** (French) - Romance, root language
- **por** (Portuguese) - Romance, root language
- **acr** (Achi) - Mayan, representative of Mesoamerican family
- Any Austronesian with documented trial (if available)

### Why These Languages?

**Coverage of Systems**:
- **Simple S/P**: English, Spanish, German, Russian
- **Dual**: Arabic, Hawaiian (confirmed - pronouns), Tongan (confirmed - pronouns)
- **Paucal**: Arabic
- **Trial**: None in dataset (gap identified)
- **Optional/General Number**: Indonesian, Mandarin Chinese
- **Noun Classes**: Swahili

**Theological Significance**:
- **Arabic**: Can explicitly mark dual for "two disciples," paucal for "a few people"
- **Hawaiian/Tongan**: Can distinguish pairs from groups using dual pronouns
- **None with trial**: Cannot explicitly mark Trinity as "exactly 3" (gap)

## 7. Cultural Nuances & Special Cases

### 7.1 Honorifics & Number

**Japanese** (if jpn in dataset, suspected):
- Plural suffix -たち (-tachi) restricted to human animates
- Honorific contexts may require singular for respect (e.g., 先生 sensei "teacher" stays singular)

**Korean** (if kor in dataset, suspected):
- Plural suffix -들 (-deul) for animates
- Honorific register affects number usage

**Impact**: In languages with honorifics, number marking may interact with social register (not a factor in Hebrew/Greek).

### 7.2 Collective Nouns

**English**: "The people said" (singular noun, plural verb in Hebrew)

**Challenge**: Does target language mark "people" as singular or plural?

**Typological Variation**:
- Some languages: Collective nouns are **singular** (morphology)
- Other languages: Collective nouns are **plural** (semantic number)

**TBTA Policy**: Not documented (see TBTA.md Section 6, Edge Case 1)

### 7.3 Associative Plural

**Maori**: "a Pita ma" = "Peter and company" (plural marking on name implies associates)

**Other Languages**: Some Austronesian and Polynesian languages use plural on personal names to mean "X and their group"

**Example**: "Paul" (singular) vs. "Pauls" (Paul and his companions)

**TBTA Challenge**: How to mark associative plurals? Not documented.

## 8. Gaps & Limitations in Dataset

### Critical Gaps Identified

1. **No Trial Languages**: Larike, Marshallese, Tok Pisin, Sursurunga, Lihir, etc. not in dataset
   - **Impact**: Cannot test theologically precise Trinity encoding ("exactly 3 persons")
   - **Recommendation**: Add at least one trial language if possible

2. **No Slovenian**: Only modern Slavic language with productive dual
   - **Impact**: Cannot test dual in Indo-European non-Austronesian context
   - **Recommendation**: Consider adding Slovenian if resources available

3. **Limited Paucal**: Only Arabic confirmed
   - **Impact**: Cannot test "a few people" vs. "many people" distinctions
   - **Recommendation**: Acceptable for Stage 2; paucal is rare

4. **Unclear Trial Count**: TBTA claims 172 languages, scholarship confirms ~30
   - **Impact**: Uncertainty about trial prevalence
   - **Recommendation**: Stage 2 should verify via WALS, Grambank databases

### Dataset Strengths

1. **Austronesian well-represented**: 176 languages (17.5% of dataset)
2. **Root languages present**: English, Spanish, German, Arabic, Indonesian, Mandarin
3. **Family diversity**: 30+ families across 6 continents
4. **Theological languages**: Hebrew (source), Greek (source), Arabic (dual/paucal)

## 9. Summary Table: Number System by Family

| Family | Count | Simple (S/P) | Dual | Trial | Paucal | General Number | Notes |
|--------|-------|--------------|------|-------|--------|----------------|-------|
| **Austronesian** | 176 | ~130 | 2+ confirmed (haw, ton) | 0 (gap) | ~5 (estimated) | ~20 | Most complex family, but trial languages missing |
| **Indo-European** | 135 | ~134 | 0 (Slovenian gap) | 0 | 0 | ~1 | Mostly simple S/P; Slovenian dual not in dataset |
| **Trans-New Guinea** | 141 | ~140 | ~1 (estimated) | 0 | 0 | 0 | Predominantly S/P |
| **Niger-Congo** | 89 | ~89 | 0 | 0 | 0 | 0 | Noun class systems, S/P within classes |
| **Afro-Asiatic** | 25 | ~20 | 1 confirmed (arb) | 0 | 1 confirmed (arb) | 0 | Arabic most complex |
| **Sino-Tibetan** | 18 | 0 | 0 | 0 | 0 | ~18 | Classifier languages, general number |
| **Others** | ~424 | ~420 | ~4 (estimated) | 0 | 0 | 0 | Predominantly S/P |

**Legend**:
- Numbers are estimates based on typological generalizations and dataset verification
- "confirmed" = verified in dataset and/or scholarly literature
- "estimated" = not verified, inferred from typological literature
- "gap" = documented in literature but not in dataset

## 10. Recommendations for Stage 2

### Priority Actions

1. **Verify Trial Claim**: Cross-reference TBTA's "172 languages" claim with WALS Feature 33/34 and Grambank
2. **Test Dual Languages**: Analyze how Arabic, Hawaiian, Tongan handle Genesis 1:26, Ruth 1 (dual confirmed for all three)
3. **Test General Number Languages**: How do Indonesian, Mandarin handle number inference?
4. **Test Animacy Effects**: Do languages restrict number marking by animacy hierarchy?

### Research Questions for Stage 2

1. Does TBTA mark trial on **pronouns only** or also on **nouns**?
2. How does TBTA handle **lexicalized duals** (shamayim, mayim) in Hebrew?
3. Do **optional marking languages** (Indonesian, Chinese) receive number annotations in TBTA?
4. How are **collective nouns** ("people," "crowd") marked?
5. Does TBTA distinguish **dual** (exactly 2) from **plural** (2+) in languages without dual?

## Bibliography

**Linguistic Typology**:
- {corbett-2000} Corbett, Greville G. (2000). *Number*. Cambridge University Press. https://www.cambridge.org/core/books/number/497D34AB7181174CB329E8358EB2BC36
- {wals-34} WALS Feature 34: Occurrence of Nominal Plurality. https://wals.info/chapter/34
- {greenberg-universal} Greenberg, Joseph. Grammatical Number Universal 34. https://en.wikipedia.org/wiki/Grammatical_number
- {animacy-hierarchy} Animacy Hierarchy Effects on Number Marking. https://hal.science/hal-01874511v1/document

**Language-Specific**:
- {hebrew-dual} Biblical Hebrew Dual Number. https://biblicalhebrew.org/dual-form-and-its-limited-use-in-hebrew.aspx
- {koine-dual} Moulton on Greek Dual. https://koine-greek.com/2008/12/15/moulton-on-the-greek-dual/
- {slovenian-dual} Slovenian Dual Number Grammar. https://study.2tm.eu/blogs/the-dual-number-in-the-slovenian-language-practical-feature-or-complicated-nonsense/
- {indonesian-number} Indonesian Plural Semantics. https://www.researchgate.net/publication/239568420_Plural_Semantics_Reduplication_and_Numeral_Modification_in_Indonesian
- {malay-classifiers} Malay Numeral Classifiers. https://wals.info/chapter/55
- {sursurunga-trial} Sursurunga Trial Number. https://en.wikipedia.org/wiki/Sursurunga_language
- {polynesian-grammar} Polynesian Languages. https://www.britannica.com/topic/Polynesian-languages
- {hawaiian-dual-wiki} Hawaiian Grammar - Dual Number. https://en.wikipedia.org/wiki/Hawaiian_grammar
- {tongan-dual-wiki} Tongan Language - Dual Number. https://en.wikipedia.org/wiki/Tongan_language

**Dataset**:
- {languages-tsv} /src/constants/languages.tsv - 1,008 Bible translation languages

**TBTA Sources**:
- {tbta-edge-cases} TBTA Translation Edge Cases document
- {tbta-features} TBTA Feature Catalog

---

**Document Status**: Stage 1 Research Complete
**Lines**: 574
**Next Stage**: Stage 2 Analysis - Frequency analysis, verify trial languages, test proposed languages
