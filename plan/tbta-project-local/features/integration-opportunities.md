# TBTA Integration Opportunities

**Purpose:** Analyze how TBTA integrates with our broader myBibleToolbox ecosystem, focusing on PRACTICAL integration patterns.

**Status:** Initial analysis based on:
- `/home/user/mybibletoolbox-code/plan/tbta-analysis.md`
- `/home/user/mybibletoolbox-code/src/ingest-data/macula/README.md`
- `/home/user/mybibletoolbox-code/SCHEMA.md`

---

## 1. TBTA + Macula: Merging Word-Level + Clause-Level

### Complementary Layers

**Macula provides:**
- **Word-level morphology** - case, tense, voice, mood, gender, number
- **Lexical references** - Strong's numbers, lemmata
- **Semantic domains** - Louw-Nida (Greek), SDBH (Hebrew)
- **Syntactic roles** - subject, object, predicate
- **Scholarly precision** - based on academic datasets

**TBTA provides:**
- **Clause-level pragmatics** - speaker/listener demographics, speech style
- **Discourse tracking** - participant flow (introduced, routine, exiting, restaging)
- **Cross-linguistic categories** - trial number, inclusive/exclusive person, proximity distinctions
- **Entity disambiguation** - noun list indexing (which "he" = which referent)
- **Implicit information** - what can be inferred vs. must be stated

### Integration Strategy

**Merge at verse level** - Each verse YAML contains both datasets:

```yaml
verse: GEN.001.026

# MACULA DATA: Word-level linguistic analysis
words:
  - position: 1
    text: "וַיֹּ֣אמֶר"
    lemma: "אָמַר"
    strongs: H559
    morphology:
      pos: verb
      stem: qal
      tense: imperfect
      person: 3
      number: singular
    gloss: "said" {macula-hebrew}

  - position: 2
    text: "אֱלֹהִ֔ים"
    lemma: "אֱלֹהִים"
    strongs: H430
    morphology:
      pos: noun
      number: plural  # MACULA: grammatical plural
      state: absolute
    gloss: "God" {macula-hebrew}
    semantic:
      sdbh: ["009685001001000"]
      coredomain: ["142"]

# TBTA DATA: Clause-level pragmatics & discourse
tbta_clauses:
  - id: god-said
    span: [1, 2]

    participant_tracking:
      - entity: "God"
        noun_index: "1"
        status: "routine"  # Established in narrative
        first_mention: "GEN.001.001"

    discourse:
      number: "trial"  # ⭐ Exactly 3 persons (Trinity)
      person: "first_inclusive"  # ⭐ "we" including those addressed

    speaker_demographics:
      speaker: "God"
      listener: "Trinity members"  # Father addressing Son/Spirit
      relationship: "divine_persons"
      speech_style: "formal"
      attitude: "deliberative"

    cross_linguistic:
      implications:
        - category: "number_system"
          note: |
            Languages with trial number (Austronesian, Polynesian) should use trial
            form, not generic plural. This is theologically significant - exactly
            3 divine persons. {tbta}

        - category: "person_system"
          note: |
            Languages with inclusive/exclusive distinction (Tagalog, Malay, Fijian)
            should use inclusive "we" - speaker includes addressees. {tbta}
```

**Key Integration Points:**

1. **Macula `morphology.number: plural`** + **TBTA `discourse.number: trial`**
   - Macula: grammatical analysis (Hebrew plural verb form)
   - TBTA: semantic interpretation (exactly 3 persons intended)
   - **Integration:** Grammatical plural → semantic trial for translation

2. **Macula `semantic.domain`** + **TBTA `cross_linguistic.implications`**
   - Macula: what semantic field the word belongs to
   - TBTA: how that semantic field maps across language typologies
   - **Integration:** Domain + typology = translation guidance

3. **Macula `syntax.role`** + **TBTA `participant_tracking`**
   - Macula: grammatical function (subject, object)
   - TBTA: discourse status (first mention, routine, exiting)
   - **Integration:** Grammar + discourse = entity tracking

---

## 2. Verse-Level Integration: One YAML with Both Datasets

### Proposed YAML Structure

**Yes, one file can have both.** Use separate top-level sections:

```yaml
verse: JHN.011.035

source:
  language: GRC
  text: "ἐδάκρυσεν ὁ Ἰησοῦς" {grc-NA28-1993}

# ========== MACULA DATA ==========
macula:
  source: macula-greek
  version: 1.0.0

  words:
    - position: 1
      text: "ἐδάκρυσεν"
      lemma: "δακρύω"
      strongs: G1145

      morphology:
        pos: verb
        tense: aorist
        voice: active
        mood: indicative
        person: 3
        number: singular

      semantic:
        ln: "25.139"  # Louw-Nida: Sorrow, Regret
        domain: "025019"

      syntax:
        role: predicate
        clause: 1

    - position: 2
      text: "ὁ"
      lemma: "ὁ"
      strongs: G3588
      morphology:
        pos: article
        case: nominative
        number: singular
        gender: masculine
      syntax:
        role: determiner
        head: 3

    - position: 3
      text: "Ἰησοῦς"
      lemma: "Ἰησοῦς"
      strongs: G2424
      morphology:
        pos: noun
        proper: true
        case: nominative
        number: singular
      semantic:
        entity_type: person
      syntax:
        role: subject
        head: 1

# ========== TBTA DATA ==========
tbta:
  source: tbta-db-export
  version: 1.0.0

  clauses:
    - id: jesus-wept
      span: [1, 2, 3]

      participant_tracking:
        - entity: "Jesus"
          noun_index: "1"
          status: "routine"  # Established participant
          first_mention: "JHN.011.001"
          note: "Jesus has been present throughout chapter" {tbta}

      verb_encoding:
        time_granularity: "immediate_past"  # Just happened
        completion: "complete"
        duration: "momentary"

      emotional_context:
        type: "grief_expression"
        intensity: "moderate"  # δακρύω = silent tears, not κλαίω = loud wailing
        public_private: "public"  # Witnessed by others (v36)

      implicit_information:
        culturally_inferable:
          - "Jesus knows he will raise Lazarus (foreshadowed v11)"
          - "Tears are empathy/solidarity with Mary/Martha's grief"
        requires_explicit:
          - "Reason for tears (not stated in text)"

# ========== INTEGRATED ANALYSIS ==========
integration:
  merged_insights:
    - insight: |
        Macula: Aorist tense (ἐδάκρυσεν) = point action, completed event.
        TBTA: Time granularity = immediate past, momentary duration.
        Combined: Translate with simple past punctiliar aspect: "wept" (not "was weeping").
        {llm-cs45}

    - insight: |
        Macula: δακρύω (G1145) in LN domain 25.139 = silent tears/weeping.
        TBTA: Emotional intensity = moderate (contrasts with κλαίω in v33 = loud wailing).
        Combined: Use "wept" not "wailed" - controlled emotional expression.
        {llm-cs45}

    - insight: |
        Macula: Article ὁ makes Ἰησοῦς definite/emphatic subject.
        TBTA: Participant tracking = routine (established), noun_index "1".
        Combined: "Jesus" is clear subject, no ambiguity about who wept.
        {llm-cs45}
```

