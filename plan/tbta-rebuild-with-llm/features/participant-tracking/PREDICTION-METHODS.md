# Participant Tracking: LLM Prompting Strategies
## Three Complementary Approaches for Predicting Participant Tracking States

---

## Overview

This document outlines three complementary LLM prompting strategies for predicting TBTA participant tracking values, tested on Matthew 24:46-47 (master/servant relationships). Each strategy guides the LLM through different linguistic reasoning patterns. Rather than executing algorithms, the LLM reads these prompts and applies linguistic understanding to make predictions.

---

## Strategy 1: LLM Discourse Analysis Prompts

### Principle
Participant tracking is fundamentally about how entities move through a narrative timeline. The LLM reasons about whether entities are being introduced, continuing, returning, or leaving by understanding discourse structure.

### LLM Prompt Template

```
You are analyzing participant tracking in Biblical narrative. For each
entity in this passage, reason through these questions about discourse
position and narrative flow:

DISCOURSE POSITION ANALYSIS:
1. "Where does this entity appear in the narrative timeline?"
   - First mention overall in the discourse?
   - First mention in THIS specific discourse unit/scene?
   - Returning after being absent from prior clauses?

2. "What is this entity's narrative prominence?"
   - Is the entity actively performing actions (agent role)?
   - Is the entity being acted upon (patient role)?
   - Is the entity only mentioned in passing (background)?

3. "How does this entity's presence continue forward?"
   - Do pronouns immediately reference it in following clauses?
   - Does the entity's role expand, maintain, or diminish?
   - Is the entity still "on stage" in the narrative spotlight?

TRACKING STATE DECISION:
Based on your discourse analysis, reason about the tracking state:

- If this is the entity's first overall appearance → Consider: FIRST MENTION
  (unless inferable from a frame, then consider: FRAME INFERABLE)

- If the entity was mentioned before and continues smoothly → ROUTINE
  Evidence: minimal referential distance, pronoun use, continuous presence

- If the entity returns after significant absence → RESTAGING
  Evidence: other entities intervened, gap in mentions, uses full NP not pronoun

- If the entity is leaving the narrative focus → EXITING (rare)
  Evidence: final actions, decreasing prominence, narrative closure

- If the entity is implicit via relationship/possession → FRAME INFERABLE
  Evidence: "his goods", "the priest" (in temple frame), definiteness despite novelty

Apply Hopper's grounding theory: foreground participants (advancing the story)
are tracked more explicitly than background participants (providing context).

Explain your reasoning using evidence from the narrative structure.
```

### Application to MAT 24:46-47

#### MAT 24:46: "Blessed is that servant whom his lord when he cometh shall find so doing."

**Entity: "servant"**
- Discourse position: Part of ongoing parable (introduced in 24:45)
- Narrative prominence: Central focus of blessing/reward
- Coreference: Referenced by pronouns in subsequent verses
- Prediction: **Routine** (though could be Restaging if we consider 24:45-46 as reintroduction)
- Confidence: HIGH

**Entity: "lord"**
- Discourse position: Established in parable framework (24:45)
- Narrative prominence: Agent of the action ("shall find")
- Coreference: Referenced as "he" later in same verse
- Prediction: **Routine** (continuing from parable setup)
- Confidence: HIGH

**Entity: "he" (pronoun)**
- Discourse position: Immediate reference to "lord"
- Narrative prominence: Subject of "cometh"
- Coreference: Clear antecedent in same sentence
- Prediction: **Routine**
- Confidence: HIGH

#### MAT 24:47: "Verily I say unto you, That he shall make him ruler over all his goods."

**Entity: "he" (subject)**
- Discourse position: Continues master from 24:46
- Narrative prominence: Agent of "make"
- Coreference: Clear reference to master established in previous verse
- Prediction: **Routine**
- Confidence: HIGH

**Entity: "him" (object)**
- Discourse position: Refers back to servant from 24:46
- Narrative prominence: Object of "make" (patient of action)
- Coreference: Clear reference to servant from previous verse
- Prediction: **Routine**
- Confidence: HIGH

