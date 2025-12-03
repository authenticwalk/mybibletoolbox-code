<<<<<<< HEAD
# Person System: Language Family & Typology Analysis

**Feature**: Person System (Grammatical Person + Clusivity)
**Source**: `/src/constants/languages.tsv`, WALS Feature 39A, linguistic typology
**Analysis Date**: 2025-11-26

## 1. Source Language Encoding Check (CRITICAL)

### Hebrew (Old Testament)

**Status**: ❌ CLUSIVITY NOT ENCODED in morphology

**Evidence**:
- Hebrew אֲנַחְנוּ (*anachnu*) = "we" (AMBIGUOUS - no distinction between inclusive/exclusive)
- No morphological marking for inclusive vs. exclusive first person
- Only 1st/2nd/3rd person distinctions exist morphologically

**Encoding**: Hebrew marks person (1/2/3) and number (singular/plural/dual) but NOT clusivity.

**Implication**: TBTA's inclusive/exclusive distinction for Hebrew source text is **INTERPRETIVE**, not morphologically explicit. This is a **high-value annotation** for translation.

### Greek (New Testament)

**Status**: ❌ CLUSIVITY NOT ENCODED in morphology

**Evidence**:
- Greek ἡμεῖς (*hēmeis*) = "we" (AMBIGUOUS - no inclusive/exclusive distinction)
- ἐγώ (*egō*) = "I"
- σύ (*sy*) = "you" (singular)
- ὑμεῖς (*hymeis*) = "you" (plural)

**Encoding**: Greek marks person (1/2/3) and number (singular/plural) but NOT clusivity.

**Implication**: Like Hebrew, clusivity determination in Greek text is **SEMANTIC/CONTEXTUAL**, requiring exegetical analysis.

### English (Major Translation Source)

**Status**: ❌ CLUSIVITY NOT ENCODED

**Evidence**:
- English "we" is ambiguous (no inclusive/exclusive distinction)
- "I" (1st singular), "we" (1st plural), "you" (2nd), "he/she/it/they" (3rd)

**Encoding**: English has basic 3-way person system (1/2/3) with no clusivity.

## 2. Language Family Distribution

**Sources**:
- WALS Feature 39A: Inclusive/Exclusive Distinction in Independent Pronouns {wals-39a}
- `/src/constants/languages.tsv` (1,009 languages analyzed)
- Wikipedia: Clusivity {wiki-clusivity}

{wals-39a}: https://wals.info/feature/39A
{wals-39a-chapter}: https://wals.info/chapter/39
{wiki-clusivity}: https://en.wikipedia.org/wiki/Clusivity

### Global Distribution (WALS Data)

**From 200 languages surveyed by WALS**:

| Category | Count | Percentage | Description |
|----------|-------|------------|-------------|
| Inclusive/Exclusive (both forms) | 63 | 31.5% | Full distinction {wals-39a-chapter} |
| No distinction | 120 | 60% | Like English - ambiguous "we" {wals-39a-chapter} |
| Only inclusive marked | 5 | 2.5% | Exclusive = "I" form {wals-39a-chapter} |
| 'We' same as 'I' | 10 | 5% | Plural identical to singular {wals-39a-chapter} |
| No 'we' | 2 | 1% | No first-person plural {wals-39a-chapter} |

**Key Finding**: Approximately **1/3 of world's languages** have inclusive/exclusive distinction {wals-39a}.

### Top Language Families in Dataset

**From `/src/constants/languages.tsv`** (1,009 languages analyzed):

| Rank | Family | Count | Clusivity Relevance |
|------|--------|-------|---------------------|
| 1 | **Austronesian** | 176 | **CRITICAL** - Nearly universal clusivity {wals-39a-chapter} |
| 2 | Trans-New Guinea | 141 | LOW - Mostly absent {wals-39a-chapter} |
| 3 | Indo-European | 135 | ABSENT - No European language has it {wals-39a-chapter} |
| 4 | Niger-Congo | 89 | ABSENT - Rare in Africa {wals-39a-chapter} |
| 5 | Otomanguean | 69 | MEDIUM - Some Mesoamerican languages (suspected) |
| 6 | Mayan | 41 | MEDIUM - Some languages (suspected) |
| 7 | Australian | 36 | **HIGH** - Non-Pama-Nyungan nearly universal {wals-39a-chapter} |
| 8 | Afro-Asiatic | 25 | ABSENT - Semitic lacks it {wals-39a-chapter} |
| 9 | Uto-Aztecan | 21 | MEDIUM - Some languages (suspected) |
| 10 | Sino-Tibetan | (not in top 10) | **HIGH** - Mandarin has it {wals-39a-chapter} |

## 3. Required Language Families (Grammatically Mandatory)

### Family 1: Austronesian (176 languages in dataset)

**Clusivity Status**: **NEARLY UNIVERSAL** - "Almost all languages have the distinction" {wals-39a-chapter}

**Evidence**:
- {wals-39a-chapter}: "In both groups [Austronesian and Australian], almost all languages have the distinction."
- {tbta-source/TBTA-FEATURES.md}: "Person System | 1st/2nd/3rd + Inclusive/Exclusive (8-way system) | Tagalog, Malay, Fijian, Vietnamese"
- {medium-clusivity}: "In Malay and Indonesian, *kita* is inclusive and *kami* is exclusive."
- {apics-clusivity}: "Most Austronesian languages distinguish first person plural inclusive and exclusive"

{medium-clusivity}: https://medium.com/language-lab/the-many-faces-of-we-dd41df4879ba
{apics-clusivity}: https://apics-online.info/parameters/15.chapter.html

**Examples from Dataset**:

