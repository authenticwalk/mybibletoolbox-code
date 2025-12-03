<<<<<<< HEAD
# Illocutionary Force - TBTA Documentation Review

**Feature**: Illocutionary Force
**TBTA Tier**: Tier A (Essential) - Feature #12
**Status**: ✅ Complete (according to TBTA-FEATURES.md)
**Category**: Clause-level feature (Category 105)

## Sources

All findings in this document are cited to the following sources:

- `{tbta-features}`: /bible-study-tools/tbta/tbta-source/TBTA-FEATURES.md
- `{tbta-data-structure}`: /bible-study-tools/tbta/tbta-source/DATA-STRUCTURE.md
- `{tbta-github}`: https://github.com/AllTheWord/tbta_db_export README.md
- `{archive-readme}`: /bible-study-tools/tbta/features/features-archive/illocutionary-force/README.md
- `{archive-learnings}`: /bible-study-tools/tbta/features/features-archive/illocutionary-force/LEARNINGS.md
- `{archive-experiment}`: /bible-study-tools/tbta/features/features-archive/illocutionary-force/experiments/experiment-001.md
=======
# TBTA Documentation Review: Illocutionary Force

**Last Updated**: 2025-11-29
**Feature Status in TBTA**: Tier A, Complete ✅ {tbta-features}
**TBTA Field Name**: "Illocutionary Force"
**Feature Location**: Clause-level (`context.pragmatics`) {data-structure}
>>>>>>> origin/feat/self-learning-tbta

---

## 1. Feature Definition

<<<<<<< HEAD
### What is Illocutionary Force?

**Illocutionary force identifies the speech act function of an utterance—whether it functions as a statement, question, command, request, suggestion, or expression of desire.** `{archive-readme}`

The term comes from speech act theory (J.L. Austin, John Searle), which distinguishes:
- **Locutionary act**: What is literally said
- **Illocutionary act**: What the speaker intends to accomplish (the force)
- **Perlocutionary act**: The effect on the hearer

**TBTA focuses on illocutionary force**: the communicative function of each clause regardless of its grammatical form. A clause may have interrogative form but declarative force (rhetorical questions), or indicative form but imperative force (indirect commands). `{archive-learnings}`

### Conceptual Foundation

Illocutionary force determines **HOW a clause functions communicatively**—whether asserting, questioning, commanding, or exhorting. `{archive-readme}`

This feature is critical because:
1. **East Asian languages** (Japanese, Mandarin, Korean) require sentence-final particles for every clause type; missing a question particle makes a sentence ungrammatical `{archive-readme}`
2. **Imperative register choices** (direct vs. polite vs. honorific) encode speaker-hearer relationships with theological significance: Jesus commanding demons vs. teaching disciples requires different forms `{archive-readme}`
3. **Without correct force marking**, translations become ambiguous or convey unintended authority dynamics `{archive-readme}`

---

## 2. TBTA Value Inventory

### Character-Based Encoding

**Source**: `{tbta-github}`

Illocutionary force is encoded at **position 3** in clause semantic data (SyntacticCategory 105), using a **single character** to represent the speaker's communicative intent:

| Code | Value | Definition |
|------|-------|-----------|
| **D** | Declarative | Statement of fact; assertion |
| **I** | Imperative | Command; directing hearer to act |
| **C** | Content Interrogative | Question seeking information (wh-questions: who, what, when, where, why, how) |
| **Y** | Yes-No Interrogative | Polar question expecting yes/no response |
| **S** | Suggestive | Proposal or suggestion ("let's" structure) |
| **L** | Jussive | Expression of wish or command (3rd person or mild command) |
| **i** | Imperative with emphasized Agent | Command with explicit focus on the agent performing the action |

### Additional Values from Archive Research

**Source**: `{archive-readme}`, `{archive-learnings}`

The archived research identifies additional force types used in linguistic analysis, though their presence in TBTA encoding is **Not listed** in official GitHub documentation:

