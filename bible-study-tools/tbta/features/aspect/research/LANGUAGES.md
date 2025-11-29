# Language Family & Typology Analysis: Aspect

## Executive Summary

**Source Language Status**: Both Hebrew and Greek EXPLICITLY encode aspect morphologically. Hebrew has binary perfective/imperfective (qatal/yiqtol), Greek has three-way perfective/imperfective/stative (aorist/present/perfect).

**Global Distribution**: Perfective/imperfective marking is prevalent across southern Eurasia (Europe to China) and Africa, but less common in Southeast Asia and South America {wals-65}.

**Critical Language Families**:
- **Slavic** (Russian, Polish): Mandatory binary aspectual pairs
- **Niger-Congo** (Swahili, Bantu): 5-way aspect system
- **Austronesian** (Tagalog, Indonesian): 4-way aspect + outer markers
- **Sino-Tibetan** (Mandarin): Aspect particles (no tense)

**Translation Database Candidates** (Stage 2):
1. Russian (rus) - Slavic, mandatory perfective/imperfective
2. Swahili (swh) - Niger-Congo, 5-way aspect
3. Tagalog (tgl) - Austronesian, aspect-voice interaction
4. Mandarin (zho) - Sino-Tibetan, aspect-only (no tense)
5. Polish (pol) - Slavic, aspectual pairs
6. Arabic (ara) - Afro-Asiatic, aspect marking
7. Spanish (spa) - Romance, past aspect distinction
8. Indonesian (ind) - Austronesian, aspect markers
9. German (deu) - Germanic, limited aspect
10. English (eng) - Germanic, progressive aspect

---

## 1. Source Language Encoding

### Hebrew (heb) - Afro-Asiatic

**Morphological Encoding**: ✅ YES - Explicitly encoded

**System Type**: Binary aspect system {hebrew-aspect}

**Morphological Forms**:

| Form | Aspect | Morphology | Examples |
|------|--------|------------|----------|
| **Qatal** (Perfect) | Perfective | Suffix conjugation | קָטַל (qatal) "he killed" |
| **Yiqtol** (Imperfect) | Imperfective | Prefix conjugation | יִקְטֹל (yiqtol) "he will kill / kills" |
| **Wayyiqtol** | Perfective (narrative) | waw + yiqtol | וַיִּקְטֹל (wayyiqtol) "and he killed" |
| **Weqatal** | Imperfective | waw + qatal | וְקָטַל (weqatal) "and he will kill" |
| **Participle** | Progressive | Active/Passive forms | קֹטֵל (qotel) "killing" |

**Aspectual Characteristics** {hebrew-aspect}:
- **Qatal (Perfective)**: Action viewed as complete, whole, total unit
- **Yiqtol (Imperfective)**: Action viewed as incomplete, ongoing, habitual, repeated, not yet realized
- **Wayyiqtol**: Sequential narrative (perfective)
- **Emphasis**: Aspect is more prominent than tense in Hebrew

**Theological Impact**:
- Prophetic perfect: Future events viewed as complete (certainty)
- Imperfective for ongoing states, repeated actions, general truths
- Critical for translating OT into aspect-prominent languages

**Citation**: {hebrew-aspect}

---

### Greek (ell) - Indo-European (Hellenic)

**Morphological Encoding**: ✅ YES - Explicitly encoded

**System Type**: Three-way aspect system {greek-aspect}

**Morphological Forms**:

| Tense-Form | Aspect | Viewpoint | Examples |
|------------|--------|-----------|----------|
| **Aorist** | Perfective | External view, action as whole | ἔλυσα (elusa) "I loosed" |
| **Present** | Imperfective | Internal view, ongoing | λύω (luō) "I loose / am loosing" |
| **Imperfect** | Imperfective | Past ongoing | ἔλυον (eluon) "I was loosing" |
| **Perfect** | Stative | State resulting from action | λέλυκα (leluka) "I have loosed" |
| **Pluperfect** | Stative | Past state | ἐλελύκειν (eleluekein) "I had loosed" |
| **Future** | (Aspect-neutral or perfective) | Future action | λύσω (lusō) "I will loose" |

