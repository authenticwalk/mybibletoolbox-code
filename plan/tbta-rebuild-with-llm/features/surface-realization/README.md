# Surface Realization in Bible Translation Languages

## Executive Summary

Surface Realization describes how noun phrases appear in actual discourse - whether they manifest as full nouns, pronouns, null/dropped arguments (pro-drop), or clitics. This feature is critical for languages with null subject parameters, pro-drop constraints, and pronoun deletion rules. Understanding surface realization patterns is essential for accurate, natural-sounding translations across diverse linguistic systems.

The TBTA Surface Realization feature tracks four distinct realization types:
1. **Noun**: Full lexical noun appears
2. **Pronoun**: Pronoun appears (explicit reference)
3. **Zero**: Dropped/null (no surface form, but understood contextually)
4. **Clitic**: Reduced form attached to another word

## What is Surface Realization?

Surface Realization refers to the phonologically realized form of a noun phrase in a sentence. The same semantic entity can appear in different ways depending on context, discourse, and language-specific rules.

### Example: English vs Spanish

**English (Non-pro-drop):**
```
Speaker: "John arrived at the market."
Response: "He bought fruits there."  ← Must use pronoun "he"
         NOT "Bought fruits there."   ← Ungrammatical without subject
```

**Spanish (Pro-drop):**
```
Hablante: "Juan llegó al mercado."
Response: "Compró frutas allí."      ← Pronoun can be dropped
         "Él compró frutas allí."    ← Or explicitly stated
```

The semantic meaning is identical, but Spanish allows zero realization while English requires overt pronouns for most persons/numbers.

### Key Linguistic Concepts

#### 1. Pro-Drop (Pronoun Drop)
The ability to omit pronouns when their referent is recoverable from context. Languages vary in:
- **Which persons**: Spanish drops all persons; Japanese drops all; English drops none
- **Which numbers**: Some languages only drop singular
- **Which clause types**: Some only in main clauses, others in all clause types
- **Which tenses/moods**: Some restrict to certain forms

#### 2. Null Subject Parameter
A syntactic property where languages may have empty (non-phonological) subjects in finite clauses. This requires:
- Rich agreement morphology on the verb
- Discourse-based resolution mechanisms
- Syntactic null categories (empty pronouns)

#### 3. Topic Drop / Zero Anaphora
Dropping of arguments that are:
- Discourse topics
- Recently mentioned
- Contextually obvious
- Semantically recoverable from the clause

Examples across languages:
- **Japanese**: Extensive argument drop for all semantic roles
- **Korean**: Similar to Japanese
- **Mandarin**: Drop of all arguments under appropriate conditions
- **Spanish/Italian**: Drop of subjects; optional drop of objects with clitics

#### 4. Clitic Pronouns
Reduced pronouns that must attach to a host (usually the verb):
- **Spanish**: lo/la/le/les (object clitics)
- **French**: me/te/se/nous/vous/les
- **Romance**: General pattern
- **Slavic**: Limited clitic systems
- **Balkan**: Extensive clitic doubling

## Surface Realization Types in TBTA

### Type 1: Noun
Full lexical noun phrase appears in surface position.

**Examples:**
```yaml
- Constituent: Jesus
  Surface Realization: Noun
  Example: "Jesus went to the temple"

- Constituent: disciple
  Surface Realization: Noun
  Example: "The disciples followed him"
```

**Languages that prefer this:**
- Non-pro-drop languages (English, German, Dutch)
- When introducing new referents (first mention)
- In formal or emphatic contexts
- Languages without rich morphology to recover arguments

**When to use:**
- First introduction of character/entity
- Emphasis or contrast
- Formal register
- When disambiguation is needed

### Type 2: Pronoun
Explicit pronoun (standalone or clitic-like) appears.

**Examples:**
```yaml
- Constituent: Jesus
  Surface Realization: Pronoun
  Example: "He went to the temple" (English)
           "Él fue al templo" (Spanish)

- Constituent: disciples
  Surface Realization: Pronoun
  Example: "They followed him"
```

**Languages that commonly use pronouns:**
- Non-pro-drop languages (required for grammaticality)
- East Asian languages when not dropping
- Instances where zero is not acceptable
- Formal contexts in some pro-drop languages

**When to use:**
- Established referent, no emphasis
- When zero would be ungrammatical
- Clarification contexts
- Certain syntactic positions (fronted objects, non-adjacent antecedents)

### Type 3: Zero (Pro-drop)
The argument is not realized phonologically but is understood from context.

**Examples:**
```yaml
- Constituent: Jesus
  Surface Realization: Zero
  Example: "∅ went to the temple" (recoverable from previous context)
           "John arrived. ∅ bought fruits." (Spanish: Juan llegó. ∅ Compró frutas.)

- Constituent: disciple
  Surface Realization: Zero
  Example: "The disciples followed. ∅ Listened carefully." (in pro-drop language)
```