| ISO-639-3 | Language | Country | Inclusive | Exclusive | Status |
|-----------|----------|---------|-----------|-----------|--------|
| tgl | Tagalog | Philippines | *tayo* | *kami* | Mandatory {tbta-source} |
| zsm/ind | Malay/Indonesian | Malaysia/Indonesia | *kita* | *kami* | Mandatory {medium-clusivity} |
| fij | Fijian | Fiji | (forms exist) | (forms exist) | Mandatory {tbta-source} |
| vie | Vietnamese | Vietnam | (has distinction) | (has distinction) | Mandatory {tbta-source} |
| haw | Hawaiian | United States | (has distinction) | (has distinction) | Mandatory {wals-39a-chapter} |
| ceb | Cebuano | Philippines | (has distinction) | (has distinction) | Mandatory (suspected) |
| ilo | Ilocano | Philippines | (has distinction) | (has distinction) | Mandatory (suspected) |
| pam | Pampangan | Philippines | (has distinction) | (has distinction) | Mandatory (suspected) |
| war | Waray | Philippines | (has distinction) | (has distinction) | Mandatory (suspected) |
| pau | Palauan | Palau | (has distinction) | (has distinction) | Mandatory (suspected) |

**Note on Indonesian**: {medium-clusivity} reports colloquial tendency to merge *kami* (exclusive) with *kita* (inclusive) in modern usage, but formal/written language maintains distinction.

**Additional Complexity**: {apics-clusivity} - "Some languages with trial ('exactly three') or paucal ('a few') marking in the inclusive and the exclusive are also found... for example, in Paamese (Oceanic; Vanuatu). Languages that exhibit clusivity in the first person and also have a dual number in personal pronouns can actually have up to a four-way distinction, as seen in Hawaiian."

### Family 2: Australian (Non-Pama-Nyungan) (36 languages in dataset)

**Clusivity Status**: **NEARLY UNIVERSAL** in non-Pama-Nyungan languages {wals-39a-chapter}

**Evidence**:
- {wals-39a-chapter}: "In both groups [Austronesian and Australian], almost all languages have the distinction. In contrast, it is rather uncommon... among the non-Austronesian ('Papuan') languages of New Guinea."
- Pama-Nyungan languages show "areal patterns near northern boundaries" {wals-39a-chapter}

**Examples from Dataset** (suspected classifications):

| ISO-639-3 | Language | Family | Clusivity |
|-----------|----------|--------|-----------|
| aer | Arrernte, Eastern | Australian | Mandatory (suspected) |
| aly | Alyawarr | Australian | Mandatory (suspected) |
| amx | Anmatyerre | Australian | Mandatory (suspected) |
| aoi | Anindilyakwa | Australian | Mandatory (suspected) |

**Note**: Dataset does not clearly distinguish Pama-Nyungan from non-Pama-Nyungan. Further research needed.

### Family 3: Sino-Tibetan (Mandarin Chinese)

**Clusivity Status**: **MANDATORY** in Mandarin

**Evidence**:
- {wals-39a-chapter}: "Mandarin Chinese" listed as Type 5 (both inclusive and exclusive differentiated)
- {apics-clusivity}: "The great majority of the world's most spoken languages with clusivity are... among northern varieties of Chinese."

**Examples**:
- Mandarin: 咱们 (*zánmen*) = inclusive "we" (you and I)
- Mandarin: 我们 (*wǒmen*) = exclusive "we" (I and others, not you) {wals-39a-chapter}

**Dataset**: Mandarin Chinese is NOT in `/src/constants/languages.tsv` (focused on minority languages).

### Family 4: Dravidian (South India)

**Clusivity Status**: **WIDESPREAD** in Dravidian languages

**Evidence**:
- {apics-clusivity}: "The great majority of the world's most spoken languages with clusivity are found among Austronesian languages (in particular Malay and Javanese), among Dravidian languages (in particular Tamil and Telugu)"
- {wals-39a-chapter}: Lists Dravidian as major family with clusivity

**Examples from Literature** (not in dataset):
- Tamil: நாம் (*nām*) = inclusive, நாங்கள் (*nāṅkaḷ*) = exclusive (suspected)
- Telugu: మనం (*manaṁ*) = inclusive, మేము (*mēmu*) = exclusive (suspected)

**Dataset**: Dravidian languages are NOT well-represented in `/src/constants/languages.tsv`.

### Family 5: Quechuan (South America)

**Clusivity Status**: **MANDATORY**

**Evidence**:
- {wals-39a-chapter}: Lists Quechuan as major family
- Historical note {wals-39a-chapter}: "The discovery was made by the Dominican friar Domingo de Santo Tomás, as described in his grammar of Quechua, the language of the Incas, first published in 1560."

**Examples from Dataset**:
- Quechua varieties present in dataset (needs verification)

## 4. Available Language Analysis (from languages.tsv)

### Languages REQUIRING Clusivity Marking (Mandatory)

Based on family classification and linguistic typology:

#### Austronesian Family (176 languages) - NEARLY ALL MANDATORY

**Philippine Subgroup** (high representation in dataset):

| ISO-639-3 | Language | Country | Inclusive | Exclusive | Certainty |
|-----------|----------|---------|-----------|-----------|-----------|
| tgl | Tagalog | Philippines | *tayo* | *kami* | Confirmed {tbta-source} |
| ceb | Cebuano | Philippines | (exists) | (exists) | Mandatory (suspected) |
| ilo | Ilocano | Philippines | (exists) | (exists) | Mandatory (suspected) |
| hil | Hiligaynon | Philippines | (exists) | (exists) | Mandatory (suspected) |
| war | Waray | Philippines | (exists) | (exists) | Mandatory (suspected) |
| pam | Pampangan | Philippines | (exists) | (exists) | Mandatory (suspected) |
| pag | Pangasinan | Philippines | (exists) | (exists) | Mandatory (suspected) |
| bik | Bikol | Philippines | (exists) | (exists) | Mandatory (suspected) |

**Malayo-Polynesian Subgroup**:

| ISO-639-3 | Language | Country | Inclusive | Exclusive | Certainty |
|-----------|----------|---------|-----------|-----------|-----------|
| zsm | Malay | Malaysia | *kita* | *kami* | Confirmed {medium-clusivity} |
| ind | Indonesian | Indonesia | *kita* | *kami* | Confirmed {medium-clusivity} |
| jav | Javanese | Indonesia | (exists) | (exists) | Confirmed {apics-clusivity} |
| sun | Sundanese | Indonesia | (exists) | (exists) | Mandatory (suspected) |
| mad | Madurese | Indonesia | (exists) | (exists) | Mandatory (suspected) |
| min | Minangkabau | Indonesia | (exists) | (exists) | Mandatory (suspected) |

**Oceanic Subgroup**:

| ISO-639-3 | Language | Country | Inclusive | Exclusive | Certainty |
|-----------|----------|---------|-----------|-----------|-----------|
| fij | Fijian | Fiji | (exists) | (exists) | Confirmed {tbta-source} |
| haw | Hawaiian | United States | (4-way) | (4-way) | Confirmed {apics-clusivity} |
| pau | Palauan | Palau | (exists) | (exists) | Mandatory (suspected) |
| chk | Chuukese | Micronesia | (exists) | (exists) | Mandatory (suspected) |
| kos | Kosraean | Micronesia | (exists) | (exists) | Mandatory (suspected) |
| poh | Pohnpeian | Micronesia | (exists) | (exists) | Mandatory (suspected) |
| mah | Marshallese | Marshall Islands | (exists) | (exists) | Mandatory (suspected) |
| smo | Samoan | Samoa | (exists) | (exists) | Mandatory (suspected) |
| ton | Tongan | Tonga | (exists) | (exists) | Mandatory (suspected) |

**Note**: {apics-clusivity} reports "trial or paucal marking only occurs among Austronesian languages" - Paamese (Vanuatu) example given.

#### Australian Family (36 languages) - NON-PAMA-NYUNGAN MANDATORY

| ISO-639-3 | Language | Subgroup | Clusivity | Certainty |
|-----------|----------|----------|-----------|-----------|
| aer | Arrernte, Eastern | Pama-Nyungan (Arandic) | Kinship-based (not traditional clusivity) | Confirmed {arrernte-pronouns} |
| aly | Alyawarr | Pama-Nyungan (Arandic) | Mandatory | Suspected (has I/E per dialectal reports) {arrernte-pronouns} |
| aoi | Anindilyakwa | Gunwinyguan | Mandatory | Suspected |
| gup | Gunwinggu | Gunwinyguan | Mandatory | Suspected |

{arrernte-pronouns}: Based on linguistic research, Central/Eastern Arrernte encodes kinship-based distinctions (agnatic, harmonious, disharmonious) in non-singular pronouns rather than traditional inclusive/exclusive clusivity. Alyawarr (related Arandic language) shows dialectal inclusive/exclusive distinctions.

**Note**: Need to distinguish Pama-Nyungan (variable) from non-Pama-Nyungan (nearly universal) {wals-39a-chapter}. Arandic languages show complex pronominal systems with kinship-based distinctions.

### Languages NOT Requiring Clusivity (Absent)

#### Indo-European Family (135 languages) - COMPLETELY ABSENT

{wals-39a-chapter}: "This distinction between inclusive and exclusive is not found in any European language, nor in the languages in its wider surrounding."

**Examples from Dataset**:

| ISO-639-3 | Language | Subfamily | Clusivity |
|-----------|----------|-----------|-----------|
| eng | English | Germanic | Absent (confirmed) |
| spa | Spanish | Romance | Absent (confirmed) |
| fra | French | Romance | Absent (confirmed) |
| deu | German | Germanic | Absent (confirmed) |
| rus | Russian | Slavic | Absent (confirmed) |
| pol | Polish | Slavic | Absent (confirmed) |
| por | Portuguese | Romance | Absent (confirmed) |

#### Afro-Asiatic Family (25 languages) - ABSENT

{wals-39a-chapter}: "In general, the inclusive/exclusive distinction is rather uncommon in Africa and Eurasia."

**Examples from Dataset**:

| ISO-639-3 | Language | Subfamily | Clusivity |
|-----------|----------|-----------|-----------|
| heb | Hebrew | Semitic | Absent (confirmed - source language) |
| arb | Arabic, Standard | Semitic | Absent (confirmed) {apics-clusivity} |
| aii | Assyrian Neo-Aramaic | Semitic | Absent (suspected) |
| amh | Amharic | Semitic | Absent (suspected) |

#### Niger-Congo Family (89 languages) - MOSTLY ABSENT

{apics-clusivity}: "This distinction is not found at all in European languages, and is hardly found in West African, Bantu and Semitic languages."

**Examples from Dataset**:

| ISO-639-3 | Language | Subfamily | Clusivity |
|-----------|----------|-----------|-----------|
| swa | Swahili | Bantu | Absent (suspected) {apics-clusivity} |
| zul | Zulu | Bantu | Absent (suspected) {apics-clusivity} |
| aka | Akan | Niger-Congo | Absent (suspected) {apics-clusivity} |

## 5. Root Languages (Major Bible Translation Sources)

**Analysis**: Which major "root languages" (languages translators commonly work from) have clusivity?

| Language | Family | Clusivity | Impact on Translation |
|----------|--------|-----------|----------------------|
| **Hebrew** | Afro-Asiatic | ❌ ABSENT | Must interpret from context |
| **Greek** | Indo-European | ❌ ABSENT | Must interpret from context |
| **Latin** | Indo-European | ❌ ABSENT | No help for clusivity |
| **English** | Indo-European | ❌ ABSENT | No help for clusivity |
| **Spanish** | Indo-European | ❌ ABSENT | No help for clusivity |
| **German** | Indo-European | ❌ ABSENT | No help for clusivity |
| **French** | Indo-European | ❌ ABSENT | No help for clusivity |
| **Arabic** | Afro-Asiatic | ❌ ABSENT | No help for clusivity {apics-clusivity} |
| **Indonesian** | Austronesian | ✅ PRESENT | *kita* (incl) / *kami* (excl) {medium-clusivity} |
| **Swahili** | Niger-Congo | ❌ ABSENT | No help (suspected) {apics-clusivity} |

