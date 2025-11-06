# TBTA Degree Annotation System: Comprehensive Documentation

## Overview

This document provides a comprehensive analysis of TBTA's degree annotation system for adjectives, adverbs, and verbs. The degree feature captures how languages express comparison, intensification, and gradation of properties.

## TBTA Degree Values

TBTA encodes degree information using single-letter codes at specific positions in the semantic string. The complete inventory varies by part of speech:

### Adjectives (Position 4)
11 possible values:

| Code | Meaning | Description |
|------|---------|-------------|
| N | No Degree | Positive/base form with no degree marking |
| C | Comparative | Expresses "more X than Y" |
| S | Superlative | Expresses "most X (of all)" |
| I | Intensified | Enhanced degree ("very X", "extremely X") |
| E | Extremely Intensified | Highest intensification ("exceedingly X") |
| T | 'too' | Excessive degree ("too X") |
| L | 'less' | Downward comparison ("less X than Y") |
| l | 'least' | Downward superlative ("least X of all") |
| q | Equality | Equative comparison ("as X as Y") |
| i | Intensified Comparative | "Much more X than Y" |
| s | Superlative of 2 items | "The X-er of the two" |

### Adverbs (Position 4)
8 possible values:

| Code | Meaning |
|------|---------|
| N | No Degree |
| C | Comparative |
| S | Superlative |
| V | Intensified (equivalent to I for adjectives) |
| E | Extremely Intensified |
| T | 'too' |
| L | 'less' |
| l | 'least' |

Note: Adverbs lack the adjective-specific values for equality (q), intensified comparative (i), and superlative of 2 items (s).

### Verbs (Position 9)
8 possible values:

| Code | Meaning |
|------|---------|
| N | No Degree |
| C | Comparative |
| S | Superlative |
| I | Intensified |
| E | Extremely Intensified |
| T | 'too' |
| L | 'less' |
| l | 'least' |

Note: Verbs lack equality and comparative variation markers but include intensification.

## Cross-Linguistic Typology of Comparison

### 1. Comparative Constructions

Based on WALS Chapter 121 (Stassen), comparative constructions are classified by how the standard NP (comparison benchmark) receives case marking:

#### Fixed-Case Comparatives

**A. Exceed Comparative**
- Standard NP functions as direct object of "exceed/surpass" verb
- Example: Duala "this house it big exceed that" = "This house is bigger than that"
- Common in: Sub-Saharan Africa, Southeast Asia
- Distribution: 33/167 languages surveyed

**B. Locational Comparative**
- Standard NP takes locational/adverbial case form
- Three subtypes:
  - **From-comparatives**: Estonian "spring is more beautiful than fall" (standard marked with "from")
  - **To-comparatives**: Maasai "hartebeest is bigger than waterbuck" (standard marked with "to")
  - **At-comparatives**: Tubu "his eye is redder than blood" (standard marked with "at")
- Common in: Northern Africa, Eurasia
- Distribution: 78/167 languages (most common type)

#### Derived-Case Comparatives

**C. Conjoined Comparative**
- Two parallel clauses with independent predicates
- Uses antonymous terms or positive-negative polarity
- Example: Amele "this house big, that house small" = "This house is bigger than that house"
- Common in: Australia, New Guinea
- Distribution: 34/167 languages
- **Crucial**: Used in degree-neutral languages (see section 3)

**D. Particle Comparative**
- Comparative particle accompanies standard NP
- Example: English "taller than", French "plus grand que", Hungarian "István taller than Peter"
- Common in: Europe
- Distribution: 22/167 languages

### 2. Degree Morphology Types

Languages employ different strategies for marking degree:

#### A. Synthetic/Morphological
Formation through affixation:

**Indo-European Examples:**
- English: -er (comparative), -est (superlative)
- Latin: -ior/-ius (comparative), -issimus/-a/-um (superlative)
- Ancient Greek: -τερος/-τέρᾱ/-τερον (comparative), -τατος/-τάτη/-τατον (superlative)
- Alternative Greek: -ῑ́ων/-ῐ́ον (comparative), -ιστος/-ιστη/-ιστον (superlative)

**Characteristics:**
- Inherited from Proto-Indo-European *-yos-/-ies- (comparative), *-isto- (superlative)
- Retained in Germanic, Slavic, some Romance
- Most robust in languages with fusional morphology