### Benefits of Single-File Integration

1. **No data duplication** - verse reference, source text stored once
2. **Easy comparison** - see Macula grammar vs TBTA pragmatics side-by-side
3. **Merged insights section** - explicit integration analysis
4. **Tool independence** - can query Macula-only, TBTA-only, or both
5. **Standard schema compliance** - follows SCHEMA.md structure

### Alternative: Separate Files with Cross-References

If files get too large:

```yaml
# JHN-011-035-macula.yaml
verse: JHN.011.035
source: macula-greek
# ... Macula data

# JHN-011-035-tbta.yaml
verse: JHN.011.035
source: tbta-db-export
related_data:
  macula: "JHN-011-035-macula.yaml"
# ... TBTA data

# JHN-011-035-integrated.yaml
verse: JHN.011.035
sources:
  - macula: "JHN-011-035-macula.yaml"
  - tbta: "JHN-011-035-tbta.yaml"
# ... Merged insights only
```

**Recommendation:** Start with single-file integration for simplicity, split only if files exceed ~500 lines.

---

## 3. Complementary Strengths: Concrete Examples

### Example 1: Genesis 1:26 - Trial Number + Morphology

**Verse:** "Let us make man in our image..."

**Macula provides:**
```yaml
words:
  - text: "נַֽעֲשֶׂ֥ה"
    lemma: "עָשָׂה"
    morphology:
      stem: qal
      tense: imperfect
      person: 1
      number: plural  # ⭐ Grammatical plural
    gloss: "let us make"
```

**TBTA provides:**
```yaml
discourse:
  number: "trial"  # ⭐ Exactly 3 persons (semantic)
  person: "first_inclusive"
  noun_index: "1"  # God as Trinity
```

**Why both are needed:**
- **Macula alone:** "Plural verb" - could be 2, 3, 10, 1000 persons
- **TBTA alone:** "Trial number" - but no grammatical verification
- **Together:** Hebrew grammar (plural) + semantic analysis (trial) + theological interpretation (Trinity)

**Translation impact:**
- **Polynesian languages** (trial number exists): Use trial form
- **English** (no trial): Use "we" with footnote explaining "three persons"
- **Morphologically rich languages**: Match Hebrew plural verb form

---

### Example 2: Genesis 4:8 - Participant Tracking + Syntax

**Verse:** "Cain said to Abel... and he rose up and he killed him"

**Macula provides:**
```yaml
words:
  - text: "קַ֔יִן"
    morphology:
      pos: noun
      proper: true
    syntax:
      role: subject
  - text: "הֶ֖בֶל"
    morphology:
      pos: noun
      proper: true
    syntax:
      role: object
```

**TBTA provides:**
```yaml
participant_tracking:
  - entity: "Cain"
    noun_index: "1"
    status: "routine"
    role: "agent"  # Doer of action
  - entity: "Abel"
    noun_index: "2"
    status: "exiting"  # Dies this verse
    role: "patient"  # Receiver of action
```

**Why both are needed:**
- **Macula alone:** Subject/object roles clear, but multiple pronouns later ("he... he... him") - which is which?
- **TBTA alone:** Noun indices show distinct entities, but no grammatical verification
- **Together:** Syntax (subject/object) + participant tracking (entity continuity) = clear referent chain

**Translation impact:**
- **Switch-reference languages** (Native American, Papua New Guinea): Mark same-subject vs different-subject
- **Pro-drop languages** (Spanish, Italian): Can omit pronouns, context clear from tracking
- **Explicit languages** (English): May need to repeat names for clarity

---

### Example 3: John 19:31 - Speaker Demographics + Semantic Domains

**Verse:** Older sister speaking to younger sister

**Macula provides:**
```yaml
semantic:
  ln: "33.79"  # Louw-Nida: Communication domain
  domain: "033079"
words:
  - text: "daughter"
    semantic:
      entity_type: person
      relationship: "familial"
```

**TBTA provides:**
```yaml
speaker_demographics:
  speaker: "daughter (older)"
  listener: "daughter (younger)"
  speaker_age: "young_adult_18_24"
  speaker_listener_age: "essentially_same_age"
  relationship: "sibling"
  speech_style: "informal"
  attitude: "neutral"
```

**Why both are needed:**
- **Macula alone:** Identifies speech act, family relationship domain
- **TBTA alone:** Age/relationship, but no semantic verification
- **Together:** Semantic field (communication/family) + pragmatics (age/register) = appropriate register

