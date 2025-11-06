# Participant Tracking: Initial Reproduction Thesis

**Date**: 2025-11-05
**Feature**: Noun Participant Tracking
**TBTA States**: 9 defined, 5 actively used
**Data Analyzed**: 171,875 annotations from TBTA database export

---

## Executive Summary

Participant tracking can be reproduced with **high accuracy (estimated 85-90%)** using a combination of:
1. Coreference resolution
2. Referential distance calculation
3. Frame semantics / FrameNet integration
4. Generic reference detection
5. Interrogative clause identification

The key insight: **Only 5 states are actively needed** for Biblical text (Routine, Generic, Frame Inferable, First Mention, Interrogative). The other 4 states (Integration, Exiting, Restaging, Offstage) are either theoretical or extremely rare.

---

## Core Algorithm (5-State Simplified System)

### State 1: ROUTINE (73% of cases)
**When to use**: Referent mentioned in last 1-3 clauses with low competing referents

**LLM Prompt for Detection**:
```
For this referent, ask yourself:
1. "Was this referent mentioned recently (within last 1-3 clauses)?"
2. "Are there few competing referents between mentions?"
3. "Is this referent maintaining continuous presence in the discourse?"

If YES to all three → Label as ROUTINE

Reasoning: Apply Givón's continuity principle - continuous topics require
minimal linguistic marking. This referent is "in focus" per Gundel's
hierarchy, maintaining high accessibility per Ariel's scale.
```

**Validation**: Most common state. If you're getting <60% Routine, something is wrong.

**Surface forms**:
- Pronouns (he, she, it, they)
- Zero anaphora in pro-drop languages
- Repeated full nouns when necessary for clarity

---

### State 2: GENERIC (14% of cases)
**When to use**: Reference to types/classes, not specific individuals; timeless statements

**LLM Prompt for Detection**:
```
For this referent, ask yourself:
1. "Is this statement timeless, or about a specific event?"
2. "Does this refer to a type/class or a particular individual?"
3. "Is this making a general claim or describing a specific action?"

Generic indicators to look for:
- Timeless present tense ("Lions are dangerous")
- Habitual aspect ("A man goes to work daily")
- Definitional statements ("Water is H₂O")
- Bare plurals ("Dogs bark")
- Proverbial/wisdom context

If the statement is about classes/types → Label as GENERIC
If the statement is about a specific entity in time → Continue checking other states

Reasoning: Generic references are not tracked as individual participants.
They make claims about categories, not about specific discourse referents.
```

**Indicators**:
- Timeless present tense ("Lions are dangerous")
- Habitual aspect ("A man goes to work daily")
- Definitions ("Water is H₂O")
- Bare plurals in English ("Dogs bark")
- Generic singulars ("The lion is a mammal")
- Proverbs/wisdom statements

**Common in**: Wisdom literature, teaching passages, parables, explanatory material

---

### State 3: FRAME INFERABLE (7.5% of cases)
**When to use**: First occurrence BUT inferable from established scene/frame

**LLM Prompt for Detection**:
```
For this referent appearing for the first time, ask yourself:
1. "Has a frame/scene been established in prior context?"
   (e.g., restaurant, temple, well, market, creation, etc.)
2. "Is this referent a typical participant in that frame?"
3. "Does the text use definite marking despite first mention?"
   (e.g., "the waiter" without previously mentioning waiter)

Frame examples:
- Restaurant frame → waiter, menu, food, bill are inferable
- Well frame → water, bucket, rope are inferable
- Temple frame → altar, priest, sacrifice are inferable
- Creation frame → heaven, earth, light are inferable

If frame is active AND referent belongs to it → Label as FRAME INFERABLE
If no active frame → Label as FIRST MENTION

Reasoning: Apply Fillmore's Frame Semantics - certain words evoke frames
that make their typical participants accessible even without explicit mention.
This is "uniquely identifiable" per Gundel's hierarchy via frame inference.
```

