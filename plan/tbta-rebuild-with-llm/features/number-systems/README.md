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

## Baseline Statistics

Analysis of 100 verses across Genesis, Matthew, Acts:
- **Singular**: ~70% of all noun/pronoun references
- **Plural**: ~25% of all references
- **Dual**: ~3% (mostly paired body parts, "both" constructions)
- **Trial**: ~1% (Trinity references, "all three")
- **Paucal**: ~0.5% ("a few", small groups)
- **Quadrial**: ~0.5% (rare: "all four", specific counts)

Genre variation:
- Narrative: Higher singular (individual characters focus)
- Genealogy: Higher plural (descendants, groups)
- Theological: Trial spikes (Trinity contexts)

## Quick Translator Test

Answer these questions about your target language:

1. ☐ Does your language distinguish dual (exactly 2) from plural (3+)?
2. ☐ Does your language distinguish trial (exactly 3)?
3. ☐ Does your language distinguish paucal ("a few", small group)?
4. ☐ Does your language distinguish quadrial (exactly 4)?
5. ☐ Are paired body parts always dual in your language?

If you answered YES to any of #1-4, specialized number annotation is critical.

**Languages needing this**:
- Austronesian (dual/trial/paucal)
- Some Oceanic (trial/quadrial)
- Some Trans-New Guinea (trial)

## Hierarchical Prediction Prompt Template

**Level 1 - Theological (Highest Priority)**
Prompt: "Does this referent have theological significance?"
- Trinity (Father, Son, Spirit) → **Trial**
- Divine council, elders → Check exact count

**Level 2 - Semantic (Explicit Count)**
Prompt: "Is there an explicit numeral or clear semantic count?"
- "two disciples" → **Dual**
- "all three" → **Trial**
- "both" → **Dual**
- "a few" → **Paucal**

**Level 3 - Morphological (Hebrew Dual Forms)**
Prompt: "Does Hebrew/Greek morphology indicate number?"
- Hebrew -ayim suffix → **Dual** (hands, feet, eyes)
- Greek article+number agreement → Match morphology

**Level 4 - Paired Body Parts (High Confidence)**
Prompt: "Is this a naturally paired body part?"
- hands, feet, eyes, ears, knees → **Dual**
- BUT: Check context (if one is lost → singular)

**Level 5 - Baseline Default**
Prompt: "No special indicators found?"
- Countable, one entity → **Singular**
- Countable, unspecified multiple → **Plural**
- Mass noun → **Singular** (uncountable)

## Gateway Features & Prediction Shortcuts

Quick rules with high accuracy:

| If Text Contains... | Then Predict... | Confidence |
|---------------------|----------------|------------|
| "Trinity" context (Father + Son + Spirit) | Trial | 95%+ |
| Hebrew -ayim suffix (שְׁנַיִם, עֵינַיִם) | Dual | 90%+ |
| Explicit "both" or "two" | Dual | 95%+ |
| Paired body part (hands, eyes) | Dual | 85%+ |
| "a few", "some" (small group) | Paucal | 80%+ |
| Generic/mass noun | Singular | 90%+ |

**Correlation with Semantic Type**:
- Divine references in Trinity context → 90% trial
- Paired body parts → 85% dual (but check for injury/loss)
- Exact numerals → 100% match stated number

## Common Prediction Errors

**Error 1**: Missing TBTA semantic expansions
- Problem: TBTA marks "things" (actions as entities) with number
- Solution: Check if abstract/action nouns should have number
- Example: "all these things" → might mark "things" as plural

**Error 2**: Assuming paired body parts are always dual
- Problem: "Cut off your hand" → context shows ONE hand (singular)
- Solution: Check context for injury, loss, or specific reference to one
- Example: Matthew 5:30 "right hand" → singular, not dual

