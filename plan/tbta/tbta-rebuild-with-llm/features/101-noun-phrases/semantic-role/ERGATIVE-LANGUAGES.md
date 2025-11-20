# Ergative Languages: Semantic Role Patterns

This document provides detailed examples of how semantic role affects translation in ergative and split-ergative languages.

---

## Understanding Ergativity

### Accusative vs. Ergative Alignment

**Accusative Languages (English, Greek, Hebrew, Latin, German):**
- **S** (intransitive subject) = **A** (transitive agent) → Same case (nominative)
- **O** (transitive object) = different case (accusative)
- Pattern: **S=A** vs. **O**

**Ergative Languages (Basque, Georgian, K'iche', Dyirbal):**
- **S** (intransitive subject) = **O** (transitive patient) → Same case (absolutive)
- **A** (transitive agent) = different case (ergative)
- Pattern: **S=O** vs. **A**

**Why Semantic Role Matters:**
- Accusative languages mark Patient differently from Agent/Theme
- Ergative languages mark Agent differently from Patient/Theme
- Same Greek subject can map to different cases in ergative languages!

---

## Basque (euskara)

**Alignment:** Pure ergative-absolutive

**Case System:**
- **Absolutive** (unmarked or -a): Patient and intransitive subject (Theme)
- **Ergative** (-k): Agent of transitive verbs
- **Dative** (-ri): Beneficiary, Experiencer (with some verbs)

### Example 1: Transitive Verb

**John 3:16** - "God loved the world"

**Greek:** ὁ θεός (nom.) ἠγάπησεν τὸν κόσμον (acc.)
**Basque:** Jainkoak (erg.) mundua (abs.) maite izan zuen

- **Jainkoak**: God + ergative -k (Agent)
- **mundua**: world + absolutive -a (Patient)
- **maite izan zuen**: loved (past) - agrees with absolutive mundua

**Semantic Role Analysis:**
- God → Agent → Ergative case required
- world → Patient → Absolutive case required

---

### Example 2: Intransitive Verb

**John 1:14** - "The Word became flesh"

**Greek:** ὁ λόγος (nom.) σὰρξ (nom.) ἐγένετο
**Basque:** Hitza (abs.) haragi bihurtu zen

- **Hitza**: Word + absolutive -a (Theme, not Agent)
- **haragi**: flesh (predicate nominative)
- **bihurtu zen**: became - agrees with absolutive Hitza

**Semantic Role Analysis:**
- Word → Theme (undergoes change, not volitional agent) → Absolutive case

**Translation Impact:**
- If translator incorrectly assigns Agent role → would use ergative Hitzak
- But "become" is change-of-state (Theme), not volitional action (Agent)
- Correct: Absolutive case

---

## Georgian (ქართული)

**Alignment:** Split ergative (changes by tense)

**Present Tense:** Nominative-accusative alignment
**Aorist (past) Tense:** Ergative-absolutive alignment

**Case System:**
- **Nominative** (-i in present): Subject
- **Ergative** (-ma in past): Agent of transitive verbs (aorist series)
- **Dative** (-s): Experiencer, Beneficiary, Patient in aorist

### Example: Matthew 2:11 - "They saw the child"

**Present Tense (if ongoing):**
- isini (nom.) khedebs (sees) bavshvs (dat.)
- They-NOM see child-DAT
- Alignment: Nominative-accusative

**Aorist (past, completed):**
- mat (erg.) nakhes (saw) bavshvi (nom.)
- They-ERG saw child-NOM
- Alignment: Ergative-absolutive

**Semantic Role Analysis:**
- "They" → Experiencer (perception verb, not volitional agent)
- "child" → Stimulus

**Translation Impact:**
- Tense determines case system!
- Past tense: Experiencer takes ergative (mat)
- Present tense: Experiencer takes nominative (isini)
- Semantic role + tense → case selection

---

## K'iche' Maya (K'iche')

**Alignment:** Ergative-absolutive

