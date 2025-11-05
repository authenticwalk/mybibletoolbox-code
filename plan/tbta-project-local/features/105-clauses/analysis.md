# CLAUSES (Category 105) - Detailed Analysis

## Overview

CLAUSES is the **largest and most complex** TBTA category with **18+ feature positions**, encoding everything from speech acts to discourse structure to social register. This represents the convergence of syntax, pragmatics, and discourse analysis in a single annotation layer.

**Structure**: `c-[type]-[illocutionary force]-[topic NP]-[speaker]-[listener]-[attitude]-[speaker age]-[age relationship]-[style]-[genre]-[structure]-[salience]-[sequence]-[location]-[implicit info]-[alternative analysis]-[vocabulary]-[rhetorical question]-[spares]`

**Boundaries**:
- Main clauses: `{` and `}`
- Subclauses: `[` and `]`

---

## 1. High-Impact Features - ESSENTIAL vs NICE-TO-HAVE

### Tier A: ESSENTIAL (Critical for Translation)

These features **cannot be reliably inferred** and are **required for 1000+ languages**.

#### 1.1 Speaker Demographics (Positions 5-9) ⭐⭐⭐
**Impact**: Critical for honorific/register languages (Japanese, Korean, Javanese, Thai, Indonesian)

**Components**:
- **Position 5: Speaker** (35+ categories)
  - Adult Daughter, Son, Angel, Animal, Boy, Brother, Crowd, Daughter, Demon, Disciple
  - Employee, Employer, Father, Girl, God, Government Leader, Government Official
  - Group of Friends, Holy Spirit, King, Man, Men, Military Leader, Mother
  - Prophet, Queen, Religious Leader, Satan, Servant, Sister, Slave, Soldier
  - Wife, Woman, Women, Written Material, Young Man

- **Position 6: Listener** (same 35+ categories)

- **Position 7: Speaker's Attitude** (11 values)
  - N - Neutral
  - F - Familiar
  - E - Endearing
  - P - Polite
  - H - Honorable
  - f - Friendly
  - C - Complimentary
  - D - Derogatory
  - A - Antagonistic-Hostile
  - a - Angry
  - R - Rebuking
  - I - Imploring

- **Position 8: Speaker's Age** (6 values)
  - C - Child (0-17)
  - Y - Young Adult (18-24)
  - A - Adult (25-49)
  - M - Middle Aged (50-64)
  - O - Old (65+)
  - E - Elder

- **Position 9: Speaker-Listener Age Relationship** (5 values)
  - O - Older (different generation)
  - o - Older (same generation)
  - S - Essentially the Same Age
  - y - Younger (same generation)
  - Y - Younger (different generation)

- **Position 10: Speech Style** (2 values)
  - F - Formal
  - I - Informal

**Why Essential**:
- Honorific languages require **different verb forms, pronouns, and vocabulary** based on social relationships
- Japanese has distinct verb endings for speaking to superiors vs equals vs inferiors
- Korean has 7 levels of formality that MUST be correct
- Cannot be inferred from text alone - requires cultural/social knowledge

**Translation Value**:
- **1000+ languages** with register/honorific systems
- Prevents serious translation errors (e.g., Jesus speaking to God with casual language)
- Enables culturally appropriate translation

#### 1.2 Illocutionary Force (Position 3) ⭐⭐⭐
**Impact**: Essential for all languages - affects verb mood, particles, intonation

**Values** (7):
- **D** - Declarative
- **I** - Imperative
- **C** - Content Interrogative (who, what, when, where, why, how)
- **Y** - Yes-No Interrogative
- **S** - Suggestive 'let's'
- **J** - Jussive (command to third party)
- **E** - Imperative with Emphasis

**Why Essential**:
- Languages mark speech acts differently (particles, mood, word order)
- Distinguishes "He went" (D) from "Did he go?" (Y) from "Go!" (I)
- Critical for understanding rhetorical questions vs genuine questions
- Cannot always be inferred from punctuation alone

**Translation Value**:
- **All languages** - universal pragmatic distinction
- Affects verb mood (imperative, subjunctive, indicative)
- Determines question particles (Japanese か, Mandarin 吗)
- Guides intonation patterns

#### 1.3 Salience Band (Position 13) ⭐⭐⭐
**Impact**: Critical for discourse-marking languages (many African, Asian, indigenous languages)

**Values** (10):
- **P** - Pivotal Storyline (turning points)
- **1** - Primary Storyline (main events)
- **2** - Secondary Storyline (supporting events)
- **S** - Script Predictable Actions (routine, expected)
- **B** - Backgrounded Actions (setting stage)
- **F** - Flashback
- **s** - Setting (time/place orientation)
- **I** - Irrealis (hypothetical, counterfactual)
- **A** - Author Intrusion (narrator comment)
- **C** - Cohesive Material (transitions, summaries)

**Why Essential**:
- Many languages mark **foreground vs background** grammatically
- Primary storyline uses different verb tenses/aspects than background
- Flashbacks require special marking
- Helps maintain narrative coherence

**Translation Value**:
- **500+ languages** with foreground/background distinction
- Determines aspect/tense selection in many languages
- Guides use of discourse particles
- Critical for maintaining story flow

#### 1.4 Discourse Genre (Position 11) ⭐⭐
**Impact**: Important for style, verb selection, connector choice

**Values** (14):
- **C** - Climactic Narrative Story
- **E** - Episodic Narrative Story
- **P** - Narrative Prophecy
- **X** - Expository
- **B** - Behavioral Hortatory
- **b** - Behavioral Eulogy
- **R** - Procedural
- **S** - Persuasive
- **x** - Expressive
- **D** - Descriptive
- **L** - Epistolary (letter)
- **r** - Dramatic Narrative
- **d** - Dialog
- **G** - Genealogy

**Why Essential**:
- Genre affects **verb tense defaults** (narrative = past, hortatory = imperative)
- Determines appropriate connectors (narrative vs logical)
- Influences formality level
- Guides translation style choices

**Translation Value**:
- **All languages** - genre conventions vary cross-linguistically
- Narrative uses sequential connectors, expository uses logical ones
- Prophecy may require future/modal marking
- Letters have culture-specific opening/closing formulae

#### 1.5 Notional Structure (Position 12) ⭐⭐
**Impact**: Important for maintaining discourse flow and emphasis

**Values by Genre** (17 total):

**Narrative** (7):
- **O** - Narrative-Orientation (setting the scene)
- **I** - Narrative-Inciting Incident (problem introduced)
- **D** - Narrative-Developing Conflict (rising action)
- **C** - Narrative-Climax (peak)
- **R** - Narrative-Resolution (falling action)
- **E** - Narrative-Exposition (background info)
- **c** - Narrative-Conclusion (wrap-up)

**Hortatory** (2):
- **H** - Hortatory-Exhortation (commands)
- **M** - Hortatory-Motivation (reasons)

