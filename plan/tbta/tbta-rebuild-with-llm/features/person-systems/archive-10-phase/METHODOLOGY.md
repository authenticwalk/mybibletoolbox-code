# Person Systems Prediction Methodology

This document describes the systematic methodology for predicting person-system features (especially clusivity) in Biblical texts using LLM prompt engineering.

**Achievement**: 100% accuracy (11/11 test cases) using hierarchical prompting framework.

## Core Principle: Prediction, Not Extraction

Person-system features (clusivity, obviation) are **implicit** in Biblical source languages. We predict values based on:
- Theological context
- Discourse structure
- Speaker/addressee relationships
- Action semantics

We validate predictions against actual Bible translations in person-marking languages.

## Hierarchical Prompting Framework

The key to high accuracy is checking factors in priority order, terminating early when confident.

```
Level 1: THEOLOGICAL/SEMANTIC PROMPTS (Most Important)
  Ask LLM about theological meaning first
  ↓ If not determined, move to...

Level 2: CAPABILITY/RESTRICTION PROMPTS
  Ask if participants can/must perform action
  ↓ If not determined, move to...

Level 3: DISCOURSE FUNCTION PROMPTS
  Ask about rhetorical purpose and speech act
  ↓ If not determined, move to...

Level 4: GRAMMATICAL CUE PROMPTS
  Ask about explicit markers in text
  ↓ If not determined, move to...

Level 5: BASELINE (Default)
  Use rarity principle - most common value (65% exclusive)
```

**Why This Works**:
- Prioritizes meaning over form (theological factors resolve ambiguity before grammar)
- Early termination (most cases resolved at Level 1-2)
- Clear decision points (each level has binary or categorical outcomes)
- Leverages LLM strengths (modern LLMs excel at theological and semantic analysis)

## Level 1: Theological Analysis Prompt

Use this prompt first for maximum accuracy:

```
Theological Analysis for Clusivity:

Verse: {reference}
Text: "{verse text}"
Pronoun under analysis: "{we/us/our}"

Theological Framework Questions:

1. Who is speaking? (Divine, Apostolic, Prophet, Believer, etc.)
2. Who is being addressed? (God, Believers, Unbelievers, etc.)
3. What action/state is described?
4. Does this involve a divine prerogative?
   - Creation, omniscience, judgment → Restricts participation
   - Example: Genesis 1:26 "Let us make" → Only God creates → EXCLUSIVE

5. Does this describe a salvific/shared experience?
   - Justification, peace with God, faith → Shared participation
   - Example: Romans 5:1 "We have peace" → All believers → INCLUSIVE

6. Is there an authority structure?
   - Apostolic witness, prophetic role → Limited participation
   - Example: Acts 2:32 "We are witnesses" → Only apostles → EXCLUSIVE

7. Does this express community identity?
   - Unity, worship, shared faith → Inclusive participation
   - Example: Hebrews 10:24 "Let us consider one another" → INCLUSIVE

Based on theological context, predict clusivity:
- INCLUSIVE (speaker includes addressee)
- EXCLUSIVE (speaker excludes addressee)

Confidence: High/Medium/Low
Reasoning: [explain based on theological factors]
```

**Theological Categories That Drive Decisions**:
- Divine prerogatives → Restrict participation (EXCLUSIVE)
- Salvific experiences → Shared participation (INCLUSIVE)
- Authority structures → Limited participation (EXCLUSIVE)
- Community identity → Inclusive participation (INCLUSIVE)

## Level 2: Capability Analysis Prompt

If Level 1 doesn't resolve, check capability:

```
Capability Analysis for Clusivity:

Verse: {reference}
Speaker: {who is speaking}
Addressee: {who is being addressed}
Action/State: {what is described}
Pronoun: "{we/us/our}"

CAPABILITY TEST:

1. Identify the specific action or state described

2. Can the addressee perform/participate in this action?

   Questions to ask:
   - Is this within human capability? (walking, speaking, believing)
   - Is this a divine-only capability? (creating, omniscience, forgiveness of sins)
   - Is this role-specific? (apostolic witness, priestly service)
   - Is this a shared experience? (suffering, joy, faith)

3. Decision Rules:
   - If NO (addressee CANNOT participate) → EXCLUSIVE
   - If YES (addressee CAN participate) → Continue to Level 3

Result:
- Can addressee participate? Yes/No
- If No: EXCLUSIVE
- Confidence: High (95%+ for clear capability constraints)
- Reasoning: [explain capability constraint]
```