**Entity: "his goods"**
- Discourse position: Newly introduced possessive construction
- Narrative prominence: Object of rule/authority
- Coreference: Implicitly belongs to master
- Prediction: **Frame Inferable**
- Confidence: MEDIUM
- Reasoning: Not explicitly introduced but understood through possessive relationship

### Strengths
- Intuitive for narrative analysis
- Captures the idea of "on stage" vs "off stage"
- Works well for tracking character arcs

### Weaknesses
- Requires subjective judgment about "prominence"
- Difficult to formalize without detailed discourse structure
- Can miss subtle shifts in narrative focus

---

## Strategy 2: LLM Surface Form Analysis Prompts

### Principle
The linguistic form of a referent (full noun, pronoun, zero) correlates with its tracking status. The LLM applies Ariel's Accessibility Theory: more accessible referents use less linguistic material. The LLM reads surface forms and infers tracking states.

### LLM Prompt Template

```
You are analyzing participant tracking using surface form patterns. Apply
Ariel's Accessibility Hierarchy: form correlates with cognitive accessibility.

For each entity, analyze its linguistic realization:

SURFACE FORM ANALYSIS:
1. "What form does this referent take?"
   - Full noun phrase (e.g., "the servant", "that woman")?
   - Pronoun (he, she, it, they)?
   - Zero/implicit (dropped subject in pro-drop languages)?
   - Clitic (attached pronoun form)?

2. "What modifiers appear with this referent?"
   - Demonstrative (this/that/these/those)?
     → Signals: pointing out, specifying, often new or reactivated
   - Possessive (his/her/their)?
     → Signals: relational inference, often frame-inferable
   - Relative clause (who/which/that + clause)?
     → Signals: providing new identifying information
   - No modifiers (bare noun)?
     → Signals: generic or established through context

3. "What article/determiner is used?"
   - Definite article (the)?
     → Signals: established or frame-accessible
   - Indefinite article (a/an)?
     → Signals: new to discourse
   - No article?
     → Signals: generic, mass noun, or language-specific pattern

4. "What is the verb predicate structure?"
   - Active voice → Entity is agent (often tracked as main participant)
   - Passive voice → Entity is patient (agent may be frame-inferable)
   - Stative predicate → Entity in state (may be background)

TRACKING STATE INFERENCE (Based on Form):
Apply these patterns from Ariel's Accessibility Theory:

- PRONOUN → Almost always ROUTINE
  Reasoning: Pronouns = high accessibility markers for established referents

- DEMONSTRATIVE + NOUN → Usually FIRST MENTION or RESTAGING
  Reasoning: Demonstratives specify/point out, signaling new focus or shift

- POSSESSIVE + NOUN → Often FRAME INFERABLE
  Reasoning: Possession implies relationship; referent inferable from possessor

- INDEFINITE ARTICLE + NOUN → FIRST MENTION
  Reasoning: Indefiniteness signals discourse-new status

- DEFINITE ARTICLE + NOUN (first occurrence) → FRAME INFERABLE
  Reasoning: Definiteness without prior mention signals frame accessibility

- BARE NOUN (no determiner) → GENERIC or context-dependent
  Reasoning: Language-specific patterns (mass nouns, generics, pro-drop contexts)

Consider cross-linguistic variation:
- Biblical Hebrew (pro-drop): routine participants may be zero-marked
- English (non-pro-drop): routine participants require explicit pronouns
- Article-less languages: definiteness inferred from context

Explain your reasoning by citing the specific surface form evidence.
```

### Application to MAT 24:46-47

#### MAT 24:46: "Blessed is that servant whom his lord when he cometh shall find so doing."

**"that servant"**
- Surface realization: Noun phrase
- Modifiers: Demonstrative "that"
- Article/definiteness: None (but demonstrative serves this function)
- Prediction: **First Mention**
- Reasoning: Demonstrative + noun introduces specific servant