**Translation impact:**
- **Japanese/Korean**: Choose correct honorific level (siblings same age → casual form)
- **Javanese**: Select politeness register (same age → ngoko/low register)
- **European languages**: May add "sister" explicitly where English omits

---

### Example 4: Matthew 5:3 - Louw-Nida Domains + Cross-Linguistic Implications

**Verse:** "Blessed are the poor in spirit"

**Macula provides:**
```yaml
words:
  - text: "πτωχοὶ"
    lemma: "πτωχός"
    semantic:
      ln: "88.57"  # Domain 88.G "Humility" NOT economic poverty
      domain: "088057"
    morphology:
      case: nominative
      number: plural
```

**TBTA provides:**
```yaml
cross_linguistic:
  semantic_field: "humility_spiritual_poverty"
  implications:
    - category: "metaphorical_extension"
      note: |
        Many languages distinguish economic poverty (literal) from spiritual
        poverty (metaphorical). Greek πτωχός can be both, context determines.
        Here: spiritual humility, not economic state. {tbta}

    - category: "cultural_adaptability"
      note: |
        Cultures with strong honor/shame orientation may need to explicitly
        mark this as positive virtue, not negative status. {tbta}
```

**Why both are needed:**
- **Macula alone:** Louw-Nida 88.57 identifies semantic domain (humility), but doesn't guide cross-cultural mapping
- **TBTA alone:** Cross-linguistic implications, but no verification of which sense is intended
- **Together:** Semantic domain (humility) + cultural mapping = avoid mistranslation as economic poverty

**Translation impact:**
- **Languages with separate poverty words**: Choose humility/lowliness word, not economic poverty
- **Honor/shame cultures**: May add "those who humble themselves" to clarify positive virtue
- **Literal cultures**: May need footnote explaining metaphorical extension

---

## 4. Query Patterns: Combined Macula + TBTA Searches

### Query Pattern 1: Find verses with specific grammatical + discourse features

**Query:** "Find verses with trial number AND Louw-Nida domain 12.A (Supernatural Beings)"

```python
# Pseudo-code query
results = query_verses(
    tbta={
        "discourse.number": "trial"
    },
    macula={
        "semantic.ln": "12.*"  # Domain 12 = Supernatural Beings
    }
)

# Expected result: GEN.001.026
# - TBTA: number="trial" (3 persons)
# - Macula: ln="12.01" (God/supernatural being)
# - Insight: Trinitarian reference with explicit trial number
```

**Use case:** Find all potential Trinitarian references in Scripture

---

### Query Pattern 2: Cross-linguistic translation difficulty

**Query:** "Find verses requiring inclusive/exclusive distinction with imperative verbs"

```python
results = query_verses(
    tbta={
        "discourse.person": ["first_inclusive", "first_exclusive"]
    },
    macula={
        "morphology.mood": "imperative"
    }
)

# Use case: Identify verses that are especially challenging for
# languages with inclusive/exclusive distinction (Tagalog, Malay, etc.)
```

---

### Query Pattern 3: Participant tracking + syntactic complexity

**Query:** "Find verses with 3+ distinct participants (noun indices) AND complex clause structure"

```python
results = query_verses(
    tbta={
        "participant_tracking": lambda participants: len(set(p["noun_index"] for p in participants)) >= 3
    },
    macula={
        "syntax.clause": lambda clauses: len(clauses) >= 2  # Multi-clause
    }
)

# Use case: Identify narratively complex verses needing explicit referent marking
```

---

### Query Pattern 4: Emotional intensity + semantic domains

**Query:** "Find grief expressions with specific semantic domains"

```python
results = query_verses(
    tbta={
        "emotional_context.type": "grief_expression",
        "emotional_context.intensity": ["moderate", "high"]
    },
    macula={
        "semantic.ln": "25.*"  # Domain 25 = Attitudes and Emotions
    }
)

# Example results:
# - JHN.011.035: δακρύω (moderate intensity, silent tears)
# - JHN.011.033: κλαίω (high intensity, loud wailing)
#
# Use case: Study emotional vocabulary across Scripture
```

---

### Query Pattern 5: Time granularity + tense/aspect

**Query:** "Find immediate past events with aorist tense"

```python
results = query_verses(
    tbta={
        "verb_encoding.time_granularity": ["immediate_past", "earlier_today"]
    },
    macula={
        "morphology.tense": "aorist"
    }
)

# Use case: Understand how Hebrew/Greek encode recent past,
# guide translation for languages with fine-grained temporal systems
```

---

### Query Pattern 6: Demonstrative proximity + morphology

**Query:** "Find demonstratives with 4-way proximity distinctions"

```python
results = query_verses(
    tbta={
        "proximity": ["near_speaker", "near_listener", "remote_sight", "remote_no_sight"]
    },
    macula={
        "morphology.pos": "demonstrative"
    }
)

# Use case: Identify verses requiring demonstrative precision
# for languages with 3-5 way demonstrative systems (Japanese, Korean, etc.)
```

---

## 5. AI Prompt Patterns: Presenting Combined Data to LLMs

### Pattern 1: Translation Assistance for Minority Languages

**Scenario:** AI helping translator working in Kilivila (Papua New Guinea) - has trial number

**Prompt structure:**