**Conditions for zero realization:**
1. **Recoverability**: Antecedent must be clear from discourse
2. **Agreement morphology**: Verb must have rich enough agreement
3. **Language-specific rules**: Some languages restrict zero to certain persons
4. **Syntactic position**: Main clause subjects are most common
5. **Discourse status**: Established, salient, or generic referents

**When NOT to use zero:**
- First introduction of character
- Ambiguous antecedents
- Subject changes in non-switch-reference languages
- In non-pro-drop languages

### Type 4: Clitic
Reduced pronoun form attached to a host word (usually verb).

**Examples:**
```yaml
- Constituent: object
  Surface Realization: Clitic
  Example: "Lo vi" (Spanish: "I saw-it" = "I saw him/it")
           "Te lo dije" (Spanish: "I told-you-it")

- Constituent: indirect object
  Surface Realization: Clitic
  Example: "Le doy el libro" (Spanish: "(To-him) I-give the book")
```

**Languages with systematic clitics:**
- Romance languages (Spanish, French, Italian, Portuguese, Romanian)
- Slavic languages (some)
- Greek (Modern)
- Balkan languages (extensive system)
- Some Austronesian languages

**Properties of clitics:**
- Phonologically dependent on host
- Typically follow special ordering rules
- May have limited case/number distinctions
- Can stack/double (multiple clitics per verb)
- Often have special positioning relative to verbs (proclisis/enclisis)

## Languages from Our TSV with Pro-Drop Characteristics

### High Pro-Drop Propensity (Extensive null subject systems)

#### East Asian Languages
- **Mandarin Chinese** (zho): Extensive pro-drop for all arguments
- **Cantonese** (yue): Extensive pro-drop
- **Japanese** (jpn): All arguments can drop; heavily pro-drop
- **Korean** (kor): Extensive pro-drop; topic-oriented
- **Vietnamese** (vie): Drop subject and object pronouns
- **Thai** (tha): Subject drop
- **Lao** (lao): Subject drop
- **Burmese** (mya): Subject drop

#### Romance Languages (Moderate to High)
- **Spanish** (spa): Drop subjects freely
- **Italian** (ita): Drop subjects freely
- **Portuguese** (por): Drop subjects; languages vary
- **Romanian** (ron): Drop subjects (archaic/dialectal)
- **Catalan** (cat): Drop subjects
- **Galician** (glg): Drop subjects
- **French** (fra): Limited drop (mainly in informal)
- **Occitan** (oci): Drop subjects

#### Slavic Languages (Limited drop, some clitics)
- **Russian** (rus): Drop subjects in 3rd person, infinitives
- **Bulgarian** (bul): Clitic pronouns (obligatory in many contexts)
- **Serbian** (srp): Some subject drop
- **Polish** (pol): Some subject drop in infinitives
- **Czech** (ces): Limited drop

#### Austronesian Languages (Variable)
- **Indonesian** (ind): Some subject drop in connected discourse
- **Malay** (zlm): Some subject drop
- **Tagalog** (tgl): Varies; focus system interacts
- **Javanese** (jav): Subject drop
- **Cebuano** (ceb): Varies
- **Ilocano** (ilo): Variable
- **Pampangan** (pam): Variable

#### Quechuan Languages
- **Quechua** languages (que, quy, etc.): Drop subjects with person/number agreement

#### Other Families
- **Greek** (Modern, ell): Subject drop; clitic objects
- **Hebrew** (Modern, heb): Limited drop
- **Arabic** (arb, ara, acm, etc.): Drop subjects with agreement
- **Persian** (pes): Subject drop
- **Turkish** (tur): Subject drop
- **Hungarian** (hun): Limited drop
- **Finnish** (fin): Limited drop
- **Estonian** (est): Limited drop
- **Basque** (eus): Limited drop

### Moderate Pro-Drop (Some contexts)

#### Trans-New Guinea Languages
Many TNGLanguages show:
- Subject drop in chain clauses
- Object drop with agreement marking
- Topic drop
- Discourse context-dependent patterns

Examples: Agarabi (agd), Amele (aey), etc.

#### Mayan Languages
- Context-dependent subject drop
- Complex verbal agreement systems

#### Cariban Languages
- Subject drop in certain contexts

### Non-Pro-Drop or Minimal Pro-Drop

#### Germanic Languages
- **English** (eng): No subject drop (highly non-pro-drop)
- **German** (deu): Very limited; mostly in infinitives
- **Dutch** (nld): Very limited
- **Afrikaans** (afr): Very limited
- **Swedish** (swe): Very limited

#### Others
- **Finnish** (fin): Limited
- **Hungarian** (hun): Limited
- **Basque** (eus): Limited

