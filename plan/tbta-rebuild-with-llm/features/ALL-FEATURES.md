# TBTA Features: Comprehensive Documentation

## Overview

This document comprehensively catalogs ALL features found in The Bible Translator's Assistant (TBTA) database exports. TBTA is a rules-based system that encodes semantic and syntactic information critical for accurate Bible translation, especially for languages with grammatical categories that don't align with English, Greek, or Hebrew.

## Table of Contents

1. [Noun Features](#noun-features)
2. [Verb Features](#verb-features)
3. [Clause-Level Features](#clause-level-features)
4. [Adjective Features](#adjective-features)
5. [Adposition Features](#adposition-features)
6. [Particle Features](#particle-features)
7. [Conjunction Features](#conjunction-features)
8. [Phrase Features](#phrase-features)
9. [Discourse Features](#discourse-features)

---

## Noun Features

### NounListIndex

**Description**: Tracks which nouns refer to the same entity within a verse or discourse unit.

**Possible Values**:
- `1-9`: First 9 unique entities
- `A-Z`: Next 26 entities (uppercase)
- `a-z`: Next 26 entities (lowercase)
- Total: 61 possible unique entity references per verse

**Position**: Separate field in noun encoding

**Examples from Data**:
```yaml
- Constituent: Jesus
  NounListIndex: '1'
- Constituent: disciple
  NounListIndex: '8'
- Constituent: God
  NounListIndex: A
```

**Why This Matters**:
- Languages with switch-reference systems need to track when the subject changes
- Prevents ambiguity in pronoun resolution
- Critical for languages that mark same/different subject explicitly

**Language Types That Need This**:
- Switch-reference languages (many Native American, Papua New Guinea)
- Languages with elaborate pronoun systems
- Languages requiring explicit subject tracking

### Number

**Description**: Grammatical number beyond simple singular/plural distinctions.

**Possible Values**:
- `Singular`: Exactly one
- `Dual`: Exactly two
- `Trial`: Exactly three
- `Quadrial`: Exactly four
- `Paucal`: A few (small indefinite number)
- `Plural`: Multiple (general plural)

**Position**: Field in noun properties

**Examples from Data**:
```yaml
# From GEN 19:31 - daughters speaking as dual
- Constituent: daughter
  Number: Dual
  Person: First Inclusive

# From MAT 24:1
- Constituent: disciple
  Number: Plural
```

**Why This Matters**:
- Many Austronesian & Polynesian languages have dual/trial/paucal distinctions
- Theological precision (e.g., Trinity as trial number in Genesis 1:26)
- Must choose correct form or sounds ungrammatical to native speakers

**Language Types That Need This**:
- Polynesian languages (Hawaiian, Samoan, Maori)
- Many Austronesian languages
- Some Slavic languages (have dual)
- Various Papua New Guinea languages

### Person

**Description**: Grammatical person with inclusive/exclusive distinctions and special forms.

**Possible Values**:
- `First`: First person (I/we)
- `Second`: Second person (you)
- `Third`: Third person (he/she/it/they)
- `First Inclusive`: We including you (speaker + listener)
- `First Exclusive`: We excluding you (speaker + others, not listener)
- `First as Third`: First person referenced as third
- `Second as Third`: Second person referenced as third
- `First Inclusive as Third`: First inclusive referenced as third
- `First Exclusive as Third`: First exclusive referenced as third

**Position**: Field in noun properties

**Examples from Data**:
```yaml
# From GEN 19:31
- Constituent: daughter
  Person: First Inclusive  # "we" including sister

# From MAT 24:1
- Constituent: Jesus
  Person: Third
```

**Why This Matters**:
- Critical for languages distinguishing inclusive/exclusive "we"
- Prevents theological misinterpretation
- Essential for accurate discourse representation

**Language Types That Need This**:
- Malay/Indonesian (kami vs kita)
- Tagalog/Filipino (tayo vs kami)
- Fijian and other Pacific languages
- Many Native American languages
- Vietnamese (various "we" forms)
- Quechua languages

### Participant Tracking

**Description**: How entities are introduced and tracked through discourse.

**Possible Values**:
- `First Mention`: New entity introduced
- `Routine`: Established participant continuing
- `Integration`: Being integrated into narrative
- `Exiting`: Leaving the narrative
- `Restaging`: Reintroduced after absence
- `Offstage`: Not currently present but referenced
- `Generic`: Generic/non-specific reference
- `Interrogative`: In question context
- `Frame Inferable`: Can be inferred from context

**Position**: Field in noun properties

**Examples from Data**:
```yaml
# From MAT 24:2
- Constituent: stone
  Participant Tracking: First Mention

# From MAT 24:1
- Constituent: Jesus
  Participant Tracking: Routine

# From GEN 19:31
- Constituent: father
  Participant Tracking: Frame Inferable
```

**Why This Matters**:
- Languages with different markers for new vs known information
- Helps determine article usage
- Critical for topic/focus marking
- Prevents confusion about entity identity

**Language Types That Need This**:
- Japanese (wa/ga distinction)
- Korean (topic/subject markers)
- Languages with obviative/proximate distinctions
- Languages with definiteness marking
- Bantu languages (noun class agreement)

### Proximity

**Description**: Demonstrative/deictic distinctions for spatial, temporal, and discourse distance.

**Possible Values**:
- `Near Speaker and Listener`: Close to both
- `Near Speaker`: Close to speaker only
- `Near Listener`: Close to listener only
- `Remote within Sight`: Visible but distant
- `Remote out of Sight`: Not visible
- `Temporally Near`: Recent in time
- `Temporally Remote`: Distant in time
- `Contextually Near`: Recently mentioned
- `Contextually Near with Focus`: Recently mentioned with emphasis

**Position**: Field in noun properties

**Examples from Data**:
```yaml
# From MAT 24:2
- Constituent: disciple
  Proximity: Contextually Near

- Constituent: thing
  Proximity: Contextually Near with Focus

- Constituent: temple
  Proximity: Contextually Near with Focus
```

**Why This Matters**:
- English has 2-way (this/that), many languages have 3+ way systems
- Critical for accurate demonstrative translation
- Affects discourse coherence

**Language Types That Need This**:
- Japanese (kore/sore/are - 3-way)
- Korean (3-way system)
- Spanish (este/ese/aquel - 3-way)
- Some Native American languages (5+ distinctions)
- Tagalog (multiple proximity levels)

### Polarity

**Description**: Whether the noun's existence/presence is affirmed or negated.

**Possible Values**:
- `Affirmative`: Normal positive assertion
- `Negative`: Negated existence/presence

**Position**: Field in noun properties

**Examples from Data**:
```yaml
# From GEN 19:31
- Constituent: man
  Number: Plural
  Polarity: Negative  # "no men"
```

**Why This Matters**:
- Some languages have special forms for negated nouns
- Affects quantifier selection
- Important for existential statements

**Language Types That Need This**:
- Turkish (negative existential)
- Finnish (partitive case with negation)
- Russian (genitive with negation)

### Surface Realization

**Description**: How the noun actually appears in the surface structure.

**Possible Values**:
- `Noun`: Realized as full noun
- `Pronoun`: Realized as pronoun
- `Zero`: Dropped/null (pro-drop)
- `Clitic`: Realized as clitic

**Position**: Field in noun properties

**Examples from Data**:
```yaml
- Constituent: Jesus
  Surface Realization: Noun
```

**Why This Matters**:
- Pro-drop languages need to know when to drop pronouns
- Clitic placement rules
- Pronoun vs full noun choice

**Language Types That Need This**:
- Spanish, Italian (pro-drop)
- Japanese, Korean (extensive pro-drop)
- Slavic languages (clitics)

---

## Verb Features

### Time

**Description**: Fine-grained temporal distinctions for when events occur.

**Possible Values**:
- **Immediate**:
  - `Immediate Past`: Just happened
  - `Immediate Future`: About to happen
- **Today**:
  - `Earlier Today`: Earlier same day
  - `Later Today`: Later same day
  - `Present`: Now
- **Near Past**:
  - `Yesterday`: One day ago
  - `2 Days Ago` through `6 Days Ago`: Specific days
  - `A Week Ago`: Seven days past
  - `A Month Ago`: One month past
  - `A Year Ago`: One year past
- **Near Future**:
  - `Tomorrow`: One day ahead
  - `2 Days from Now` through `6 Days from Now`
  - `A Week from Now`
  - `A Month from Now`
  - `A Year from Now`
- **Remote**:
  - `Historic Past`: Long ago
  - `Remote Past`: Distant past
  - `Remote Future`: Distant future
  - `Eternity Past`: Before time
  - `Eternity Future`: After time
- **Special**:
  - `Discourse`: Narrative/timeless present

**Position**: Field in verb properties

**Examples from Data**:
```yaml
# From MAT 24:1
- Constituent: destroy
  Time: Immediate Future

- Constituent: leave
  Time: Discourse

- Constituent: look
  Time: Later Today
```

**Why This Matters**:
- Some languages require specific temporal markers
- Affects verb form selection
- Critical for narrative coherence

**Language Types That Need This**:
- Tagalog (different past forms by recency)
- Yagua (5 past tenses by time distance)
- Kiksht (multiple degrees of past)
- ChiBemba (degrees of past/future)

### Aspect

**Description**: How the action unfolds over time.

**Possible Values**:
- `Unmarked`: No specific aspect
- `Perfective`: Completed action viewed as whole
- `Imperfective`: Ongoing/habitual action
- `Progressive`: Currently in progress
- `Iterative`: Repeated action
- `Habitual`: Regular occurrence
- `Inceptive`: Beginning of action
- `Cessative`: End of action
- `Completive`: Fully completed

**Position**: Field in verb properties

**Examples from Data**:
```yaml
# From MAT 24:2
- Constituent: tell
  Aspect: Imperfective

- Constituent: destroy
  Aspect: Unmarked
```

**Why This Matters**:
- Slavic languages have obligatory aspect
- Affects translation of Greek aspects
- Critical for accurate action representation

**Language Types That Need This**:
- All Slavic languages (aspect pairs)
- Mandarin (aspect markers)
- Arabic (complex aspect system)
- Many African languages

### Mood

**Description**: Speaker's attitude toward the action.

**Possible Values**:
- `Indicative`: Statement of fact
- `Imperative`: Command
- `Subjunctive`: Hypothetical/wished
- `Optative`: Wish/desire
- `'should' Obligation`: Deontic necessity
- `'must' Obligation`: Strong necessity
- `Potential`: Possibility
- `Conditional`: If-then
- `Interrogative`: Question

**Position**: Field in verb properties

**Examples from Data**:
```yaml
# From MAT 24:1
- Constituent: look
  Mood: 'should' Obligation

- Constituent: worship
  Mood: Indicative
```

**Why This Matters**:
- Many languages have rich mood systems
- Affects politeness and force
- Critical for accurate command/wish representation

**Language Types That Need This**:
- Turkish (evidential moods)
- Japanese (multiple politeness moods)
- Greek (preserving subjunctive/optative)

### LexicalSense

**Description**: Specific sense of polysemous verbs.

**Possible Values**:
- Letter codes `A` through `Z` representing different senses
- Each verb can have multiple senses distinguished by context

**Position**: Field in verb properties

**Examples from Data**:
```yaml
- Constituent: say
  LexicalSense: A

- Constituent: be
  LexicalSense: F  # existential "be"

- Constituent: ask
  LexicalSense: E  # specific type of asking
```

**Why This Matters**:
- Disambiguates polysemous verbs
- Helps select correct target language verb
- Critical for accurate meaning transfer

**Language Types That Need This**:
- All languages (polysemy is universal)
- Especially important for basic verbs like "be", "have", "do"

---

## Clause-Level Features

### Illocutionary Force

**Description**: The speech act type of the clause.

**Possible Values**:
- `Declarative`: Statement
- `Interrogative`: Question
- `Yes-No Interrogative`: Polar question
- `Wh-Interrogative`: Content question
- `Imperative`: Command
- `Hortative`: Exhortation ("let us...")
- `Exclamative`: Exclamation

**Position**: Clause-level property

**Examples from Data**:
```yaml
Part: Clause
Illocutionary Force: Declarative

Part: Clause
Illocutionary Force: Yes-No Interrogative

Part: Clause
Illocutionary Force: Imperative
```

**Why This Matters**:
- Determines sentence-final particles in many languages
- Affects word order
- Critical for pragmatic accuracy

**Language Types That Need This**:
- Japanese (sentence-final particles)
- Chinese (question particles)
- Korean (speech level endings)

### Speaker Demographics

**Description**: Information about the speaker in quoted speech.

**Possible Values**:
- **Speaker**: Man, Woman, Boy, Girl, Deity, Angel, Demon
- **Listener**: Man, Woman, Boy, Girl, Group, Deity
- **Speaker's Age**: Child, Adolescent, Young Adult (18-24), Middle Aged, Old
- **Speaker-Listener Age**:
  - Essentially the Same Age
  - Older Speaking to Younger
  - Younger Speaking to Older
  - Adult to Child
- **Speaker's Attitude**: Neutral, Respectful, Familiar, Hostile, Formal

**Position**: Clause-level properties (for quoted speech)

**Examples from Data**:
```yaml
# From GEN 19:31
Speaker: Woman
Listener: Woman
Speaker`s Age: Young Adult (18-24)
Speaker-Listener Age: Essentially the Same Age
Speaker`s Attitude: Familiar
```

**Why This Matters**:
- Languages with honorific systems need this
- Determines register and politeness level
- Critical for appropriate social marking

**Language Types That Need This**:
- Japanese (keigo honorific system)
- Korean (speech levels)
- Javanese (3-5 politeness levels)
- Thai (royal vocabulary)
- European languages (T-V distinction)

### Discourse Genre

**Description**: The type of discourse or text.

**Possible Values**:
- `Climactic Narrative Story`: Main narrative
- `Background Narrative`: Supporting narrative
- `Procedural`: Instructions/how-to
- `Expository`: Teaching/explanation
- `Poetic`: Poetry/songs
- `Hortatory`: Exhortation/sermon
- `Prophetic`: Prophecy
- `Legal`: Laws/regulations
- `Epistolary`: Letter format

**Position**: Clause-level property

**Examples from Data**:
```yaml
Discourse Genre: Climactic Narrative Story
```

**Why This Matters**:
- Different genres require different registers
- Affects tense/aspect choices
- Determines discourse markers

**Language Types That Need This**:
- Languages with genre-specific particles
- Languages with narrative vs non-narrative tenses

### Topic NP

**Description**: Which noun phrase is the topic of the clause.

**Possible Values**:
- `Most Agent-like`: Subject/agent is topic
- `Most Patient-like`: Object/patient is topic
- `Destination`: Goal/recipient is topic
- `State`: Stative argument is topic

**Position**: Clause-level property

**Examples from Data**:
```yaml
Topic NP: Most Agent-like
Topic NP: Most Patient-like
```

**Why This Matters**:
- Topic-prominent languages need explicit marking
- Affects word order
- Critical for information structure

**Language Types That Need This**:
- Japanese (wa topic marker)
- Korean (neun/eun topic marker)
- Chinese (topic-comment structure)
- Tagalog (ang marking)

### Salience Band

**Description**: Foreground vs background information.

**Possible Values**:
- `Foregrounded Actions`: Main storyline
- `Backgrounded Actions`: Supporting events
- `Setting`: Scene-setting information
- `Evaluation`: Commentary/evaluation
- `Collateral`: Parenthetical information

**Position**: Clause-level property

**Examples from Data**:
```yaml
Salience Band: Backgrounded Actions
```

**Why This Matters**:
- Affects verb form choice
- Determines discourse markers
- Critical for narrative flow

**Language Types That Need This**:
- Languages with foreground/background verb forms
- Bantu languages (narrative tenses)

### Rhetorical Question

**Description**: Questions that aren't seeking information.

**Possible Values**:
- `Yes-No Question Expects 'Yes'`: Rhetorical expecting agreement
- `Yes-No Question Expects 'No'`: Rhetorical expecting disagreement
- `Equivalent Statement`: Question functioning as statement
- `Challenge`: Question as challenge

**Position**: Clause-level property

**Examples from Data**:
```yaml
Rhetorical Question: Yes-No Question Expects 'Yes'
Rhetorical Question: Equivalent Statement
```

**Why This Matters**:
- Some languages mark rhetorical questions differently
- Affects particle choice
- Important for pragmatic accuracy

**Language Types That Need This**:
- Languages with rhetorical question particles
- Languages requiring explicit markers

### Implicit Information

**Description**: Information that can be inferred but isn't explicitly stated.

**Possible Values**:
- `Implicit Situational Information`: Context provides info
- `Implicit Cultural Information`: Culture provides info
- `Optional Agent of Passive`: Agent can be inferred
- `No`: Nothing implicit

**Position**: Clause-level or phrase-level property

**Examples from Data**:
```yaml
Implicit Information: Implicit Situational Information
Implicit: Optional Agent of Passive
```

**Why This Matters**:
- Languages differ in what must be explicit
- Prevents over-translation or under-translation
- Critical for natural-sounding translation

**Language Types That Need This**:
- High-context cultures (East Asian)
- Languages with obligatory participants

### Type (Clause Type)

**Description**: Syntactic type of the clause.

**Possible Values**:
- `Independent`: Main clause
- `Dependent`: Subordinate clause
- `Restrictive Thing Modifier (Relative Clause)`: Restrictive relative
- `Non-restrictive Thing Modifier`: Non-restrictive relative
- `Event Modifier (Adverbial Clause)`: Adverbial subordinate
- `Patient (Object Complement)`: Complement clause
- `Attributive Patient (Adjectival Object Complement)`: Adjectival complement

**Position**: Clause-level property

**Examples from Data**:
```yaml
Type: Independent
Type: Restrictive Thing Modifier (Relative Clause)
Type: Event Modifier (Adverbial Clause)
Type: Patient (Object Complement)
```

**Why This Matters**:
- Languages have different subordination strategies
- Affects conjunction choice
- Critical for syntactic accuracy

**Language Types That Need This**:
- Languages with different relative clause strategies
- Languages with clause chaining
- Switch-reference languages

### Sequence

**Description**: Whether the clause is part of a sequence.

**Possible Values**:
- `Not in a Sequence`: Stand-alone
- `First in Sequence`: Sequence initial
- `Middle of Sequence`: Sequence medial
- `Last in Sequence`: Sequence final

**Position**: Clause-level property

**Examples from Data**:
```yaml
Sequence: Not in a Sequence
```

**Why This Matters**:
- Languages with clause chaining need this
- Affects conjunction selection
- Important for narrative flow

**Language Types That Need This**:
- Papua New Guinea languages (clause chaining)
- Some Native American languages

### Location

**Description**: Special discourse locations.

**Possible Values**:
- `Discourse Title`: Title/heading
- `Discourse Opening`: Introduction
- `Discourse Closing`: Conclusion
- `Episode Boundary`: Between episodes
- `Peak`: Climactic moment

**Position**: Clause-level property

**Examples from Data**:
```yaml
Location: Discourse Title
```

**Why This Matters**:
- Special markers for discourse boundaries
- Affects formatting and style
- Critical for discourse structure

**Language Types That Need This**:
- Languages with discourse particles
- Languages with special peak markers

---

## Adjective Features

### Degree

**Description**: Degree of comparison for adjectives.

**Possible Values**:
- `No Degree`: Basic form
- `Comparative`: More than
- `Superlative`: Most
- `Excessive`: Too much
- `Intensive`: Very/extremely

**Position**: Field in adjective properties

**Examples from Data**:
```yaml
# From GEN 19:31
- Constituent: old
  Degree: Comparative  # "older"

- Constituent: beautiful
  Degree: No Degree
```

**Why This Matters**:
- Languages differ in how they mark comparison
- Some languages lack morphological comparison
- Important for accurate degree representation

**Language Types That Need This**:
- Languages using particles for comparison
- Languages with complex degree systems

### Usage

**Description**: Syntactic position of the adjective.

**Possible Values**:
- `Attributive`: Modifying a noun directly
- `Predicative`: In predicate position
- `Substantive`: Used as a noun

**Position**: Field in adjective phrase properties

**Examples from Data**:
```yaml
Part: AdjP
Usage: Attributive

Part: AdjP
Usage: Predicative
```

**Why This Matters**:
- Some languages have different adjective forms by position
- Affects agreement patterns
- Critical for syntactic accuracy

**Language Types That Need This**:
- German (different endings)
- Russian (short vs long forms)
- Japanese (different forms)

---

## Adposition Features

### LexicalSense

**Description**: Specific sense of polysemous prepositions.

**Possible Values**: Letter codes A-Z for different senses

**Examples from Data**:
```yaml
- Constituent: in
  LexicalSense: A  # physical location

- Constituent: at
  LexicalSense: C  # temporal

- Constituent: -Generic Genitive
  LexicalSense: A  # possession
```

**Why This Matters**:
- Prepositions are highly polysemous
- Critical for selecting correct target preposition
- Affects case selection in case-marking languages

**Language Types That Need This**:
- All languages (preposition systems vary greatly)
- Case-marking languages

### Special Adpositions

**Description**: Semantic role markers not corresponding to lexical prepositions.

**Possible Values**:
- `-Generic Genitive`: Possessive relationship
- `-Kinship`: Family relationship
- `-Subgroup`: Part of whole
- `-Begin Scene`: Discourse boundary marker

**Examples from Data**:
```yaml
- Constituent: -Generic Genitive
  Part: Adposition

- Constituent: -Kinship
  Part: Adposition

- Constituent: -Subgroup
  Part: Adposition
```

**Why This Matters**:
- Languages mark these relationships differently
- Some use case, others use prepositions
- Critical for accurate relationship marking

**Language Types That Need This**:
- Languages with alienable/inalienable possession
- Languages with special kinship marking

---

## Particle Features

### Type

**Description**: Type of particle.

**Possible Values**:
- `-QuoteBegin`: Start of quotation
- `-QuoteEnd`: End of quotation
- `-Focus`: Focus particle
- `-Topic`: Topic particle
- `-Emphasis`: Emphasis particle
- `-Negation`: Negative particle

**Examples from Data**:
```yaml
- Constituent: -QuoteBegin
  Part: Particle

- Constituent: -QuoteEnd
  Part: Particle
```

**Why This Matters**:
- Languages vary in quotation marking
- Some use particles instead of punctuation
- Critical for discourse marking

**Language Types That Need This**:
- Japanese (quotative particle と)
- Languages without quotation marks
- Languages with reportative evidentials

---

## Conjunction Features

### LexicalSense

**Description**: Specific sense of the conjunction.

**Possible Values**: Letter codes A-Z

**Examples from Data**:
```yaml
- Constituent: and
  LexicalSense: A

- Constituent: therefore
  LexicalSense: A
```

### Implicit

**Description**: Whether the conjunction can be left implicit.

**Possible Values**:
- `Yes`: Can be omitted
- `No`: Must be explicit

**Examples from Data**:
```yaml
- Constituent: and
  Implicit: 'No'
```

**Why This Matters**:
- Languages differ in conjunction requirements
- Affects naturalness
- Important for discourse flow

**Language Types That Need This**:
- Languages with zero-conjunction
- Languages requiring explicit conjunctions

---

## Phrase Features

### Semantic Role

**Description**: The semantic/thematic role of the phrase.

**Possible Values**:
- `Most Agent-like`: Proto-agent (doer)
- `Most Patient-like`: Proto-patient (undergoer)
- `Destination`: Goal/recipient
- `Source`: Origin
- `State`: Stative role
- `Instrument`: Tool/means
- `Beneficiary`: For whom
- `Location`: Where
- `Time`: When
- `Manner`: How
- `Purpose`: Why

**Position**: NP (Noun Phrase) level property

**Examples from Data**:
```yaml
Semantic Role: Most Agent-like
Semantic Role: Most Patient-like
Semantic Role: Destination
Semantic Role: State
```

**Why This Matters**:
- Languages mark semantic roles differently
- Affects case assignment
- Critical for argument structure

**Language Types That Need This**:
- Ergative-absolutive languages
- Languages with semantic case
- Philippine-type languages

### Relativized

**Description**: Whether the phrase is relativized.

**Possible Values**:
- `Yes`: Is relativized
- `No`: Not relativized

**Examples from Data**:
```yaml
Relativized: 'No'
```

**Why This Matters**:
- Languages have different relativization strategies
- Affects pronoun retention
- Important for relative clause formation

**Language Types That Need This**:
- Languages with resumptive pronouns
- Languages with relative particles

### Part (Phrase Type)

**Description**: Type of phrase.

**Possible Values**:
- `NP`: Noun phrase
- `VP`: Verb phrase
- `AdjP`: Adjective phrase
- `AdvP`: Adverb phrase
- `PP`: Prepositional phrase
- `Clause`: Full clause

**Examples from Data**:
```yaml
Part: NP
Part: VP
Part: AdjP
Part: Clause
```

**Why This Matters**:
- Basic syntactic categorization
- Affects word order
- Critical for parsing

---

## Discourse Features

### SemanticComplexityLevel

**Description**: How semantically complex the constituent is.

**Possible Values**:
- `1`: Simple/basic
- `2`: Moderate complexity
- `3`: Complex
- `4`: Very complex

**Position**: Field in most constituents

**Examples from Data**:
```yaml
SemanticComplexityLevel: '1'
```

**Why This Matters**:
- May affect translation strategy
- Important for readability
- Helps identify difficult passages

**Language Types That Need This**:
- All languages (universal consideration)

---

## Summary of Critical Features for Translation

### Most Important for Cross-Linguistic Variation

1. **Person** (Inclusive/Exclusive) - Critical for ~40% of world's languages
2. **Number** (Dual/Trial/Paucal) - Critical for many Pacific/Australian languages
3. **Proximity** (3+ way demonstratives) - Critical for Asian/African languages
4. **Speaker Demographics** - Critical for languages with honorifics
5. **Participant Tracking** - Critical for switch-reference languages
6. **Time Granularity** - Critical for languages with temporal distance marking
7. **Semantic Role** - Critical for ergative and Philippine-type languages

### Features Preventing Common Translation Errors

1. **NounListIndex** - Prevents pronoun ambiguity
2. **Participant Tracking** - Prevents losing track of entities
3. **Implicit Information** - Prevents over/under-translation
4. **Rhetorical Question** - Prevents misunderstanding intent
5. **Illocutionary Force** - Ensures correct speech act

### Features for Specific Language Families

#### Austronesian/Pacific
- Number (dual/trial)
- Person (inclusive/exclusive)
- Focus/Topic marking

#### East Asian
- Proximity (3-way demonstratives)
- Speaker Demographics
- Topic marking
- Politeness levels

#### Native American
- Switch-reference
- Evidentiality
- Person (inclusive/exclusive)
- Proximity (4+ way)

#### African (Bantu)
- Noun class agreement
- Participant tracking
- Salience bands

#### Slavic
- Aspect (perfective/imperfective)
- Case-semantic role alignment
- Motion verbs

#### South Asian
- Honorifics
- Inclusive/exclusive
- Ergative alignment

---

## Usage Notes

1. **Not all features appear in every verse** - TBTA only encodes what's relevant
2. **Features can combine** - E.g., dual + first inclusive = "we two including you"
3. **Context determines selection** - The same English may require different features based on context
4. **Target language determines needs** - Translator should focus on features their language requires

## Integration with Other Systems

TBTA features complement other linguistic annotations:
- **Macula**: Provides Greek/Hebrew morphology
- **Strong's**: Provides lexical connections
- **TBTA**: Provides cross-linguistic pragmatic features

Together, these provide comprehensive guidance for accurate Bible translation across all human languages.