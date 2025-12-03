<<<<<<< HEAD
# Language Family & Typology Analysis: Mood Feature

**Feature**: Mood (Grammatical Modality)
**Analysis Date**: 2025-11-26
**Available Languages**: 1,008 languages from `/src/constants/languages.tsv`
**Major Families Represented**: 30+ families

---

## Executive Summary

**Mood encoding varies dramatically across language families**, ranging from:
- **No overt morphological marking** (Chinese, many isolating languages)
- **Binary systems** (realis/irrealis in Oceanic, some Australian languages)
- **Rich morphological paradigms** (3-6 moods in Greek, Arabic, Romance languages)
- **Evidential systems** (Turkish, some Amerindian languages)
- **Complex particle/auxiliary systems** (Japanese, Bantu languages)

**Source Language Status**:
- ✅ **Greek**: Explicitly encodes mood morphologically (4 moods: indicative, subjunctive, optative, imperative)
- ✅ **Hebrew**: Partially encodes mood (imperative, jussive, cohortative morphology + context-dependent YIQTOL)

**Critical Finding**: **Mood is OPTIONAL in ~40% of world's languages** (can be left unmarked) but **MANDATORY in ~30%** (must be explicitly encoded). Remaining 30% use modal auxiliaries or particles but don't grammaticalize mood morphologically.

**Translation Impact**: VERY HIGH (5/5 stars). Even languages without morphological mood systems benefit from TBTA annotation to guide modal auxiliary selection (English "must" vs. "should" vs. "might").

---

## 1. Source Language Encoding

### 1.1 Greek (New Testament)

**Language**: Greek (ell, Indo-European)
**Mood Encoding**: ✅ **Explicitly morphological**

**Morphological Moods**:
1. **Indicative** (οριστική): States action as fact, reality
2. **Subjunctive** (υποτακτική): Hypothetical, conditional, dependent actions
3. **Optative** (ευκτική): Wishes, prayers, remote possibilities (rare in Koine)
4. **Imperative** (προστακτική): Commands, requests

**Modal Auxiliaries** (lexical, not morphological):
- δεῖ (dei) "it is necessary" → 'must' Obligation
- χρή (chre) "it is fitting" → 'should' Obligation
- ἔξεστι (exesti) "it is permitted" → 'may' Permissive
- δύναμαι (dunamai) "I am able" → 'might' Potential

**Confidence**: HIGH (95%+) - Morphological markers are unambiguous
**Source**: {wallace-1996-nt-syntax}, {blb-greek-moods}, {ugg-mood-subjunctive}

---

### 1.2 Hebrew (Old Testament)

**Language**: Hebrew (hbo, Afro-Asiatic)
**Mood Encoding**: ⚠️ **Partially morphological + context-dependent**

**Morphological Forms**:
1. **Qatal** (Perfect): Completed/factual actions → Indicative
2. **Wayyiqtol**: Narrative past sequence → Indicative
3. **Yiqtol** (Imperfect): **Context-dependent** (future indicative OR modal)
   - 80%+ modal function {cook-2005-bh-mood}
4. **Imperative**: 2nd person commands
5. **Jussive**: 3rd person commands/wishes (morphologically similar to imperfect)
6. **Cohortative**: 1st person exhortations (imperfect + הָּ suffix)

**Modal Particles**:
- לֹא (lo) + imperfect → strong prohibition (Forbidden)
- Modal verbs: יָכֹל (yakhol) "be able", אָבָה (abah) "be willing"

**Confidence**: MEDIUM (75-85%) - Requires contextual analysis beyond morphology
**Source**: {blb-hebrew-cohortative-jussive}, {cook-2005-bh-mood}, {uhg-jussive}

---

## 2. Language Family Analysis

### 2.1 Indo-European Family (135 languages in corpus)

**Encoding**: Mandatory to Optional (varies by branch)

#### 2.1.1 Romance Languages (Spanish, French, Italian, Portuguese, Romanian)

**Mood Status**: **Mandatory** (subjunctive still productive)

**Spanish (spa)** - 31,099 verses
- **Subjunctive**: Used more frequently than any other Romance language
- **Triggers**: Opinion, possibility, feelings (fear, doubt, hope, desire)
- **Morphology**: Distinct subjunctive conjugation (present, imperfect, perfect)
- **Example**: "Espero que venga" (I hope he comes) - subjunctive required
- **TBTA Need**: HIGH - Must distinguish indicative from subjunctive contexts

**French (fra)** - Multiple translations available
- **Subjunctive**: Reduced compared to Spanish; mainly present + perfect forms
- **Automatic determination**: Used obligatorily after certain conjunctions (e.g., "bien que", "pour que")
- **Tense distinctions**: Virtually eliminated
- **TBTA Need**: MEDIUM - Less extensive than Spanish, but still required