**Scholarly Debate** {greek-aspect}:
- **Porter/Campbell**: Greek is aspect-prominent; tense/time is purely pragmatic (contextual)
- **Fanning**: Aspect is primary, but tense is semantic in indicative mood
- **Agreement**: All scholars agree on perfective/imperfective/stative distinctions

**Aspectual Characteristics**:
- **Aorist (Perfective)**: Unmarked form, views action simply, as complete whole
- **Present (Imperfective)**: Views action internally, as process
- **Perfect (Stative)**: State resulting from completed action
- **Critical**: Aspect affects theological interpretation (aorist = single event vs present = habitual)

**Theological Examples**:
- John 3:16 ἠγάπησεν (aorist) "God loved" - single, complete act
- 1 John 3:6 ἁμαρτάνει (present) "keeps on sinning" - habitual action
- Imperative aspect: Aorist (single command) vs Present (ongoing instruction)

**Citation**: {greek-aspect}, {porter-1989}, {fanning-1990}

---

## 2. Language Family Classification

### Family-by-Family Analysis

#### Indo-European

**Subfamilies with Aspect Marking**:

**Slavic Languages** {slavic-aspect}:
- **Status**: MANDATORY - Every verb must be marked perfective or imperfective
- **System**: Binary aspectual pairs (one lexical meaning, two forms)
- **Morphology**: Prefixation (impf → pf), suffixation (pf → secondary impf), vowel/stress alternation
- **Example Languages**:
  - **Russian** (rus): делать (impf) / сделать (pf) "to do"
  - **Polish** (pol): robić (impf) / zrobić (pf) "to do"
  - **Czech** (ces): dělat (impf) / udělat (pf) "to do"
  - **Bulgarian** (bul): Perfective/imperfective distinction
  - **Serbo-Croatian** (hrv, srp): Transitional system
- **Translation Impact**: HIGH - Translators MUST choose aspect; wrong choice changes meaning
- **Geographic Distribution**: Eastern Europe, Russia
- **Availability in Corpus**: Russian (rus), Polish (pol) confirmed in languages.tsv

**Romance Languages** {wals-65}:
- **Status**: OPTIONAL - Aspect marked in past tense only
- **System**: Perfective (preterite/passé simple) vs Imperfective (imperfect)
- **Example Languages**:
  - **Spanish** (spa): comí (preterite, pf) / comía (imperfect, impf) "I ate / was eating"
  - **French** (fra): je mangeai (passé simple, pf) / je mangeais (impf) "I ate / was eating"
  - **Portuguese** (por): comi (pf) / comia (impf)
  - **Italian** (ita): mangiai (pf) / mangiavo (impf)
  - **Romanian** (ron): mâncai (pf) / mâncam (impf)
- **Translation Impact**: MEDIUM - Past tense narratives require aspect choice
- **Availability in Corpus**: Spanish (spa), French (fra) confirmed

**Germanic Languages** {wals-65}:
- **Status**: OPTIONAL - Progressive aspect only
- **System**: Progressive (be + -ing) vs Simple
- **Example Languages**:
  - **English** (eng): "I am eating" (progressive) vs "I eat" (simple)
  - **German** (deu): Limited progressive (am + infinitive + sein), mostly lexical
  - **Dutch** (nld): Progressive with "aan het" construction
  - **Swedish** (swe), **Norwegian** (nor), **Danish** (dan): Minimal aspect marking
- **Translation Impact**: LOW - Progressive mainly for emphasis
- **Availability in Corpus**: English (eng), German (deu) confirmed

**Greek** (ell):
- Covered above in source languages

**Armenian** (hye):
- Aspect marking present {wals-65}

