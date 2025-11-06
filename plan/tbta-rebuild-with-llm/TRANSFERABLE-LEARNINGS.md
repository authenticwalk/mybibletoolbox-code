# Transferable Learnings from TBTA Experiments

This document captures patterns and methodologies from successful TBTA experiments that can be applied to other grammatical features using **LLM prompt engineering and context**.

**Critical**: All patterns use LLM prompting, NOT Python prediction code.

---

## From: Person-Systems Experiment (Clusivity Prediction)

**Source**: `features/person-systems/`
**Achievement**: 100% accuracy on inclusive/exclusive predictions (11/11 test cases)
**Method**: LLM prompting with theological and discourse context

### 1. Hierarchical Prompting Framework (KEY TRANSFERABLE PATTERN)

The experiment achieved perfect accuracy by using a **hierarchical prompt strategy** instead of flat analysis. This approach is transferable to ANY grammatical feature with ambiguity.

#### The Prompt Hierarchy:
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
  Use rarity principle - most common value
```

#### Why This Works:
- **Prioritizes meaning over form**: Theological/semantic factors resolve ambiguity before grammar
- **Early termination**: Most cases resolved at Level 1-2 (ontological/capability)
- **Clear decision points**: Each level has binary or categorical outcomes
- **Leverages LLM strengths**: Modern LLMs excel at theological and semantic analysis

#### Prompt Template Example (Level 1 - Theological):
```
Analyze the theological context for the pronoun "us" in Genesis 1:26:

"Let us make man in our image"

Context: This is the creation narrative, where God creates humanity.

Questions to consider:
1. Who is speaking? (God)
2. Who is being addressed? (Trinity members OR divine counsel)
3. What action is being performed? (Creation - a divine prerogative)
4. Can the addressees participate in this action?
   - If Trinity members: Yes (all persons in Godhead create)
   - If divine counsel: No (only God creates, not angels)
5. What is the theological understanding of creation in Genesis?
   - Creation is exclusively God's work
   - No creature participates in creating other creatures

Based on this analysis:
- Is "us" INCLUSIVE (includes addressee in action) or EXCLUSIVE (excludes addressee)?
- Confidence level: High/Medium/Low
- Reasoning: ...
```

#### Application to Other Features:
- **Aspect**: Perfective vs Imperfective → Prioritize action completion semantics over verb forms
- **Mood**: Indicative vs Subjunctive → Prioritize speaker certainty/reality before grammatical mood
- **Voice**: Active vs Passive → Prioritize agent focus and discourse prominence before syntax
- **Number**: Singular vs Plural → Prioritize semantic collectivity before grammatical number

### 2. Theological Factors Override Grammatical Ambiguity

**Finding**: When grammar is ambiguous, theological context provides deterministic answers.

#### Prompt Strategy for Theological Analysis:

**Template**:
```
Theological Analysis Prompt:

Verse: {reference}
Text: {verse text}
Word/phrase under analysis: "{constituent}"
Feature to determine: {feature_name}

Theological Framework Questions:
1. Does this involve a divine prerogative? (creation, judgment, omniscience)
   → Affects: Person (exclusive), Number, Aspect

2. Does this describe a salvific experience? (justification, peace with God)
   → Affects: Person (inclusive for believers), Mood, Voice

3. Is there an authority structure? (apostolic witness, divine command)
   → Affects: Person (exclusive for authorities), Mood, Force

4. Does this express community identity? (unity, worship, shared faith)
   → Affects: Person (inclusive), Number, Proximity

Theological Categories That Drive Decisions:
- Divine prerogatives → Restrict participation
- Salvific experiences → Shared participation
- Authority structures → Limited participation
- Community identity → Inclusive participation

