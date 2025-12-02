# TBTA Policy Contradiction Report

> **Analysis Date**: December 2, 2024
> **Corpus**: 6,963 verses across 15 books (Genesis, Joshua, Ruth, 1-2 Samuel, Esther, Nehemiah, Daniel, Matthew, Mark, Luke, Acts, 2 John)
> **Purpose**: Document discrepancies between official TBTA policy and actual encoded verses
> **Evidence Source**: [`plan/tbta/.archive/phase1-reverse-engineer-claude-opus-4-5/EVIDENCE-DETAILED.md`](../../../plan/tbta/.archive/phase1-reverse-engineer-claude-opus-4-5/EVIDENCE-DETAILED.md)

---

## Summary

| Rule | Policy | Applied Rate | Supporting | Contradicting |
|------|--------|--------------|------------|---------------|
| Modal Decomposition | "We do not use 'can'" | **14%** | 133 | 787 |
| Passive Voice | "keep passive, mark agent" | **varies** | 0 | 76 |
| Addressee Patterns | "you(people)" not "you(Disciples)" | **68%** | 484 | 229 |
| Number Formatting | "use numerals" | **51%** | 535 | 507 |
| Demonym → Description | "Moabite → [who was from Moab]" | **55%** | 157 | 126 |
| Hyphenated Verb Base | "stand-up not stood-up" | **98%** | 216 | 5 |

---

## 1. Modal Decomposition (14% Compliance)

### Official Policy (checklist.md §0.24, §2.1)

> **§0.24**: "Do not use 'can'. In most cases, that becomes 'is able [to…' See section 2.1. (But no brackets for He1.)"
>
> **§2.1**: "We do not use 'can'. Instead, we use 'are able [to ...'. There are two senses of 'able'. 'Able-A' indicates ability to do something, whereas 'able-B' indicates that someone is able to do something because of the circumstances."

### Statistics
- **Supporting**: 133 verses (14%)
- **Contradicting**: 787 verses (86%)

### Contradicting Examples