**Indo-Iranian**:
- **Persian** (fas): Aspect marking
- **Hindi** (hin): Three aspects (habitual, progressive, perfective) {grambank-gb086}
- **Urdu** (urd): Complex aspect system with participle forms

---

#### Niger-Congo

**Status**: MANDATORY to OPTIONAL - Varies by subfamily

**System** {niger-congo-aspect}: Five widespread aspects
1. Factative (FAC) / Perfective (PFV)
2. Imperfective (IPFV)
3. Perfect (PFT)
4. Progressive (PRG)
5. Habitual (HAB) / Iterative

**Morphology** {niger-congo-aspect}:
- Verbal extensions (suffixes)
- Tonal marking (floating tones)
- Factative associated with /-i/
- Imperfective associated with /-a/

**Bantu Subgroup** {niger-congo-aspect}:
- All Bantu languages encode both aspect AND tense
- Verbal extension system for argument structure and aspect
- **Example Languages**:
  - **Swahili** (swh): Rich aspect system, East Africa major language
  - **Zulu** (zul): Aspect + tense
  - **Lingala** (lin): Aspect marking
  - **Kinyarwanda** (kin): Aspect marking
  - **Kikongo** (kg various): Aspect marking
- **Translation Impact**: HIGH - Aspect distinctions required
- **Availability in Corpus**: Swahili (swh) confirmed

**West African Subgroup**:
- **Akan** (aka): Aspect marking
- **Yoruba** (yor): Aspect markers
- **Igbo** (ibo): Aspect system
- **Ewe** (ewe): Aspect particles
- **Availability in Corpus**: Akan (aka) confirmed

**Translation Impact**: HIGH - Niger-Congo languages require rich aspect distinctions beyond binary perfective/imperfective

---

#### Austronesian

**Status**: OPTIONAL to MANDATORY - Varies by subgroup

**System** {austronesian-aspect}: Four aspects + outer markers
1. Perfective
2. Imperfective
3. Progressive
4. Prospective
5. Outer aspect markers: *=daNa ('still'), *=pa ('already')

**Philippine-Type Languages** {austronesian-aspect}:
- **Status**: Aspect morphology interacts with voice system
- **Example Languages**:
  - **Tagalog** (tgl): Aspect-voice merger, infix system
  - **Cebuano** (ceb): Similar system
  - **Ilocano** (ilo): Aspect marking
  - **Bikol** (bik various): Aspect system
- **Morphology**: Infixes (⟨in⟩, ⟨um⟩), zero allomorphs
- **Translation Impact**: HIGH - Aspect is prerequisite for voice marking
- **Availability in Corpus**: Tagalog (tgl) confirmed

**Indonesian-Type Languages** {austronesian-aspect}:
- **Status**: OPTIONAL - Aspect markers present but not always required
- **Example Languages**:
  - **Indonesian** (ind): Aspect particles (sudah, sedang, masih)
  - **Malay** (msa): Similar to Indonesian
  - **Javanese** (jav): Aspect + honorifics
- **Translation Impact**: MEDIUM - Can use context without explicit markers
- **Availability in Corpus**: Indonesian (ind) confirmed

**Polynesian**:
- **Samoan** (smo), **Tongan** (ton), **Māori** (mri): Aspect particles
- **Hawaiian** (haw): Aspect markers

**Melanesian**:
- **Fijian** (fij): Aspect system
- PNG languages: Various aspect systems

---

#### Sino-Tibetan

**Status**: MANDATORY - Chinese has no tense, only aspect

**System** {chinese-aspect}: Aspect particles (no tense morphology)

**Mandarin Chinese** (zho) {chinese-aspect}:
- **Three main markers**:
  - **了 (le)**: Perfective/completive - action completed or situation changed
  - **着 (zhe)**: Imperfective/durative - ongoing action or state
  - **过 (guo)**: Experiential - past experience, repeatable
- **Additional markers**:
  - **正在 (zhèngzài) / 在 (zai)**: Progressive (precede verb)