#### B. Analytic/Periphrastic
Formation through separate degree words:

**Examples:**
- English: more/most (esp. polysyllabic adjectives)
- Ancient Greek: μᾶλλον (more), μάλιστα (most)
- French: plus (more), le plus (most)
- Mandarin: 更 gèng (more), 最 zuì (most)

**Usage Contexts:**
- Greek: Required for participles, compound adjectives, -τός verbal adjectives, -ιος adjectives
- English: Polysyllabic adjectives, stylistic variation
- Universal: Languages without synthetic morphology

#### C. Mixed Systems
Many languages employ both strategies contextually:
- English: good → better/best (synthetic) vs. beautiful → more/most beautiful (analytic)
- Greek: Simple adjectives (synthetic) vs. compounds (analytic)
- Romance: Varying degrees of synthesis retention (Romanian high, French low)

### 3. Degree-Neutral Languages

Recent research (Beck et al. 2009, Bochnak 2013) identifies languages lacking degree-based semantics entirely.

#### The Degree Semantics Parameter
Languages systematically differ in whether gradable predicates introduce degree arguments:
- **Degree-based**: Predicates have type ⟨d,⟨e,t⟩⟩ with explicit degree variable
- **Delineation-based**: Predicates have type ⟨e,t⟩ without degree variable

#### Confirmed Degree-Neutral Languages

**Motu** (Austronesian, Papua New Guinea)
- Uses conjoined comparison exclusively
- Lacks degree morphology entirely

**Fijian** (Austronesian, Fiji)
- IC-only language (individual comparison)
- No degree arguments in gradable predicates

**Washo** (isolate/Hokan, California/Nevada)
- Systematically lacks degree morphology
- Gradable predicates type ⟨e,t⟩

**Warlpiri** (Pama-Nyungan, Australia)
- Gradable predicates do not combine with degree arguments
- Uses alternative comparison strategies

#### Comparison Strategies in Degree-Neutral Languages
- Conjoined comparatives (most common)
- Positive-negative polarity
- Contextual inference
- Absolute rather than scalar semantics

### 4. Biblical Languages Comparison Systems

#### Ancient Greek (Koine)

**Synthetic Formation:**
- Regular comparative: -τερος/-τέρᾱ/-τερον (suffix to masculine stem)
- Regular superlative: -τατος/-τάτη/-τατον
- Irregular comparative: -ῑ́ων/-ῑ́ᾱ/-ῐ́ον (masculine/feminine, neuter)
- Irregular superlative: -ιστος/-ιστη/-ιστον

**Analytic Formation:**
- μᾶλλον + positive adjective (comparative)
- μάλιστα + positive adjective (superlative)

**Required Analytic Contexts:**
- Participles (cannot take comparative/superlative suffixes)
- Compound adjectives
- Prepositional prefix adjectives
- Verbal adjectives in -τός
- Adjectives in -ιος

**New Testament Examples:**
- John 15:13: μείζονα (greater, comparative from μέγας)
- Synthetic comparative forms common in NT

#### Biblical Hebrew

**Fundamental Difference:** Hebrew lacks morphological comparison entirely. All comparison is periphrastic.

**Comparative Strategies:**

1. **Preposition מִן (min) "from"**
   - Adjective remains in base form
   - Example: "X is great from Y" = "X is greater than Y"
   - Standard marked with מִן
   - Can also use מִכֹּל (mikkol) "from all" for emphasis

2. **Comparative Context Without Overt Marking**
   - Context-dependent interpretation
   - Adjective + implied comparison

**Superlative Strategies:**

1. **Construct State: Singular + Plural**
   - Pattern: "X of Xs"
   - Example: שִׁיר הַשִּׁירִים (shir ha-shirim) "Song of Songs" = "Best/Greatest Song"

2. **Construct State: Adjective + Noun**
   - Pattern: "Adjective of Noun"
   - Example: "wise of men" = "wisest of men"

3. **Preposition מִן with Definite Article**
   - Pattern: "the X מִן Y"
   - Example: "the good מִן your children" = "the best of your children"

4. **Definite Article on Adjective**
   - Making adjective determinate implies superlative
   - Often with partitive genitive or suffix

**Typological Classification:** Hebrew uses locational comparative (from-type) and periphrastic superlative strategies.

