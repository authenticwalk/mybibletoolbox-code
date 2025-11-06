# TBTA Use Case Patterns

## Overview

This document analyzes how Bible translators actually use TBTA features in real translation scenarios. It groups languages by their feature requirements, identifies feature combinations, validates priority tiers, and provides concrete translation workflows.

---

## 1. Language Family Patterns

### Pattern A: Austronesian Languages (1200+ languages)
**Key Feature Requirements**: Person Systems (Inclusive/Exclusive), Number Systems, Participant Tracking

**Representative Languages**: Tagalog, Ilokano, Malay, Indonesian, Fijian, Tongan, Samoan, Māori

**Feature Dependencies**:
- **Person Systems**: First Inclusive vs First Exclusive (critical)
- **Number Systems**: Many have dual/paucal (important)
- **Participant Tracking**: Helps with topic prominence (medium)
- **Time Granularity**: Some have aspectual distance markers (medium)

**Example: Tagalog Translator on Acts 15:25**

**Verse**: "It seemed good to us, having become of one mind, to select men to send to you"

**TBTA Features Needed**:
```yaml
person: First Exclusive  # "us" = apostles, not including recipients
number: Plural
participant_tracking: Routine  # Apostles are established participants
speaker_listener_age: Not Applicable
attitude: Formal
```

**Translation Decision**:
- Use **"kami"** (exclusive we) not **"tayo"** (inclusive we)
- Recipients are NOT part of "us" making the decision
- Without TBTA: translator must infer from context (error-prone)
- With TBTA: explicit encoding prevents error

**Impact**: Prevents theological misunderstanding about who made the decision

---

### Pattern B: East Asian Languages (400+ languages)
**Key Feature Requirements**: Proximity Systems, Speaker Demographics, Honorifics

**Representative Languages**: Japanese, Korean, Mandarin, Cantonese, Vietnamese, Thai

**Feature Dependencies**:
- **Proximity Systems**: 3-5 way demonstrative distinctions (critical)
- **Speaker Demographics**: Age, relationship, social register (critical)
- **Participant Tracking**: Topic-comment structure (important)
- **Number Systems**: Less critical (most lack plural marking)

**Example: Japanese Translator on John 1:29**

**Verse**: "Behold, the Lamb of God!"

**TBTA Features Needed**:
```yaml
proximity: Near Speaker (John), Remote from Listener  # Jesus visible to John
speaker: John the Baptist
listener: Crowd
speaker_age: Adult (30s)
speaker_listener_age: Mixed
attitude: Respectful
speech_style: Formal
```

**Translation Decisions**:
1. **Demonstrative**: Use **"あの"** (ano - that far from both) not **"この"** (kono - this near me)
   - Jesus is at a distance from John
   - Not near the crowd listening to John

2. **Verb Ending**: Use **"です"** (desu - formal) not casual form
   - John speaking to mixed crowd
   - Respectful attitude toward crowd
   - Formal proclamation context

**Impact**: Correct spatial reference + appropriate social register

---

### Pattern C: Papua New Guinea Languages (800+ languages)
**Key Feature Requirements**: Number Systems (trial/quadrial), Switch-Reference, Participant Tracking

**Representative Languages**: Kilivila, Kewa, Huli, Melpa, Enga

**Feature Dependencies**:
- **Number Systems**: Dual, trial, sometimes quadrial (critical)
- **Participant Tracking**: Switch-reference marking (critical)
- **Semantic Roles**: Explicit case marking (important)
- **Person Systems**: Often have inclusive/exclusive (important)

**Example: Kilivila Translator on Genesis 1:26**

**Verse**: "Then God said, 'Let us make man in our image'"

**TBTA Features Needed**:
```yaml
speaker: God
number: Trial  # Exactly 3 persons
person: First Inclusive  # Trinity members addressing each other
participant_tracking: First Mention (man)
```

**Translation Decisions**:
1. **Number**: Use **trial pronoun** (exactly 3) not plural (3+)
   - Kilivila distinguishes: singular / dual / trial / plural
   - "Us" = Trinity (Father, Son, Spirit) = exactly 3