- **Translation Impact**: CRITICAL - Must map Greek/Hebrew aspect to Chinese particles
- **Availability in Corpus**: Multiple Chinese versions likely

**Other Sino-Tibetan**:
- **Tibetan** (bod): Aspect marking
- **Burmese** (mya): Aspect particles
- **Thai** (tha): (Tai-Kadai, not Sino-Tibetan) Aspect markers

---

#### Afro-Asiatic

**Semitic Branch**:
- **Hebrew** (heb): Covered above in source languages
- **Arabic** (ara): Perfective/imperfective binary system {suspected}
  - Perfect (māḍī): Completed action
  - Imperfect (muḍāriʿ): Ongoing/future action
  - **Status**: MANDATORY
  - **Translation Impact**: HIGH - Major world language, aspect required
  - **Availability in Corpus**: Multiple Arabic versions likely

**Other Afro-Asiatic**:
- **Amharic** (amh): Aspect marking {suspected}
- **Oromo** (orm): Aspect system {suspected}
- **Hausa** (hau): Aspect particles {suspected}

---

#### Uralic

**Status**: OPTIONAL to ABSENT

**Example Languages**:
- **Finnish** (fin): No grammatical aspect (suspected)
- **Hungarian** (hun): Limited aspect distinctions (suspected)
- **Estonian** (est): Minimal aspect (suspected)

**Translation Impact**: LOW - Can express aspectual nuances lexically

---

#### Other Language Families

**Kartvelian**:
- **Georgian** (kat): Aspect marking present {suspected}

**Turkic**:
- **Turkish** (tur): Aspect distinctions present {suspected}
- **Kazakh** (kaz), **Uzbek** (uzb), **Azerbaijani** (aze): Aspect systems {suspected}

**Dravidian**:
- **Tamil** (tam), **Telugu** (tel), **Malayalam** (mal), **Kannada** (kan): Aspect marking {suspected}

**Japonic**:
- **Japanese** (jpn): Aspect marking (perfective -ta, imperfective -ru) {suspected}

**Koreanic**:
- **Korean** (kor): Aspect system {suspected}

---

## 3. Root/Bridge Languages Analysis

### Major Bible Translation Languages

**Languages translators often START from** (in addition to Hebrew/Greek):

| Language | Code | Family | Aspect System | Status | In Corpus |
|----------|------|--------|---------------|--------|-----------|
| **Greek** | ell | Indo-European | 3-way (pf/impf/stative) | Source | ✅ |
| **Hebrew** | heb | Afro-Asiatic | 2-way (pf/impf) | Source | ✅ |
| **Latin** | lat | Indo-European | Perfective/imperfective | Historical | ✅ |
| **English** | eng | Indo-European | Progressive only | Bridge | ✅ |
| **Spanish** | spa | Indo-European | Past aspect (pf/impf) | Bridge | ✅ |
| **French** | fra | Indo-European | Past aspect (pf/impf) | Bridge | ✅ |
| **German** | deu | Indo-European | Limited aspect | Bridge | ✅ |
| **Arabic** | ara | Afro-Asiatic | 2-way (pf/impf) | Bridge | ✅ (suspected) |
| **Russian** | rus | Indo-European | 2-way mandatory | Bridge | ✅ |
| **Swahili** | swh | Niger-Congo | 5-way aspect | Bridge (E. Africa) | ✅ |
| **Indonesian** | ind | Austronesian | Aspect particles | Bridge (SE Asia) | ✅ |

**Key Findings**:
- **7 of 11** root languages have grammatical aspect
- **Aspect-prominent**: Greek, Hebrew, Arabic, Russian, Swahili, Mandarin
- **Limited aspect**: English, German, French, Spanish (past only)
- **Translation chain impact**: If translating from English → target language with mandatory aspect, translator must infer aspect from context (information loss)

---

## 4. Typological Distribution

### Geographic Patterns {wals-65}