**Verb Agreement:**
- **Ergative markers** (Set A): Prefix on verb for Agent (transitive)
- **Absolutive markers** (Set B): Suffix on verb for Patient (transitive) or Subject (intransitive)

**Pronominal System:**
- Set A (ergative): nu- (1sg), a- (2sg), u- (3sg)
- Set B (absolutive): -in (1sg), -at (2sg), -∅ (3sg)

### Example 1: Transitive Verb

**John 3:16** - "God loved the world"

**K'iche':** X-u-loq'oj ri Dios ri uwachulew
- X- (aspect marker: completive)
- u- (Set A ergative 3sg: his/her/its = God)
- loq'oj (love)
- -∅ (Set B absolutive 3sg: it = world, zero-marked)
- ri Dios (the God - Agent)
- ri uwachulew (the world - Patient)

**Semantic Role Analysis:**
- God → Agent → Ergative prefix u-
- world → Patient → Absolutive suffix -∅

---

### Example 2: Intransitive Verb

**John 1:14** - "The Word became flesh"

**K'iche':** X-∅-uxlan ri Tzij pa tyoꞌjal
- X- (completive aspect)
- ∅- (Set A: no ergative prefix - intransitive)
- uxlan (became)
- -∅ (Set B absolutive 3sg: it = Word)
- ri Tzij (the Word - Theme)

**Semantic Role Analysis:**
- Word → Theme (not Agent) → Only absolutive marking, no ergative
- Intransitive verb → Only Set B agreement

**Translation Impact:**
- If translator mistakenly assigns Agent role → would add ergative prefix
- Correct: Theme role → intransitive construction, absolutive only

---

## Dyirbal (Australian Aboriginal)

**Alignment:** Syntactic ergativity (rare and complex)

**Case System:**
- **Absolutive** (-∅): S and O
- **Ergative** (-ŋgu): A
- **Dative** (-gu): Indirect object, Beneficiary

**Syntactic Ergativity:**
- In subordinate clauses, only absolutive NPs can be omitted (S and O, not A)
- This is extremely rare cross-linguistically

### Example: "The man saw the woman"

**Dyirbal:** Bayi yara-∅ baŋgul yaṛa-ŋgu buṛan
- bayi yara-∅: the man-ABS (Patient/Stimulus)
- baŋgul yaṛa-ŋgu: the woman-ERG (Experiencer/Agent-like)
- buṛan: saw

**Semantic Role Analysis:**
- Dyirbal treats Experiencer like Agent in some constructions
- "see" takes ergative-marked Experiencer
- Seen entity (Stimulus) → absolutive

**Translation Impact:**
- Requires careful Experiencer vs. Agent distinction
- Perception verbs pattern with transitive action verbs

---

## Tongan (Polynesian)

**Alignment:** Ergative-absolutive

**Case Markers:**
- **Absolutive**: 'a (proper nouns), he/e (common nouns)
- **Ergative**: 'e (marks Agent)
- **Dative**: kia/ki (Beneficiary, Goal)

### Example: Acts 2:38 - "Peter said to them"

**Tongan:** Pea pehē 'e Pita kiate kinautolu
- Pea pehē: and said
- 'e Pita: ERG Peter (Agent - speaker)
- kiate kinautolu: to them (Goal/Beneficiary)

**Semantic Role Analysis:**
- Peter → Agent → Ergative marker 'e
- them → Goal/Beneficiary → Dative marker kiate

---

## Hindi/Urdu (Split Ergativity)

**Alignment:** Split ergative (perfective aspect only)

**Simple Past (Perfective):** Ergative-absolutive
**Present/Imperfective:** Nominative-accusative

**Case System:**
- **Ergative** (-ne): Agent in perfective transitive
- **Nominative** (-∅): Subject in present, S and O in perfective
- **Accusative** (-ko): Definite/animate objects

### Example: John 1:14 - "We saw his glory"