**CRITICAL FINDING**: Only **Indonesian** (Malay) among major regional Bible translation languages has clusivity distinction. All major European and Semitic languages lack it.

**Implication**: Translators working in clusivity-marking languages (Tagalog, Fijian, etc.) cannot rely on source texts or common translation languages - they need **TBTA's interpretive annotations**.

## 6. Language Candidates for Translation Database (Stage 2)

**Selection Criteria**:
- Mix of marking vs. non-marking languages
- Diverse language families
- Languages available in `/src/constants/languages.tsv`
- Representative of global distribution

### Proposed 10 Languages for Stage 2 Analysis:

| # | ISO-639-3 | Language | Family | Clusivity | Rationale |
|---|-----------|----------|--------|-----------|-----------|
| 1 | **tgl** | Tagalog | Austronesian | ✅ Mandatory | TBTA example, well-documented {tbta-source} |
| 2 | **ind** | Indonesian | Austronesian | ✅ Mandatory | Major regional language {medium-clusivity} |
| 3 | **fij** | Fijian | Austronesian (Oceanic) | ✅ Mandatory | TBTA example, Oceanic representative {tbta-source} |
| 4 | **haw** | Hawaiian | Austronesian (Polynesian) | ✅ Mandatory + 4-way | Complex system {apics-clusivity} |
| 5 | **vie** | Vietnamese | Austroasiatic | ✅ Mandatory | TBTA example, confirmed chúng ta/chúng tôi {vie-pronouns} |
| 6 | **eng** | English | Indo-European | ❌ Absent | Source language, baseline |
| 7 | **spa** | Spanish | Indo-European | ❌ Absent | Major translation language |
| 8 | **swa** | Swahili | Niger-Congo (Bantu) | ❌ Absent | African representative {apics-clusivity} |
| 9 | **aly** | Alyawarr | Australian (Arandic) | ✅ Mandatory (suspected) | Australian representative with I/E distinction {arrernte-pronouns} |
| 10 | **cmn** | Mandarin Chinese | Sino-Tibetan | ✅ Mandatory | Major language, zánmen/wǒmen {wals-39a-chapter} |

**Note**: Mandarin (cmn) may not be in dataset - substitute with available Sino-Tibetan language if needed.

## 7. Cultural Nuances (Honorific Person Systems)

### Honorifics vs. Clusivity (Distinct Features)

**Important Distinction**:
- **Clusivity**: Inclusive vs. exclusive "we" - semantic distinction
- **Honorifics**: Formal vs. informal "you" - social register distinction

{tbta-source/TBTA.md}: "TBTA does not encode honorific distinctions in the Person field itself. Honorific person systems (T/V distinction, formal/informal 'you') are handled separately by Speaker Demographics (Feature #13)."

### Languages with Honorific Person Systems

#### Japanese (jpn)

**Honorific Complexity**: **EXTREME** - Multiple levels of formality

**Second Person "You"** (all = "2" in Person field, differ in register):
- あなた (*anata*) - neutral/polite
- お前 (*omae*) - informal/rude
- 貴様 (*kisama*) - hostile
- そちら (*sochira*) - polite/distant

**First Person "I"** (all = "1" in Person field, differ in register):
- 私 (*watashi*) - formal
- 僕 (*boku*) - casual (male)
- 俺 (*ore*) - very casual (male)

**Clusivity**: Japanese does NOT have inclusive/exclusive distinction - "we" = 私たち (*watashitachi*) is ambiguous.

**TBTA Encoding**: Person = "2" or "1", honorific level in Speaker Demographics feature {tbta-source/TBTA.md}.

#### Korean (kor)

**Honorific Complexity**: **EXTREME** - Multiple levels (similar to Japanese)

**Second Person "You"**:
- 당신 (*dangsin*) - formal
- 너 (*neo*) - informal
- 자네 (*jane*) - older to younger

**First Person "I"**:
- 저 (*jeo*) - humble/formal
- 나 (*na*) - casual

**Clusivity**: Korean does NOT have inclusive/exclusive distinction.

#### Javanese (jav)

**Honorific Complexity**: **EXTREME** - Three speech levels (ngoko, madya, krama)

**Evidence**: {apics-clusivity} mentions Javanese among major languages with clusivity.

**Note**: Javanese has BOTH clusivity (Austronesian feature) AND honorifics (cultural feature).

#### Tagalog (tgl)

**Honorific Complexity**: **MODERATE**

**Second Person "You"**:
- *ikaw* / *ka* - familiar
- *kayo* - polite (plural form used as polite singular)

**Clusivity**: ✅ YES
- *tayo* - inclusive "we"
- *kami* - exclusive "we"

**TBTA Encoding**: Person field encodes clusivity (A/B codes); honorific register in Speaker Demographics.

### T-V Distinction (European Languages)

**Concept**: Formal vs. informal "you" (from Latin *tu* vs. *vos*)

**Examples**:
- Spanish: *tú* (informal) vs. *usted* (formal)
- French: *tu* (informal) vs. *vous* (formal)
- German: *du* (informal) vs. *Sie* (formal)

**TBTA Encoding**: Both = "2" (Second Person), register distinguished via Speaker Demographics {tbta-source/TBTA.md}.

**Clusivity**: All these languages LACK inclusive/exclusive distinction.

## 8. Geographic Distribution Summary

**From WALS and research**:

