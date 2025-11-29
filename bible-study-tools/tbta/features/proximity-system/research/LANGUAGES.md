# Language Family & Typology Analysis: Proximity System

## Critical Finding: Source Language Encoding

**Hebrew**: 2-way system - זֶה (zeh - this, near) vs. הַהוּא (hahu - that, far)
**Greek**: 2-3 way system - οὗτος (houtos - this, near) vs. ἐκεῖνος (ekeinos - that, far) vs. ὅδε (hode - this here, proximal)
**Koine Greek**: Typically 2-way - οὗτος (near) / ἐκεῖνος (far)

**Conclusion**: Proximity is **PARTIALLY** encoded in Hebrew/Greek morphology (basic near/far distinction), but TBTA's 10-value system **EXTENDS BEYOND** source language morphology to include:
- Finer spatial distinctions (near speaker/listener/both vs. remote visible/invisible)
- Temporal proximity (near/remote time)
- Discourse proximity (contextual/anaphoric reference)
- Visibility distinctions

**Implication**: Proximity values require **CONTEXTUAL INFERENCE** from narrative, not just morphological copying from source text.

## Required Language Families

Based on {wals-41-distance}, {grambank-database}, {diessel-1999-demonstratives}, and linguistic literature, the following families **grammatically require** proximity marking:

### 1. Austronesian (1,200+ languages)

**System Type**: Predominantly person-oriented 3-way systems

**Examples**:
- **Tagalog** (Philippines, 11M speakers): ito (near speaker) / iyan (near listener) / iyon (remote)
- **Malay/Indonesian** (Indonesia, 43M speakers): ini (near) / itu (far) - 2-way (simplified)
- **Fijian**: 4-way system with visibility distinctions
- **Many Polynesian**: 3-way person-oriented

**Necessity**: **MANDATORY** - Demonstratives grammatically required, distance distinctions obligatory

**TBTA Coverage**: Indonesian (ind) present in translation database

---

### 2. Japonic (2 languages: Japanese, Ryukyuan)

**System Type**: Person-oriented 3-way

**Japanese** (jpn, 125M speakers):
- これ (kore): Near speaker
- それ (sore): Near listener/addressee
- あれ (are): Remote from both participants

**Adnominal Forms**: kono / sono / ano (attributive)

**Necessity**: **MANDATORY** - Cannot omit demonstrative distance; ungrammatical to use wrong distance marker

**TBTA Coverage**: Japanese (jpn) present in translation database

---

### 3. Koreanic (Korean)

**System Type**: Person-oriented 3-way (similar to Japanese)

**Korean** (kor, 81M speakers):
- 이 (i): Proximal (near speaker)
- 그 (ku): Medial (near addressee OR anaphoric/discourse reference)
- 저 (ce): Distal (away from both)

**Directional Forms**: i-li / ku-li / ce-li (toward speaker / toward listener / away from both)

**Special Feature**: **그** (ku) dual function - spatial + discourse anaphoric

**Necessity**: **MANDATORY**

**TBTA Coverage**: Not present in current database (opportunity to add)

---

### 4. Trans-New Guinea (300+ languages, Papua New Guinea)

**System Type**: Highly variable; many complex multi-dimensional systems

**Examples from Translation Database**:
- Ankave (aak), Awa (awb), Benabena (bef), Kaluli (bco) - Various systems
- Elevation and visibility distinctions common

**Necessity**: **MANDATORY** in most languages; complex systems with 3-5+ distinctions

**TBTA Coverage**: 100+ Trans-New Guinea languages in database

---

### 5. Sino-Tibetan (450+ languages)

**System Type**: Variable

**Mandarin Chinese** (cmn, 918M speakers):
- 这/這 (zhè): Proximal (this)
- 那 (nà): Distal (that)
- 2-way distance-oriented system

**Necessity**: **MANDATORY** - Must mark demonstrative distance

**TBTA Coverage**: Mandarin (cmn) present in database

---

### 6. Indo-European: Romance, Slavic, Indo-Aryan

**Romance Languages** (Spanish, French, Portuguese, Italian):
- **Spanish** (spa, 548M speakers): 3-way person-oriented
  - este (near speaker)
  - ese (near listener / moderate distance)
  - aquel (remote from both) - declining in modern use