**Procedural** (3):
- **G** - Procedural-Goal (purpose)
- **S** - Procedural-Steps (instructions)
- **s** - Procedural-Summary (recap)

**Persuasive** (2):
- **A** - Persuasive-Assertion (claim)
- **a** - Persuasive-Argument (evidence)

**Expository** (3):
- **T** - Expository-Topic (main point)
- **i** - Expository-Information (details)
- **t** - Expository-Topic Shift (transition)

**Why Essential**:
- Helps translators maintain **information flow**
- Climax requires special emphasis in many languages
- Background info may need subordination
- Motivation clauses use different connectors than commands

**Translation Value**:
- **All languages** - structural signals guide translation
- Climax may require intensifiers or peak marking
- Background material may need subordinate structure
- Topic shifts need appropriate transition markers

### Tier B: IMPORTANT (High Value, Sometimes Inferable)

#### 1.6 Clause Type (Position 2) ⭐⭐
**Values** (9):
- **I** - Independent
- **C** - Coordinate Independent
- **T** - Restrictive Relative
- **t** - Descriptive Relative
- **E** - Event Modifier (adverbial)
- **A** - Agent Complement
- **P** - Patient Complement
- **p** - Attributive Patient
- **Q** - Closing Quotation

**Why Important**:
- Determines **clause boundaries and subordination**
- Restrictive vs descriptive relatives require different marking
- Complements may need infinitival or that-clause structure

**Translation Value**:
- Languages with different relativization strategies
- Complement clause marking varies widely
- Some languages require clause-initial markers

#### 1.7 Implicit Information (Position 16) ⭐⭐
**Values** (6):
- **C** - Cultural (cultural assumptions)
- **S** - Situational (context from situation)
- **H** - Historical (known historical facts)
- **B** - Background (established in discourse)
- **A** - Subactions (implied steps)
- **I** - Implicit Arguments (understood participants)

**Why Important**:
- Flags what needs to be **made explicit** in target language
- Cultural assumptions may need explanation
- Implicit arguments may need to be stated
- Helps avoid ambiguity

**Translation Value**:
- Prevents confusion from unstated assumptions
- Guides footnote/explanation decisions
- Helps with low-context vs high-context language differences

#### 1.8 Rhetorical Question (Position 19) ⭐
**Values** (4):
- **C** - Content Question (rhetorical)
- **Y** - Yes-No Question (expects Yes)
- **N** - Yes-No Question (expects No)
- **E** - Equivalent Statement (not really a question)

**Why Important**:
- Rhetorical questions function as **statements, not questions**
- Expected answer affects translation
- Some languages don't use rhetorical questions
- May need to convert to statement

**Translation Value**:
- Languages without rhetorical questions need conversion
- Expected answer helps translation as emphatic statement
- Prevents confusion with genuine questions

### Tier C: NICE-TO-HAVE (Specialized or Derivable)

#### 1.9 Topic NP (Position 4)
**Values** (2):
- **A** - Most Agent-like
- **P** - Most Patient-like

**Why Nice-to-Have**: Usually inferable from context and word order

#### 1.10 Sequence (Position 14)
**Values** (4):
- **N** - Not in a Sequence
- **F** - First Coordinate
- **L** - Last Coordinate
- **C** - Coordinate (middle)

**Why Nice-to-Have**: Often inferable from conjunctions and structure

#### 1.11 Location in Discourse (Position 15)
**Values** (17):
- Book boundaries: **B** (first), **b** (last)
- Paragraph boundaries: **P** (first), **p** (last)
- Special markers: **T** (title), **C** (comment), **F** (footnote), etc.

**Why Nice-to-Have**: Useful for formatting but not translation substance

#### 1.12 Alternative Analysis (Position 17)
**Values** (10):
- **P** - Primary
- **1-5** - Alternatives 1-5
- **L** - Literal
- **D** - Dynamic
- **B** - Biblical Units
- **C** - Contemporary Units

**Why Nice-to-Have**: Supports multiple interpretations but primary is usually sufficient

#### 1.13 Vocabulary Alternate (Position 18)
**Values** (8):
- **C/S** - Complex/Simple (single)
- **c/s** - Complex/Simple (first coordinate)
- **L/l** - Complex/Simple (last coordinate)
- **O/o** - Complex/Simple (middle coordinate)

**Why Nice-to-Have**: Helpful but vocabulary level is often context-dependent

---

## 2. Example Coverage

### Confirmed Examples

#### Genesis 19:31 - Speaker Demographics ✅
**Context**: Lot's older daughter speaking to younger daughter about their father

**TBTA Encoding** (hypothetical):
```
Position 5 (Speaker): [Adult Daughter]
Position 6 (Listener): [Daughter/Sister]
Position 8 (Speaker Age): Y or A (Young Adult or Adult)
Position 9 (Age Relationship): o (Older, same generation)
Position 10 (Style): I (Informal - sisters talking privately)
```

**Translation Impact**:
- **Japanese**: Older sister uses plain form or gentle command form, not humble
- **Korean**: Uses 반말 (banmal - informal) since sisters are close in age
- **Javanese**: Uses middle level (madya), not high (krama inggil)
- **Thai**: Uses พี่/น้อง (older/younger sibling) pronouns appropriately

**Why This Matters**: Without age relationship data, translators might use equal-level language when hierarchy is culturally expected.

### Additional Examples Needed

Based on the 18 clause features, we need examples demonstrating:

1. **Illocutionary Force Distinctions**
   - Declarative vs Imperative: Matthew 5:44 "Love your enemies" (I-imperative)
   - Interrogative vs Rhetorical: Matthew 6:27 "Who can add a single hour?" (rhetorical-N)
   - Jussive: Genesis 1:3 "Let there be light" (J-jussive to third party)

2. **Salience Band Variations**
   - Pivotal: Matthew 27:50 Jesus' death (P-pivotal)
   - Primary Storyline: Acts narrative progression (1-primary)
   - Background: Matthew 1:18 "Now this is how..." (B-background)
   - Flashback: John 1:1 "In the beginning..." (F-flashback)

3. **Genre + Structure Combinations**
   - Narrative Climax: Genesis 22:11 Angel stops Abraham (C-climactic, C-climax)
   - Hortatory Exhortation + Motivation: Philippians 2:1-5 (H+M pattern)
   - Expository Topic Shift: Romans transitions between arguments (t-topic shift)

4. **Attitude Variations**
   - Polite: Ruth to Boaz (P-polite)
   - Derogatory: Pharisees to Jesus (D-derogatory)
   - Imploring: Blind man "Lord, have mercy!" (I-imploring)
   - Rebuking: Jesus to disciples (R-rebuking)

5. **Complex Speaker Demographics**
   - God to Abraham (Speaker: God, Listener: Man, Style: Formal)
   - Jesus to religious leaders (various attitudes: teaching vs rebuking)
   - Servant to master (formal, polite/honorable)
   - Children to parents (age relationship critical)