## Clitic Placement Rules

### Enclisis (Clitics follow the verb)
Common in:
- Spanish: habla-me (speak to-me) → but "me habla" in present tense
- Portuguese: fala-me
- Romance languages (especially imperative/infinitive forms)
- Many Balkan languages

### Proclisis (Clitics precede the verb)
Common in:
- French: me parle (me speaks)
- Spanish: la veo (her I-see)
- Many Balkan languages with obligatory proclisis
- Modern Greek

### Variable placement based on:
- Tense/mood/aspect
- Verb form (finite vs non-finite)
- Clause type (main vs subordinate)
- Negation
- Stress/pragmatics

## Cross-Linguistic Variation

### Person/Number Restrictions on Pro-Drop

| Language | 1sg | 2sg | 3sg | 1pl | 2pl | 3pl |
|----------|-----|-----|-----|-----|-----|-----|
| Spanish | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Portuguese | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Italian | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Japanese | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Russian | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ |
| English | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |

### Clause Type Restrictions

**Subjects allowed to drop in:**
1. **Main clauses**: Most pro-drop languages
2. **Subordinate clauses**: Some pro-drop languages
3. **Infinitives**: Many non-pro-drop languages allow (English: "I want [∅ to go]")
4. **Imperatives**: Often special rules
5. **Conditionals**: Often allowed

**Objects rarely drop except with:**
1. Clitic pronouns (Romance languages)
2. Highly salient topics (East Asian languages)
3. Generic/indefinite readings

## Discourse Factors Affecting Surface Realization

### 1. Givenness/Information Status
- **New/Unknown**: Strongly prefer noun → "A rabbi came to town"
- **Given/Known**: Prefer pronoun/zero → "He taught the people" or "∅ Taught the people"
- **Accessible/Inferrable**: More flexible

### 2. Discourse Topic
- Topic-prominent languages mark topics explicitly
- Zero realization most likely for current topics
- Switch to pronoun when topic shifts
- Use noun for new topic introduction

### 3. Distance from Antecedent
- **Adjacent**: Zero most common
- **Nearby (1-2 clauses)**: Pronoun common
- **Distant (3+ clauses)**: Noun preferred for clarity
- Language-specific: some (Japanese) allow zero even at distance; others (English) require noun

### 4. Semantic Role and Saliency
- **Agents**: Pro-drop more likely
- **Patients**: May require more explicit marking
- **Inanimate**: More likely to require explicit marking
- **Salient characters**: Pro-drop more likely even at distance

### 5. Register and Style
- **Formal written**: More nouns, more explicit
- **Informal spoken**: More pro-drop, more pronouns
- **Narrative**: Often high use of zero
- **Direct speech**: More pronouns for clarity

### 6. Negation
Some languages require or forbid pro-drop with negation
- Spanish: "No lo sé" (not it I-know) requires clitic, not null

## Bible Translation Implications

### Problem 1: The Holy Spirit Reference Problem

**Greek**: "To pneuma ho hagios" → Often understood with dropped pronouns

**English requirement**: "The Holy Spirit" (explicit noun)

**Spanish option**:
1. "El Espíritu Santo" (noun)
2. "Él" (pronoun, if recently mentioned)
3. "∅" (zero, if very clear from discourse)

**Japanese option**: Extensive zero use possible

### Problem 2: The Theological Ambiguity

Some passages use zero subjects in the source language, creating intentional theological ambiguity:

**Romans 10:9** (Greek has ambiguous subject):
- "If you believe that God raised [someone] from the dead..."
- Could be: God raised Jesus, OR God raised us, OR God raised the dead generally

Pro-drop languages may preserve this ambiguity; non-pro-drop languages must disambiguate.

### Problem 3: The Clitic Object Problem

**Spanish/Italian/Portuguese**: Objects often appear as clitics, changing word order

**Example**:
```
English: "He told them the story"
Spanish: "Les contó la historia" (to-them told the story)
         "Se la contó" (to-them it told) - with double clitics
```

Must choose whether to use:
- Full object NP: "a ellos"
- Clitic: "les"
- Zero: "∅" (only in certain contexts)

### Problem 4: Switching Between Realization Types

Bible discourse often switches between realization types:

```
New character: "A woman came to the well"      [Noun]
Continues: "She drank water"                  [Pronoun]
Later in story: "∅ Returned to her home"      [Zero - in pro-drop language]
Change of topic: "Jesus asked the woman..."   [Noun - reintroduction]
```

Translators must ensure consistency within each language's constraints.

## Detailed Analysis: Pro-Drop by Language Family