| Region | Clusivity Prevalence | Notes |
|--------|---------------------|-------|
| **Europe** | ❌ ABSENT | No European language has it {wals-39a-chapter} |
| **Africa** | ❌ RARE | Uncommon in Africa {wals-39a-chapter} |
| **Middle East** | ❌ ABSENT | Semitic languages lack it |
| **South Asia** | ✅ COMMON | Dravidian languages {apics-clusivity} |
| **Southeast Asia** | ✅ COMMON | Austronesian, Sino-Tibetan {wals-39a-chapter} |
| **East Asia** | ✅ COMMON | Mandarin and northern Chinese {apics-clusivity} |
| **Pacific** | ✅ NEARLY UNIVERSAL | Austronesian dominance {wals-39a-chapter} |
| **Australia** | ✅ COMMON | Non-Pama-Nyungan near-universal {wals-39a-chapter} |
| **Americas** | ✅ SCATTERED | Quechuan, some Mesoamerican, some North American {wals-39a-chapter} |
| **New Guinea** | ❌ RARE | Papuan languages mostly lack it {wals-39a-chapter} |

## 9. Summary Statistics

**Global Prevalence** (from WALS 200-language sample):
- **31.5%** of languages have full inclusive/exclusive distinction
- **60%** have no distinction (like English)
- **Approximately 1,000+ languages** estimated to have clusivity (TBTA estimate {tbta-source/README.md})

**Dataset Coverage** (1,009 languages in `/src/constants/languages.tsv`):
- **Austronesian: 176 languages** (nearly all have clusivity) ≈ 176 languages
- **Australian: 36 languages** (many have clusivity) ≈ 20-30 languages (estimated)
- **Other families**: Scattered distribution
- **Estimated total with clusivity in dataset**: ~200-250 languages (20-25%)

**Critical Languages for Bible Translation**:
- Major clusivity languages: Tagalog (45M speakers), Indonesian (43M L1, 156M L2), Vietnamese (85M), Fijian (350K), Mandarin (900M+)
- These represent **BILLIONS** of speakers requiring clusivity-aware Bible translation

## 10. Typological Classification Summary

### Mandatory Clusivity (Must Mark):
- **Austronesian family** (nearly all 176 languages in dataset)
- **Australian (non-Pama-Nyungan)** (majority of 36 languages)
- **Dravidian** (Tamil, Telugu - not in dataset)
- **Sino-Tibetan (Mandarin)** (not in dataset)
- **Quechuan** (limited in dataset)

### Optional Clusivity (Can Mark):
- Very rare - most languages either have it (mandatory) or lack it entirely

### Absent Clusivity (Cannot Mark):
- **All Indo-European** (135 languages in dataset) {wals-39a-chapter}
- **All Afro-Asiatic** (25 languages in dataset) {wals-39a-chapter}
- **Most Niger-Congo** (89 languages in dataset) {apics-clusivity}
- **Most Trans-New Guinea** (141 languages in dataset) {wals-39a-chapter}

## 11. Bibliography

{wals-39a}: Cysouw, Michael. 2013. Inclusive/Exclusive Distinction in Independent Pronouns. In: Dryer, Matthew S. & Haspelmath, Martin (eds.) The World Atlas of Language Structures Online. Leipzig: Max Planck Institute for Evolutionary Anthropology. https://wals.info/feature/39A

{wals-39a-chapter}: Cysouw, Michael. 2013. Inclusive/Exclusive Distinction in Independent Pronouns. In: Dryer, Matthew S. & Haspelmath, Martin (eds.) WALS Online (v2020.3). Zenodo. https://wals.info/chapter/39

{wiki-clusivity}: Wikipedia contributors. (2024). Clusivity. Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Clusivity

{medium-clusivity}: Paiman, Norazha. (2020). The Many Faces of 'We': Inclusive and exclusive pronouns. Medium Language Lab. https://medium.com/language-lab/the-many-faces-of-we-dd41df4879ba

{apics-clusivity}: Michaelis, Susanne Maria & Maurer, Philippe & Haspelmath, Martin & Huber, Magnus (eds.) 2013. Chapter 15: Inclusive/exclusive distinction in independent personal pronouns. In: APiCS Online. Leipzig: Max Planck Institute for Evolutionary Anthropology. https://apics-online.info/parameters/15.chapter.html

{tbta-source/TBTA-FEATURES.md}: Internal TBTA documentation - `/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md`

{tbta-source/README.md}: Internal TBTA documentation - `/bible-study-tools/tbta/tbta-source/README.md`

{tbta-source/DATA-STRUCTURE.md}: Internal TBTA documentation - `/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md`

{tbta-source/TBTA.md}: Internal research - `/bible-study-tools/tbta/features/person-system/research/TBTA.md`

{vie-pronouns}: Vietnamese pronouns - inclusive (chúng ta, chúng mình) vs. exclusive (chúng tôi, chúng tao). Wikipedia. https://en.wikipedia.org/wiki/Vietnamese_pronouns

{arrernte-pronouns}: Arrernte/Arandic pronominal systems - kinship-based distinctions in Central/Eastern Arrernte, dialectal I/E distinctions in Alyawarr. Based on linguistic research including Breen's Grammar of Arandic Kinship Terminology and related sources.
=======
# Language Family & Typology Analysis: Person Systems & Clusivity

## Executive Summary

Grammatical person systems vary from simple 3-way (1st/2nd/3rd) to complex systems including clusivity (inclusive/exclusive distinction in first person plural). **Critical finding**: Hebrew and Greek do NOT encode clus ivity morphologically, but approximately **31.5% of world languages do** {wals-clusivity-2025}. This feature is **nearly universal in Austronesian** (1000+ languages), common in Americas, Australia, and parts of Asia, but **rare in Europe and Africa** {wikipedia-clusivity-2025}.

**Translation Impact**: For ~1/3 of world languages, translators must disambiguate every "we" in Scripture based on context—getting it wrong can alter theological meaning (e.g., Trinity references, apostolic authority).

---

## 1. Source Language Encoding (Hebrew & Greek)

### CRITICAL: Clusivity is NOT Encoded in Biblical Source Languages

**Hebrew**:
- First person singular: אֲנִי (ani), אָנֹכִי (anokhi)
- First person plural: אֲנַחְנוּ (anachnu), נוּ (nu suffix)
- **NO** morphological distinction between inclusive/exclusive "we"

