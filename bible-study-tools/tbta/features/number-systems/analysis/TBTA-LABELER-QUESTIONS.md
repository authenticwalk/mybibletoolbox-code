# Number Systems - Questions for TBTA Labelers

**Purpose**: Clarify labeling rules based on prediction errors from baseline testing.
**Context**: We tested an AI model against 100 TBTA-labeled verses. The model achieved 78% accuracy. The 22 errors reveal ambiguities in the labeling rules that need clarification.

**Note on TBTA Text Format**: The `text` field in TBTA data is a **semantic decomposition** into propositions, NOT a direct translation. Each verse is broken into multiple clauses representing semantic units. For example, PHM-001-020 has 10 different text representations for different clauses within the verse.

---

## Question 1: When is a first-person plural ("we/us/our") labeled Plural vs Singular?

**Pattern observed**: Several verses with Paul as constituent are labeled "Plural" even though Paul is one person.

### Examples

| Verse | Text | Constituent | TBTA Label | English Translation |
|-------|------|-------------|------------|---------------------|
| PHM-001-020 | "God unite **Paul** Lord" | Paul | **Plural** | "Yes, brother, **I** (ἐγώ - singular!) may have benefit from you in the Lord" |
| 1TH-002-019 | "**Paul** know God honor work Paul do" | Paul | **Plural** | "what is our hope, or joy" |
| EPH-001-003 | "God give Paul thing **Paul** be able" | Paul | **Plural** | "who did bless us in every spiritual blessing" |
| 1TH-002-002 | "God Paul cause **Paul** be brave" | Paul | **Plural** | "we were bold in our God" |
| 1TH-002-015 | "Jew treat **Paul** also badly" | Paul | **Plural** | "did persecute us" |

### Key Finding
**PHM-001-020 has INCONSISTENT labeling within TBTA's own data:**

| Clause Path | Text | TBTA Label |
|-------------|------|------------|
| Clause[0]/Clause[1] | "friend **Paul** want Philemon welcome Onesimus" | Singular |
| Clause[1]/Clause[2] | "God unite **Paul** Lord" | **Plural** ← This one is in test set |
| Clause[3]/Clause[3] | "then Philemon cause **Paul** be happy" | Singular |

The same "Paul" in the same verse is labeled BOTH Singular and Plural depending on clause position.

**Greek evidence**: ἐγώ (I) - singular. G1473 confirms first person singular.
- Co-authors: Philemon 1:1 lists "Paul... and Timothy the brother"
- Other examples (1TH, EPH) DO use Greek plural pronouns (ἡμεῖς, ἡμῶν, ἡμᾶς)

### Questions
- Is "Paul" labeled Plural because the Greek/Hebrew uses first-person plural pronouns ("we/us/our") which include Paul plus others (Timothy, Silas, etc.)?
- If so, should the rule be: **Label reflects the pronoun's grammatical number, not the named individual**?
- **Why is PHM-001-020 Plural when Greek uses singular ἐγώ?** Is it because of co-authorship (Paul+Timothy)?
- How should we document this for languages that distinguish inclusive vs exclusive "we"?

---

## Question 2: What is the rule for Quadrial?

**Pattern observed**: Some explicit counts of 4 are labeled Quadrial, but this is linguistically unusual (no attested language has productive quadrial).

### Examples

| Verse | Text | Constituent | TBTA Label | English |
|-------|------|-------------|------------|---------|
| 1KI-007-010 | "stone be 4 **meter** long" | meter | **Quadrial** | "stones of ten cubits" |
| JOS-021-018 | "give 4 **town** tribe Benjamin" | town | **Quadrial** | "four cities" |
| GEN-009-007 | "**Noah** increase number person" | Noah | **Quadrial** | "be fruitful and multiply" (addressed to Noah + 3 sons?) |

### Questions
- Is Quadrial used for any explicit count of 4?
- How is GEN-009-007 Quadrial? Is it because God addresses Noah + his 3 sons (= 4 people)?
- Linguistic note: Corbett (2000) documents no language with productive quadrial. Should this value be:
  - Kept for semantic precision (count of 4)?
  - Merged with Paucal (few)?
  - Removed as not linguistically attested?

---

## Question 3: When is Trial used vs Plural for groups of 3?

**Pattern observed**: Some groups of 3 are labeled Trial, others Plural.

### Examples labeled Trial

| Verse | Text | Constituent | TBTA Label | Context |
|-------|------|-------------|------------|---------|
| DAN-003-015 | "when **man** hear sound man bow statue" | man | **Trial** | Shadrach, Meshach, Abednego (3 friends) |
| GEN-036-016 | "**son** become chief in Edom" | son | **Trial** | 3 chiefs listed: Korah, Gatam, Amalek |
| 1SA-020-022 | "**arrow** be past boy" | arrow | **Trial** | Jonathan's 3 arrows signal |

### Questions
- Is Trial always used when exactly 3 entities are referenced?
- Why is 1SA-020-022 Trial? The English says "arrows" (plural) - is there Hebrew evidence for exactly 3?
- For DAN-003-015: The verse itself doesn't mention "3" - is Trial assigned based on narrative context (we know there are 3 friends)?