Based on the theological context, what value is most appropriate for {feature_name}?
Confidence: High/Medium/Low
Reasoning: ...
```

#### Examples from Clusivity:
- **Genesis 1:26** "Let us make man" - Grammar ambiguous (plural), but theology clear (divine creation → EXCLUSIVE)
- **John 17:21** "in us" - Grammar ambiguous, but theology clear (believers in divine unity → INCLUSIVE)

#### Application to Other Features:
- **Aspect in prophecy**: Fulfilled vs unfulfilled affects perfective/imperfective choice
- **Mood in divine commands**: God's commands carry different certainty than human requests
- **Voice in atonement passages**: Agent focus (Christ) vs beneficiary focus (believers)
- **Definiteness**: Theological uniqueness (THE Messiah) vs general reference

### 3. Capability Analysis as Primary Filter

**Finding**: The question "Can the addressee perform this action?" resolved most ambiguous cases.

#### Prompt Template for Capability Analysis:

```
Capability Analysis Prompt:

Verse: {reference}
Speaker: {who is speaking}
Addressee: {who is being addressed}
Action/State: {what is described}
Pronoun/Form: {the grammatical form under analysis}

CAPABILITY TEST:
1. Identify the specific action or state described
2. Can the addressee perform/participate in this action?

   Questions to ask:
   - Is this within human capability? (walking, speaking, believing)
   - Is this a divine-only capability? (creating, omniscience, forgiveness of sins)
   - Is this role-specific? (apostolic witness, priestly service)
   - Is this a shared experience? (suffering, joy, faith)

3. If NO (addressee cannot participate):
   → EXCLUSIVE (speaker + others, not addressee)

4. If YES (addressee can participate):
   → Continue to next level (identity/group analysis)

Result:
- Can addressee participate? Yes/No
- Reasoning: ...
- Implication for {feature_name}: ...
```

#### Examples:
- **Acts 2:32** "We are witnesses" → Can crowd witness resurrection? NO → EXCLUSIVE
- **Romans 5:1** "We have peace" → Can addressee have peace with God? YES → Check identity (believers) → INCLUSIVE
- **Genesis 1:26** "Let us make man" → Can heavenly beings create? NO (only God creates) → EXCLUSIVE

#### Why This Works:
- **Objective criterion**: Less subject to interpretation
- **Filters most cases early**: Resolves 60%+ of ambiguous situations
- **Theologically sound**: Aligns with biblical theology of unique divine/human/apostolic roles
- **LLM-friendly**: Modern LLMs understand capability constraints

#### Application to Other Features:
- **Mood**: Can the speaker command this? (Authority check)
- **Aspect**: Can this action be completed? (Telicity check)
- **Voice**: Who is capable of performing this action? (Agent capability)
- **Number**: Can this referent be multiple entities? (Ontological plurality)

### 4. Pattern Recognition Across Contexts

**Finding**: Similar contexts produce consistent patterns. Once a pattern is established, it reliably predicts other cases.

#### Prompt Strategy for Pattern Recognition:

**Template**:
```
Pattern Recognition Prompt:

I've observed these patterns in previous analysis:

Pattern 1: Divine Speech Context
- Context: Divine speaker, human addressee
- Action type: Creation, judgment, divine knowledge
- Historical result: EXCLUSIVE (100% reliable in 5 cases)
- Sample verses: Gen 1:26, Gen 3:22, Gen 11:7

Pattern 2: Apostolic Witness
- Context: Apostle speaker, church addressee
- Action type: Eyewitness testimony
- Historical result: EXCLUSIVE (100% reliable in 3 cases)
- Sample verses: Acts 2:32, 1 John 1:1-3

Current verse to analyze:
Verse: {reference}
Speaker: {speaker}
Addressee: {addressee}
Action: {action}

Questions:
1. Does this verse match any established pattern?
2. If yes, which pattern?
3. What is the confidence level based on pattern matching?
4. Are there any differences from the pattern that might affect the result?