**Greek (Koine)**:
- First person singular: ἐγώ (egō)
- First person plural: ἡμεῖς (hēmeis), ἡμῶν (hēmōn), ἡμῖν (hēmin), ἡμᾶς (hēmas)
- **NO** morphological distinction between inclusive/exclusive "we"

{koine-greek-clusivity-2025}

**Implication**: All clusivity annotations in TBTA (and all translations into clusivity-marking languages) are **INTERPRETIVE**, based on contextual/exegetical analysis, not morphological encoding.

---

## 2. Global Distribution of Clusivity

### Geographic Patterns

From WALS chapter 39 {wals-clusivity-2025}:

| Region | Prevalence | Notes |
|--------|------------|-------|
| **Austronesia** | Nearly universal | ~1000+ languages |
| **Northern Australia** | Nearly universal | All surveyed languages |
| **Americas** | Common | North, Central, South America |
| **Asia (South/SE)** | Common | Dravidian, some Sino-Tibetan, Vietnamese |
| **Papuan** | Rare | Despite proximity to Austronesian |
| **Europe** | Absent (except Caucasus) | No Indo-European outside Caucasus |
| **Africa** | Sporadic | Rare in Niger-Congo, Nilo-Saharan |

### Statistical Prevalence

- **31.5%** of world languages show inclusive/exclusive distinction (WALS sample of 200 languages: 63 with distinction, 137 without) {wals-clusivity-2025}
- **68.5%** of languages do NOT mark clusivity
- Among languages WITH clusivity, the feature is often **obligatory** (must be marked on every first person plural pronoun)

---

## 3. Language Family Analysis

### Families That REQUIRE Clusivity (Mandatory)

#### Austronesian (Nearly Universal)

The inclusive–exclusive distinction occurs **nearly universally among the Austronesian languages** {wikipedia-clusivity-2025}.

**Examples from our translation database**:

| Language (ISO) | Family | Example Pronouns | Country | Status |
|----------------|--------|------------------|---------|--------|
| **Tagalog** (tgl) | Austronesian | *tayo* (incl) vs *kami* (excl) | Philippines | Mandatory |
| **Malay** (zlm) | Austronesian | *kita* (incl) vs *kami* (excl) | Malaysia/Indonesia | Mandatory (but *kami* falling out of use) |
| **Fijian** (fij) | Austronesian | Dual/trial/plural all distinguish | Fiji | Mandatory |
| **Cebuano** (ceb) | Austronesian | Similar to Tagalog | Philippines | Mandatory (suspected) |
| **Chuukese** (chk) | Austronesian | Micronesian system | Micronesia | Mandatory (suspected) |
| **Chamorro** (cha) | Austronesian | Micronesian system | Guam | Mandatory (suspected) |

**Additional Austronesian languages in our database** (likely mandatory, pending verification):
- Miniafia (aai), Ankave (aak), Abau (aau), Amarasi (aaz), Ambulas (abt), Inabaknon (abx)
- 200+ more Austronesian languages from Papua New Guinea, Philippines, Indonesia, Solomon Islands, Vanuatu, Micronesia

#### Australian Languages (Nearly Universal)

**Examples from our database**:

| Language (ISO) | Example | Country | Status |
|----------------|---------|---------|--------|
| **Arrernte, Eastern** (aer) | Dual: *ngali* (incl) vs *ngaliju* (excl) | Australia | Mandatory |
| **Alyawarr** (aly) | Similar to Arrernte | Australia | Mandatory (suspected) |
| **Burarra** (bvr) | Northern Australian | Australia | Mandatory (suspected) |

Many Australian languages distinguish clusivity **especially in dual number** {wals-clusivity-2025}.

#### Dravidian Languages

**Most Dravidian languages have a clusivity distinction** {wikipedia-clusivity-2025}.

**Examples**:
- **Tamil**: *ñām* (inclusive) vs *yām* (exclusive) - not in our database
- **Telugu**: *mana-* (inclusive) vs *ma-* (exclusive) - not in our database
- Dravidian clusivity was borrowed into some Indo-European languages of India (Gujarati, Marathi, Punjabi) as substrate {wikipedia-clusivity-2025}

**Note**: No Dravidian languages found in our current translation database.

#### Sino-Tibetan (Partial - Northern Mandarin)

**Mandarin Chinese** (cmn):
- Inclusive: 咱们 *zánmen* (you and I and possibly others)
- Ambiguous/Exclusive: 我们 *wǒmen* (I and others, may or may not include you)
- **Status**: Optional/contextual (not strictly exclusive)
- **Historical note**: Acquired from Altaic languages (Mongolian, Manchu, Turkic) after late Tang {languagelog-clusivity-2025}

Other Sino-Tibetan:
- **Burmese (Chin languages)** in our database (cek, csy, cth): Mandatory (suspected)

#### Quechuan, Aymaran (South America)

Discovered in **1560 by Domingo de Santo Tomás** (first description of clusivity) {wikipedia-clusivity-2025}.

**Not represented in our database** - but historically significant for identifying the feature.

### Families That LACK Clusivity (Absent)

#### Indo-European (with rare exceptions)

**NO European language outside the Caucasus makes this distinction grammatically** {wikipedia-clusivity-2025}.

**Languages in our database WITHOUT clusivity**:
- **English** (eng): No distinction
- **Spanish** (spa): No distinction
- **German** (deu): No distinction
- **French** (fra): No distinction (assumed - not explicitly in database but standard Indo-European)
- **Russian** (rus): No distinction (assumed)
- **Greek** (Modern): No distinction (Koine Greek also lacks it)

**Note**: Some Indo-European languages of India acquired clusivity as substrate from Dravidian (Gujarati, Marathi, Odia, Punjabi) {wikipedia-clusivity-2025}, but these are not in our database.

#### Afro-Asiatic

**Hebrew, Arabic, Coptic, Assyrian Neo-Aramaic** (aii, arb, cop) in our database: **No clusivity**