## Specialized Degree Categories

### 5. Intensification

Intensifiers enhance degree without comparison:

#### Types of Intensifiers

**A. Maximizers**
- Absolute endpoint: "completely", "totally", "absolutely"
- Scales with upper bound

**B. Boosters**
- Scalar increase: "very", "extremely", "really"
- Open-ended intensification

**C. Approximators**
- Near endpoint: "almost", "nearly", "practically"
- Approaching maximum

#### Cross-Linguistic Patterns

**Lexical Intensifiers:**
- English: very, extremely, incredibly, absolutely
- Ancient Greek: λίαν, πάνυ, σφόδρα
- Hebrew: מְאֹד (meod) "very"

**Morphological Intensification:**
- Reduplication (many languages)
- Intensive prefixes
- Augmentative affixes

**Semantic Bleaching:**
- Intensifiers grammaticalize from content words
- "Very" < Latin vērus "true"
- Sociolinguistic variation in intensifier use

#### TBTA Intensification Values

- **I (Intensified)**: General intensification ("very")
- **E (Extremely Intensified)**: Maximum intensification ("exceedingly")
- **i (Intensified Comparative)**: Enhanced comparison ("much more")

### 6. Excessive Degree ("Too")

Marks degree beyond acceptable/optimal threshold:

**Characteristics:**
- Indicates over-sufficiency
- Negative implicature
- Often triggers consequence clauses

**Cross-Linguistic Encoding:**
- Dedicated lexical items (English "too", French "trop")
- Verbal constructions ("exceed")
- Contextual inference

**TBTA Code:** T = "too"

### 7. Equative Constructions

Expresses equality of degree between comparee and standard:

#### Structure
- English: "as...as" (Kim is as tall as Pat)
- French: "aussi...que" (aussi grand que)
- German: "so...wie" (so groß wie)

#### Typological Patterns (Haspelmath 2017)

Six equative types identified, based on presence of:
- Equative degree marker (first "as")
- Standard marker (second "as")

**Generalization 1:** No equative construction has degree marker without standard marker.

**Common Type:** Both degree marker and standard marker present (European pattern).

#### Cross-Linguistic Variation
- Parameter marking: Languages vary in whether equative uses parameter marker
- Similative vs. Equative: Different constructions for similarity vs. equality
- Zero-marking: Some languages lack overt equative morphology

**TBTA Code:** q = "Equality" (adjectives only)

### 8. Downward Comparison

Less common than upward comparison but attested widely:

**"Less" (L):**
- Comparative of inferiority
- "X is less tall than Y"
- Romance: French "moins...que", Spanish "menos...que"
- English analytical: "less...than"

**"Least" (l):**
- Superlative of inferiority
- "X is the least tall"
- Parallel to regular superlative

**Cross-Linguistic Pattern:**
- More common in languages with analytic comparison
- Rare in purely synthetic systems
- Often uses separate lexical items rather than affixes

### 9. Superlative Subtypes

#### Relative vs. Absolute Superlative

**Relative Superlative:**
- Compares entity to group
- Requires/implies comparison set
- "She is the most beautiful (of all)"

**Absolute Superlative (Elative):**
- Expresses very high degree
- No comparison set
- "She is extremely/most beautiful"

**Morphological Distinction:**
- **Latin**: Same form, distinguished by context/complements
- **Romance**: Distinct constructions
  - Portuguese: superlativo relativo (mais + article + adjective) vs. superlativo absoluto (muito + adjective OR adjective + -íssimo)
  - Italian: più (relative) vs. molto/-issimo (absolute)
  - Spanish: más (relative) vs. muy/-ísimo (absolute)

**Elative in Non-European Languages:**
- **Arabic**: al-ism al-tafḍīl (single pattern for comparative, superlative, and elative)
- **Tagalog**: napaka- prefix (elative) vs. pinaka- prefix (superlative)

#### Superlative of Two Items

Specialized construction for binary comparison:
- English: "the taller of the two" (not "tallest")
- Uses comparative form with superlative syntax
- Grammaticalized in some languages

**TBTA Code:** s = "Superlative of 2 items" (adjectives only)

### 10. Degree Words and Ordering

Based on WALS Chapter 91 (Dixon):

#### Degree Word Categories

**Separate Words:**
- Meanings: "very", "more", "a little"
- Modify adjectives to indicate property degree