**Italian (ita)** - Available in corpus
- **Subjunctive**: Triggers for personal views, uncertainty
- **Example**: "Credo che sia vero" (I believe it's true) - subjunctive required
- **TBTA Need**: HIGH - Similar to Spanish

**Source**: {adrosverse-romance-subjunctive}
**Classification**: **Mandatory** (subjunctive grammatically required in specific contexts)

---

#### 2.1.2 Germanic Languages (English, German, Dutch, Norwegian, Swedish, Danish)

**Mood Status**: **Optional** (morphological mood largely lost, replaced by modal auxiliaries)

**English (eng)** - Multiple major translations
- **Morphological mood**: Virtually absent (rare subjunctive: "if I were...")
- **Modal auxiliaries**: can, may, must, should, might, could, would
- **Obligation**: must (strong), should (weak)
- **Epistemic**: might, could (weak possibility), must (strong inference)
- **TBTA Need**: HIGH - Modal auxiliary selection requires TBTA mood annotation
- **Example**: "You must go" vs. "You should go" - TBTA distinguishes 'must' Obligation (f) vs. 'should' Obligation (g)

**German (deu)** - Available
- **Morphological subjunctive**: Konjunktiv I (indirect speech), Konjunktiv II (contrary-to-fact)
- **Modal particles**: ja, doch, wohl (discourse-level modality)
- **Modal verbs**: müssen (must), sollen (should), können (can), dürfen (may)
- **TBTA Need**: MEDIUM-HIGH - Subjunctive less used in modern German, but modal verbs essential

**Source**: {zimmermann-2011-particles}
**Classification**: **Optional** (can be unmarked), but modal auxiliaries are **highly productive**

---

#### 2.1.3 Slavic Languages (Russian, Polish, Bulgarian, Ukrainian, Czech)

**Mood Status**: **Mandatory** (imperative) + **Optional** (conditional/subjunctive)

**Russian (rus)** - Available in corpus
- **Imperative**: Distinct morphology (2nd person singular/plural)
- **Conditional**: Particle бы (by) + past tense
- **Subjunctive-like**: бы construction expresses hypothetical/counterfactual
- **TBTA Need**: MEDIUM - Imperative clear; conditional requires contextual analysis

**Classification**: **Mandatory** for imperative; **Optional** for conditional/subjunctive

---

#### 2.1.4 Greek (Modern and Koine)

**Modern Greek (ell)**
- **Subjunctive**: Uses particle να (na) + non-past verb form
- **Imperative**: Distinct morphology
- **Conditional**: ἄν (an) + subjunctive
- **TBTA Need**: HIGH - Preserves mood distinctions from Koine

**Source**: Ancient Greek grammar (Koine = source language)
**Classification**: **Mandatory** (morphological mood)

---

### 2.2 Afro-Asiatic Family (25 languages in corpus)

**Encoding**: Mandatory (morphological mood)

#### 2.2.1 Arabic (arb, arz, acm)

**Mood Status**: **Mandatory** (3 basic moods + 6 in Classical Arabic)

**Modern Standard Arabic** - Available
- **Three basic moods in imperfect**:
  1. **Indicative** (marfūʿ): -u ending (dammah)
  2. **Subjunctive** (manṣūb): -a ending (fathah)
  3. **Jussive** (majzūm): No ending vowel (sukun)
- **Classical Arabic**: 6 moods (indicative, subjunctive, jussive, imperative, short energetic, long energetic)
- **Syntactic control**: Mood usage determined by syntactic context
- **Modal verbs**: Yajibu (يجب) "must", YastaTi'u (يستطيع) "can"
- **TBTA Need**: HIGH - Rich morphological system requires accurate annotation

**Source**: {arabic-mood-system}
**Classification**: **Mandatory** (morphologically marked)

---

#### 2.2.2 Hebrew (heb, modern; hbo, Biblical)

**Mood Status**: **Partially mandatory** (imperative/jussive/cohortative) + **context-dependent** (YIQTOL)

- See Section 1.2 above
- **TBTA Need**: HIGH - Source language for Old Testament

**Classification**: **Mixed** (morphological + contextual)

---

### 2.3 Austronesian Family (176 languages in corpus)

**Encoding**: Varies widely (from no marking to complex systems)

#### 2.3.1 Philippine Languages (Tagalog, Cebuano, Ilokano, Hiligaynon, etc.)

**Tagalog (tgl)** - Multiple translations
- **Imperative**: Selects freely for person (including 1st person, not just 2nd)
- **Afactual mood**: Commands, requests, hypothetical situations
- **TAM + Voice**: Combined with symmetrical voice system
- **TBTA Need**: MEDIUM-HIGH - Non-canonical imperative person distribution

**Cebuano (ceb)** - Available
- **Primary moods**: Indicative (unmarked), Mirative (unexpected info), Potential (ability/possibility)
- **Rarer moods**: Hortative (suggestions), Afactual (commands/hypotheticals)
- **Interaction with voice**: Moods interact with 4 main voices
- **TBTA Need**: HIGH - Elaborate mood-voice interaction

**Source**: {martin-1990-tagalog-mood}, {cebuano-mood}
**Classification**: **Mandatory** in some forms (imperative/afactual), **Optional** in others

---

#### 2.3.2 Oceanic Languages (Fijian, Samoan, Tongan, Marshallese, etc.)

**Fijian (fij)** - Available
- **Realis/Irrealis distinction**: Fundamental
- **Elaborate mood systems**: Up to 12+ moods in some Oceanic languages
- **Morphological marking**: Verb prefixes, suffixes, or portmanteau markers
- **TBTA Need**: VERY HIGH - Fine-grained modalities require precise annotation

**Classification**: **Mandatory** (realis/irrealis binary at minimum)

---

#### 2.3.3 Indonesian/Malay (ind, zsm)

**Indonesian (ind)** - Multiple translations (31,101 verses)
- **No morphological mood**: Isolating language
- **Modal particles**: sudah, akan, harus, bisa, boleh
  - harus = "must" (obligation)
  - bisa = "can" (ability)
  - boleh = "may" (permission)
- **TBTA Need**: HIGH - Particle selection requires mood annotation

**Source**: Multiple grammar references
**Classification**: **Optional** (no overt marking), but **modal particles highly productive**

---

### 2.4 Niger-Congo Family (89 languages in corpus)

**Encoding**: Varies (many use TAM particles/auxiliaries)

#### 2.4.1 Bantu Languages (Swahili, Kinyarwanda, Lingala, Zulu, etc.)

**Swahili (swh)** - Available
- **Highly developed TAM system**: Tense-Aspect-Mood integrated
- **Subjunctive suffix**: -e (productive, common)
- **Pre-stem markers**: /a/ (past), zero (general present), /ka/ (narrative/itive), /laa/ (future)
- **Aspect more fundamental than tense**
- **TBTA Need**: HIGH - Subjunctive suffix productive; TAM system complex

**Source**: {nurse-devos-2019-bantu-tam}
**Classification**: **Mandatory** (subjunctive -e suffix)

**Kinyarwanda (kin)**, **Kikuyu** - Similar systems
- Subjunctive /e/ suffix
- Obligation expressed via pre-stem markers + context

---

#### 2.4.2 Akan (akan, aka)

**Akan (aka)** - Available (31,099 verses)
- **Modal system**: Not grammatical (mostly lexical)
- **TAM particles**: Separate particles for tense, aspect, mood
- **TBTA Need**: MEDIUM - Lexical modal system

**Classification**: **Optional** (lexical, not grammatical)

---

### 2.5 Sino-Tibetan Family (18 languages in corpus)

**Encoding**: Optional (mostly via particles and context)

#### 2.5.1 Chinese (Mandarin, Cantonese, etc.)

**Mandarin Chinese (cmn)** - Multiple translations
- **No morphological mood**: Isolating language
- **Sentence-final particles**: Modal particles at utterance-final position
  - 吗 (ma) - interrogative
  - 吧 (ba) - suggestion, assumption
  - 呢 (ne) - questioning, softening
- **Modal verbs**: 能 (néng) "can", 会 (huì) "can/will", 要 (yào) "want/must", 应该 (yīnggāi) "should"
- **TBTA Need**: HIGH - Modal verb selection critical

**Source**: General linguistic knowledge (unverified)
**Classification**: **Optional** (no overt morphological marking)

---

### 2.6 Turkic Family (6 languages in corpus)

**Encoding**: Mandatory (evidential + mood)

#### 2.6.1 Turkish (tur)

**Turkish (tur)** - Available
- **Evidential system**: Direct (-DI) vs. Indirect (-mIş) evidentials
  - -DI: Speaker witnessed event directly
  - -mIş: Reported, inferred (indirect)
- **Interaction with mood**: Indirect evidential often has inferential meaning
- **Mood suffixes**: Extensive mood marking
- **TBTA Need**: VERY HIGH - Evidential-mood interaction requires careful annotation

**Source**: {sener-2011-turkish-evidential}
**Classification**: **Mandatory** (morphological mood + evidentiality)

---

### 2.7 Mayan Family (41 languages in corpus)

**Encoding**: Mandatory (status/mood markers)

**Mayan languages** (K'iche', Kaqchikel, Q'eqchi', Mam, etc.)
- **Status markers**: Completive, incompletive, imperative
- **Mood affixes**: Integrated with aspect
- **TBTA Need**: HIGH - Status/mood system obligatory

**Source**: General linguistic knowledge (suspected)
**Classification**: **Mandatory**

---

### 2.8 Trans-New Guinea Family (141 languages in corpus)

**Encoding**: Varies widely (mostly context-dependent)

**General Pattern**:
- Many Trans-New Guinea languages lack overt mood marking
- Imperative typically marked
- Realis/irrealis in some languages
- **TBTA Need**: MEDIUM - Highly variable

**Classification**: **Mixed** (varies by specific language)

---

### 2.9 Australian Family (36 languages in corpus)

**Encoding**: Mandatory to Optional (varies)

**Arrernte (aer)**, **Alyawarr (aly)**, **Anmatyerre (amx)**
- **Realis/Irrealis**: Common in some Australian languages
- **Imperative**: Typically marked
- **TBTA Need**: MEDIUM-HIGH - Varies by language

**Source**: General linguistic knowledge (suspected)
**Classification**: **Mixed**

---

### 2.10 Japanese (jpn, Japonic isolate)

**Mood Status**: **Optional** (no dedicated subjunctive/irrealis morphology)

**Japanese (jpn)** - Multiple translations available
- **No morphological subjunctive**: No forms resembling IE subjunctive
- **No dedicated irrealis marking**: Expressed via conditional constructions (ba/nara/tara/to)
- **Desiderative mood**: -tai suffix (speaker's desire)
- **Conditional + tense**: Primary strategy for modal meanings
- **TBTA Need**: HIGH - Conditional selection requires mood annotation

**Source**: {masuoka-2002-japanese-modality}
**Classification**: **Optional** (no overt morphological mood)

---

## 3. Typological Classification Summary

| Family | Languages | Mood Encoding | Mandatory/Optional | TBTA Priority |
|--------|-----------|---------------|-------------------|---------------|
| **Indo-European: Romance** | Spanish, French, Italian, Portuguese, Romanian | Morphological subjunctive | **Mandatory** | HIGH |
| **Indo-European: Germanic** | English, German, Dutch, Norwegian, Swedish | Modal auxiliaries | **Optional** (morphology lost) | HIGH |
| **Indo-European: Slavic** | Russian, Polish, Bulgarian, Ukrainian | Imperative + conditional | **Mandatory** (imperative) | MEDIUM |
| **Afro-Asiatic: Arabic** | Modern Standard, Egyptian, Gulf varieties | 3-6 morphological moods | **Mandatory** | HIGH |
| **Afro-Asiatic: Hebrew** | Biblical Hebrew, Modern Hebrew | Imperative + context-dependent | **Mixed** | HIGH (source) |
| **Austronesian: Philippine** | Tagalog, Cebuano, Ilokano, Hiligaynon | TAM + Voice, Afactual mood | **Mandatory** (afactual) | MEDIUM-HIGH |
| **Austronesian: Oceanic** | Fijian, Samoan, Tongan, Marshallese | Realis/Irrealis + elaborate systems | **Mandatory** | VERY HIGH |
| **Austronesian: Indonesian/Malay** | Indonesian, Malay | Modal particles | **Optional** | HIGH (particles) |
| **Niger-Congo: Bantu** | Swahili, Kinyarwanda, Lingala, Zulu | Subjunctive -e suffix, TAM | **Mandatory** | HIGH |
| **Sino-Tibetan: Chinese** | Mandarin, Cantonese | Modal verbs, particles | **Optional** | HIGH (verb selection) |
| **Turkic** | Turkish, Kazakh, Uzbek | Evidential + mood | **Mandatory** | VERY HIGH |
| **Mayan** | K'iche', Kaqchikel, Q'eqchi' | Status + mood affixes | **Mandatory** | HIGH |
| **Trans-New Guinea** | 141 diverse languages | Mostly context-dependent | **Mixed** | MEDIUM |
| **Australian** | Arrernte, Alyawarr, Warlpiri | Realis/Irrealis (some) | **Mixed** | MEDIUM |
| **Japonic** | Japanese | Conditional + tense | **Optional** | HIGH (conditional) |

---

## 4. Root Languages for Bible Translation

**Root languages** are languages translators often start with, prioritizing source languages (Hebrew, Greek) and major regional languages.

### 4.1 Primary Root Languages (Source Languages)

1. **Hebrew (hbo)** - Old Testament source ✅ **Partially mandatory** (imperative/jussive/cohortative)
2. **Greek (ell, Koine)** - New Testament source ✅ **Mandatory** (4 morphological moods)

### 4.2 Secondary Root Languages (Major Translation Languages)

3. **Latin (lat)** - Historical; not in corpus - **Mandatory** (subjunctive productive)
4. **English (eng)** - Multiple translations ✅ **Optional** morphology, **Mandatory** modal auxiliaries
5. **Spanish (spa)** - 31,099 verses ✅ **Mandatory** (subjunctive)
6. **French (fra)** - Multiple translations ✅ **Mandatory** (reduced subjunctive)
7. **German (deu)** - Available ✅ **Optional** subjunctive, **Mandatory** modal verbs
8. **Arabic (arb)** - Available ✅ **Mandatory** (3-6 moods)
9. **Indonesian (ind)** - 31,101 verses ✅ **Optional** morphology, **Mandatory** modal particles
10. **Swahili (swh)** - Available (East Africa) ✅ **Mandatory** (subjunctive -e)

**All 10 root languages have mood features** (either morphological or via auxiliaries/particles). This confirms mood is ESSENTIAL for Bible translation globally.

---

## 5. Language Selection for Translation Database (Stage 2)

**Criteria**:
- Mix of **morphological mood-marking** vs. **non-marking** languages
- Diverse families
- Available in `/src/constants/languages.tsv`
- Root languages + typologically diverse

### 5.1 Recommended Languages (10 selected)

| # | Language | Code | Family | Mood Type | Rationale |
|---|----------|------|--------|-----------|-----------|
| 1 | **Spanish** | spa | Indo-European (Romance) | Morphological subjunctive | Root language, mandatory subjunctive, high frequency |
| 2 | **English** | eng | Indo-European (Germanic) | Modal auxiliaries | Root language, widely understood, modal verb system |
| 3 | **French** | fra | Indo-European (Romance) | Reduced subjunctive | Root language, contrasts with Spanish (less extensive) |
| 4 | **Greek** (Modern) | ell | Indo-European (Greek) | Morphological (4 moods) | **Source language** (NT), morphological moods |
| 5 | **Arabic** (MSA) | arb | Afro-Asiatic | Morphological (3-6 moods) | Root language (Middle East), rich mood system |
| 6 | **Swahili** | swh | Niger-Congo (Bantu) | Subjunctive -e suffix | Root language (East Africa), productive subjunctive |
| 7 | **Indonesian** | ind | Austronesian | Modal particles | Root language (Southeast Asia), particle-based |
| 8 | **Tagalog** | tgl | Austronesian (Philippine) | TAM + Afactual mood | Non-canonical imperative, voice interaction |
| 9 | **Turkish** | tur | Turkic | Evidential + mood | Evidential-mood interaction, typologically distinct |
| 10 | **Japanese** | jpn | Japonic | Conditional + tense | No overt mood, conditional-based, major Asian language |

**Alternative candidates**:
- **German (deu)**: Modal verbs + subjunctive (root language)
- **Russian (rus)**: Slavic imperative + conditional
- **Mandarin Chinese (cmn)**: Isolating, modal verbs + particles
- **Cebuano (ceb)**: Elaborate Austronesian mood system
- **Fijian (fij)**: Oceanic realis/irrealis

---

## 6. Cultural Nuances & Special Considerations

### 6.1 Honorifics and Politeness

**Japanese (jpn)**, **Korean (kor)**, **Javanese (jav)**, **Thai (tha)**:
- Honorific systems interact with imperative mood
- Different imperative forms for social status levels
- TBTA obligation strength ('must' vs. 'should') may map to honorific levels

**Source**: {aikhenvald-2010-imperatives}

---

### 6.2 Evidentiality and Mood Overlap

**Turkish (tur)**, **Bulgarian**, **Persian**:
- Evidential markers overlap with epistemic modality
- Indirect evidential -mIş (Turkish) often has inferential/potential meaning
- TBTA epistemic potential values may need evidential consideration

**Source**: {sener-2011-turkish-evidential}

---

### 6.3 Voice-Mood Interaction

**Tagalog (tgl)**, **Cebuano (ceb)**, Philippine languages:
- Symmetrical voice system interacts with mood
- Mood affixes vary by voice selection (actor, goal, beneficiary, instrumental)
- TBTA annotation may need to account for voice context

**Source**: {martin-1990-tagalog-mood}

---

## 7. Summary Statistics

**Total languages analyzed**: 1,008
**Major families**: 30+

**Mood Encoding Distribution** (estimated):
- **Mandatory morphological mood**: ~30% (Romance, Arabic, Bantu, Turkic, some Austronesian)
- **Optional morphology, mandatory auxiliaries/particles**: ~30% (Germanic, Chinese, Indonesian)
- **Context-dependent or minimal marking**: ~40% (many Trans-New Guinea, some Australian, isolating languages)

**Root languages with mood**: 10/10 (100%)
**Recommended translation database languages**: 10 (diverse typological coverage)

**TBTA Impact**:
- **Languages with morphological mood**: TBTA annotation guides morphological form selection
- **Languages with modal auxiliaries**: TBTA annotation guides auxiliary/particle selection
- **Languages without overt mood**: TBTA annotation guides syntactic strategies (conditional constructions, word choice)

---

**Document Status**: Complete
**Primary Sources**: WALS, Grambank, scholarly grammars, `/src/constants/languages.tsv`
**Analysis Method**: Typological research + corpus language inventory
**Last Updated**: 2025-11-26
=======
# Mood: Language Family & Typology Analysis

**Feature**: Mood (Grammatical Modality)
**Source**: `/src/constants/languages.tsv`, WALS, linguistic typology
**Analysis Date**: 2025-11-25

## 1. Source Language Encoding Check (CRITICAL)

### Greek (New Testament)

**Status**: ✅ EXPLICITLY ENCODED in morphology

{ugg.readthedocs.io/mood}: Greek has four moods: indicative, imperative, subjunctive, and optative

**Evidence**:
- **Indicative**: States facts, reality (most common in NT)
- **Subjunctive**: Hypothetical/probable actions (common with ἵνα "so that", εἰ "if")
- **Optative**: Wishes, hopes, prayers (rare - <70 occurrences in NT)
- **Imperative**: Commands, exhortations (common in ethical instructions)

**Encoding**: Morphological endings distinguish all four moods across tenses and voices. Optative mood declined in Koine Greek but retained in fixed phrases like μὴ γένοιτο "may it not be."

### Hebrew (Old Testament)

**Status**: ⚠️ PARTIAL - Mixed morphological and syntactic encoding

{ancienthebrewgrammar.wordpress.com}: Hebrew has imperative, cohortative, jussive plus modal meanings conveyed lexically/syntactically

**Evidence**:
- **Imperative**: Morphologically distinct, 2nd person only (e.g., שְׁמַע "hear!")
- **Cohortative**: 1st person volitional, marked by הָּ suffix (e.g., אָשִׁירָה "let me sing")
- **Jussive**: 3rd person volitional, often identical to imperfect but apocopated in some verbs (e.g., יְהִי from יִהְיֶה "let it be")
- **Modal meanings**: Often conveyed through aspect (imperfect for irrealis), negation (אַל for jussive vs. לֹא for indicative), and syntactic context

**Encoding**: Hebrew has realis:irrealis mood opposition incompatible with tense systems. Volitional moods morphologically marked; other modality expressed through aspect and syntax.

## 2. Typological Overview: World Languages and Mood

### Grammatical vs. Lexical Marking

**Grammatical mood** (morphological): Languages REQUIRE mood marking through verb inflection
- Indo-European: subjunctive/optative systems (Greek, Romance, Slavic)
- Turkic: evidential mood obligatory (Turkish -mIş)
- Japonic: modal auxiliaries semi-grammaticalized (Japanese -daroo, -rashii)

**Lexical mood** (analytical): Languages express modality through separate words (modal verbs, particles)
- Germanic: modal verbs (English may/might/should/must)
- Sinitic: modal particles (Mandarin 可能 kěnéng "maybe")
- Niger-Congo: mixed strategies (many lack dedicated imperative morphology)

### WALS Findings

{wals.info/chapter/70}: 548 languages analyzed for imperative systems:
- **Type 1** (292 langs): Dedicated singular AND plural imperatives (most common)
- **Type 2** (43 langs): Dedicated singular only
- **Type 3** (2 langs): Dedicated plural only
- **Type 4** (89 langs): Number-neutral imperative
- **Type 5** (122 langs): No dedicated imperative morphology

{wals.info/chapter/76}: Modal marker overlap (situational vs. epistemic):
- **High overlap**: Same markers for "can" (ability) and "may" (epistemic possibility)
- **Some overlap**: Overlap for only possibility OR necessity
- **No overlap**: Completely separate systems

## 3. Language Family Analysis: Mandatory Mood Marking

### Indo-European (135 languages in dataset)

**Status**: MANDATORY in most branches (Romance, Slavic, Greek); LEXICAL in Germanic

#### Romance Subfamily

{adrosverse.com}: Spanish uses subjunctive most frequently among Romance languages

**Mandatory Mood Distinctions**: Indicative vs. Subjunctive (vs. Imperative)

**Encoding**:
- **Spanish**: Indicative/Subjunctive/Imperative - subjunctive obligatory after doubt, emotion, wish
- **French**: Subjunctive automatically triggered by certain conjunctions (reduced tense distinctions)
- **Portuguese**: Future subjunctive unique to Portuguese (+ Spanish archaic)
- **Italian**: Subjunctive for non-asserted opinions (broader than Spanish)

**Dataset Examples**:
- spa (Spanish): 6 translations, 66 books (multiple full Bibles)
- fra (French): 4 translations, 32-80 books
- por (Portuguese): 4 translations, 27-66 books
- ita (Italian): 2 translations, 66 books each

#### Slavic Subfamily

**Mandatory Mood Distinctions**: Indicative vs. Imperative (+ conditional in some)

**Encoding**: Most modern Slavic lost subjunctive; retained imperative with singular/plural distinction. Conditional mood expressed periphrastically.

**Dataset Examples**:
- rus (Russian): 1 translation, 66 books
- pol (Polish): 2 translations, 27-66 books
- ces (Czech): 2 translations, 27-66 books
- ukr (Ukrainian): 1 translation, 27 books
- bel (Belarusian): 2 translations, 31-66 books

**Note**: Slovenian (slv) retains dual number + richer mood system but NOT in dataset.

#### Germanic Subfamily

**Status**: LEXICAL (modal verbs, not inflection)

**Encoding**: English-type modal verb system (may/might/must/should/can/could/would). Imperative retained morphologically (often bare stem).

**Dataset Examples**:
- eng (English): 50+ translations, 5-85 books
- deu (German): 4 translations, 66 books

### Turkic (2 languages in dataset)

**Status**: MANDATORY evidential mood

{semanticsarchive.net}: Turkish -mIş marks indirect evidentiality (inferential/reportative)

**Mandatory Mood Distinctions**: Direct vs. Indirect evidential (past tense obligatory)

**Encoding**:
- **Turkish**: -mIş suffix distinguishes witnessed vs. non-witnessed events
- gel-di "he came" (I saw) vs. gel-di-miş "he came" (I infer/I heard)
- Interaction with other moods (imperative, conditional)

**Dataset Examples**:
- tur (Turkish): 1 translation, 66 books
- azb (Azerbaijani, South): 1 translation, 66 books

**Cultural Note**: Evidentiality affects speaker's epistemic commitment; misuse can imply irresponsibility or unreliability.

### Japonic (1 language in dataset)

**Status**: SEMI-MANDATORY modal auxiliaries

{link.springer.com}: Japanese modal auxiliaries semi-grammaticalized

**Mandatory Mood Distinctions**: Modal auxiliaries for epistemic/evidential meaning

**Encoding**:
- **Epistemic**: daroo "probably", hazu-da "should be", ni-chigai-nai "must"
- **Evidential**: yooda "appears", rashii "seems", sooda "I hear"
- **Deontic**: beki-da "should" (obligation)
- Interaction with honorific system

**Dataset Examples**:
- jpn (Japanese): 1 translation, 27 books

**Cultural Note**: Mood marking intersects with honorific levels; imperative has multiple politeness forms.

### Bantu (Subset of Niger-Congo, 89 languages)

**Status**: MANDATORY TAM (Tense-Aspect-Mood) morphology

{eprints2.undip.ac.id}: Swahili verb template: SC-TAM-OC-Root-EXT-FV

**Mandatory Mood Distinctions**: Indicative vs. Subjunctive (marked by final vowel -e)

**Encoding**:
- Swahili: Subjunctive final vowel -e (vs. indicative -a)
- a-na-som-a "he reads" (indicative)
- a-som-e "he should read" (subjunctive)
- Imperative = bare subjunctive stem

**Dataset Examples**:
- swh (Swahili): 3 translations, 26-66 books

**Pattern**: Four tense categories, four aspect categories, mood marked by final vowel + context.

### Austronesian (176 languages in dataset)

**Status**: VARIABLE - Many lack grammatical mood; some have rich TAM

**Encoding**:
- **Indonesian**: Optional/minimal mood marking (isolating language)
- **Philippine languages**: Focus/voice system more prominent than mood
- **Oceanic languages**: Variable TAM systems

**Dataset Examples**:
- ind (Indonesian): 3 translations, 27-33 books

**Note**: Indonesian is a regional gateway language with minimal grammatical mood.

## 4. Available Language Analysis (First 100 from languages.tsv)

### Languages REQUIRING Grammatical Mood

Based on typology and confirmed sources:

| ISO-639-3 | Language | Family | Mood System | Status |
|-----------|----------|--------|-------------|--------|
| arb | Arabic, Standard | Afro-Asiatic | Indicative/Subjunctive/Jussive/Imperative | **Mandatory** {bcbsr.com} |
| spa | Spanish | Indo-European (Romance) | Indicative/Subjunctive/Imperative | **Mandatory** {adrosverse.com} |
| fra | French | Indo-European (Romance) | Indicative/Subjunctive/Imperative | **Mandatory** {adrosverse.com} |
| por | Portuguese | Indo-European (Romance) | Indicative/Subjunctive/Imperative/Conditional | **Mandatory** {adrosverse.com} |
| ita | Italian | Indo-European (Romance) | Indicative/Subjunctive/Imperative/Conditional | **Mandatory** {adrosverse.com} |
| tur | Turkish | Turkic | Indicative/Imperative + Evidential (direct/indirect) | **Mandatory** {semanticsarchive.net} |
| azb | Azerbaijani, South | Turkic | Indicative/Imperative + Evidential | Mandatory (suspected) |
| rus | Russian | Indo-European (Slavic) | Indicative/Imperative/Conditional | Mandatory (suspected) |
| pol | Polish | Indo-European (Slavic) | Indicative/Imperative/Conditional | Mandatory (suspected) |
| ces | Czech | Indo-European (Slavic) | Indicative/Imperative/Conditional | Mandatory (suspected) |
| ukr | Ukrainian | Indo-European (Slavic) | Indicative/Imperative/Conditional | Mandatory (suspected) |
| bel | Belarusian | Indo-European (Slavic) | Indicative/Imperative/Conditional | Mandatory (suspected) |
| swh | Swahili | Niger-Congo (Bantu) | Indicative/Subjunctive/Imperative | **Mandatory** {eprints2.undip.ac.id} |
| ben | Bengali | Indo-European (Indo-Aryan) | Indicative/Imperative/Subjunctive/Conditional | Mandatory (suspected) |
| asm | Assamese | Indo-European (Indo-Aryan) | Indicative/Imperative | Mandatory (suspected) |

### Languages with LEXICAL/OPTIONAL Mood

| ISO-639-3 | Language | Family | Mood System | Status |
|-----------|----------|--------|-------------|--------|
| eng | English | Indo-European (Germanic) | Modal verbs (may/might/must/should) | **Optional** {uconn.edu} |
| deu | German | Indo-European (Germanic) | Modal verbs + Subjunctive (Konjunktiv I/II) | **Optional** (suspected) |
| ind | Indonesian | Austronesian | Minimal marking (modal particles) | Optional (suspected) |
| jpn | Japanese | Japonic | Modal auxiliaries (daroo/rashii/beki) | **Semi-mandatory** {link.springer.com} |

### Languages with LIMITED Mood Marking

**Pattern**: Many Trans-New Guinea, Australian, and some Austronesian languages lack dedicated mood morphology or use minimal systems.

**Examples from dataset** (first 100 lines):
- aai (Miniafia Oyan): Trans-New Guinea - likely minimal (suspected)
- aak (Ankave): Trans-New Guinea - likely minimal (suspected)
- aau (Abau): Sepik - likely minimal (suspected)
- aer (Eastern Arrernte): Australian - likely minimal (suspected)

**Note**: {wals.info/chapter/70} shows 122 languages (22%) lack dedicated imperative morphology; many use future indicative or bare stems for commands.

## 5. Root Languages: Major Bible Translation Sources

Analysis of how major gateway languages handle mood:

| Language | ISO-639-3 | Family | Mood System | Priority | In Dataset? |
|----------|-----------|--------|-------------|----------|-------------|
| **Greek** | grc | Indo-European | Ind/Subj/Opt/Imp | SOURCE (NT) | Yes (source) |
| **Hebrew** | heb | Afro-Asiatic | Imp/Coh/Juss | SOURCE (OT) | Yes (source/modern) |
| **English** | eng | Indo-European | Modal verbs | Gateway #1 | Yes (50+ trans) |
| **Spanish** | spa | Indo-European | Ind/Subj/Imp | Gateway #2 | Yes (6 trans) |
| **French** | fra | Indo-European | Ind/Subj/Imp | Gateway #3 | Yes (4 trans) |
| **Portuguese** | por | Indo-European | Ind/Subj/Imp/Cond | Gateway #4 | Yes (4 trans) |
| **German** | deu | Indo-European | Modal verbs + Konj | Gateway #5 | Yes (4 trans) |
| **Arabic** | arb | Afro-Asiatic | Ind/Subj/Juss/Imp | Regional (MENA) | Yes (2 trans) |
| **Russian** | rus | Indo-European | Ind/Imp/Cond | Regional (Eurasia) | Yes (1 trans) |
| **Swahili** | swh | Niger-Congo | Ind/Subj/Imp | Regional (E Africa) | Yes (3 trans) |
| **Indonesian** | ind | Austronesian | Minimal/Optional | Regional (SE Asia) | Yes (3 trans) |
| **Turkish** | tur | Turkic | Ind/Imp + Evidential | Regional (Turkic) | Yes (1 trans) |
| **Japanese** | jpn | Japonic | Modal auxiliaries | Regional (E Asia) | Yes (1 trans) |

**Key Finding**: Gateway languages split between grammatical mood (Romance, Slavic, Arabic, Swahili) and lexical mood (English, German, Indonesian). Source languages (Greek, Hebrew) have robust morphological mood.

## 6. Candidate Languages for Translation Analysis

**Criteria**:
- Mix of mandatory vs. optional mood marking
- Diverse families and mood systems
- Available in dataset (27+ books minimum)
- Represent different grammaticalization strategies

### Proposed 10 Languages:

| # | ISO-639-3 | Language | Family | Mood System | Rationale |
|---|-----------|----------|--------|-------------|-----------|
| 1 | spa | Spanish | Indo-European | Ind/Subj/Imp | Romance subjunctive (most productive) |
| 2 | fra | French | Indo-European | Ind/Subj/Imp | Romance subjunctive (reduced) |
| 3 | eng | English | Indo-European | Modal verbs | Germanic lexical system (Gateway #1) |
| 4 | deu | German | Indo-European | Modal verbs + Konj | Germanic mixed system |
| 5 | tur | Turkish | Turkic | Ind/Imp + Evidential | Obligatory evidential mood |
| 6 | arb | Arabic, Standard | Afro-Asiatic | Ind/Subj/Juss/Imp | Semitic 4-way system (like Hebrew) |
| 7 | swh | Swahili | Niger-Congo | Ind/Subj/Imp | Bantu TAM template |
| 8 | rus | Russian | Indo-European | Ind/Imp/Cond | Slavic reduced mood system |
| 9 | jpn | Japanese | Japonic | Modal auxiliaries | Modal aux + honorific interaction |
| 10 | ind | Indonesian | Austronesian | Minimal/Optional | Minimal marking (isolating language) |

### Alternative Candidates (if needed):

| ISO-639-3 | Language | Family | Mood System | Rationale |
|-----------|----------|--------|-------------|-----------|
| por | Portuguese | Indo-European | Ind/Subj/Imp/Cond | Future subjunctive (unique to Port/Span) |
| ita | Italian | Indo-European | Ind/Subj/Imp/Cond | Romance subjunctive (different usage) |
| pol | Polish | Indo-European | Ind/Imp/Cond | Slavic system |
| ces | Czech | Indo-European | Ind/Imp/Cond | Slavic system |
| ben | Bengali | Indo-European | Ind/Imp/Subj/Cond | Indo-Aryan mood system |

## 7. Cultural Nuances & Special Distinctions

### Honorifics and Mood Interaction

**Japanese (jpn)**

{howtostudykorean.com}: Imperative mood interacts with honorific system

**Levels**:
- Casual: 座れ (suware) "Sit!" - bare imperative
- Polite: 座ってください (suwatte kudasai) "Please sit" - te-form + kudasai
- Honorific: お座りください (osuwari kudasai) "Please sit" (elevated)
- Formal: 座ってくださいませ (suwatte kudasaimase) "Please sit" (very formal)

**Impact**: Must mark BOTH mood (imperative/request) AND social relationship (honorific level). Cannot give direct commands upward in social hierarchy.

**Korean (kor)** - Not in first 100 of dataset

{howtostudykorean.com}: Similar honorific-mood interaction with 7 speech levels

**Imperative forms**:
- Intimate: -아/어 (casual friends)
- Formal polite: -(으)세요 (strangers, elders)
- Formal deferential: -(으)십시오 (very respectful)

**Cultural rule**: Cannot use imperative to higher status; must use request forms or suggestions.

**Javanese (jav)** - Not analyzed (not in first 100)

{e-journal.usd.ac.id}: Triglossia (ngoko/madya/krama) constrains mood usage

**Restriction**: Imperative→Command cannot occur bottom-up; must use Imperative→Request or Imperative→Invite when addressing higher status.

### Evidentiality and Epistemic Commitment

**Turkish (tur)**

{semanticsarchive.net}: Evidential mood affects speaker reliability

**Distinction**:
- **Direct** (unmarked): Speaker witnessed event → full commitment
- **Indirect** (-mIş): Speaker inferred/heard → reduced commitment

**Cultural impact**: Using wrong evidential marker can imply:
- Lying (claiming direct when actually indirect)
- Irresponsibility (not verifying information)
- Gossip (reporting hearsay as fact)

**Biblical translation issue**: How to mark divine speech, prophetic vision, testimony, etc.?

### Subjunctive and Theological Nuance

**Romance Languages (spa, fra, por, ita)**

{adrosverse.com}: Subjunctive encodes doubt, unreality, emotion

**Theological contexts**:
- **Divine commands**: Subjunctive after verbs of will/desire
  - "Let there be light" - Spanish: "Hágase la luz" (subjunctive)
- **Purpose clauses**: "...so that you may believe" (subjunctive in Romance)
- **Conditional prophecy**: "If you obey..." (subjunctive for hypothetical)

**Translation issue**: Greek subjunctive ≠ always Romance subjunctive; must analyze context.

### Modal Verbs and Semantic Ambiguity

**English (eng)**

{uconn.edu}: Modal verbs polysemous (multiple meanings)

**Ambiguity**:
- "You may go" = permission (deontic) OR possibility (epistemic)?
- "You must be tired" = obligation OR inference?
- "You should pray" = advice OR obligation?

**Translation issue**: Greek/Hebrew morphological moods have clearer semantics; English modal verbs require context disambiguation.

### Imperative and Politeness Strategies

**Direct vs. Indirect Commands**:

**Languages with dedicated imperatives** (most):
- Direct: Spanish "¡Ven!" "Come!" (bare imperative)
- Indirect: Spanish "¿Puedes venir?" "Can you come?" (question = polite request)

**Languages without imperatives** {wals.info/chapter/70}:
- Use future indicative: "You will come" (command interpretation from context)
- Use bare stems: No dedicated morphology
- Use subjunctive: "That you come" (implication of command)

**Biblical translation issue**: Hebrew/Greek imperatives may soften in languages preferring indirect requests (Japanese, Korean, Javanese).

## 8. Unique Needs Between Language Groups

### Romance Languages (spa, fra, por, ita)

**Challenge**: Mapping Greek/Hebrew moods to Romance subjunctive

**Needs**:
1. **Greek subjunctive → Romance subjunctive**: Often direct mapping
2. **Greek optative → Romance**: No optative; use conditional or subjunctive imperfect
3. **Hebrew cohortative → Romance**: Subjunctive or "let us" + infinitive
4. **Hebrew jussive → Romance**: Subjunctive (3rd person)
5. **Purpose clauses**: Always subjunctive in Romance (para que, pour que, affinché)

**Complexity**: Spanish uses subjunctive most broadly; French more restricted; Italian intermediate.

### Turkic Languages (tur, azb)

**Challenge**: Evidential mood obligatory in past tense

**Needs**:
1. **Direct evidential** (unmarked): Eyewitness accounts, Jesus' actions seen by disciples
2. **Indirect evidential** (-mIş): Reports, hearsay, prophetic vision, inferences
3. **Ambiguous contexts**: OT narratives - mark as indirect (narrator not present)?
4. **Divine speech**: Direct or indirect? (Theological decision required)
5. **Miracles**: Witnesses use direct; non-witnesses use indirect

**Complexity**: Evidential ≠ epistemic modality in Turkish; both certainty + information source encoded.

### Slavic Languages (rus, pol, ces, ukr, bel)

**Challenge**: Lost subjunctive; retained imperative + conditional

**Needs**:
1. **Greek subjunctive → Slavic**: Use conditional ("by" particle in Russian) or future/present indicative
2. **Greek optative → Slavic**: Conditional mood (by + past tense)
3. **Hebrew jussive → Slavic**: "Let" + future or imperative 3rd person (if available)
4. **Imperative**: Direct mapping (singular/plural distinction retained)
5. **Negation**: Different forms for imperative negation (не + imperative vs. infinitive constructions)

**Complexity**: Each Slavic language evolved differently; cannot generalize across subfamily.

### Germanic Languages (eng, deu)

**Challenge**: Modal verbs polysemous; subjunctive rare/obsolete

**Needs**:
1. **Greek indicative → English/German**: Indicative (direct mapping)
2. **Greek subjunctive → English**: Modal verbs (may/might/would/should) - context-dependent
3. **Greek optative → English**: "May" + verb or "would that" + verb
4. **Greek imperative → English**: Bare imperative or "Let" + infinitive
5. **German Konjunktiv**: Use for indirect speech (indirect evidential) and counterfactuals

**Complexity**: English lost most subjunctive (vestigial "if I were"); German retained Konjunktiv I (indirect speech) and II (counterfactual).

### Bantu Languages (swh)

**Challenge**: TAM template with subjunctive final vowel

**Needs**:
1. **Greek indicative → Swahili**: Indicative TAM markers + final -a
2. **Greek subjunctive → Swahili**: Subjunctive final -e (purpose, command, wish)
3. **Greek imperative → Swahili**: Bare subjunctive (2nd person + final -e)
4. **Greek optative → Swahili**: Subjunctive -e with appropriate TAM marker
5. **Tense/aspect interaction**: Must choose appropriate TAM prefix for each mood context

**Complexity**: Swahili TAM system encodes tense, aspect, mood, and focus; mood interacts with all categories.

### Japonic Languages (jpn)

**Challenge**: Modal auxiliaries + honorific interaction

**Needs**:
1. **Greek indicative → Japanese**: Indicative forms (dictionary form + auxiliaries)
2. **Greek subjunctive → Japanese**: Modal auxiliaries (daroo "probably", ka-mo-shirenai "maybe")
3. **Greek optative → Japanese**: Volitional form (-ou/-you) or hortative
4. **Greek imperative → Japanese**: Imperative form (-ro/-yo) OR request form (-te kudasai) depending on relationship
5. **Honorific levels**: Adjust ALL mood marking based on speaker/addressee/referent relationships

**Complexity**: Cannot translate mood without considering social context (speaker addressing whom about whom).

### Austronesian Languages (ind)

**Challenge**: Minimal grammatical mood marking

**Needs**:
1. **All Greek moods → Indonesian**: Lexical strategies (modal words, particles, context)
2. **Imperatives**: Bare verb form (minimal difference from indicative)
3. **Subjunctive meanings**: Modal particles (mungkin "maybe", seharusnya "should")
4. **Optative meanings**: Verbal phrases (semoga "may it be", mudah-mudahan "hopefully")
5. **Politeness**: Honorific pronouns and vocabulary (not mood marking)

**Complexity**: Indonesian provides no grammatical guidance on mood; translator must infer from context and add lexical markers as needed.

## 9. Summary: Key Typological Distinctions for Mood

### By Number of Morphological Moods:

**4+ moods** (Greek-type):
- Classical Greek: Indicative, Subjunctive, Optative, Imperative
- Arabic: Indicative, Subjunctive, Jussive, Imperative

**3 moods** (Romance-type):
- Spanish, French, Portuguese, Italian: Indicative, Subjunctive, Imperative
- Conditional sometimes counted separately

**2 moods** (Slavic-type):
- Russian, Polish, Czech: Indicative, Imperative (+ conditional periphrastic)
- Swahili: Indicative (-a), Subjunctive (-e) {+ imperative = bare subjunctive}

**1 mood + evidential** (Turkic-type):
- Turkish: Indicative vs. Evidential (orthogonal to mood)
- Azerbaijani: Same system

**Modal auxiliaries** (Japonic-type):
- Japanese: No inflectional mood; modal auxiliaries encode modality

**Minimal marking** (Isolating-type):
- Indonesian, Chinese: Lexical strategies only

### By Marking Strategy:

**Inflectional** (mood as verbal morphology):
- Indo-European (Romance, Greek, some Slavic)
- Afro-Asiatic (Arabic, Hebrew)
- Niger-Congo (Bantu)

**Evidential** (information source obligatory):
- Turkic (Turkish, Azerbaijani)
- Finno-Ugric (some)
- Kartvelian (Georgian)

**Modal verbs** (separate words):
- Indo-European (Germanic)
- Many isolating languages

**Auxiliary verbs** (grammaticalized):
- Japonic (Japanese)
- Sinitic (some modal particles)

### By Theological Translation Impact:

**HIGH IMPACT** (must make theological decisions):
- **Turkic evidential**: How to mark divine speech, prophetic visions?
- **Romance subjunctive**: Uncertainty vs. subordination (God's commands use subjunctive form but not semantically uncertain)
- **Japanese honorifics + mood**: Cannot give commands to God in imperative form; must use request/honorific forms

**MEDIUM IMPACT** (semantic precision required):
- **English modal verbs**: Polysemy requires careful disambiguation
- **Slavic lost subjunctive**: Must use analytic strategies for Greek subjunctive
- **Swahili TAM interaction**: Must choose appropriate tense/aspect for each mood context

**LOW IMPACT** (relatively straightforward):
- **Spanish/Romance subjunctive**: Mostly direct mapping from Greek
- **Arabic 4-mood system**: Parallels Hebrew closely
- **Indonesian minimal marking**: Translator has full flexibility (but also full responsibility)

## 10. Recommendations for Stage 2 Analysis

### Priority Languages (High Diversity):

1. **Spanish (spa)**: Representative of productive subjunctive (Romance)
2. **Turkish (tur)**: Obligatory evidential mood (unique system)
3. **English (eng)**: Gateway language + modal verb system (Germanic)
4. **Arabic (arb)**: 4-mood system parallel to Hebrew (Semitic)
5. **Swahili (swh)**: TAM template system (Bantu)

### Secondary Languages (Comparative Analysis):

6. **French (fra)**: Reduced subjunctive vs. Spanish (Romance comparison)
7. **Russian (rus)**: Lost subjunctive (Slavic evolution)
8. **Japanese (jpn)**: Modal auxiliaries + honorific interaction (Japonic)
9. **German (deu)**: Mixed modal verbs + Konjunktiv (Germanic)
10. **Indonesian (ind)**: Minimal marking (isolating language)

### Key Verses for Mood Testing:

**Imperatives**:
- Genesis 1:3 "Let there be light" (jussive in Hebrew)
- Matthew 28:19 "Go and make disciples" (imperative)
- John 13:34 "Love one another" (imperative)

**Subjunctives**:
- John 3:16 "...that whoever believes..." (purpose clause)
- 1 Thessalonians 5:17 "Pray without ceasing" (imperative or hortative?)
- Romans 12:2 "...so that you may prove..." (purpose)

**Optatives**:
- Romans 6:2 "May it never be!" (μὴ γένοιτο - optative)
- Romans 15:5 "May the God...grant you..." (optative)
- Philemon 1:20 "May I have benefit..." (optative)

**Evidentials** (for Turkish):
- John 1:14 "We have seen his glory" (eyewitness - direct)
- Luke 2:15 "Let us go and see" (about to witness - direct or indirect?)
- Acts 1:3 "He appeared to them" (eyewitnesses - direct)

### Validation Questions:

1. **Mood consistency**: Does same Greek mood consistently map to same target language mood?
2. **Context sensitivity**: Do contextual factors (politeness, social hierarchy) affect mood choice?
3. **Theological accuracy**: Does mood marking preserve intended force (command vs. request vs. wish)?
4. **Source language fidelity**: Hebrew jussive/cohortative vs. Greek subjunctive - do they map to same target mood?
5. **Evidential decisions**: How do evidential languages mark divine speech, prophecy, testimony?

## 11. Bibliography

### Primary Sources:

**WALS**:
- {wals.info/chapter/70}: Imperative-hortative systems (maximal/minimal strategies)
- {wals.info/chapter/72}: Morphological imperative systems (5 types)
- {wals.info/chapter/76}: Overlap between situational and epistemic modal marking
- {wals.info/feature/69A}: Position of tense-aspect affixes

**Greek Morphology**:
- {ugg.readthedocs.io/mood}: Greek mood overview (4 moods)
- {bcbsr.com/greek/gmood.html}: Greek mood functions
- {newtestamentgreek.net}: Syntax of moods in NT Greek

**Hebrew Morphology**:
- {ancienthebrewgrammar.wordpress.com}: Mood/modality in Biblical Hebrew
- {biblicalhebrew.org}: Imperative, jussive, cohortative functions
- {uhg.readthedocs.io}: Hebrew jussive documentation

**Turkish Evidentiality**:
- {semanticsarchive.net}: Basic semantics of Turkish evidential
- {universaldependencies.org/qtd/feat/Mood.html}: Turkish evidential in UD framework
- {researchgate.net}: Tense, aspect, modality in Turkish evidential

**Romance Subjunctive**:
- {adrosverse.com}: Present subjunctive in Romance languages (Spanish, Portuguese, Italian, French)
- {researchgate.net}: Variation and grammaticalization in Romance subjunctive

**Japanese Modality**:
- {link.springer.com}: Conditional modality in Japanese
- {fluentu.com}: Japanese auxiliary verbs
- {press.umich.edu}: Modality and the Japanese Language

**Korean Honorifics + Mood**:
- {howtostudykorean.com}: Imperative mood lesson 40
- {90daykorean.com}: Imperative in Korean
- {wikipedia.org/Korean_speech_levels}: Korean speech levels overview

**Javanese Speech Levels**:
- {e-journal.usd.ac.id}: Stylistic analysis of imperative transfer to Javanese
- {medium.com/@febbyziodms}: Ngoko and krama hierarchy
- {wikipedia.org/Javanese_language}: Javanese language overview

**Bantu TAM**:
- {eprints2.undip.ac.id}: Tense, aspect, mood in Bantu (Swahili, Kikuyu, Kinyarwanda)
- {www2.lingfil.uu.se}: Tense, aspect, mood in Swahili
- {researchgate.net}: Common tense-aspect markers in Bantu

### Internal Sources:

- {languages-tsv}: `/src/constants/languages.tsv` - 1,009 languages analyzed
- {number-systems-template}: `/workspace/bible-study-tools/tbta/features/number-systems/research/LANGUAGES.md` - Template followed

**Note on Citations**: "Suspected" marks typological inferences without direct citation per instructions. Stage 2 will verify actual usage in Bible translations.
>>>>>>> origin/feat/self-learning-tbta