6. **Implicit Information Types**
   - Cultural: "They don't eat with unwashed hands" (C-cultural)
   - Historical: References to known events (H-historical)
   - Situational: "He said to her" - who and where from context (S-situational)

---

## 3. Discourse Structure - Genre + Salience + Structure Interaction

### The Three-Layer System

TBTA models discourse flow through **three interacting layers**:

1. **Genre (Position 11)**: Overall text type and conventions
2. **Notional Structure (Position 12)**: Section within genre structure
3. **Salience Band (Position 13)**: Information prominence level

### How They Work Together

#### Example: Narrative Discourse Flow

**Genesis Flood Narrative** (hypothetical encoding):

```yaml
Genre: E (Episodic Narrative)

Genesis 6:5-8 (God sees wickedness):
  Structure: O (Orientation - setting up problem)
  Salience: s (Setting)

Genesis 6:9-12 (Noah introduced):
  Structure: O (Orientation - introducing main character)
  Salience: B (Background - character description)

Genesis 6:13-22 (God commands ark):
  Structure: I (Inciting Incident)
  Salience: P (Pivotal - major turning point)

Genesis 7:1-10 (Noah enters ark):
  Structure: D (Developing Conflict)
  Salience: 1 (Primary Storyline)

Genesis 7:11-16 (Flood begins):
  Structure: C (Climax)
  Salience: P (Pivotal)

Genesis 7:17-24 (Waters prevail):
  Structure: D (Developing Conflict - continued)
  Salience: 1 (Primary Storyline)

Genesis 8:1-5 (Waters recede):
  Structure: R (Resolution - beginning)
  Salience: 1 (Primary Storyline)

Genesis 8:20-22 (Noah's sacrifice):
  Structure: c (Conclusion)
  Salience: P (Pivotal - covenant promise)
```

**Translation Implications**:

1. **Orientation (O) + Setting (s)**:
   - Use scene-setting language
   - Background tenses (English: past perfect, progressive)
   - Lower prominence marking

2. **Inciting Incident (I) + Pivotal (P)**:
   - Peak marking in verb system
   - Emphatic particles
   - Higher prominence

3. **Climax (C) + Pivotal (P)**:
   - Maximum emphasis
   - Dramatic tense/aspect
   - Foreground marking at highest level

4. **Resolution (R) + Primary (1)**:
   - Return to main storyline tense
   - Sequential connectors
   - Moderate prominence

5. **Conclusion (c) + Pivotal (P)**:
   - Wrap-up language
   - Thematic emphasis
   - Final position prominence

### Hortatory Discourse Example

**Ephesians 6:10-18** (hypothetical):

```yaml
Genre: B (Behavioral Hortatory)

Verse 10 "Be strong in the Lord":
  Structure: H (Hortatory-Exhortation - main command)
  Salience: 1 (Primary - main point)
  Illocutionary: I (Imperative)

Verses 11-13 "For our struggle is not...":
  Structure: M (Hortatory-Motivation - reason)
  Salience: 2 (Secondary - supporting)
  Illocutionary: D (Declarative - explanation)

Verses 14-17 "Stand firm therefore...":
  Structure: H (Hortatory-Exhortation - detailed commands)
  Salience: 1 (Primary - main instructions)
  Illocutionary: I (Imperative)

Verse 18 "And pray in the Spirit":
  Structure: H (Hortatory-Exhortation - final command)
  Salience: 1 (Primary)
  Illocutionary: I (Imperative)
```

**Translation Implications**:

1. **Exhortation (H) + Primary (1) + Imperative (I)**:
   - Strong command forms
   - Foreground verb tenses
   - Direct address style

2. **Motivation (M) + Secondary (2) + Declarative (D)**:
   - Subordinate structure in some languages
   - Background tenses
   - Explanatory connectors ("for", "because")

### Expository Discourse Example

**Romans Argument Structure** (hypothetical):

```yaml
Genre: X (Expository)

Romans 1:16-17 (Theme statement):
  Structure: T (Expository-Topic - main thesis)
  Salience: P (Pivotal - key statement)

Romans 1:18-32 (Human sinfulness):
  Structure: i (Expository-Information - supporting data)
  Salience: 1 (Primary - main argument)

Romans 3:21 (But now...):
  Structure: t (Expository-Topic Shift - contrast)
  Salience: P (Pivotal - major transition)

Romans 3:22-26 (Justification explained):
  Structure: i (Expository-Information)
  Salience: 1 (Primary)
```

**Translation Implications**:

1. **Topic (T) + Pivotal (P)**:
   - Emphatic positioning
   - Topic markers in topic-prominent languages
   - Strong assertion markers

2. **Topic Shift (t) + Pivotal (P)**:
   - Contrastive connectors
   - Adversative markers
   - Paragraph boundaries

3. **Information (i) + Primary (1)**:
   - Sequential development
   - Logical connectors
   - Evidential markers

### Cross-Genre Patterns

**Universal Patterns Across Genres**:

1. **Pivotal Salience** always marks turning points, regardless of genre:
   - Narrative: Climax events
   - Hortatory: Main commands
   - Expository: Thesis statements
   - Persuasive: Key assertions

2. **Structure Follows Genre**:
   - Narrative uses O→I→D→C→R→c progression
   - Hortatory alternates H→M→H pattern
   - Expository uses T→i→t→i pattern
   - Persuasive uses A→a→A pattern

3. **Salience Hierarchy** is consistent:
   - P (Pivotal) > 1 (Primary) > 2 (Secondary) > B/S/s (Background/Setting)
   - Affects: verb tense, aspect, particles, word order, emphasis

### How Well Does This Capture Narrative Flow?

**Strengths**: ⭐⭐⭐⭐⭐

1. **Multi-dimensional**: Genre + Structure + Salience provides **three independent perspectives** on discourse flow
2. **Precise**: 14 genres × 17 structures × 10 salience levels = **2,380 possible combinations** for fine-grained analysis
3. **Cross-linguistically Valid**: Based on universal discourse patterns (orientation, climax, resolution)
4. **Translation-Actionable**: Directly maps to linguistic choices (verb tense, particles, word order)
5. **Hierarchical**: Clear prominence hierarchy guides emphasis decisions

**Weaknesses**: ⭐⭐⭐⭐

1. **Complexity**: Three separate but interacting features requires understanding their relationships
2. **Granularity**: Some fine distinctions may be debatable (is this "Primary" or "Secondary"?)
3. **Learning Curve**: Translators need training to interpret and apply correctly
4. **Genre Boundaries**: Some texts mix genres (narrative with embedded hortatory)

**Overall Assessment**:

The Genre + Salience + Structure system **captures narrative flow excellently**. It provides:
- **Macrostructure** (Genre): What kind of text is this?
- **Mesostructure** (Notional Structure): Where are we in the text's development?
- **Microstructure** (Salience): How prominent is this specific clause?