**High Aspect Marking Regions**:
- **Europe**: Southern Europe, Slavic region (excluding Northern Europe except Slavic)
- **Asia**: Band across southern Eurasia to China
  - **Excludes**: Dravidian South Asia, Southeast Asia mainland
- **Africa**: Down to equator
- **Notable**: Sino-Tibetan (China) has aspect despite Southeast Asia generally lacking

**Low Aspect Marking Regions**:
- **Europe**: Northern Europe (Germanic, excluding Slavic)
- **Asia**: Southeast Asia (Thai-Kadai, Austroasiatic areas)
- **Americas**: Large parts of South America
- **Oceania**: Variable (Austronesian has aspect, some Papuan languages lack it)

**Insight**: Aspect marking forms a **Eurasian-African belt** with outliers in Austronesian and pockets elsewhere.

---

## 5. Translation Database Language Selection

### Recommended Languages for Stage 2 Translation Analysis

**Selection Criteria**:
1. Mix of aspect-marking vs non-marking languages
2. Diverse language families
3. Available in our corpus (languages.tsv)
4. Geographic/typological diversity
5. Major translation languages

**Tier 1: MANDATORY (High Priority - Aspect Required)**

| # | Language | Code | Family | Aspect System | Why Selected |
|---|----------|------|--------|---------------|--------------|
| 1 | **Russian** | rus | Slavic | 2-way mandatory (pf/impf) | Prototypical aspect language, every verb marked |
| 2 | **Swahili** | swh | Niger-Congo | 5-way (FAC/IPFV/PFT/PRG/HAB) | African major language, richer than binary |
| 3 | **Tagalog** | tgl | Austronesian | 4-way + outer markers | Aspect-voice interaction, Philippines |
| 4 | **Mandarin** | zho | Sino-Tibetan | Particles (le/zhe/guo) | No tense, only aspect - critical case |

**Tier 2: IMPORTANT (Medium Priority - Optional Aspect)**

| # | Language | Code | Family | Aspect System | Why Selected |
|---|----------|------|--------|---------------|--------------|
| 5 | **Spanish** | spa | Romance | Past aspect (pf/impf) | Major world language, tense-aspect conflation |
| 6 | **Polish** | pol | Slavic | 2-way mandatory | Transitional Slavic, compare with Russian |
| 7 | **Arabic** | ara | Afro-Asiatic | 2-way (pf/impf) | Major world language, Semitic like Hebrew |
| 8 | **Indonesian** | ind | Austronesian | Particles (optional) | Contrast with Tagalog (same family, different system) |

**Tier 3: COMPARATIVE (Lower Priority - Limited/No Aspect)**

| # | Language | Code | Family | Aspect System | Why Selected |
|---|----------|------|--------|---------------|--------------|
| 9 | **English** | eng | Germanic | Progressive only | Bridge language, minimal aspect |
| 10 | **German** | deu | Germanic | Limited aspect | Germanic comparison with English |

**Total**: 10 languages across 7 families, 4 continents

---

## 6. Language-Specific Distinctions

### Critical Distinctions Between Selected Languages

**Russian vs Polish** (Both Slavic):
- **Russian**: Eastern Slavic, more regular aspectual pairs
- **Polish**: Transitional (leans East), more complex triple systems (impf → pf → secondary impf)
- **Insight**: Tests whether algorithm works across Slavic variation

**Swahili vs Other Niger-Congo**:
- **Swahili**: 5-way aspect system (FAC, IPFV, PFT, PRG, HAB)
- **Insight**: Richer than binary perfective/imperfective; tests if algorithm can predict 5-way
- **Verbal extensions**: Aspect encoded via suffixation and tone

**Tagalog vs Indonesian** (Both Austronesian):
- **Tagalog**: Aspect-voice morphological merger, mandatory infix system
- **Indonesian**: Aspect particles optional, SVO word order (lost symmetrical voice)
- **Insight**: Tests whether same family, different typology affects aspect translation