**Hindi (Perfective):**
- ham-ne (we-ERG) us-kii mahimaa (his glory-NOM) dekhii (saw-FEM.SG)
- ham-ne: we + ergative -ne (Agent/Experiencer)
- mahimaa: glory + nominative (Stimulus, feminine)
- dekhii: saw (agrees with Stimulus "glory" in gender/number, not with Agent)

**Hindi (Imperfective/Present):**
- ham (we-NOM) us-kii mahimaa (his glory-ACC/NOM) dekhte haiṅ
- No ergative case in present tense
- Nominative-accusative alignment

**Semantic Role Analysis:**
- "we" → Experiencer
- "glory" → Stimulus
- Perfective aspect → Experiencer takes ergative case
- Imperfective aspect → Experiencer takes nominative case

**Translation Impact:**
- Aspect + semantic role → case selection
- Verb agrees with Stimulus (Patient), not Experiencer (Agent-like)

---

## Translation Implications Summary

### Critical Distinctions for Ergative Languages

1. **Agent vs. Theme in Subjects**
   - Greek/Hebrew nominative subject ≠ automatic ergative case
   - Volitional action (Agent) → Ergative
   - Change-of-state/motion (Theme) → Absolutive

2. **Experiencer Treatment**
   - Perception verbs (see, hear, know)
   - Some ergative languages treat Experiencer like Agent (ergative case)
   - Others treat Experiencer differently (dative, special construction)

3. **Verb Agreement**
   - Ergative languages often agree with absolutive (Patient/Theme), not ergative (Agent)
   - Translator must identify correct semantic role to set agreement

4. **Split Ergativity Triggers**
   - Aspect: Perfective vs. imperfective (Hindi/Urdu)
   - Tense: Past vs. non-past (Georgian)
   - Person: 1st/2nd vs. 3rd (some Australian languages)
   - Semantic role determines case ONLY in ergative context

5. **Passive-like Constructions**
   - Antipassive: Demotes Patient, promotes Agent to absolutive
   - Needed when absolutive NP must be syntactic pivot (Dyirbal)
   - Semantic role identification enables antipassive selection

---

## Validation Strategy for Ergative Languages

**Test Verses:**
1. High-volition transitive (Jesus heals) → Agent + Patient
2. Low-volition transitive (see, hear) → Experiencer + Stimulus
3. Change-of-state intransitive (become, arise) → Theme
4. Motion intransitive (go, come) → Theme + Goal/Source
5. Passive constructions → Patient as subject (absolutive)

**Expected Mappings:**
- Agent → Ergative case (or nominative in split-erg non-erg context)
- Patient → Absolutive case (or accusative in split-erg non-erg context)
- Theme → Absolutive case (or nominative if subject)
- Experiencer → May vary (ergative, dative, or nominative)

**Cross-check Against:**
- Published Basque Bible (Navarro-Labourdin translation)
- Published Georgian Bible
- Published K'iche' Maya Bible (SIL)
- Verify case marking aligns with predicted semantic roles

---

## Language Family Coverage

**Ergative language families:**
- **Kartvelian**: Georgian, Mingrelian, Laz, Svan
- **Basque**: Isolate (no relatives)
- **Mayan**: K'iche', Kaqchikel, Q'eqchi', Yucatec, ~30 languages
- **Polynesian**: Tongan, Samoan, Maori, Hawaiian (some have ergative features)
- **Australian**: Dyirbal, Warlpiri, Arrernte, ~200 languages
- **Caucasian**: Avar, Chechen, Ingush, Lezgian
- **Tibeto-Burman**: Nepali (split), Dzongkha, some Tibetan dialects
- **Inuit-Yupik**: Greenlandic, Inuktitut
- **Sumerian**: Ancient (extinct, but studied)

**Total speakers:** ~50-100 million Bible users (conservative estimate)
**Translation priority:** High for indigenous/minority language translation

---

**Document Status:** Production-ready
**Last Updated:** 2025-11-07
**Purpose:** Detailed ergative language patterns for semantic role feature