- **French** (fra, 280M speakers): 2-way
  - ce/cet/cette (proximal - this)
  - celui/celle (distal - that)
- **Portuguese** (por, 264M speakers): 2-way to 3-way

**Necessity**: **MANDATORY**

**TBTA Coverage**: Spanish (spa), French (fra), Portuguese (por) all present

**Slavic Languages** (Russian, etc.):
- **Russian** (rus, 258M speakers): Demonstratives with case declension
  - этот (etot - this)
  - тот (tot - that)
- 2-way systems typical

**Necessity**: **MANDATORY**

**Indo-Aryan** (Hindi, Bengali, Tamil, Telugu):
- **Hindi** (hin, 602M speakers): 3-way
  - yah (near speaker)
  - vah (near listener)
  - vo (remote)
- **Tamil** (tam, 79M speakers): 3-way with multiple registers
- **Telugu** (tel, 83M speakers): 3-way

**Necessity**: **MANDATORY**

**TBTA Coverage**: Hindi (hin), Tamil (tam), Telugu (tel) present

---

### 7. Niger-Congo: Bantu

**Bantu Subfamily** (500+ languages, 300M speakers):
- **Swahili** (swh, 200M speakers): Demonstrative system integrated with noun class
  - huyu/hawa (near - class 1/2)
  - huyo/hao (medial - class 1/2)
  - yule/wale (distal - class 1/2)
  - Complex agreement with 15+ noun classes

**Necessity**: **MANDATORY** - Locative constructions very prominent {nurse-philippson-2003-bantu}

**TBTA Coverage**: Swahili (swh) present

---

### 8. Mayan (31 languages, Central America)

**System Type**: Variable; often 2-3 way

**Examples in Database**:
- Achi (acr), Kaqchikel, K'iche', Mam, Q'eqchi'

**Necessity**: **MANDATORY**

**TBTA Coverage**: Multiple Mayan languages present (acr, agu, etc.)

---

### 9. Uto-Aztecan (61 languages, North/Central America)

**System Type**: Variable

**Nahuatl** (azz, multiple dialects): 2-3 way systems typical

**Necessity**: **MANDATORY**

**TBTA Coverage**: Nahuatl (azz) present

---

### 10. Afro-Asiatic (Arabic, Amharic, etc.)

**Arabic** (arb, 310M speakers):
- Modern Standard Arabic: 2-way
  - هَذَا (hāḏā - this)
  - ذَلِكَ (ḏālika - that)
- Dialectal variation extensive

**Necessity**: **MANDATORY**

**TBTA Coverage**: Arabic (arb) present

---

## Language Classification by Proximity Requirements

### Analysis of Available Translations (from /workspace/src/constants/languages.tsv)

**Total Languages in Database**: 1,008 languages

**Classification Criteria**:
- **Mandatory**: Language MUST mark demonstrative distance (no grammatical alternative)
- **Optional**: Language CAN mark distance but has alternatives (articles, zero marking)

**Distribution by Family** (Major families with 10+ language varieties in database):

| Family | Count | Proximity Status | Typical System |
|--------|-------|------------------|----------------|
| Austronesian | 280+ | Mandatory | 2-3 way, person-oriented |
| Trans-New Guinea | 180+ | Mandatory | 2-5+ way, often elevation/visibility |
| Niger-Congo | 80+ | Mandatory (Bantu) | 3-way with noun class agreement |
| Indo-European | 50+ | Mandatory | 2-3 way (Romance 3-way, Germanic 2-way, Slavic 2-way, Indo-Aryan 3-way) |
| Sino-Tibetan | 35+ | Mandatory | 2-way (Mandarin), variable in Tibeto-Burman |
| Otomanguean | 70+ | Mandatory | 2-3 way typical (Zapotec languages) |
| Mayan | 15+ | Mandatory | 2-3 way |
| Creole | 20+ | Variable | Often 2-way (derived from source language) |
| Australian | 30+ | Mandatory | Variable, some with elevation |
| Sepik | 25+ | Mandatory | Variable |

**Estimated Mandatory Marking**: ~95% of languages in TBTA database (960+ languages)

**Estimated Optional**: ~5% (Germanic languages, some creoles) - though even these typically prefer demonstratives

---

## Root Translation Languages (Priority for Algorithm Training)