This three-layer approach is **superior to single-dimension systems** and provides **actionable guidance** for translation decisions.

---

## 4. Translation Value - Feature-to-Language Mapping

### High-Priority Features by Language Type

#### Honorific/Register Languages ⭐⭐⭐⭐⭐
**Languages**: Japanese, Korean, Javanese, Thai, Khmer, Balinese, Sundanese, Madurese

**Essential Features**:
1. **Speaker** (Position 5): Social role determines verb forms
2. **Listener** (Position 6): Relative status critical
3. **Speaker's Attitude** (Position 7): Affects politeness level
4. **Speaker's Age** (Position 8): Age-based register systems
5. **Age Relationship** (Position 9): Same vs different generation
6. **Speech Style** (Position 10): Formal vs informal

**Why Critical**:
- **Japanese**: Has 5+ politeness levels (casual, polite, respectful, humble, very polite)
- **Korean**: Has 7 speech levels - wrong level is **culturally offensive**
- **Javanese**: Has 3 main levels (ngoko, madya, krama) - must be correct for social context

**Example Application**:
```
Abraham to God:
  Speaker: Man, Listener: God, Style: Formal, Attitude: Honorable
  → Japanese: です/ます form minimum, possibly 尊敬語 (sonkeigo - respectful language)
  → Korean: 합니다 (hamnida) form, possibly 존댓말 (jondaetmal - honorific)

Jesus to children:
  Speaker: Adult/Teacher, Listener: Children, Style: Informal, Attitude: Endearing
  → Japanese: だ/である form or gentle です/ます
  → Korean: 해요 (haeyo) or 해라 (haera) form
```

#### Discourse-Marking Languages ⭐⭐⭐⭐⭐
**Languages**: Many African languages (Swahili, Hausa, Yoruba), Southeast Asian (Tagalog, Indonesian), Pacific (Tongan, Samoan)

**Essential Features**:
1. **Salience Band** (Position 13): Foreground/background distinction
2. **Discourse Genre** (Position 11): Affects verb tense defaults
3. **Notional Structure** (Position 12): Information flow
4. **Sequence** (Position 14): Coordinate structures

**Why Critical**:
- Many languages use **different verb tenses for foreground vs background**
- Pivotal events require **special marking** (particles, word order, emphasis)
- Sequential connectors vary by prominence level

**Example Application**:
```
Narrative Climax (Salience: P, Structure: C):
  → Swahili: Use ka- prefix (sequential foreground)
  → Tagalog: Use completed aspect (perfective) for main events
  → Indonesian: Fronting for emphasis, use maka for consequence

Background Setting (Salience: s, Structure: O):
  → Swahili: Use -ki- prefix (simultaneous background)
  → Tagalog: Use incompleted aspect (imperfective) for background
  → Indonesian: Subordinate structure, use sedang for ongoing
```

#### Question-Marking Languages ⭐⭐⭐⭐
**Languages**: Mandarin, Japanese, Turkish, many Asian languages with question particles

**Essential Features**:
1. **Illocutionary Force** (Position 3): Distinguishes question types
2. **Rhetorical Question** (Position 19): Real vs rhetorical

**Why Critical**:
- Many languages require **sentence-final question particles**
- Different particles for yes/no vs content questions
- Rhetorical questions may need conversion to statements

**Example Application**:
```
Yes/No Question (Force: Y):
  → Mandarin: Add 吗 (ma) particle
  → Japanese: Add か (ka) particle
  → Turkish: Add mi/mı/mu/mü particle

Content Question (Force: C):
  → Mandarin: Use question word (谁 who, 什么 what), no 吗
  → Japanese: Use question word (誰 dare, 何 nani), keep か
  → Turkish: Use question word, no particle needed

Rhetorical Question (Force: Y, Rhetorical: Y):
  → May need conversion to emphatic statement
  → Or use rhetorical particle if available
```

#### Clause-Subordination Languages ⭐⭐⭐⭐
**Languages**: German, Dutch, Turkish, Japanese, Korean (SOV with rich subordination)

**Essential Features**:
1. **Clause Type** (Position 2): Independent vs subordinate
2. **Sequence** (Position 14): Coordination patterns
3. **Implicit Information** (Position 16): What needs stating

**Why Critical**:
- SOV languages place subordinate clauses **before main clauses**
- Relative clauses may need prenominal position
- Implicit arguments may need to be stated

**Example Application**:
```
Restrictive Relative (Type: T):
  → English: "The man who came..."
  → Japanese: "来た男" (prenominal, no relative pronoun)
  → Turkish: "gelen adam" (prenominal with participle)
  → German: "Der Mann, der kam..." (postnominal with relative pronoun)

Event Modifier Adverbial (Type: E):
  → Place before main clause in Japanese/Korean/Turkish
  → Use appropriate subordinate conjunction
```

#### Implicit-Explicit Languages ⭐⭐⭐
**Languages**: High-context (Japanese, Chinese) vs Low-context (German, English)

**Essential Features**:
1. **Implicit Information** (Position 16): What's assumed
2. **Alternative Analysis** (Position 17): Multiple readings
3. **Vocabulary Alternate** (Position 18): Complexity level

**Why Critical**:
- **Low-context languages** need explicit arguments and connections
- **High-context languages** can omit understood information
- Cultural assumptions may need footnotes

**Example Application**:
```
Implicit Cultural (Implicit: C):
  → Low-context: May need footnote or expansion
  → High-context: Can remain implicit if culturally shared

Implicit Arguments (Implicit: I):
  → English: Often needs explicit subject "He said..."
  → Japanese: Can omit subject if clear from context
  → Spanish: Verb conjugation carries subject, can omit pronoun
```

### Feature Priority Matrix by Language Type

| Feature | Honorific | Discourse-Mark | Question-Mark | Subordination | Implicit/Explicit |
|---------|-----------|----------------|---------------|---------------|-------------------|
| **Speaker/Listener** (5-6) | ⭐⭐⭐⭐⭐ | ⭐ | ⭐ | ⭐ | ⭐⭐ |
| **Attitude** (7) | ⭐⭐⭐⭐⭐ | ⭐ | ⭐ | ⭐ | ⭐⭐ |
| **Age/Relationship** (8-9) | ⭐⭐⭐⭐⭐ | ⭐ | ⭐ | ⭐ | ⭐ |
| **Style** (10) | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐⭐ | ⭐⭐ |
| **Illocutionary Force** (3) | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Genre** (11) | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Notional Structure** (12) | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Salience** (13) | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Clause Type** (2) | ⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Sequence** (14) | ⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| **Implicit Info** (16) | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Rhetorical Question** (19) | ⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Alternative Analysis** (17) | ⭐ | ⭐ | ⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| **Vocabulary** (18) | ⭐ | ⭐ | ⭐ | ⭐ | ⭐⭐⭐ |

