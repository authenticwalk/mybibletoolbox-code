# TBTA Policy Contradiction Report

> **Analysis Date**: December 2, 2024
> **Corpus**: 6,963 verses across 15 books (Genesis, Joshua, Ruth, 1-2 Samuel, Nehemiah, Esther, Daniel, Jonah, Nahum, Matthew, Mark, Acts, Titus, Philemon, 2 John)
> **Purpose**: Document discrepancies between official TBTA policy and actual encoded verses
> **Source**: [sources.tabitha.bible](https://sources.tabitha.bible) — Click verse links to verify

---

## Important: Two Encoding Layers

The TBTA data has **two distinct encoding fields**:

| Field | Description | Example (Gen 1:16) |
|-------|-------------|-------------------|
| `phase_1_encoding` | Human-readable He1 text | `"God made two lights"` |
| `semantic_encoding` | Machine-parsed structure | Contains `~\lu 2~` (digit) |

**Key Finding**: In many cases, the `semantic_encoding` is correct (uses digits) while the `phase_1_encoding` is inconsistent (uses words). This report analyzes the `phase_1_encoding` field since that's the actual He1 text output.

See **Section 5** for detailed encoding layer discrepancies.

---

## Summary

| Rule | Policy | Status | Notes |
|------|--------|--------|-------|
| Addressee Patterns | "you(people)" not "you(Disciples)" | ⚠️ **68%** | He1 vs He2 style difference |
| Demonym → Description | "Moabite → [who was from Moab]" | ⚠️ **55%** | Inconsistent application |
| Hyphenated Verb Base | "stand-up not stood-up" | ⚠️ **98%** | 5 NT verses need correction |
| Number Formatting | "use numerals" | ⚠️ text layer | See Section 5 |

---

## 1. Addressee Patterns (68% Compliance)

### Official Policy (checklist.md §0.1)

> **§0.1**: "First and second person pronouns (like 'I' and 'you') and 'each-other' must have the referent (person that the pronoun refers to or represents) indicated in parentheses, like 'I(John) talked to Mary'."
>
> **From analysis conventions**: The referent should use generic terms like "you(people)", "you(person)", not specific group names like "you(Disciples)", "you(followers)".

### Statistics
- **Supporting (generic)**: 484 verses (68%)
- **Contradicting (specific)**: 229 verses (32%)

### Contradicting Examples

| # | Verse | Contradicting Text | Source |
|---|-------|-------------------|--------|
| 1 | **Matthew 8:26** | "Jesus asked, ['Why are **you(followers)** afraid?]" | [🔗](https://sources.tabitha.bible/Bible/Matthew/8/26) |
| 2 | **Matthew 9:13** | "But **you(Pharisees)** (imp) go..." | [🔗](https://sources.tabitha.bible/Bible/Matthew/9/13) |
| 3 | **Matthew 9:38** | "Therefore **you(disciples)** (imp) earnestly ask God..." | [🔗](https://sources.tabitha.bible/Bible/Matthew/9/38) |
| 4 | **Matthew 10:8** | "**You(disciples)** (imp) heal the sick people..." | [🔗](https://sources.tabitha.bible/Bible/Matthew/10/8) |
| 5 | **Matthew 10:16** | "**You(disciples)** (imp) listen/behold..." | [🔗](https://sources.tabitha.bible/Bible/Matthew/10/16) |

### Analysis
The corpus shows inconsistent application:
- OT: Predominantly uses generic terms (you(people), you(man), you(woman))
- NT: Frequently uses specific groups (you(disciples), you(Pharisees), you(followers))
- This appears to be a stylistic difference between He1 (OT) and He2 (NT) encoding teams

---

## 2. Number Formatting (Text Layer Issue)

### Official Policy (from vocabulary.md, derived from practice)

> "Use numerals: '2 sons', '10 years'"
> "Not words: 'two sons', 'ten years'"
> "Number words not recognized as adjectives in ontology"

### Statistics
- **Supporting (digits)**: 535 verses (51%)
- **Contradicting (words)**: 507 verses (49%)

### Contradicting Examples

| # | Verse | Actual `phase_1_encoding` Text | Source |
|---|-------|-------------------------------|--------|
| 1 | **Genesis 1:16** | `"God made two lights"` — uses word "two" | [🔗](https://sources.tabitha.bible/Bible/Genesis/1/16) |
| 2 | **Genesis 6:10** | `"Noah had 3 three sons"` — BOTH digit AND word! | [🔗](https://sources.tabitha.bible/Bible/Genesis/6/10) |
| 3 | **Genesis 2:9** | `"put 2 special trees...one of these 2 trees"` — mixed in same sentence | [🔗](https://sources.tabitha.bible/Bible/Genesis/2/9) |
| 4 | **Genesis 2:21** | `"God took one rib"` — uses word "one" | [🔗](https://sources.tabitha.bible/Bible/Genesis/2/21) |
| 5 | **Ruth 1:3** | `"Naomi's two sons"` — uses word "two" | [🔗](https://sources.tabitha.bible/Bible/Ruth/1/3) |

### Analysis
The `phase_1_encoding` field shows extreme inconsistency:
- "2" and "two" appear interchangeably
- "one" is almost always written as a word, not "1"
- Small numbers (1-10) frequently use words
- Large numbers (127, 180, 10000) consistently use digits
- Genesis 6:10 shows "3 three" - both digit and word in same phrase!

**⚠️ Important**: The `semantic_encoding` layer uses digits correctly (see Section 7). This appears to be a `phase_1_encoding` generation issue, not a semantic encoding error.

---

## 3. Demonym → Description (55% Compliance)

### Official Policy (notation.md, Special Relations)

> **nationality** – "Hebrew man"
>
> Common practice suggests converting demonyms to relative clauses: "Moabite" → "[who was from Moab]"

### Statistics
- **Supporting (converted)**: 157 verses (55%)
- **Contradicting (kept as demonym)**: 126 verses (45%)

### Contradicting Examples

| # | Verse | Contradicting Text | Source |
|---|-------|-------------------|--------|
| 1 | **Genesis 10:16** | "...ancestor of the **Jebusite**, Amorite, Girgashite" | [🔗](https://sources.tabitha.bible/Bible/Genesis/10/16) |
| 2 | **Genesis 10:17** | "...ancestor of the **Hivite**, Arkite, and Sinite" | [🔗](https://sources.tabitha.bible/Bible/Genesis/10/17) |
| 3 | **Genesis 10:18** | "...ancestor of the **Arvadite**, Zemarite, and **Hamathite**" | [🔗](https://sources.tabitha.bible/Bible/Genesis/10/18) |
| 4 | **Genesis 12:6** | "At that time the **Canaanite** were living..." | [🔗](https://sources.tabitha.bible/Bible/Genesis/12/6) |
| 5 | **Genesis 12:12** | "Then an **Egyptian** man will kill me(Abram)..." | [🔗](https://sources.tabitha.bible/Bible/Genesis/12/12) |

### Analysis
- Ethnic group names in genealogies are almost never converted
- "Egyptian", "Jew/Jewish", "Greek" are frequently kept as-is
- Conversion happens more often for specific individuals: "Ruth [who was from Moab]"
- No clear rule distinguishes when to convert vs. keep

---

## 4. Hyphenated Verb Base Form (98% Compliance)

### Official Policy (checklist.md §0.26, §1)

> **§0.26**: "Don't write hyphenated words inflected. Don't write 'John stood-up'; write 'John stand-up'."
>
> **§1**: "With a few exceptions, like 'in order to', words that are hyphenated in the ontology need to be hyphenated in the phase 1. For instance, in order to say 'John stood up', write it as 'John stand-up'. Don't write hyphenated words inflected. Don't write 'John stood-up.'"

### Statistics
- **Supporting (base form)**: 216 verses (98%)
- **Contradicting (inflected)**: 5 verses (2%)

### Contradicting Examples

| # | Verse | Contradicting Text | Source |
|---|-------|-------------------|--------|
| 1 | **Matthew 7:25** | "...the rain _frameInferable **fell-A**..." | [🔗](https://sources.tabitha.bible/Bible/Matthew/7/25) |
| 2 | **Matthew 7:27** | "...the rain _frameInferable **fell-A**..." | [🔗](https://sources.tabitha.bible/Bible/Matthew/7/27) |
| 3 | **Matthew 28:4** | "...those guards **fell-B** on the ground" | [🔗](https://sources.tabitha.bible/Bible/Matthew/28/4) |
| 4 | **Matthew 28:6** | "...see the place [where Jesus **lay-B**]" | [🔗](https://sources.tabitha.bible/Bible/Matthew/28/6) |
| 5 | **Mark 12:8** | "...people/farmers **threw-B** that son..." | [🔗](https://sources.tabitha.bible/Bible/Mark/12/8) |

### Analysis
This rule has high compliance (98%), but the contradicting examples are notable:
- All contradictions are in NT (Matthew, Mark) - He2 format
- All involve past tense forms: "fell-A", "lay-B", "threw-B"
- The sense suffix (-A, -B) is preserved but inflection was not removed
- May indicate He2 encoder did not apply the base form rule consistently

---

## Recommendations

### For TBTA Policy Team

1. **Addressee Patterns**: Standardize He1 vs He2 approach
   - He1 uses generic: `you(people)`
   - He2 uses specific: `you(disciples)`
   - Recommend documenting this as intentional format difference

2. **Number Formatting**: Fix `phase_1_encoding` text generation
   - `semantic_encoding` correctly uses digits
   - `phase_1_encoding` inconsistently renders as words
   - Consider regenerating text from semantic layer

3. **Demonym Handling**: Clarify conversion criteria
   - Genealogies: keep demonyms (Jebusite, Hivite)
   - Individual references: convert to relative clause
   - Major ethnic groups (Jew, Egyptian): optional

4. **Hyphenated Verbs**: Reinforce base form rule for He2 encoders
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
| "can" → "is able" | 133 | 0 | 100% ✅ (no "can" found) |
| Demonym → Description | 157 | 126 | **55%** |
| Gap-filling (Implicit) | 1,526 | 0 | 100% |
| Yahweh Substitution | 914 | 1 | 99.9% |
| Number Formatting | — | — | ✅ semantic / ⚠️ text |
| Passive Voice | 76 | 0 | 100% ✅ |
| Title Patterns | 378 | 0 | 100% |
| Addressee Patterns | 484 | 229 | **68%** |
| Hyphenated Base Form | 216 | 5 | **98%** |
| Underscore Markers | 1,416 | 0 | 100% |

---

## 5. Encoding Layer Discrepancies

These are cases where `semantic_encoding` is correct but `phase_1_encoding` differs. Since the semantic layer shows the intended value, these may be generation/rendering issues rather than policy contradictions.

### Number Formatting Discrepancies

| Verse | `phase_1_encoding` | `semantic_encoding` | Source |
|-------|-------------------|---------------------|--------|
| Genesis 1:16 | `"two lights"` (word) | `~\lu 2~` (digit) | [🔗](https://sources.tabitha.bible/Bible/Genesis/1/16) |
| Genesis 6:10 | `"3 three sons"` (both!) | `~\lu 3~` (digit only) | [🔗](https://sources.tabitha.bible/Bible/Genesis/6/10) |
| Ruth 1:3 | `"two sons"` (word) | `~\lu 2~` (digit) | [🔗](https://sources.tabitha.bible/Bible/Ruth/1/3) |
| Genesis 2:21 | `"one rib"` (word) | `~\lu 1~` (digit) | [🔗](https://sources.tabitha.bible/Bible/Genesis/2/21) |

### Analysis

The `semantic_encoding` consistently uses digits as policy requires. However, when rendered to `phase_1_encoding`:
- Small numbers (1-10) are often converted to words
- Genesis 6:10 shows **both** digit and word: `"3 three sons"`
- This suggests a text generation step that inconsistently converts digits to words

### Recommendation

The semantic layer appears correct. The issue is in the `phase_1_encoding` generation:
1. Numbers should render as digits, not words
2. Genesis 6:10's "3 three" indicates a bug where both representations appear
3. Consider regenerating `phase_1_encoding` from `semantic_encoding` with consistent number handling

---

*Report generated from analysis of encoded TBTA verses against official policy documents (checklist.md, notation.md)*