---

## Question 4: When is Dual used without explicit count of 2?

**Pattern observed**: Some Dual labels don't have an explicit "2" in the text.

### Examples

| Verse | Text | Constituent | TBTA Label | English | Analysis |
|-------|------|-------------|------------|---------|----------|
| MAT-020-033 | "**man** see" | man | **Dual** | "that our eyes may be opened" | Makes sense - two blind men |
| PRO-007-018 | "**woman** until morning" | woman | **Dual** | "we are filled with loves" | Why Dual? |
| DAN-006-004 | "other **leader** and governor accuse Daniel" | leader | **Dual** | "presidents and satraps" | Why Dual? Only 2 presidents? |

### Questions
- PRO-007-018: Why is "woman" Dual? The context is one woman (the adulteress) speaking. Is it because she says "we" (referring to herself + the man)?
- DAN-006-004: Why is "leader" Dual? Is this because Daniel 6:2 says "three presidents, of whom Daniel was one" - making the OTHER leaders = 2?
- Rule clarification: Is Dual assigned based on:
  - Explicit count of 2?
  - Hebrew/Greek dual morphology?
  - Inferred count from context?

---

## Question 5: When is Paucal used vs Plural?

**Pattern observed**: "A few" sometimes triggers Paucal, but the boundary is unclear.

### Examples

| Verse | Text | Constituent | TBTA Label | English |
|-------|------|-------------|------------|---------|
| MAT-025-023 | "master give **thing** servant" | thing | **Paucal** | "over a few things thou wast faithful" |
| MRK-008-007 | "disciple have small **fish** also" | fish | **Paucal** | "they had a few small fishes" |
| LUK-005-018 | "**man** carry man" | man | **Paucal** | "men bearing upon a couch" (4 men per Mark 2:3?) |

### Questions
- Is Paucal triggered by:
  - The word "few" (ὀλίγος in Greek)?
  - A specific numeric range (3-10)?
  - Contextual inference?
- LUK-005-018: The text just says "men" - is this Paucal because the parallel in Mark 2:3 says "four"? Or because "a few" is implied?
- What's the boundary between Paucal and Plural?

---

## Question 6: When is a morphologically plural word labeled Singular?

**Pattern observed**: GEN-001-007 "water" is labeled Singular despite Hebrew מַיִם (mayim) being morphologically dual/plural.

### Example

| Verse | Text | Constituent | TBTA Label | Hebrew | English |
|-------|------|-------------|------------|--------|---------|
| GEN-001-007 | "God separate **water**" | water | **Singular** | מַיִם (mayim) | "waters which are under" |

### Question
- Is this the "semantic over morphological" rule? (The waters as a single mass = Singular, even though Hebrew form is plural)
- This is similar to שָׁמַיִם (shamayim, "heavens") - is that also labeled Singular?
- How do we document this rule: "Lexicalized plurals treated as Singular when referring to a unified concept"?

---

## Question 7: Why are some singular proper names labeled Plural?

**Pattern observed**: Beyond the "Paul" cases, some singular entities get Plural.

### Examples

| Verse | Text | Constituent | TBTA Label | English |
|-------|------|-------------|------------|---------|
| JDG-019-001 | "man treat woman just-like man treat wife **man**" | man | **Plural** | "a man, a Levite" (clearly singular) |
| JDG-020-009 | "man choose tribe **tribe** attack Gibeah" | tribe | **Plural** | (context unclear) |
| 2SA-021-018 | "Saph be 1 **descendant** Rapha" | descendant | **Plural** | "who is among the children of the giant" |

### Questions
- JDG-019-001: The text explicitly says "a man" (singular). Why Plural?
- 2SA-021-018: Text says "1 descendant" but labeled Plural. Is this because Hebrew בְּנֵי (b'nei, "children of") is grammatically plural?
- Rule: Does morphological plurality in Hebrew override semantic singularity?

---

## Summary of Needed Clarifications

| # | Topic | Core Question |
|---|-------|---------------|
| 1 | First-person plural | Why is PHM-001-020 "Paul" Plural when Greek uses singular ἐγώ? Co-authorship rule? |
| 2 | Quadrial | Is this for any count of 4? Should it exist as a value? |
| 3 | Trial | Always for 3? Based on text or context? |
| 4 | Dual inference | When is Dual assigned without explicit "2"? |
| 5 | Paucal boundary | What triggers Paucal vs Plural? |
| 6 | Morphological vs semantic | When does semantic unity override morphological plurality? |
| 7 | Singular as Plural | When does Hebrew morphology override English meaning? |

---

## Requested Deliverables

1. **Explicit rules** for each number value (when to use it)
2. **Decision tree** for ambiguous cases
3. **Examples** of correct labeling for each edge case type
4. **Clarification** on whether Quadrial should remain in the schema

---

*Document generated from baseline testing analysis on 2025-12-01*
*Model accuracy: 78% (Opus) - errors analyzed to identify rule ambiguities*