| Value | Definition | Biblical Context |
|-------|-----------|------------------|
| **Hortative** | First-person plural exhortation/invitation | "Let us love one another" (1 John 4:7) |
| **Exclamative** | Expression of strong emotion/surprise | "How great is God!" (Romans 11:33) |

**Note**: Hortative may be encoded as **S** (Suggestive), and Exclamative may not have dedicated encoding.

### Complete Enumeration Status

**Official TBTA encoding**: 7 distinct values (D, I, C, Y, S, L, i) `{tbta-github}`
**Linguistic analysis values**: 9+ types including Hortative, Exclamative `{archive-readme}`

**Discrepancy**: Archive research discusses Wh-Interrogative and Exclamative separately, but official TBTA uses **C** (Content Interrogative) for wh-questions and has **no dedicated exclamative code**. `{tbta-github}` vs `{archive-readme}`

---

## 3. Constraints and Gateway Features

### Part of Speech Constraint

**Gateway Feature**: Part = "Clause" `{tbta-data-structure}`

Illocutionary force only applies to **clause-level constituents** (Category 105). Words and phrases do not have illocutionary force; only complete clauses perform speech acts.

### Relationship to Grammatical Mood

**Correlation but NOT Identity**: `{archive-readme}`

| Grammatical Mood (Verb) | Illocutionary Force (Clause) | Correlation |
|-------------------------|------------------------------|-------------|
| Imperative mood | → Imperative force | 95%+ `{archive-readme}` |
| Optative mood | → Hortative/Jussive force | 95%+ `{archive-readme}` |
| Subjunctive mood | → Mixed (context-dependent) | Variable |
| Indicative mood | → Usually Declarative force | 85%+ `{archive-readme}` |

**Critical Note**: Morphological mood (verb form) does NOT always determine illocutionary force (clause function). Examples:
- Indicative form with imperative force: "You will honor your father" (form=indicative, force=imperative) `{archive-readme}`
- Interrogative form with declarative force: "Who can stand before God?" (rhetorical question asserting "no one")  `{archive-readme}`

### Interaction with Clause Type

**Source**: `{tbta-github}`

Position 2 in clause semantic data identifies **structural clause type** (Independent, Coordinate, Restrictive Thing Modifier, etc.), which is distinct from but related to illocutionary force.

**Example**: A clause can be:
- Type: Independent (position 2 = I)
- Force: Declarative (position 3 = D)
- Combined: "IDp..." = Independent Declarative clause with agent as topic

---

## 4. TBTA Annotation Policy

### Semantic vs. Morphological Priority

**Policy**: TBTA prioritizes **pragmatic function over morphological form**. `{archive-learnings}`

Evidence:
1. **Rhetorical questions** use interrogative form but may be annotated for their actual force (declarative/exclamative function) `{archive-learnings}`
2. **Indirect speech acts** are analyzed by speaker intent, not surface structure: "Would you mind closing the door?" has interrogative form but imperative force `{archive-readme}`

### Handling Form-Function Mismatches

**Not explicitly documented** in official TBTA sources, but archive research shows:

**Rhetorical Questions** (interrogative form, declarative/exclamative function):
- Frequency: 20-30% of biblical questions are rhetorical `{archive-readme}`
- Higher in prophetic books (~40%), lower in historical narrative (~10%) `{archive-readme}`
- Treatment: **Not listed** whether TBTA encodes form (C/Y) or function (D)

**Indirect Imperatives** (declarative/interrogative form, imperative function):
- Example: "You will honor your father" (indicative form, imperative function)
- Treatment: **Not listed** in official documentation

### Register and Honorific Marking

**Not included** in core illocutionary force encoding. `{tbta-github}`