**Affixes:**
- Bound morphology attached to adjectives
- English -er/-est
- Maricopa intensive prefix

#### Cross-Linguistic Ordering Patterns

**DegAdj (Degree word precedes):**
- 227/481 languages
- Dominant in: Europe, Asia, North America
- English: very tall, more beautiful

**AdjDeg (Adjective precedes):**
- 192/481 languages
- Dominant in: Africa, New Guinea, Southeast Asia

**Both Orders:**
- 62/481 languages
- No dominant pattern
- Common in: Austronesian family
- May vary by:
  - Attributive vs. predicative position
  - Specific degree word
  - Register/style

## Language Family Patterns

### Indo-European

**General Characteristics:**
- Proto-IE had synthetic comparison: *-yos-/-ies- (comparative), *-isto- (superlative)
- Modern languages show varying retention

**Germanic:**
- Retains synthetic system broadly
- English: Mixed (synthetic for short, analytic for long)
- German: Primarily synthetic with -er/-st
- Scandinavian: Primarily synthetic

**Romance:**
- Evolved toward analytic strategies
- French: Highly analytic (plus/moins, le plus/le moins)
- Italian: Mixed (più/meno but also -issimo for absolute)
- Spanish: Primarily analytic
- Portuguese: Analytic with synthetic absolute (-íssimo)
- Romanian: Retains most synthesis (mai)

**Slavic:**
- Preserves fusional morphology
- Rich inflectional systems
- Synthetic comparison retained
- Examples: Russian, Polish, Czech all maintain morphological comparison

**Greek:**
- Ancient: Robust synthetic + analytic option
- Modern: Primarily analytic (πιο, ο πιο)

**Celtic:**
- Variable patterns
- Irish: Analytic (níos, is)
- Welsh: Mixed strategies

### Niger-Congo

**Characteristics:**
- World's largest family (1,540 languages)
- Diverse comparison strategies
- Many use exceed comparatives
- Noun class systems interact with degree marking

**Bantu Subfamily:**
- Exceed comparative common
- Locational strategies
- Verb-based comparison

**West Atlantic:**
- Various strategies
- Often analytic

### Austronesian

**Characteristics:**
- 1,256 languages
- High diversity in comparison strategies
- Many degree-neutral languages
- Conjoined comparison common

**Confirmed Patterns:**
- Fijian: Degree-neutral
- Motu: Conjoined comparison only
- Tagalog: Morphological markers (mas-, pinaka-, napaka-)
- Indonesian/Malay: Analytic (lebih, paling)

**Ordering:**
- Both DegAdj and AdjDeg common
- High within-family variation

### Sino-Tibetan

**Characteristics:**
- Highly isolating morphology
- Primarily analytic comparison
- Dedicated degree words

**Chinese:**
- Mandarin: 更 gèng (comparative), 最 zuì (superlative), 很 hěn (very)
- Cantonese: 更 gang3 (more), 最 zeoi3 (most)
- Analytic exclusively

**Tibeto-Burman:**
- Variable patterns
- Many analytic systems
- Some languages lack formal comparison

### Pama-Nyungan (Australian)

**Characteristics:**
- Many conjoined comparison languages
- Several degree-neutral languages confirmed
- Warlpiri: Lacks degree arguments
- Often use positive-negative polarity

### Uralic

**Characteristics:**
- Synthetic comparison in many languages
- Finnish: Comparative -mpi, superlative -in
- Hungarian: Comparative -bb, superlative leg-...-bb
- Estonian: Locational from-comparative

### Afro-Asiatic

**Semitic:**
- **Arabic**: Unique elative system (comparative/superlative/intensive in one form)
- **Hebrew**: Periphrastic only (see Biblical Hebrew section)
- **Aramaic**: Similar to Hebrew patterns

**Berber:**
- Various strategies
- Often analytic

### Isolates and Small Families

**Washo** (Hokan, isolate):
- Degree-neutral confirmed
- Lacks degree morphology entirely

**Basque** (isolate):
- Analytic comparison
- Suffix -ago (comparative), -en (superlative)

## Degree in Semantic Theory

### Degree Semantics vs. Delineation Semantics

**Degree-Based Semantics:**
- Gradable predicates have type ⟨d,⟨e,t⟩⟩
- Explicit degree argument
- Scalar comparison along dimension
- Presumes degree ontology in language