```
You are assisting a Bible translator working in Kilivila, a language spoken in Papua New Guinea.

LANGUAGE FEATURES:
- Number system: singular, dual (2), trial (3), plural (4+)
- Person system: 1st, 2nd, 3rd, plus inclusive/exclusive distinction
- Switch-reference: marks whether subject changes between clauses

VERSE: Genesis 1:26

MACULA DATA (Word-level linguistics):
Word 2: "נַֽעֲשֶׂ֥ה" (na'aseh)
- Lemma: עָשָׂה (asah) = make, do
- Morphology: Qal imperfect, 1st person, PLURAL
- Gloss: "let us make"
- Semantic domain: Creation, making

TBTA DATA (Cross-linguistic pragmatics):
Discourse encoding:
- Number: TRIAL (exactly 3 persons)
- Person: First Inclusive (speaker includes addressees)
- Participant: God (noun index "1", routine status)

TRANSLATION QUESTION:
How should this be translated in Kilivila?

GUIDANCE:
1. Hebrew uses grammatical plural (נַֽעֲשֶׂ֥ה)
2. TBTA analysis indicates TRIAL number (exactly 3 persons)
3. This is theologically significant (Trinitarian reference)
4. Kilivila HAS a trial number form - use it!
5. The "we" is inclusive (Father addressing Son/Spirit)

RECOMMENDED TRANSLATION:
Use Kilivila trial number form (3 persons exactly), not generic plural (4+).
Mark as 1st person inclusive.

Does this match Kilivila's grammatical system? What adjustments are needed?
```

**Why this works:**
- Provides BOTH grammatical data (Macula) and semantic analysis (TBTA)
- Explains WHY trial number matters (theology + language typology)
- Connects Hebrew grammar → semantic interpretation → target language form
- Empowers translator to verify against their linguistic knowledge

---

### Pattern 2: Exegetical Study - Understanding Original Intent

**Scenario:** Pastor preparing sermon on John 11:35

**Prompt structure:**

```
I'm studying John 11:35 ("Jesus wept") for a sermon. Help me understand the original Greek.

VERSE: John 11:35
Greek: ἐδάκρυσεν ὁ Ἰησοῦς

MACULA DATA (Scholarly linguistic analysis):
Word 1: ἐδάκρυσεν (edakrysen)
- Lemma: δακρύω (dakryō) = to weep, shed tears
- Strong's: G1145
- Morphology: Aorist active indicative, 3rd person singular
- Louw-Nida: 25.139 (Sorrow, Regret - subdomain: weeping/tears)
- Syntax: Main verb (predicate)

CONTRASTING WORD (from v33):
Word: ἐκλαύσαν (eklausan)
- Lemma: κλαίω (klaiō) = to wail, weep loudly
- Strong's: G2799
- Louw-Nida: 25.138 (Sorrow - subdomain: loud lamentation)

TBTA DATA (Discourse & pragmatic analysis):
Emotional context:
- Type: grief_expression
- Intensity: MODERATE (δακρύω = silent tears)
- Contrasts with v33: κλαίω = HIGH intensity (loud wailing)
- Public setting: witnessed by others (v36)

Participant tracking:
- Jesus: routine participant (present since v1)
- Status: active agent
- Emotional state: controlled grief

Implicit information:
- Jesus knows he will raise Lazarus (foreshadowed v11)
- Tears are empathy with Mary/Martha, not hopelessness
- Cultural context: public mourning expected loud wailing (κλαίω)
- Jesus' quiet tears (δακρύω) show dignity/self-control

EXEGETICAL INSIGHT:
John deliberately contrasts:
- Mourners in v33: κλαίω (loud, uncontrolled wailing)
- Jesus in v35: δακρύω (silent, controlled tears)

This shows:
1. Jesus enters human sorrow (empathy)
2. Jesus maintains composure (divine dignity)
3. Jesus' tears are real but purposeful (not despair)

SERMON APPLICATIONS:
- Jesus weeps WITH us, not AT us
- Controlled emotion ≠ lack of feeling
- Dignity in grief is possible
```

**Why this works:**
- Macula provides precise lexical/grammatical data (aorist tense, LN domain)
- TBTA provides emotional intensity coding and cultural context
- Combined: deep exegetical insight (word choice contrast + cultural expectations)
- Practical sermon applications emerge from integrated data

---

### Pattern 3: Translation Checking - Quality Assurance

**Scenario:** Checking a new translation for cultural appropriateness

**Prompt structure:**

```
Review this Bible translation for cultural appropriateness in Japanese.

VERSE: Genesis 19:31 (older sister speaking to younger)
TRANSLATION: "お姉さんは妹に言った..." (Onēsan wa imōto ni itta...)

MACULA DATA:
- Semantic domain: 33.79 (Communication - dialogue)
- Participants: Two daughters (familial relationship)

TBTA DATA:
Speaker demographics:
- Speaker: daughter (older)
- Listener: daughter (younger)
- Age: Young adult (18-24), essentially same age
- Relationship: sibling
- Speech style: INFORMAL
- Attitude: NEUTRAL

JAPANESE LANGUAGE CONSTRAINTS:
- Requires honorific system based on age/relationship
- Siblings close in age: casual form (よ/yo, だ/da endings)
- Older to younger: can use casual, but not rude
- Formal endings (です/desu, ます/masu) inappropriate for peers

TRANSLATION CHECK:
Current translation uses: "お姉さんは..." (onēsan wa...)
- This is 3rd person formal ("the older sister...")
- Does not reflect INFORMAL speech style from TBTA

RECOMMENDED FIX:
Use direct speech without formal titles:
- "姉が妹に言った" (ane ga imōto ni itta) = "older sister said to younger"
- Or: "姉は妹に言った" (ane wa imōto ni itta)
- Speech content should use casual endings (よ、ね、etc.)

Does this translation match the TBTA speaker demographics (informal, sibling relationship)?
```

**Why this works:**
- TBTA provides speaker demographics that Macula doesn't capture
- Identifies mismatch between source pragmatics and target translation
- Prevents cultural inappropriateness (overly formal language between siblings)
- Ensures translation reflects original register/tone

---

### Pattern 4: Discourse Analysis - Tracking Participants

**Scenario:** Understanding complex narrative with multiple actors