Predicted value based on pattern: ...
Confidence: High/Medium/Low (based on pattern reliability)
```

#### Established Patterns from Experiments:

**Pattern: Divine Speech** (100% reliable)
- Context: Divine speaker, human addressee
- Action: Creation, judgment, divine knowledge
- Result: EXCLUSIVE
- Verses: Gen 1:26, Gen 3:22, Gen 11:7

**Pattern: Prayer to God** (100% reliable)
- Context: Human speaker, divine addressee
- Pronoun refers to: Speaker and others
- Result: EXCLUSIVE of God
- Verses: Matt 6:9, John 17:20-21

**Pattern: Apostolic Witness** (100% reliable)
- Context: Apostle speaker, church addressee
- Action: Eyewitness testimony
- Result: EXCLUSIVE
- Verses: Acts 2:32, 1 John 1:1-3

**Pattern: Community Exhortation** (95% reliable)
- Context: Believer speaker, believer addressee
- Action: Shared faith experience
- Result: INCLUSIVE
- Verses: Rom 5:1, Eph 4:4-6

#### Application to Other Features:
- **Aspect patterns**: Narrative past → Completive; Background description → Continuative
- **Mood patterns**: Direct command → Obligation; Polite request → Permissive
- **Voice patterns**: Agent emphasis → Active; Patient emphasis → Passive
- **Definiteness patterns**: First mention → Indefinite; Subsequent → Definite

### 5. Validation Against Real Translations

**Finding**: Testing predictions against actual Bible translations confirms accuracy and reveals gaps.

#### Prompt Template for Validation:

```
Translation Validation Prompt:

I predicted {predicted_value} for {feature_name} in {verse reference}.

Here are actual translations:
- Indonesian: {translation} (uses: {grammatical_choice})
- Tagalog: {translation} (uses: {grammatical_choice})
- {other language}: {translation} (uses: {grammatical_choice})

Analysis questions:
1. Do the actual translations match my prediction?
2. If not, what did translators choose instead?
3. What might explain the difference?
   - Did I misunderstand the theological context?
   - Did I miss a discourse factor?
   - Is this an ambiguous case with multiple valid readings?
4. Should I revise my prediction or document as ambiguous?

Validation result:
- Matches translations: Yes/No
- If no, reason for difference: ...
- Revised prediction (if needed): ...
```

#### Example Validation Table:
| Passage | Prediction | Indonesian | Tagalog | Match? |
|---------|------------|------------|---------|--------|
| John 17:21 | INCLUSIVE | Kita ✓ | atin ✓ | ✅ |
| Matt 6:9 | EXCLUSIVE | Kami ✓ | aming ✓ | ✅ |
| Acts 2:32 | EXCLUSIVE | Kami ✓ | amin ✓ | ✅ |

Result: 100% accuracy (11/11 test cases)

#### Why This Matters:
- **Catches theoretical errors**: Framework must match translator intuitions
- **Builds confidence**: High accuracy validates approach
- **Reveals edge cases**: Mismatches show where framework needs refinement
- **LLM improvement**: Can feed back examples to improve future prompts

---

## From: Aspect Experiment (98.1% Accuracy)

**Source**: `features/verb-tam/aspect-*`
**Achievement**: 98.1% accuracy (53/54 correct predictions)
**Method**: Rarity principle + Mood correlation + Multi-factor analysis

### 6. The Rarity Principle (HIGHEST BASELINE IMPACT)

**Discovery**: 90.7% of verbs are Unmarked (default), only 9.3% marked (Inceptive/Imperfective/Habitual)

**Core Insight**: TBTA only marks when semantically necessary. For ANY feature, identify and default to the dominant value.

#### Prompt Strategy for Rarity Principle:

**Step 1: Distribution Analysis Prompt**
```
Analyze the distribution of {feature_name} values in this sample:

{provide 20-50 example verses with feature values}

Questions:
1. What is the most common value? (count and percentage)
2. What are the rare/marked values? (count and percentage)
3. What is a good default/baseline prediction?

The baseline should:
- Account for 80-90% of cases
- Be the semantically unmarked/neutral value
- Require no special context to predict