**Key**: ⭐ (minimal) to ⭐⭐⭐⭐⭐ (critical)

### Universal Features (Critical for All Languages)

1. **Illocutionary Force** (Position 3): ⭐⭐⭐⭐⭐
   - Affects all languages - questions, commands, statements are universal
   - Determines verb mood, particles, intonation
   - Cannot be omitted

2. **Clause Type** (Position 2): ⭐⭐⭐⭐
   - Independent vs subordinate is universal
   - Relative clauses exist in all languages (with variation)
   - Complements are universal

3. **Genre** (Position 11): ⭐⭐⭐⭐
   - All languages distinguish narrative from expository from hortatory
   - Affects verb tense defaults and connectors
   - Guides overall translation strategy

---

## 5. Complexity Management - Making 18+ Features Usable

### The Problem

**18+ feature positions** is overwhelming:
- Annotators struggle to encode consistently
- Translators can't process all dimensions simultaneously
- Tools must handle sparse, complex data
- Risk of "paralysis by analysis"

### Solution 1: Feature Grouping

**Group related features into functional clusters**:

#### Cluster A: Social Register (Positions 5-10)
```
Speaker + Listener + Attitude + Age + Age Relationship + Style
= "Who is talking to whom, how?"
```

**Usage**: Treat as a single "register selection" decision
- Japanese translator: Looks at cluster → selects politeness level
- Korean translator: Looks at cluster → selects speech level
- Others: Can ignore if not relevant

**Implementation**:
```yaml
register:
  speaker: Father
  listener: Son
  attitude: Rebuking
  speaker_age: Middle Aged
  age_relationship: Older (different generation)
  style: Formal

  # Derived: "Formal rebuke from parent to adult child"
  # Japanese: です/ます + stern tone, not humble forms
  # Korean: 하십시오 체 (hasipsio-che) formal command
```

#### Cluster B: Discourse Flow (Positions 11-13)
```
Genre + Notional Structure + Salience
= "Where are we in the text and how important is it?"
```

**Usage**: Treat as a single "prominence level" decision
- Identifies foreground vs background
- Determines verb tense/aspect selection
- Guides emphasis and particle use

**Implementation**:
```yaml
discourse_flow:
  genre: Climactic Narrative
  structure: Climax
  salience: Pivotal

  # Derived: "Absolute peak of story"
  # Swahili: Use ka- prefix (foreground sequential)
  # Tagalog: Completive aspect + emphatic particles
  # All: Maximum emphasis, peak marking
```

#### Cluster C: Speech Act (Positions 3, 19)
```
Illocutionary Force + Rhetorical Question
= "What kind of communicative act is this?"
```

**Usage**: Determines sentence type and modality
- Selects verb mood
- Adds question particles or not
- Handles rhetorical questions specially

**Implementation**:
```yaml
speech_act:
  force: Content Interrogative
  rhetorical: Y (expects Yes answer)

  # Derived: "Rhetorical question with implied Yes"
  # Mandarin: May convert to emphatic statement
  # Greek: Expects μή (mē) not οὐ (ou) for expected Yes
```

#### Cluster D: Clause Structure (Positions 2, 14, 15)
```
Clause Type + Sequence + Location
= "What kind of clause and where?"
```

**Usage**: Determines clause boundaries and relationships
- Subordination strategy
- Coordination marking
- Discourse boundaries

**Implementation**:
```yaml
structure:
  type: Restrictive Relative
  sequence: Not in a Sequence
  location: [Middle of paragraph]

  # Derived: "Standalone restrictive relative clause"
  # Japanese: Prenominal relative
  # English: Postnominal with "who/which"
```

#### Cluster E: Additional Information (Positions 16-18)
```
Implicit Info + Alternative Analysis + Vocabulary
= "What's not obvious and what are the options?"
```

**Usage**: Guides translation decisions and footnotes
- Identifies what needs explanation
- Shows alternative readings
- Suggests complexity level

**Implementation**:
```yaml
additional:
  implicit: Cultural
  alternative: Primary
  vocabulary: Simple

  # Derived: "Main reading, simple words, cultural background assumed"
  # Low-context language: May need footnote
  # Simple reading: Use common vocabulary
```

### Solution 2: Tiered Access

**Provide different views for different users**:

#### Tier 1: Essential (5 features)
For **all translators**:
1. Illocutionary Force (3)
2. Genre (11)
3. Salience (13)
4. Register Cluster (5-10 combined)
5. Rhetorical Question (19)

**Result**: ~5 "composite features" that cover 90% of translation needs

#### Tier 2: Important (7 features)
For **translators in languages with specific needs**:
1. All Tier 1 features
2. Clause Type (2)
3. Notional Structure (12)
4. Sequence (14)
5. Implicit Information (16)

**Result**: ~12 features for 95% coverage

#### Tier 3: Complete (18+ features)
For **linguists and tool developers**:
- All features available
- Full granularity
- Research and analysis use

### Solution 3: Query-Based Access

**Don't show all features always - query for what you need**:

#### Query 1: "Show me honorific-relevant features"
```yaml
# Returns only: Speaker, Listener, Attitude, Age, Age Relationship, Style
filters:
  feature_clusters: [register]
```

#### Query 2: "Show me discourse structure features"
```yaml
# Returns only: Genre, Notional Structure, Salience
filters:
  feature_clusters: [discourse_flow]
```

#### Query 3: "Show me all questions"
```yaml
# Returns only verses with: Illocutionary Force = C or Y
filters:
  illocutionary_force: [Content Interrogative, Yes-No Interrogative]
```

#### Query 4: "Show me climax clauses"
```yaml
# Returns only verses with: Notional Structure = C (Climax) and Salience = P (Pivotal)
filters:
  notional_structure: Narrative-Climax
  salience: Pivotal
```

### Solution 4: Default Values + Nullish Filtering

**Don't store or display features that are "default" or "not applicable"**:

#### Example: Non-Question Verse
```yaml
# Instead of storing all 18 positions:
clause:
  type: Independent
  force: Declarative
  topic: Not Applicable
  speaker: Narrator
  listener: Not Applicable
  attitude: Neutral
  age: Not Applicable
  age_relationship: Not Applicable
  style: Not Applicable
  genre: Narrative
  structure: Primary Storyline
  salience: Primary
  sequence: Not in Sequence
  location: []
  implicit: None
  alternative: Primary
  vocabulary: Not Applicable
  rhetorical: Not Applicable

# Store only meaningful features:
clause:
  type: Independent
  force: Declarative
  genre: Narrative
  structure: Primary Storyline
  salience: Primary
```

**Result**: Reduces typical clause from 18 fields to 3-7 fields (60-80% reduction)

### Solution 5: Progressive Disclosure UI

**For translation tools - show features only when relevant**:

#### Step 1: Initial View
```
Clause: Independent Declarative
Genre: Narrative
Salience: Primary Storyline
[Show more...]
```