**Definition**: Languages translators often start with (besides Hebrew/Greek) due to existing quality translations, regional lingua franca status, or parent language relationships.

### Primary Root Languages (All in TBTA Database)

1. **English** (eng) - 2-way distance-oriented [this/that] - **MANDATORY marking**
2. **Spanish** (spa) - 3-way person-oriented [este/ese/aquel] - **MANDATORY**
3. **French** (fra) - 2-way distance-oriented [ce/celui] - **MANDATORY**
4. **Portuguese** (por) - 2-3 way [este/esse/aquele] - **MANDATORY**
5. **German** (deu) - Minimal adnominal contrast (dieser/jener), relies on adverbs - **OPTIONAL** (can use articles)
6. **Russian** (rus) - 2-way [этот/тот] - **MANDATORY**
7. **Arabic** (arb) - 2-way [هَذَا/ذَلِكَ] - **MANDATORY**
8. **Mandarin Chinese** (cmn) - 2-way [这/那] - **MANDATORY**
9. **Indonesian/Malay** (ind/zlm) - 2-way [ini/itu] - **MANDATORY**
10. **Swahili** (swh) - 3-way with noun class [huyu/huyo/yule] - **MANDATORY**
11. **Hindi** (hin) - 3-way [yah/vah/vo] - **MANDATORY**
12. **Tamil** (tam) - 3-way [itu/atu/atu] - **MANDATORY**
13. **Japanese** (jpn) - 3-way person-oriented [kore/sore/are] - **MANDATORY**

### Secondary Root Languages (Regional)

14. **Tagalog** (Philippines) - 3-way person-oriented - **NOT in database** (opportunity)
15. **Korean** (East Asia) - 3-way person-oriented - **NOT in database** (opportunity)
16. **Amharic** (Ethiopia) - 2-way - Not in database
17. **Thai** (Southeast Asia) - Variable - Not in database

---

## Candidate Languages for Translation Database (Stage 2)

**Criteria**: Diverse families, mix of 2-way/3-way/4+ way systems, present in available translations

### Recommended 10 Languages (All Available in Database)

| # | Language | ISO 639-3 | Family | System Type | Rationale |
|---|----------|-----------|--------|-------------|-----------|
| 1 | **English** | eng | Indo-European (Germanic) | 2-way distance | Baseline, most common source |
| 2 | **Spanish** | spa | Indo-European (Romance) | 3-way person | Person-oriented contrast |
| 3 | **Japanese** | jpn | Japonic | 3-way person | Prototypical person-oriented |
| 4 | **Mandarin** | cmn | Sino-Tibetan | 2-way distance | Largest L1 population |
| 5 | **Swahili** | swh | Niger-Congo (Bantu) | 3-way + noun class | Locative prominence, African context |
| 6 | **Indonesian** | ind | Austronesian | 2-way (simplified) | Major Austronesian representative |
| 7 | **Hindi** | hin | Indo-European (Indo-Aryan) | 3-way person | South Asian context |
| 8 | **Russian** | rus | Indo-European (Slavic) | 2-way distance | Slavic representative, case system |
| 9 | **Arabic** | arb | Afro-Asiatic | 2-way distance | Semitic (related to Hebrew) |
| 10 | **Kaluli** | bco | Trans-New Guinea | Complex multi-dimensional | Papua New Guinea complexity |

**Alternative Candidates** (if above unavailable):
- **Portuguese** (por) - Romance 2-3 way
- **French** (fra) - Romance 2-way
- **Tamil** (tam) - Dravidian 3-way
- **Tagalog** (tgl) - If available, ideal Austronesian person-oriented representative

---

## Unique Cross-Linguistic Needs

### 1. Person-Oriented vs. Distance-Oriented (Key Distinction)

**Distance-Oriented Languages** (Majority):
- Encode distance from deictic center (speaker typically)
- Examples: English (this/that), Mandarin (这/那), Russian (этот/тот)
- **TBTA Mapping**:
  - Proximal → S (Near Speaker) or N (Near Both)
  - Distal → R (Remote Visible) or r (Remote out of Sight)

