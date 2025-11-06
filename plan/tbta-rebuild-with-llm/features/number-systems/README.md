# Linguistic Number Systems in TBTA Languages

## Executive Summary

This document provides a comprehensive analysis of grammatical number systems beyond the simple singular/plural distinction found in English and biblical source languages (Hebrew, Aramaic, Greek). Our analysis of the ~1000 languages in the TBTA database reveals significant diversity in how languages encode number, with implications for Bible translation accuracy and cultural appropriateness.

## Overview of Number Systems

### Basic Number Categories

1. **Singular** - One entity
2. **Dual** - Exactly two entities
3. **Trial** - Three entities (often minimum of three)
4. **Quadrial** - Four entities (often minimum of four)
5. **Paucal** - A few entities (typically 3-5, but can range up to 15)
6. **Plural** - Many entities

### Greenberg's Number Hierarchy

According to linguist Joseph Greenberg's universal hierarchy:
- No language has a trial without a dual
- No language has a dual without a plural
- Almost all languages with paucal also have dual (with rare exceptions)

## Distribution in TBTA Languages

Based on our analysis of languages.tsv, the following language families show complex number systems:

### Major Language Families with Complex Number Systems

#### 1. Austronesian Languages (176 languages in database)
- **Most complex number systems** found in Papua New Guinea and Indonesia
- Many distinguish dual, trial, and paucal
- Notable languages in our database:
  - **Sursurunga (sgz)**: 5-way distinction (singular/dual/trial/quadrial/plural)
  - **Mussau-Emira (emi)**: Dual, trial, and paucal in pronouns
  - **Manam (mva)**: Trial number in pronouns

#### 2. Trans-New Guinea Languages (141 languages in database)
- Typically distinguish 1st, 2nd, 3rd person with number markers
- Many have dual, some have paucal
- Less commonly have trial

#### 3. Australian Languages (36 languages in database)
- Almost all distinguish at least singular/dual/plural in pronouns
- Notable language in our database:
  - **Murrinh-Patha (mwf)**: Paucal (3-15 individuals) plus plural (>15)
- Languages like Alyawarr (aly), Anmatyerre (amx), and Arrernte (aer) have dual marking

#### 4. Afro-Asiatic Languages (25 languages in database)
- **Arabic varieties**: Mandatory dual in nouns, verbs, adjectives, pronouns
- **Hebrew**: Dual restricted to time periods and body parts
- **Ethiopian Semitic (Amharic, etc.)**: Lost dual, only singular/plural

## Specific Examples from Our Database

### Languages with Confirmed Special Number Systems

| Language Code | Language Name | Family | Number System Features |
|--------------|--------------|--------|------------------------|
| sgz | Sursurunga | Austronesian | 5-way: singular/dual/trial/quadrial/plural |
| emi | Mussau-Emira | Austronesian | Dual/trial/paucal in pronouns |
| mva | Manam | Austronesian | Trial in pronouns |
| mwf | Murrinh-Patha | Australian | Singular/dual/paucal(3-15)/plural(>15) |
| aer | Arrernte, Eastern | Australian | Dual marking in pronouns |
| aly | Alyawarr | Australian | Dual marking expected |
| amx | Anmatyerre | Australian | Dual marking expected |

### Languages Likely to Have Complex Systems (Based on Family)

Given language family patterns, the following groups likely have dual or more complex systems:

**Austronesian (Papua New Guinea/Indonesia):**
- Most of our 176 Austronesian languages from PNG/Indonesia likely have dual
- Many probably have trial or paucal, especially in pronouns

**Australian Languages:**
- All 36 Australian languages likely have at least dual in pronouns
- Some may have trial or paucal

**Sepik Languages (14 in database):**
- Contact with Austronesian languages suggests possible complex systems

## Bible Translation Implications

### Key Translation Challenges

#### 1. Pronoun Precision
When Greek/Hebrew uses "we" or "they," translators must determine:
- Exact number (2, 3, 4, or many?)
- Inclusivity (does "we" include the listener?)
- Cultural context (is this a formal or informal group?)

#### 2. Specific Biblical Examples

**"We apostles" passages:**
- Languages with dual must specify if referring to two apostles
- Trial languages need clarity when three apostles are involved
- Paucal languages distinguish "a few apostles" from "all apostles"

**Trinity references:**
- Trial number languages may have special grammatical forms for exactly three
- This could affect theological expressions