**Prompt structure:**

```
Help me understand who does what in this complex narrative passage.

VERSE: Genesis 4:8 (Cain and Abel)
Hebrew: "וַיֹּ֥אמֶר קַ֖יִן אֶל־הֶ֣בֶל אָחִ֑יו וַֽיְהִי֙ בִּהְיוֹתָ֣ם בַּשָּׂדֶ֔ה וַיָּ֥קָם קַ֛יִן אֶל־הֶ֥בֶל אָחִ֖יו וַיַּהַרְגֵֽהוּ"

MACULA DATA (Word-level syntax):
Word 2: קַיִן (Cain)
- Morphology: proper noun
- Syntax: subject of "said"

Word 4: הֶבֶל (Abel)
- Morphology: proper noun
- Syntax: object of "to"

Word 5: אָחִיו (his brother)
- Morphology: noun + 3ms suffix
- Syntax: apposition to Abel

[Multiple "he" pronouns follow...]

TBTA DATA (Participant tracking):
Noun list indices:
- Index "1": Cain (subject, agent)
  - Status: routine (established participant)
  - Role: doer of action
  - Tracking: introduced v1, active throughout

- Index "2": Abel (object, patient)
  - Status: routine → EXITING (dies this verse)
  - Role: receiver of action
  - Note: "brother" (pos 5) also index "2" (same referent)

Clause structure:
1. "Cain said to Abel" - Cain=agent, Abel=listener
2. "he rose up" - he=Cain (index "1", same subject)
3. "he killed him" - he=Cain (index "1"), him=Abel (index "2")

ENTITY CHAIN:
Cain (index "1"): subject → subject → subject
Abel (index "2"): object → object → object
Brother: co-referent with Abel (both index "2")

CLARIFIED TRANSLATION:
"Cain said to Abel his brother. When they were in the field, Cain rose up
against Abel his brother and killed him."

Key insight: TBTA noun indices disambiguate pronouns - both "he"s refer to
Cain (index "1"), while "him" refers to Abel (index "2").
```

**Why this works:**
- Macula provides syntactic roles (subject/object) but can't disambiguate pronouns
- TBTA provides noun indices that track entities across clauses
- Combined: clear participant flow through complex narrative
- Prevents mistranslation in languages requiring explicit referent marking

---

## 6. Future Tools: What Would Complement TBTA?

### Tool 1: **Cultural Context Database**

**What it provides:**
- Ancient Near Eastern cultural practices
- Greco-Roman social customs
- Honor/shame cultural codes
- Economic systems
- Religious practices

**How it complements TBTA:**
- TBTA encodes speaker demographics → Cultural DB explains WHY those demographics matter
- TBTA marks implicit information → Cultural DB fills in what ancient audiences knew automatically
- Example: TBTA marks "speech_style: formal" → Cultural DB explains Roman patron-client relationships

**Integration example:**
```yaml
verse: LUK.007.002
tbta:
  speaker_demographics:
    speaker: "centurion"
    listener: "Jesus"
    relationship: "military_to_religious"
    speech_style: "respectful"

cultural_context:
  source: cultural-db
  practices:
    - type: "roman_military_hierarchy"
      note: |
        Centurions commanded 80-100 soldiers, significant authority.
        Addressing Jewish rabbi shows unusual humility given cultural
        context of Roman occupation. {cultural-db}

    - type: "patron_client"
      note: |
        Centurion acts as patron (built synagogue, Luke 7:5), but
        addresses Jesus as superior. Inverts expected social dynamic. {cultural-db}
```

---

### Tool 2: **Translation Memory / Parallel Corpus**

**What it provides:**
- How verse X has been translated in 1000+ languages
- Translation patterns grouped by language family
- Successful vs problematic translation strategies
- Annotated with rationales

**How it complements TBTA:**
- TBTA identifies cross-linguistic features → Translation Memory shows how languages with those features handled the verse
- TBTA flags "trial number" → Translation Memory shows all trial-number language translations
- Example: TBTA marks "demonstrative: near_speaker" → TM shows Japanese translations using これ (kore)

**Integration example:**
```yaml
verse: GEN.001.026
tbta:
  discourse:
    number: "trial"

translation_memory:
  source: parallel-corpus

  by_feature:
    - feature: "trial_number_languages"
      examples:
        - lang: "Kilivila"
          translation: "[trial form verb]"
          note: "Uses grammatical trial matching Hebrew semantics" {parallel-corpus}

        - lang: "Fijian"
          translation: "[trial pronoun] make"
          note: "Explicit trial pronoun + verb" {parallel-corpus}

    - feature: "no_trial_number"
      examples:
        - lang: "English"
          translation: "Let us make"
          note: "Generic plural, theological footnote needed" {parallel-corpus}
```

---

### Tool 3: **Theological Tradition Database**

**What it provides:**
- How different theological traditions interpret verses
- Denominational perspectives (Reformed, Catholic, Orthodox, Pentecostal, etc.)
- Historical interpretations (Church Fathers, Reformers, modern scholarship)
- Controversial verses with competing interpretations

**How it complements TBTA:**
- TBTA encodes semantic data neutrally → Theological DB shows how traditions interpret that data
- TBTA marks "implicit_information" → Theological DB provides competing views on what's implicit
- Example: TBTA marks trial number in Gen 1:26 → Theological DB shows Trinitarian vs non-Trinitarian interpretations