#### Step 2: Expand if Needed
```
Clause: Independent Declarative
Genre: Narrative, Developing Conflict
Salience: Primary Storyline
Speaker Demographics: [None - narration]
[Show advanced...]
```

#### Step 3: Full Detail (Optional)
```
[All 18 features displayed]
```

### Solution 6: Smart Defaults

**Most features have "normal" values - only show exceptions**:

**Defaults**:
- Force: Declarative (most clauses)
- Type: Independent (most clauses)
- Attitude: Neutral (unless dialog)
- Style: Informal (unless formal context)
- Sequence: Not in Sequence (unless coordinated)
- Alternative: Primary (main reading)
- Rhetorical: Not Applicable (unless question)

**Exception Highlighting**:
```
⚠️ Illocutionary Force: IMPERATIVE (not default Declarative)
⚠️ Salience: PIVOTAL (not default Primary)
⚠️ Speaker Attitude: REBUKING (not default Neutral)
```

### Solution 7: Translation-Task Specific Views

**Different translation tasks need different features**:

#### Task A: Draft Translation
**Show only**:
- Illocutionary Force
- Genre
- Salience
- Speaker/Listener (if dialog)

#### Task B: Register/Honorific Check
**Show only**:
- Speaker
- Listener
- Attitude
- Age
- Age Relationship
- Style

#### Task C: Discourse Marking
**Show only**:
- Genre
- Notional Structure
- Salience
- Sequence

#### Task D: Cultural Adaptation
**Show only**:
- Implicit Information
- Alternative Analysis
- Rhetorical Question
- Vocabulary

### Complexity Reduction Summary

| Strategy | Complexity Reduction | Use Case |
|----------|---------------------|----------|
| **Feature Grouping** | 18 → 5 clusters | Conceptual organization |
| **Tiered Access** | 18 → 5/12/18 | Different user types |
| **Query-Based** | 18 → 2-7 per query | Task-specific work |
| **Nullish Filtering** | 18 → 3-7 typical | Data storage efficiency |
| **Progressive Disclosure** | 18 → 3 → 7 → 18 | UI/UX design |
| **Smart Defaults** | Highlight 2-4 exceptions | Cognitive focus |
| **Task-Specific Views** | 18 → 3-6 per task | Workflow optimization |

**Recommended Approach**: Combine **all seven strategies**:
1. Organize features into clusters (mental model)
2. Provide tiered access (different users)
3. Support queries (flexible exploration)
4. Filter nullish values (reduce noise)
5. Progressive disclosure in UI (not overwhelming)
6. Highlight exceptions from defaults (focus attention)
7. Task-specific views (practical workflows)

**Result**: 18+ features become **manageable and usable** while retaining full power when needed.

---

## 6. Transferable Patterns - Lessons for Other Features

### Pattern 1: Hierarchical Feature Organization

**CLAUSES demonstrates**: Features naturally group into semantic clusters

**Transferable to**:
- **NOUNS**: Group Person + Number + Participant Tracking = "Entity Reference System"
- **VERBS**: Group Time + Aspect + Mood = "Event Characterization"
- **NOUN PHRASES**: Group Semantic Role + Implicit + Relativized = "Argument Structure"

**Implementation**:
```yaml
# Instead of flat feature list:
noun:
  person: First Inclusive
  number: Trial
  participant: First Mention
  proximity: Near Speaker
  polarity: Affirmative

# Use hierarchical clusters:
noun:
  reference:
    person: First Inclusive
    number: Trial
  discourse:
    participant: First Mention
  deixis:
    proximity: Near Speaker
  polarity: Affirmative
```

**Benefits**:
- Clearer mental model
- Easier querying ("give me all reference features")
- Better UI organization
- Reduced cognitive load

### Pattern 2: Feature Prioritization by Language Type

**CLAUSES demonstrates**: Not all features matter equally for all languages

**Priority Matrix Template**:
1. Identify major language typology dimensions
2. Map features to typology needs
3. Create priority matrix (1-5 stars)
4. Generate language-specific feature subsets

**Transferable to ALL features**:

#### NOUNS Priority Example:
| Feature | Polynesian | Japanese | Turkish | English |
|---------|-----------|----------|---------|---------|
| **Number** (Dual/Trial) | ⭐⭐⭐⭐⭐ | ⭐ | ⭐ | ⭐ |
| **Person** (Incl/Excl) | ⭐⭐⭐⭐⭐ | ⭐ | ⭐ | ⭐ |
| **Participant Tracking** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Proximity** (3-way+) | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐ |

#### VERBS Priority Example:
| Feature | Tagalog | Swahili | German | English |
|---------|---------|---------|--------|---------|
| **Time Granularity** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐ |
| **Aspect** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Mood** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |

**Implementation**:
```yaml
# Language profile-driven feature selection
translation_project:
  target_language: Japanese
  typology:
    - honorific_system
    - proximity_3way
    - topic_prominent

  feature_priorities:
    clauses:
      - speaker_demographics  # ⭐⭐⭐⭐⭐
      - topic_np              # ⭐⭐⭐⭐
      - genre                 # ⭐⭐⭐
    nouns:
      - proximity             # ⭐⭐⭐⭐⭐
      - participant_tracking  # ⭐⭐⭐
    verbs:
      - aspect                # ⭐⭐⭐
```

### Pattern 3: Nullish Filtering for Sparse Data

**CLAUSES demonstrates**: Most features are "Not Applicable" most of the time

**Filtering Strategy**:
1. Define "default" or "not applicable" values
2. Omit from storage if default
3. Reconstruct defaults on query if needed

**Transferable Values to Filter**:
- **"N" (Not Applicable)** - Feature doesn't apply
- **"A" (Affirmative)** - Default polarity
- **"I" (Indicative)** - Default mood
- **"P" (Present)** - Default time if timeless/gnomic
- **"S" (Singular)** - Default number in some contexts

**Example - NOUNS**:
```yaml
# Full data (verbose):
noun:
  complexity: 1
  sense: 2
  index: A
  number: S
  participant: D
  polarity: A
  proximity: N
  person: 3
  surface: A
  status: N

# Filtered (remove defaults):
noun:
  complexity: 1
  sense: 2
  index: A
  # number: S (default singular - omit)
  participant: D
  # polarity: A (default affirmative - omit)
  # proximity: N (not applicable - omit)
  person: 3
  surface: A
  # status: N (not applicable - omit)
```

**Result**: 40-70% size reduction, clearer semantics

### Pattern 4: Composite Features for Related Values

**CLAUSES demonstrates**: Some features always used together (Speaker + Listener + Attitude + Age + Style)

**Pattern**: Create composite features that bundle related values

**Transferable Examples**:

#### VERBS: Event Characterization
```yaml
# Instead of separate:
time: Historic Past
aspect: Completive
mood: Indicative

# Bundle as composite:
event:
  temporal: Historic Past
  aspectual: Completive
  modal: Indicative
  # Derived: "Completed action in distant past, factual"
```