**Body parts and pairs:**
- "Eyes," "hands," "feet" often use dual in languages that retain it
- Hebrew has dual for these, making translation more direct

### Translation Strategies

1. **Context Analysis**: Careful study of biblical context to determine exact numbers
2. **Cultural Sensitivity**: Understanding when precision matters culturally
3. **Consistency**: Maintaining consistent number usage across passages
4. **Footnoting**: Explaining number ambiguities when necessary

## Detection and Prediction Guidelines

### How to Identify Number Systems

#### By Language Family:
1. **Austronesian (Oceanic)**: Expect dual, possibly trial/paucal in pronouns
2. **Trans-New Guinea**: Expect dual, possibly paucal
3. **Australian**: Almost certainly has dual, possibly trial/paucal
4. **Afro-Asiatic**:
   - Arabic varieties: Full dual system
   - Hebrew: Restricted dual
   - Ethiopian: No dual
5. **Niger-Congo**: Generally only singular/plural
6. **Indo-European**: Most have only singular/plural (except some Slavic with dual remnants)
7. **Mayan**: Primarily singular/plural with classifier systems

#### By Geographic Region:
- **Papua New Guinea**: High likelihood of complex systems
- **Indonesia (especially eastern)**: Often have dual/trial/paucal
- **Australia**: Dual very common, paucal possible
- **Pacific Islands**: Dual common, trial/paucal in some areas

### Diagnostic Questions for Field Linguists

1. How do speakers say "we two" vs "we all"?
2. Is there a difference between "we (including you)" and "we (not including you)"?
3. Are there special pronoun forms for groups of 3 or 4?
4. Do number distinctions appear in:
   - Independent pronouns?
   - Verbal affixes?
   - Possessive markers?
   - Demonstratives?

## Academic Citations and Sources

### Primary Sources
- Corbett, Greville G. (2000). *Number*. Cambridge: Cambridge University Press. [Seminal cross-linguistic survey]
- Greenberg, Joseph H. (1963). "Some universals of grammar with particular reference to the order of meaningful elements"
- Lynch, John (1998). *Pacific Languages: An Introduction*. University of Hawaii Press

### Language-Specific Sources
- Hutchisson, Don (1986). "Sursurunga pronouns and the special uses of quadral number"
- Neuhaus, Karl (1930s). *Grammar of the Lihir Language of New Ireland, Papua New Guinea*
- Walsh, Michael (1976). "The Muɹinypata language of North-West Australia"

### Bible Translation Sources
- Hong, Yung-Ja (1994). "The Translation of the Names of God in the South Pacific Languages"
- Various SIL International publications on Bible translation in Oceanic languages

## Implementation Recommendations

### For TBTA Development

1. **Database Schema Enhancement**:
   - Add `number_system` field to language metadata
   - Values: "singular_plural", "has_dual", "has_trial", "has_paucal", "has_quadrial"
   - Allow multiple values (e.g., "has_dual,has_paucal")

2. **Translation Interface Features**:
   - Pronoun disambiguation tool for source texts
   - Number category selector when appropriate
   - Contextual hints for number determination

3. **Training Materials**:
   - Create guides for each number system type
   - Provide biblical examples with number implications
   - Develop decision trees for translators

### Priority Languages for Number System Documentation

Based on our database and linguistic importance:

1. **High Priority** (complex systems, many speakers):
   - Sursurunga (sgz) - quadrial system
   - Mussau-Emira (emi) - trial/paucal
   - Murrinh-Patha (mwf) - extended paucal

2. **Medium Priority** (dual systems, significant populations):
   - All Australian languages in database
   - Austronesian languages from PNG/Indonesia
   - Arabic varieties

3. **Lower Priority** (simpler systems):
   - Niger-Congo languages (mostly singular/plural only)
   - Most Indo-European languages
   - Mayan languages

## Conclusion

The complexity of number systems across the world's languages presents both challenges and opportunities for Bible translation. While English and biblical source languages primarily distinguish only singular and plural, many target languages encode much more precise numerical information grammatically. Understanding these systems is crucial for:

1. **Accuracy**: Ensuring the correct number of participants is conveyed
2. **Naturalness**: Using the target language's number system appropriately
3. **Clarity**: Avoiding ambiguity where the target language demands precision
4. **Theological Precision**: Particularly important for Trinity discussions and apostolic references

The TBTA project should prioritize documenting number systems for all supported languages, particularly those from Austronesian, Trans-New Guinea, and Australian families where complex systems are most common.