2. **Person**: Use inclusive form
   - All Trinity members participating

3. **Participant**: Mark "man" as new participant
   - First introduction in discourse
   - Use switch-reference marker (different subject)

**Impact**: Preserves Trinitarian theology + correct discourse structure

---

### Pattern D: African Languages (2000+ languages)
**Key Feature Requirements**: Noun Classes, Time Granularity, Salience Bands

**Representative Languages**: Swahili, Yoruba, Zulu, Amharic, Luganda

**Feature Dependencies**:
- **Participant Tracking**: Noun class agreement (critical)
- **Time Granularity**: Remote past distinctions (important)
- **Salience Bands**: Foreground/background marking (important)
- **Number Systems**: Some have associative plurals (medium)

**Example: Swahili Translator on Genesis 4:8**

**Verse**: "Cain said to his brother Abel. And when they were in the field, Cain rose up against Abel his brother and killed him."

**TBTA Features Needed**:
```yaml
participants:
  - entity: Cain
    index: "1"
    tracking: Routine
    class: Person (m-class)
  - entity: Abel
    index: "2"
    tracking: Routine → Exiting
    class: Person (m-class)
salience:
  - clause: "Cain said"
    band: Primary Storyline
  - clause: "when they were in field"
    band: Setting
  - clause: "Cain rose up"
    band: Pivotal Storyline
  - clause: "killed him"
    band: Pivotal Storyline
```

**Translation Decisions**:
1. **Participant Tracking**: Maintain Cain (index 1) as subject
   - Use m-class pronouns consistently for Cain
   - Mark Abel (index 2) as object throughout

2. **Salience Bands**:
   - Setting clause: use background tense (imperfect)
   - Pivotal action: use foreground tense (perfect)

3. **Switch-Reference**: No subject change until "killed him"
   - Cain remains grammatical subject
   - Abel marked as exiting participant (dies)

**Impact**: Clear subject tracking + correct discourse prominence

---

### Pattern E: Native American Languages (1000+ languages)
**Key Feature Requirements**: Evidentiality, Switch-Reference, Obviation

**Representative Languages**: Navajo, Cherokee, Cree, Quechua, Aymara

**Feature Dependencies**:
- **Participant Tracking**: Obviation/proximate marking (critical)
- **Evidentiality**: Source of knowledge (critical for some)
- **Number Systems**: Some have obviative plural (important)
- **Semantic Roles**: Direct/inverse voice (important)

**Example: Quechua Translator on Mark 1:40**

**Verse**: "A leper came to him pleading with him"

**TBTA Features Needed**:
```yaml
participants:
  - entity: leper
    index: "1"
    tracking: First Mention
    semantic_role: Agent
  - entity: Jesus (implied)
    index: "2"
    tracking: Routine
    semantic_role: Goal
evidentiality: Narrative (witnessed)
```

**Translation Decisions**:
1. **Evidentiality**: Use **-sqa** (reported/narrative) suffix
   - Translator not present at event
   - Biblical narrative = reported knowledge

2. **Obviation**: Mark leper as proximate, Jesus as obviative
   - Leper = new focus participant (proximate)
   - Jesus = continuing participant (obviative)

3. **Semantic Role**: Use direct voice
   - Leper = agent (higher animacy as new focus)
   - Jesus = goal

**Impact**: Correct knowledge source + participant hierarchy

---

## 2. Feature Combinations

### Combination 1: Honorifics Package
**Features Required Together**: Speaker Demographics + Attitude + Speech Style + Age Relationship

**When Used**: Japanese, Korean, Javanese, Balinese, Thai, Vietnamese

**Example: Korean Translator on Genesis 19:31**

**Verse**: "The older sister said to her younger sister"

**TBTA Data**:
```yaml
speaker: daughter (older)
listener: daughter (younger)
speaker_age: Young Adult (18-24)
listener_age: Young Adult (18-24)
speaker_listener_age: Essentially the Same Age
speaker_attitude: Neutral
speech_style: Informal
relationship: Sibling
```