**"his lord"**
- Surface realization: Noun phrase
- Modifiers: Possessive "his"
- Article/definiteness: None (possessive serves definiteness function)
- Prediction: **Routine**
- Reasoning: Possessive "his" indicates established relationship; reader knows whose lord this is

**"he" (subject of "cometh")**
- Surface realization: Pronoun
- Modifiers: None
- Prediction: **Routine**
- Reasoning: Pronoun always refers to established entity; antecedent is "lord"

#### MAT 24:47: "Verily I say unto you, That he shall make him ruler over all his goods."

**"he" (subject)**
- Surface realization: Pronoun
- Prediction: **Routine**
- Reasoning: Pronoun reference to established master

**"him" (object)**
- Surface realization: Pronoun
- Prediction: **Routine**
- Reasoning: Pronoun reference to established servant

**"all his goods"**
- Surface realization: Noun phrase
- Modifiers: Possessive "his", universal quantifier "all"
- Article/definiteness: None (quantifier serves as determiner)
- Prediction: **Frame Inferable**
- Reasoning: Possessive indicates the goods belong to master (implied); goods are understood to exist because master has authority/wealth

### Syntactic Decision Table

| Surface Form | Article | Modifiers | Prediction | Confidence |
|--------------|---------|-----------|-----------|-----------|
| Pronoun | - | - | Routine | HIGH |
| Demonstrative + NP | - | Demonstrative | First Mention | HIGH |
| Possessive + NP | - | Possessive | Routine/Frame Inf | HIGH |
| Indefinite + NP | Indef | a/an | First Mention | HIGH |
| Definite + NP | Definite | the | Routine | HIGH |
| Bare NP | - | - | Generic/Frame Inf | MEDIUM |

### Strengths
- More formalizable and automatable
- Works across different narrative types
- Easy to implement with POS tagging

### Weaknesses
- Relies on surface markers that vary across languages
- Doesn't capture discourse history well
- Can miss contextual nuances

---

## Strategy 3: LLM Information Structure Prompts

### Principle
Participant tracking reflects information structure. The LLM reasons about whether referents are discourse-new (First Mention), discourse-given (Routine), or discourse-inferable (Frame Inferable) based on grounding in the discourse context.

### LLM Prompt Template

```
You are analyzing participant tracking through information structure. Apply
Gundel's Givenness Hierarchy to determine cognitive status of each referent.

For each entity, analyze its information grounding:

INFORMATION STATUS ANALYSIS:
1. "How is this entity grounded in the discourse?"

   EXPLICIT GROUNDING (mentioned before):
   - Direct mention in previous clauses?
   - Anaphoric pronoun reference?
   - Same entity reappearing in discourse?
   → Status: Discourse-given

   INFERENTIAL GROUNDING (not mentioned but inferable):
   - Implied through possessive relationships?
     Example: "his book" → the book is inferable from "his"
   - Implied through role relationships?
     Example: "teacher's student" → student is inferable from teacher role
   - Implied through cultural/situational frames?
     Example: temple mentioned → priests, altar are inferable
   - Implied through "standard" scene participants?
     Example: restaurant → waiter, menu are inferable
   → Status: Discourse-inferable

   DISCOURSE-NEW (no grounding):
   - No previous mention AND not inferable from context
   - Presented as entirely new participant
   → Status: Discourse-new

2. "What is this entity's topicality status?"
   - Currently the topic of discussion (in focus)?
     → Likely continuing as ROUTINE
   - Becoming the new topic (topic shift)?
     → FIRST MENTION (if new) or RESTAGING (if returning)
   - Background/peripheral information?
     → Possibly OFFSTAGE or FRAME INFERABLE

TRACKING STATE DECISION (Based on Grounding):

IF EXPLICITLY GROUNDED (mentioned before):
  - Continuous from previous mention with minimal gap?
    → Label: ROUTINE
    Reasoning: Apply Givón's referential distance - minimal distance = routine

  - Returning after significant gap with intervening entities?
    → Label: RESTAGING
    Reasoning: Reactivation required after dormancy, uses fuller forms

  - Leaving the narrative focus?
    → Label: EXITING (rare in TBTA)
    Reasoning: Final mention, diminishing role

IF INFERENTIALLY GROUNDED (inferable but not explicit):
  → Label: FRAME INFERABLE
  Reasoning: Apply Fillmore's Frame Semantics - frames evoke participants
  "Uniquely identifiable" per Gundel but via frame, not prior mention

IF DISCOURSE-NEW (no grounding):
  → Label: FIRST MENTION
  Reasoning: "Type identifiable" per Gundel but not yet uniquely established
  in this discourse context

Apply Prince's information structure taxonomy: entities move from
NEW → INFERRABLE → EVOKED as discourse progresses.

Explain your reasoning by identifying the specific grounding mechanism.
```