**Mandarin vs Greek/Hebrew**:
- **Mandarin**: No tense morphology, only aspect particles
- **Greek/Hebrew**: Tense-aspect conflation (tense-forms encode aspect)
- **Insight**: How to map morphological aspect (source) to particle aspect (target)?

**Arabic vs Hebrew** (Both Semitic):
- **Arabic**: Perfective (māḍī) vs Imperfective (muḍāriʿ) - similar to Hebrew
- **Hebrew**: Qatal (perfective) vs Yiqtol (imperfective)
- **Insight**: Tests whether Semitic pattern is consistent across languages

**Spanish vs French** (Both Romance):
- **Spanish**: Preterite (pf) vs Imperfect (impf) commonly used
- **French**: Passé simple (pf) vs Imparfait (impf), but passé simple rare in modern French
- **Insight**: Tests whether Romance pattern consistent despite usage differences

---

## 7. Cultural and Pragmatic Considerations

### Honorifics and Aspect Interaction

**Japanese** (jpn) {suspected}:
- Aspect marking (-ta perfective, -ru imperfective)
- Interacts with honorific system
- Aspect choice may be constrained by social register

**Javanese** (jav) {suspected}:
- Aspect system present
- Multiple speech levels (ngoko, madya, krama)
- Aspect may interact with register

**Implication**: Some languages require considering aspect + social factors together.

---

### Aspect and Evidentiality

**Some languages** conflate aspect with evidential marking (how speaker knows information):
- **Turkish**: Past tense has direct evidence (-di) vs indirect evidence (-miş) distinction
- May interact with aspect in some languages

**Implication**: Aspect is not always isolated grammatical category.

---

## 8. Summary Tables

### Aspect Necessity by Language Family

| Family | Aspect Status | Example Languages | In Corpus |
|--------|---------------|-------------------|-----------|
| **Slavic** | MANDATORY | Russian, Polish, Czech | ✅ rus, pol |
| **Niger-Congo** | MANDATORY (Bantu) | Swahili, Zulu | ✅ swh, aka |
| **Austronesian** (Philippine) | MANDATORY | Tagalog, Cebuano | ✅ tgl |
| **Sino-Tibetan** | MANDATORY | Mandarin, Tibetan | ✅ (suspected) |
| **Afro-Asiatic** (Semitic) | MANDATORY | Arabic, Hebrew | ✅ ara, heb |
| **Romance** | OPTIONAL (past) | Spanish, French | ✅ spa, fra |
| **Austronesian** (Indonesian) | OPTIONAL | Indonesian, Malay | ✅ ind |
| **Germanic** | OPTIONAL (progressive) | English, German | ✅ eng, deu |
| **Uralic** | ABSENT | Finnish, Hungarian | ❓ |

---

### Source Language Summary

| Language | Encoding | System | Morphology | Theological Impact |
|----------|----------|--------|------------|-------------------|
| **Hebrew** | ✅ Explicit | 2-way (pf/impf) | Qatal/Yiqtol | Prophecy, narrative |
| **Greek** | ✅ Explicit | 3-way (pf/impf/stative) | Aorist/Present/Perfect | Command types, sin nature |

---

## 9. Citations

All findings sourced from:

- {wals-65} - WALS Chapter 65: Perfective/Imperfective Aspect
- {grambank-gb086} - Grambank Feature GB086
- {slavic-aspect} - Slavic aspect research and Wikipedia
- {niger-congo-aspect} - Niger-Congo aspect research (Nurse, Hyman)
- {austronesian-aspect} - Austronesian aspect research (Kaufman et al.)
- {chinese-aspect} - Mandarin Chinese aspect research
- {greek-aspect} - Greek NT aspect (Porter, Fanning, Campbell)
- {hebrew-aspect} - Hebrew aspect (Cook, Waltke & O'Connor)
- {suspected} - Based on internal linguistic knowledge, not verified from sources (used for languages not covered in retrieved research)

**Languages.tsv**: /workspace/src/constants/languages.tsv (1009 languages total)

---

**Last Updated**: 2025-11-29