#### Most Papuan Languages

Despite proximity to Austronesian, **Papuan languages rarely show clusivity** {wikipedia-clusivity-2025}.

**Trans-New Guinea family** (200+ languages in our database): Mostly absent (suspected)

---

## 4. Root/Bridge Languages for Bible Translation

### Definition
A "root language" is a source language translators commonly use as their starting point, prioritizing Hebrew/Greek but often using regional dominant languages.

### Clusivity Status of Major Root Languages

| Language | ISO-639-3 | Family | Clusivity | Role |
|----------|-----------|--------|-----------|------|
| **Hebrew** | heb | Afro-Asiatic | **ABSENT** | Original OT |
| **Greek** (Koine/Modern) | grc/ell | Indo-European | **ABSENT** | Original NT |
| **Latin** | lat | Indo-European | **ABSENT** | Historical bridge |
| **English** | eng | Indo-European | **ABSENT** | Global bridge |
| **Spanish** | spa | Indo-European | **ABSENT** | Latin America bridge |
| **French** | fra | Indo-European | **ABSENT** | Africa bridge |
| **Arabic** | arb | Afro-Asiatic | **ABSENT** | Middle East bridge |
| **Swahili** | swa | Niger-Congo | **ABSENT** (suspected) | East Africa bridge |
| **Indonesian/Malay** | ind/zlm | Austronesian | **MANDATORY** | SE Asia bridge ✅ |
| **Mandarin Chinese** | cmn | Sino-Tibetan | **OPTIONAL** | East Asia bridge ⚠️ |

**Key Finding**: Of the 10 major root languages, **only Indonesian/Malay REQUIRES clusivity**, and Mandarin optionally marks it. All others lack the distinction entirely.

**Translation Challenge**: When translating from non-clusivity languages (Hebrew/Greek/English) into clusivity-required languages (Austronesian, Australian, Dravidian), translators must infer clusivity from **context alone**.

---

## 5. Analysis of Available Translations (Sample)

From `/workspace/src/constants/languages.tsv` (1008 total translations):

### Austronesian Languages (Estimated ~250-300 in database)

**Mandatory clusivity** (high confidence):
- Tagalog (tgl), Malay (zlm), Cebuano (ceb), Chuukese (chk), Chamorro (cha)
- Filipino Austronesian: Agutaynen (agn), Binukid (bkd), Blaan varieties (bpr, bps), Bontok (ebk)
- Indonesian Austronesian: Alune (alp), Ambai (amk), Balantak (blz)
- PNG Austronesian: 100+ languages from Papua New Guinea
- Solomon Islands/Vanuatu: Arosi (aia), Sa'a (apb), Baki (bki)

### Australian Languages (Estimated ~30 in database)

**Mandatory clusivity** (especially in dual):
- Arrernte (aer, are), Alyawarr (aly), Burarra (bvr), Dhangu (dhg), Djinang (dji)

### Sino-Tibetan (Optional clusivity)

**Mandarin** (cmn): Optional
**Chin languages** (cek, csy, cth): Mandatory (suspected based on family)

### Indo-European (~50 in database)

**Absent**: English (eng), Spanish (spa), German (deu), Czech (ces), Danish (dan), Russian (rus - not in db), French (fra - not in db)

### Trans-New Guinea (~200+ in database)

**Mostly absent** (suspected, pending verification)

### Niger-Congo (~50 in database)

**Mostly absent** (suspected, pending verification)

### Mayan (~20 in database)

**Unknown** - requires further research. Possible clusivity in some branches.

---

## 6. Candidate Languages for Translation Database (Stage 2)

**Criteria**:
1. Mix of clusivity-marking vs non-marking
2. Diverse language families
3. Availability in our translation database
4. Theological/geographical significance

### Recommended 10 Languages

| # | Language | ISO | Family | Clusivity | Rationale |
|---|----------|-----|--------|-----------|-----------|
| 1 | **Tagalog** | tgl | Austronesian | **Mandatory** | Large speaker base, clear incl/excl distinction, Philippines |
| 2 | **Malay** | zlm | Austronesian | **Mandatory** | Bridge language for Indonesia/Malaysia, 200M+ speakers |
| 3 | **Mandarin Chinese** | cmn | Sino-Tibetan | **Optional** | 1B+ speakers, optionally marks clusivity (zánmen vs wǒmen) |
| 4 | **English** | eng | Indo-European | **Absent** | Global bridge language, no clusivity |
| 5 | **Spanish** | spa | Indo-European | **Absent** | Latin America bridge, no clusivity |
| 6 | **Cebuano** | ceb | Austronesian | **Mandatory** | Philippines, similar to Tagalog |
| 7 | **Arrernte (Eastern)** | aer | Australian | **Mandatory (dual)** | Australian Aboriginal, marks clusivity in dual number |
| 8 | **Fijian** | fij | Austronesian | **Mandatory** | Pacific, trial/dual distinctions |
| 9 | **Vietnamese** | vie | Austroasiatic | **Mandatory** (suspected) | SE Asia, 80M+ speakers, *chúng ta* (incl) vs *chúng tôi* (excl) |
| 10 | **Chuukese** | chk | Austronesian | **Mandatory** | Micronesian, full Bible available |

**Alternative candidates**:
- Chamorro (cha) - Micronesian Austronesian
- Chin languages (cek, csy, cth) - Sino-Tibetan, Myanmar
- Enga (enq) - Trans-New Guinea (verify if has clusivity)

---

## 7. Cultural & Social Nuances

### Honorifics Interaction

In some languages, **clusivity interacts with social register**:

**Vietnamese** {medium-clusivity-2025}:
- *ta* (familiar "I") → *chúng ta* (inclusive we)
- *tôi* (formal "I") → *chúng tôi* (exclusive we)
- The formality level of the singular pronoun carries into the plural

**Japanese/Korean**: No clusivity distinction, but **elaborate honorific systems** affect person reference
- Not a clusivity issue, but affects how "we" is expressed

