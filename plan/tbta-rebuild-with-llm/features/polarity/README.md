# TBTA Feature: Polarity

## Overview

Polarity is a linguistic feature that encodes whether a constituent's existence, presence, or assertion is affirmed (positive polarity) or negated (negative polarity). In The Bible Translator's Assistant (TBTA), this feature is crucial for accurate translation into languages that have complex polarity systems, including negative concord languages, languages with negative polarity items (NPIs), and languages with special grammatical forms for negated constituents.

## Linguistic Definition

### What is Polarity?

Polarity in linguistics refers to the distinction between affirmative (positive) and negative expressions. It encompasses:

1. **Sentential Polarity**: Whether an entire sentence is affirmative or negative
2. **Constituent Polarity**: Whether specific elements (especially nouns) are affirmed or negated
3. **Polarity Sensitivity**: How certain lexical items (polarity items) are restricted to particular polarity contexts

### Key Concepts

#### Negative Polarity Items (NPIs)
NPIs are expressions that typically only appear in negative contexts. They are not inherently negative but require licensing by negation or similar environments (Giannakidou & Zwarts, 1999).

Examples in English:
- "at all" (*I didn't like it at all* vs. **I liked it at all*)
- "any" in certain uses (*I don't have any money* vs. **I have any money*)
- "ever" (*Nobody ever told me* vs. **Somebody ever told me*)

#### Negative Concord
In negative concord (NC) languages, multiple negative elements combine to express a single semantic negation rather than canceling each other out (Dalmi, 2022).

#### Double Negation
In non-NC languages like Standard English, two negatives typically yield a positive meaning: "I didn't see nothing" = "I saw something"

## TBTA Encoding

### Values

TBTA uses a simple binary distinction for the Polarity feature:

```yaml
Polarity: Affirmative  # Normal positive assertion (default)
Polarity: Negative     # Negated existence/presence
```

### Application Context

In TBTA, Polarity is primarily encoded at the **noun level** rather than verb level. This captures whether the noun's existence or presence is negated.

### Example from TBTA Data

```yaml
# From GEN 19:31 - "there is not a man in the earth"
- Constituent: man
  Number: Plural
  Polarity: Negative  # "no men"
  Participant Tracking: First Mention
```

## Quick Translator Test

**Use this checklist to determine if your target language requires detailed polarity annotation:**

### Negation Strategy

1. ☐ **Does your language use negative particles or affixes for negation?**
   - Negative particle (English "not", French "ne...pas", Japanese "nai")
   - Negative affix (Turkish -ma/-me, Finnish negative auxiliary "ei")
   - Negative verb forms (suppletive negation)
   - Tonal negation (some African languages)

2. ☐ **Where does negation appear in the clause?**
   - Preverbal particle (Mayan languages, many African languages)
   - Postverbal particle or suffix (Turkish, Japanese)
   - Auxiliary verb (Finnish "ei", some Austronesian)
   - Multiple positions possible (French "ne...pas" discontinuous)

### Negative Concord

3. ☐ **Does your language allow or require negative concord?**
   - **Strict NC**: Multiple negatives required (Russian, Spanish, Greek, Turkish)
     - "I nothing not saw" = "I didn't see anything"
   - **Optional NC**: Varies by context or register (some Romance)
   - **No NC (Double Negation)**: Two negatives = positive (Standard English, German)
     - "I didn't see nothing" = "I saw something"

4. ☐ **If you have negative concord, is it strict or optional?**
   - Strict: Always required with negative indefinites
   - Optional: Depends on emphasis, formality, or context
   - Note: Most NC languages have strict NC

### Negative Polarity Items (NPIs)

5. ☐ **Does your language have negative polarity items (any, ever, at all)?**
   - Yes, special items required in negative contexts (English "any", Japanese も-series)
   - No dedicated NPIs (negation expressed through standard forms)
   - Universal quantifiers used (some languages use "all" in negative contexts)

6. ☐ **Can your NPIs appear in non-negative contexts?**
   - Restricted: Only with negation or negative-like contexts (questions, conditionals)
   - Some flexibility: Can appear with certain verbs or in specific constructions
   - Note: True NPIs are licensed environments, not inherently negative

### Scope & Case Marking

7. ☐ **Can negation scope over the entire sentence vs. just one element?**
   - Sentential negation: Negates whole proposition ("It is not the case that...")
   - Constituent negation: Negates specific element ("Not the man, but the woman")
   - Both possible, distinguished by syntax/prosody
   - Language-specific restrictions

8. ☐ **Does negation affect case marking or grammatical form?**
   - **Genitive of negation**: Objects take genitive case under negation (Russian, Finnish)
   - **Partitive case**: Required with negated objects (Finnish)
   - **No case change**: Negation doesn't affect case (English, Mandarin)
   - **Special negative forms**: Different verb or noun forms in negative contexts

### Existential & Quantificational Negation

9. ☐ **Does your language have special negative existential constructions?**
   - Dedicated negative existential word (Hebrew אֵין ein, Russian нет net, Turkish yok)
   - Negated copula or existential verb (English "there isn't")
   - Same as verbal negation (no special form)

10. ☐ **How does your language express "no one," "nothing," "never"?**
   - Negative indefinites: Single negative word (English "nobody", German "niemand")
   - NPI + negation: Requires negative verb (Japanese "dare-mo...nai" = "no one")
   - Multiple negation: NC language requires negative verb + negative pronoun (Russian, Spanish)

### Critical Indicators

**If your language has STRICT NEGATIVE CONCORD (question 3), you MUST use multiple negative forms. Annotating only the verb or only the noun will produce ungrammatical output.**

**If your language has GENITIVE OF NEGATION or case changes (question 8), polarity annotation affects not just the negative marker but also noun case/form.**

**If your language has SPECIAL NEGATIVE EXISTENTIALS (question 9), existential negation requires different vocabulary, not just adding "not."**

**If your language uses NPIs (question 5), you must select appropriate polarity-sensitive items (like "any" instead of "some") in negative contexts.**

### Language Family Patterns

**Negative Concord Languages** (multiple negatives required):
- **Slavic**: Russian, Polish, Czech, Bulgarian (strict NC)
- **Romance**: Spanish, Italian, Portuguese, Romanian (strict NC); French (optional NC)
- **Greek**: Ancient and Modern Greek (strict NC)
- **Turkic**: Turkish, Azerbaijani, Uzbek (strict NC)
- **Uralic**: Finnish, Hungarian (strict NC with special negative auxiliary)
- Strategy: Annotate all constituents in scope of negation as Negative

**Non-NC Languages** (double negation = affirmative):
- **Germanic**: Standard English, German, Dutch, Swedish
- **Sino-Tibetan**: Mandarin Chinese, Cantonese
- Strategy: Annotate only the negated element, avoid multiple negatives

**NPI Languages** (require polarity items):
- **Japanese**: Uses も (mo) series NPIs with negative verbs
- **Korean**: Similar to Japanese with NPI system
- **English**: "any," "ever," "at all" required in negative contexts
- Strategy: Select NPIs for negative contexts, standard forms for affirmative

**Genitive/Partitive of Negation**:
- **Russian**: Direct objects become genitive under negation
- **Finnish**: Partitive case required for negated objects
- **Estonian**: Similar to Finnish
- Strategy: Polarity affects case marking, not just negative particle

**Special Negative Existentials**:
- **Hebrew**: אֵין (ein) "there is not" (distinct from לֹא lo "not")
- **Russian**: нет (net) "there is not" (distinct from не ne "not")
- **Turkish**: yok "there is not" (distinct from negative suffix)
- **Arabic**: ليس (laysa) negative copula, ما (ma) standard negation
- Strategy: Use dedicated negative existential forms for "there is not" constructions

**Tone/Suprasegmental Negation** (rare):
- Some **African languages**: Negation marked by tone change
- **Mayan languages**: Often preverbal negative particles
- Strategy: Ensure negation marking aligns with tonal/prosodic requirements

## Language-Specific Polarity Systems

### 1. Negative Concord Languages

#### Russian (Slavic Family)
Russian exhibits **strict negative concord** where multiple negative elements affirm each other:

```
Я ничего не знаю
Ya nichevo nye znayu
I nothing NEG know
"I don't know anything" (lit. "I nothing not know")
```

Key features:
- Requires negative verb with negative indefinites
- All indefinites in scope of negation must be negative
- Genitive case often used with negated existence

#### Turkish (Turkic Family)
Turkish also shows strict NC properties:

```
Hiçbir şeyim yok
Not-one thing-of-mine exists-not
"I don't have anything"
```

Features:
- Negative verb forms required with negative pronouns/adverbs
- Special negative existential constructions
- Morphological negation on verbs

#### Finnish (Uralic Family)
Finnish has a unique negation system using the auxiliary 'ei':

```
En tiedä mitään
NEG.1SG know anything.PARTITIVE
"I don't know anything"
```

Features:
- Negative auxiliary verb 'ei' conjugates for person
- Partitive case with negation
- Special suffixes (-kaan/-kään) for negative contexts

### 2. Languages with NPIs (Non-NC)

#### Japanese
Japanese uses NPIs in negative contexts without negative concord:

```
何も見なかった
nani-mo mi-nakatta
what-EVEN see-NEG.PAST
"didn't see anything"
```

The particle も (mo) creates NPIs that require negation.

### 3. Languages with Special Negated Forms

Some languages have distinct lexical items or morphological forms for negated nouns:

#### Tagalog (Austronesian)
Uses "wala" (none/no) vs. "may/mayroon" (there is):

```
Walang tao dito
No person here
"There's nobody here"
```

## Bible Translation Challenges

### 1. Existential Statements

Biblical Hebrew and Greek existential negations often require careful handling:

**Genesis 19:31** - "there is not a man in the earth"
- Hebrew: אֵין אִישׁ (ein ish) - uses special negative existential
- Russian: нет мужчины (net muzhchiny) - genitive with negation
- Turkish: yeryüzünde erkek yok - negative existential 'yok'
- English: "there is no man" or "there isn't a man"

### 2. Universal Negative Quantification

Passages with "no one," "nothing," "never" require language-specific strategies:

**Matthew 5:18** - "not one jot or tittle shall pass"
- NC languages: Multiple negatives required
- NPI languages: Appropriate polarity items needed

### 3. Rhetorical Negative Questions

**Romans 8:31** - "If God is for us, who can be against us?"
- Some languages require special markers for rhetorical negatives
- Polarity affects expected answer interpretation

### 4. Prophetic Negations

**Isaiah 9:7** - "Of the increase...there shall be no end"
- Eternal/absolute negations may use special forms
- Some languages distinguish temporary vs. permanent negation

## Cross-Linguistic Variation

### Languages from TBTA Database Requiring Polarity Attention

Based on the languages.tsv file, several language families in TBTA require careful polarity handling:

#### Austronesian Languages
Many Philippine and Indonesian languages (e.g., Tagalog, Inabaknon, Alune) have:
- Complex systems of existential negation
- Distinct negative and affirmative markers
- Interaction with focus/topic systems

#### Trans-New Guinea Languages
Languages like Ankave, Amele, and Angaataha may have:
- Clause-chaining with polarity dependencies
- Switch-reference interacting with negation
- Special negative verb forms

#### Australian Aboriginal Languages
Languages like Arrernte and Alyawarr often feature:
- Negative particles with specific scope
- Interaction with ergative-absolutive alignment
- Complex negation in subordinate clauses

#### Mayan Languages
Achi and Awakateko show:
- Preverbal negative particles
- Interaction with aspect markers
- Special forms for negative imperatives

## Edge Cases and Challenges

### 1. Scope Ambiguity
"All the disciples didn't flee" could mean:
- None of the disciples fled (wide scope negation)
- Not all disciples fled (narrow scope negation)

Different languages resolve this differently, requiring translator decisions.

### 2. Negative Raising
"I don't think he came" vs. "I think he didn't come"
- Some languages distinguish these
- Others treat them identically

### 3. Metalinguistic Negation
"He didn't see three men, he saw four"
- Corrective negation may use different strategies
- Some languages have special corrective particles

### 4. Expletive Negation
Some languages use "pleonastic" negation that doesn't contribute semantic negativity:
- French: "Je crains qu'il ne vienne" (I fear he might come)
- The "ne" doesn't mean "not" here

## Implementation Guidelines

### For Tool Developers

1. **Detection Strategy**
   - Look for negative particles (not, no, never, none)
   - Check for negative affixes (un-, non-, -less)
   - Identify negative existentials
   - Track scope of negation

2. **Encoding Recommendations**
   ```yaml
   # Explicit negative noun
   - Constituent: man
     Polarity: Negative
     Surface Realization: Noun

   # Implicit negative (from context)
   - Constituent: hope
     Polarity: Negative
     Implicit Information: Implicit Situational Information
   ```

3. **Validation Checks**
   - Ensure polarity consistency within scope
   - Flag potential scope ambiguities
   - Check for double negative interpretations
   - Validate against target language requirements

### For Bible Translators

1. **Assessment Questions**
   - Does the target language have negative concord?
   - Are there special negative existential constructions?
   - Do negative contexts require special case marking?
   - Are there distinct NPIs that must be used?

2. **Translation Strategies**
   - Map source polarity to target system
   - Resolve scope ambiguities based on context
   - Choose appropriate NPIs or negative forms
   - Maintain rhetorical force of negative questions

## Academic References

- Baker, C. L. (1970). "Double Negatives." *Linguistic Inquiry*, 1(2), 169-186.
- Dalmi, G. (2022). *Strict Negative Concord in Slavic and Finno-Ugric: Licensing, Structure and Interpretation*. De Gruyter.
- Giannakidou, A. (1998). *Polarity Sensitivity as (Non)veridical Dependency*. John Benjamins.
- Giannakidou, A., & Zwarts, F. (1999). "Temporal, aspectual structure and polarity." *The Handbook of Contemporary Syntactic Theory*, 232-250.
- Horn, L. R. (1989). *A Natural History of Negation*. University of Chicago Press.
- Ladusaw, W. A. (1979). *Polarity Sensitivity as Inherent Scope Relations*. PhD dissertation, University of Texas.
- Linebarger, M. (1987). "Negative polarity and grammatical representation." *Linguistics and Philosophy*, 10, 325-387.
- Penka, D. (2011). *Negative Indefinites*. Oxford University Press.
- Zeijlstra, H. (2004). *Sentential Negation and Negative Concord*. PhD dissertation, University of Amsterdam.

## Summary

Polarity is a critical feature for Bible translation because:

1. **Structural Requirements**: Many languages have obligatory grammatical requirements for negative contexts
2. **Lexical Selection**: NPIs and negative forms must be chosen correctly
3. **Scope Resolution**: Ambiguous negation scope must be resolved
4. **Pragmatic Force**: Rhetorical negatives must maintain their intended effect
5. **Theological Accuracy**: Existential and absolute negations must be precise

TBTA's encoding of Polarity as a binary feature on nouns provides essential information for navigating these complexities, ensuring accurate and natural translation across the world's diverse polarity systems.