**Key test**: Definite article on first mention
- "John went to a restaurant. **The waiter** was rude."
- "In the beginning God created **the heavens** and **the earth**."

**Requires**: Frame/scene database
- Restaurant → waiter, menu, food, bill
- Market → vendors, goods, prices
- Well → water, bucket, rope
- Creation → heaven, earth, light, darkness
- Temple → altar, priest, sacrifice

**Genesis 1:1 example**: "heaven" and "earth" are frame-inferable from "creation" frame, despite being first mentions.

---

### State 4: FIRST MENTION (5.4% of cases)
**When to use**: Truly new referent, not inferable from frame

**LLM Prompt for Detection**:
```
For this referent, ask yourself:
1. "Is this the first time this referent appears in the discourse?"
2. "Is it NOT inferable from any established frame?"
3. "Does it use indefinite marking (e.g., 'a woman', 'a man')?"

If YES to all three → Label as FIRST MENTION

Reasoning: Apply Ariel's Accessibility Theory - new referents require
"low accessibility markers" (full NPs with indefinite articles) because
they haven't been activated in the discourse model. This is "type identifiable"
per Gundel's hierarchy - we know the type (woman) but not the specific individual yet.

Surface form expectations:
- Indefinite article ("a woman")
- Existential construction ("there was a man")
- Full noun phrase with no prior context
```

**Surface forms**:
- Indefinite article in English ("a woman")
- Existential constructions ("there was a man")
- Full noun phrases with no prior context

**Common pattern**: New participants entering narrative

---

### State 5: INTERROGATIVE (0.2% of cases)
**When to use**: Referent in interrogative clause querying identity/properties

**LLM Prompt for Detection**:
```
For this referent, ask yourself:
1. "Is this referent part of an interrogative clause (question)?"
2. "Is the identity or properties of this referent being queried?"
3. "Does this use a wh-word (who, what, which, whom, whose)?"

If YES → Label as INTERROGATIVE

Note: Only the questioned referent gets this label, not all referents
in a question. Example: "Who saw the woman?" - "who" is INTERROGATIVE,
but "woman" is ROUTINE or FIRST MENTION depending on context.

Reasoning: Interrogatives mark information structure - they signal
"unknown" or "requested" information. The referent is in focus but
informationally incomplete.
```

**Indicators**:
- Wh-words: who, what, which, whom, whose
- Question context
- Querying participant identity or properties

**Note**: Only for the questioned referent, not all referents in a question

---

## Rare/Theoretical States (Not Needed for Initial Implementation)

### RESTAGING (0% in data)
**Theoretical use**: Participant returns after 4+ clause absence with high interference

**Why absent**: Biblical narrative maintains tight participant focus; few long absences

**If implementing**:
```python
if referential_distance >= 4 and competing_referents >= 3:
    return "Restaging"
```

**Likely surface form**: Full NP (not pronoun), possibly with demonstrative

---

### OFFSTAGE (1 instance total!)
**Single example**: "Samaritan" in John 4:7 modifying "woman"

**When to use**: Referent in attributive position providing background, not acting

**Detection**:
```python
if is_attributive_modifier(referent) and not is_main_argument(referent):
    return "Offstage"
```

**Recommendation**: Skip this state initially. Use Generic or omit tracking for modifiers.

---

### INTEGRATION (0% in data)
**Theoretical**: Participant transitioning from peripheral to central

**Recommendation**: Not needed. Use First Mention → Routine transition directly.

---

### EXITING (0% in data)
**Theoretical**: Participant departing narrative

**Recommendation**: Not needed. Last mention is simply last Routine instance.

---

## LLM Prediction Workflow

### Phase 1: Minimum Viable System (3 States)
Focus on the big three that cover 95% of cases:

1. **Routine** (73%)
2. **Generic** (14%)
3. **First Mention** (5.4%)

Combined: 92.4% coverage

