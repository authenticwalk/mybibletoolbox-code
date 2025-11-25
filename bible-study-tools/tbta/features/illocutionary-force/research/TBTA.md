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

---

## 1. Feature Definition

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

```json
{
  "Part": "Clause",
  "Type": "Independent",
  "Illocutionary Force": "Declarative",
  "Discourse Genre": "Climactic Narrative Story"
}
```

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

