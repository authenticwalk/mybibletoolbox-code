<<<<<<< HEAD
# Polarity Feature Research Summary

**Feature**: Polarity (Affirmation vs. Negation)
**Research Date**: 2025-11-26
**Status**: Stage 1 Complete
**Next Stage**: Stage 2 - Corpus Analysis & Translation Database

---

## Executive Summary

Polarity (negation vs. affirmation) is a **universal linguistic feature** but realized through diverse morpho-syntactic strategies. Research reveals polarity is **theologically critical** in specific contexts (divine commands, salvific promises, Christological affirmations) but **stylistically arbitrary** in most narrative contexts (~85%).

**Key Finding**: TBTA's current 3-value system (Affirmative, Negative, Emphatic Affirmative) is **insufficient** for capturing critical distinctions in Biblical source languages (Hebrew לֹא/אַל/אֵין, Greek οὐ/μή/οὐ μή) and target language requirements (negative concord, litotes, prohibition strength).

---

## Research Files

### 1. [TBTA.md](./TBTA.md) - TBTA Documentation Review

**Lines**: 349 | **Sources**: TBTA internal documentation

**Key Findings**:
- **Polarity in TBTA**: Tier A (Nouns, Feature #6), Tier B (Verbs, Feature #29)
- **Values**: Affirmative (A), Negative (N), Emphatic Affirmative (E, verbs only)
- **Encoding**: Position 7 (nouns), Position 4 (verbs) in character-based codes
- **Status**: Marked "Complete" but minimal documentation (no examples, no policy, no edge cases)

**Gaps Identified**:
- No conceptual definition of polarity
- No annotation algorithm documented
- No frequency data (are all 3 values productively used?)
- No justification for why noun polarity is Tier A vs. verb polarity Tier B
- Missing values: Emphatic Negative, Prohibitive, Existential Negative

---

### 2. [LANGUAGES.md](./LANGUAGES.md) - Language Family & Typology Analysis

**Lines**: 550 | **Sources**: WALS, languages.tsv (1,009 translations), 20+ web sources

**Key Findings**:

**Source Languages**:
- **Hebrew**: 3+ particles (לֹא *lo* absolute, אַל *al* prohibitive, אֵין *ein* existential) - **EXPLICITLY ENCODED**
- **Greek**: 2 modal systems (οὐ *ou* indicative, μή *mē* non-indicative) + emphatic οὐ μή - **EXPLICITLY ENCODED**

**Target Language Typology** (WALS global survey):
- **NegV** (preverbal): 525 languages (~40%) - most common
- **VNeg** (postverbal): 171 languages (~13%) - Central Africa, New Guinea
- **[Neg-V]** (prefix): 162 languages (~12%) - East Africa (Bantu)
- **[V-Neg]** (suffix): 202 languages (~15%) - South America
- **Double negation**: 119 languages (~9%) - French *ne...pas*
- **Negative auxiliary**: 47 languages (~4%) - Northern Eurasia (Finnish *ei*)

**Dataset Distribution**:
- 176 Austronesian (17.4%)
- 141 Trans-New Guinea (14.0%)
- 135 Indo-European (13.4%)
- 89 Niger-Congo (8.8%)

**Polarity Marking Status**:
- **MANDATORY**: 90%+ of world languages (Austronesian, Slavic, Romance, Bantu, Uralic, Mayan, etc.)
- **Optional/Contextual**: Rare exceptions (some contexts allow inference)

**Recommended Translation Database** (10 languages):
1. Tagalog (Austronesian particle system)
2. Spanish (Romance negative concord, position-dependent)
3. Russian (Slavic strict negative concord)
4. Swahili (Bantu negative prefix)
5. Finnish (Uralic negative auxiliary)
6. English (Germanic double negation + vernacular NC)
7. Indonesian (Austronesian verbal/nominal distinction)
8. Mandarin (Sino-Tibetan aspect-based negation)
9. K'iche' (Mayan)
10. Tok Pisin (Creole simplified system)

---

### 3. [SCHOLARLY.md](./SCHOLARLY.md) - Scholarly Research

**Lines**: 850 | **Sources**: 30+ scholarly references

**Foundational Typology**:
- **Horn (1989)**: *Natural History of Negation* - pragmatics, negative uninformativeness
- **Dahl (1979, 2010)**: Typology of sentence negation, Jespersen's Cycle
- **Payne (1985)**: "Standard negation" definition (negation of declarative main clauses)
- **Miestamo (2005)**: Symmetric vs. asymmetric negation (297-language sample)
  - Symmetric: Negative = affirmative + marker only
  - Asymmetric: Additional structural changes (25% A/Fin, 33% A/Cat, 13% A/NonReal, 2% A/Emph)

**Diachronic**:
- **Jespersen's Cycle**: Stage I (preverbal) → Stage II (double marking) → Stage III (postverbal)
- Explains Biblical Hebrew/Greek multiple particles as different grammaticalization stages

**Negative Polarity Items (NPIs)**:
- **Ladusaw (1979)**: Fauconnier-Ladusaw hypothesis - NPIs licensed in downward entailing environments
- Refinements: Strawson entailment, nonveridicality (broader licensing contexts)

**WALS Database** (Dryer, Haspelmath):
- Feature 112: Negative morpheme types
- Feature 143: Order of negative morpheme and verb
- Feature 115: Negative indefinite pronouns (negative concord vs. double negation)

**Syntax/Semantics**:
- **Zanuttini (1997)**: Romance negation, 4 syntactic projections for negative markers
- **Givón (1978, 2001)**: Discourse-pragmatic functions (presupposition, norm-reversal)
- **Scope ambiguity**: "Not all X" (partial negation) vs. "All X not" (total negation)

**Biblical Languages**:
- **Hebrew negation**: לֹא + imperfective = permanent prohibition (Ten Commandments)
- **Greek negation**: οὐ μή + aorist subjunctive = most emphatic negation in NT (salvific promises)
- **Litotes**: Rhetorical double negative = emphatic positive (Romans 1:16 "not ashamed" = "proud")

**Translation Theory**:
- **Nida & Taber (1969)**: Dynamic equivalence - replicate meaning/response, not word-for-word
- Greek μὴ γένοιτο (*mē genoito*) → "God forbid!" / "By no means!" (translate force, not literal)

---

### 4. [THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](./THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml) - Theological Analysis

**Lines**: 450+ | **Sources**: Biblical theology + linguistic research

**Theological Significance**: EXISTS (non-arbitrary in specific contexts)

**Non-Arbitrary Contexts** (15% of negated verses estimated):

1. **Divine Commands** (Ten Commandments) - **HIGH STAKES**
   - Exodus 20:13-17: לֹא (*lo*) absolute prohibition
   - Requires: Strongest negation in target language (e.g., Tagalog *huwag* prohibitive)
   - Forbidden: Temporal/mitigated prohibition

2. **Salvific Promises** (Eternal Security) - **HIGH STAKES**
   - John 10:28, Hebrews 13:5: οὐ μή (*ou mē*) emphatic negation "Never, no never"
   - Requires: Emphatic negative or intensive adverb
   - Forbidden: Simple negative (weakens assurance)

3. **Christological Denials** (Orthodoxy vs. Heresy) - **HIGH STAKES**
   - 1 John 2:22, 2 John 7: Denial of Christ = Antichrist
   - Requires: Exact preservation of negative polarity
   - Forbidden: Weakening negation

4. **Ethical Prohibitions** (NT Moral Law) - **MEDIUM-HIGH STAKES**
   - Romans 13:9, Matthew 5:21-48: Reaffirmation of OT law
   - Requires: Prohibitive/imperative form

5. **Divine Attributes** (Immutability, Truthfulness) - **HIGH STAKES**
   - Numbers 23:19, Malachi 3:6: "God does NOT lie/change"
   - Requires: Emphatic negation
   - Forbidden: Qualified negation ("not usually")

6. **Idolatry Prohibitions** (Monotheism) - **HIGH STAKES**
   - Exodus 20:3-5: "No other gods before me"
   - Requires: Absolute prohibition despite cultural discomfort

7. **Litotes** (Rhetorical Double Negatives) - **MEDIUM STAKES**
   - Romans 1:16: "not ashamed" = "proud"
   - Requires: Emphatic positive if target language lacks litotes
   - Avoid: Literal translation losing rhetorical force

**Arbitrary Contexts** (85% of negated verses estimated):
- General narrative statements
- Descriptive negations
- Questions with negative polarity
- Conditional statements
- Temporal/aspectual negations
- Comparative negations
- Existential statements
- Indirect speech negations
- Poetic parallelism (stylistic)

**Translation Principles**:
1. Theological accuracy (non-arbitrary) > Grammaticality > Rhetorical force > Naturalness (arbitrary)
2. Never deviate on divine commands, salvific promises, Christological affirmations, divine attributes
3. Adapt for litotes, negative concord, asymmetric negation structures

---

## Key Discrepancies Between Research Sections

### TBTA vs. Scholarly Research

**TBTA Documentation**:
- 3 values: Affirmative (A), Negative (N), Emphatic Affirmative (E)
- Minimal conceptual definition
- No examples of negative or emphatic affirmative in documentation

**Scholarly Research**:
- Negation requires distinguishing: Simple, Emphatic, Prohibitive, Existential
- Source languages (Hebrew, Greek) have 3+ distinct particles with semantic differences
- Target languages require: Negative concord markers, asymmetric structural changes, NPI licensing

**Gap**: TBTA schema does not capture source language distinctions (לֹא vs. אַל, οὐ vs. μή) or target language requirements (negative concord, litotes, prohibitive vs. general).

### TBTA Tier Classification vs. Linguistic Reality

**TBTA Classification**:
- Noun Polarity: Tier A (Essential) - affects 1000+ languages
- Verb Polarity: Tier B (Important but inferable) - sometimes contextual

**Linguistic Reality**:
- Both noun and verb polarity are **MANDATORY** in 90%+ of languages
- Negative concord affects BOTH nouns (negative indefinites) and verbs (predicate negation)
- Distinction between "essential" and "inferable" not supported by typology

**Possible Explanation**: Tier A/B may reflect *annotation difficulty* rather than linguistic necessity. Verb polarity may be harder to infer from Greek/Hebrew morphology than noun polarity.

---

## Critical Findings for TBTA Implementation

### 1. Insufficient Value Inventory

**Current**: Affirmative (A), Negative (N), Emphatic Affirmative (E)

**Needed**:
- Emphatic Negative (οὐ μή in Greek)
- Prohibitive (Hebrew אַל *al*, Greek μή *mē* + imperative)
- Existential Negative (Hebrew אֵין *ein*)
- Litotes (rhetorical double negative → emphatic positive)
- Negative Concord Marker (flag for clauses with multiple negatives)

### 2. Missing Scope Annotation

**Problem**: "Not all disciples" (partial negation) vs. "All disciples not" (total negation) - different meanings, same words

**Solution**: Annotate which constituent is negated (clause-level, NP-level, VP-level, quantifier scope)

### 3. No Source Language Detail

**Problem**: TBTA collapses Hebrew לֹא/אַל/אֵין into single "Negative" value. Loses critical distinction for languages needing prohibition strength.

**Solution**: Preserve source language particle in metadata field (allows target language to select appropriate equivalent)

### 4. No Target Language Strategy Guidance

**Problem**: Translator sees "Negative" but doesn't know:
- Does target language require negative concord?
- Is this asymmetric negation (structural changes required)?
- Should litotes be preserved or made explicit?

**Solution**: Link polarity annotation to target language typology (provide decision tree based on language family)

---

## Recommendations for Stage 2

### Corpus Analysis Tasks

1. **Value Frequency**: Analyze TBTA database export to determine:
   - How often is Emphatic Affirmative (E) actually used? (Suspected: rare or unused)
   - Noun vs. verb polarity distribution
   - Affirmative vs. negative ratio

2. **Source Language Mapping**:
   - Map all Hebrew לֹא/אַל/אֵין instances to TBTA polarity values
   - Map all Greek οὐ/μή/οὐ μή instances to TBTA polarity values
   - Identify cases where TBTA collapses meaningful distinctions

3. **Cross-Reference Validation**:
   - Parallel Gospel passages: Do they have consistent polarity annotations?
   - OT → NT quotations: Do negations match?

### Translation Database Tasks

1. **Collect Translations** (10 recommended languages from LANGUAGES.md):
   - For 20-30 key verses (Ten Commandments, salvific promises, litotes examples)
   - Document how each language handles emphatic negation, prohibitions, negative concord

2. **Typological Classification**:
   - Classify each language: Symmetric/Asymmetric, Negative Concord/Double Negation, Preverbal/Postverbal/Affix
   - Identify structural consequences of negation (finiteness, mood, aspect changes)

3. **Case Studies**:
   - Deep dive: 2-3 languages with complex negation systems (Finnish, Spanish, Tagalog)
   - Document decision-making process for translating high-stakes verses

---

## Sources Cited

**TBTA Internal Documentation**:
- TBTA-FEATURES.md
- DATA-STRUCTURE.md
- README.md
- CRITIQUE.md

**Typological Databases**:
- WALS Features 112, 143, 115, 144
- Languages.tsv (1,009 Bible translations)

**Scholarly Sources** (30+):
- Horn (1989), Dahl (1979, 2010), Payne (1985), Miestamo (2005)
- Jespersen (1917), Ladusaw (1979), von Fintel (1999)
- Dryer (WALS chapters), Zanuttini (1997), Givón (2001), Mithun (1999)
- Wallace (1996), Nida & Taber (1969)

**Biblical Language Grammars**:
- Hebrew negation (unfoldingWord, HebrewPod101, Blue Letter Bible)
- Greek negation (Blue Letter Bible, multiple NT grammar sources)

---

## Next Steps

**Stage 2**: Corpus Analysis & Translation Database (See STAGE-2-ANALYSIS.md in parent directory for methodology)

**Stage 3**: Algorithm Development & Prediction (Train models to predict polarity based on context, morphology, semantics)

**Stage 4**: Validation & Documentation (Theological review, cross-checking, production-ready documentation)

---

**Document Status**: Stage 1 Research Complete
**Total Research Lines**: 2,199 across 4 files
**Confidence**: HIGH (typological findings), MEDIUM-HIGH (theological analysis - unverified by human scholar)
=======
# Polarity Feature: Research Summary

**Feature Name**: Polarity (Affirmative vs. Negative)
**TBTA Tier**: A (Essential) - Nouns (#6), B (Important) - Verbs (#29)
**Research Completed**: 2025-11-29
**Status**: Stage 1 Complete (Research & Definition)

---

## Quick Overview

**Polarity** distinguishes affirmative (positive) from negative constructions. It is a **linguistic universal**—all languages have mechanisms to negate propositions. TBTA encodes polarity for both nouns and verbs using a 2-way system (Affirmative, Negative) for nouns and a 3-way system (Affirmative, Negative, Emphatic Affirmative) for verbs.

**Theological Significance**: ~15% of polarity contexts are theologically critical (divine commands, promises, Christological exclusivity, soteriological doctrines); ~85% are stylistic/narrative.

---

## Key Values

### TBTA Value Inventory

**Nouns** (2 values):
- **A** (Affirmative): Positive/non-negated entity
- **N** (Negative): Negated entity

**Verbs** (3 values):
- **A** (Affirmative): Positive/non-negated action
- **N** (Negative): Negated action
- **E** (Emphatic Affirmative): Strongly affirmed action

**Missing Value** (identified in research):
- **Emphatic Negative**: Not in TBTA but needed for Greek οὐ μή (double negative = emphatic negation)

---

## Source Language Encoding

### Biblical Hebrew
- ✅ **Explicitly encoded** via negative particles
- **לֹא** (lo): Standard negative (most common)
- **אַל** (al): Prohibitive negative (for commands)
- **Negative concord**: Multiple negatives = single emphatic negation (NOT double positive)
- **Scope-sensitive**: Position determines what is negated

### Biblical Greek
- ✅ **Explicitly encoded** via negative particles
- **οὐ** (ou): Standard negative (indicative mood)
- **μή** (mē): Non-indicative negative (subjunctive, imperative)
- **οὐ μή** (ou mē): **Emphatic negation** (double negative = strongest negation in Greek NT)
- **Mood-sensitive**: Different particles for different moods

**CRITICAL**: Both source languages explicitly mark polarity, making it a **high-priority** feature for translation.

---

## Global Typology (WALS & Grambank)

### Encoding Types (WALS Feature 112A, 1,157 languages)

| Type | Percentage | Examples |
|------|------------|----------|
| **Negative particle** | 43.4% | English *not*, Spanish *no* |
| **Negative affix** | 34.2% | Turkish *-mA*, Swahili *ha-* |
| **Negative auxiliary verb** | 4.1% | Finnish *ei-*, Estonian *ei* |
| **Double negation** | 10.3% | French *ne...pas* |
| **Other/Variation** | 8.0% | Mixed strategies |

**Universal**: 100% of languages have negative morphemes (no language uses only word order/intonation).

### Structural Patterns (Miestamo 2005, 2007)

- **Symmetric negation** (~60%): Negative = Affirmative + negative marker only
- **Asymmetric negation** (~40%): Additional structural changes in negatives
  - Constructional asymmetry: Word order, TAM changes
  - Paradigmatic asymmetry: Tense/aspect neutralization in negatives (e.g., Finnish)

**Implication**: Algorithm must account for target languages where negation triggers structural changes beyond adding a negative marker.

---

## Critical Languages for Translation

### Recommended 10 Languages for Stage 2

| Language | Family | Encoding | Reason |
|----------|--------|----------|--------|
| **English** | Indo-European | Particle | Baseline; no negative concord |
| **Spanish** | Indo-European | Particle + Concord | Double negation (*no...nada*) |
| **French** | Indo-European | Double particle | *ne...pas* circumfix |
| **Swahili** | Niger-Congo | Affix | Negative integrated into TAM |
| **Arabic** | Afro-Asiatic | Particle (multiple) | TAM-sensitive particles |
| **Indonesian** | Austronesian | Particle (multiple) | Verb/noun distinction (*tidak*/*bukan*) |
| **Mandarin** | Sino-Tibetan | Particle (aspect-based) | 不 (general) vs. 没 (perfective) |
| **Finnish** | Uralic | Auxiliary verb | Inflecting negative *ei-* |
| **Turkish** | Turkic | Affix | Negative suffix *-mA* |
| **Tagalog** | Austronesian | Particle | *hindi* (general) vs. *huwag* (prohibitive) |

**Diversity coverage**: 6 families, 4 encoding types, mix of symmetric/asymmetric negation, represents major Bible translation languages.

---

## Theological Significance

### Non-Arbitrary Contexts (~15%)

**CRITICAL** (affects core doctrines):
1. **Ten Commandments** (Exodus 20): Prohibitions define divine law
2. **Christological exclusivity** (John 14:6): "No one comes to Father except through me"
3. **Unforgivable sin** (Matthew 12:31-32): "Will not be forgiven"
4. **Law vs. grace** (Romans 6:14): "Not under law but under grace"

**HIGH** (affects assurance/promise):
5. **Divine promises** (Hebrews 13:5): Emphatic negative (5 negatives) = "will never leave you"
6. **Eternal life** (John 11:25-26): "Will never die" (emphatic negative)
7. **Sin and righteousness** (1 John 1:8): Polarity distinguishes true from false claims

**MEDIUM** (theological inference):
8. **Creation ex nihilo** (Genesis 1:1-2): Implies "nothing pre-existed"

### Arbitrary Contexts (~85%)

- Narrative facts ("He did not go to Jerusalem")
- Descriptions ("There was no water")
- Historical events (polarity follows factual narrative)
- Temporal sequences ("He had not yet arrived")
- Character dialogue (non-divine speakers)

**Key Insight**: Polarity is **stylistic/factual** in most contexts, but **doctrinally critical** in commands, promises, and exclusivity claims.

---

## Translation Challenges

### 1. Emphatic Negation (Greek οὐ μή)

**Problem**: English lacks grammatical emphatic negation; double negatives cancel.
**Greek**: οὐ μή (ou mē) = **strongest** negation in NT (e.g., Hebrews 13:5: 5 negatives)
**English renderings** (all understate emphasis):
- KJV: "I will never leave thee"
- NIV: "Never will I leave you"
- Needed: "I will absolutely not, under any circumstances, ever leave you"

**Solution**: Use lexical intensifiers ("never, ever," "by no means"), adverbial stacking, or footnotes.

### 2. Negative Concord

**Problem**: Hebrew/Greek use negative concord (multiple negatives = emphatic); English does not.
**Hebrew**: לֹא + negative pronoun = emphatic negation (NOT positive)
**English**: "not...nothing" = "something" ❌ (wrong interpretation)
**Solution**: Consolidate to single emphatic negative in English; preserve multiple negatives in concord languages (Spanish, Russian).

### 3. Mood-Specific Negation

**Problem**: Many languages distinguish declarative negative from prohibitive negative.
**Hebrew**: לֹא (lo) = declarative, אַל (al) = prohibitive
**Indonesian**: *tidak* (declarative), *jangan* (prohibitive)
**Solution**: Use target language's prohibitive form for {Mood: Imperative, Polarity: Negative}.

### 4. Part-of-Speech-Specific Negation

**Problem**: Some languages (Austronesian, Sinitic) use different negators for verbs vs. nouns.
**Indonesian**: *tidak* (verbs), *bukan* (nouns), *jangan* (imperatives)
**Mandarin**: 不 *bù* (general), 没 *méi* (perfective)
**Solution**: Check target language for POS-specific or TAM-specific negators.

### 5. Scope Ambiguity

**Problem**: Hebrew לֹא position varies; affects what is negated.
**Example**:
- לֹא כָּל-הָעָם "Not *all* the people" (constituent negation)
- כָּל-הָעָם לֹא "All the people did *not*..." (sentential negation)
**Solution**: Mark scope explicitly in TBTA (proposed enhancement).

---

## Gaps in TBTA Documentation

### Identified Gaps

1. **No Emphatic Negative value**: TBTA has Emphatic Affirmative (E) but NOT Emphatic Negative (critical for Greek οὐ μή)
2. **No scope marking**: TBTA does not distinguish constituent vs. sentential negation
3. **No negative concord flagging**: Multiple negatives not explicitly marked
4. **No frequency statistics**: Unknown distribution of affirmative vs. negative
5. **No OT/NT comparison**: Polarity distribution differences unknown
6. **No edge case documentation**: Double negatives, NPIs, scope interactions not documented

### Recommendations for TBTA Enhancement

1. **Add {Polarity: Emphatic Negative}** for verbs (to capture Greek οὐ μή)
2. **Add {Negation Scope: Sentential | Constituent}** sub-feature
3. **Flag multiple negative elements** in same clause (for negative concord)
4. **Cross-reference Mood + Polarity** for prohibitives (document interaction)

---

## Research Document Details

### 1. TBTA Documentation ([TBTA.md](TBTA.md))

**Lines**: 425
**Key Findings**:
- Polarity encoded at position 7 (nouns) and position 4 (verbs)
- 2-way system (A/N) for nouns, 3-way (A/N/E) for verbs
- JSON export expands character codes to readable fields
- Genesis 1:1 example: Verb "create" marked {Polarity: Affirmative}
- Status: ✅ Complete in TBTA database

**Gaps**:
- No edge case handling documented
- No examples of Emphatic Affirmative usage
- No negative examples in documentation
- No coverage statistics

**See**: [TBTA.md](TBTA.md) for detailed findings

### 2. Language Family & Typology Analysis ([LANGUAGES.md](LANGUAGES.md))

**Lines**: 540
**Languages Analyzed**: 10 in detail, 20+ surveyed
**Databases**: WALS (1,157 languages), Grambank (2,467 languages)

**Key Findings**:
- **Source languages**: Hebrew and Greek both explicitly encode polarity
- **Global distribution**: Particles (43%), affixes (34%), auxiliaries (4%), double negation (10%)
- **Position**: NegV (60%), VNeg (30%), both (10%)
- **Negative concord**: Present in ~30-40% of languages (Romance, Slavic, Hebrew, Greek)

**Root languages for translation**:
- English (baseline)
- Spanish (negative concord)
- French (double negation)
- Arabic, Swahili (major translation languages)
- Indonesian, Mandarin (Asian representatives)
- Finnish, Turkish (unique encoding types)

**See**: [LANGUAGES.md](LANGUAGES.md) for typological details and candidate language selection

### 3. Scholarly Research ([SCHOLARLY.md](SCHOLARLY.md))

**Lines**: 700+
**Sources**: 27 (exceeds minimum of 10)
**Source Types**: Monographs (5), articles (2), theses (1), reference works (5), databases (3), biblical/theological (4), additional scholarly (7)

**Major Frameworks**:
- **Miestamo (2005, 2007)**: Standard negation typology; symmetric vs. asymmetric
- **Dryer (2013)**: WALS Features 112A (negative morphemes), 143 (order)
- **Grambank (2023)**: 17 negation features (GB107, GB137-140, GB298-299)
- **Payne (1985)**: Scope of negation, NPIs, Jespersen's Cycle
- **Comrie (1981)**: Negative universals, markedness
- **Horn (1989)**: Neg-raising, scalar implicatures, metalinguistic negation
- **Giannakidou (2011)**: NPI licensing, downward entailing environments
- **Haspelmath (1997)**: Indefinite pronouns, negative concord variation

**Translation case studies**:
1. Greek emphatic negation (οὐ μή) → English (under-translated)
2. Hebrew negative concord → English (avoid double negative)
3. Indonesian POS-specific negation (verbal vs. nominal)
4. Finnish negative auxiliary and TAM neutralization

**Critical verses analyzed**:
- Exodus 20:1-17 (Ten Commandments): Prohibitions
- Hebrews 13:5 (5 negatives): Emphatic promise
- John 8:12 ("I am the light"): Implicit negation of alternatives
- Matthew 5:17 ("not to abolish"): Scope ambiguity
- John 14:6 ("no one...except"): Exclusive claim

**See**: [SCHOLARLY.md](SCHOLARLY.md) for full bibliography and case studies

### 4. Theological Significance ([THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml))

**Non-Arbitrary Contexts**: 8 groups identified
**Arbitrary Contexts**: 7 patterns identified
**Theological Stakes**: CRITICAL (5), HIGH (2), MEDIUM (1)

**Non-Arbitrary Groups**:
1. Divine commands (Ten Commandments)
2. Divine promises (God's faithfulness)
3. Christological exclusivity (only Savior)
4. Sin and righteousness (moral absolutes)
5. Resurrection and eternal life
6. Creation ex nihilo (nothing pre-existed)
7. Law vs. grace (not under law)
8. Unforgivable sin (blasphemy against Spirit)

**Arbitrary Contexts** (~85%):
- Narrative negations
- Descriptive negations
- Historical events
- Temporal sequences
- Character dialogue (non-divine)

**Key Recommendations**:
1. Add Emphatic Negative value (for Greek οὐ μή)
2. Distinguish prohibitives from declarative negatives
3. Mark negation scope (constituent vs. sentential)
4. Flag negative concord constructions

**See**: [THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml](THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml) for full analysis and translator guidance

---

## Discrepancies Between Sections

### TBTA vs. Scholarly Research

**Discrepancy**: TBTA has "Emphatic Affirmative" but scholarly research reveals Greek has **Emphatic Negative** (οὐ μή), which is MORE COMMON and THEOLOGICALLY SIGNIFICANT than emphatic affirmative.

**Resolution**: Recommend adding {Polarity: Emphatic Negative} to TBTA schema.

### TBTA vs. Typology

**Discrepancy**: TBTA treats polarity as simple 2-way (A/N) or 3-way (A/N/E), but typology reveals:
- Mood-specific negation (prohibitive vs. declarative)
- POS-specific negation (verbal vs. nominal)
- Scope variation (constituent vs. sentential)

**Resolution**: Document interaction with Mood and Part of Speech; consider adding Scope sub-feature.

### Theological vs. Linguistic

**Discrepancy**: Theological analysis identifies ~15% of contexts as non-arbitrary (doctrinally significant), but linguistic analysis treats polarity as universal/obligatory (100% of clauses marked).

**Resolution**: These are compatible. Polarity is linguistically obligatory (all clauses have polarity), but theologically significant only in specific contexts (commands, promises, exclusivity claims).

---

## Next Steps (Stage 2: Analysis)

### Required Tasks

1. **Generate test set** (100+ verses per value minimum)
   - Balanced sampling: OT/NT, genres, typical + adversarial cases
   - Include emphatic negation examples (Greek οὐ μή)
   - Include prohibitives (Hebrew אַל, Greek μή)
   - Include negative concord examples

2. **Collect translation data** for 10 selected languages
   - English, Spanish, French, Swahili, Arabic, Indonesian, Mandarin, Finnish, Turkish, Tagalog
   - Analyze how each language handles:
     - Standard negation
     - Emphatic negation
     - Prohibitives
     - Negative concord
     - Scope ambiguity

3. **Analyze patterns** from translations
   - Calculate frequency: affirmative vs. negative (~90% affirmative expected)
   - Identify asymmetric negation patterns
   - Discover mood-polarity interactions
   - Test negative concord predictions

4. **Develop prediction algorithm**
   - Use WALS/Grambank features to predict target language behavior
   - Account for emphatic negation, prohibitives, scope
   - Handle negative concord vs. non-concord languages
   - Cross-reference Mood, Part of Speech, TAM features

### Key Questions for Stage 2

1. What is the frequency of affirmative vs. negative in biblical text?
2. How frequent is emphatic negation (οὐ μή) in Greek NT?
3. Do OT and NT differ in polarity distribution?
4. Which moods are most frequently negated (imperative vs. indicative)?
5. Are there genre differences (narrative vs. law vs. prophecy vs. poetry)?
6. How do translation languages handle Greek emphatic negation?
7. What percentage of negatives are prohibitives vs. declaratives?

---

## Summary: Polarity in One Paragraph

Polarity (affirmative vs. negative) is a linguistic universal—all 1,157+ surveyed languages have negative morphemes. TBTA encodes polarity for nouns (2-way: A/N) and verbs (3-way: A/N/E), with explicit marking in Hebrew (לֹא, אַל) and Greek (οὐ, μή, οὐ μή). Global typology shows 43% of languages use particles, 34% affixes, 10% double negation, and 4% auxiliary verbs. Theologically, polarity is critical in ~15% of contexts (divine commands, promises, Christological exclusivity, soteriological doctrines) and stylistic in ~85% (narrative, description). Key translation challenges: (1) Greek emphatic negation (οὐ μή) under-translated in English, (2) Hebrew/Greek negative concord misunderstood as double positive, (3) mood-specific and POS-specific negators vary cross-linguistically, (4) scope ambiguity requires careful analysis. TBTA enhancement needed: add Emphatic Negative value, mark scope, flag negative concord, document Mood-Polarity interaction.

---

**Research Completed**: 2025-11-29
**Total Research Lines**: ~2,200+ lines across 4 documents
**Languages Analyzed**: 10 in detail, 1,157 (WALS) + 2,467 (Grambank) surveyed
**Scholarly Sources**: 27 (exceeds minimum 10)
**Theological Contexts**: 8 non-arbitrary groups + 7 arbitrary patterns
**Stage**: 1 of 6 (Research & Definition) ✅ COMPLETE

**Next Stage**: Stage 2 - Generate Test Set with Translation Data
>>>>>>> origin/feat/self-learning-tbta