**Korean Translation Decisions**:
All four features needed to select correct verb ending:

1. **Age Relationship**: Same age → can use casual
2. **Attitude**: Neutral → not extra polite
3. **Speech Style**: Informal → family context
4. **Relationship**: Sibling → intimate register

**Verb Ending**: Use **-어/-아** (casual) not **-요** (polite) or **-습니다** (formal)

**If Missing Any Feature**:
- Missing age: might use wrong formality level
- Missing relationship: might use stranger register
- Missing attitude: might be too casual or too formal
- Missing style: might misread context as public/formal

**Impact**: All four features work together to determine single translation choice

---

### Combination 2: Demonstrative Package
**Features Required Together**: Proximity + Participant Tracking + Semantic Role

**When Used**: Languages with 3+ demonstrative distinctions

**Example: Spanish Translator on Luke 7:44**

**Verse**: "Do you see this woman?"

**TBTA Data**:
```yaml
proximity: Near Speaker (Jesus), Remote from Listener (Simon)
participant_tracking: Routine (woman is present in scene)
semantic_role: Patient (woman being pointed out)
speaker: Jesus
listener: Simon the Pharisee
```

**Spanish Translation Decisions**:

Demonstratives: este (near me) / ese (near you) / aquel (far from both)

1. **Proximity**: Near Jesus, far from Simon → **"esta"** (feminine, near speaker)
2. **Tracking**: Woman is present → visible demonstrative (not abstract)
3. **Role**: Being indicated → accusative case with "ver"

**Translation**: "¿Ves a **esta** mujer?"

**If Using Only Proximity**:
- Might use wrong demonstrative if not tracking speaker/listener positions
- Context-free "this" is ambiguous in 3-way system

**Impact**: Spatial + discourse tracking combine for correct reference

---

### Combination 3: Narrative Tense Package
**Features Required Together**: Time Granularity + Salience Band + Discourse Genre

**When Used**: Languages with complex tense/aspect systems marking temporal distance + discourse level

**Example: Tagalog Translator on Genesis 1:1**

**Verse**: "In the beginning God created the heavens and the earth"

**TBTA Data**:
```yaml
time_granularity: Eternity Past
salience_band: Pivotal Storyline
discourse_genre: Narrative
aspect: Completive
```

**Tagalog Translation Decisions**:

Tense forms: recent (nag-), today (-um-), yesterday (nag- + kahapon), remote (nag-)

1. **Time Granularity**: Eternity Past → remote past
2. **Salience**: Pivotal → foreground (perfective)
3. **Genre**: Narrative → past tense frame
4. **Aspect**: Completive → perfective

**Translation**: Use **"lumikha"** (remote past perfective)

**Why All Three Matter**:
- Time: determines past vs present
- Salience: determines perfective vs imperfective
- Genre: determines narrative frame vs expository

**Impact**: Correct temporal + aspectual + discourse marking

---

### Combination 4: Participant Tracking Package
**Features Required Together**: Noun List Index + Participant Tracking + Semantic Role + Switch-Reference

**When Used**: Switch-reference languages with complex participant systems

**Example: Navajo Translator on John 18:10**

**Verse**: "Simon Peter, having a sword, drew it and struck the high priest's servant and cut off his right ear"

**TBTA Data**:
```yaml
participants:
  - entity: Simon Peter
    index: "1"
    tracking: Routine
    semantic_role: Agent
  - entity: sword
    index: "2"
    tracking: Routine
    semantic_role: Instrument
  - entity: servant
    index: "3"
    tracking: First Mention
    semantic_role: Patient
  - entity: ear
    index: "4"
    tracking: Routine (part of index 3)
    semantic_role: Patient
switch_reference:
  - "drew it": same subject (Peter)
  - "struck": same subject (Peter)
  - "cut off": same subject (Peter)
```

**Navajo Translation Decisions**:

1. **Index Tracking**:
   - Peter (1) = subject throughout
   - Sword (2) = instrument
   - Servant (3) = primary object
   - Ear (4) = secondary object (part of 3)