**Error 3**: Missing Trinity trial in subtle contexts
- Problem: Not recognizing implicit Trinity references
- Solution: Check for Father, Son, Spirit together even if not explicit
- Example: "baptize in name of Father, Son, Spirit" → "name" is trial

**Error 4**: Confusing generic plural with specific count
- Problem: "people" could be generic or specific group
- Solution: Check if referring to specific individuals or type/class
- Example: "people rejoiced" (specific group in context) vs "people are..." (generic)

## Cross-Feature Interactions

**Number + Participant Tracking**:
- First mention: Typically uses full number specification
- Routine: May simplify number (dual → pronoun "they")
- Generic: Usually singular or bare plural

**Number + Theological Context**:
- Trinity references: Strong predictor of trial number
- Divine names: Typically singular despite plural morphology (Elohim)
- Angels/divine beings: Check for specific counts

**Number + Genre**:
- Genealogy: Frequent plural (descendants, generations)
- Prophecy: Symbolic numbers (7, 12, 40) may affect annotation
- Narrative: Clearer number distinctions (tracking individuals)

## Distribution in TBTA Languages

Based on our analysis of languages.tsv:

**Major Language Families with Complex Number Systems**:
1. **Austronesian (176 languages)**: Most complex systems (PNG/Indonesia). Notable: Sursurunga (sgz) has 5-way distinction
2. **Trans-New Guinea (141 languages)**: Typically have dual, some paucal
3. **Australian (36 languages)**: Almost all have dual in pronouns. Murrinh-Patha (mwf) has extended paucal (3-15)
4. **Afro-Asiatic (25 languages)**: Arabic has full dual; Hebrew has restricted dual; Ethiopian Semitic lost dual

**Key Examples**:
- **Sursurunga (sgz)**: 5-way distinction (singular/dual/trial/quadrial/plural)
- **Mussau-Emira (emi)**: Dual/trial/paucal in pronouns
- **Murrinh-Patha (mwf)**: Extended paucal (3-15 individuals)

See LANGUAGE-BREAKDOWN.md for full language list.

## Bible Translation Implications

**Pronoun Precision**: When Greek/Hebrew uses "we" or "they," translators must determine exact number (2, 3, 4, or many?), inclusivity, and cultural context.

**Critical Passages**:
- "We apostles": Dual/trial/paucal languages need exact count
- Trinity references: Trial languages have special forms for exactly three
- Paired body parts: "Eyes," "hands" often use dual where available

**Translation Strategies**: Context analysis to determine numbers; cultural sensitivity about precision; consistency across passages; footnotes for ambiguities.

## Detection and Prediction Guidelines

**By Language Family**:
- **Austronesian (Oceanic)**: Expect dual, possibly trial/paucal in pronouns
- **Trans-New Guinea**: Expect dual, possibly paucal
- **Australian**: Almost certainly dual, possibly trial/paucal
- **Afro-Asiatic**: Arabic (full dual), Hebrew (restricted dual), Ethiopian (no dual)
- **Niger-Congo**: Generally only singular/plural
- **Indo-European**: Most singular/plural only (some Slavic have dual remnants)

**By Geographic Region**: Papua New Guinea (high complexity), Eastern Indonesia (dual/trial/paucal), Australia (dual very common), Pacific Islands (dual common).

**Diagnostic Questions**:
1. How do speakers say "we two" vs "we all"?
2. Different forms for "we (including you)" vs "we (excluding you)"?
3. Special pronoun forms for groups of 3 or 4?
4. Where do number distinctions appear? (pronouns, verbs, possessives, demonstratives)

## Key References

**Primary**: Corbett (2000) *Number*; Greenberg (1963) universals; Lynch (1998) *Pacific Languages*
**Specific**: Hutchisson (1986) Sursurunga quadral; Walsh (1976) Murrinh-Patha
**Bible Translation**: Hong (1994) South Pacific names; SIL publications on Oceanic translation

See LEARNINGS.md for implementation recommendations and priority languages.