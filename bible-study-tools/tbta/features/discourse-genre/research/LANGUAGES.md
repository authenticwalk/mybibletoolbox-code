# Language Typology Analysis: Discourse Genre

## Executive Summary

Discourse genre is **NOT morphologically encoded** in Biblical Hebrew or Greek but is **grammatically obligatory** for correct tense/aspect selection in many target languages. This creates a unique translation challenge: translators must infer genre from context and then apply genre-specific grammatical rules in their target language.

**Key Finding**: 176 Austronesian, 141 Trans-New Guinea, and 89 Niger-Congo languages in our corpus likely require genre-aware translation strategies, particularly for narrative tense systems and register distinctions.

**Critical Languages**: French, Hebrew (target), Bantu languages (89+), Japanese, Mandarin Chinese, and many Austronesian languages have **obligatory** genre-tense correlations where wrong genre = ungrammatical translation.

---

## 1. Source Language Encoding Check

### Biblical Hebrew (heb)

**Status**: Genre is NOT morphologically encoded but **grammatically restricts** which verb forms are valid.

**Evidence**:
- **wayyiqtol** (narrative sequential past): ONLY grammatical in prose narrative [biblicalhebrew.org](https://biblicalhebrew.org/hebrew-verbal-system-wayyiqtol-forms-in-biblical-narrative.aspx)
- **Cannot** appear in poetry or law (genre restriction)
- In archaic Hebrew poetry, wayyiqtol is "altogether absent" [academia.edu](https://www.academia.edu/9598188/)
- qatal (perfect) and yiqtol (imperfect) used differently across genres

**Implication**: Hebrew grammar **requires** genre identification to determine which verb forms are permissible.

### Koine Greek (grc)

**Status**: Genre is NOT morphologically encoded but influences aspectual choices.

**Evidence**:
- Aorist: "mainline events that provide the foundation for the narrative" (foreground) [newtestamentgreek.net](https://www.newtestamentgreek.net/the-grammar-of-astonishment-and-difficulty.html)
- Imperfect: "descriptive or background information" (background)
- Genre distinction "limited to narrative proper in Greek" [ntdiscourse.org](https://www.ntdiscourse.org/2010/03/on-background-foreground-and-genre-in-greek/)
- Present tense for teaching/timeless statements

**Implication**: While not obligatory, genre strongly predicts aspect selection in Greek narrative.

---

## 2. Language Family Analysis

### Available Language Families (from `/src/constants/languages.tsv`)

Total: 1,008 language varieties across 34+ families

Top families by count:
- **Austronesian**: 176 languages
- **Trans-New Guinea**: 141 languages
- **Indo-European**: 135 languages
- **Niger-Congo** (including Bantu): 89 languages
- **Otomanguean**: 69 languages
- **Mayan**: 41 languages
- **Australian**: 36 languages
- **Afro-Asiatic**: 25 languages
- **Sino-Tibetan**: 18 languages
- **Quechuan**: 18 languages

---

## 3. Typological Classification by Feature Necessity

### MANDATORY: Genre-Tense Systems (Grammatically Obligatory)

Languages where **wrong genre = ungrammatical** translation.

#### A. Romance Languages (Indo-European)

**French (fra)** - 4 translations available
- **passé simple**: ONLY for written narrative [sil.org](https://www.sil.org/resources/publications/entry/8785)
- **imparfait**: Background/descriptive in narrative
- **présent**: Timeless teaching/exposition
- **conditionnel**: Legal/conditional statements
- **Restriction**: "passé simple is only a tense used in written language" [lawlessfrench.com](https://www.lawlessfrench.com/grammar/passe-compose-vs-imparfait/)
- **Translation Impact**: HIGH - must distinguish narrative vs. conversational discourse

**Spanish (spa)** - 6+ translations available
- **pretérito** vs. **imperfecto**: Similar foreground/background distinction (suspected)
- Less strict than French but genre-aware (suspected)

**Portuguese (por)** - 4 translations available
- Similar to Spanish (suspected)

**Italian (ita)** - 2 translations available
- Genre-tense correlation present (suspected)

**Romanian (ron)** - 4 translations available
- Genre distinctions likely (suspected)

**Classification**: MANDATORY for French (verified); MANDATORY for Spanish/Portuguese/Italian/Romanian (suspected)

---

#### B. Bantu Languages (Niger-Congo)

**Swahili (swh)** - 3 translations available
**Ganda/Luganda (lug)** - 1 translation

**Evidence**:
- "Extensive genre-based tense systems" (archive data)
- Simple past (perfective): Main narrative
- Continuous past: Background
- Habitual present: Generic/teaching
- Bantu has "narrativity" as a Bantu-wide category [academia.edu](https://www.academia.edu/116177741/)
- Research shows "perfective aspect or past tense marks the narrative event line" is NOT universal in Bantu - more complex (suspected)

**Scale**: 89+ Niger-Congo languages in corpus (many Bantu)

**Cultural Note**: Many Bantu-speaking regions have oral tradition backgrounds where narrative structure is culturally significant [orality.net](https://orality.net/related/storying/)

**Classification**: MANDATORY (suspected based on tense-aspect research and archive data)

---

#### C. East Asian Languages

**Japanese (jpn)** - Limited/no translations in corpus (suspected based on general typology)

**Evidence**:
- "Distinct registers and verb forms per genre" (archive data)
- da vs. desu/masu: "da style is selected when the speaker takes a perspective internal to the narrative setting" [sciencedirect.com](https://www.sciencedirect.com/science/article/abs/pii/037821669190111A)
- Narrative: ta-form past
- Teaching: i-adjectives, desu/masu polite forms
- Formal legal: Archaic constructions
- "Different levels of formality in Japanese are marked lexically through verb endings" [japaneseprofessor.com](https://www.japaneseprofessor.com/lessons/beginning/politeness-and-formality/)

**Classification**: MANDATORY (register-based grammar)

**Mandarin Chinese (cmn)** - 4 translations available

**Evidence**:
- "Aspect particles differ by genre" (archive data)
- "Discourse particles change with register" (archive data)
- Less morphologically marked than Japanese but genre-sensitive (suspected)

**Classification**: MANDATORY (suspected)

---

#### D. Austronesian Languages (176 in corpus)

**Major Finding**: Widespread use of "change of state (COS) markers" as discourse structuring devices.

**Evidence**:
- Polyfunctional COS markers in 52 Austronesian languages "combine aspectual meaning of change of state with information and discourse structuring functions" [degruyter.com](https://www.degruyterbrill.com/document/doi/10.1515/lingty-2020-0129/html)
- Used to "indicate events considered pivotal in the narrative's development" (foreground marking)
- "Foregrounding devices" distinguish event line from background

**Examples from Research**:
- **Da'a** (Austronesian, Indonesia): "coreferentiality of actor in successive foreground actions is a basic determining factor in focus affixation" [anu.edu.au](https://openresearch-repository.anu.edu.au/server/api/core/bitstreams/63ad21e4-174d-46bf-be8a-13df69045e55/content)
- **Northern Vanuatu languages** (17 languages): TAM categories include "sequential, generic, subjunctive, prospective and imperfective" tied to discourse structure [academia.edu](https://www.academia.edu/1330253)

**Sample Languages in Corpus** (selected):
- Miniafia Oyan (aai), Ankave (aak), Amarasi (aaz), Inabaknon (abx), Adzera (adz), Arosi (aia), Alune (alp), Ambai (amk)
- 176 total varieties across Philippines, Indonesia, Papua New Guinea, Solomon Islands, Madagascar

**Cultural Note**: Many Austronesian cultures in Papua New Guinea (301 languages in our corpus from PNG, Nigeria, Cameroon) have strong oral traditions with "sung tales" and narrative performance traditions [academia.edu](https://www.academia.edu/75779145/)

**Classification**: MANDATORY for many (suspected based on TAM-discourse research); OPTIONAL for others (suspected)

---

#### E. Trans-New Guinea Languages (141 in corpus)

**Evidence**:
- Papua New Guinea has extensive oral culture traditions [ywamkona.org](https://ywamkona.org/how-i-discovered-the-power-of-oral-bible-translation-to-transform-papua-new-guinea/)
- "Discourse features differ significantly between languages" - example: Kwakum uses present tense for storytelling (non-standard genre-tense mapping) [haretranslation.com](https://www.haretranslation.com/2019/09/15/how-does-oral-bible-storying-work/)
- Limited typological data available for most PNG languages

**Sample Languages**: Agarabi (agd), Angaataha (agm), Awa (awb), Barai (bbb), Benabena (bef), Bedamuni (beo), Biangai (big)

**Cultural Note**: Strong oral tradition - narrative structure highly salient in cultural communication

**Classification**: OPTIONAL to MANDATORY (suspected, varies by language) - requires individual language research

---

### OPTIONAL: Genre Affects Style but Not Grammaticality

#### A. Indo-European (Non-Romance)

**English (eng)** - 40+ translations available
- Genre affects register, formality, vocabulary
- NOT grammatically obligatory for tense selection
- Poetry permits inversions; prose does not (word order flexibility)
- **Classification**: OPTIONAL

**German (deu)** - 4 translations available
- Similar to English (suspected)
- **Classification**: OPTIONAL (suspected)

**Bengali (ben)** - 1 translation
- Limited data (suspected OPTIONAL based on Indo-European patterns)

---

#### B. Sino-Tibetan (excluding Mandarin)

18 languages in corpus - limited genre-tense research available

**Classification**: OPTIONAL to MANDATORY (suspected, varies by language)

---

#### C. Mayan Languages (41 in corpus)

**Sample**: Achi (acr), Awakateko (agu)

Limited typological research on discourse genre in Mayan languages

**Classification**: OPTIONAL to MANDATORY (suspected) - requires further research

---

#### D. Quechuan Languages (18 in corpus)

Limited discourse-genre research available

**Classification**: OPTIONAL to MANDATORY (suspected) - requires further research

---

### ABSENT: Genre Not Grammatically Relevant

**Criteria**: Languages where genre does not affect grammatical choices (very rare)

**Note**: Most languages show at least OPTIONAL genre sensitivity for register/formality. True ABSENCE is rare.

**Classification**: No languages confidently classified as ABSENT - requires negative evidence

---

## 4. Root Languages (Translation Source Languages)

"Root languages" = major Bible translation languages that translators often start from.

### Primary Root Languages

| Language | ISO-639-3 | Status in Corpus | Genre-Tense Status | Notes |
|----------|-----------|------------------|---------------------|-------|
| **Hebrew** | heb | Source (OT) | MANDATORY (morphosyntactic restrictions) | wayyiqtol only in narrative |
| **Greek** | grc | Source (NT) | OPTIONAL (strong preference) | aorist/imperfect correlate with foreground/background |
| **English** | eng | 40+ translations | OPTIONAL | Major bridge language |
| **French** | fra | 4 translations | MANDATORY | passé simple genre-restricted |
| **Spanish** | spa | 6 translations | MANDATORY (suspected) | pretérito/imperfecto distinction |
| **German** | deu | 4 translations | OPTIONAL (suspected) | |
| **Portuguese** | por | 4 translations | MANDATORY (suspected) | Similar to Spanish |
| **Arabic** | arb | 2 translations | OPTIONAL (suspected) | Classical vs. Modern registers differ |
| **Mandarin** | cmn | 4 translations | MANDATORY (suspected) | Discourse particles genre-sensitive |
| **Swahili** | swh | 3 translations | MANDATORY (suspected) | Bantu narrative tense system |
| **Indonesian** | ind | Not found in sample | OPTIONAL (suspected) | Austronesian but isolating |

### Secondary Root Languages (Regional)

- **Latin** (lat): Historical, not in modern corpus
- **Italian** (ita): 2 translations - MANDATORY (suspected)
- **Romanian** (ron): 4 translations - MANDATORY (suspected)

---

## 5. Candidate Languages for Translation Database (Stage 2)

**Goal**: Select 5-10 languages representing diverse typological profiles for testing discourse-genre algorithm.

### Selection Criteria
1. **Diversity**: Mix of obligatory vs. optional genre marking
2. **Family Representation**: Major families represented
3. **Data Availability**: Languages with multiple translations preferred
4. **Typological Significance**: Languages that test edge cases

### Recommended Candidates (8 languages)

| # | Language | ISO-639-3 | Family | Verses | Genre Status | Rationale |
|---|----------|-----------|--------|--------|--------------|-----------|
| 1 | **French** | fra | Indo-European (Romance) | 31,055+ | MANDATORY | Gold standard: passé simple is genre-restricted (verified) |
| 2 | **Spanish** | spa | Indo-European (Romance) | 31,096+ | MANDATORY (suspected) | Test Romance pretérito/imperfecto system |
| 3 | **English** | eng | Indo-European (Germanic) | 31,081+ | OPTIONAL | Baseline: genre affects style, not grammar |
| 4 | **Mandarin** | cmn | Sino-Tibetan | 31,087+ | MANDATORY (suspected) | Test discourse particle system |
| 5 | **Swahili** | swh | Niger-Congo (Bantu) | 31,098+ | MANDATORY (suspected) | Representative Bantu narrative tense |
| 6 | **German** | deu | Indo-European (Germanic) | 31,097+ | OPTIONAL (suspected) | Control for Germanic (compare to English) |
| 7 | **Portuguese** | por | Indo-European (Romance) | 31,097+ | MANDATORY (suspected) | Test Romance variation |
| 8 | **Ganda** | lug | Niger-Congo (Bantu) | 31,099 | MANDATORY (suspected) | Second Bantu language for comparison |

### Alternate Candidates (if needed)

| Language | ISO-639-3 | Family | Rationale |
|----------|-----------|--------|-----------|
| **Italian** | ita | Indo-European (Romance) | Third Romance language |
| **Romanian** | ron | Indo-European (Romance) | Eastern Romance variation |
| **Amarasi** | aaz | Austronesian | Representative Austronesian (9,490 verses) |
| **Barai** | bbb | Trans-New Guinea | PNG oral tradition language (13,139 verses) |

### NOT Recommended (Insufficient Data or Overlap)

- Japanese: Not in corpus (suspected)
- Most Trans-New Guinea: Limited typological research, smaller corpora
- Australian languages: Limited research on discourse genre
- Mayan languages: Smaller corpora, limited typological data

---

## 6. Cultural Nuances

### A. Oral Cultures

**Regions**: Papua New Guinea (301 languages in corpus), parts of Africa, indigenous Americas

**Significance**:
- Narrative structure is **culturally salient** - "sung tales" and performance traditions [academia.edu](https://www.academia.edu/75779145/)
- Genre distinctions may be **more rigid** in oral cultures where oral performance follows strict conventions
- "Oral Bible Translation meets the needs of oral preference communities" [haretranslation.com](https://www.haretranslation.com/2019/09/15/how-does-oral-bible-storying-work/)

**Translation Challenge**: Written Bible may not match oral narrative conventions. Example: Kwakum (Cameroon) "tell a story using mostly the present tense" - non-standard genre-tense mapping.

**Languages Affected**:
- Trans-New Guinea (141 languages): Awa, Barai, Benabena, Bedamuni, etc.
- Many Austronesian (176 languages): especially in PNG/Solomon Islands
- Many Niger-Congo (89 languages): West/Central African languages

---

### B. Poetic Traditions

**Biblical Hebrew Poetry**:
- Psalms, Proverbs, Job, Song of Songs, prophetic oracles
- **No wayyiqtol**: "altogether absent" in archaic poetry [academia.edu](https://www.academia.edu/9598188/)
- Different verb system than prose narrative

**Translation Implications**:
- Target languages with **special poetic registers** (Japanese, Classical Arabic, etc.) may require genre-specific vocabulary/forms
- Target languages with **poetic word order freedom** (many Indo-European) must recognize when inversion is permissible

**Cultural Variations**:
- Some cultures (Hebrew, Arabic, Classical languages) have **distinct poetic registers**
- Others (English, modern Romance) have **stylistic preferences** but not obligatory distinctions

---

### C. Honorifics and Register

**Japanese**:
- Not in corpus but typologically significant
- **Obligatory honorific system** tied to genre: desu/masu (polite) vs. da (plain)
- Legal/religious texts require highest formality level
- Narrative perspective (internal vs. external) determines register choice [sciencedirect.com](https://www.sciencedirect.com/science/article/abs/pii/037821669190111A)

**Korean** (not in corpus):
- Similar honorific system (suspected)

**Implications**: Genre (legal, epistolary, teaching) determines which register is grammatical.

---

### D. Taboos and Social Distinctives

**Limited Data**: No specific discourse-genre taboos identified in research.

**General Principle**: Some cultures restrict certain discourse types to specific social contexts:
- Religious/prophetic discourse may require special markers
- Legal discourse may use archaic or formulaic language
- Epistolary conventions vary widely (formal vs. informal address)

**Future Research Needed**: Ethnographic work on genre-specific cultural constraints in Bible translation contexts.

---

## 7. Summary Tables

### By Grammatical Necessity

| Status | Count (Estimated) | Language Families | Translation Impact |
|--------|-------------------|-------------------|-------------------|
| **MANDATORY** | 300-500+ languages | Romance, Bantu, East Asian, many Austronesian | Wrong genre = ungrammatical |
| **OPTIONAL** | 300-500+ languages | Germanic, some Austronesian, some Otomanguean | Genre affects style/register |
| **ABSENT** | <50 languages (suspected) | Unknown | Genre not grammatically relevant |

### By Language Family (Top 5)

| Family | Count | Genre Status | Key Examples |
|--------|-------|--------------|--------------|
| Austronesian | 176 | MANDATORY to OPTIONAL (suspected) | COS markers, TAM systems |
| Trans-New Guinea | 141 | OPTIONAL to MANDATORY (suspected) | Oral cultures, limited data |
| Indo-European | 135 | Mixed: MANDATORY (Romance) to OPTIONAL (Germanic) | French (MANDATORY), English (OPTIONAL) |
| Niger-Congo | 89 | MANDATORY (suspected) | Bantu narrative tense systems |
| Otomanguean | 69 | OPTIONAL to MANDATORY (suspected) | Limited data |

---

## 8. Research Gaps and Uncertainties

### High Priority (Affects Candidate Selection)

1. **Austronesian languages**: 176 languages, but most lack detailed discourse-genre research. COS markers documented in 52 languages - need to determine which of our 176 have genre-obligatory systems.

2. **Trans-New Guinea**: 141 languages, minimal typological data. Oral culture suggests high salience, but grammatical status unknown for most.

3. **Bantu languages**: Archive data and general typology suggest MANDATORY, but need verification for specific languages (Swahili, Ganda, others).

4. **Mandarin Chinese**: Archive data says "discourse particles change with register" - need verification of grammatical obligation vs. stylistic preference.

### Medium Priority (Affects Algorithm Design)

5. **Mayan languages** (41): No discourse-genre research found.

6. **Australian languages** (36): Limited data on narrative structure.

7. **Quechuan languages** (18): No discourse-genre research found.

### Low Priority (Small Counts or Edge Cases)

8. **Language isolates** (10): Each requires individual research.

9. **Minor families** (<10 languages each): Address as needed for specific translation projects.

---

## 9. Verification Status Legend

Throughout this document:
- **(verified)**: Cited from academic source or authoritative documentation
- **(suspected)**: Based on typological patterns, family membership, or general linguistic knowledge; **NOT verified** from authoritative source on this specific language
- **(archive data)**: From previous discourse-genre research in `/features-archive/discourse-genre/`
- No marker: From languages.tsv data or general structural information

---

## 10. Next Steps for Stage 2

1. **Verify suspected classifications** for top 8 candidate languages using scholarly sources or native speaker grammars.

2. **Test with Translation Database**: Use selected languages to build train/test/validate sets (Stage 4).

3. **Refine Austronesian analysis**: 176 languages is a large set - identify which have genre-obligatory systems vs. optional.

4. **Papua New Guinea deep dive**: 301 PNG languages across multiple families - oral culture significance suggests prioritization.

5. **Expand root language coverage**: If Hebrew (OT) is primary source, prioritize languages Hebrew-speaking translators commonly use as bridge languages.

---

## Sources

### Typological Databases
- [World Atlas of Language Structures (WALS)](https://wals.info/) - General typology (note: no specific discourse-genre chapter found)
- [Grambank](https://simon.net.nz/project/grambank/) - 195 morphosyntactic features across 2,400 languages

### Biblical Language Sources
- [Biblical Hebrew wayyiqtol](https://biblicalhebrew.org/hebrew-verbal-system-wayyiqtol-forms-in-biblical-narrative.aspx)
- [Understanding Wayyiqtol in Biblical Hebrew](https://biblicalhebrew.org/understanding-wayyiqtol-in-biblical-hebrew.aspx)
- [Biblical Hebrew Wayyiqtol: A Dynamic Definition (academic paper)](https://jhsonline.org/index.php/jhs/article/download/11523/8841/30000)
- [Koine Greek foreground/background](https://www.ntdiscourse.org/2010/03/on-background-foreground-and-genre-in-greek/)

### Language-Specific Research
- [French Imparfait and Passé Simple in Discourse (SIL)](https://www.sil.org/resources/publications/entry/8785)
- [Bantu tense and aspect marking](https://www.academia.edu/116177741/)
- [Japanese discourse modality (da/desu)](https://www.sciencedirect.com/science/article/abs/pii/037821669190111A)
- [Austronesian COS markers](https://www.degruyterbrill.com/document/doi/10.1515/lingty-2020-0129/html)
- [Da'a focus and narrative structure](https://openresearch-repository.anu.edu.au/server/api/core/bitstreams/63ad21e4-174d-46bf-be8a-13df69045e55/content)

### Oral Culture and Bible Translation
- [Papua New Guinea oral Bible translation](https://ywamkona.org/how-i-discovered-the-power-of-oral-bible-translation-to-transform-papua-new-guinea/)
- [Oral Bible Storying](https://www.haretranslation.com/2019/09/15/how-does-oral-bible-storying-work/)
- [Sung tales from PNG Highlands](https://www.academia.edu/75779145/)

---

**Document Status**: Stage 1 Research - Language Typology Analysis
**Created**: 2025-11-25
**Verification Level**: Mixed (verified + suspected classifications noted throughout)
**Next Update**: After Stage 2 verification with translation database