2. **Participant Status**:
   - Peter: continuing (use zero anaphora)
   - Servant: new (mark as new participant)

3. **Semantic Roles**:
   - Agent (Peter) = direct voice
   - Instrument (sword) = instrumental prefix
   - Patient (servant/ear) = object marking

4. **Switch-Reference**:
   - All clauses same subject → use same-subject marker
   - No switch throughout sequence

**Translation**: Maintains single subject chain with proper participant hierarchy

**Impact**: Clear reference tracking in complex action sequence

---

## 3. Priority Tier Validation

### Tier A: Essential (Cannot Be Inferred)

#### Feature: Person Systems (Inclusive/Exclusive)
**Tier A Justified**: ✅

**Validation**:
- Affects: 1000+ languages (Austronesian, some Native American, some African)
- Cannot infer from context reliably
- Binary choice with theological implications

**Test Case**: Acts 15:25 - "seemed good to us"
- Context clues: Could be inclusive OR exclusive
- Greek: ἡμῖν (hēmin) - ambiguous
- English: "us" - ambiguous
- TBTA: First Exclusive - EXPLICIT

**Without TBTA**: 50% chance of error
**With TBTA**: Deterministic

**Conclusion**: Must remain Tier A

---

#### Feature: Number Systems (Trial/Quadrial)
**Tier A Justified**: ✅

**Validation**:
- Affects: 100+ languages (Austronesian, Pacific, some PNG)
- Cannot infer exact count from English/Greek plural
- Theological significance (Trinity)

**Test Case**: Genesis 1:26 - "Let us make"
- Context clues: "Us" could be 2, 3, or many
- Hebrew: plural - ambiguous
- English: "us" - ambiguous
- TBTA: Trial - EXPLICIT

**Without TBTA**: Translator must rely on theology/tradition
**With TBTA**: Linguistic data supports theology

**Conclusion**: Must remain Tier A

---

#### Feature: Speaker Demographics
**Tier A Justified**: ✅

**Validation**:
- Affects: 500+ languages (East Asian, some Austronesian, some African)
- Cannot infer age/relationship from text alone
- Required for grammatical correctness

**Test Case**: Genesis 19:31 - "sister said to sister"
- Context clues: "Older" mentioned in verse 31, but not always clear
- TBTA provides: Age, relationship, formality

**Without TBTA**: Translator must reconstruct social context
**With TBTA**: Explicit demographics

**Conclusion**: Must remain Tier A

---

### Tier B: Important (Sometimes Inferable)

#### Feature: Proximity Systems
**Current Tier**: B
**Validation**: Should remain B with notes

**Rationale**:
- Often inferable from narrative context
- But not always (especially in dialogue)

**Test Case Where Inferable**: John 1:29 - "Behold the Lamb"
- Context: Jesus approaching, John speaking
- Inferable: Jesus at distance but visible

**Test Case Where NOT Inferable**: Matthew 3:17 - "This is my beloved Son"
- Context: Voice from heaven
- Not clear: Is Jesus near the voice? Near listeners? Remote?
- TBTA needed for spatial encoding

**Conclusion**: Tier B correct, with note that some cases require explicit marking

---

#### Feature: Semantic Roles
**Current Tier**: B
**Validation**: ✅ Correct

**Rationale**:
- Often derivable from syntax
- Important for flexible word order languages
- Not critical for fixed word order

**Conclusion**: Tier B appropriate

---

### Tier C: Specialized

#### Feature: Alternative Analyses
**Current Tier**: C
**Validation**: ✅ Correct

**Rationale**:
- Helpful for ambiguous passages
- Not needed for most translation
- Scholarly tool more than translation tool

**Conclusion**: Tier C appropriate

---

#### Feature: Implicit Information
**Current Tier**: C
**Validation**: Should be elevated to B

**Rationale**:
- High-context vs low-context languages
- Critical for cross-cultural translation
- Helps translators know what to make explicit

**Example**: John 4:9 - "How is it that you, a Jew, ask for a drink from me, a Samaritan woman?"

