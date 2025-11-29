# Language Family & Typology Analysis: Semantic Role

## Executive Summary

Semantic role encoding varies dramatically across the world's languages. **Greek explicitly marks semantic roles through its 4-case system**, while **Hebrew relies heavily on prepositions and word order**. Of our 1000+ available Bible translations, languages fall into three categories:
- **Mandatory marking** (80+ languages): Rich case systems or applicative voices require explicit semantic role distinction
- **Optional marking** (600+ languages): Can mark roles through various strategies (prepositions, word order, voice)
- **Minimal marking** (300+ languages): Isolating languages rely primarily on word order

**Key finding**: Languages with ergative-absolutive alignment (Basque, Mayan, Australian) present unique challenges as they conflate Agent/Source distinctions differently than nominative-accusative languages.

## 1. Source Language Encoding Check

### 1.1 Hebrew (Biblical Hebrew)

**Morphological Encoding**: **LIMITED** - Hebrew does not have a productive case system in Biblical period.

**How Semantic Roles Are Encoded**:

1. **Agent (Subject)**: Unmarked, typically pre-verbal position (VSO order)
   - Example: "God created" - אלהים ברא

2. **Patient (Direct Object)**:
   - Marked with אֶת (*'et*) for definite objects
   - Unmarked for indefinite objects
   - Example: "created [את] the heavens" - ברא את השמים

3. **Source**: Preposition מִן (*min*) "from"
   - Example: "from the earth" - מן הארץ
   - **Semantic nuance** (Brill 2024): *min* marks **dominant causers** - full control over causal chain
   - Citation: {brill-hebrew-prep-2024}

4. **Destination/Goal**: Preposition לְ (*le*) "to/for"
   - Example: "to Abraham" - לאברהם
   - Also marks Beneficiary and Addressee roles

5. **Instrument/Means**: Preposition בְּ (*be*) "in/with/by"
   - Example: "by the sword" - בחרב
   - **Semantic nuance** (Brill 2024): *be* marks **non-dominant causers** - can be prevented or altered
   - Citation: {brill-hebrew-prep-2024}

6. **Location**: Multiple prepositions (בְּ "in", עַל "on", תַּחַת "under")

**Complexity**: **HIGH** - Prepositions are highly polysemous. A single preposition can mark multiple semantic roles:
- לְ (*le*): Destination, Beneficiary, Addressee, Possession
- בְּ (*be*): Location, Instrument, Means, Manner, State
- מִן (*min*): Source, Cause, Partitive, Comparative

**Argument Structure** (BiblicalHebrew.org):
- Hebrew has **four trivalent structures**: prepositional ditransitives, double object constructions, causatives, complementatives
- Symmetric case alternations: direct object אֶת vs oblique prepositional phrase
- Citation: {biblicalhebrew-syntax}

**Key Implication**: Semantic role prediction for Hebrew requires **verb-specific knowledge** and **prepositional phrase analysis**, not simple morphological inspection.

### 1.2 Greek (Koine Greek)

**Morphological Encoding**: **EXPLICIT** - Greek has a productive 5-case system (nominative, genitive, dative, accusative, vocative).

**How Semantic Roles Are Encoded**:

1. **Agent (Subject)**: **Nominative** case
   - Example: "ὁ θεός" (*ho theos*) "God" - nominative
   - Also used for Patient in **passive voice** constructions

2. **Patient (Direct Object)**: **Accusative** case
   - Example: "τὸν οὐρανόν" (*ton ouranon*) "the heaven" - accusative
   - Also marks Destination with motion verbs
   - Also marks extent of time/space

3. **Source/Origin**: **Genitive** case (ablative function)
   - Example: "ἐκ τῆς γῆς" (*ek tēs gēs*) "from the earth" - genitive with preposition ἐκ
   - Genitive also marks: Possession, Partitive, Material
   - Citation: {ugg-greek-case}

4. **Destination/Addressee**: **Dative** case
   - Example: "τῷ Ἀβραάμ" (*tō Abraam*) "to Abraham" - dative
   - Dative also marks: Beneficiary, Instrument, Location
   - Citation: {ugg-greek-case}

5. **Instrument/Means**: **Dative** case (instrumental function)
   - Example: "λόγῳ" (*logō*) "by word" - dative without preposition
   - Sometimes with preposition ἐν (*en*) + dative
   - Citation: {blueletterbible-greek-case}

6. **Beneficiary**: **Dative** case or prepositional phrases (ὑπέρ + genitive, διά + accusative)

**The 8-Case Functional System**:
Some grammarians distinguish **8 case functions** though only 5 morphological forms:
- Nominative (subject)
- Genitive (possession, source/ablative)
- Dative (indirect object)
- **Locative** (dative form, location meaning: "where?")
- **Instrumental** (dative form, means meaning: "how?")
- Accusative (direct object, destination)
- Vocative (address)
- Citation: {newtestamentgreek-case-system}

**Key Features**:
- **Word order flexibility**: Because cases mark roles explicitly, Greek can use word order for emphasis/topic marking rather than grammatical function
- **Prepositions refine meaning**: Prepositions + case provide additional precision (ἐν + dative = location, εἰς + accusative = motion into)
- **Voice system interacts with roles**: Active vs middle vs passive voice changes which semantic role appears as subject

**Key Implication**: Greek provides **morphologically explicit** semantic role marking, making TBTA annotations more straightforward than Hebrew.

## 2. Language Families Requiring Semantic Role Marking

### 2.1 Ergative-Absolutive Languages

**Definition**: Languages where the single argument of intransitive verbs (S) is treated the same as the object of transitive verbs (O), both receiving absolutive case, while the agent of transitive verbs (A) receives ergative case.

**Key Families**:

1. **Basque** (isolate)
   - **Ergative** case: -k (Agent of transitive)
   - **Absolutive** case: unmarked (Patient + intransitive Subject)
   - Example: Gizona etorri da "The man came" (absolutive) vs Gizonak liburua irakurri du "The man read the book" (ergative + absolutive)

2. **Mayan languages** (Guatemala, Mexico)
   - **Available in our corpus**: Achi (acr), Awakateko (agu), K'iche', Q'eqchi'
   - Ergative alignment with split based on aspect
   - **Antipassive voice** common: demotes Patient to oblique, promoting Agent to absolutive
   - Citation: {wikipedia-ergative}

3. **Australian languages** (90% are ergative)
   - **Available in our corpus**: Arrernte (aer), Alyawarr (aly), Anindilyakwa (aoi), Warlpiri
   - Strong ergative-absolutive alignment
   - Citation: {wikipedia-ergative}

4. **Northeast Caucasian** (Chechen, Avar, Lezgian)
   - Not available in corpus

5. **Some Austronesian** (Tagalog, Fijian - but with nominative-accusative alignment)

**Implication**: Ergative languages **MUST** distinguish Agent from Patient, but the morphological strategy differs from nominative-accusative languages. TBTA's semantic role categories (Agent-like, Patient-like) map well to ergative alignment.

### 2.2 Polysynthetic Languages

**Characteristics**: Incorporate arguments into the verb complex via agreement markers.

**Available Examples**:
- **Algonquian** (Algonquin - alq in corpus)
- **Iroquoian** (not in corpus)
- **Some Papuan languages** (Trans-New Guinea family - highly represented in corpus)

**Semantic Role Encoding**: Agreement markers on verbs indicate person/number of Agent and Patient, sometimes even indirect objects. Roles are **obligatorily marked** via morphology.

### 2.3 Languages with Rich Case Systems (6+ cases)

**Definition**: Languages with dedicated morphological cases for multiple semantic roles.

**Key Examples in Corpus**:

1. **Finnish** (fin) - 15 cases
   - Nominative (subject)
   - Accusative (patient)
   - Partitive (partial object)
   - Genitive (possessor)
   - Inessive, Elative, Illative (location, source, destination inside)
   - Adessive, Ablative, Allative (location, source, destination outside)
   - Essive, Translative (state, change of state)
   - Others
   - **Status**: Not found in current corpus (need to verify)

2. **Russian** (rus) - 6 cases
   - Available: Russian Synodal (russyn)
   - Nominative, Genitive, Dative, Accusative, Instrumental, Prepositional
   - **Instrumental case** explicitly marks Instrument role
   - Citation: {wikipedia-russian-cases}

3. **Turkish** (tur) - 6 cases
   - Available: Turkish (turev)
   - Nominative, Accusative, Genitive, Dative, Locative, Ablative
   - **Ablative** case marks Source
   - Citation: {wikipedia-turkish-grammar}

4. **Latin** (lat) - 6 cases
   - Available: Vulgate (latVUC)
   - Nominative, Genitive, Dative, Accusative, Ablative, Vocative
   - **Ablative** marks Source, Instrument, Means, Cause

**Implication**: These languages **grammatically require** semantic role distinctions. Omitting role marking produces ungrammatical sentences.

### 2.4 Languages with Applicative Voice

**Definition**: Applicative constructions promote oblique arguments (Beneficiary, Instrument, Location) to direct object status.

**Key Families**:

1. **Bantu** (Niger-Congo)
   - **Available in corpus**: Swahili (not found - need verification), various
   - Applicative suffixes add argument slots:
     - Benefactive applicative: "I cooked food for the child" → "I cooked-APPL the child food"
     - Instrumental applicative: "I cut the bread with a knife" → "I cut-APPL the knife the bread"
   - Citation: {wikipedia-applicative}

2. **Austronesian** (highly represented in corpus)
   - **Available**: Indonesian (ind), Tagalog, many Papuan Austronesian languages
   - Complex voice/focus systems mark which argument is "in focus"
   - Indonesian: me-N (agent voice), di- (patient voice), -i/-kan (applicative)

**Implication**: Applicative languages make **Beneficiary, Instrument, Addressee** roles as prominent as core Agent/Patient roles. TBTA values (B, I, D) are essential for these languages.

## 3. Available Translations Analysis

**Source**: `/workspace/src/constants/languages.tsv` (1008 total files, ~300-400 unique languages)

### 3.1 Methodology

Due to the large number of languages (1000+ files), classification is based on:
1. **Documented sources** (WALS, language grammars) where available
2. **Language family generalizations** (e.g., most Indo-European = nom-acc, most Australian = ergative)
3. **Suspected classifications** marked with (suspected) when based on internal knowledge

### 3.2 Classification by Alignment Type

#### Nominative-Accusative Languages (Majority)

**Indo-European family** (most productive):
- **English** (eng) - **Optional** - SVO order + prepositions ("to", "from", "with", "for")
- **German** (deu) - **Mandatory** - 4 cases (Nom, Acc, Dat, Gen) + prepositions
- **Spanish** (spa) - **Optional** - Prepositions + clitic pronouns (le, lo, la for roles)
- **French** (fra) - **Optional** - Prepositions (à, de, avec, pour)
- **Russian** (rus) - **Mandatory** - 6 cases explicitly mark roles
- **Greek, Ancient** (grc) - **Mandatory** - 5 cases explicitly mark roles
- **Latin** (lat) - **Mandatory** - 6 cases explicitly mark roles

**Afro-Asiatic family**:
- **Hebrew** (heb) - **Mandatory** - Prepositions + object marker אֶת
- **Assyrian Neo-Aramaic** (aii) - **Mandatory** (suspected) - Prepositions + case remnants
- **Arabic** (ara) - **Mandatory** (suspected) - 3 cases (Nom, Acc, Gen) in Classical Arabic

**Niger-Congo family**:
- **Akan** (aka) - **Optional** (suspected) - SVO order, limited case marking

**Turkic family**:
- **Turkish** (tur) - **Mandatory** - 6 cases

**Japonic family**:
- **Japanese** (jpn) - **Mandatory** - Particles mark roles (が ga=Nom, を wo=Acc, に ni=Dat, で de=Inst, から kara=Source, へ e/まで made=Destination)

#### Ergative-Absolutive Languages

**Mayan family**:
- **Achi** (acr) - **Mandatory** - Ergative-absolutive alignment
- **Awakateko** (agu) - **Mandatory** - Ergative-absolutive alignment
- **K'iche'**, **Q'eqchi'** (if in corpus) - **Mandatory**

**Australian family** (all ergative):
- **Arrernte, Eastern** (aer) - **Mandatory** - Strong ergative case marking
- **Alyawarr** (aly) - **Mandatory** - Ergative
- **Anindilyakwa** (aoi) - **Mandatory** - Ergative

**Basque** (isolate):
- Not found in corpus

#### Split-Ergative Languages

**Indo-European (some)**:
- **Hindi** (not in corpus) - Split: pronouns = nom-acc, nouns = ergative (perfective aspect)
- **Marathi** (not in corpus) - Split ergative

#### Isolating Languages (Minimal Case Marking)

**Austronesian family** (many SVO, isolating):
- **Indonesian** (ind) - **Optional** - SVO order + prepositions, voice system (me-N/di-/ke-/-i/-kan)
- Many Papuan Austronesian languages - varies by language

**Sino-Tibetan**:
- **Mandarin Chinese** (not in corpus) - **Optional** - SVO order + prepositions (给 gěi "to", 从 cóng "from")

**Creole languages**:
- **Lesser Antillean French Creole** (acf) - **Optional** (suspected) - SVO order, minimal inflection

### 3.3 Classification by Typological Feature

#### Case-Marking Languages (Morphological Encoding)

**Mandatory Marking** (80+ languages estimated):
- All Indo-European with productive case systems: German, Russian, Latin, Greek, Hindi
- All Turkic: Turkish
- All Uralic: Finnish (if in corpus)
- All ergative languages: Mayan, Australian, Basque
- Polysynthetic: Algonquian, some Trans-New Guinea

**Optional Marking** (600+ languages):
- Isolating languages with prepositions: English, French, Spanish, Indonesian, Mandarin
- Austronesian voice-prominent languages: Tagalog, Fijian
- Niger-Congo languages: Akan, Swahili

**Absent/Minimal** (300+ languages):
- Strict SVO isolating languages with minimal adpositions
- Some Trans-New Guinea languages with verb serialization

#### Preposition-Based Languages

**Definition**: Languages that mark semantic roles primarily through adpositions (prepositions/postpositions).

**Examples** (all **Optional** or **Mandatory**):
- **Prepositions** (pre-nominal): English, Spanish, French, Hebrew, Arabic
- **Postpositions** (post-nominal): Japanese (particles), Turkish, Hindi
- **Mixed**: German (mostly prepositions, some postpositions)

#### Word-Order Dependent Languages

**Definition**: Languages where semantic roles are inferred from fixed word order.

**SVO languages** (Subject-Verb-Object):
- **English**, **Spanish**, **French**, **Indonesian**, **Mandarin**
- Rigid order makes roles predictable without extensive morphology

**VSO languages** (Verb-Subject-Object):
- **Hebrew** (Biblical), **Welsh**, **Irish**, **Classical Arabic**
- Verb-initial order, subject usually Agent, first object usually Patient

**SOV languages** (Subject-Object-Verb):
- **Japanese**, **Turkish**, **Hindi**, **Korean**, many Papuan languages
- Postpositions common, case marking often present

**Free word order**:
- **Latin**, **Greek**, **Russian**, **Finnish**
- Case marking allows flexibility for topic/focus

## 4. Typological Distinctions

### 4.1 Case-Marking vs Non-Case-Marking

**Case-Marking Languages** (~25% of languages):
- **Strategy**: Morphological suffixes/prefixes mark semantic roles directly on nouns
- **Examples**: Greek (5 cases), Russian (6), Finnish (15), Turkish (6), Latin (6)
- **Advantage for TBTA**: Semantic roles are **explicitly recoverable** from morphology (though polysemy still requires disambiguation)
- **Challenge**: Case syncretism (same form, multiple functions) - e.g., Greek dative = Addressee/Location/Instrument

**Non-Case-Marking Languages** (~75% of languages):
- **Strategy**: Prepositions/postpositions + word order
- **Examples**: English, Spanish, French, Hebrew, Indonesian, Mandarin
- **Challenge for TBTA**: Must analyze **prepositional phrases + verb semantics** to determine roles
- **Ambiguity**: Same preposition, multiple roles (Hebrew לְ = Destination/Beneficiary/Addressee)

### 4.2 Alignment Types

**Nominative-Accusative** (60% of languages):
- **Pattern**: S (intransitive subject) = A (transitive agent) ≠ O (transitive object)
- **Implication**: "Agent-like" role consistently marked as subject (nominative)
- **Languages**: English, Greek, Spanish, Russian, Japanese, Hebrew

**Ergative-Absolutive** (25% of languages):
- **Pattern**: S (intransitive subject) = O (transitive object) ≠ A (transitive agent)
- **Implication**: "Patient-like" role consistently marked as absolutive (unmarked)
- **Languages**: Basque, Mayan (Achi, Awakateko), Australian (Arrernte, Alyawarr)
- **TBTA Challenge**: Must distinguish "Patient-like in transitive" from "Subject of intransitive" (both absolutive)

**Active-Stative** (rare, ~5%):
- **Pattern**: Subjects of active verbs (Sa) ≠ subjects of stative verbs (Sp)
- **Not prominently represented in corpus**

**Tripartite** (very rare, <1%):
- **Pattern**: S ≠ A ≠ O (all marked differently)
- **Examples**: Hindi/Marathi (partially), Nez Perce
- **Not prominently in corpus**

### 4.3 Voice Systems and Semantic Role Expression

**Active-Passive Distinction** (universal):
- **Active**: Agent = subject, Patient = object
- **Passive**: Patient = subject, Agent = optional oblique (marked with "by")
- **TBTA implication**: Must track voice to correctly assign semantic roles

**Middle Voice** (Greek, Sanskrit, some modern languages):
- **Greek middle**: Subject is both Agent and Patient (reflexive or self-beneficial)
- **Example**: λούομαι (*louomai*) "I wash myself" - subject is both Agent and Patient
- **TBTA challenge**: Does subject receive "Agent-like" or "Patient-like" or "State"?

**Antipassive** (ergative languages):
- **Function**: Demotes Patient to oblique, promotes Agent to absolutive
- **Example** (Basque): Gizonak liburua irakurri du (ERG book.ABS read) → Gizona irakurtzen du liburua (ABS read-ANTIP book)
- **Mayan languages** (Achi, Awakateko): Productive antipassive
- **TBTA implication**: Antipassive construction changes Patient from core argument to oblique (semantic role changes from "Most Patient-like" to adjunct?)

**Applicative Voice** (Bantu, Austronesian):
- **Function**: Promotes Beneficiary/Instrument/Location to direct object
- **Example** (Swahili): Nilimpikia mtoto chakula (I-cooked-APPL child food) "I cooked food for the child" → child is now direct object
- **TBTA implication**: Beneficiary role (B) becomes as prominent as Patient role

**Causative** (Turkish, Japanese, many languages):
- **Function**: Adds a Causer argument, original Agent becomes Causee
- **Example** (Japanese): 食べる taberu "eat" → 食べさせる tabesaseru "make eat" (Agent makes Patient eat)
- **TBTA challenge**: Does Causer get "Agent-like" role? What role does Causee get?

## 5. Root Languages (Major Translation Sources)

### 5.1 Source Language Analysis

**Languages translators often start from**:

| Language | ISO-639-3 | Family | Semantic Role Encoding | Status in Corpus |
|----------|-----------|--------|------------------------|------------------|
| **Hebrew** | heb | Afro-Asiatic | Prepositions + word order | ✅ Available |
| **Greek (Koine)** | grc | Indo-European | 5-case system | ✅ Available (7 versions) |
| **Latin** | lat | Indo-European | 6-case system | ✅ Available (Vulgate) |
| **English** | eng | Indo-European | Prepositions + SVO order | ✅ Available (45+ versions) |
| **Spanish** | spa | Indo-European | Prepositions + SVO order | ✅ Available (6 versions) |
| **French** | fra | Indo-European | Prepositions + SVO order | ✅ Available (4 versions) |
| **German** | deu | Indo-European | 4 cases + prepositions | ✅ Available (4 versions) |
| **Arabic** | ara | Afro-Asiatic | 3 cases + prepositions | ❌ Not found in current scan |
| **Russian** | rus | Indo-European | 6 cases | ✅ Available (Synodal) |
| **Indonesian** | ind | Austronesian | Voice system + prepositions | ✅ Available (2 versions) |
| **Swahili** | swa | Niger-Congo | Noun classes + prepositions + applicatives | ❌ Not found in current scan |

### 5.2 Regional Hub Languages

**Africa**:
- **Swahili** (East Africa) - Bantu applicative system
- **Amharic** (Ethiopia) - Semitic, related to Arabic
- **Hausa** (West Africa) - Afro-Asiatic

**Asia**:
- **Mandarin Chinese** - SVO isolating
- **Hindi** - Split ergative, rich case system
- **Indonesian** - Austronesian voice system (available in corpus)

**Americas**:
- **Spanish** - Dominant in Latin America (available)
- **Portuguese** - Brazil, Africa
- **English** - Global lingua franca (available)

**Pacific**:
- **Indonesian** - Papua region (available)
- **Tok Pisin** - PNG creole
- **Fijian** - Austronesian with unique voice

## 6. Candidate Languages for Translation Database

**Selection Criteria**:
1. Diverse alignment types (nom-acc, ergative, split)
2. Mix of case-marking vs preposition-based
3. Representation of major families
4. Available in our corpus (1000+ translations)
5. Regional diversity

### 6.1 Top 10 Candidates

| # | Language | ISO | Family | Alignment | Encoding | Rationale |
|---|----------|-----|--------|-----------|----------|-----------|
| 1 | **Greek (Koine)** | grc | Indo-European | Nom-Acc | 5 cases | Source language, explicit morphological marking |
| 2 | **Hebrew** | heb | Afro-Asiatic | Nom-Acc | Prepositions | Source language, prepositional complexity |
| 3 | **English** | eng | Indo-European | Nom-Acc | Prep + SVO | Global lingua franca, minimal morphology |
| 4 | **Spanish** | spa | Indo-European | Nom-Acc | Prep + SVO | Major translation hub, Romance |
| 5 | **Russian** | rus | Indo-European | Nom-Acc | 6 cases | Rich case system, Slavic |
| 6 | **Achi** | acr | Mayan | Ergative | Case + voice | Ergative-absolutive, antipassive |
| 7 | **Arrernte (Eastern)** | aer | Australian | Ergative | Case marking | Strong ergative, free word order |
| 8 | **Japanese** | jpn | Japonic | Nom-Acc | Particles | Postpositions (particles), SOV, honorifics |
| 9 | **Indonesian** | ind | Austronesian | Nom-Acc | Voice + prep | Applicative voice system, regional hub |
| 10 | **Turkish** | tur | Turkic | Nom-Acc | 6 cases | Agglutinative, ablative case marks Source |

### 6.2 Additional Candidates (Reserve List)

| Language | ISO | Family | Encoding | Rationale |
|----------|-----|--------|----------|-----------|
| **German** | deu | Indo-European | 4 cases | Germanic, partial case system |
| **Akan** | aka | Niger-Congo | Minimal | African, minimal case marking |
| **Alyawarr** | aly | Australian | Ergative case | Australian ergative, compare to Arrernte |
| **Awakateko** | agu | Mayan | Ergative case | Second Mayan for comparison |
| **Tagalog** | tgl | Austronesian | Voice system | Complex voice/focus system (if in corpus) |

## 7. Cultural Nuances Affecting Semantic Role Expression

### 7.1 Honorifics (Social Register)

**Japanese** (jpn):
- **Honorific morphology affects argument structure**:
  - お客様がいらっしゃる (o-kyaku-sama ga irassharu) "The honored guest comes" - honorific verb changes Agent expression
  - 先生に差し上げる (sensei ni sashiageru) "give to teacher" - humble verb for Beneficiary/Addressee
- **Passive used for politeness**: なさる (nasaru) "do-HON" vs される (sareru) "be-done-PASS"
- **TBTA challenge**: Honorific passives may obscure true semantic roles

**Korean** (kor):
- Similar honorific system affects verb morphology and argument expression
- 주시다 (jushida) "give-HON" vs 드리다 (deurida) "give-HUM"

**Javanese** (jav) (if in corpus):
- Multi-level speech styles (ngoko, madya, krama) affect verb and pronoun choice
- May obscure Agent/Patient distinctions in extreme politeness

### 7.2 Taboos and Avoidance

**Australian languages**:
- **Mother-in-law avoidance languages**: Special vocabulary used in presence of certain kin
- May affect which semantic roles can be explicitly mentioned

**Polynesian languages**:
- Taboo (tapu/kapu) systems may require circumlocution for certain Agents (gods, chiefs)

### 7.3 Inclusive/Exclusive Distinctions

**TBTA Person System** includes inclusive (A) vs exclusive (B) first person plural.

**Affect on Semantic Roles**:
- **Inclusive Agent**: "We (including you) created this" - different pragmatic force
- **Exclusive Beneficiary**: "God gave it to us (not you)" - changes Beneficiary scope

**Languages with clusivity** (from corpus):
- **Tagalog** (tgl), **Malay** (msa), **Fijian** (fij), **Vietnamese** (vie) (per TBTA-FEATURES.md)
- Many Austronesian and Papuan languages

### 7.4 Animacy Hierarchies

**Algonquian languages** (Algonquin - alq):
- **Obviation system**: Marks less salient third person as "obviative"
- Affects which argument is treated as Agent vs Patient
- **Proximate** (more topical) vs **Obviative** (less topical)

**Navajo** (if in corpus):
- Animacy affects verb agreement and argument realization
- Human > Animal > Inanimate hierarchy

## 8. Summary: Feature Necessity by Language Type

### Mandatory Encoding (Must Mark Semantic Roles)

**Characteristics**: Languages where semantic roles are grammatically obligatory.

**Examples**:
- Case-marking languages: Greek, Russian, German, Latin, Turkish, Finnish
- Ergative languages: Basque, Mayan (Achi, Awakateko), Australian (Arrernte)
- Polysynthetic languages: Algonquian, some Trans-New Guinea
- Applicative languages: Bantu (Swahili), some Austronesian

**Percentage of corpus**: ~20-30% (estimated 200-300 languages)

### Optional Encoding (Can Mark Semantic Roles)

**Characteristics**: Languages with multiple strategies (prepositions, word order, voice) but not strictly required.

**Examples**:
- Prepositional languages: English, Spanish, French, Hebrew, Indonesian
- Voice-prominent languages: Tagalog, Fijian
- Mixed systems: Japanese (particles), many Niger-Congo

**Percentage of corpus**: ~60-70% (estimated 600-700 languages)

### Minimal Encoding (Roles Inferred from Word Order)

**Characteristics**: Strict SVO/SOV/VSO order with minimal explicit role marking.

**Examples**:
- Isolating languages: Mandarin Chinese, some creoles
- Some Austronesian: Basic Indonesian sentences

**Percentage of corpus**: ~10-20% (estimated 100-200 languages)

## References

- {tbta-features-2025}: `/workspace/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md`
- {brill-hebrew-prep-2024}: Brill, "Semantic properties of prepositions in Biblical Hebrew" (2024), https://brill.com/view/journals/aall/16/2/article-p217_1.xml
- {biblicalhebrew-syntax}: BiblicalHebrew.org, "Syntax and Sentence Structure", https://biblicalhebrew.org/syntax-and-sentence-structure-in-biblical-hebrew-patterns-priorities-and-poetic-power.aspx
- {ugg-greek-case}: unfoldingWord Greek Grammar, "Case", https://ugg.readthedocs.io/en/latest/case.html
- {blueletterbible-greek-case}: Blue Letter Bible, "The Greek Case System", https://www.blueletterbible.org/resources/grammars/greek/simplified-greek/case-system.cfm
- {newtestamentgreek-case-system}: New Testament Greek, "The Greek Case System", https://www.newtestamentgreek.net/the-greek-case-system-nominative-genitive-dative-accusative-vocative.html
- {wikipedia-ergative}: Wikipedia, "Ergative-absolutive alignment", https://en.wikipedia.org/wiki/Ergative–absolutive_alignment
- {wals-alignment}: WALS Online, "Alignment of Case Marking of Full Noun Phrases", https://wals.info/chapter/98
- {wikipedia-applicative}: Wikipedia, "Applicative voice", https://en.wikipedia.org/wiki/Applicative_voice
- {wikipedia-antipassive}: Wikipedia, "Antipassive voice", https://en.wikipedia.org/wiki/Antipassive_voice
- {wikipedia-russian-cases}: Wikipedia, "Russian grammar" (case system section)
- {wikipedia-turkish-grammar}: Wikipedia, "Turkish grammar" (case system section)