**LLM Prompting Approach**:
```
Given a Biblical passage, prompt the LLM:

"For each nominal constituent in this passage, determine its
participant tracking state using these steps:

STEP 1: Check if GENERIC
Ask: Is this a timeless statement about types/classes?
Look for: bare plurals, habitual aspect, definitional contexts
If YES → Label: GENERIC

STEP 2: Check if FIRST MENTION (for non-generic referents)
Ask: Is this the first occurrence in the discourse?
Look for: indefinite article, new participant introduction
If YES → Label: FIRST MENTION

STEP 3: Default to ROUTINE (for previously mentioned)
Ask: Has this referent appeared before?
Look for: pronouns, repeated nouns, continued reference
If YES → Label: ROUTINE

Provide your reasoning for each decision using linguistic evidence
from the text."

This simple 3-state system achieves 92.4% coverage and establishes
the foundation for more complex tracking.
```

---

### Phase 2: Add Frame Inferability (4 States)
Add 7.5% more coverage:

4. **Frame Inferable** (7.5%)

Total: 99.9% coverage

**Requirements**:
- Provide LLM with frame knowledge (FrameNet concepts)
- Include examples of common Biblical frames
- Guide frame-participant inference

**Enhanced LLM Prompting**:
```
"For each nominal constituent, determine tracking state:

STEP 1: Check if GENERIC (timeless/type reference)
→ If YES: GENERIC

STEP 2: For first occurrences, check FRAME INFERABILITY
Ask yourself:
- 'What frame/scene has been established in prior context?'
- 'Is this referent a typical participant in that frame?'
- 'Does the text use definite marking despite first mention?'

Common Biblical frames:
- Temple frame (altar, priest, sacrifice, incense)
- Well frame (water, bucket, rope)
- Market frame (vendor, goods, prices)
- Creation frame (heaven, earth, light, darkness)
- Household frame (master, servant, goods, authority)

If frame is active AND referent belongs to it → FRAME INFERABLE
If no frame connection → FIRST MENTION

STEP 3: For previously mentioned → ROUTINE

Explain which frame (if any) makes each referent inferable."

This 4-state system covers 99.9% of active TBTA annotations.
```

---

### Phase 3: Add Interrogatives (5 States)
Add remaining 0.2%:

5. **Interrogative** (0.2%)

Total: 100% of active states

**Complete LLM Prompting**:
```
"For each nominal constituent, determine tracking state:

STEP 0: Check if INTERROGATIVE
Ask: Is this referent in a question querying identity/properties?
Look for: wh-words (who, what, which, whom, whose)
→ If YES: INTERROGATIVE (only for the queried referent itself)

STEP 1: Check if GENERIC
Ask: Is this a timeless statement about types/classes?
→ If YES: GENERIC

STEP 2: For first occurrences, check FRAME INFERABILITY
Ask: Is there an active frame that makes this referent inferable?
→ If frame is active: FRAME INFERABLE
→ If no frame: FIRST MENTION

STEP 3: For previously mentioned
→ ROUTINE

This complete 5-state system covers 100% of TBTA's active annotations."
```

---

## Key Dependencies

### 1. Coreference Resolution
**What**: Identify when different mentions refer to same entity

**Challenges**:
- Pronouns → antecedents
- Synonyms ("the woman" = "the Samaritan")
- Name variants ("Jesus" = "He" = "the Nazarene" = "the Teacher")

**Solutions**:
- Use existing NLP tools (SpaCy, CoreNLP)
- Build referent chains
- Track across clause boundaries

**Critical for**: Distinguishing First Mention from Routine

---

### 2. Referential Distance (RD)
**What**: Count clauses between mentions of same referent

**Formula**:
```
RD = current_clause_number - last_mention_clause_number
```

**Usage**:
- RD = 1-2 → Routine
- RD = 3+ → Consider Restaging (but rarely needed)

**Critical for**: Routine vs. Restaging distinction

---