**Implicit Information**:
- Jews don't associate with Samaritans (cultural)
- Men don't speak to unrelated women in public (cultural)
- Requesting drink implies touching her vessel (purity issue)

**Impact**: Without marking implicit info, translator might not make explicit what target culture needs

**Recommendation**: Move to Tier B

---

## 4. Translation Workflows

### Workflow 1: Pre-Translation Planning

**Goal**: Translator reviews target language needs and identifies required TBTA features

**Steps**:

1. **Language Profile Creation**
   ```yaml
   language: Tagalog
   iso_639_3: tgl
   required_features:
     - person_inclusive_exclusive: critical
     - time_granularity: important
     - participant_tracking: helpful
   optional_features:
     - proximity: rarely needed
     - trial_number: not applicable
   ```

2. **Book-Level Feature Scan**
   - Query: "Show all verses in Acts with First Inclusive/Exclusive"
   - Result: 47 verses need attention
   - Translator can plan translation session

3. **Create Translation Checklist**
   ```markdown
   ## Acts 15 Translation - Tagalog

   - [ ] v.22 - "us" → kami/tayo?
   - [ ] v.25 - "us" → kami/tayo?
   - [ ] v.28 - "us" → kami/tayo?
   ```

**Tools Needed**:
- Feature query by language requirements
- Verse list export
- Checklist generator

---

### Workflow 2: Verse-by-Verse Translation

**Goal**: Translator works through a passage using TBTA data

**Example: Japanese Translator on Luke 7:36-50**

**Step 1: Read Passage Context**
- Query: "Get Luke 7:36-50 TBTA data"
- Review: speakers, participants, demographics

**Step 2: Identify Key Features**
- v.40 - Jesus to Simon: demographics?
  ```yaml
  speaker: Jesus
  listener: Simon (Pharisee)
  attitude: Respectful but Teaching
  speech_style: Formal
  ```
  Decision: Use です (desu) polite form

- v.44 - "this woman" proximity?
  ```yaml
  proximity: Near Speaker (Jesus), Remote from Listener (Simon)
  ```
  Decision: Use この (kono - near me) not その (sono - near you)

**Step 3: Apply Demographics**
- Woman to Jesus:
  ```yaml
  speaker_listener_age: Younger to Older
  attitude: Reverent
  ```
  Decision: Use honorific forms for Jesus

**Step 4: Check Participant Tracking**
- Woman: First Mention (v.37) → Routine (v.38-50)
- Track as consistent participant
- Use same pronoun/reference throughout

**Tools Needed**:
- Verse range query
- Feature highlighting
- Cultural context notes

---

### Workflow 3: Post-Translation Review

**Goal**: Check translation against TBTA features

**Steps**:

1. **Feature Audit**
   - List: All First Inclusive instances in Acts
   - Check: Did translator use kami or tayo?
   - Verify: Consistency with TBTA encoding

2. **Consistency Check**
   - Query: "All instances of participant index '1' (Peter) in Acts 1-12"
   - Verify: Same participant reference throughout
   - Check: Proper exiting/restaging markers

3. **Register Audit**
   - Query: "All speaker demographics in Luke 1"
   - Check: Mary to Elizabeth (cousins, intimate)
   - Check: Angel to Mary (formal, reverent)
   - Verify: Translator used appropriate register throughout

**Tools Needed**:
- Feature consistency checker
- Participant tracking across chapters
- Register audit tool

---

### Workflow 4: Translation Team Collaboration

**Goal**: Team discusses ambiguous passages using TBTA data

**Scenario**: Translation team meeting on Genesis 1:26

**Discussion Points**:

1. **Consultant presents TBTA data**:
   ```yaml
   speaker: God
   number: Trial
   person: First Inclusive
   ```

2. **Team Discussion**:
   - Language has dual/trial distinction
   - Team debates: Trinity (3) or God + angels (2+)?
   - TBTA evidence: Trial number supports Trinity
   - Theological consultation confirms

3. **Decision Making**:
   - Use trial pronoun
   - Add footnote explaining theological interpretation
   - Document decision for consistency

**Tools Needed**:
- TBTA data presentation view
- Team discussion notes
- Decision documentation system