**Examples**:
- **Acts 2:32** "We are witnesses" → Can crowd witness resurrection? NO → EXCLUSIVE
- **Romans 5:1** "We have peace" → Can addressee have peace with God? YES → Check identity → INCLUSIVE
- **Genesis 1:26** "Let us make man" → Can heavenly beings create? NO (only God creates) → EXCLUSIVE

**Why Capability Works**:
- Objective criterion (less interpretive)
- Filters 60%+ of cases early
- Theologically sound (aligns with biblical theology of roles)
- LLM-friendly (modern LLMs understand capability constraints)

## Level 3: Discourse Function Prompt

If Levels 1-2 don't resolve, check discourse patterns:

```
Discourse Function Analysis:

Verse: {reference}
Genre: {Narrative/Epistle/Poetry/Prophecy/etc.}
Speaker: {identity}
Addressee: {identity}
Speech Act: {invitation/command/testimony/contrast/etc.}

DISCOURSE PATTERNS:

1. Check for explicit invitation:
   - "Come, let us..." → INCLUSIVE (90%+)
   - Example: Psalm 95:1

2. Check for direct contrast:
   - "We... but you..." → EXCLUSIVE (95%+)
   - Example: John 3:11 "We speak... you do not receive"

3. Check for reciprocal action:
   - "one another" → INCLUSIVE (100%)
   - Example: Hebrews 10:24

4. Check for epistolary structure:
   - Letter sender → recipient → EXCLUSIVE (90%+)
   - Example: Acts 15:25 "We send to you"

5. Check for prayer context:
   - To God → EXCLUSIVE of God (95%+)
   - Example: Matthew 6:9 "Our Father"

6. Check genre baseline:
   - Narrative (OT): 90%+ exclusive
   - Epistles (NT): 50/50 mixed
   - Prophecy: 90%+ exclusive
   - Worship/Praise: 80%+ inclusive

Based on discourse function:
- Predicted value: INCLUSIVE/EXCLUSIVE
- Confidence: High/Medium/Low
- Pattern matched: [which pattern from above]
```

## Level 4: Grammatical Cues

If Levels 1-3 don't resolve, check grammatical markers:

```
Grammatical Cue Analysis:

Verse: {reference}
Pronoun form: {we/us/our/let us}

Check for explicit markers:
- Hortatory subjunctive ("let us") → Check for invitation vs royal "we"
- Possessive form ("our") → Check relationship to noun
- Contrast markers ("but", "however") → Check for explicit exclusion

Note: In Biblical source languages, these cues are weak.
Rely primarily on Levels 1-3.

If grammatical cues present:
- Predicted value: ...
- Confidence: Low-Medium
- Reasoning: ...
```

## Level 5: Baseline Default

If no clear triggers from Levels 1-4:

```
Baseline Default:

Overall baseline: EXCLUSIVE (65% of first-person plurals)

Genre-specific baseline:
- Narrative: 90% exclusive
- Prophecy: 90% exclusive
- Epistles: 50% exclusive, 50% inclusive
- Poetry/Wisdom: 70% exclusive

Use genre baseline with LOW confidence (50-60%).
Flag for human review if high-stakes passage.
```

## Pattern Recognition

Once patterns are established, use pattern matching for efficiency:

```
Pattern Matching:

Known high-reliability patterns (95%+ accuracy):

Pattern 1: Divine Speech
- Context: Divine speaker, human addressee
- Action: Creation, judgment, divine knowledge
- Result: EXCLUSIVE
- Sample verses: Gen 1:26, Gen 3:22, Gen 11:7

Pattern 2: Prayer to God
- Context: Human speaker, divine addressee
- Pronoun refers to: Speaker and others
- Result: EXCLUSIVE (excludes God)
- Sample verses: Matt 6:9, Psalm 79:8

Pattern 3: Apostolic Witness
- Context: Apostle speaker, church addressee
- Action: Eyewitness testimony
- Result: EXCLUSIVE
- Sample verses: Acts 2:32, 1 John 1:1-3

Pattern 4: Worship Invitation
- Context: Believer speaker, believer addressee
- Speech act: "Come, let us..."
- Result: INCLUSIVE
- Sample verses: Psalm 95:1, Isaiah 2:3

Pattern 5: Reciprocal Action
- Context: "one another" construction
- Result: INCLUSIVE (100% reliable)
- Sample verses: Hebrews 10:24, Job 34:4

Current verse: {reference}
Does this match any established pattern? [Yes/No]
If yes, which pattern? [1-5 or other]
Predicted value based on pattern: [INCLUSIVE/EXCLUSIVE]
Confidence: High (based on pattern reliability)
```

## Multi-Method Validation

For maximum confidence, use multiple methods and check agreement:

```
Multi-Method Validation:

Verse: {reference}

Method 1: Theological Analysis → Prediction A: [INCL/EXCL]
Method 2: Capability Analysis → Prediction B: [INCL/EXCL]
Method 3: Discourse Function → Prediction C: [INCL/EXCL]

Agreement Check:
- 3/3 methods agree → 95%+ confidence
- 2/3 methods agree → 80% confidence
- 1/3 or 0/3 agree → Flag for human review, use baseline

Final Prediction:
- Value: [INCLUSIVE/EXCLUSIVE]
- Confidence: [High/Medium/Low]
- Agreement: [3/3 or 2/3 or 1/3]
- Reasoning: [summarize convergent evidence]
```

## Translation Validation

Always validate predictions against actual translations in clusivity-marking languages:

```
Translation Validation:

Predicted value: {INCLUSIVE/EXCLUSIVE} for {verse reference}

Check actual translations:
- Indonesian: {translation text} → Uses: kita (INCL) or kami (EXCL)?
- Tagalog: {translation text} → Uses: tayo (INCL) or kami (EXCL)?
- Tok Pisin: {translation text} → Uses: yumi (INCL) or mipela (EXCL)?
- {Other clusivity-marking language}

Validation Questions:
1. Do translations match prediction?
2. If not, what did translators choose?
3. What might explain the difference?
   - Misunderstood theological context?
   - Missed discourse factor?
   - Ambiguous case with multiple valid readings?
4. Should prediction be revised or documented as ambiguous?

Validation Result:
- Matches translations: Yes/No [X/Y matches]
- If no, revised prediction: ...
- If ambiguous, document both readings
```

## Confidence Levels

Assign confidence based on convergent evidence:

| Triggers | Confidence | Expected Accuracy |
|----------|------------|-------------------|
| 0 triggers (baseline only) | 30-50% | 65% (baseline rate) |
| 1 trigger (single method) | 60% | ~75% |
| 2 triggers (methods agree) | 80% | ~85% |
| 3+ triggers (strong convergence) | 95%+ | ~95%+ |
| Pattern match + convergence | 98%+ | ~98%+ |

**Achieved Results**:
- Person (Clusivity): 100% accuracy (11/11)
- All test cases had 2-3 triggers with high convergence

## Common Pitfalls to Avoid

**Pitfall 1**: Looking at translation before prediction
- **Problem**: Causes unconscious bias
- **Solution**: Blind testing - predict first, validate after

**Pitfall 2**: Ignoring genre patterns
- **Problem**: Narrative rules ≠ Epistle rules
- **Solution**: Always check genre baseline (Level 5)

**Pitfall 3**: Assuming all prayer is exclusive
- **Problem**: "God is with us" ≠ "Our Father who is in heaven"
- **Solution**: Check who is addressee vs who is referent

**Pitfall 4**: Missing speaker changes
- **Problem**: Not tracking when speaker shifts mid-passage
- **Solution**: Identify speaker for each "we" instance separately

**Pitfall 5**: Overconfidence on weak signals
- **Problem**: Single grammatical cue → high confidence
- **Solution**: Require 2-3 converging factors for high confidence

## Implementation Checklist

For ANY first-person plural pronoun in Biblical text:

1. ☐ Identify speaker and addressee
2. ☐ Run Level 1: Theological Analysis
3. ☐ If not resolved, run Level 2: Capability Analysis
4. ☐ If not resolved, run Level 3: Discourse Function
5. ☐ If not resolved, run Level 4: Grammatical Cues
6. ☐ If not resolved, apply Level 5: Baseline
7. ☐ Check for pattern match (efficiency boost)
8. ☐ Validate with 2-3 clusivity-marking translations
9. ☐ Assign confidence level
10. ☐ Document reasoning

## Transferability

This hierarchical framework applies to other grammatical features:

- **Aspect**: Perfective vs Imperfective → Prioritize action completion semantics
- **Mood**: Indicative vs Subjunctive → Prioritize speaker certainty/reality
- **Voice**: Active vs Passive → Prioritize agent focus and discourse prominence
- **Definiteness**: Definite vs Indefinite → Prioritize first mention vs anaphoric reference

**Key insight**: Always prioritize **meaning over form** (theological/semantic → discourse → grammar).

## Resources

- **Complete framework**: Sections 9-10 in [../TRANSFERABLE-LEARNINGS.md](../TRANSFERABLE-LEARNINGS.md)
- **Validation data**: [clusivity/](clusivity/) - 14 analyzed verses with 98% consensus
- **Language examples**: [clusivity/README.md](clusivity/README.md) - 9 clusivity-marking languages