**Delineation-Based Semantics:**
- Gradable predicates have type ⟨e,t⟩
- No degree argument
- Vague boundaries
- Contextual standards

**Parameter Setting:**
- Not correlated with language family
- Crosscuts traditional typology
- Degree-neutral: Motu, Fijian, Washo, Warlpiri
- Degree-based: English, Greek, most Indo-European

### Scale Structure

**Types of Scales:**
- **Open scales**: No maximum/minimum (tall, short)
- **Closed scales**: Upper bound (full, empty)
- **Partially closed**: One bound (wet, dry)

**Interaction with Degree:**
- Modifiers select for scale types
- "Completely" requires closed scale
- "Very" compatible with open scales
- Cross-linguistic variation in scale lexicalization

## Methodology for Annotation

### Identifying Degree in Biblical Texts

#### Step 1: Identify Source Language Form

**Greek:**
1. Check for comparative suffix: -τερος/-τέρᾱ/-τερον, -ῑ́ων/-ῐ́ον
2. Check for superlative suffix: -τατος/-τάτη/-τατον, -ιστος/-ιστη/-ιστον
3. Check for μᾶλλον (comparative analytic)
4. Check for μάλιστα (superlative analytic)
5. Identify intensifiers: λίαν, πάνυ, σφόδρα

**Hebrew:**
1. Check for מִן (min) preposition → comparative
2. Check construct state patterns → potential superlative
3. Check for מְאֹד (meod) → intensifier
4. Check for definite article on adjective in specific contexts → superlative

#### Step 2: Analyze Target Language Translation

**For Adjectives:**
1. Identify base form degree marking
2. Determine construction type:
   - Synthetic morphology (-er, -est, etc.)
   - Analytic construction (more, most, less, least)
   - Intensifier + adjective (very, extremely, too)
   - Equative construction (as...as)
   - Excessive (too)
3. Assess comparative context:
   - Binary comparison → may be "s" (superlative of 2)
   - Group comparison → standard "S" (superlative)
   - Enhanced comparison → may be "i" (intensified comparative)

**For Adverbs:**
1. Same as adjectives but without q, i, s values
2. Use V for intensified (not I)

**For Verbs:**
1. Check for degree adverbials modifying verb
2. Identify modal intensification
3. Note excessive constructions

#### Step 3: Map to TBTA Codes

**Mapping Rules:**

| Linguistic Feature | TBTA Code | Notes |
|-------------------|-----------|-------|
| Base/positive form | N | Default |
| Comparative morphology/syntax | C | "more X than Y" |
| Superlative morphology/syntax | S | "most X of all" |
| Very, really, quite | I | General intensification |
| Extremely, exceedingly, incredibly | E | Extreme intensification |
| Too (+ negative implicature) | T | Excessive |
| Less than | L | Downward comparative |
| Least of | l | Downward superlative |
| As...as construction | q | Adjectives only |
| Much more, far more | i | Adjectives only |
| Comparative of two | s | Adjectives only |

#### Step 4: Context Validation

**Questions to Ask:**
1. Does the source language have this degree marking?
2. Is the target language faithfully rendering source degree?
3. Is this degree marking required by target language grammar?
4. Are there competing interpretations?

**Common Ambiguities:**
- Absolute vs. relative superlative (context-dependent)
- Intensifier vs. excessive (pragmatic)
- Elative vs. superlative (requires complement analysis)

## Sources Consulted

### Primary Linguistic Resources