**Person-Oriented Languages** (Common in Asia, Pacific):
- Encode location relative to speaker AND addressee
- Examples: Japanese (kore/sore/are), Korean (i/ku/ce), Spanish (este/ese/aquel), Tagalog (ito/iyan/iyon)
- **TBTA Mapping**:
  - Near speaker → S
  - Near addressee → L
  - Remote from both → R or r

**Translation Challenge**: English "that" is ambiguous - could mean "near you" (L) or "far from both" (R). TBTA disambiguation critical for person-oriented target languages.

---

### 2. Visibility Distinctions

**Languages with Visibility Encoding**:
- **Yupik** (Central Alaskan): Visible vs. invisible categories {miyaoka-2012-yupik}
- **Malagasy** (Austronesian): Special deictics for hidden objects
- **Muna** (Austronesian, Sulawesi): Three dimensions - distance, height, visibility

**TBTA Values**: R (Remote within Sight) vs. r (Remote out of Sight)

**Challenge**: Hebrew/Greek do not morphologically mark visibility - contextual inference required

---

### 3. Elevation/Verticality Systems

**Languages with Elevation Marking**:
- **Yupik**: UP / DOWN / LEVEL / ACROSS {miyaoka-2012-yupik}
- **Some Australian languages**: Uphill/downhill distinctions
- **Some Austronesian**: Height relative to speaker

**TBTA Gap**: No specific elevation values (would need expansion beyond 10 values)

**Workaround**: Use spatial values (S/L/R) + context notes for elevation-critical verses

---

### 4. Temporal vs. Spatial Demonstratives

**All Languages Studied**: Can extend spatial demonstratives to temporal domain

**English Examples**:
- Spatial: "this book" (near) / "that book" (far)
- Temporal: "this week" (recent) / "that ancient time" (remote)

**TBTA Values**: T (Temporally Near) vs. t (Temporally Remote)

**Cross-Linguistic Pattern**: {piwek-2007-proximal-distal} Proximal demonstratives preferred in scientific/expository text; distal in spoken interaction

**Biblical Application**:
- **Genesis 1:1 "In the beginning"**: Temporally Remote (t)
- **Hebrews 1:2 "in these last days"**: Temporally Near (T)
- **Romans 3:26 "at the present time"**: Temporally Near (T)

---

### 5. Discourse/Anaphoric Demonstratives

**All Languages**: Can use demonstratives for discourse reference (textual, not physical)

**Halliday & Hasan Classification** {halliday-hasan-1976-cohesion}:
- **Exophoric**: Physical world reference (spatial/temporal)
- **Endophoric**: Textual reference (anaphoric/cataphoric)

**TBTA Values**: C (Contextually Near with Focus) vs. c (Contextually Near)

**Genre Variation** {piwek-2007-proximal-distal}:
- **Epistles/Expository**: High frequency of proximal anaphoric demonstratives
- **Narrative/Spoken**: Higher frequency of distal anaphoric

**Biblical Application**:
- **Romans 8:1**: "There is therefore now no condemnation for **those** who are in Christ" - Anaphoric demonstrative (c or C)
- **1 Cor 15:1**: "the gospel I preached to you" - Anaphoric (c)

---

### 6. Noun Class Agreement (Bantu)

**Bantu Languages** (Swahili, Kinyarwanda, Zulu, etc.): Demonstratives agree with noun class

**Swahili Example** (15 noun classes):
- Class 1 (m-/mw- singular): **huyu** (near), **huyo** (medial), **yule** (distal)
- Class 2 (wa- plural): **hawa** (near), **hao** (medial), **wale** (distal)
- Class 5 (ji-/Ø- singular): **hili** (near), **hilo** (medial), **lile** (distal)

**TBTA Treatment**: Proximity value (S/L/R) independent of noun class - target language applies appropriate agreement morphology

---

### 7. Minimal Demonstrative Languages (Germanic Example)

**German**: Adnominal demonstratives limited (dieser/jener), **prefers adverbs** (hier/da) for spatial contrast

**TBTA Implication**: Even "optional" marking languages typically render proximity - TBTA values guide choice between:
- Definite article: *der Mann* (the man - no distance)
- Demonstrative: *dieser Mann* (this man - near)
- Adverbial: *der Mann hier* (the man here - proximal spatial)

---

## Cultural and Social Nuances

### Honorifics and Register (Not Proximity per se, but related)

**Japanese, Korean, Javanese**: Demonstrative choice can interact with social register