**Integration example:**
```yaml
verse: GEN.001.026
tbta:
  discourse:
    number: "trial"
    person: "first_inclusive"

theological_traditions:
  source: theology-db

  interpretations:
    - tradition: "Trinitarian (Nicene)"
      view: |
        Trial number (3 persons) indicates Trinity: Father, Son, Holy Spirit
        in counsel before creation. First inclusive = Father addressing Son/Spirit. {theology-db}

      denominations: ["Catholic", "Orthodox", "Protestant Reformed"]

    - tradition: "Non-Trinitarian"
      view: |
        Plural of majesty (grammatical plural), not literal plurality.
        God speaking in royal "we" without implying distinct persons. {theology-db}

      denominations: ["Jehovah's Witnesses", "Oneness Pentecostal"]

    - tradition: "Jewish (Rabbinic)"
      view: |
        God consulting heavenly court (angels). Plural is real but not
        divine plurality - God + angels in deliberation. {theology-db}

      sources: ["Talmud", "Midrash Rabbah"]
```

---

### Tool 4: **Discourse Structure Analyzer**

**What it provides:**
- Paragraph-level discourse analysis
- Episode boundaries
- Narrative peak identification
- Information flow (theme/rheme)
- Coherence relations between clauses

**How it complements TBTA:**
- TBTA does clause-level tracking → Discourse Analyzer shows paragraph/episode structure
- TBTA marks participant status changes → Discourse Analyzer shows why (episode boundaries)
- Example: TBTA marks "participant: exiting" → Discourse Analyzer identifies this as episode climax

**Integration example:**
```yaml
verse: GEN.004.008
tbta:
  participant_tracking:
    - entity: "Abel"
      status: "exiting"  # Dies this verse

discourse_structure:
  source: discourse-analyzer

  episode: "cain_and_abel"
  section: "climax"

  structure:
    setup: "GEN.004.001-007"  # Brothers introduced, Cain angry
    rising_action: "GEN.004.008a"  # "Cain said to Abel"
    climax: "GEN.004.008b"  # Murder (participant exits)
    falling_action: "GEN.004.009-012"  # God's judgment
    resolution: "GEN.004.013-16"  # Cain's exile

  participant_arc:
    - entity: "Abel"
      arc: "introduced (v2) → routine (v3-4) → EXITING (v8) → referenced (v9-10)"
      peak: "v8"  # Death is narrative climax
```

---

### Tool 5: **Phonological & Orthographic Database**

**What it provides:**
- Original language pronunciation
- Transliteration standards
- Sound symbolism
- Wordplay/puns
- Alphabetic acrostics

**How it complements TBTA:**
- TBTA marks semantic meaning → Phonological DB shows sound patterns affecting meaning
- TBTA doesn't capture wordplay → Phonological DB identifies puns/acrostics
- Example: Psalm 119 acrostic structure (TBTA misses this, Phono DB captures it)

**Integration example:**
```yaml
verse: GEN.002.023
source:
  text: "זֹ֣את הַפַּ֗עַם עֶ֚צֶם מֵֽעֲצָמַ֔י וּבָשָׂ֖ר מִבְּשָׂרִ֑י לְזֹאת֙ יִקָּרֵ֣א אִשָּׁ֔ה כִּ֥י מֵאִ֖ישׁ לֻֽקֳחָה־זֹּֽאת"

phonology:
  source: phono-db

  wordplay:
    - type: "etymological_pun"
      words: ["אִישׁ" (ish/man), "אִשָּׁה" (ishah/woman)]
      pattern: "Sound similarity suggests derivation"

      analysis: |
        Hebrew wordplay: אִשָּׁה (woman) sounds like feminine form of אִישׁ (man).
        Not true etymology, but deliberate poetic connection. English "woman"
        from "wife-man" captures similar wordplay. {phono-db}

      translation_note: |
        Translators should preserve wordplay if possible. Options:
        - "She shall be called Woman, for she was taken out of Man" (preserves sound)
        - Add footnote explaining Hebrew pun
        {phono-db}
```

---

### Tool 6: **Syntax-Semantics Mapping Engine**

**What it provides:**
- Maps syntactic structures to semantic roles
- Identifies construction grammar patterns
- Tracks idiomatic constructions
- Analyzes information structure

**How it complements TBTA:**
- Macula provides syntax → TBTA provides pragmatics → Syntax-Semantics bridges the gap
- Maps grammatical forms to communicative functions
- Example: Identifies "fronted constituent" construction as marking focus/emphasis

**Integration example:**
```yaml
verse: JHN.001.001
source:
  text: "Ἐν ἀρχῇ ἦν ὁ λόγος"  # Word order: "In beginning was the Word"

macula:
  syntax:
    - word: "Ἐν ἀρχῇ"
      role: "temporal_adjunct"
      position: 1  # Fronted (not default position)

syntax_semantics:
  source: syntax-sem-engine

  construction:
    type: "fronted_adjunct"
    function: "topic_establishing"

    analysis: |
      Prepositional phrase "Ἐν ἀρχῇ" (in beginning) fronted to clause-initial
      position. Default Greek word order: Verb - Subject - Object - Adjuncts.
      Fronting marks temporal setting as TOPIC for entire Gospel narrative. {syn-sem}

    information_structure:
      given: null  # Opening sentence, no given info
      new: "ὁ λόγος" (the Word)  # Main new information
      topic: "Ἐν ἀρχῇ" (in beginning)  # Temporal frame

    translation_implications: |
      Maintain fronted temporal phrase in translation to preserve topic-marking:
      ✓ "In the beginning was the Word" (English preserves fronting)
      ✗ "The Word was in the beginning" (loses topic structure)
      {syn-sem}
```

---

## 7. Transferable Patterns: Multi-Source Data Integration Strategies

### Strategy 1: **Layered Architecture**

**Principle:** Stack data sources from most concrete (grammatical) to most abstract (pragmatic)

```
LAYER 1: MACULA (Morphology, Syntax, Lexicon)
    ↓ provides grammatical foundation
LAYER 2: TBTA (Discourse, Pragmatics, Cross-linguistic)
    ↓ provides semantic interpretation
LAYER 3: CULTURAL-DB (Historical, Social Context)
    ↓ provides cultural background
LAYER 4: THEOLOGY-DB (Interpretive Traditions)
    ↓ provides theological perspectives
```