### 3. Frame Semantics Database
**What**: Map frame-evoking words to expected participants

**Example frames**:

```yaml
restaurant:
  evoking_words: [restaurant, cafe, diner, eatery]
  participants: [waiter, waitress, server, menu, food, table, bill, cook, chef]

well:
  evoking_words: [well, spring, cistern]
  participants: [water, bucket, rope, draw]

market:
  evoking_words: [market, marketplace, bazaar, souk]
  participants: [vendor, merchant, goods, wares, price, buyer, stall]

temple:
  evoking_words: [temple, sanctuary, tabernacle, altar]
  participants: [priest, sacrifice, offering, altar, incense, holy]

creation:
  evoking_words: [beginning, create, creation]
  participants: [heaven, earth, sky, light, darkness, land, sea]
```

**Sources**:
- FrameNet (computational resource)
- Manual curation for Biblical frames
- Learn from TBTA examples

**Critical for**: Frame Inferable detection

---

### 4. Generic Reference Detection
**What**: Identify non-specific, type-level reference

**Indicators**:

**Syntactic**:
- Bare plurals in English ("Lions are dangerous")
- Generic singular with definite article ("The lion is dangerous")
- Timeless present tense

**Semantic**:
- Habitual aspect
- Definitional statements
- Universal quantifiers (all, every, any)
- Proverbs and wisdom sayings

**Clause-level features**:
- Gnomic aspect (timeless truth)
- No specific time reference
- Generic subject → generic object typically

**Challenges**:
- Context-dependent (same form can be specific or generic)
- "The water is essential" (generic) vs. "The water is cold" (specific)

**Critical for**: Separating Generic from all other states

---

### 5. Clause Segmentation
**What**: Divide text into clauses (independent and dependent)

**Why important**: Referential distance measured in clauses, not sentences or words

**Challenges**:
- Identifying clause boundaries
- Handling embedded clauses
- Distinguishing independent from dependent

**Solutions**:
- Dependency parsing
- Identify predicates (verbs)
- Tree structure analysis

---

## Validation Approach

### Test 1: Frequency Distribution
**TBTA Baseline**:
- Routine: 73.0%
- Generic: 13.9%
- Frame Inferable: 7.5%
- First Mention: 5.4%
- Interrogative: 0.2%

**Validation**:
If your distribution is vastly different (e.g., 50% First Mention), you have systematic errors.

**Acceptable ranges** (based on narrative text):
- Routine: 60-80%
- Generic: 5-20% (genre-dependent: low in narrative, high in wisdom/teaching)
- Frame Inferable: 5-10%
- First Mention: 3-8%
- Interrogative: 0-2%

---

### Test 2: Surface Form Consistency
**Check**: Do surface forms match expected patterns for each state?

| State | Expected Surface | Problem if... |
|-------|-----------------|---------------|
| First Mention | Indefinite NP ("a woman") | Pronoun ("she") |
| Routine | Pronoun, zero, or repeated NP | Indefinite NP ("a man" when already mentioned) |
| Frame Inferable | **Definite** NP on first mention | Indefinite article |
| Generic | Bare plural, generic singular | Specific demonstrative ("this dog") |
| Interrogative | Wh-word | Not in question |

**Implementation**:
```python
def validate_surface_form(state, surface_form, article):
    if state == "First Mention" and article == "definite":
        warn("First Mention usually indefinite")
    if state == "Frame Inferable" and article == "indefinite":
        warn("Frame Inferable should be definite")
    if state == "Routine" and surface_form == "full_np" and article == "indefinite":
        error("Routine should not be indefinite")
```

---

### Test 3: Referent Chain Continuity
**Check**: Does each referent chain follow logical progression?

**Valid patterns**:
1. First Mention → Routine → Routine → Routine
2. First Mention → Routine → [gap] → Restaging → Routine
3. Frame Inferable → Routine → Routine

