# TBTA Mood: Detailed Interpretation Rules

This document provides comprehensive interpretation rules for each mood type. Use this for edge cases and complex constructions.

**For quick reference**, see mood-README.md which contains the decision tree and gateway features.

---

## What is Mood?

**Mood** (also called modality) indicates the speaker's stance toward the action:
- **Indicative**: States action as fact
- **Imperative**: Commands/requests action
- **Subjunctive**: Hypothetical or dependent action
- **Optative**: Wishes or desires
- **Obligation**: Necessity (must/should)
- **Potential**: Possibility (might/could)
- **Permissive**: Permission (may)

---

## Detailed Interpretation Rules

### 1. INDICATIVE MOOD (94.62% in test data)

**Definition**: Speaker states action as fact, reality, or certain prediction.

**Identification Criteria**:
- Mood field = 'Indicative'
- Present, past, or future time all possible
- IlLocutionary Force typically 'Declarative'
- No modal auxiliaries present
- Standard narrative statements

**Greek Morphology**:
- Indicative mood endings (οριστική)
- Can be present, past (aorist/imperfect), future, perfect

**Hebrew Equivalents**:
- Qatal (perfect) - completed/factual actions
- Wayyiqtol - narrative past sequence
- Yiqtol in declarative context

**Examples from Matthew 24**:
- "Jesus **answered**" (Mood: Indicative, Time: Present)
- "You will **hear** about wars" (Mood: Indicative, Time: Immediate Future)
- "Disciples will **see** terrible things" (Mood: Indicative, Time: Immediate Future)

**Translation Implications**:
- Most direct translation path
- Use language's standard declarative forms
- Tense depends on Time field, not mood

**Common Confusion**:
- Future Indicative ≠ Potential: "will hear" (certain) vs "might hear" (uncertain)
- Interrogative Indicative: Questions can use indicative mood for factual queries
  - Example: "Do you **see** all these things?" (Indicative mood, Interrogative force)

---

### 2. OBLIGATION MOODS (2.85% in test data)

Obligation moods indicate necessity, permission, or prohibition along a strength continuum.

#### 2.1 'must' Obligation (Strong) - 1.58% of verbs

**Definition**: Strong necessity; action MUST occur.

**Identification Criteria**:
- δεῖ (dei) + infinitive: "it is necessary to..."
- Strong imperative force
- Time: Typically Immediate Future
- Context: Urgent commands, divine requirements, moral imperatives

**Greek Constructions**:
- δεῖ ἀκοῦσαι "it is necessary to hear" → 'must hear'
- ἀνάγκη (anankē) "necessity"
- Imperative forms with strong authority context

**Hebrew Equivalents**:
- Strong imperatives with divine authority
- Legal language (Leviticus, Deuteronomy)

**Example**: "You **must** go into the fields" (MAT 24:16)
- Urgent escape command
- Life-or-death context (flee persecution)
- Strong necessity, not optional

**Translation**: Strongest necessity markers in target language
- English: "must," "have to," "required to"
- Spanish: "tener que," "deber" (strong)
- German: "müssen"

---

#### 2.2 'should' Obligation (Weak) - 0.32% of verbs

**Definition**: Moderate necessity; action SHOULD occur (advice, recommendation).

**Identification Criteria**:
- χρή (chre) + infinitive: "it is fitting/proper to..."
- δέον ἐστίν (deon estin) "it is necessary" (weaker than δεῖ)
- Advice or recommendation, not mandate
- Time: Often Later Today or near-future

**Greek Constructions**:
- χρή με λέγειν "I should speak"
- Weaker than δεῖ, stronger than simple statement

**Example**: "You **should** look at these buildings" (MAT 24:1)
- Jesus directing disciples' attention
- Recommendation, not command
- Polite directive

**Translation**: Moderate obligation markers
- English: "should," "ought to"
- Spanish: "debería"
- German: "sollte"

**Distinction from 'must'**:
- 'must' = mandatory, required
- 'should' = advisable, recommended
- Context and Greek auxiliary determine strength

---

#### 2.3 Forbidden Obligation (Strong Prohibition) - 0.63% of verbs

**Definition**: Strong prohibition; action MUST NOT occur.

**Identification Criteria**:
- μή (mē) + aorist subjunctive: Greek prohibition structure
- οὐ μή (ou mē) + subjunctive: Emphatic negation
- Strong negative imperative
- Context: Laws, urgent warnings, divine commands

**Greek Constructions**:
- μὴ κλέψῃς (mē klepsēs) "you must not steal" (aorist subjunctive)
- οὐ μή + future indicative/aorist subjunctive: "certainly will not"

**Hebrew Equivalents**:
- לֹא (lo) + imperfect: Ten Commandments structure
- Strong prohibitions in legal texts

