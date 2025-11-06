# TBTA Polarity Annotation System: Comprehensive Research

**Document Created**: 2025-11-05
**Research Focus**: Deep investigation into TBTA's polarity annotation values and cross-linguistic negation typology
**Purpose**: Understand how to reproduce TBTA's polarity decisions for 1009 languages across diverse families

---

## Table of Contents

1. [TBTA's Polarity Values](#tbtas-polarity-values)
2. [Cross-Linguistic Negation Typology](#cross-linguistic-negation-typology)
3. [Biblical Source Language Negation](#biblical-source-language-negation)
4. [Language Family Negation Patterns](#language-family-negation-patterns)
5. [Scope of Negation](#scope-of-negation)
6. [Emphatic Affirmation](#emphatic-affirmation)
7. [Methodology for Reproduction](#methodology-for-reproduction)
8. [Sources Consulted](#sources-consulted)

---

## TBTA's Polarity Values

### Identified Values

Based on examination of TBTA JSON export data from `https://github.com/AllTheWord/tbta_db_export`:

1. **Affirmative** - Marks positive polarity (non-negated elements)
2. **Negative** - Marks negative polarity (negated elements)

### Application Scope

The `Polarity` field appears on:

- **Nouns** (SyntacticCategory 1)
- **Verbs** (SyntacticCategory 2)

**Note**: TBTA documentation mentions "Affirmative (A) or Negative (N)" encoding for polarity in position 7 for nouns and position 8 for verbs in their semantic strings.

### Examples from TBTA Data

#### Genesis 1:1 (All Affirmative)
```json
{
  "Constituent": "God",
  "Part": "Noun",
  "Polarity": "Affirmative",
  // ... other fields
}

{
  "Constituent": "create",
  "Part": "Verb",
  "Polarity": "Affirmative",
  // ... other fields
}
```

All elements in this verse are marked "Affirmative" - no negation present.

#### Genesis 1:2 (Mixed: Negative + Affirmative)

**Clause 2 (Vocabulary Alternate): "earth have form"**
```json
{
  "Constituent": "have",
  "Part": "Verb",
  "Polarity": "Negative",  // ← NEGATED VERB
  // ...
}

{
  "Constituent": "form",
  "Part": "Noun",
  "Polarity": "Affirmative",  // Object noun remains affirmative
  // ...
}
```

**Clause 3 (Simple Alternate): "thing exist on earth"**
```json
{
  "Constituent": "thing",
  "Part": "Noun",
  "Polarity": "Negative",  // ← NEGATED NOUN (semantically: "nothing")
  // ...
}

{
  "Constituent": "exist",
  "Part": "Verb",
  "Polarity": "Affirmative",  // Verb remains affirmative
  // ...
}
```

### Key Observation: Semantic Negation Location

TBTA marks polarity **on the semantically negated element**, not necessarily where the negative morpheme appears syntactically:

- **Negative verb** ("did not have"): Polarity marked on verb
- **Negative noun** ("nothing" = "no thing"): Polarity marked on noun, not verb

This is **semantic**, not **surface-syntactic** annotation.

---

## Cross-Linguistic Negation Typology

### 1. Types of Negative Morphemes (WALS Chapter 112 - Dryer)

Based on survey of 1,257 languages:

| Type | Count | Description | Examples |
|------|-------|-------------|----------|
| **Negative Particle** | 502 | Separate word | English *not*, Musgu *pày* |
| **Negative Affix** | 395 | Bound morpheme | Kolyma Yukaghir *el-* (prefix) |
| **Negative Auxiliary** | 47 | Inflecting verb | Finnish *e-n* (person-marked) |
| **Double Negation** | 119 | Two simultaneous markers | French *ne...pas* |
| **Unclear Word/Affix** | 73 | Ambiguous status | Maori *kaahore* |
| **Variation (Word+Affix)** | 21 | Both strategies | Rama *aa* (particle) / *-taama* (suffix) |

#### Geographic Distribution

- **Negative particles & affixes**: Globally widespread
- **Negative auxiliaries**: Concentrated in northern Eurasia (Finland → Siberia)
- **Double negation**: Common in New Guinea and Africa; rare in Europe/Asia
- **Unclear negatives**: Predominate in Southeast Asia (isolating languages)

### 2. Position of Negative Morpheme (WALS Chapter 143)

| Type | Count | Description | Examples |
|------|-------|-------------|----------|
| **NegV (Preverbal)** | 525 | Negative precedes verb | Most common globally |
| **VNeg (Postverbal)** | 171 | Negative follows verb | Central Africa, New Guinea |
| **[Neg-V] (Prefix)** | 162 | Negative prefix | Africa, Tibeto-Burman |
| **[V-Neg] (Suffix)** | 202 | Negative suffix | South America (concentrated) |
| **Negative Tone** | 1 | Tone alone marks negation | Very rare |

**Key Pattern**: Overwhelming cross-linguistic preference for **preverbal negation** (Type 1).

### 3. Standard Negation: Symmetric vs. Asymmetric (Miestamo 2005, 2007)

#### Symmetric Negation
Affirmative and negative clauses differ **only** by presence/absence of the negator.

**Example (English)**:
- Affirmative: *John **sleeps***
- Negative: *John **does not sleep***

(Structure remains parallel; only negator added)

#### Asymmetric Negation
Negation triggers **additional structural changes**:

- **TAM (Tense/Aspect/Mood) modifications**
- **Person/number agreement changes**
- **Word order shifts**
- **Finiteness reduction**

**Example (Finnish - Negative Auxiliary)**:
- Affirmative: *Minä **laula-n*** (I sing-1SG)
- Negative: ***E-n** laula* (NEG-1SG sing)

(Person/number shifts from verb to negative auxiliary)

**Example (Slavic - Genitive of Negation)**:
- Affirmative: *Я читаю **книгу*** (I read book-ACC)
- Negative: *Я не читаю **книги*** (I not read book-GEN)

(Object case changes from accusative to genitive under negation)

### 4. Constituent vs. Sentential Negation

#### Sentential Negation
Negates the entire proposition/clause.

**Example**: *John **did not** come.*
(The entire event is negated)

#### Constituent Negation
Negates a specific element within the clause.

**Example**: ***Not** John came, but Mary.*
(Only the subject is negated; event itself is affirmed)

### 5. Scope Ambiguity

Negation can create scope ambiguities depending on what falls under its semantic influence.

**Classic Example**: *"I did not find many valuable books"*

- **Reading 1 (Wide scope)**: "There were many valuable books which I did not find" (many > not)
- **Reading 2 (Narrow scope)**: "There were not many valuable books which I found" (not > many)

**Another Example**: *"Arthur does not discipline his children because he loves them"*

- **Reading 1**: The reason he doesn't discipline = he loves them
- **Reading 2**: He disciplines them, but not because he loves them (for some other reason)

### 6. Negative Concord vs. Double Negation

#### Negative Concord (Romance, Slavic)
Multiple negative elements express **single negation**.

**Spanish**: *No veo nada* (NEG see nothing) = "I see nothing" (not "I don't see something")

**Italian**: *Non ho visto nessuno* (not have seen nobody) = "I saw nobody"

#### Double Negation (English, Logic)
Multiple negatives **cancel out** to create affirmation.

**English (non-standard)**: *"I didn't see nothing"* (prescriptively = "I saw something")

**Standard Logic**: ¬¬P = P

#### Types of Negative Concord

**Strict NC**: N-word requires negative marker in all positions
**Non-strict NC**: Preverbal n-word alone suffices; postverbal requires marker

**Spanish/Italian (Non-strict)**:
- Postverbal: *No vino **nadie*** (NEG came nobody) - marker required
- Preverbal: ***Nadie** vino* (Nobody came) - no marker

### 7. Negative Polarity Items (NPIs)

Lexical items that require negative (or downward-entailing) licensing contexts.

**English NPIs**: *any, ever, yet, at all, lift a finger*

**Example**:
- ✓ *I didn't see **anyone***
- ✗ **I saw **anyone*** (ungrammatical without negation)

**Licensing Contexts** (beyond negation):
- Questions: *Did you see **anyone**?*
- Conditionals: *If you see **anyone**, tell me*
- Universal quantifiers: *Everyone who saw **anyone** reported it*
- Comparatives: *He's smarter than **anyone** I know*

**Cross-linguistic Variation**: NPIs show substantial language-specific restrictions.

**Example**: German *jemals* ("ever") cannot be licensed by clause-mate negation, while English *ever* can.

### 8. Jespersen's Cycle

A grammaticalization process where negation markers strengthen and eventually replace themselves.

#### The Stages

**Stage 1**: Simple preverbal negator (NEG1)
- Latin: *non*

**Stage 2**: NEG1 + emphatic element (NEG2)
- Old French: *ne...pas* ("not...step")

**Stage 3**: NEG2 becomes obligatory, NEG1 optional
- Modern spoken French: *ne* often dropped

**Stage 4**: NEG1 extinct, NEG2 sole marker
- (Could begin cycle again)

#### Examples

**French**: *ne* → *ne...pas* → *pas* (in speech)
**English**: *ne* (Old English) → *not*
**Greek**: Classical forms → various modern dialectal patterns

---

## Biblical Source Language Negation

### Hebrew Negation

Hebrew uses **different negative particles** for different contexts:

| Particle | Form | Usage | Examples |
|----------|------|-------|----------|
| **לֹא** (lo) | Absolute negation | Declarative statements, permanent prohibitions | Ten Commandments: *לֹא תִרְצָח* (lo tirtzach) "You shall not murder" |
| **אַל** (al) | Qualified negation | Immediate/specific prohibitions, jussive/cohortative negation | *אַל־תִּירָא* (al-tira) "Do not fear" (immediate) |
| **אֵין** (ein) | Existential negation | "There is not", possession | *אֵין אֱלֹהִים* (ein elohim) "There is no God" |

#### Key Distinctions

**לֹא vs. אַל in Prohibitions**:

- **לֹא + Imperfect**: Permanent, absolute command (legal/declarative)
  - Example: *לֹא תִגְנֹב* (lo tignov) "You shall not steal" (universal law)

- **אַל + Jussive**: Immediate, specific request (imperative)
  - Example: *אַל תִּגְנֹב* (al tignov) "Don't steal [right now]" (specific context)

The **choice between לֹא and אַל** carries **semantic and pragmatic weight**:
- **לֹא**: Authority, permanence, objective prohibition
- **אַל**: Urgency, specific situation, subjective request

### Greek Negation

Ancient Greek distinguishes negation by **mood and semantic context**:

| Particle | Usage | Semantics |
|----------|-------|-----------|
| **οὐ** (ou) | Indicative mood, objective facts | "Negation of fact/statement" - categorical denial |
| **μή** (mē) | Subjunctive, optative, imperative, non-indicative | "Negation of will/thought" - hypothetical/subjective |

#### οὐ - Negation of Fact
- **Declarative statements**
- **Factual denials**
- **Indicative mood**

**Example**: *οὐκ οἶδα* (ouk oida) "I do not know" (statement of fact)

#### μή - Negation of Will/Thought
- **Prohibitions** (negative commands)
- **Purpose clauses**
- **Conditions**
- **Wishes/fears**

**Example**: *μὴ φοβοῦ* (mē phobou) "Do not fear!" (prohibition)

#### The Emphatic Construction: οὐ μή

When **οὐ** and **μή** combine (in that order), they create the **strongest possible future negation**:

**οὐ μή + Subjunctive/Future Indicative** = Emphatic future negation

**Example (John 11:26)**:
*ὁ πιστεύων εἰς ἐμὲ **οὐ μὴ** ἀποθάνῃ εἰς τὸν αἰῶνα*
"Whoever believes in me will **certainly never** die forever"

**Semantic Force**:
- **οὐ**: Absolute negation component
- **μή**: Subjective/modal component
- **Combined**: Emphatic denial of possibility - "absolutely will not, by no means"

#### Scholarly Debate

Recent research (Hübner 2021, "The Emphatic Hypernegation That Was(n't)") questions whether οὐ μή is always maximally emphatic or potentially context-dependent, but traditional grammars (Smyth, BDF) consistently treat it as the strongest negation available.

### Implications for TBTA

TBTA's **binary "Affirmative"/"Negative"** system collapses these distinctions:

- Hebrew **לֹא** vs. **אַל**: Both marked "Negative" (loses modal/pragmatic distinction)
- Greek **οὐ** vs. **μή**: Both marked "Negative" (loses mood distinction)
- Greek **οὐ μή**: Still just "Negative" (loses emphasis marking)

**Question for Reproduction**: Should we:
1. **Preserve TBTA's simplicity** (binary marking)?
2. **Extend with subtypes** (Negative-Declarative, Negative-Imperative, Negative-Emphatic)?

For target languages with Hebrew-like or Greek-like distinctions, the **source language context** will be crucial for selecting appropriate forms.

---

## Language Family Negation Patterns

### Overview of Our Dataset

From the 1009 languages in `src/constants/languages.tsv`, major families include:

- **Austronesian**: 176 languages (realis/irrealis interactions)
- **Trans-New Guinea**: 129 languages (Proto-TNG *ma- negation)
- **Niger-Congo**: 94 languages (tone, serial verbs, diverse strategies)
- **Indo-European**: 55 languages (genitive of negation, negative concord)
- **Other families**: 555 languages (70+ additional families)

### 1. Austronesian Languages (176 languages)

#### Realis/Irrealis Mood Interaction

Many Austronesian languages have primary **realis vs. irrealis** distinction:

**Realis Contexts**:
- Non-future tense
- **Positive polarity** ← relevant to negation
- Indicative mood

**Irrealis Contexts**:
- Future tense/prospective aspect
- **Negative polarity** ← negation often triggers irrealis
- Conditionals, counterfactuals
- Jussive modalities

**Implication**: Negation is often **morphologically linked to mood** in Austronesian languages.

**Example Pattern**:
- Affirmative past: REALIS marker + verb
- Negative past: IRREALIS marker + negative + verb

#### Translation Consideration

For Austronesian languages, polarity annotation must account for:
1. **Negative morpheme** itself
2. **Mood shift** triggered by negation
3. Possible **aspect changes** in negative contexts

### 2. Trans-New Guinea Languages (129 languages)

#### Proto-TNG Negation

**Reconstructed form**: **\*ma** (negative marker)

**Modern reflexes**:
- **mV- forms** (often \*ma): Angaatɨha, Apalɨ, Waskia, Kalam, Kâte, Kombe
- **nV- forms** (\*na ~ \*naa): Awara, Enga, Ku Waru, Middle Wahgi, Oksapmin

#### Typical Pattern

**Preverbal negative particle/prefix** (aligns with global NegV preference)

#### Additional Features

Many TNG languages exhibit:
- **Switch-reference systems**: Negative clauses may trigger different switch-reference marking
- **Clause chaining**: Negation scope over entire chains
- **Evidentiality** (in some Highland languages): Interaction with information source marking

#### Translation Consideration

Negation in TNG languages may affect:
1. Switch-reference marking (same/different subject)
2. Clause chain structure
3. Evidential marking (if present)

### 3. Niger-Congo Languages (94 languages)

Niger-Congo exhibits **extreme diversity** in negation strategies:

#### Bantu Languages (Majority of our NC dataset)

**Common Patterns**:
- **Preverbal negative markers**
- **Negative suffixes on verbs**
- **Double/triple negation** (Jespersen's Cycle stages)
- **Tone changes** under negation

**Example (Kongo)**:
- Preverbal *ka* + verb suffix *-a:* + clause-final *kó*
(Triple negation strategy)

**Example (Ewondo)**:
- Negative word + **negative tone on verb** + postverbal negative word

**Genitive of Negation**: Absent in Bantu (unlike Slavic), but **noun class agreement** may be affected

#### Serial Verb Constructions + Negation

**Unity of Polarity**: A key feature of SVCs is that negation scopes over the **entire verb series**.

**Example Pattern**:
- Affirmative: *Subject + V1 + V2 + V3 + Object*
- Negative: *Subject + **NEG** + V1 + V2 + V3 + Object*

**Implication**: TBTA marks each verb in an SVC individually, but all would receive same polarity value if the entire series is negated.

#### Tone and Negation

**Tonal Languages** (most Niger-Congo): Negation may:
1. Introduce **negative tone patterns**
2. **Override lexical tones** on verbs
3. Create **tonal spreading** effects

**Example (Igbo, Orsu dialect)**: Tone variation alone marks negation

#### Translation Consideration

For Niger-Congo languages, polarity reproduction must account for:
1. **Multiple negative morphemes** (identify all components)
2. **Tonal changes** (not visible in TBTA's gloss representation)
3. **Serial verb unity** (all verbs share polarity)
4. **Noun class agreement** in negative clauses (may differ from affirmative)

### 4. Indo-European Languages (55 languages)

#### Slavic Languages: Genitive of Negation

**Rule**: Direct object in accusative case → **genitive case** under negation

**Example (Russian)**:
- Affirmative: *Я читаю **книгу*** (I read book-**ACC**)
- Negative: *Я не читаю **книги*** (I NEG read book-**GEN**)

**Distribution**:
- **Mandatory**: Slovenian, Polish, Lithuanian, Old Church Slavonic
- **Optional**: Russian, Belarusian (genitive preferred)
- **Archaic**: Czech, Slovak, Serbo-Croatian (accusative now preferred)

**Implication**: Negation is **asymmetric** in these languages (triggers case change)

#### Slavic Languages: Negative Concord

**Pattern**: Multiple n-words + negative marker = single negation

**Example (Russian)**:
*Я **никогда ничего никому** не говорил*
"I **never nothing nobody** NEG told"
= "I never told anything to anyone"

**Types**:
- **Strict NC**: N-word always requires negative marker (Old Romance)
- **Non-strict NC**: Preverbal n-word alone, postverbal requires marker (Spanish, Italian)

Most Slavic languages show **strict or nearly strict** negative concord.

#### Romance Languages: Negative Concord + Jespersen's Cycle

**Spanish**: *No...nada/nadie/nunca*
**French**: *ne...pas/rien/personne/jamais*
**Italian**: *non...niente/nessuno/mai*

**French Jespersen's Cycle**:
- Stage 1 (Latin): *non*
- Stage 2 (Old French): *ne...pas*
- Stage 3 (Modern Standard): *ne...pas* (both obligatory)
- Stage 4 (Spoken French): *pas* alone (ne dropping)

#### Germanic Languages: Single Negation

**English, German, Dutch**: Multiple negatives = multiple negations (prescriptively)

**Example (Standard English)**:
*I didn't see nothing* ≠ *I saw nothing*
(Double negation = affirmation, prescriptively)

**Note**: Non-standard dialects often have negative concord

#### Translation Consideration

For Indo-European languages in our dataset:
1. **Slavic**: Mark genitive case on affected nouns; handle n-words correctly
2. **Romance**: Understand negative concord patterns; track Jespersen's Cycle stage
3. **Germanic**: Simple symmetric negation (generally)

### 5. Other Major Families

#### Afro-Asiatic (25 languages)
- **Semitic** (includes Hebrew patterns): Diverse strategies
- **Berber**: Negative circumfixes common
- **Cushitic**: Variable patterns

#### Sino-Tibetan
- **Tibeto-Burman**: Often [Neg-V] prefix pattern (WALS 143)
- **Chinese**: Preverbal negators (*bù*, *méi*)

#### Otomanguean (69 languages)
- **Tonal**: Negation interacts with tone
- Many have **negative prefixes**

#### Mayan (41 languages)
- Complex **TAM systems**: Negation often triggers asymmetry
- Ergative-absolutive: Negation may affect case marking

#### Australian (36 languages)
- Diverse strategies (family-level patterns weak)
- Some have **negative auxiliary** structures

---

## Scope of Negation

### Definition

**Scope of negation**: The portion of the sentence that falls under the semantic influence of the negative operator.

### Scope and Syntactic Position

**General Principle**: Negation takes scope over **all constituents to its right** (in languages with right-branching structure).

**C-command**: In hierarchical syntax, negation operator c-commands (and thus scopes over) elements in its c-command domain.

### Scope Ambiguity Examples

#### Example 1: Quantifier Scope
*"I did not find many valuable books"*

- **Reading 1**: ∃ many valuable books [I did not find them]
  (Many books exist that I failed to find)

- **Reading 2**: ¬∃ many valuable books [that I found]
  (Few books of value were found by me)

**Difference**: Relative scope of **negation** and **quantifier** ("many")

#### Example 2: Reason Clause
*"Arthur does not discipline his children because he loves them"*

- **Reading 1**: ¬discipline **because** loves
  (He doesn't discipline; the reason is love)

- **Reading 2**: discipline ¬**because** loves
  (He does discipline, but for a different reason)

**Difference**: Does negation scope over the main clause only, or over the reason relation?

#### Example 3: Universal Quantifier
*"All that glitters is not gold"* (proverb)

- **Reading 1** (Intended): ¬∀x [glitters(x) → gold(x)]
  (Not everything that glitters is gold)

- **Reading 2** (Logical): ∀x [glitters(x) → ¬gold(x)]
  (Everything that glitters is non-gold)

**Difference**: Scope of **negation** relative to **universal quantifier** ("all")

### Implications for TBTA Polarity

TBTA's approach:
- Marks polarity on **semantically negated elements**
- Does **not explicitly encode scope**

**For reproduction**:
1. Identify **semantic scope** of negation
2. Mark all elements **under negation's scope** as "Negative"
3. Elements **outside scope** remain "Affirmative" even if syntactically in a negative clause

**Example Analysis**:
*"I didn't buy many books because they were expensive"*

If interpretation = "I bought few books" (negation scopes over "many"):
- Verb "buy": Negative
- Quantifier "many": Under negation's scope → annotate accordingly

Scope ambiguities require **semantic/pragmatic analysis**, not just syntactic parsing.

---

## Emphatic Affirmation

While TBTA's system focuses on **Affirmative vs. Negative**, many languages mark **degrees of affirmation**.

### Types of Emphatic Affirmation

#### 1. Affirmative Particles

**Hebrew**:
- **אָמֵן** (amen): "Truly, verily, so be it"
- **אָכֵן** (aken): "Indeed, surely"
- **אֲבָל** (aval): "Indeed, truly, verily"

**Greek**:
- **ἀμήν** (amēn): "Truly, verily, amen" (borrowed from Hebrew)
- **ναί** (nai): "Yes, indeed"
- **ἀληθῶς** (alēthōs): "Truly, really"

**New Testament Usage**:
- **"Ἀμὴν ἀμὴν λέγω ὑμῖν"** (amēn amēn legō hymin)
  "Truly, truly, I say to you" (double amen = emphatic assertion)

#### 2. Focus Particles

Many languages use particles to emphasize affirmation:
- **English**: *indeed, certainly, definitely, truly, really*
- **Cross-linguistic**: Particles marking **epistemic certainty** or **speaker commitment**

#### 3. Reduplication

Some languages use **reduplication** for emphasis:
- **Hebrew**: *אָמֵן וְאָמֵן* (amen ve-amen) "Amen and amen"
- **Greek**: *ἀμὴν ἀμήν* (double amen)

#### 4. Morphological Marking

Languages may have **affirmative mood** or **emphatic verbal morphology**:
- Contrasts with plain indicative
- Signals speaker's strong commitment to truth

### Potential TBTA Extension

Currently TBTA uses binary **Affirmative/Negative**. A potential extension:

- **Affirmative** (unmarked)
- **Emphatic Affirmative** (marked with emphatic particles/morphology)
- **Negative**
- **Emphatic Negative** (e.g., οὐ μή in Greek)

However, **TBTA appears to collapse emphasis** into simple binary polarity.

### Translation Implication

For target languages with **emphatic affirmation marking**:
- Translator must recognize emphatic markers in source (ἀμήν, οὐ μή)
- Select appropriate emphatic form in target language
- TBTA polarity alone insufficient (needs commentary/exegetical context)

---

## Methodology for Reproduction

### Step-by-Step Process

#### 1. Source Language Analysis

**For each word/constituent in the verse**:

**A. Identify Negation Morphology**
- Does the word contain a negative morpheme?
  - Hebrew: **לֹא**, **אַל**, **אֵין**, negative prefixes
  - Greek: **οὐ**, **μή**, **οὐ μή** (emphatic)

**B. Analyze Semantic Role**
- Is this element **semantically negative**?
  - English "nothing" = "no thing" → noun is negative
  - Hebrew *אֵין* ("there is not") → existential verb is negative

**C. Determine Scope**
- What is the **scope of negation**?
  - Which elements fall under the negative operator's c-command domain?
  - Resolve scope ambiguities using context

#### 2. Polarity Assignment

**Rule 1**: If element is **negated** (morphologically or semantically) → **"Negative"**

**Rule 2**: If element is **under scope of negation** → Consider scope:
  - **Narrow scope**: Only syntactically marked element is Negative
  - **Wide scope**: Multiple elements may be Negative

**Rule 3**: All other elements → **"Affirmative"**

**Rule 4**: Emphatic markers (ἀμήν, οὐ μή) → Currently collapsed to binary (Affirmative or Negative)

#### 3. Language-Specific Considerations

**Check target language family** (from our 1009 languages):

**Austronesian**:
- Will negation trigger **realis → irrealis** shift?
- Note: Mood shift is separate from polarity marking

**Trans-New Guinea**:
- Identify **negative morpheme** (*ma-* or *na-* reflex)
- Check for **switch-reference** effects
- Clause-chaining implications

**Niger-Congo**:
- **Bantu**: Multiple negative morphemes (mark each)
- **Serial verbs**: Unity of polarity across series
- **Tone**: Negative tones (not marked in TBTA, but present in target language)

**Indo-European**:
- **Slavic**: Genitive of negation on objects (separate from polarity)
- **Negative concord**: N-words require coordination with negative marker
- **Romance**: Jespersen's Cycle stage affects form selection

**Other families**: Consult family-specific negation patterns

#### 4. Validation

**Check consistency**:
- All verbs in a serial verb construction share polarity
- Negative concord n-words are not separately marked "Negative" for noun itself (polarity is on the construction as a whole)
- Scope ambiguities resolved consistently across similar contexts

#### 5. Metadata Annotation

**Beyond binary polarity**, record:
- **Emphasis**: Is this emphatic affirmation (ἀμήν) or emphatic negation (οὐ μή)?
- **Negation type**: Sentential vs. constituent
- **Source morphemes**: Which negative particles/affixes are present?
- **Target language implications**: Does this trigger asymmetric negation?

---

## Sources Consulted

### TBTA Primary Sources

1. **TBTA Database Export**
   GitHub: https://github.com/AllTheWord/tbta_db_export
   Files examined: `json/00_001_001_Genesis.json`, `json/00_001_002_Genesis.json`, `json/00_003_019_Genesis.json`

### Cross-Linguistic Typology

2. **Dryer, Matthew S. (2013).** "Negative Morphemes." In: *The World Atlas of Language Structures Online*. Chapter 112.
   URL: https://wals.info/chapter/112
   Coverage: 1,257 languages, six types of negative morphemes, geographic distribution

3. **Dryer, Matthew S. (2013).** "Order of Negative Morpheme and Verb." In: *The World Atlas of Language Structures Online*. Chapter 143.
   URL: https://wals.info/chapter/143
   Coverage: Five positional types, overwhelming preverbal preference

4. **Miestamo, Matti (2005).** *Standard Negation: The Negation of Declarative Verbal Main Clauses in a Typological Perspective*. Berlin/New York: Mouton de Gruyter.
   Key concepts: Symmetric vs. asymmetric negation, structural differences in negative constructions

5. **Miestamo, Matti (2007).** "Negation – An Overview of Typological Research." *Language and Linguistics Compass* 1(5): 552–570.
   URL: https://linguistics.berkeley.edu/~syntax-circle/syntax-group/spr08/miestamo.pdf
   Comprehensive overview of negation typology

6. **Klima, Edward (1964).** "Negation in English." In: *The Structure of Language*, eds. Fodor & Katz. Prentice-Hall.
   Classic work distinguishing sentential vs. constituent negation

### Biblical Languages

7. **Blue Letter Bible (2012).** "Emphatic Negations in Biblical Greek."
   URL: https://blogs.blueletterbible.org/blb/2012/05/23/emphatic-negations-in-biblical-greek/
   Focus on οὐ μή construction and emphatic force

8. **Mitiku, Abera.** "The Use of Οὐ Μή in the New Testament: Emphatic or Mild Negation?" *Filologia Neotestamentaria* 22:2.
   URL: https://www.galaxie.com/article/fm22-2-05
   Scholarly debate on strength of οὐ μή negation

9. **Smyth, Herbert Weir.** *A Greek Grammar for Colleges, Part IV: Syntax* - "Negative Sentences."
   URL: https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.04.0007:part=4:chapter=59
   Comprehensive description of οὐ vs. μή distinction

10. **Unfold Word Hebrew Grammar.** "Particle Negative."
    URL: https://uhg.readthedocs.io/en/latest/particle_negative.html
    Detailed treatment of לֹא, אַל, and אֵין

11. **Blue Letter Bible.** "Hebrew Grammar - Imperatives, Emphatic Imperatives, & Negative Prohibitions."
    URL: https://www.blueletterbible.org/resources/grammars/hebrew/simplified-hebrew/imperatives.cfm
    Explanation of לֹא vs. אַל in prohibitive contexts

### Negative Concord and Polarity Items

12. **Giannakidou, Anastasia & Zeijlstra, Hedde (2017).** "The Landscape of Negative Dependencies: Negative Concord and N-Words." In: *The Wiley Blackwell Companion to Syntax*, 2nd ed.
    URL: https://home.uchicago.edu/~giannaki/pubs/Giannakidou.zeijlstra.proofs.SC2017.pdf
    Comprehensive analysis of negative concord typology

13. **Giannakidou, Anastasia (2011).** "Negative and positive polarity items." In: Maienborn et al. (eds.), *Semantics: An International Handbook of Natural Language Meaning*.
    URL: https://home.uchicago.edu/~giannaki/pubs/HSK.chapter64.pdf
    Theoretical treatment of NPIs and their licensing

14. **MDPI (2021).** "Pas de Problème: The Distribution and Nature of Double Negation in French and Other Romance Negative Concord Languages." *Languages* 8(2):118.
    URL: https://www.mdpi.com/2226-471X/8/2/118
    Romance negative concord patterns

### Language Family Specific

15. **Pawley, Andrew & Hammarström, Harald (2018).** "The Trans New Guinea family." In: Palmer (ed.), *The Languages and Linguistics of the New Guinea Area*, pp. 21-195. De Gruyter.
    Proto-TNG *ma negation reconstruction

16. **Güldemann, Tom (1999).** "The genesis of verbal negation in Bantu and its dependency on functional features of clause types." In: Hombert & Hyman (eds.), *Bantu Historical Linguistics*, pp. 545-587. CSLI.
    URL: https://www.researchgate.net/publication/319527597
    Detailed analysis of Bantu negation strategies

17. **Schneider, Lauren (2019).** "Negation Patterns in the Kwa Language Group." Academia.edu.
    URL: https://www.academia.edu/43811381/
    Niger-Congo Kwa negation study

18. **Partee, Barbara H. & Borschev, Vladimir (various).** "The Russian Genitive of Negation in Existential Sentences."
    URL: http://people.umass.edu/partee/docs/GenNegTravaux.pdf
    Slavic genitive of negation analysis

19. **Pirnat, Agata (2011).** "Genesis of the Genitive of Negation in Balto-Slavic and Its Evidence in Contemporary Slovenian." *Kansas Working Papers in Linguistics* 32.
    URL: https://kuscholarworks.ku.edu/bitstream/handle/1808/18309/01_Pirnat.pdf
    Historical and contemporary analysis

20. **Cleary-Kemp, Jessica (2015).** "Irrealis as verbal non-specificity in Koro (Oceanic)." *Proceedings of the Linguistic Society of America*.
    URL: https://journals.linguisticsociety.org/proceedings/index.php/BLS/article/download/3131/2849/3634
    Austronesian irrealis and negation interaction

### Scope and Ambiguity

21. **Linguistics Stack Exchange (various contributors).** "What is the scope of negation?"
    URL: https://linguistics.stackexchange.com/questions/8912/what-is-the-scope-of-negation
    Discussion with examples of scope ambiguity

22. **Kroeger, Paul (2018).** *Analyzing Meaning: An Introduction to Semantics and Pragmatics*. Section 14.5: "Scope ambiguities." Social Sci LibreTexts.
    URL: https://socialsci.libretexts.org/Bookshelves/Linguistics/Analyzing_Meaning
    Textbook treatment of scope interactions

23. **Wikipedia.** "Affirmation and negation."
    URL: https://en.wikipedia.org/wiki/Affirmation_and_negation
    Overview of constituent vs. sentential negation

### Jespersen's Cycle

24. **Wikipedia.** "Jespersen's cycle."
    URL: https://en.wikipedia.org/wiki/Jespersen's_cycle
    Historical development of negation markers

25. **Kiparsky, Paul.** "Tracking Jespersen's Cycle." Stanford University.
    URL: https://web.stanford.edu/~kiparsky/Papers/lesvosnegation.pdf
    Detailed formal analysis of grammaticalization stages

### Additional Academic Sources

26. **Oxford Research Encyclopedia of Linguistics.** "Negation (Chapter 13)." In: *The Cambridge Handbook of Linguistic Typology*.
    URL: https://www.cambridge.org/core/books/abs/cambridge-handbook-of-linguistic-typology/negation/
    Comprehensive typological overview

27. **Stanford Encyclopedia of Philosophy.** "Negation."
    URL: https://plato.stanford.edu/entries/negation/
    Philosophical and logical perspectives

---

## Document Summary

This comprehensive research document examined:
1. **TBTA's binary polarity system** (Affirmative/Negative) with application to nouns and verbs
2. **Six types of negative morphemes** across 1,257 languages with geographic distributions
3. **Symmetric vs. asymmetric negation** patterns and their implications
4. **Hebrew and Greek negation systems** with emphasis on distinctions collapsed by TBTA
5. **Language family-specific negation strategies** for our 1009-language dataset
6. **Scope of negation** and ambiguity resolution
7. **Emphatic affirmation** as potential extension point

**Key Finding**: TBTA uses **semantic polarity marking** (marks the negated element, not just where negation appears), requiring interpreters to:
- Analyze source language negation morphology
- Determine semantic scope
- Consider target language implications (mood shifts, case changes, negative concord)
- Understand family-specific patterns for natural translation

**Next Steps**: See `LEARNINGS.md` for initial thesis on reproducing TBTA polarity decisions.

---

**Document Status**: Research complete, ready for reproduction experimentation
**Total Sources**: 27+ academic and primary sources consulted
**Languages Covered**: 1,009 (dataset) + 1,257 (WALS typological sample)
**Date**: 2025-11-05
