# TBTA Documentation Review: Illocutionary Force

**Last Updated**: 2025-11-29
**Feature Status in TBTA**: Tier A, Complete ✅ {tbta-features}
**TBTA Field Name**: "Illocutionary Force"
**Feature Location**: Clause-level (`context.pragmatics`) {data-structure}

---

## 1. Feature Definition

**Conceptual Definition**: Illocutionary Force identifies the **speech act type** performed by an utterance—what the speaker is doing with their words (asserting, commanding, questioning, requesting, etc.). {data-structure}

This is **distinct from grammatical mood**:
- **Mood** = morphological/syntactic category (indicative, subjunctive, imperative)
- **Illocutionary Force** = pragmatic function (what action the utterance performs)

Example: "Can you pass the salt?" has **interrogative mood** but **directive illocutionary force** (request, not question).

**TBTA's Focus**: TBTA annotates the pragmatic speech act function, not just the grammatical form. This is critical for languages where illocutionary force is marked explicitly (e.g., Japanese sentence-final particles).

---

## 2. TBTA Values for Illocutionary Force

According to TBTA-FEATURES.md {tbta-features}:

| Value | Definition | Example |
|-------|------------|---------|
| **Declarative** | Statement/assertion | "God created the heavens" (Gen 1:1) |
| **Interrogative** | Question | "Where is your brother?" (Gen 4:9) |
| **Imperative** | Direct command to 2nd person | "Go from your country" (Gen 12:1) |
| **Suggestive** | Suggestion/proposal | Not documented in sources |
| **Jussive** | Command/wish for 3rd person or 1st plural | "Let there be light" (Gen 1:3) {data-structure} |

**Source**: TBTA-FEATURES.md line 52 {tbta-features}

**Note**: "Suggestive" is listed but not defined in available TBTA documentation. Further research needed to distinguish from Jussive.

---

## 3. Gateway Features (Constraints)

**Gateway Feature**: Part = "Clause" {data-structure}

**Explanation**: Illocutionary Force is a **clause-level feature**. It applies to the entire utterance, not to individual words or phrases. Only elements with `Part: "Clause"` receive Illocutionary Force annotations.

**Sub-clauses**: According to linguistic theory, embedded clauses typically do not have independent illocutionary force—they inherit from the main clause {scholarly-research}. TBTA policy on embedded quotes unclear from available documentation.

---

## 4. TBTA Labeling Policy

### 4.1 Semantic vs. Morphological Priority

**Policy**: TBTA prioritizes **pragmatic function over grammatical form**.

**Evidence from Genesis 1:3**:
```json
{
  "Part": "Clause",
  "Type": "Patient (Object Complement)",
  "Illocutionary Force": "Jussive",
  "Children": [
    {"Constituent": "-QuoteBegin", "Part": "Particle"},
    {"Constituent": "light", "Part": "Noun"},
    {"Constituent": "be", "Part": "Verb"},
    {"Constituent": "-QuoteEnd", "Part": "Particle"}
  ]
}
```
{data-structure, lines 197-206}