**Example**: "Do not go into the houses" (MAT 24:17)
- Urgent prohibition (flee quickly, don't delay)
- Life-or-death context
- Absolute prohibition

**Translation**: Strongest prohibition markers
- English: "must not," "do not," "forbidden to"
- Spanish: "no debes" (strong)
- German: "darfst nicht"

---

#### 2.4 'should not' Obligation (Moderate Prohibition) - 0.32% of verbs

**Definition**: Negative advice; action SHOULD NOT occur.

**Identification Criteria**:
- μή (mē) + present imperative (not aorist subjunctive)
- Weaker prohibition (advice against)
- Context: General wisdom, recommendations

**Greek Constructions**:
- μὴ φοβοῦ (mē phobou) "you should not fear" (present imperative)
- Continuous action advised against

**Translation**: Moderate negative advice markers
- English: "should not," "ought not to"
- Spanish: "no deberías"

**Distinction**:
- Forbidden Obligation (μή + aorist subj): "Don't do it!" (absolute)
- 'should not' (μή + present imp): "You shouldn't do that" (advice)

---

#### 2.5 'may' (permissive) - <0.1% of verbs

**Definition**: Permission granted; action is ALLOWED.

**Identification Criteria**:
- ἔξεστι (exesti) "it is permitted/lawful"
- Permission context (authority grants allowance)
- Not possibility (epistemic), but permission (deontic)

**Greek Constructions**:
- ἔξεστίν σοι "it is permitted to you"
- Authority figure granting permission

**Translation**: Permission markers
- English: "may," "allowed to," "permitted to"
- Spanish: "puedes" (permission)
- German: "darfst" (permission)

**Distinction from 'might' Potential**:
- 'may' (permissive) = permission granted by authority
- 'might' (potential) = epistemic possibility
- English "may" is ambiguous—context disambiguates

---

### 3. POTENTIAL MOODS (2.53% in test data)

Potential moods indicate epistemic possibility along a certainty continuum.

#### 3.1 'might' Potential (Weak Possibility) - 2.53% of verbs

**Definition**: Action is possible but uncertain; hypothetical scenario.

**Identification Criteria**:
- δύναμαι (dunamai) "I am able, I can" (capability → possibility)
- ἴσως (isōs) "perhaps"
- τάχα (tacha) "perhaps, possibly"
- Time: Often "Later Today" or future
- Context: Hypothetical or uncertain future events

**Greek Constructions**:
- δύναμαι ποιῆσαι "I might do" (capability as possibility)
- Conditional structures suggesting uncertainty

**Examples**:
- "False prophets **might** deceive many" (MAT 24:24)
  - Hypothetical future scenario
  - Uncertain outcome (possible, not certain)
  - Warning about potential danger

**Translation**: Weak possibility markers
- English: "might," "could," "may" (epistemic)
- Spanish: "podría"
- German: "könnte"

---

#### 3.2 Probable Potential (Moderate Possibility)

**Definition**: Outcome is probable but not certain.

**Identification Criteria**:
- Stronger than 'might' but weaker than 'definite'
- Likely scenarios, probable outcomes
- Evidence suggests likelihood

**Translation**: Probability markers
- English: "probably will," "likely to"
- Spanish: "probablemente"

---

#### 3.3 Definite Potential (High Possibility)

**Definition**: Certain capability or definite possibility.

**Identification Criteria**:
- Action is definitely possible/capable
- Stronger certainty than 'might' or 'probable'
- Context: Demonstrated capability

**Translation**: Strong capability markers
- English: "definitely can," "is able to"
- Spanish: "puede" (strong capability)

---

### 4. SUBJUNCTIVE MOOD

**Definition**: Hypothetical, conditional, or dependent action.

**Greek Morphology**:
- Subjunctive endings (υποτακτική)
- Often in conditional clauses (ἐάν + subjunctive)
- Purpose clauses (ἵνα + subjunctive)

**Contexts**:
- **Conditional**: ἐὰν ἔλθῃ "if he should come"
- **Purpose**: ἵνα ἀκούσω "in order that I might hear"
- **Indefinite temporal**: ὅταν ἔλθῃ "whenever he comes"
- **Deliberative questions**: τί ποιήσω; "what should I do?"

**Distinction from Indicative**:
- Indicative: Factual conditions (εἰ + indicative)
- Subjunctive: Hypothetical conditions (ἐάν + subjunctive)

---

### 5. OPTATIVE MOOD

**Definition**: Wishes, prayers, remote possibilities.

**Greek Morphology**:
- Optative endings (ευκτική)
- Rare in Koine Greek (more common in Classical)

**Contexts**:
- **Wishes**: γένοιτο "may it be," "let it happen"
- **Prayers**: εὐλογήσαι σε ὁ θεός "may God bless you"
- **Remote possibility**: τάχα ἂν γένοιτο "perhaps it might happen"

**Translation**:
- English: "may," "might," "would that"
- Often requires modal constructions or subjunctive

---

### 6. IMPERATIVE MOOD

**Definition**: Commands, requests, exhortations.

**Greek Morphology**:
- Imperative endings (προστακτική)
- Second person (commands to listener)
- Third person (exhortations: "let him go")

**Hebrew Morphology**:
- Imperative (second person commands)
- Jussive (third person: "let him go")
- Cohortative (first person: "let us go")

**Contexts**:
- Direct commands: ἄκουε "hear!"
- Prohibitions: μὴ φοβοῦ "do not fear"
- Requests: δός μοι "give me"

**Translation**:
- Use target language's imperative forms
- Consider politeness levels (some languages have multiple)

---

## Time Field Correlation

The Time field provides additional semantic information about mood:

| Time | Mood Type | Interpretation |
|------|-----------|-----------------|
| Present | Indicative | Current state of affairs |
| Immediate Future | Obligation/Indicative | Imminent action (factual or required) |
| Later Today | Potential/'should' | Near-term possibility/recommendation |
| Discourse | Indicative | Narrative/timeless present |
| Historic Past | Indicative | Historical fact |
| Remote Future | Potential | Distant possibility |

---

## Aspect Correlation

Aspect modifies mood interpretation:

| Aspect | Mood | Combined Meaning |
|--------|------|------------------|
| Perfective | Indicative | Completed fact |
| Imperfective | Obligation | Ongoing requirement |
| Progressive | Imperative | Action in progress requested |
| Habitual | Indicative | Regular factual pattern |
| Inceptive | Obligation | Beginning requirement |

---

## Clause Type Significance

Clause structure affects mood interpretation:

| Clause Type | Typical Moods | Meaning |
|------------|---------------|---------|
| Independent | Indicative, Imperative | Main statement or command |
| Event Modifier (Adverbial) | Subjunctive, Conditional | Dependent hypothetical |
| Object Complement | Obligation, Indicative | Embedded requirement/statement |
| Relative Clause | Indicative | Describing factual referent |
| Purpose Clause | Subjunctive | Goal/intention |

---

## Polarity Interaction

Polarity (affirmative/negative) modifies obligation strength:

| Construction | Mood | Interpretation |
|-------------|------|----------------|
| Affirmative + 'must' | Strong positive obligation | "You must go" |
| Negative + 'must' | Forbidden Obligation | "You must not go" |
| Affirmative + 'should' | Moderate advice | "You should go" |
| Negative + 'should' | 'should not' Obligation | "You shouldn't go" |
| Affirmative + 'may' | Permission | "You may go" |
| Negative + 'may' | No permission | "You may not go" (polite prohibition) |

---

## Worked Example: Matthew 24:2

**Greek**: ἀποκριθεὶς δὲ ὁ Ἰησοῦς εἶπεν αὐτοῖς· οὐ βλέπετε ταῦτα πάντα;
**English**: "Jesus answered and said to them, 'Do you not see all these things?'"

### Prediction Process

**Verb 1: εἶπεν (eipen) "he said"**
1. **Morphology**: Aorist Indicative Active, 3rd singular
2. **Prediction**: Indicative (factual statement)
3. **Confidence**: HIGH (explicit indicative morphology)
4. **Reasoning**: Standard narrative verb, no modal markers

**TBTA Validation**: Indicative ✓

---

**Verb 2: βλέπετε (blepete) "you see"**
1. **Morphology**: Present Indicative Active, 2nd plural
2. **Context**: In interrogative clause ("Do you not see...?")
3. **IlLocutionary Force**: Interrogative (yes-no question)
4. **Semantic**: Genuine question about observable fact, not command
5. **Prediction**: Indicative (question about fact, not obligation)
6. **Confidence**: HIGH
7. **Reasoning**: Interrogative force ≠ non-indicative mood

**Key Insight**: IlLocutionary Force and Mood are separate dimensions
- A question can have Indicative mood (asking about facts)
- Imperative mood would be command phrased as question

**TBTA Validation**: Indicative ✓

---

## Complex Cases and Edge Cases

### Case 1: Indirect Commands
**Pattern**: Indicative form with imperatival force
**Example**: "You will go to Jerusalem" (could be prediction OR command)
**Resolution**: Check IlLocutionary Force, speaker authority, context

### Case 2: Rhetorical Questions
**Pattern**: Interrogative form with statement/command force
**Example**: "Should we not obey God?" (expects yes, functions as obligation)
**Resolution**: Analyze rhetorical function, not just syntax

### Case 3: Embedded Moods
**Pattern**: Infinitive clauses inheriting mood from parent verb
**Example**: δεῖ ἀκοῦσαι "it is necessary to hear"
- Parent: δεῖ (modal auxiliary)
- Embedded: ἀκοῦσαι (infinitive "to hear")
- Result: 'must' Obligation applies to "hear"

### Case 4: Mixed Polarity
**Pattern**: Negation affecting mood strength
**Example**: "You should not fear" vs "You must not steal"
- 'should not' = μή + present imperative
- 'must not' = μή + aorist subjunctive
**Resolution**: Greek construction determines strength

---

**Document Version**: 2.0
**Last Updated**: 2025-11-07
**Test Data**: Matthew 24 (316 verbs, 51 verses)