### Theological/Cultural Sensitivity

**The Lord's Prayer Error** {tips-translation-bible-2025}:
- Early missionaries in Kwara'ae used **inclusive "we"** in "Forgive us our trespasses"
- This implied **God shares in human sin** (God + us sinned)
- Had to be corrected to **exclusive "we"** (we humans sinned, not you God)

**Implication**: Getting clusivity wrong can create **heresy**, not just awkwardness.

---

## 8. Typological Classifications for Selected Languages

### Austronesian Languages (Mandatory Clusivity)

**Tagalog** (tgl):
- **Status**: Mandatory
- **Forms**: *tayo* (1PL.INCL) vs *kami* (1PL.EXCL)
- **Number interaction**: Singular *ako* (1SG) → Plural splits into two forms
- **Dual**: Not distinguished (only singular vs plural)

**Malay/Indonesian** (zlm/ind):
- **Status**: Mandatory (but *kami* declining in colloquial use)
- **Forms**: *kita* (1PL.INCL) vs *kami* (1PL.EXCL)
- **Sociolinguistic note**: *kita* increasingly used for both functions in informal speech {medium-clusivity-2025}

**Fijian** (fij):
- **Status**: Mandatory across all plural numbers
- **Number interaction**: Distinguishes singular, dual, trial, plural
- **Forms**: All plural numbers (dual, trial, paucal, plural) distinguish inclusive vs exclusive
- **Example**: Trial inclusive (exactly 3, including you) vs trial exclusive (exactly 3, not including you)

### Australian Languages (Mandatory in Dual)

**Arrernte** (aer):
- **Status**: Mandatory in dual number, extends to plural
- **Forms**:
  - Dual inclusive: *ngali* (we two, including you)
  - Dual exclusive: *ngaliju* (we two, not including you)
- **Typological note**: Dual clusivity is **more common** than plural clusivity in Australian languages {wals-clusivity-2025}

### Sino-Tibetan (Optional/Contextual)

**Mandarin Chinese** (cmn):
- **Status**: Optional (not grammatically required)
- **Forms**:
  - Inclusive: 咱们 *zánmen* (you and I and possibly others)
  - Ambiguous: 我们 *wǒmen* (we - may or may not include addressee)
- **Usage**: *Zánmen* is **explicitly inclusive**, *wǒmen* is **neutral/ambiguous**, NOT strictly exclusive
- **Historical**: Borrowed from Altaic substrate after late Tang dynasty {languagelog-clusivity-2025}

**Chin languages** (cek, csy, cth - Sino-Tibetan, Myanmar):
- **Status**: Mandatory (suspected based on Tibeto-Burman typology)
- **Requires verification** from grammars

### Indo-European (Absent)

**English** (eng):
- **Status**: Absent
- **Form**: *we* is ambiguous (covers both inclusive and exclusive meanings)
- **Semantic options**: Can use *we* (speaker + others) vs *you and I* (explicitly inclusive), but not grammaticalized

**Spanish** (spa):
- **Status**: Absent
- **Form**: *nosotros/nosotras* (we.MASC/we.FEM) - gender-marked but no clusivity

---

## 9. Summary Statistics

From our translation database (~1000 languages):

| Category | Estimated Count | % of Database |
|----------|----------------|---------------|
| **Austronesian** (mandatory clusivity) | ~250-300 | ~25-30% |
| **Australian** (mandatory clusivity) | ~30 | ~3% |
| **Dravidian** (mandatory clusivity) | 0 | 0% |
| **Sino-Tibetan** (optional clusivity) | ~15 | ~1.5% |
| **Indo-European** (absent) | ~50 | ~5% |
| **Trans-New Guinea** (mostly absent) | ~200+ | ~20% |
| **Niger-Congo** (absent) | ~50 | ~5% |
| **Other families** | ~200 | ~20% |

**Estimate**: ~30-35% of languages in our database REQUIRE clusivity marking, aligning with global prevalence of 31.5% {wals-clusivity-2025}.

---

## 10. Gaps & Further Research Needed

1. **Trans-New Guinea family**: Verify clusivity status (200+ languages in database)
2. **Mayan languages**: Check if any mark clusivity (~20 in database)
3. **Dravidian**: No languages in current database - consider adding Tamil/Telugu
4. **Algonquian**: Only 2 languages in database (Algonquin, Blackfoot) - verify clusivity + check for **obviation** (proximate/obviative "fourth person")
5. **Vietnamese**: Verify clusivity status (suspected mandatory based on web research, but no grammar consulted)
6. **Dual vs Plural**: Which languages mark clusivity ONLY in dual vs across all plural numbers?
7. **Trial/Paucal**: How does clusivity interact with trial/paucal numbers in Austronesian?

---

## Bibliography

- {wikipedia-clusivity-2025}: [Wikipedia: Clusivity](https://en.wikipedia.org/wiki/Clusivity)
- {wals-clusivity-2025}: [WALS Online - Chapter 39: Inclusive/Exclusive Distinction](https://wals.info/chapter/39)
- {medium-clusivity-2025}: [The Many Faces of 'We': Inclusive and exclusive pronouns](https://medium.com/language-lab/the-many-faces-of-we-dd41df4879ba)
- {tips-translation-bible-2025}: [TIPs Bible Translation Resources on Clusivity](https://tips.translation.bible/)
- {koine-greek-clusivity-2025}: [The curious case of clusivity marking - Koine-Greek](https://koine-greek.com/2020/03/28/the-curious-case-of-clusivity-marking/)
- {languagelog-clusivity-2025}: [Language Log: Inclusive and exclusive first person plural pronouns in Sinitic](https://languagelog.ldc.upenn.edu/nll/?p=48494)
- `/workspace/src/constants/languages.tsv`: Database of 1008 Bible translations

---

**Document Status**: Complete
**Last Updated**: 2025-11-29
>>>>>>> origin/feat/self-learning-tbta