**Invalid patterns**:
1. Routine → First Mention (can't be routine if never mentioned!)
2. Frame Inferable → First Mention (can't be both)
3. Generic → Routine (generic refs don't become specific tracked participants)

**Implementation**:
```python
def validate_referent_chain(mentions):
    for i in range(len(mentions)):
        current = mentions[i]

        # First in chain must be First Mention or Frame Inferable
        if i == 0 and current not in ["First Mention", "Frame Inferable", "Generic"]:
            error("Chain must start with introduction")

        # Can't have First Mention after Routine for same referent
        if i > 0 and current == "First Mention":
            error("First Mention must be first in chain")
```

---

### Test 4: Frame Consistency
**Check**: Are frame inferables actually inferable from prior frames?

**For each Frame Inferable**:
1. Look back in context for frame-evoking word
2. Check if current referent is expected participant of that frame
3. If no frame found → Should be First Mention, not Frame Inferable

**Example**:
✅ "John went to the **restaurant**. The **waiter** approached."
   → "waiter" is frame-inferable from "restaurant"

❌ "John walked down the street. The **waiter** approached."
   → "waiter" has no frame context, should be First Mention

---

## Expected Accuracy Rates

Based on the systematic approach outlined:

| State | Expected Accuracy | Confidence |
|-------|------------------|------------|
| Routine | 90-95% | High - clear patterns |
| Generic | 75-85% | Medium - context-dependent |
| First Mention | 85-90% | High - clear introduction |
| Frame Inferable | 70-80% | Medium - requires frame DB |
| Interrogative | 95-99% | High - syntactic marker |

**Overall System Accuracy**: 85-90%

**Main Error Sources**:
1. Generic vs. specific ambiguity
2. Frame database incompleteness
3. Coreference resolution failures
4. Clause boundary errors

---

## LLM-Based Annotation Plan

### Week 1: Foundation Prompts
- [ ] Develop core prompts for 3-state system (Routine, Generic, First Mention)
- [ ] Test prompts on Genesis 1 (31 verses)
- [ ] Refine prompts based on LLM output quality
- [ ] Establish prompt template structure

### Week 2: Validation and Refinement
- [ ] Add self-validation prompts (referential distance checks)
- [ ] Test on John 4 (54 verses)
- [ ] Compare LLM predictions to TBTA gold standard
- [ ] Identify patterns in LLM errors (generic vs. specific confusion, etc.)
- [ ] Refine prompts to address error patterns

### Week 3: Frame Semantics Integration
- [ ] Develop frame identification prompts
- [ ] Provide LLM with common Biblical frame examples
- [ ] Add Frame Inferable detection to prompts
- [ ] Test on narrative passages (Ruth, Jonah)
- [ ] Expand frame examples based on LLM performance

### Week 4: Complete System and Validation
- [ ] Add Interrogative detection prompts
- [ ] Implement multi-pass validation workflow (initial → validation → refinement)
- [ ] Run complete system on Mark (16 chapters)
- [ ] Compare results with TBTA annotations systematically
- [ ] Document edge cases where LLM reasoning differs from TBTA

### Week 5: Scale and Quality Assurance
- [ ] Process entire New Testament using refined prompts
- [ ] Calculate precision/recall per state
- [ ] Identify passages where LLM marks [UNCERTAIN]
- [ ] Build quality assurance workflow using LLM self-checking
- [ ] Create annotation guidelines based on successful prompts

---

## Edge Cases & Challenges

### Challenge 1: Pronouns in Biblical Hebrew
**Problem**: Hebrew is pro-drop; subjects often implicit in verb morphology

**TBTA Solution**: Marks implicit subjects as Routine with surface realization coded

**Reproduction**:
- Parse Hebrew verb morphology
- Extract person/number/gender from verb
- Track implicit subject as Routine
- Mark Surface Realization as "Implicit" or "Verb"

---

### Challenge 2: Generic vs. Specific "Water"
**Examples**:
- Generic: "Water is essential for life" (type-level)
- Frame Inferable: "The water was in the well" (specific quantity, part of scene)
- Routine: "She drew the water and drank it" (tracked participant)

**Detection**:
- Check verb: stative/definitional → Generic
- Check context: frame + definite → Frame Inferable
- Check tracking: mentioned before → Routine

---

### Challenge 3: Collective References
**Example**: "The disciples" - one referent or many?

**TBTA Approach**: Treats collective as single tracked participant

**Reproduction**:
- Track "the disciples" as single entity
- Same tracking states apply
- Mark number as Plural

---

### Challenge 4: Quoted Speech
**Problem**: "The woman said, 'I want water'" - who is "I"?

**TBTA Approach**:
- "I" in quote refers to speaker (the woman)
- Marks as Routine (coreferent with main clause subject)
- Person shifts from Third to First within quote

**Reproduction**:
- Track quote boundaries
- Resolve pronouns to speaker/addressee
- Continue referent chains across quote boundaries

---

### Challenge 5: Titles and Epithets
**Example**: "Jesus" → "He" → "the Teacher" → "the Nazarene"

**Problem**: Different surface forms, same referent

**Solution**:
- Build title/epithet database
- Map epithets to primary referents (Jesus → Teacher, Nazarene, Son of Man, etc.)
- All should be Routine once established

---

## Success Metrics

### Metric 1: State-level Precision/Recall
For each state, calculate:
```
Precision = True Positives / (True Positives + False Positives)
Recall = True Positives / (True Positives + False Negatives)
F1 = 2 * (Precision * Recall) / (Precision + Recall)
```

**Target**: F1 > 0.85 for each state

---

### Metric 2: Overall Accuracy
```
Accuracy = Correct Annotations / Total Annotations
```

**Target**: > 85%

---

### Metric 3: Referent Chain Coherence
For randomly sampled referent chains:
- Manual review of logical progression
- Check for state transition violations
- Validate surface form consistency

**Target**: > 90% coherent chains

---

### Metric 4: Cross-validator Agreement
Have multiple annotators code same passages:
- Calculate inter-annotator agreement (Kappa)
- Identify systematic disagreements
- Refine guidelines

**Target**: Kappa > 0.80

---

## Next Steps

1. **Implement MVP (3-state system)** on Genesis 1
   - Routine, Generic, First Mention only
   - Validate against TBTA gold standard
   - Measure baseline accuracy

2. **Build frame database** from TBTA examples
   - Extract all Frame Inferable instances
   - Identify evoking words and participants
   - Create structured YAML database

3. **Add Frame Inferable detection**
   - Test on narrative passages
   - Iterate on frame definitions
   - Expand database

4. **Scale to full Gospel**
   - Run on Mark (shortest gospel)
   - Calculate comprehensive metrics
   - Document edge cases

5. **Extend to other genres**
   - Test on Epistles (different discourse structure)
   - Test on Wisdom literature (high Generic percentage)
   - Test on Prophets (mix of narrative and oracle)

---

## Conclusion

Participant tracking is **highly reproducible** using:
1. Coreference resolution (80%+ accuracy with modern NLP)
2. Simple heuristics (referential distance, generic detection)
3. Frame semantics database (manual curation + FrameNet)
4. Syntactic parsing (interrogative detection)

The **5-state simplified system** covers 100% of TBTA's active annotations. The remaining 4 theoretical states can be added later if needed for other genres or languages.

**Estimated development time**: 4-5 weeks for full implementation and validation

**Expected accuracy**: 85-90% matching TBTA annotations

**Primary challenges**:
- Generic vs. specific ambiguity (context-dependent)
- Frame database completeness
- Coreference resolution in complex passages

**Risk mitigation**:
- Start with high-precision rules, expand coverage iteratively
- Use confidence scores to flag uncertain cases for manual review
- Build genre-specific models (narrative vs. wisdom vs. epistle)

This feature is **ready for implementation**.