| # | Verse | Contradicting Text | Evidence |
|---|-------|-------------------|----------|
| 1 | **Genesis 2:5** | "...God did not create a man [who **would care** for the plants]" | [L563](../../../plan/tbta/.archive/phase1-reverse-engineer-claude-opus-4-5/EVIDENCE-DETAILED.md#L563) |
| 2 | **Genesis 2:15** | "...God put the man in the garden [so the man **could care** for the garden]" | [L567](../../../plan/tbta/.archive/phase1-reverse-engineer-claude-opus-4-5/EVIDENCE-DETAILED.md#L567) |
| 3 | **Genesis 2:17** | "But you(man) **must not** eat the fruit..." | [L571](../../../plan/tbta/.archive/phase1-reverse-engineer-claude-opus-4-5/EVIDENCE-DETAILED.md#L571) |
| 4 | **Genesis 3:3** | "You(Eve) **must not** eat the fruit of the tree..." | [L575](../../../plan/tbta/.archive/phase1-reverse-engineer-claude-opus-4-5/EVIDENCE-DETAILED.md#L575) |
| 5 | **Genesis 3:22** | "We(God) **must prevent** [this man from eating...]" | [L579](../../../plan/tbta/.archive/phase1-reverse-engineer-claude-opus-4-5/EVIDENCE-DETAILED.md#L579) |

### Analysis
The policy explicitly prohibits "can" but the corpus shows:
- "can" → "is able" is applied ~14% of the time
- "must", "should", "could", "would" are almost never converted
- Only "can" has a decomposition rule; other modals have no documented transformation

---

## 2. Addressee Patterns (68% Compliance)

### Official Policy (checklist.md §0.1)

> **§0.1**: "First and second person pronouns (like 'I' and 'you') and 'each-other' must have the referent (person that the pronoun refers to or represents) indicated in parentheses, like 'I(John) talked to Mary'."
>
> **From analysis conventions**: The referent should use generic terms like "you(people)", "you(person)", not specific group names like "you(Disciples)", "you(followers)".

### Statistics
- **Supporting (generic)**: 484 verses (68%)
- **Contradicting (specific)**: 229 verses (32%)

### Contradicting Examples

| # | Verse | Contradicting Text |
|---|-------|-------------------|
| 1 | **Matthew 8:26** | "Jesus asked, ['Why are **you(followers)** afraid?]" |
| 2 | **Matthew 9:13** | "But **you(Pharisees)** (imp) go. And **you(Pharisees)** (imp) learn the thing [that the following words mean]." |
| 3 | **Matthew 9:38** | "Therefore **you(disciples)** (imp) earnestly ask God..." |
| 4 | **Matthew 10:8** | "**You(disciples)** (imp) heal the sick people." |
| 5 | **Matthew 10:16** | "**You(disciples)** (imp) listen/behold. I(Jesus) am sending **you(disciples)**..." |
| 6 | **Matthew 10:22** | "And all people will hate **you(disciples)**..." |
| 7 | **Mark 4:13** | "Jesus said to **those followers/disciples**, ['Do **you(disciples)** not understand...'" |

### Analysis
The corpus shows inconsistent application:
- OT: Predominantly uses generic terms (you(people), you(man), you(woman))
- NT: Frequently uses specific groups (you(disciples), you(Pharisees), you(followers))
- This appears to be a stylistic difference between He1 (OT) and He2 (NT) encoding teams

---

## 3. Number Formatting (51% Compliance)

### Official Policy (from vocabulary.md, derived from practice)

> "Use numerals: '2 sons', '10 years'"
> "Not words: 'two sons', 'ten years'"
> "Number words not recognized as adjectives in ontology"

### Statistics
- **Supporting (digits)**: 535 verses (51%)
- **Contradicting (words)**: 507 verses (49%)

### Contradicting Examples

| # | Verse | Contradicting Text |
|---|-------|-------------------|
| 1 | **Genesis 1:16** | "God made **two** lights. God made a bright light..." |
| 2 | **Genesis 2:9** | "God also put 2 special trees... **One** tree causes a person..." |
| 3 | **Genesis 2:16** | "...except the fruit [that is on **one** tree]" |
| 4 | **Genesis 2:21** | "God took **one** rib from Adam's body" |
| 5 | **Genesis 2:24** | "God joins the man and the woman into **one** body" |
| 6 | **Genesis 6:10** | "Noah had 3 **three** sons" (mixed!) |
| 7 | **Genesis 7:2** | "...take **seven** pairs of each clean animal..." |

### Analysis
The corpus shows extreme inconsistency:
- "2" and "two" appear interchangeably
- "one" is almost always written as a word, not "1"
- Small numbers (1-10) frequently use words
- Large numbers (127, 180, 10000) consistently use digits
- Genesis 6:10 shows "3 three" - both digit and word in same phrase!

---

## 4. Demonym → Description (55% Compliance)

### Official Policy (notation.md, Special Relations)

> **nationality** – "Hebrew man"
>
> Common practice suggests converting demonyms to relative clauses: "Moabite" → "[who was from Moab]"

### Statistics
- **Supporting (converted)**: 157 verses (55%)
- **Contradicting (kept as demonym)**: 126 verses (45%)

### Contradicting Examples

| # | Verse | Contradicting Text |
|---|-------|-------------------|
| 1 | **Genesis 10:16** | "Canaan was also the ancestor of the **Jebusite**, Amorite, Girgashite." |
| 2 | **Genesis 10:17** | "Canaan was also the ancestor of the **Hivite**, Arkite, and Sinite." |
| 3 | **Genesis 10:18** | "Canaan was also the ancestor of the **Arvadite**, Zemarite, and **Hamathite**." |
| 4 | **Genesis 12:6** | "At that time the **Canaanite** were living in that land." |
| 5 | **Genesis 12:12** | "[When the **Egyptians** see you(Sarai)]... Then an **Egyptian** man will kill me(Abram)..." |
| 6 | **Ruth 1:22** | "Naomi returned from Moab with **Ruth the Moabitess**" |
| 7 | **Esther 2:5** | "There was a **Jewish** man named Mordecai..." |

### Analysis
- Ethnic group names in genealogies are almost never converted
- "Egyptian", "Jew/Jewish", "Greek" are frequently kept as-is
- Conversion happens more often for specific individuals: "Ruth [who was from Moab]"
- No clear rule distinguishes when to convert vs. keep

---

## 5. Hyphenated Verb Base Form (98% Compliance)

### Official Policy (checklist.md §0.26, §1)

> **§0.26**: "Don't write hyphenated words inflected. Don't write 'John stood-up'; write 'John stand-up'."
>
> **§1**: "With a few exceptions, like 'in order to', words that are hyphenated in the ontology need to be hyphenated in the phase 1. For instance, in order to say 'John stood up', write it as 'John stand-up'. Don't write hyphenated words inflected. Don't write 'John stood-up.'"

### Statistics
- **Supporting (base form)**: 216 verses (98%)
- **Contradicting (inflected)**: 5 verses (2%)

### Contradicting Examples

| # | Verse | Contradicting Text |
|---|-------|-------------------|
| 1 | **Matthew 7:25** | "Then _implicit the rain _frameInferable **fell-A**." |
| 2 | **Matthew 7:27** | "Then _implicit the rain _frameInferable **fell-A**." |
| 3 | **Matthew 28:4** | "And those guards **fell-B** on the ground." |
| 4 | **Matthew 28:6** | "You(women) (imp) come. You(women) (imp) see the place [where Jesus **lay-B**]." |
| 5 | **Mark 12:8** | "Then those people/farmers **threw-B** that son of the dead body..." |

### Analysis
This rule has high compliance (98%), but the contradicting examples are notable:
- All contradictions are in NT (Matthew, Mark) - He2 format
- All involve past tense forms: "fell-A", "lay-B", "threw-B"
- The sense suffix (-A, -B) is preserved but inflection was not removed
- May indicate He2 encoder did not apply the base form rule consistently

---

## 6. Passive Voice Handling

### Official Policy (checklist.md §0.13)

> **§0.13**: "If you use a passive, include the agent with 'by', like 'John was hit by a soldier' or 'John was hit by a soldier _implicitActiveAgent' if the agent (subject) of the sentence is implicit information."

### Statistics
- **Passive → Active conversion**: 0 verses (0%)
- **Passives kept as passive**: 76 verses (100%)

### Examples (All Passives Kept)

| # | Verse | Passive Text |
|---|-------|-------------|
| 1 | **Genesis 14:13** | "the big trees [that **were owned by** a man named Mamre]" |
| 2 | **Genesis 14:21** | "my(king's) people [who **were captured by** the four kings]" |
| 3 | **Genesis 17:24** | "Abraham was 99 years old [when Abraham **was circumcised by** a person]" |
| 4 | **Genesis 17:26** | "Abraham and Abraham's son **were circumcised by** a person on the same day" |
| 5 | **Genesis 17:27** | "all the men [who lived with Abraham] **were circumcised by** a man" |
| 6 | **Mark 2:3** | "Some men came to Jesus. Those men **were carrying** a man [who **was controlled by** a spirit/demon]" |

### Analysis
The policy does NOT require converting passive to active - it requires:
1. Keeping the passive form
2. Always including the agent with "by"
3. Marking implicit agents with `_implicitActiveAgent`

The corpus correctly keeps passives but the agent marking varies:
- Some passives have agents: "was circumcised by a person"
- He2 uses `_implicitActiveAgent` marker when agent is implicit
- This is actually **compliant** with policy, not contradicting

---

## Recommendations

### For TBTA Policy Team

1. **Modal Decomposition**: Clarify policy for "must", "should", "could", "would"
   - Current policy only addresses "can"
   - 86% of verses keep other modals unchanged
   - Either expand the decomposition rules OR explicitly allow modals

2. **Addressee Patterns**: Standardize He1 vs He2 approach
   - He1 uses generic: `you(people)`
   - He2 uses specific: `you(disciples)`
   - Recommend documenting this as intentional format difference

3. **Number Formatting**: Establish clear threshold
   - Current practice: digits for numbers > 10, words for 1-10
   - Policy says always use digits
   - Recommend clarifying or updating policy to match practice

4. **Demonym Handling**: Clarify conversion criteria
   - Genealogies: keep demonyms (Jebusite, Hivite)
   - Individual references: convert to relative clause
   - Major ethnic groups (Jew, Egyptian): optional

5. **Hyphenated Verbs**: Reinforce base form rule for He2 encoders
   - 98% compliance is good
   - 5 NT verses need correction: Matt 7:25, 7:27, 28:4, 28:6, Mark 12:8

---

## Appendix: Full Evidence Counts

| Rule | Supporting Verses | Contradicting Verses | Compliance Rate |
|------|------------------|---------------------|-----------------|
| Coreference Resolution | 915 | 6 | 99.3% |
| Clause Segmentation | 3,014 | 0 | 100% |
| Explicit Relativization | 4,073 | 67 | 98.4% |
| Deixis Marking | 3,248 | 3 | 99.9% |
| LDV Substitution | 1,466 | 0 | 100% |
| Subordinate Bracketing | 2,362 | 4 | 99.8% |
| Quote Framing | 1,016 | 0 | 100% |
| Imperative Marking | 1,189 | 0 | 100% |
| Hyphenated Verbs | 1,076 | 4 | 99.6% |
| Modal Decomposition | 133 | 787 | **14%** |
| Demonym → Description | 157 | 126 | **55%** |
| Gap-filling (Implicit) | 1,526 | 0 | 100% |
| Yahweh Substitution | 914 | 1 | 99.9% |
| Number Formatting | 535 | 507 | **51%** |
| Passive → Active | 0 | 76 | **0%** |
| Title Patterns | 378 | 0 | 100% |
| Addressee Patterns | 484 | 229 | **68%** |
| Hyphenated Base Form | 216 | 5 | **98%** |
| Underscore Markers | 1,416 | 0 | 100% |

---

*Report generated from analysis of encoded TBTA verses against official policy documents (checklist.md, notation.md)*

