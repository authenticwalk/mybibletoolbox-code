# TBTA Mood Prediction Method

## Overview

This document describes how to PREDICT mood values for biblical verbs using Greek/Hebrew morphology, semantics, and discourse context. The goal is to generate TBTA-style mood annotations WITHOUT looking at existing TBTA labels.

**Methodology**: Analyze source language morphology + semantic patterns + discourse context → Predict mood → Validate against TBTA

**NOT**: Extract mood values from TBTA data structures (that's just reading the answer key!)

## What is Mood?

**Mood** (also called modality) indicates the speaker's stance toward the action:
- **Indicative**: States action as fact
- **Imperative**: Commands/requests action
- **Subjunctive**: Hypothetical or dependent action
- **Optative**: Wishes or desires
- **Obligation**: Necessity (must/should)
- **Potential**: Possibility (might/could)
- **Permissive**: Permission (may)

## Prediction Method

### Step 1: Identify the Verb

From source text (Greek/Hebrew), identify:
- **Lemma**: Base form of verb (e.g., ἀκούω "to hear")
- **Morphology**: Parse code showing mood marking
- **Context**: Clause type, surrounding words

### Step 2: Analyze Greek Morphology

Greek verbs explicitly mark mood in their morphology:

| Greek Mood | Morphology Marker | TBTA Label | Examples |
|------------|------------------|------------|----------|
| **Indicative** (Οριστική) | Indicative endings | `Indicative` | ἀκούω (I hear), ἤκουσα (I heard) |
| **Subjunctive** (Υποτακτική) | Subjunctive endings | `Subjunctive` | ἀκούσω (that I might hear) |
| **Optative** (Ευκτική) | Optative endings | `Optative` | ἀκούσαιμι (may I hear/would that I hear) |
| **Imperative** (Προστακτική) | Imperative endings | `Imperative` | ἄκουε (hear!), ἀκούσατε (hear! pl) |

**Prediction Rule 1**: If Greek morphology shows indicative/subjunctive/optative/imperative mood, use that directly.

### Step 3: Analyze Semantic Modality

Greek indicatives often express modality semantically (through modal verbs or context):

| Semantic Pattern | Greek Construction | TBTA Label | Example |
|-----------------|-------------------|------------|---------|
| **Strong Necessity** | δεῖ + infinitive | `'must' Obligation` | δεῖ ἀκοῦσαι "it is necessary to hear" |
| **Weak Necessity** | δέον ἐστίν, χρή | `'should' Obligation` | χρή με λέγειν "I should speak" |
| **Prohibition** | μή + aorist subjunctive | `Forbidden Obligation` | μὴ κλέψῃς "you must not steal" |
| **Negative Advice** | μή + present imperative | `'should not' Obligation` | μὴ φοβοῦ "you should not fear" |
| **Permission** | ἔξεστι, δυνατός | `'may' (permissive)` | ἔξεστίν σοι "it is permitted to you" |
| **Possibility** | δύναμαι, ἴσως, τάχα | `'might' Potential` | τάχα ἂν γένοιτο "perhaps it might happen" |

**Prediction Rule 2**: Check for modal auxiliary constructions and obligation particles.

### Step 4: Analyze Hebrew Morphology

Hebrew has fewer explicit mood markers:

| Hebrew Form | Semantic Function | TBTA Label | Example |
|------------|------------------|------------|---------|
| **Qatal (Perfect)** | Completed/factual | Usually `Indicative` | שָׁמַע "he heard" |
| **Yiqtol (Imperfect)** | Incomplete/modal | `Indicative` OR modal | יִשְׁמַע "he will hear / let him hear" |
| **Wayyiqtol** | Narrative past | `Indicative` | וַיִּשְׁמַע "and he heard" |
| **Imperative** | Command (2nd person) | `Imperative` | שְׁמַע "hear!" |
| **Jussive** | Command/wish (3rd person) | Context-dependent | יֵלֵךְ "let him go" |
| **Cohortative** | Self-exhortation (1st person) | Context-dependent | נֵלְכָה "let us go" |

**Prediction Rule 3**: Hebrew imperatives → `Imperative`. Jussive/cohortative → Analyze context for obligation vs. permission.

### Step 5: Apply TBTA's Extended Mood Categories

TBTA expands beyond traditional grammatical moods to include semantic obligation/potential:

| TBTA Category | When to Predict | Strength |
|--------------|----------------|----------|
| **'must' Obligation** | δεῖ, strong necessity | Mandatory |
| **'should' Obligation** | δέον, χρή, weak necessity | Recommended |
| **'should not' Obligation** | Negative recommendation | Advised against |
| **Forbidden Obligation** | μή + subjunctive, prohibition | Prohibited |
| **'may' (permissive)** | ἔξεστι, permission granted | Permitted |
| **'might' Potential** | δύναμαι, ἴσως, possibility | Possible |
| **Probable Potential** | Strong likelihood | Probably |
| **Definite Potential** | Certain possibility | Definitely can |

### Step 6: Check Discourse Context

Mood can be modified by discourse function:

| Context | Mood Prediction Impact |
|---------|----------------------|
| **Direct command** | `Imperative` even if not imperative morphology |
| **Prohibition** | `Forbidden Obligation` or `'should not' Obligation` |
| **Conditional clause** | May shift indicative → `Conditional` or `Potential` |
| **Question with command force** | Rhetorical → treat as obligation |
| **Prayer/wish** | May shift to `Optative` semantically |

## Interpretation Rules

### Indicative Mood (94.62% in test data)

**Definition**: Speaker states action as fact

**Identification**:
- Mood field = 'Indicative'
- Present, past, or future time all possible
- IlLocutionary Force typically 'Declarative'

**Examples from Matthew 24**:
- "Jesus answered" (Mood: Indicative, Time: Present)
- "You will hear about wars" (Mood: Indicative, Time: Immediate Future)
- "Disciples will see terrible things" (Mood: Indicative, Time: Immediate Future)

**Translation Implication**: Most direct translations; verb tense depends on Time field

---

### Obligation Moods (2.85% in test data)

**Definition**: Speaker indicates necessity, permission, or prohibition

#### 'must' Obligation (Strong)
- **Count**: 5 in test data
- **Time**: Typically Immediate Future
- **Context**: Actions that MUST occur
- **Example**: "You must go into the fields" (MAT 24:16)
- **Translation**: Strongest necessity; mandatory

#### 'should' Obligation (Weak)
- **Count**: 1 in test data
- **Time**: Typically Later Today
- **Context**: Actions that SHOULD occur but not mandatory
- **Example**: "You should look at these buildings" (MAT 24:1)
- **Translation**: Recommendation; advisable

#### Forbidden Obligation
- **Count**: 2 in test data
- **Time**: Typically Immediate Future
- **Context**: Actions that MUST NOT occur
- **Example**: "Do not go into the houses" (MAT 24:17)
- **Translation**: Prohibition; negative imperative

#### 'should not' Obligation
- **Count**: 1 in test data
- **Context**: Actions that should be avoided
- **Translation**: Negative recommendation

---

### Potential Mood (2.53% in test data)

**Definition**: Action is possible but uncertain

#### 'might' Potential
- **Count**: 8 in test data
- **Time**: Often "Later Today" or future
- **Context**: Hypothetical or uncertain future
- **Examples**:
  - "False prophets might deceive many" (MAT 24:24)
  - "Some might think they are the elect" (MAT 24:24)
- **Translation**: Possibility; conditional possibility

#### Probable Potential
- Less common; indicates probable but uncertain outcome

#### Definite Potential
- Possible but not in test data; indicates more certain possibility

---

## Decision Tree for Mood Prediction

**IMPORTANT**: This is a **reasoning framework for LLM prompts**, NOT code to implement!

This flowchart describes the reasoning steps to include in your prompt to guide the LLM's analysis. The LLM reads these instructions and applies them through natural language reasoning, not through algorithmic execution.

**Method**: Prompt engineering + context engineering
- Include these reasoning steps in your prompt text
- Provide examples showing this reasoning process
- Give the LLM access to source text + translations as context
- Let the LLM reason through the steps using its language understanding

Use this flowchart to PREDICT mood from source text:

```
START: Analyzing verb in source text (Greek/Hebrew)

STEP 1: Check morphological mood
│
├─ Greek Imperative form? → Predict: Imperative
├─ Greek Subjunctive form? → Predict: Subjunctive (check if prohibition)
├─ Greek Optative form? → Predict: Optative
├─ Hebrew Imperative? → Predict: Imperative
└─ Indicative morphology? → Continue to STEP 2

STEP 2: Check for modal auxiliaries
│
├─ δεῖ (dei) + infinitive? → Predict: 'must' Obligation
├─ χρή (chre) + infinitive? → Predict: 'should' Obligation
├─ ἔξεστι (exesti)? → Predict: 'may' (permissive)
├─ δύναμαι (dunamai)? → Predict: 'might' Potential
└─ No modal auxiliary? → Continue to STEP 3

STEP 3: Check for prohibition/negative modality
│
├─ μή + aorist subjunctive? → Predict: Forbidden Obligation
├─ μή + present imperative? → Predict: 'should not' Obligation
├─ οὐ μή + subjunctive (emphatic negation)? → Predict: Forbidden Obligation
└─ Not prohibition? → Continue to STEP 4

STEP 4: Check discourse context
│
├─ In conditional clause? → Predict: Conditional (or keep Subjunctive)
├─ Rhetorical question with command force? → Predict: Imperative
├─ Prayer/wish context? → Predict: Optative (semantic)
├─ Prophetic/oracular statement? → Predict: Indicative (but note genre)
└─ Standard statement? → Predict: Indicative

STEP 5: Determine obligation strength (if obligation detected)
│
├─ Strong necessity (must happen)? → 'must' Obligation
├─ Recommendation (should happen)? → 'should' Obligation
├─ Permission (may happen)? → 'may' (permissive)
├─ Prohibition (must not)? → Forbidden Obligation
└─ Negative advice (should not)? → 'should not' Obligation

STEP 6: Determine potential type (if potential detected)
│
├─ Mere possibility? → 'might' Potential
├─ Probable outcome? → Probable Potential
├─ Certain capability? → Definite Potential
└─ Unlikely scenario? → Unlikely Potential

END: Output predicted mood label
```

## Time Field Correlation

The Time field provides additional semantic information about mood:

| Time | Mood Type | Interpretation |
|------|-----------|-----------------|
| Present | Indicative | Current state |
| Immediate Future | Obligation/Potential | Imminent action |
| Later Today | Should/Might | Near-term possibility/recommendation |
| Discourse | Indicative | Narrative/timeless |
| Historic Past | Indicative | Historical fact |
| Remote Future | Potential | Distant possibility |

## Aspect Correlation

Aspect modifies mood interpretation:

| Aspect | Mood | Meaning |
|--------|------|---------|
| Perfective | Indicative | Completed fact |
| Imperfective | Obligation | Ongoing requirement |
| Progressive | Imperative | Action in progress requested |
| Habitual | Indicative | Regular fact |
| Inceptive | Obligation | Beginning requirement |

## Clause Type Significance

Clause structure affects mood interpretation:

| Type | Typical Moods | Meaning |
|------|---------------|---------|
| Independent | Any | Main statement |
| Event Modifier | Obligation/Potential | Conditional actions |
| Object Complement | Any | Embedded requirement/statement |
| Relative Clause | Indicative | Describing facts |

## Polarity Interaction

Polarity modifies obligation strength:

- **Affirmative + Obligation** → Strong deontic force
- **Negative + 'should'** → Weaker prohibition
- **Negative + 'must'** → Strong prohibition

## Worked Example: Matthew 24:2

**Greek**: ἀποκριθεὶς δὲ ὁ Ἰησοῦς εἶπεν αὐτοῖς· οὐ βλέπετε ταῦτα πάντα;
**English**: "Jesus answered and said to them, 'Do you not see all these things?'"

### Prediction Process

**Verb 1: εἶπεν (eipen) "he said"**
1. Morphology: Aorist Indicative Active, 3rd singular
2. Prediction: `Indicative` (factual statement)
3. Confidence: High (explicit indicative morphology)

**Verb 2: βλέπετε (blepete) "you see"**
1. Morphology: Present Indicative Active, 2nd plural
2. Context: In interrogative clause ("Do you not see...?")
3. Semantic: Genuine question, not command
4. Prediction: `Indicative` (question about fact, not obligation)
5. Confidence: High

**TBTA Validation**: Compare predictions with TBTA labels to verify accuracy.

## Validation Method

After making predictions, validate against TBTA:

### How to Read TBTA Data (for validation only!)

TBTA encodes moods in verb phrase (VP) nodes:

```yaml
clause:
  children:
    - Part: VP
      children:
        - Constituent: look
          Mood: 'should' Obligation  # TBTA's label (for validation)
          Time: Later Today
          Aspect: Unmarked
```

### Validation Process

1. **Make prediction** using morphology + semantics (as described above)
2. **Read TBTA label** from Mood field in VP node
3. **Compare**: Do they match?
4. **Analyze mismatches**:
   - Did we miss a modal auxiliary?
   - Did we misinterpret discourse context?
   - Is TBTA possibly incorrect? (rare but possible)
5. **Refine method**: Update prediction rules based on systematic errors

## Accuracy Assessment

**Current Status**: Methodology defined but needs comprehensive testing

**Needed**:
- Test on 100+ verses across genres (narrative, prophecy, epistle, etc.)
- Calculate accuracy by mood type (Indicative vs Obligation vs Potential)
- Document systematic errors and edge cases
- Measure inter-annotator agreement

**Expected Accuracy**:
- Indicative: 90-95% (most common, clear morphology)
- Imperative: 95-100% (explicit morphology)
- Subjunctive/Optative: 85-90% (context-dependent)
- Obligation: 70-85% (requires semantic analysis)
- Potential: 70-80% (subtle distinctions)

**NOT**: 100% accuracy from extraction - that's just reading the answer key!

## Language-Specific Applications

### Languages with Rich Mood Systems

**Turkish**: Distinguish 'must' from 'should' for evidential system
**Japanese**: Map obligations to keigo (politeness) levels
**Greek**: Preserve original subjunctive/optative distinctions
**Arabic**: Handle complex obligation/permission hierarchies

### Languages with Simple Mood

**English**: Primarily Indicative with modal verbs for obligation/potential
**Mandarin**: Aspect-based; map TBTA mood to aspect markers
**Vietnamese**: Separate mood and aspect; use time field

## Limitations and Edge Cases

1. **Implicit Imperatives**: Commands phrased as questions
   - IlLocutionary Force = Interrogative
   - But context suggests command
   - Solution: Use clause-level force as secondary check

2. **Mixed Moods**: Coordination of different moods
   - Multiple verbs with different moods
   - Context determines scope
   - Solution: Analyze each VP independently

3. **Rare Moods**: Subjunctive/Optative rarely appear in test data
   - Confidence lower for these values
   - More testing needed
   - Solution: Expand test corpus

## Future Extensions

1. **Comprehensive Testing**: Test on 400+ verses across all genres
2. **Nested Clause Analysis**: How moods interact in embedded structures
3. **Discourse Patterns**: Mood sequencing across verses and chapters
4. **Translation Matrices**: Map TBTA moods to target language features
5. **Confidence Scoring**: Refine reliability assessment per mood type
6. **Exception Handling**: Document edge cases and systematic errors
7. **Multi-language Validation**: Use 900+ translations to verify mood predictions

## Key Takeaways

### What This Document Provides

✅ **Prediction method** based on Greek/Hebrew morphology and semantics
✅ **Decision trees** for determining mood from source text
✅ **Validation workflow** comparing predictions to TBTA labels
✅ **Worked examples** showing prediction process
✅ **Honest accuracy estimates** based on feature difficulty

### What This Document Does NOT Do

❌ **Extract moods** from TBTA data (that's not prediction, that's copying)
❌ **Claim 100% accuracy** (prediction is harder than extraction)
❌ **Skip validation** (TBTA labels are our gold standard for testing)

### The Right Approach

1. **Predict** mood using source text + linguistic analysis
2. **Validate** against TBTA to measure accuracy
3. **Learn** from mismatches to improve predictions
4. **Iterate** until accuracy plateaus (likely 80-95% depending on mood type)

## References

- TBTA Feature Doc: `../../FEATURE-SUMMARY.md` (Mood section)
- Greek Grammar: Smyth's Greek Grammar, sections on mood
- Hebrew Grammar: Waltke & O'Connor, Hebrew verb system
- Sample Data (for validation): `../../../../.data/commentary/MAT/024/` (51 verses)