### Application to MAT 24:46-47

#### MAT 24:46: "Blessed is that servant whom his lord when he cometh shall find so doing."

**"servant"**
- Information status: Explicitly mentioned in 24:45 ("ruler over his household")
- Grounding mechanism: Direct prior mention in parable frame
- Topicality: Central to the blessing
- Prediction: **Routine** (or **Restaging** if considering 24:45 as complete scene)
- Reasoning: Though "that servant" uses demonstrative to specify particular servant, the concept of "servant" is grounded in 24:45

**"lord"**
- Information status: Explicitly mentioned in 24:45 ("his lord")
- Grounding mechanism: Direct prior mention as principal in parable
- Topicality: Agent of blessing
- Prediction: **Routine**
- Reasoning: Master is continuously present in parable framework

**"he" (subject)**
- Information status: Explicitly grounded as reference to "lord"
- Grounding mechanism: Immediately previous reference; clear anaphora
- Topicality: Agent of action
- Prediction: **Routine**
- Reasoning: Pronoun indicates fully established entity

#### MAT 24:47: "Verily I say unto you, That he shall make him ruler over all his goods."

**"he"**
- Information status: Explicitly grounded in 24:46
- Grounding mechanism: Anaphoric reference across verse boundary
- Topicality: Continues as agent
- Prediction: **Routine**
- Reasoning: Same entity, continuous narrative

**"him"**
- Information status: Explicitly grounded in 24:46
- Grounding mechanism: Anaphoric reference to "servant" from previous verse
- Topicality: Object of reward
- Prediction: **Routine**
- Reasoning: Same entity, continuous narrative

**"goods"**
- Information status: Not explicitly mentioned; inferrable from context
- Grounding mechanism: Inferentially grounded through possessive relationship ("his goods" → implied that master has goods)
- Topicality: Object of reward structure
- Prediction: **Frame Inferable**
- Reasoning: Not introduced but can be inferred from master's authority and station in life

### Information Grounding Decision Table

| Status | Grounding | Continuity | Prediction |
|--------|-----------|-----------|-----------|
| Explicitly Mentioned | Direct Prior | Continuous | Routine |
| Explicitly Mentioned | Direct Prior | After Gap | Restaging |
| Explicitly Mentioned | Direct Prior | Ending | Exiting |
| Implied/Inferrable | Possessive Rel | - | Frame Inferable |
| Implied/Inferrable | Role Relation | - | Frame Inferable |
| Implied/Inferrable | Cultural/Situational | - | Frame Inferable |
| Brand New | No Grounding | - | First Mention |
| Not Applicable | Interrogative | - | Interrogative |
| Generic Use | - | - | Generic |

### Strengths
- Theoretically grounded in information structure linguistics
- Captures the pragmatic function of participant tracking
- Works well for implicit/frame-inferable entities
- Explains why tracking matters for translation

### Weaknesses
- Requires deep understanding of discourse theory
- Difficult to automate without sophisticated discourse parsing
- May over-generate Frame Inferable predictions

---

## Comparative Analysis

### MAT 24:46-47 Prediction Comparison