### Austronesian (176 languages in our TSV)
- **Patterns**: Variable; often focus-aligned rather than person-aligned
- **Subgroups with high pro-drop**: Indonesian, Malaysian, Tagalog languages
- **Special feature**: Focus system may determine realization (focus > topical > background)
- **Subgroups with moderate pro-drop**: Javanese, Central Philippine languages

### Trans-New Guinea (141 languages in our TSV)
- **Patterns**: Often clause-chaining languages with specific pro-drop rules
- **Features**: Subject drop in medial clauses (between-clause subjects)
- **Special feature**: Switch-reference systems may override general pro-drop
- **Note**: Highly diverse; individual language investigation needed

### Indo-European (135 languages in our TSV)
- **Slavic subgroup**: Limited subject drop (mainly 3rd person Russian); some clitic systems
- **Romance subgroup**: High pro-drop (Spanish, Portuguese, Italian, Romanian, Catalan)
- **Germanic subgroup**: Generally non-pro-drop (English, German, Dutch, Swedish)
- **Greek**: Subject drop allowed
- **Armenian**: Limited drop
- **Balkan languages**: Various cliticization patterns

### Niger-Congo (89 languages in our TSV)
- **Patterns**: Varies greatly by subgroup
- **Bantu**: Generally non-pro-drop; rich noun class systems provide discourse tracking
- **Kwa**: Variable
- **Other groups**: Individual investigation needed

### Sino-Tibetan (18 languages in our TSV)
- **Mandarin, Cantonese**: Extensive pro-drop
- **Other languages**: Vary

### Afro-Asiatic (25 languages in our TSV)
- **Semitic languages** (Hebrew, Arabic): Subject drop with rich agreement
- **Other languages**: Vary

## Prediction Guide for Translators

### When to Use Zero (Pro-drop):
1. ✓ Immediately after explicit mention of referent
2. ✓ Current discourse topic is clearly established
3. ✓ Language explicitly allows this person/number/clause-type combination
4. ✓ Reflexivity or saliency suggests zero is natural
5. ✓ Narrative/discourse context strongly supports recovery

### When to Use Pronoun:
1. ✓ Referent is not current discourse topic but still clear
2. ✓ Some distance from antecedent (language-specific threshold)
3. ✓ Need mild emphasis or contrast without full noun
4. ✓ Formal register preferences pronouns over zero
5. ✓ Negation requires pronoun/clitic (some languages)

### When to Use Noun:
1. ✓ First introduction of new entity
2. ✓ Extended absence from discourse and reintroduction
3. ✓ Emphasis or strong contrast
4. ✓ Disambiguation needed (ambiguous referent)
5. ✓ Formal written register (especially expository text)

### When to Use Clitic:
1. ✓ Language has obligatory clitic system (Romance, Greek, Balkan)
2. ✓ Object expression and clitic is standard for your language
3. ✓ Verb-doubling or clitic-doubling is required for clarity
4. ✓ Specific syntactic construction demands it
5. ✓ Register/style preference for clitic over other forms

## Empirical Findings on Bible Translation

### High Pro-Drop in Asian/Pacific Languages
Languages like Japanese, Korean, Mandarin, and many Austronesian languages use extensive pro-drop in Bible translations. This:
- Reads naturally to native speakers
- Requires good discourse tracking
- Preserves more source language ambiguity
- Demands careful antecedent clarity

### Romance Language Patterns
Spanish and Portuguese Bibles:
- Subject pronouns rarely appear when subject is clear
- Object pronouns appear as clitics
- Creates different word order from English source texts
- Requires careful handling of emphatic subjects

### Germanic Non-Pro-Drop Constraints
English, German, Dutch Bible translations:
- Must make explicit all subjects and objects
- Cannot preserve source language ambiguities
- Relies more on context and extra-textual knowledge
- May be more verbose than source

### TNGLanguage Complexity
- Often have switch-reference + pro-drop interactions
- Medial clauses (in clause chains) have special pro-drop rules
- Require sophisticated tracking of subject continuity/change
- Need language-specific guidance for each translation project

## Resources for Further Study

### Academic Sources (when available)
- Language-specific grammars
- Typological studies of pro-drop
- Discourse analysis of Bible translations
- Studies of clitic systems

### For This Project
- Individual language analysis documents
- Corpus analysis of existing translations
- Discourse tracking experiments
- Comparative studies of related languages

## Notes for Tool Development

1. **Pro-drop detection** should consider:
   - Language family and known features
   - Distance from previous mention
   - Discourse topic status
   - Register and text type
   - Specific syntactic constraints

2. **Validation should check**:
   - Consistency within verse
   - Consistency with language family patterns
   - Compatibility with switch-reference (if applicable)
   - Register appropriateness

3. **Training data** needed:
   - Native speaker judgments of naturalness
   - Corpus analysis of translations
   - Language-specific grammatical constraints
   - Discourse pattern analysis