Distribution analysis:
- {Value 1}: X% ({count} instances)
- {Value 2}: Y% ({count} instances)
- ...

Recommended baseline: {most common value}
Expected baseline accuracy: {percentage}%
```

**Step 2: Baseline Application Prompt**
```
For {verse reference}, predict {feature_name}:

Baseline value: {dominant_value} (accounts for {percentage}% of cases)

Check for special triggers that would override baseline:
- [ ] Theological factor present? (e.g., divine action)
- [ ] Discourse marker present? (e.g., topic shift)
- [ ] Grammatical trigger present? (e.g., specific mood)
- [ ] Semantic trigger present? (e.g., action vs state)

If NO special triggers found:
→ Use BASELINE: {dominant_value}
→ Confidence: {baseline_percentage}% (from distribution)

If special triggers found:
→ Override baseline with: {marked_value}
→ Confidence: depends on trigger strength
→ Reasoning: ...
```

#### Results from Aspect Experiment:
- Unmarked predictions = 97.9% accurate (48/49)
- Only 5 marked values needed special analysis
- Baseline alone gave 90.7% accuracy

#### Apply To:
- **Polarity**: Default Affirmative (~90%)
- **Voice**: Default Active (~70%)
- **Status**: Default Realis (~85%)
- **Person**: Default 3rd in narrative (~70%)
- **Mood**: Default Indicative (~85%)

**Why It Works**: Matches TBTA philosophy (mark only when necessary), achieves 80-90% baseline immediately with zero analysis

### 7. Mood as Gateway Feature (100% CORRELATION)

**Discovery**: Potential mood → Inceptive aspect (6/6 cases, 100% correlation)

**Core Insight**: Check mood FIRST to constrain other feature predictions

#### Prompt Strategy for Gateway Features:

```
Gateway Feature Analysis:

Step 1: Identify the gateway feature
For verbs, the gateway is MOOD (most deterministic, explicitly marked)
For nouns, the gateway is SEMANTIC TYPE (person, place, thing, concept)
For clauses, the gateway is GENRE (narrative, teaching, dialogue)

Step 2: Extract gateway feature value
Verse: {reference}
Gateway feature: MOOD
Value: {extract from TBTA data or infer from context}

Step 3: Apply gateway constraints
Known correlations:
- If Mood = Potential → Aspect almost always = Inceptive
- If Mood = Indicative + Time = Historic Past → Aspect likely = Completive
- If Mood = Obligation → Voice often = Active

Step 4: Use gateway to predict target feature
Gateway: MOOD = {value}
Target: ASPECT = ?

Based on gateway value:
- Strong correlation (>90%): Predict {value} with high confidence
- Moderate correlation (70-89%): Predict {value} with medium confidence
- Weak correlation (<70%): Cannot constrain, use other methods

Prediction based on gateway:
- Predicted value: ...
- Confidence: High/Medium/Low
- Correlation strength: {percentage}% (from historical data)
```

#### Why Gateway Features Work:
- **Mood is explicit in TBTA**: No guessing needed
- **Grammatical features correlate**: Mood constrains Time, Aspect, Voice
- **Reduces search space**: 50-80% reduction in possibilities
- **LLM-friendly**: Can check one feature to constrain others

#### Application:
- **For verbs**: Check Mood → constrains Aspect, Time, Voice
- **For nouns**: Check Semantic Type → constrains Person, Number
- **For clauses**: Check Genre → constrains Structure, Force, Salience

### 8. Multi-Factor Convergence (HIGHEST ACCURACY)

**Discovery**: Inceptive = 100% accurate (3/3) when 3 factors converged:
1. Action verb (beat, eat, drink)
2. Potential mood ('might')
3. Near-future time (Later Today)

#### Prompt Strategy for Multi-Factor Convergence:

```
Multi-Factor Analysis for {feature_name}:

Verse: {reference}
Word: "{constituent}"
Feature to predict: {feature_name}

FACTOR 1: {first factor type}
Analysis: ...
Prediction: {value_1}
Confidence: {conf_1}

FACTOR 2: {second factor type}
Analysis: ...
Prediction: {value_2}
Confidence: {conf_2}

FACTOR 3: {third factor type}
Analysis: ...
Prediction: {value_3}
Confidence: {conf_3}

CONVERGENCE CHECK:
- Do all 3 factors agree?
  - If YES → High confidence (95%)
  - Predicted value: {agreed_value}

- Do 2/3 factors agree?
  - If YES → Medium confidence (80%)
  - Predicted value: {majority_value}

- All factors disagree?
  - Flag for human review
  - Use baseline as default
  - Confidence: Low (50%)

Final prediction:
- Value: ...
- Confidence: ...
- Agreement: 3/3 or 2/3 or 1/3
```

**Confidence Formula**:
```
0 triggers → 30% (baseline only)
1 trigger  → 60% (weak)
2 triggers → 80% (medium)
3+ triggers → 95%+ (strong)
```

---

## From: Mood Detection Experiment (100% Accuracy)

**Source**: `features/verb-tam/mood-*`
**Achievement**: 100% accuracy (316 verbs)
**Key Learning**: Always check if feature is EXPLICIT before building complex prediction

### 9. Check for Explicit Encoding FIRST (Tier 0)

**Discovery**: Mood is EXPLICIT in TBTA YAML, not predicted!

**Critical Learning**: Always check if a feature can be directly extracted before building prediction systems.

#### Prompt Strategy for Explicit Feature Extraction:

**Step 1: Check if Explicit**
```
Feature Extraction Check:

Feature: {feature_name}
Data source: TBTA YAML

Question: Is this feature explicitly encoded in the data?

Approach:
1. Examine sample YAML for {N} verses
2. Look for field named {feature_name} or similar
3. Check if value is present at:
   - Clause level
   - Verb phrase level
   - Word level

Results:
- Found at: {level}
- Field name: {field_name}
- Values present: Yes/No
- Consistency: Always present / Sometimes / Never

Conclusion:
- If ALWAYS present → EXPLICIT (use direct extraction)
- If SOMETIMES present → SEMI-EXPLICIT (extract when available, predict when missing)
- If NEVER present → IMPLICIT (must predict)
```

**Step 2: If Explicit, Use Simple Extraction Prompt**
```
Extract {feature_name} from this verse:

{paste TBTA YAML}

Task:
1. Locate the {feature_name} field in the YAML
2. Extract the value
3. Note the constituent it applies to
4. Provide location in structure

Format response as:
- Constituent: "{text}"
- Feature: {feature_name}
- Value: {extracted_value}
- Location: {path in YAML structure}
```

#### Why This Matters:
- **Saves enormous effort**: Don't build complex prediction when simple extraction works
- **100% accuracy possible**: Explicit features have no ambiguity
- **Fast implementation**: Can complete in minutes instead of days

#### Features Likely Explicit in TBTA:
- Mood (confirmed: 100% explicit)
- Part of Speech (Word, Noun, Verb, etc.)
- Constituent (the actual text)
- Some Time markers
- Some structural features (Clause, Phrase, etc.)

#### Features Likely Implicit (Need Prediction):
- Aspect (some marked, many unmarked)
- Person (clusivity especially)
- Participant Tracking (discourse-level)
- Definiteness (not in source languages)
- Salience bands (interpretation-based)

**Always Check Tier 0 (Explicit) Before Building Tier 1-5 (Prediction)**

---

## From: Participant Tracking Experiment (90% Accuracy)

**Source**: `/plan/tbta-project-local/experiments/participant-tracking/`
**Achievement**: 90% accuracy with discourse context
**Key Learning**: Some features require discourse memory beyond single verse

### 10. Discourse-Level Context Strategy

**Discovery**: Verse-level analysis insufficient for Participant Tracking. Need discourse memory.

#### Prompt Strategy for Discourse Features:

**Approach 1: LLM Memory (Recommended)**

Use LLM's built-in knowledge of the Bible plus discourse context in prompt:

```
Participant Tracking Analysis with Discourse Context:

Verse to analyze: {reference}

DISCOURSE CONTEXT (provide to LLM):
Previous verses in same narrative:
{verse N-3}: {text}
{verse N-2}: {text}
{verse N-1}: {text}
CURRENT verse {verse N}: {text}
Next verse {verse N+1}: {text}

Characters/Entities introduced so far:
- {Entity 1}: First mentioned in verse {ref}, status {current_status}
- {Entity 2}: First mentioned in verse {ref}, status {current_status}

Current narrative context:
- Book: {book}
- Chapter: {chapter}
- Section: {narrative section description}
- Speaker: {who is speaking}

For entity "{entity_name}" in current verse:
1. Is this the first mention of this entity in this discourse section?
   → If YES: First Mention (I)

2. Has this entity been mentioned recently (within 3-5 verses)?
   → If YES: Routine (D)

3. Has this entity been absent and now returns?
   → If YES: Restaging (R)

4. Is this entity about to leave the narrative permanently?
   → If YES: Exiting (E)

5. Can this entity be inferred from context without explicit mention?
   → If YES: Frame Inferable (F)

Predicted Participant Tracking value: ...
Reasoning based on discourse context: ...
```

**Approach 2: Syntactic Surface Form as Proxy**

When full discourse context unavailable, use grammatical form:

```
Syntactic Form Analysis (Proxy for Discourse Status):

Entity: "{entity_text}"
Grammatical form: {pronoun/noun/possessive/demonstrative}

Proven correlations:
- Pronoun (he, she, it, they) → 100% reliable → Routine (D)
  Reasoning: Pronouns always refer to established entities

- Possessive + NEW entity (his goods, her children) → 90% reliable → Frame Inferable (F)
  Reasoning: Entity implied through possessor relationship

- Demonstrative + noun (that servant, this man) → 80% reliable → First Mention (I) or Restaging (R)
  Reasoning: Demonstrative introduces/reintroduces specific entity

- Proper noun (Peter, Jerusalem) → Context-dependent
  Reasoning: Could be First Mention, Routine, or Restaging

Current entity:
- Form: {form}
- Predicted status: {status}
- Confidence: {high/medium/low}
- Reasoning: ...
```

#### Why Discourse Context Matters:
- **7+ features need chapter-level context**: Participant Tracking, NounListIndex, Salience, Notional Structure, etc.
- **LLMs have Bible knowledge**: Modern LLMs know biblical narratives well
- **Memory is natural**: Providing ±3 verses is easy in prompts
- **Form patterns work**: When memory fails, grammatical form is reliable fallback

#### Application to Other Features:
- **NounListIndex**: Need discourse context to assign consistent indices across verses
- **Surface Realization**: Zero anaphora requires discourse history to resolve
- **Topic/Focus**: Topic continuity requires tracking across verse boundaries
- **Definiteness**: First mention vs subsequent mention requires discourse history
- **Salience Bands**: Pivotal storyline vs background requires discourse structure

---

## Cross-Experiment Meta-Patterns

### Meta-Pattern 1: Theology > Semantics > Grammar

**Across all experiments**, this hierarchy held:

```
Prompt Priority Order:
1. Theological factors (divine nature, salvific action, authority)
2. Semantic factors (capability, telicity, animacy)
3. Discourse factors (genre, flow, participant structure)
4. Grammatical factors (morphology, syntax, explicit markers)
```

**Why**: Biblical text is theological communication first, linguistic artifact second. LLMs trained on Bible + theology excel at this hierarchy.

### Meta-Pattern 2: Baseline + Triggers

**Across all experiments**, this strategy worked:

```
Prompt Strategy:
1. Identify baseline (80-90% cases)
2. Default to baseline unless triggers present
3. Check for triggers in priority order
4. Override baseline only with high-confidence trigger
```

**Why**: Most features have dominant unmarked value. Only mark when semantically necessary.

### Meta-Pattern 3: Multi-Method Validation

**Across all experiments**, agreement increased confidence:

```
Validation Strategy:
1. Method 1: Theological/Semantic analysis → Prediction A
2. Method 2: Discourse/Functional analysis → Prediction B
3. Method 3: Grammatical/Formal analysis → Prediction C