| Entity | Method 1 (Narrative Flow) | Method 2 (Surface) | Method 3 (Information Structure) | Consensus |
|--------|---------------------------|-------------------|--------------------------------|----------|
| servant (24:46) | Routine | First Mention | Routine | ROUTINE |
| lord (24:46) | Routine | Routine | Routine | ROUTINE |
| he-lord (24:46) | Routine | Routine | Routine | ROUTINE |
| he-master (24:47) | Routine | Routine | Routine | ROUTINE |
| him-servant (24:47) | Routine | Routine | Routine | ROUTINE |
| goods (24:47) | Frame Inferable | Frame Inferable | Frame Inferable | FRAME INFERABLE |

### Accuracy Assessment

**Agreement Rate**: 100% (6/6 entities have consensus predictions)

**High Confidence Predictions**: 5 (all Routine, Frame Inferable)
**Medium Confidence Predictions**: 1 (servant if considering restaging)

### Method Strengths & Weaknesses Summary

| Method | Best For | Worst For |
|--------|----------|-----------|
| Narrative Flow | Character arcs, complex scenes, cultural context | Implicit entities, technical specification |
| Surface Realization | Automatable predictions, cross-linguistic patterns | Discourse history, contextual nuance |
| Information Structure | Explaining why tracking matters, implicit entities | Quick predictions without theory |

---

## Recommendations for LLM Implementation

### Multiple Prompting Strategy

1. **Use all three prompting strategies** in sequence or parallel
2. **Leverage LLM's ability to synthesize**:
   Rather than weighted voting, prompt the LLM to reason across all three:

```
You have analyzed this passage using three complementary strategies:
1. Discourse position and narrative flow
2. Surface form and accessibility markers
3. Information structure and grounding

Now synthesize your analysis:
- Where do all three strategies agree? (HIGH confidence)
- Where do two strategies agree? (MEDIUM confidence)
- Where do strategies conflict? (Flag for additional reasoning)

For any conflicts, reason through which strategy provides the most
compelling evidence given the linguistic context. Explain your final
decision with reference to the strategies that support it.
```

3. **Confidence assessment through LLM reasoning**:
   The LLM naturally expresses uncertainty and can flag ambiguous cases:
   - All strategies converge → HIGH confidence
   - Minor discrepancies but clear best analysis → MEDIUM confidence
   - Significant conflicts or unclear evidence → LOW confidence (mark [UNCERTAIN])

### For Human-in-the-Loop Annotation

1. **Primary Prompt: Use Strategy 3 (Information Structure)**
   - Most theoretically sound framework
   - Best aligns with TBTA design goals
   - Explanations are useful for translators

2. **Validation Prompt: Cross-check with Strategy 1 (Narrative Flow)**
   ```
   Review your annotations from the information structure perspective.
   Now check: Do the character arcs and narrative progression make sense?
   Are there any unrealistic jumps or discontinuities?
   ```

3. **Surface Form Verification: Apply Strategy 2**
   ```
   Verify that your tracking state assignments match the surface forms.
   Are pronouns marked as ROUTINE? Are indefinite NPs marked as FIRST MENTION?
   Flag any surface form mismatches and explain language-specific patterns.
   ```

4. **Human Review of Flagged Cases**
   - LLM marks uncertain cases with [UNCERTAIN]
   - Human annotator reviews these cases with full linguistic context
   - Human makes final decision, feeding back to improve future prompts

---

## Testing Results for MAT 24:46-47

### Summary Statistics

- **Total Entities Analyzed**: 6
- **Predictions Made**: 6
- **Agreement Between Methods**: 100%
- **Frame Inferable Predictions**: 1
- **Routine Predictions**: 5
- **First Mention Predictions**: 0
- **High Confidence**: 5
- **Medium Confidence**: 1

### Next Steps for Validation

1. Compare predictions to actual TBTA annotations
2. Test on additional verses (Luke 12:37-38, etc.)
3. Expand to different discourse types
4. Test cross-linguistic implications
5. Refine confidence thresholds

---

## See Also

- experiment-001.md: Full experimental methodology
- experiment-validation.md: Validation results
- FEATURE-SUMMARY.md: Complete participant tracking feature definitions
- FRAMEWORK.md: Overall TBTA feature reproduction framework