**Application pattern:**
```yaml
verse: JHN.011.035

# Layer 1: Grammar (concrete)
macula:
  morphology:
    tense: "aorist"  # Grammatical fact
    voice: "active"

# Layer 2: Pragmatics (interpretation)
tbta:
  emotional_context:
    intensity: "moderate"  # Inferred from lexeme choice

# Layer 3: Culture (background)
cultural:
  mourning_practices:
    expected: "loud_wailing"  # Cultural norm
    actual: "silent_tears"    # Jesus' deviation

# Layer 4: Theology (meaning)
theological:
  interpretations:
    - "Jesus' empathy with human suffering"
    - "Jesus' grief at death's ravages"
```

**Why this works:**
- Each layer builds on previous
- Can query any layer independently
- Prevents circular reasoning (grammar → semantics → culture → theology, not reverse)
- Makes data dependencies explicit

---

### Strategy 2: **Feature Flagging**

**Principle:** Tag verses with specific linguistic features for targeted querying

```yaml
verse: GEN.001.026

feature_flags:
  # MACULA features
  morphology:
    - "hebrew_plural_verb"
    - "qal_stem"

  syntax:
    - "cohortative_construction"

  # TBTA features
  discourse:
    - "trial_number"
    - "first_inclusive"

  cross_linguistic:
    - "number_system_rare"
    - "person_system_inclusive_exclusive"

  # Cultural features
  cultural:
    - "ancient_near_east"
    - "creation_narrative"

  # Theological features
  theological:
    - "trinitarian_reference"
    - "disputed_interpretation"
```

**Query examples:**
```python
# Find all verses with rare number systems
verses = query(feature_flags__cross_linguistic__contains="number_system_rare")

# Find verses with both Hebrew plural AND semantic trial
verses = query(
    feature_flags__morphology__contains="hebrew_plural_verb",
    feature_flags__discourse__contains="trial_number"
)

# Find theologically disputed verses with cross-linguistic complexity
verses = query(
    feature_flags__theological__contains="disputed_interpretation",
    feature_flags__cross_linguistic__regex=".*_system_.*"
)
```

**Why this works:**
- Fast querying without parsing full YAML
- Enables faceted search
- Documents what makes each verse "interesting"
- Supports use case discovery

---

### Strategy 3: **Confidence Scoring**

**Principle:** Tag interpretations with confidence levels based on data source consensus

```yaml
verse: GEN.001.026

interpretations:
  - claim: "Hebrew uses grammatical plural form"
    confidence: 1.0  # Certain (Macula morphological analysis)
    sources: ["macula-hebrew"]

  - claim: "Semantic number is trial (exactly 3)"
    confidence: 0.8  # High (TBTA encoding, but interpretation-dependent)
    sources: ["tbta-db"]
    note: "Depends on Trinitarian theological framework"

  - claim: "Refers to Trinity (Father, Son, Spirit)"
    confidence: 0.6  # Medium (theological interpretation, not linguistic data)
    sources: ["theology-db:trinitarian"]
    note: "Majority Christian tradition, not universally accepted"

  - claim: "God consulting angels"
    confidence: 0.4  # Lower (minority interpretation)
    sources: ["theology-db:rabbinic"]
    note: "Jewish rabbinic tradition"
```

**Usage in AI prompts:**
```
VERSE: Genesis 1:26

FACTS (Confidence 1.0):
- Hebrew verb is grammatical plural (Macula)

HIGH CONFIDENCE (0.7-0.9):
- Semantic number is trial/3 persons (TBTA)

INTERPRETATIONS (0.4-0.6):
- Trinitarian: Father, Son, Spirit (Christian theology)
- Rabbinic: God + angels (Jewish tradition)

Recommendation: Present high-confidence linguistic facts, acknowledge
interpretive debates. Don't claim certainty where sources disagree.
```

**Why this works:**
- Distinguishes facts from interpretations
- Prevents AI from over-confidently asserting debated points
- Makes source reliability transparent
- Enables filtering by confidence threshold

---

### Strategy 4: **Canonical Data Representation**

**Principle:** Normalize data from different sources into standardized format

**Problem:** Different sources use different terminologies:
- Macula: `morphology.pos = "verb"`
- TBTA: `part_of_speech = "V"`
- Cultural-DB: `word_type = "action"`

**Solution:** Map to canonical schema:
```yaml
# Canonical schema (SCHEMA.md standard)
verse: MAT.005.003

words:
  - position: 1

    # Source 1: Macula (original)
    _macula:
      morph: "A-NPM"
      class: "adj"

    # Source 2: TBTA (original)
    _tbta:
      part_of_speech: "ADJ"

    # Canonical (normalized)
    morphology:
      pos: "adjective"  # Standardized
      case: "nominative"
      number: "plural"
      gender: "masculine"
```

**Normalization mapping:**
```python
# Canonical POS tags
POS_CANONICAL = {
    "verb": ["verb", "V", "action", "predicate"],
    "noun": ["noun", "N", "substantive", "nomina"],
    "adjective": ["adj", "A", "modifier"],
    # ...
}

# Normalization function
def normalize_pos(source_value, source_name):
    for canonical, variants in POS_CANONICAL.items():
        if source_value.lower() in [v.lower() for v in variants]:
            return canonical
    return source_value  # Fallback
```

**Why this works:**
- Single query language works across all sources
- No need to remember each source's terminology
- Easy to add new sources (just map their terms)
- Preserves original data under `_source_name` for verification

---

### Strategy 5: **Dependency Injection**

**Principle:** Make data sources modular and swappable