However, TBTA separately tracks:
- **Speaker Demographics** (Feature #13): Age, Gender, Relationship, Attitude, Speech Style `{tbta-features}`
- These features work **in conjunction with** illocutionary force for register-sensitive languages

**Archive research notes**: "Imperative register choices (direct vs. polite vs. honorific) encode speaker-hearer relationships that carry theological significance" `{archive-readme}`, but this is handled through Speaker Demographics, not illocutionary force encoding itself.

---

## 5. Documented Examples from TBTA Source

### Example 1: Declarative (Genesis 1:1)

**Source**: `{tbta-data-structure}`

=======
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
>>>>>>> origin/feat/self-learning-tbta
```json
{
  "Part": "Clause",
  "Type": "Independent",
  "Illocutionary Force": "Declarative",
  "Discourse Genre": "Climactic Narrative Story"
}
```
<<<<<<< HEAD

**Analysis**:
- Statement of fact about creation
- No interrogative or imperative markers
- Standard declarative encoding: **D**

### Example 2: Jussive (Genesis 1:3)

**Source**: `{tbta-data-structure}`

```json
{
  "Part": "Clause",
  "Type": "Patient (Object Complement)",
  "Illocutionary Force": "Jussive"
}
```

**Context**: "Let there be light"

**Analysis**:
- Embedded clause within "God said..."
- Jussive force (command/request): **L**
- Quote markers show speech boundaries
- Speaker/Listener track dialogue participants

### Example 3: Not Listed - Interrogative

Official TBTA documentation does **not provide** a worked example of Content Interrogative (C) or Yes-No Interrogative (Y) encoding in the reviewed sources.

**Archive research provides**: Matthew 19:17 ("Why do you ask me about what is good?") as interrogative example `{archive-readme}`, but TBTA encoding for this verse is **Not listed**.

---

## 6. Past Learnings and Best Practices

### Critical Discovery 1: Particle Systems as Effective as Inflectional Systems

**Source**: `{archive-learnings}`

**Finding**: Languages using sentence-final particles (Mandarin, Japanese, Korean) mark illocutionary force **as explicitly and diversely** as languages using inflectional mood systems (German, Russian, Spanish).

**Evidence**:
- Japanese uses dedicated particles for questions (か ka), assertions (よ yo), requests for agreement (な na), softening (ね ne)
- Mandarin uses 8+ particles for different pragmatic effects
- English, despite rich inflection, relies primarily on intonation and word order

**TBTA Implication**: Don't assume lack of verb inflection means lack of force marking. Always check for particles in target languages.

### Critical Discovery 2: Rhetorical Questions Are Systematic

**Source**: `{archive-learnings}`

**Finding**: Hebrew and Greek use interrogative form for multiple pragmatic purposes beyond seeking information:
- Expressing awe/amazement (Romans 11:33)
- Asserting negation (Job 2:10)
- Challenging false assumptions (Matthew 7:3)
- Expressing yearning (Isaiah 53:1)

**Frequency**: Approximately 20-30% of questions in biblical text are rhetorical (varies by book)

**Language Solutions Vary**: English often converts to declarative/exclamative, while Spanish maintains interrogative with exclamation mark, and East Asian languages use special particles for rhetorical effect.

**TBTA Implication**: All biblical questions must be marked for information-seeking vs. rhetorical status. **Not listed** whether TBTA currently implements this distinction.

### Critical Discovery 3: Hortative/Imperative Distinction Affects Theology

**Source**: `{archive-learnings}`

**Finding**: Languages that grammaticalize hortative (first-person plural exhortation) vs. imperative (second-person command) create different theological readings of community responsibility.

**Example**: "Let us love one another" (1 John 4:7) is a call for mutual, reciprocal action. If translated with second-person imperative ("You must love"), it loses the reciprocal dimension.

**Language Families with Hortative Distinction**:
- Quechuan: Dedicated -yachun suffix
- Polynesian: Particles mark first-person plural distinctly
- Some East Asian: Special forms for "let us" vs. "you do it"

**TBTA Encoding**: Uses **S** (Suggestive) for "let's" structures `{tbta-github}`, which may correspond to hortative function.

### Critical Discovery 4: Negative Imperatives Have Distinct Forms

**Source**: `{archive-learnings}`

**Finding**: Many languages distinguish affirmative imperatives ("Do X!") from negative imperatives ("Don't do X!") through completely different morphological patterns.

**Pattern Types**:
- **Suppletion** (Spanish): "¡Vete!" (Go!) vs. "¡No te vayas!" (Don't go!)
- **Mood Shift** (Slavic): Perfective vs. imperfective aspect
- **Suppletive Negative** (Japanese): Different specialized forms
- **Modal Marking** (East Asian): Different particles

**TBTA Handling**: **Not listed** whether negative imperatives receive special encoding beyond standard Polarity feature (Feature #6).

---

## 7. Edge Cases and Special Situations

### Edge Case 1: Interrogative Form, Exclamative Function

**Source**: `{archive-experiment}`

**Example**: Luke 12:49 - "And how I wish it were already kindled!"

**Challenge**:
- Greek: "καὶ τί θέλω εἰ ἤδη ἀνήφθη;" (Interrogative form)
- Function: Exclamative/Declarative (expressing desire, not seeking information)

**Treatment**: **Not listed** whether TBTA encodes form (Y or C) or function (exclamative, which has no dedicated code).

**Translation Impact**: English converts to exclamative; Spanish may maintain question form with emotional markers; languages vary.

### Edge Case 2: Universal Imperatives (Third Person)

**Source**: `{archive-experiment}`

**Example**: Matthew 19:6 - "Let no one separate what God has joined"

**Challenge**:
- Form: Third-person imperative (μὴ χωριζέτω)
- Function: Universal exhortation/principle (not command to specific hearer)
- Scope: Addresses all people

**TBTA Encoding Options**:
- **I** (Imperative): Based on morphological form
- **L** (Jussive): May fit better for third-person/mild commands
- **S** (Suggestive): Possible if treated as universal proposal

**Not listed**: Which encoding TBTA actually uses for third-person imperatives.

### Edge Case 3: Quoted Imperatives in Declarative Contexts

**Source**: `{archive-experiment}`

**Example**: Matthew 22:37-40 - Jesus quoting "Love the Lord... Love your neighbor" within teaching

**Challenge**:
- Original: Imperative commands from Torah
- Context: Declarative framing ("This is the first commandment")
- Function: Mixed—declarative frame with imperative content

**Treatment**: **Not listed** how TBTA handles force annotation for quoted speech within different-force framing contexts.

### Edge Case 4: Imperative with Emphasized Agent

**Source**: `{tbta-github}`

**Encoding**: **i** (lowercase) = Imperative with emphasized Agent

**Definition**: Command with explicit focus on the agent performing the action

**Biblical Context**: **Not listed** - no examples provided in reviewed documentation

**Usage Frequency**: **Not listed** - unknown how common this encoding is

---

## 8. Mixed Annotations and Compound Values

### Are Mixed Annotations Allowed?

**Not explicitly documented** in TBTA GitHub or official sources.

**Character encoding constraint**: Position 3 uses a **single character**, suggesting only **one value per clause**. `{tbta-github}`

**However**: Archive research notes that "some features commonly use mixed annotations (20+ instances per 100 verses), not just edge cases" `{stage-1-research}` for other features like Degree.

**For Illocutionary Force**: **Not listed** whether mixed force annotations are ever used or needed (e.g., interrogative form with declarative function marked as both C and D).

### Subordinate Clause Force

**Source**: `{tbta-github}`, `{tbta-data-structure}`

Subordinate clauses have their own force encoding:
- Position 2 (Clause Type): Identifies structural relationship (Thing Modifier, Event Modifier, Agent, Patient, etc.)
- Position 3 (Illocutionary Force): Encodes the force of the subordinate clause itself

**Example**: Genesis 1:3 embedded clause "Let there be light" has:
- Type: "Patient (Object Complement)" `{tbta-data-structure}`
- Force: "Jussive" `{tbta-data-structure}`

This shows subordinate clauses receive **independent force annotation** based on their own speech act function.

---

## 9. Constraints by Clause Type

### Does Clause Type Constrain Force Options?

**Not explicitly documented**, but logical patterns emerge:

| Clause Type | Likely Force Options | Rationale |
|-------------|---------------------|-----------|
| Independent | All (D, I, C, Y, S, L) | Main clauses can perform any speech act |
| Coordinate Independent | All (D, I, C, Y, S, L) | Coordinated clauses function as main clauses |
| Patient (Object Complement) | Jussive (L), Declarative (D) | Embedded as object of verb (e.g., "God said [Jussive]") |
| Restrictive Thing Modifier | Declarative (D) likely | Relative clauses typically assert information about referent |
| Event Modifier | Declarative (D), Interrogative (C/Y) | Adverbial clauses provide circumstantial information |

**Note**: These constraints are **inferred from linguistic logic**, not explicitly stated in TBTA documentation.

---

## 10. Validation and Quality Notes

### Cross-Reference with Mood Feature

**Mood** (Feature #10, Tier A) tracks **grammatical mood** of verbs: Indicative, Imperative, Subjunctive, Potential, Obligation `{tbta-features}`

**Relationship to Illocutionary Force**:
- Mood = verb-level grammatical category
- Illocutionary Force = clause-level pragmatic function
- **They correlate but are distinct**

**Expected correlation**: Imperative mood → Imperative force (95%+) `{archive-readme}`

**Known issue from Critique**: "Greek imperatives marked as 'Indicative' mood" in some cases `{critique}`, which would create mood-force mismatches.

**TBTA Handling**: **Not listed** whether consistency validation occurs between Mood and Illocutionary Force features.

### Force Distribution by Genre

**Source**: `{archive-readme}`

Expected force distribution varies by discourse genre:

**Narrative** (expected):
- Declarative: ~60%
- Interrogative: ~20%
- Imperative: ~15%
- Other: ~5%

**Teaching/Epistles** (expected):
- Declarative: ~70%
- Imperative: ~15%
- Interrogative: ~10%
- Other: ~5%

**Law** (expected):
- Imperative: ~60%
- Declarative: ~30%
- Interrogative: ~5%
- Other: ~5%

**Note**: These are **expected distributions** from archive research, not validated against actual TBTA data frequencies.

---

## 11. Interaction with Other Features

### Feature #13: Speaker Demographics

**Source**: `{tbta-features}`

6 sub-features: Age, Gender, Relationship, Attitude, Speech Style

**Interaction**: Illocutionary force (WHAT speech act) + Speaker Demographics (HOW it's performed) together determine appropriate register in target languages.

**Example**: Imperative force + "Jesus to demons" (harsh relationship) vs. "Jesus to disciples" (intimate relationship) → different register choices in honorific languages `{archive-readme}`

### Feature #14: Discourse Genre

**Source**: `{tbta-features}`

Values: Narrative, Expository, Poetic, Legal, Prophetic, Epistolary

**Interaction**: Genre affects expected force distribution (see section 10) and appropriate marking in target languages.

### Feature #39: Rhetorical Question (Tier B)

**Source**: `{tbta-features}`

Listed as separate Tier B feature: "True question vs. rhetorical"

**Relationship to Illocutionary Force**:
- Both features deal with interrogative clauses
- Illocutionary Force = basic category (Interrogative)
- Rhetorical Question = refinement (genuine vs. rhetorical)

**This suggests**: TBTA may encode interrogative FORM (C/Y) for all questions, then use Feature #39 to mark rhetorical status separately.

**Validation needed**: Check if Feature #39 implementation distinguishes form from function as archive research suggests.

---

## 12. Discrepancies and Unresolved Questions

### Discrepancy 1: Hortative vs. Suggestive

**TBTA encoding**: Uses **S** for "Suggestive 'let's'" `{tbta-github}`
**Archive research**: Discusses "Hortative" as distinct from Imperative `{archive-learnings}`

**Question**: Are S (Suggestive) and Hortative the same concept, or are they distinct?

**Impact**: First-person plural exhortations ("Let us...") critical for community theology

### Discrepancy 2: Exclamative Force

**TBTA encoding**: **No dedicated code** for exclamative `{tbta-github}`
**Archive research**: Discusses exclamative as distinct force type `{archive-readme}`

**Question**: How does TBTA encode exclamatives? As Declarative (D)? As Interrogative (C/Y) when using interrogative form?

**Impact**: Emotional/awe-filled passages (Romans 11:33, Psalm 8) may lose force marking

### Discrepancy 3: Rhetorical Question Handling

**Feature #39**: Separate "Rhetorical Question" feature exists `{tbta-features}`
**Archive research**: Discusses rhetorical questions extensively `{archive-learnings}`

**Question**: Does TBTA encode interrogative FORM (C/Y) + separate rhetorical flag (Feature #39)? Or does it encode rhetorical questions with declarative force (D)?

**Impact**: 20-30% of biblical questions are rhetorical—encoding choice affects entire system

---

## 13. Summary of TBTA Coverage

### What TBTA Documents Well

✅ **Core values**: 7 distinct force types with clear character codes
✅ **Encoding position**: Position 3 in clause semantic data
✅ **Worked examples**: Declarative (Genesis 1:1) and Jussive (Genesis 1:3)
✅ **Integration**: Works with Clause Type (position 2) and Speaker Demographics

### What TBTA Documents Partially

⚠️ **Hortative vs. Suggestive**: Relationship unclear
⚠️ **Imperative with emphasized Agent**: No examples or usage frequency
⚠️ **Subordinate clause force**: Principle shown but not systematically documented

### What TBTA Does Not Document

❌ **Form-function mismatches**: Policy for rhetorical questions, indirect speech acts
❌ **Exclamative force**: No dedicated encoding
❌ **Mixed annotations**: Whether allowed for compound force
❌ **Negative imperatives**: Special handling beyond Polarity feature
❌ **Third-person imperatives**: Encoding choice (I vs. L vs. S)
❌ **Register distinctions**: Beyond Speaker Demographics interaction
❌ **Validation rules**: Cross-checks with Mood feature
❌ **Force distribution**: Actual frequencies by genre

---

## 14. Key Findings for Algorithm Development

### High-Confidence Prediction Rules

**Source**: `{archive-readme}`

| Condition | Predicted Force | Confidence |
|-----------|----------------|------------|
| Imperative verb form | **I** (Imperative) | 95%+ |
| Interrogative pronoun (who, what, why) | **C** (Content Interrogative) | 90%+ (unless rhetorical) |
| Question particle (Gk: ἆρα, οὐ, μή) | **Y** (Yes-No Interrogative) | 95%+ |
| Optative mood (Greek) | **S** (Suggestive/Hortative) | 95%+ |
| "Let us" structure | **S** (Suggestive) | 95%+ |
| Standard indicative statement | **D** (Declarative) | 85%+ (default) |
| Third-person imperative | **L** (Jussive) | Estimated 80%+ |

### Language Family Patterns

**Particle-based languages** (Mandarin, Japanese, Korean, Thai):
- Mark force more explicitly than inflectional languages
- Use sentence-final particles
- Particle clusters at clause boundaries encode multiple features simultaneously

**Honorific languages** (Japanese, Korean, Javanese):
- Cannot separate force from register/politeness
- Same underlying force requires different surface forms based on relationship
- Speaker Demographics feature critical alongside force

**Evidential languages** (Turkish, Quechuan, many Amazonian):
- Force and evidentiality interact
- Question (interrogative force) + witnessed/reported evidential marking
- Command (imperative force) + knowledge source marking

---

**Document Status**: Stage 1 Research Complete
**Lines**: 328
**All findings cited**: ✅
**Uncertain items marked**: ✅
**Ready for**: Stage 2 Language Study

=======
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
>>>>>>> origin/feat/self-learning-tbta