---

## 5. AI Integration Patterns

### Pattern 1: Query-Response Interface

**User Query**: "How should I translate 'we' in Acts 15:25 to Tagalog?"

**AI Response** (using TBTA):

```
In Acts 15:25, the Greek "ἡμῖν" (to us) is encoded as:

Person: First Exclusive
Context: Apostles and elders speaking to believers

Translation Recommendation:
✅ Use "kami" (exclusive we)
❌ Do not use "tayo" (inclusive we)

Reasoning:
- The apostles and elders made this decision
- They are informing the believers about it
- The believers were not part of the decision-making group
- Exclusive form correctly excludes the recipients

Similar verses to check:
- Acts 15:22 - also First Exclusive
- Acts 15:28 - also First Exclusive
```

**Implementation**:
- Query TBTA data
- Identify target language feature
- Provide explicit recommendation
- Give reasoning from linguistic data
- Suggest related verses

---

### Pattern 2: Feature Alert System

**Scenario**: AI detects translator working in Japanese

**AI Alert** (proactive):

```
📍 You're translating John 1:29

Feature Alert: Proximity Encoding Available

TBTA Data:
- Proximity: Near Speaker (John), Remote from Listener
- Speaker: John the Baptist
- Reference: Jesus (the Lamb of God)

Japanese Translation Note:
Consider using "あの" (ano) rather than "この" (kono)
- Jesus is at a distance from John
- Not immediately near the crowd

Would you like to see:
1. Context explanation?
2. Similar proximity examples?
3. Alternative interpretations?
```

**Implementation**:
- Detect language from user profile
- Scan TBTA for features relevant to that language
- Proactively alert when features present
- Offer contextual help

---

### Pattern 3: Translation Draft Generator

**User Request**: "Generate draft translation of Genesis 1:26 in Kilivila"

**AI Process**:

1. **Load TBTA Data**:
   ```yaml
   speaker: God
   number: Trial
   person: First Inclusive
   ```

2. **Load Language Profile**:
   ```yaml
   language: Kilivila
   number_system: [singular, dual, trial, plural]
   person_system: [inclusive, exclusive]
   ```

3. **Generate Draft**:
   ```
   Kilivila Draft Translation:

   "Let taitala [trial inclusive] make man..."

   Notes:
   - taitala = first person trial inclusive pronoun
   - Reflects Trinity as exactly 3 persons
   - Inclusive form reflects internal divine dialogue

   Verification needed:
   - Check trial pronoun form with language consultant
   - Verify theological understanding in Kilivila context
   ```

**Implementation**:
- Match TBTA features to language grammar
- Generate grammatically appropriate draft
- Flag areas needing human verification

---

### Pattern 4: Consistency Checker

**User Action**: Translator marks Acts 15:25 complete

**AI Check**:

```
⚠️ Consistency Check for "kami" (exclusive we) in Acts

You translated Acts 15:25 with "kami" (exclusive)

TBTA shows similar verses in Acts:
- Acts 15:22: First Exclusive ✓ (you used "kami")
- Acts 15:28: First Exclusive ⚠️ (you used "tayo" - inconsistent!)
- Acts 16:10: First Inclusive ✓ (you used "tayo")

Recommendation:
Review Acts 15:28 - should likely be "kami" to match context

Would you like to:
1. View all three verses in context?
2. See TBTA encoding for each?
3. Update Acts 15:28 now?
```

**Implementation**:
- Track translator's choices
- Compare against TBTA encoding
- Flag inconsistencies
- Suggest corrections

---

### Pattern 5: Learning Mode

**User**: "I don't understand why Acts 15:25 is exclusive"

**AI Tutorial**:

```
Let me explain First Inclusive vs First Exclusive:

Tagalog has two words for "we":
- TAYO = me + you (inclusive of listener)
- KAMI = me + others, but not you (exclusive of listener)

In Acts 15:25:
"It seemed good to us to send men to you"

Speaker: Apostles and elders in Jerusalem
Listener: Believers in Antioch

The decision was made BY the apostles (us)
The decision was sent TO the believers (you)

Since the listeners were NOT part of "us" making the decision,
this is EXCLUSIVE "we" = KAMI

Visual:
[Apostles + Elders] → decision → [Believers]
       KAMI                         TAYO would be wrong

Try it yourself:
Acts 15:28 - "It seemed good to the Holy Spirit and to us"
Is this KAMI or TAYO?

[Answer: KAMI - same context, same speakers/listeners]
```

**Implementation**:
- Detect confusion points
- Explain linguistic concept
- Show concrete application
- Provide practice examples
- Link to TBTA data

---

## 6. Transferable Patterns

### Pattern: Multi-Tier Feature Analysis

**Methodology** (applicable to any linguistic dataset):

1. **Tier 1: Word-Level**
   - Individual lexical items
   - Morphological features
   - Basic grammatical categories

2. **Tier 2: Phrase-Level**
   - Syntactic groupings
   - Semantic roles
   - Relational features

3. **Tier 3: Discourse-Level**
   - Pragmatic information
   - Speaker/listener features
   - Information structure

**Applied to Other Tools**:

**Example: Analyzing Semantic Domains**

Tier 1 (Word):
- Strong's number
- Lexical form
- Gloss

Tier 2 (Phrase):
- Louw-Nida domain
- Semantic field
- Collocations

Tier 3 (Discourse):
- Figurative usage
- Cultural context
- Pragmatic force

---

### Pattern: Cross-Linguistic Feature Mapping

**Methodology**:

1. **Identify Source Language Features**
   - Greek/Hebrew grammatical categories
   - Biblical language specific features

2. **Map to Universal Features**
   - Number (singular, dual, trial, plural, etc.)
   - Person (1, 2, 3, inclusive, exclusive, etc.)
   - Proximity (near, far, etc.)

3. **Encode for Target Languages**
   - Provide all distinctions needed
   - Let target language select relevant ones

**Applied to Other Tools**:

**Example: Analyzing Discourse Markers**

Source: Greek μὲν...δὲ (men...de) constructions
Universal: Contrast/comparison structure
Target: Varies by language
- English: "on one hand...on the other"
- Spanish: "por un lado...por otro"
- Japanese: は (topic marker) vs が (contrast)

Tool should encode UNIVERSAL pattern, let translator apply to target

---

### Pattern: Feature Combination Analysis

**Methodology**:

1. **Identify Individual Features**
   - List all atomic features
   - Define each clearly

2. **Identify Co-Occurrence Patterns**
   - Which features appear together?
   - Are some mutually exclusive?
   - Are some dependencies?

3. **Define Feature Packages**
   - Group related features
   - Document usage patterns
   - Provide examples

**Applied to Other Tools**:

**Example: Analyzing Prayer Language**

Individual Features:
- Vocative (addressing)
- Honorific register
- Request type
- Petitioner stance

Feature Package: "Prayer to God"
- Vocative: required
- Honorific: highest level
- Request: petition/praise/thanksgiving
- Stance: humble/reverent

Co-occurrence:
- Vocative + Honorific = 98% in prayer
- Vocative alone = rare (only intimate prayer)

---

### Pattern: Priority Tiering

**Methodology**:

1. **Tier A Criteria**:
   - Cannot be inferred from context
   - Affects large number of languages
   - Binary/discrete choice
   - High error rate if wrong

2. **Tier B Criteria**:
   - Sometimes inferable
   - Affects moderate number of languages
   - Context helps narrow choices
   - Medium error rate

3. **Tier C Criteria**:
   - Usually inferable
   - Affects few languages or specialized cases
   - Context sufficient for most uses
   - Low error rate

**Applied to Other Tools**:

**Example: Analyzing Textual Variants**

Tier A Variants:
- Change meaning significantly
- Affect theology
- Cannot infer correct reading from context
- Examples: John 1:18 "only God" vs "only Son"

Tier B Variants:
- Change wording but not core meaning
- Context helps determine reading
- Examples: word order changes

Tier C Variants:
- Spelling variations
- Synonyms with same meaning
- Minimal impact
- Examples: ἰησους vs ιησους