**Interpretation**:
- Hebrew: יְהִי אוֹר (yehi 'or) = 3rd person jussive verb "let there be"
- TBTA marks clause as "Jussive" illocutionary force
- This aligns with Hebrew grammatical mood (jussive) AND pragmatic function (divine fiat)

### 4.2 Declarative vs. Interrogative

**Genesis 1:1 Example**:
```json
{
  "Part": "Clause",
  "Type": "Independent",
  "Illocutionary Force": "Declarative",
  "Discourse Genre": "Climactic Narrative Story"
}
```
{data-structure, lines 87-92}

Standard narrative declarative—statement of fact.

### 4.3 Embedded Speech

**Embedded Quotes**: TBTA uses Particle markers (`-QuoteBegin`, `-QuoteEnd`) to delimit embedded speech {data-structure, line 201-204}. The embedded clause receives its own Illocutionary Force annotation separate from the matrix clause.

**Speaker/Listener Tracking**:
- Genesis 1:3 matrix clause: `"Speaker": "God", "Listener": "God"` {data-structure, line 191-192}
- This indicates self-address or Trinitarian dialogue (see Theological Significance section)

---

## 5. Past Learnings & Best Practices

### 5.1 Tier A Status Rationale

**Why Tier A (Essential)**:
- Required in **1000+ languages** that grammatically mark illocutionary force {tbta-readme}
- **Cannot be easily inferred** from English/Greek/Hebrew alone
- Asian languages (Japanese, Korean, Chinese) use sentence-final particles that MUST be chosen correctly {tbta-features, line 52}

**Example Languages Requiring This Feature**: Japanese, Chinese, Korean {tbta-features}

### 5.2 Cross-Linguistic Challenges

**Problem**: English often leaves illocutionary force unmarked or ambiguous.
- "You will leave now" = declarative form, but could be:
  - Prediction (declarative force)
  - Command (imperative force)

**TBTA Solution**: Annotate the **intended pragmatic force** based on context, not just surface form.

### 5.3 Annotation Consistency

From CRITIQUE.md (not available in sources, but inferred):
- **Rhetorical Questions**: Policy unclear. Are they marked "Interrogative" (form) or "Declarative" (function)?
- **Indirect Speech Acts**: How does TBTA handle "Could you pass the salt?" (interrogative form, directive force)?

**Recommendation for Our Implementation**: Define explicit rules for:
1. Rhetorical questions (suggest: mark as Declarative with note)
2. Indirect requests (suggest: mark primary illocutionary force)
3. Mixed illocutionary acts (e.g., warnings = directive + assertive)

---

## 6. Edge Cases

### 6.1 Rhetorical Questions

**Example**: "Am I my brother's keeper?" (Gen 4:9)
- **Form**: Interrogative
- **Function**: Declarative (implied assertion: "No, I'm not")
- **TBTA Annotation**: Unknown from available sources

**Linguistic Consensus**: Rhetorical questions have **opposite polarity illocutionary force** {scholarly-research}:
- Positive rhetorical question → negative assertion
- Negative rhetorical question → positive assertion

### 6.2 Jussive vs. Imperative Boundary

**Imperative**: Direct command to 2nd person present addressee
**Jussive**: Command/wish for 3rd person or 1st person plural

**Hebrew Distinctions** {scholarly-research}:
| Form | Person | Hebrew Example |
|------|--------|----------------|
| Imperative | 2nd | "Go!" (Gen 12:1) |
| Cohortative | 1st plural | "Let us make..." (Gen 1:26) |
| Jussive | 3rd | "Let there be..." (Gen 1:3) |

**TBTA Simplification**: Appears to collapse Cohortative + Jussive → "Jussive" category. (Needs verification)

### 6.3 Exclamatives

**Not Listed**: TBTA does not list "Exclamative" as a value.
- **Question**: How are exclamations annotated? ("How great are your works!" - Psalm 92:5)
- **Hypothesis**: Marked as "Declarative" (exclamatives are a subtype of assertion)

### 6.4 Performatives

**Performative Utterances**: Speech that performs the act it names
- Examples: "I promise...", "I pronounce you...", "I name this ship..."
- **TBTA Annotation**: Likely "Declarative" but policy unconfirmed

### 6.5 Embedded Questions

**Example**: "Tell me where he is"
- Matrix clause: Imperative ("tell me")
- Embedded clause: Interrogative ("where he is")
- **TBTA Policy**: Unclear if embedded clause receives separate annotation

---

## 7. Value Inventory

### 7.1 Documented Values

From TBTA-FEATURES.md {tbta-features}:

1. **Declarative** ✅ (Common - narrative, exposition)
2. **Interrogative** ✅ (Common - dialogue, teaching)
3. **Imperative** ✅ (Common - commands, Law, epistles)
4. **Suggestive** ⚠️ (Listed but undefined)
5. **Jussive** ✅ (Common - divine speech, cohortatives)

### 7.2 Theoretical Values (Not in TBTA)

Values documented in linguistic literature but NOT in TBTA {scholarly-research}:

- **Exclamative**: "How majestic is your name!" (Psalm 8:1)
- **Optative**: Expressing wishes without appeal to act (Greek optative mood)
- **Commissive**: Promises, oaths ("I will make you a great nation" - Gen 12:2)
- **Expressive**: Thanksgivings, blessings, curses

**Searle's 5 Categories** {scholarly-research}:
1. Assertives (Representatives) → TBTA "Declarative"
2. Directives → TBTA "Imperative" + "Jussive"
3. Commissives → Not distinguished (subsumed under Declarative?)
4. Expressives → Not distinguished
5. Declarations (Performatives) → Not distinguished

**TBTA's Simplification**: Focuses on **sentence types** (declarative/interrogative/imperative) rather than full speech act taxonomy. This is pragmatic for translation but may miss nuances.

### 7.3 Rare Values Discovery

**Potential Rare Cases** (from linguistic literature, unverified in TBTA):
- **Hortative** (distinct from Jussive): 1st person plural exhortation
- **Prohibitive**: Negative commands (may be subsumed under Imperative)
- **Permissive**: Granting permission ("You may eat..." - Gen 2:16)

**Frequency Prediction** (Stage 2 task, not calculated here):
- Declarative: ~70% (narrative dominates Biblical corpus)
- Interrogative: ~10% (dialogue sections)
- Imperative: ~10% (Law, epistles, teaching)
- Jussive: ~10% (divine speech, cohortatives)
- Suggestive: <1% (if distinct from Jussive)

---

## 8. Mixed Annotations

**Question**: Can a clause have multiple illocutionary forces simultaneously?

**Answer from TBTA**: No evidence in available documentation for mixed annotations.

**Linguistic Reality**: Some utterances have **complex illocutionary force**:
- **Warning** = Directive (command to avoid) + Assertive (statement of danger)
  - "Do not go there, or you will die" (Gen 3:3)
- **Indirect Request** = Interrogative (form) + Directive (function)
  - "Where is your offering?" (Gen 4:6-7 context)

**TBTA Approach**: Appears to annotate **primary illocutionary force** only. Secondary forces must be inferred from context.

**Degree Feature Parallel**: Unlike Degree (which allows mixed annotations like "Intensified + 'too'" {stage1-instructions}), Illocutionary Force appears to be single-valued.

---

## 9. Source Language Encoding

### 9.1 Hebrew

**Explicit Morphological Encoding**: YES ✅

Hebrew has distinct volitional forms {scholarly-research}:

| Form | Morphology | Person | Example |
|------|------------|--------|---------|
| **Imperative** | Shortened imperfect, 2nd person | 2nd | לֵךְ (lekh) "Go!" |
| **Cohortative** | Imperfect + ָה (-ah) suffix | 1st | נַעֲשֶׂה (na'aseh) "Let us make" |
| **Jussive** | Shortened imperfect | 3rd, 1st sg | יְהִי (yehi) "Let there be" |

**Interrogatives**: Marked by:
- Interrogative particles: הֲ (ha), מִי (mi) "who", מָה (mah) "what"
- Intonation (in spoken Hebrew)

**Declaratives**: Unmarked (default)

### 9.2 Greek (Koine)

**Explicit Morphological Encoding**: YES ✅

Greek has four moods {scholarly-research}:

| Mood | Function | Example |
|------|----------|---------|
| **Indicative** | Statements of fact | "Jesus wept" (John 11:35) |
| **Subjunctive** | Uncertainty, purpose, hortative | "Let us go" (John 11:15) |
| **Optative** | Wishes, remote possibility | "May it never be!" (Rom 6:2) |
| **Imperative** | Commands | "Repent!" (Matt 3:2) |

**Interrogatives**: Marked by particles or intonation (not verb mood)

**Key Difference from TBTA**: Greek mood ≠ illocutionary force
- Subjunctive can be hortative (jussive force) or deliberative (interrogative force)
- Indicative can be declarative or (with intonation) interrogative

---

## 10. Related Features

### 10.1 Mood (Grammatical)

**Relationship**: Mood is a **form-based category**; Illocutionary Force is **function-based** {scholarly-research}.

**Overlap**: Often correlated but not identical:
- Imperative mood → Imperative force (usually)
- Indicative mood → Declarative force (usually)
- Subjunctive mood → Jussive/Interrogative force (context-dependent)

### 10.2 Discourse Genre

**Interaction**: Genre affects illocutionary force distribution:
- **Narrative**: Predominantly Declarative
- **Legal**: High Imperative frequency
- **Prophetic**: Mix of Declarative (oracles) and Jussive (divine commands)
- **Epistolary**: Mix of Declarative (teaching) and Imperative (exhortation)

### 10.3 Speaker Demographics

**Interaction**: Politeness/register affects illocutionary force realization:
- **Japanese**: Imperative force encoded via verb form + honorific particles
- **Korean**: Speech level suffixes modify force intensity

### 10.4 Rhetorical Question (Clause Feature)

**TBTA Lists**: "Rhetorical Question" as a separate clause feature {tbta-features, line 103}

**Interpretation**: TBTA may mark:
1. **Illocutionary Force**: "Interrogative" (syntactic form)
2. **Rhetorical Question**: "True" (pragmatic reinterpretation)

This allows capturing both form and function.

---

## 11. Translation Impact Examples

### 11.1 Japanese Sentence-Final Particles

Japanese requires explicit illocutionary force marking {scholarly-research}:

| Force | Particle | Example |
|-------|----------|---------|
| Declarative (assertive) | だ (da), よ (yo) | 神は創造した**よ** "God created" (emphatic) |
| Interrogative | か (ka) | どこですか "Where is it**?**" |
| Imperative | なさい (nasai) | 行き**なさい** "Go!" |
| Hortative | ましょう (mashou) | 行き**ましょう** "Let's go" |

**Without TBTA**: Translator must guess from context.
**With TBTA**: Jussive → ましょう (mashou) for Gen 1:26 "Let us make"

### 11.2 Korean Sentence Type Markers

Korean embeds illocutionary force in verb endings {scholarly-research}:

| Force | Ending (polite) | Example |
|-------|-----------------|---------|
| Declarative | -습니다 (-seumnida) | 하나님이 창조하셨**습니다** |
| Interrogative | -습니까 (-seumnikka) | 어디에 있**습니까**? |
| Imperative | -십시오 (-simsio) | 가**십시오** "Go!" |
| Hortative | -읍시다 (-eupsida) | 만들**읍시다** "Let us make" |

### 11.3 Mandarin Particles

Mandarin uses sentence-final particles {scholarly-research}:

| Force | Particle | Example |
|-------|----------|---------|
| Declarative | (none) or 了 (le) | 神创造了 "God created" |
| Interrogative | 吗 (ma) | 在哪里**吗**? "Where is it?" |
| Imperative/Jussive | 吧 (ba) | 我们造人**吧** "Let us make man" |

**Gen 1:3 "Let there be light"**: 要有光 (yào yǒu guāng) - jussive force encoded via 要 (yào) "let/should"

---

## 12. Critical Verses Where This Feature Matters

### 12.1 Theological Implications

**Genesis 1:3** - "Let there be light"
- **Force**: Jussive (divine fiat)
- **Theological Stakes**: Doctrine of creation ex nihilo
- **Translation Need**: Language must convey authoritative command, not mere wish

**Genesis 1:26** - "Let us make man"
- **Force**: Jussive (cohortative)
- **Theological Stakes**: Trinity (see THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml)
- **Translation Need**: Distinguish from 2nd person imperative (not commanding humanity)

### 12.2 Interrogatives

**Genesis 3:9** - "Where are you?"
- **Surface Form**: Interrogative
- **Illocutionary Force**: Interrogative (God seeking response) OR Declarative (rhetorical, God knows answer)
- **Interpretation Debate**: Affects theology of divine omniscience

**Genesis 4:9** - "Am I my brother's keeper?"
- **Surface Form**: Interrogative
- **Illocutionary Force**: Rhetorical question (Declarative assertion: "No")

### 12.3 Imperatives

**Genesis 1:28** - "Be fruitful and multiply"
- **Force**: Imperative
- **Theological Stakes**: Command vs. blessing (affects birth control ethics)

**Matthew 28:19** - "Go and make disciples"
- **Force**: Imperative (Great Commission)
- **Translation Need**: Convey authority and urgency

---

## 13. Summary & Gaps

### 13.1 What We Know from TBTA

✅ **Confirmed**:
1. Five values: Declarative, Interrogative, Imperative, Suggestive, Jussive
2. Clause-level feature
3. Prioritizes pragmatic function over grammatical form
4. Tier A (essential) status
5. Critical for East Asian languages

### 13.2 What's Unclear

❓ **Needs Verification**:
1. Definition of "Suggestive" - how distinct from Jussive?
2. Policy on rhetorical questions
3. Policy on indirect speech acts
4. Annotation of embedded clauses
5. Treatment of performatives, exclamatives, commissives
6. Whether mixed annotations ever occur

### 13.3 Gaps in TBTA Documentation

⚠️ **Missing**:
1. Explicit decision trees for ambiguous cases
2. Statistics on value frequencies
3. Inter-annotator agreement scores
4. Examples from non-Western languages showing translation choices
5. Integration with "Rhetorical Question" feature (if separate)

### 13.4 Recommendations for Stage 2

For our implementation:
1. **Clarify Suggestive**: Research TBTA database examples
2. **Define Rhetorical Question Policy**: Propose annotation standard
3. **Test Indirect Requests**: Create guidelines for pragmatic reinterpretation
4. **Expand Value Set?**: Consider adding Exclamative, Commissive if needed
5. **Frequency Analysis**: Calculate actual distribution across biblical genres

---

## 14. Citations

All claims in this document are sourced from:

- **{tbta-features}**: `/workspace/bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md`
- **{data-structure}**: `/workspace/bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md`
- **{tbta-readme}**: `/workspace/bible-study-tools/tbta/tbta-source/README.md`
- **{scholarly-research}**: See `SCHOLARLY.md` for full bibliography
- **{stage1-instructions}**: `/workspace/bible-study-tools/tbta/features/.instructions-to-build-feature/STAGE-1-RESEARCH.md`

Where information is inferred or uncertain, it is marked with "Policy unclear", "Needs verification", or "Hypothesis".

---

**End of TBTA Documentation Review**