**WALS (World Atlas of Language Structures):**
- Stassen, Leon. 2013. Comparative Constructions. In: Dryer, Matthew S. & Haspelmath, Martin (eds.) WALS Online (v2020.3) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7385533 (Available online at https://wals.info/chapter/121)
- Dixon, R.M.W. 2013. Order of Degree Word and Adjective. In: Dryer, Matthew S. & Haspelmath, Martin (eds.) WALS Online (v2020.3) [Data set]. https://wals.info/chapter/91

**TBTA Database:**
- AllTheWord. TBTA Database Export. GitHub repository. https://github.com/AllTheWord/tbta_db_export
- README.md documentation of semantic encoding system

### Academic Linguistics

**Degree Semantics:**
- Beck, Sigrid, Svetlana Krasikova, Daniel Fleischer, Remus Gergel, Stefan Hofstetter, Christiane Savelsberg, John Vanderelst, and Elisabeth Villalta. 2009. "Crosslinguistic Variation in Comparison Constructions." Linguistic Variation Yearbook 9: 1–66.
- Bochnak, M. Ryan. 2013. "Cross-linguistic Variation in the Semantics of Comparatives." PhD dissertation, University of Chicago.
- Kennedy, Christopher. 2007. "Vagueness and Grammar: The Semantics of Relative and Absolute Gradable Adjectives." Linguistics and Philosophy 30: 1-45.

**Equative Constructions:**
- Haspelmath, Martin. 2017. "Equative constructions in world-wide perspective." In Treis, Yvonne & Vanhove, Martine (eds.), Similative and equative constructions: A cross-linguistic perspective, 9-32. Amsterdam: Benjamins.
- Haspelmath, Martin and Oda Buchholz. 1998. "Equative and similative constructions in the languages of Europe." In van der Auwera, Johan (ed.), Adverbial constructions in the languages of Europe, 277-334. Berlin: Mouton de Gruyter.

**Indo-European Comparative Morphology:**
- Clackson, James. 2007. Indo-European Linguistics: An Introduction. Cambridge: Cambridge University Press.
- Fortson, Benjamin W. IV. 2010. Indo-European Language and Culture: An Introduction, 2nd ed. Malden, MA: Wiley-Blackwell.

**Cross-Linguistic Typology:**
- Cresswell, Cassandre and Elsi Kaiser. 2024. "Cross-Linguistic Differences in Morphological Processing: Evidence from English and Italian." Reading Research Quarterly. https://doi.org/10.1080/10888438.2024.2413108

### Biblical Language Grammars

**Ancient Greek:**
- Goodell, Thomas Dwight. 1902. "Comparison of Adjectives." In A School Grammar of Attic Greek. Dickinson College Commentaries. https://dcc.dickinson.edu/grammar/goodell/comparison-adjectives
- Smyth, Herbert Weir. 1920. A Greek Grammar for Colleges. Cambridge, MA: Harvard University Press. Perseus Digital Library. http://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.04.0007
- Peek, Corinne. Ancient Greek I: A 21st Century Approach. Open Book Publishers. https://books.openbookpublishers.com/10.11647/obp.0264/ch29.xhtml

**Biblical Hebrew:**
- Gesenius, Wilhelm. Gesenius' Hebrew Grammar, §133: "The Comparison of Adjectives (Periphrastic Expression of the Comparative and Superlative)." Wikisource. https://en.wikisource.org/wiki/Gesenius'_Hebrew_Grammar/133
- Hebrew for Christians. "Comparative Usage in Biblical Hebrew." https://hebrew4christians.com/Grammar/Unit_Five/Comparative_Usage/comparative_usage.html
- unfoldingWord Hebrew Grammar. "Adjective." https://uhg.readthedocs.io/en/latest/adjective.html

### Intensifiers and Degree Modification

**Wikipedia and Reference:**
- "Intensifier." Wikipedia. https://en.wikipedia.org/wiki/Intensifier
- "Degrees of comparison of adjectives and adverbs." Wikipedia. https://en.wikipedia.org/wiki/Comparison_(grammar)

**Academic Papers:**
- Beltrama, Andrea. 2015. "Intensification and sociolinguistic variation: a corpus study." Proceedings of the 41st Annual Meeting of the Berkeley Linguistics Society.
- Bolinger, Dwight. 1972. Degree Words. The Hague: Mouton.

### Language Family Resources

**Indo-European:**
- "Indo-European languages." Wikipedia. https://en.wikipedia.org/wiki/Indo-European_languages
- "Fusional language." Wikipedia. https://en.wikipedia.org/wiki/Fusional_language

**Niger-Congo:**
- "Niger–Congo languages." Wikipedia. https://en.wikipedia.org/wiki/Niger–Congo_languages

**Austronesian:**
- Ethnologue. "Language Families." https://www.ethnologue.com/insights/largest-families/

**General Typology:**
- "World Map of Language Families." https://maps-and-tables.neocities.org/languages_map

## Document Version

Version 1.0 - Created 2025-11-05
Research compiled by Claude (Sonnet 4.5)
Based on TBTA database export and cross-linguistic typological research