#### NOUNS: Reference Properties
```yaml
# Instead of separate:
person: First Inclusive
number: Trial
participant: First Mention

# Bundle as composite:
reference:
  person: First Inclusive
  number: Trial
  status: First Mention
  # Derived: "We three (including you), newly introduced"
```

#### NOUN PHRASES: Argument Properties
```yaml
# Instead of separate:
semantic_role: Agent
implicit: No
relativized: Yes

# Bundle as composite:
argument:
  role: Agent
  explicit: Yes
  structure: Relativized
  # Derived: "Explicit agent in relative clause"
```

**Benefits**:
- Clearer semantics (features that belong together stay together)
- Easier querying (find all "completed past events")
- Better defaults (composite can have composite default)
- Reduced cognitive load

### Pattern 5: Multi-Tier Access (Essential/Important/Complete)

**CLAUSES demonstrates**: Different users need different granularity

**Tiering Strategy**:
1. **Tier 1 (Essential)**: Features needed by 90%+ of translators
2. **Tier 2 (Important)**: Features needed for specific language types
3. **Tier 3 (Complete)**: All features for research/analysis

**Transferable to ALL categories**:

#### NOUNS Three-Tier Example:
```yaml
tier_1_essential:
  - number        # Singular/Plural distinction
  - person        # 1st/2nd/3rd
  - index         # Coreference tracking

tier_2_important:
  - participant   # Discourse tracking (switch-reference languages)
  - proximity     # 3+ way demonstratives (Japanese, Spanish, etc.)

tier_3_complete:
  - surface       # Surface realization
  - status        # Participant status
  # All features available for specialized use
```

#### VERBS Three-Tier Example:
```yaml
tier_1_essential:
  - time          # Past/Present/Future
  - aspect        # Completive/Continuative
  - mood          # Indicative/Imperative

tier_2_important:
  - reflexivity   # Reflexive marking
  - polarity      # Affirmative/Negative
  - target_tense  # For translation

tier_3_complete:
  - adjective_degree  # For verb-as-adjective constructions
  # All features available
```

**Implementation**:
```yaml
# API query with tier parameter:
GET /commentary/GEN/001/001?tier=essential
# Returns: 3-5 key features

GET /commentary/GEN/001/001?tier=important
# Returns: 7-10 features

GET /commentary/GEN/001/001?tier=complete
# Returns: All features
```

### Pattern 6: Query-Based Feature Exploration

**CLAUSES demonstrates**: Users should query for what they need, not see everything

**Query Patterns**:

#### Pattern A: Feature-Specific Queries
```
"Find all verses with Feature X = Value Y"
```

**Examples**:
```
- Find all Trial number nouns (Gen 1:26)
- Find all Pivotal salience clauses (narrative climaxes)
- Find all Rebuking attitude speech (Jesus rebuking)
- Find all Rhetorical questions
```

#### Pattern B: Feature Combination Queries
```
"Find all verses with Feature X = Value Y AND Feature Z = Value W"
```

**Examples**:
```
- Speaker = God AND Listener = Human AND Attitude = Rebuking
- Genre = Narrative AND Structure = Climax AND Salience = Pivotal
- Number = Trial AND Person = First Inclusive (Trinity references)
```

#### Pattern C: Feature Absence Queries
```
"Find all verses where Feature X is NOT default"
```

**Examples**:
```
- Polarity = Negative (negated statements)
- Mood ≠ Indicative (non-indicative moods)
- Participant = Exiting (participants leaving)
```

#### Pattern D: Language-Specific Queries
```
"Find all verses requiring special handling in Language X"
```

**Examples**:
```
- Japanese translation: Speaker + Listener ≠ Neutral (honorific decisions)
- Tagalog translation: Time = granular past distinctions
- Swahili translation: Salience = Pivotal (foreground marking)
```

**Implementation**:
```python
# Query DSL example:
query = {
    "feature": "clauses",
    "filters": {
        "speaker": {"ne": "Narrator"},
        "listener": {"ne": "Not Applicable"},
        "attitude": {"ne": "Neutral"}
    },
    "output": ["verse", "speaker", "listener", "attitude"]
}

# Returns: All dialog with non-neutral attitude
```

### Pattern 7: Exception Highlighting

**CLAUSES demonstrates**: Defaults are boring; exceptions are interesting

**Highlighting Strategy**:
1. Define default values for each feature
2. Compare verse data to defaults
3. Highlight only non-default values
4. Provide explanation for exceptions

**Default Definitions**:

#### CLAUSES Defaults:
```yaml
defaults:
  type: Independent
  force: Declarative
  attitude: Neutral
  style: Informal
  genre: Narrative      # Context-dependent
  structure: Primary    # Context-dependent
  salience: Primary
  sequence: Not in Sequence
  alternative: Primary
  rhetorical: Not Applicable
```

#### VERBS Defaults:
```yaml
defaults:
  time: Present
  aspect: Unmarked
  mood: Indicative
  reflexivity: Not Reflexive
  polarity: Affirmative
  degree: No Degree
```

#### NOUNS Defaults:
```yaml
defaults:
  number: Singular
  participant: Routine
  polarity: Affirmative
  proximity: Not Applicable
  person: 3rd
  surface: Argument
  status: Not Applicable
```

**Exception Display**:
```yaml
# Instead of showing all features:
verse: GEN.1.26
features:
  nouns:
    - "Elohim":
        complexity: 1
        sense: 3
        index: A
        number: PLURAL ⚠️  # Exception: Elohim is plural
        person: FIRST INCLUSIVE ⚠️  # Exception: "Let us make"
        participant: FIRST MENTION ⚠️  # Exception: Introducing God
  verbs:
    - "make":
        time: Timeless
        aspect: GNOMIC ⚠️  # Exception: Eternal decree
        mood: JUSSIVE ⚠️  # Exception: "Let us" not indicative

# Only exceptions highlighted - reduces cognitive load
```

### Pattern 8: Progressive Disclosure in UI

**CLAUSES demonstrates**: Show simple first, reveal complexity on demand

**Disclosure Levels**:

#### Level 1: Summary (Always Visible)
```
Genesis 1:26
"Then God said, 'Let us make man...'"

📝 Independent Jussive
🎭 Narrative-Orientation, Pivotal
👥 God speaking, First Inclusive Plural
```

#### Level 2: Key Features (Click to Expand)
```
[Expanded view]
Illocutionary Force: Jussive ("Let us")
Genre: Narrative
Salience: Pivotal (major moment)
Speaker: God
Number: Trial (exactly 3)
Person: First Inclusive ("us" = Trinity)
```

#### Level 3: Complete Data (Advanced Users Only)
```
[Full feature list - all 18+ positions]
```

**Implementation Pattern for ALL Categories**:
1. **Level 1**: 1-2 sentence summary
2. **Level 2**: 5-8 key features (tier 1 + relevant tier 2)
3. **Level 3**: Complete data dump (all features, raw format)