```python
# Define data source interface
class DataSource:
    def get_verse_data(self, verse_ref):
        raise NotImplementedError

# Implement for each source
class MaculaSource(DataSource):
    def get_verse_data(self, verse_ref):
        # Load from .data/macula/...
        return macula_data

class TBTASource(DataSource):
    def get_verse_data(self, verse_ref):
        # Load from .data/tbta/...
        return tbta_data

# Integration layer
class VerseIntegrator:
    def __init__(self, sources: List[DataSource]):
        self.sources = sources

    def get_integrated_verse(self, verse_ref):
        data = {}
        for source in self.sources:
            source_data = source.get_verse_data(verse_ref)
            data = self.merge(data, source_data)
        return data

    def merge(self, existing, new):
        # Implement merge logic
        # Handle conflicts, priority, etc.
        ...

# Usage
integrator = VerseIntegrator([
    MaculaSource(),
    TBTASource(),
    CulturalDBSource(),
])

verse = integrator.get_integrated_verse("JHN.011.035")
```

**Why this works:**
- Easy to add/remove data sources
- Testing: can mock individual sources
- Performance: can parallelize source queries
- Flexibility: different source combinations for different use cases

---

### Strategy 6: **Conflict Resolution Policies**

**Principle:** Define explicit rules for handling conflicting data

**Example conflict:** Macula says "plural", TBTA says "trial" - which is right?

**Resolution policy:**
```yaml
conflict_resolution:
  policies:
    - name: "grammatical_vs_semantic_number"

      rule: |
        When grammatical number (Macula) differs from semantic number (TBTA):
        1. Both are correct at different levels
        2. Store both with clear labels
        3. Grammatical = surface form
        4. Semantic = intended meaning

      example:
        verse: "GEN.001.026"
        macula:
          number: "plural"  # Hebrew grammar
        tbta:
          number: "trial"   # Semantic interpretation

        resolution:
          grammatical_number: "plural"
          semantic_number: "trial"
          note: "Hebrew plural form with trial semantic intent"

    - name: "multiple_semantic_domains"

      rule: |
        When multiple sources provide different semantic domains:
        1. List all domains with sources
        2. Mark primary domain if consensus exists
        3. Preserve alternatives for ambiguous cases

      example:
        verse: "MAT.005.003"

        macula:
          ln: "88.57"  # Humility

        cultural_db:
          domain: "poverty_economic"  # Surface reading

        resolution:
          primary_domain: "88.57"  # Louw-Nida definitive
          source: "macula"
          alternatives:
            - domain: "poverty_economic"
              source: "cultural-db"
              note: "Surface reading, not contextual"
```

**Why this works:**
- Makes conflict resolution transparent
- Preserves all interpretations
- Documents WHY one interpretation is preferred
- Enables users to disagree with resolution

---

### Strategy 7: **Provenance Tracking**

**Principle:** Every piece of data knows where it came from

```yaml
verse: JHN.011.035

data:
  - field: "morphology.tense"
    value: "aorist"
    provenance:
      source: "macula-greek"
      version: "1.0.0"
      extracted: "2024-11-05T10:30:00Z"
      extractor: "macula_processor.py:v2.1"
      confidence: 1.0
      method: "direct_extraction"

  - field: "emotional_context.intensity"
    value: "moderate"
    provenance:
      source: "tbta-db-export"
      version: "2024-03-15"
      extracted: "2024-11-05T10:35:00Z"
      extractor: "tbta_ingester.py:v1.3"
      confidence: 0.85
      method: "encoding_interpretation"
      note: "Inferred from verb lexeme choice (δακρύω vs κλαίω)"

  - field: "theological.interpretation"
    value: "Jesus' empathy with human suffering"
    provenance:
      source: "theology-db"
      version: "2024-10-01"
      extracted: "2024-11-05T10:40:00Z"
      extractor: "theology_db_sync.py:v1.0"
      confidence: 0.6
      method: "tradition_survey"
      note: "Majority view among commentators"
```

**Query by provenance:**
```python
# Get only high-confidence Macula data
data = get_verse_data(
    "JHN.011.035",
    filter_by=lambda d: d.provenance.source.startswith("macula")
                        and d.provenance.confidence >= 0.9
)

# Get all TBTA pragmatic data
data = get_verse_data(
    "GEN.001.026",
    filter_by=lambda d: d.provenance.source == "tbta-db-export"
)
```

**Why this works:**
- Full data lineage for debugging
- Can filter by source quality
- Enables reproducibility
- Supports data versioning

---

## Summary: Key Integration Principles

1. **Complementary, not redundant** - TBTA provides what Macula doesn't (pragmatics, discourse, cross-linguistic)
2. **Layered integration** - Grammar (Macula) → Semantics (TBTA) → Culture → Theology
3. **Single-file YAML** - Start with integrated files, split only if necessary
4. **Feature flagging** - Tag verses for fast querying
5. **Confidence scoring** - Distinguish facts from interpretations
6. **Canonical schema** - Normalize different source terminologies
7. **Provenance tracking** - Every data point knows its source
8. **Conflict resolution** - Explicit policies for handling disagreements
9. **Practical queries** - Combined Macula+TBTA queries enable powerful insights
10. **AI-friendly prompts** - Present integrated data in context with examples

---

## Next Steps

1. **Ingest TBTA data** - Parse TBTA JSON/XML into YAML format
2. **Pilot integration** - Test single-file integration on 10-20 verses
3. **Query development** - Build combined Macula+TBTA query functions
4. **AI prompt library** - Create reusable prompt templates
5. **Documentation** - Update SCHEMA.md with TBTA integration patterns
6. **Feature flag taxonomy** - Document all TBTA features for flagging
7. **Conflict resolution rules** - Formalize policies for edge cases

---

**Last Updated:** 2025-11-05
**Version:** 1.0
**Status:** Initial analysis