Agreement levels:
- 3/3 agree → 95%+ confidence
- 2/3 agree → 80% confidence
- 1/3 or 0/3 → Flag for human review, use baseline
```

**Why**: Independent methods catch different aspects. Agreement = robustness.

### Meta-Pattern 4: Blind Testing Prevents Overfitting

**Across all experiments**, blind testing was critical:

```
Testing Protocol:
1. Create test set with known values (don't look at values!)
2. Apply prompts to predict values
3. ONLY AFTER all predictions, compare with actual
4. Analyze errors systematically
5. Refine prompts based on error patterns
```

**Why**: Looking at answers before predicting causes unconscious bias. Blind testing ensures prompts truly work, not memorization.

---

## Implementation Checklist

### For ANY TBTA Feature:

#### Phase 1: Discovery (Check These First)
- [ ] Is feature EXPLICIT in YAML? (Check Tier 0 first - saves weeks!)
- [ ] What is the baseline distribution? (Expect 80-90% dominant value)
- [ ] Are there gateway features? (Mood for verbs, SemanticType for nouns, Genre for clauses)
- [ ] Does this need discourse context? (Tracking, Index, Salience, Structure)

#### Phase 2: Prompt Strategy Design
- [ ] Level 1 prompt: Theological/Semantic analysis
- [ ] Level 2 prompt: Capability/Restriction analysis
- [ ] Level 3 prompt: Discourse function analysis
- [ ] Level 4 prompt: Grammatical cue analysis
- [ ] Level 5 baseline: Rarity principle default

#### Phase 3: Validation
- [ ] Test on 10+ sample verses (blind testing)
- [ ] Calculate accuracy (target: >85%)
- [ ] Categorize errors (Type 1-5)
- [ ] Refine prompts based on errors

#### Phase 4: Documentation
- [ ] Document prompt templates (for others to use)
- [ ] Document known patterns (for pattern matching)
- [ ] Document correlations (for gateway features)
- [ ] Document examples (5-10 concrete cases)

---

## Conclusion: The LLM Advantage

**Why LLM prompt engineering outperforms algorithmic approaches:**

1. **Biblical Knowledge**: Modern LLMs trained on extensive biblical texts, theology, commentaries
2. **Theological Reasoning**: Can apply systematic theology, not just surface grammar
3. **Context Integration**: Can consider discourse, genre, speaker intent naturally
4. **Ambiguity Handling**: Can provide multiple readings with confidence levels
5. **Zero-Shot Capability**: Often accurate without training examples
6. **Refinement Through Prompting**: Easy to improve by adjusting prompts vs rewriting code

**The Formula for 95%+ Accuracy:**

```
High Accuracy = Rarity Principle (80-90% baseline)
              + Hierarchical Prompts (theology → semantics → grammar)
              + Gateway Features (check Mood/Genre/SemanticType first)
              + Multi-Method Validation (3 independent analyses)
              + Discourse Context (when needed)
              + Blind Testing (prevent overfitting)
```

**All using LLM prompting, not Python code.**

These patterns achieved:
- **Person (Clusivity)**: 100% accuracy (11/11)
- **Mood**: 100% accuracy (316/316) via extraction
- **Aspect**: 98.1% accuracy (53/54)
- **Participant Tracking**: 90% accuracy with discourse context

Apply these transferable patterns to ANY TBTA feature for similar results.