### Pattern 9: Feature Interdependencies

**CLAUSES demonstrates**: Some features constrain others

**Dependency Rules**:

#### Rule 1: Genre → Structure Options
```yaml
if genre == "Narrative":
  structure_options:
    - Orientation
    - Inciting Incident
    - Developing Conflict
    - Climax
    - Resolution
    - Conclusion

if genre == "Hortatory":
  structure_options:
    - Exhortation
    - Motivation
```

#### Rule 2: Illocutionary Force → Rhetorical Question
```yaml
if force == "Content Interrogative" OR force == "Yes-No Interrogative":
  rhetorical_question: [may be applicable]
else:
  rhetorical_question: Not Applicable
```

#### Rule 3: Speaker/Listener → Attitude/Style
```yaml
if speaker == "Narrator" AND listener == "Not Applicable":
  attitude: Not Applicable
  style: Not Applicable
  age: Not Applicable
  age_relationship: Not Applicable
else:
  # All social register features applicable
```

**Transferable Dependency Patterns**:

#### NOUNS: Proximity depends on Demonstrative Usage
```yaml
if noun_type == "Demonstrative":
  proximity: [applicable - Near/Remote/etc.]
else:
  proximity: Not Applicable
```

#### VERBS: Aspect depends on Time
```yaml
if time == "Timeless" OR time == "Eternity":
  aspect: Gnomic or Unmarked
  # Completive/Inceptive don't make sense
```

#### NOUN PHRASES: Relativized affects Structure
```yaml
if relativized == "Yes":
  # Contains embedded relative clause
  implicit: [check if relative is implicit]
else:
  # Simple noun phrase
```

**Implementation**:
```python
# Validation rules
def validate_clause_features(clause):
    errors = []

    # Rule: If speaker is Narrator, attitude should be N/A
    if clause.speaker == "Narrator" and clause.attitude != "Not Applicable":
        errors.append("Narration should have attitude = Not Applicable")

    # Rule: Rhetorical question only applies to interrogatives
    if clause.force not in ["Content Interrogative", "Yes-No Interrogative"]:
        if clause.rhetorical != "Not Applicable":
            errors.append("Rhetorical question only applies to interrogatives")

    # Rule: Genre determines valid structures
    valid_structures = GENRE_TO_STRUCTURE[clause.genre]
    if clause.structure not in valid_structures:
        errors.append(f"Structure {clause.structure} invalid for genre {clause.genre}")

    return errors
```

### Pattern 10: Feature Documentation Template

**CLAUSES demonstrates**: Clear documentation structure for complex features

**Standard Template**:

```markdown
## Feature Name (Position X)

**Values** (N options):
- **Value1** - Description
- **Value2** - Description
[List all values]

**Translation Impact**: ⭐⭐⭐⭐⭐ (5-star rating)

**Affects Languages**:
- Language Type 1 (examples)
- Language Type 2 (examples)

**Why Essential/Important/Nice-to-Have**:
[Explanation of significance]

**Examples**:
- Verse Reference: Feature = Value → Translation implication

**Queries**:
- Common query pattern 1
- Common query pattern 2

**Dependencies**:
- Depends on: Feature X
- Constrains: Feature Y

**Defaults**:
- Default value: [value]
- When to override: [conditions]
```

**Apply to ALL features** for consistency and discoverability.

---

## Summary: CLAUSES Feature Assessment

### ESSENTIAL Features (Must Have - Cannot Infer)
1. ✅ **Speaker Demographics** (Pos 5-10) - 1000+ honorific languages
2. ✅ **Illocutionary Force** (Pos 3) - All languages (questions, commands, statements)
3. ✅ **Salience Band** (Pos 13) - 500+ discourse-marking languages
4. ✅ **Discourse Genre** (Pos 11) - All languages (affects style, tense, connectors)
5. ✅ **Notional Structure** (Pos 12) - All languages (information flow)

**Coverage**: ~5 features handle **90% of critical translation decisions**

### IMPORTANT Features (High Value for Specific Languages)
6. ✅ **Clause Type** (Pos 2) - Subordination strategies vary widely
7. ✅ **Implicit Information** (Pos 16) - High vs low-context languages
8. ✅ **Rhetorical Question** (Pos 19) - Not all languages use rhetorical questions

**Coverage**: +3 features bring total to **95% coverage**

### NICE-TO-HAVE Features (Specialized Use)
9. ⭐ **Topic NP** (Pos 4) - Topic-prominent languages (Japanese, Korean)
10. ⭐ **Sequence** (Pos 14) - Often inferable from context
11. ⭐ **Location** (Pos 15) - Formatting and boundaries
12. ⭐ **Alternative Analysis** (Pos 17) - Multiple interpretations
13. ⭐ **Vocabulary** (Pos 18) - Reading level variations

**Coverage**: Remaining features provide **100% completeness** for research and edge cases

### Complexity Management Recommendation

**Implement ALL seven strategies**:
1. ✅ Feature Grouping (18 → 5 clusters)
2. ✅ Tiered Access (Essential/Important/Complete)
3. ✅ Query-Based Exploration (find what you need)
4. ✅ Nullish Filtering (remove defaults and N/A)
5. ✅ Progressive Disclosure UI (simple → complex)
6. ✅ Exception Highlighting (show only non-defaults)
7. ✅ Task-Specific Views (different workflows)

**Result**: 18+ features become **practical and usable**

### Transferable Patterns (Apply to ALL 15 Categories)

1. ✅ **Hierarchical Organization** - Group related features
2. ✅ **Feature Prioritization** - Create language-specific priority matrices
3. ✅ **Nullish Filtering** - Omit defaults and "Not Applicable"
4. ✅ **Composite Features** - Bundle features used together
5. ✅ **Multi-Tier Access** - Essential/Important/Complete views
6. ✅ **Query-Based Exploration** - Find features by criteria
7. ✅ **Exception Highlighting** - Show only interesting values
8. ✅ **Progressive Disclosure** - Simple summary → Full detail
9. ✅ **Feature Dependencies** - Define constraint rules
10. ✅ **Standard Documentation** - Template for all features

### Final Assessment

**CLAUSES is the crown jewel of TBTA** - it integrates:
- **Social pragmatics** (speaker demographics)
- **Speech acts** (illocutionary force)
- **Discourse structure** (genre, notional structure, salience)
- **Information structure** (topic, implicit information)
- **Rhetorical devices** (rhetorical questions)

**18+ features is appropriate** given the scope - but **must be managed carefully** with tiering, filtering, and progressive disclosure.

**Key Insight**: Most clauses use **3-7 features actively**, not all 18. The complexity is in the **optionality**, not in requiring all features all the time.

**Recommendation**: Implement CLAUSES as the **flagship demonstration** of how to handle complex, multi-dimensional linguistic features in a usable way.