**Example**: Japanese *kochira* (polite equivalent of *kore*) used in formal contexts

**TBTA Separation**: Handled by separate "Speaker Demographics" feature (Age, Relationship, Attitude), not Proximity

---

### Taboos and Pointing

**Some cultures**: Direct pointing (and thus exophoric demonstratives) restricted

**Implication**: Prefer endophoric/discourse demonstratives (C/c) over spatial (S/L/R) in sensitive contexts

**Biblical Consideration**: Generally not applicable - Biblical texts assume direct reference to narrative participants/objects

---

## Summary: Key Typological Insights for Algorithm Design

### 1. Universal Presence, Variable Complexity

- **All natural languages** have demonstratives {diessel-1999-demonstratives}
- **54% use 2-way** systems (proximal/distal) {wals-41-distance}
- **38% use 3-way** systems (with person vs. distance orientation split)
- **8% use 4+ way** systems (rare, specialized)

### 2. Source Languages Underspecify

- Hebrew/Greek provide **2-way morphological distinction**
- TBTA's 10-way system required because **target languages need finer granularity**
- Contextual inference from narrative **essential** for values beyond basic near/far

### 3. Person-Oriented Systems Common in Translation Context

- Major Bible translation languages include **many person-oriented** systems:
  - Spanish (548M), Japanese (125M), Korean (81M), Hindi (602M), Tagalog (estimated 90M)
- Requires distinguishing **S (near speaker) vs. L (near addressee)**
- English "that" ambiguity problematic - TBTA resolves

### 4. Three Domains: Spatial, Temporal, Discourse

- **Spatial** (S, L, N, R, r): Physical world deixis
- **Temporal** (T, t): Time reference
- **Discourse** (C, c): Textual anaphora

All three domains **cross-linguistically valid** and **necessary for Biblical translation**

### 5. Visibility and Elevation Limited

- **Visibility** (R vs. r): Present in TBTA, attested in Austronesian, Yupik
- **Elevation**: NOT in TBTA (would require expansion)
- Most languages **do not require** these features - **lower priority**

### 6. Genre Affects Discourse Demonstrative Distribution

- **Narrative**: Balanced spatial + discourse demonstratives
- **Epistolary/Expository**: High discourse demonstrative frequency (c/C)
- **Poetry/Prophecy**: Temporal demonstratives common (T/t)

**Biblical Corpus**: Multi-genre → All TBTA proximity values necessary

### 7. Target Language Adaptation

- **2-way languages**: Collapse TBTA categories (S/L/N → proximal; R/r → distal)
- **3-way languages**: Use full TBTA spatial distinctions
- **Discourse demonstratives**: Map to language-specific anaphoric forms
- **Temporal demonstratives**: Map to language-specific temporal deictics

---

## Recommended Language Family References for Stage 2

1. **Austronesian**: Himmelmann & Adelaar (2005) *The Austronesian Languages of Asia and Madagascar*
2. **Bantu**: Nurse & Philippson (2003) *The Bantu Languages*
3. **Japonic**: Hinds (1986) *Japanese*; Shibatani (1990) *The Languages of Japan*
4. **Romance**: Posner (1996) *The Romance Languages*
5. **Trans-New Guinea**: Foley (1986) *The Papuan Languages of New Guinea*
6. **Sino-Tibetan**: Norman (1988) *Chinese*; LaPolla & Thurgood (2003) *The Sino-Tibetan Languages*

---

**Lines**: ~750 (Target: ≤800 per progressive disclosure guidelines for research files)

---

## Sources

- [WALS Online - Chapter Distance Contrasts in Demonstratives](https://wals.info/chapter/41)
- [Grambank Database](https://grambank.clld.org/)
- [Grambank - Feature GB035](https://grambank.clld.org/parameters/GB035)
- [The Bantu Languages - Routledge](https://www.taylorfrancis.com/books/edit/10.4324/9780203987926/bantu-languages-derek-nurse-gérard-philippson)
- [Diessel (1999) Demonstratives - John Benjamins](https://www.benjamins.com/catalog/tsl.42)
- [Tagalog Reference Grammar - Google Books](https://books.google.com/books?id=E8tApLUNy94C)
- [Yupik Elevation Systems - Frontiers](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2020.01712/full)