---

### Pattern: Concrete Example Generation

**Methodology**:

1. **Generic Feature Description**:
   - Define the feature abstractly
   - List possible values

2. **Biblical Example**:
   - Find verse where feature matters
   - Show feature encoding

3. **Translation Example**:
   - Pick specific target language
   - Show how feature affects translation
   - Explain reasoning

4. **Contrast Wrong Choice**:
   - Show what happens if feature ignored
   - Demonstrate error or ambiguity

**Template**:

```markdown
### Feature: {feature-name}

**Definition**: {abstract-definition}

**Example Verse**: {book} {chapter}:{verse}

**TBTA Encoding**:
```yaml
{feature}: {value}
```

**Translation to {language}**:
✅ Correct: {translation-with-feature}
❌ Wrong: {translation-without-feature}

**Impact**: {what-difference-it-makes}
```

**Applied to Other Tools**:

Use this template for ANY linguistic feature to make abstract concepts concrete

---

### Pattern: Language Family Clustering

**Methodology**:

1. **Survey Languages**:
   - Identify grammatical features per language family
   - Note patterns and clusters

2. **Create Feature Profiles**:
   - Group languages by shared needs
   - Document family-level patterns

3. **Optimize for Families**:
   - Austronesian → focus on person/number
   - East Asian → focus on proximity/honorifics
   - African → focus on noun class/salience
   - etc.

4. **Provide Family-Specific Guidance**:
   - "If translating to Austronesian language, pay attention to..."
   - "Common error in East Asian translations..."

**Applied to Other Tools**:

**Example: Analyzing Lexical Semantics**

Indo-European Languages:
- Strong distinction between continuous/completed
- Aspect more than tense

Sino-Tibetan Languages:
- Classifier systems
- Topic-prominent

Afro-Asiatic Languages:
- Root-pattern morphology
- Verbal noun systems

Tool should recognize language family and emphasize relevant features

---

## Conclusion

### Key Insights

1. **Language Families Have Predictable Needs**
   - Austronesian → person/number systems
   - East Asian → proximity/honorifics
   - PNG → trial/switch-reference
   - Pattern recognition enables optimization

2. **Features Cluster into Packages**
   - Honorifics = demographics + age + attitude + style
   - Demonstratives = proximity + tracking + role
   - Narrative = time + salience + genre
   - Package-aware tools are more efficient

3. **Priority Tiers Are Validated**
   - Tier A features cannot be inferred (must remain)
   - Tier B features sometimes inferable (correct placement)
   - Tier C features usually inferable (appropriate)
   - Exception: Implicit Info should move to Tier B

4. **Workflows Are Concrete and Actionable**
   - Pre-translation: language profiling + feature scanning
   - During: verse-by-verse consultation
   - Post: consistency checking + team review
   - AI integration enhances each stage

5. **Patterns Are Transferable**
   - Multi-tier analysis applies broadly
   - Cross-linguistic mapping is general method
   - Feature packages work for any domain
   - Priority tiering works for any dataset

### Recommendations for Implementation

1. **Build Language Family Filters**
   - Let translators select language → auto-highlight relevant features
   - "Working in Tagalog? Here are your critical features..."

2. **Create Feature Package Queries**
   - "Show all honorific packages in Luke"
   - "Show all demonstrative packages in John"

3. **Implement Workflow Tools**
   - Pre-translation checklist generator
   - Verse-by-verse feature viewer
   - Post-translation consistency checker

4. **Design AI Integration**
   - Query-response for specific questions
   - Alert system for relevant features
   - Consistency checking across chapters
   - Learning mode for education

5. **Apply Patterns to Other Tools**
   - Use multi-tier approach for semantic domains
   - Use feature packages for discourse markers
   - Use priority tiering for textual variants
   - Use concrete examples for all features

### Next Steps

1. Implement language family profiles
2. Create feature package query system
3. Build translation workflow tools
4. Design AI integration interface
5. Extract transferable patterns into generic template
6. Apply learnings to next Bible study tool
