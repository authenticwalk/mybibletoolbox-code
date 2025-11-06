# Generic TBTA Feature Implementation Template

## Purpose
This template provides a standardized approach for implementing, analyzing, or predicting ANY TBTA feature using LLM prompt engineering based on learnings from successful experiments (Aspect 98%, Person 100%, Mood 100%, Participant Tracking 100%).

**Critical**: This approach uses LLM context and prompting, NOT Python prediction code.

---

## Phase 1: UNDERSTAND THE FEATURE

### Step 1.1: Feature Discovery
- [ ] Read official TBTA documentation for this feature
- [ ] Identify feature category (Noun/Verb/Clause/Phrase/Discourse)
- [ ] List all possible values (complete enumeration)
- [ ] Determine if feature is **explicit in YAML** or **must be inferred**

**Key Question**: Is this feature directly extractable from TBTA data?
- **YES** → Go to **Phase 2A: Direct Extraction** (Mood pathway - fastest)
- **NO** → Go to **Phase 2B: LLM Prediction Framework** (Aspect/Person pathway)

### Step 1.2: Translation Impact Analysis
- [ ] Which language families need this feature? (List 3-5)
- [ ] What translation errors occur without this feature? (List 2-3 examples)
- [ ] What is the priority tier? (A=Essential, B=Important, C=Nice-to-have)

### Step 1.3: Data Availability Assessment
- [ ] How many verses in TBTA data have this feature annotated?
- [ ] Are annotations consistent across books/genres?
- [ ] What is the baseline distribution? (e.g., 90% Unmarked, 10% marked)

---

## Phase 2A: DIRECT EXTRACTION (For Explicit Features)

### Step 2A.1: Locate Feature in YAML Structure

**Approach**: Ask LLM to examine sample YAML and identify where feature appears

**Prompt Template**:
```
I need to extract the "{feature_name}" feature from TBTA YAML data.

Here is a sample verse YAML:
{paste sample YAML}

Please:
1. Identify where "{feature_name}" appears in the structure
2. Note the path (e.g., clauses[0].children[1].{feature_name})
3. Check if it's at clause level, phrase level, or word level
4. Confirm the field name is consistent
```

**Test with 3 sample verses** to confirm location stability

### Step 2A.2: Build Extraction Strategy

**Approach**: Use LLM to read YAML and extract feature values with context

**Prompt Template**:
```
Extract all instances of "{feature_name}" from this verse:

{paste verse YAML}

For each instance, provide:
- Value of {feature_name}
- Constituent (the text it applies to)
- Context (parent clause/phrase)
- Location in structure

Format as simple list.
```

### Step 2A.3: Validate Extraction
- [ ] Run on 10 sample verses
- [ ] Compare extracted values vs manual inspection
- [ ] Check edge cases (nested structures, missing values, null handling)
- [ ] Document extraction reliability (should be 100% for explicit features)

**Success Criteria**: 100% extraction accuracy on all sampled verses

---

## Phase 2B: LLM PREDICTION FRAMEWORK (For Implicit Features)

### Step 2B.1: Apply Rarity Principle

**Concept**: Identify the dominant value (baseline) that accounts for 80-90% of cases

**Approach**: Ask LLM to analyze sample data and identify pattern

**Prompt Template**:
```
Analyze the distribution of "{feature_name}" values in these {N} sample verses:

{paste sample data showing feature values}

1. What is the most common value? (percentage)
2. What are the rare/marked values? (percentage)
3. What is a good default/baseline prediction?

This baseline should give 80-90% accuracy without further analysis.
```

**Target**: Baseline should give you 80-90% accuracy immediately

### Step 2B.2: Build Hierarchical Prompt Strategy

**Concept**: Layer prompts from most deterministic to least deterministic

**Template from Person/Aspect/Participant experiments**:

**LEVEL 1: Theological/Semantic Analysis (Most Important)**

Prompt:
```
Analyze the theological/semantic factors for "{constituent}" in {verse reference}:

Verse context: {surrounding verses}
Word being analyzed: "{constituent}"
Theological context: {book theme, passage theme}

For the feature "{feature_name}", consider:
- Does this refer to God/deity? (affects Person, Number)
- Is this describing capability or ontology? (affects Person, Aspect)
- What is the semantic type? (State, Action, Process, Event)
- Does theology override grammar here?

What value is most theologically appropriate? (Confidence: High/Medium/Low)
```

**LEVEL 2: Discourse Context Analysis**

Prompt:
```
Analyze the discourse context for "{constituent}" in {verse reference}:

Surrounding verses: {previous 2 verses + next 2 verses}
Discourse genre: {narrative/teaching/prophecy/etc}
Speaker: {who is speaking}
Listener: {who is being addressed}

For the feature "{feature_name}", consider:
- Is this a new participant or established? (affects Tracking)
- What is the discourse flow? (affects Salience, Structure)
- How does this fit the genre pattern?

What value fits the discourse context? (Confidence: High/Medium/Low)
```

**LEVEL 3: Grammatical Cues**

Prompt:
```
Analyze the grammatical cues for "{constituent}" in {verse reference}:

Surrounding text: {sentence or clause}
Source language: {Greek/Hebrew text if available}
Grammatical form: {morphology from Macula if available}

For the feature "{feature_name}", consider:
- What grammatical markers are present? (pronouns, articles, verb forms)
- What does the source language grammar suggest?
- Are there explicit indicators in the text?

What value do the grammatical cues suggest? (Confidence: High/Medium/Low)
```

**LEVEL 4: Cross-Feature Correlations**

Prompt:
```
Check correlations with other features for "{constituent}" in {verse reference}:

Known features from TBTA:
- Mood: {value if known}
- Time: {value if known}
- Genre: {value if known}
- {other relevant features}

For the feature "{feature_name}", historical correlations show:
- Potential mood → 100% Inceptive aspect
- Historic Past + Narrative → Usually Completive aspect
- {list known correlations}

Based on these correlations, what value is predicted?
```

**LEVEL 5: Baseline (Default)**

If all analysis is inconclusive:
```
No strong indicators found for "{feature_name}" in {verse reference}.

Applying baseline: {BASELINE_VALUE}
Confidence: {baseline_accuracy}% (from distribution analysis)
Method: Default (rarity principle)
```

### Step 2B.3: Multi-Method Validation

**Approach**: Use multiple LLM prompts independently, require agreement

**Prompt Template**:
```
I have 3 independent analyses for "{feature_name}" in {verse reference}:

Method 1 (Theological): {value_1} (Confidence: {conf_1})
Method 2 (Discourse): {value_2} (Confidence: {conf_2})
Method 3 (Grammatical): {value_3} (Confidence: {conf_3})

Evaluate:
- Do all 3 agree? → High confidence (95%)
- Do 2/3 agree? → Medium confidence (80%)
- All disagree? → Flag for human review, use baseline

What is the final prediction and confidence level?
```

### Step 2B.4: Blind Testing Protocol

**Critical for avoiding overfitting**:

1. Create test set of verses with known feature values (don't look at values!)
2. Apply LLM prompt strategy to predict values
3. ONLY AFTER all predictions are made, compare with actual values
4. Analyze errors and refine prompts

**Prompt for Error Analysis**:
```
I predicted "{predicted_value}" but the actual value was "{actual_value}" for {verse reference}.

Verse context: {context}
My reasoning: {why I predicted that value}

Why was I wrong?
1. Was theological/semantic factor missed?
2. Was discourse context misunderstood?
3. Was grammatical cue misinterpreted?
4. Was this an ambiguous case with multiple valid readings?

How should the prompt be improved to catch this case?
```

---

## Phase 3: VALIDATION & REFINEMENT

### Step 3.1: Error Categorization

For each error, ask LLM to categorize:

**Prompt**:
```
Categorize this prediction error:

Verse: {reference}
Predicted: {predicted_value}
Actual: {actual_value}
Context: {verse context}

Is this error:
Type 1: Semantic Expansion - TBTA added implicit information not in surface text
Type 2: Theological Ambiguity - Multiple valid interpretations exist
Type 3: Cultural/Historical Knowledge - Required external knowledge we didn't have
Type 4: Rare Construction - Insufficient training data for this pattern
Type 5: Prompt Limitation - Our prompt strategy didn't check the right factors

Classification: Type ___
Reasoning: ...
```

### Step 3.2: Accuracy Tiering

| Accuracy | Tier | Automation Level |
|----------|------|------------------|
| 95-100% | Tier 1 | LLM with spot checks |
| 85-94% | Tier 2 | LLM with human review |
| 75-84% | Tier 3 | LLM with fallbacks + review |
| <75% | Tier 4 | Human-driven with LLM assistance |

### Step 3.3: Documentation Requirements

Create documentation for each feature:

**1. README.md** - Translator-facing (≤500 lines, progressive disclosure)
- Purpose: What is this feature and why it matters
- Methodology: How to determine the value (LLM prompt patterns)
- Output Schema: What the YAML looks like
- Related Features: Cross-references

**2. EXAMPLES.md** - Concrete verse examples
- 5-10 example verses with detailed analysis
- Show LLM reasoning for each case
- Include edge cases and ambiguities

---

## Phase 4: INTEGRATION

### Step 4.1: Verse-Level Integration

**Approach**: Use LLM to create properly formatted YAML

**Prompt Template**:
```
Create YAML output for "{feature_name}" following SCHEMA.md format:

Verse: {reference}
Feature: {feature_name}
Value: {predicted_value}
Confidence: {confidence_score}
Method: {theological/discourse/grammatical/baseline}

Output YAML with:
- Proper nesting (if part of larger structure)
- Inline source citation
- Confidence metadata
- All required fields per SCHEMA.md

Example format: {show example}
```

### Step 4.2: Cross-Feature Validation

**Prompt Template**:
```
Validate this prediction against related features:

Feature: {feature_name} = {value}
Related features:
- Mood: {value}
- Time: {value}
- Genre: {value}

Check for contradictions:
- Does Inceptive aspect make sense with Indicative mood?
- Does Trial number align with First Inclusive person?
- Does Historic Past fit Narrative genre?

Are there any logical contradictions? If so, which value should be reconsidered?
```

---

## Phase 5: PROMPT REFINEMENT

### Step 5.1: Prompt Optimization

As you gain experience, refine prompts:

**Template for Improvement**:
```
My current prompt for "{feature_name}" is:
{paste current prompt}

Based on errors in verses {list problematic verses}, I need to:
1. Add check for: {missing factor}
2. Emphasize: {underweighted factor}
3. Clarify instruction about: {ambiguous part}

Generate improved prompt that catches these cases while staying concise.
```

### Step 5.2: Context Engineering

**Determine optimal context to provide**:

**Prompt**:
```
For predicting "{feature_name}", what context should I provide to the LLM?

Current context includes:
- The verse text
- ±2 surrounding verses
- Book theme
- {list current context}

Testing shows errors in cases like {example errors}.

What additional context would help?
- Full chapter?
- Parallel passages?
- Source language grammar?
- Theological commentary?
- {other options}

Recommend optimal context (balance accuracy vs token cost).
```

### Step 5.3: Monitoring & Feedback Loop

- [ ] Track prediction accuracy on new data
- [ ] Collect human corrections from users
- [ ] Update prompts based on feedback patterns
- [ ] Document new edge cases in EXAMPLES.md

---

## Success Checklist

### Minimum Viable Implementation
- [ ] Feature values enumerated
- [ ] Baseline prompt working
- [ ] Tested on 10+ verses with >80% accuracy
- [ ] README.md created (≤500 lines)
- [ ] Output YAML format validated

### Production-Ready Implementation
- [ ] Tested on 100+ verses with documented accuracy
- [ ] Hierarchical prompt strategy (5 levels)
- [ ] Error categorization complete
- [ ] Cross-feature validation working
- [ ] EXAMPLES.md with 5-10 detailed cases

### Excellent Implementation
- [ ] Tested on 500+ verses
- [ ] Multiple validation prompts agree
- [ ] Transferable patterns documented
- [ ] Language-specific guidance provided
- [ ] Integration with translation workflows

---

## Feature-Specific Prompt Adaptations

### For Noun Features (Number, Person, Proximity, etc.)

**Priority**: Semantic/ontological analysis over grammar

**Prompt Emphasis**:
- What is the referent? (God, human, object)
- What are the ontological properties?
- What theological factors override grammar?
- How is this tracked in discourse?

**Key Context**: Referent identity, theological category, discourse tracking

### For Verb Features (Time, Aspect, Mood, etc.)

**Priority**: Mood as gateway, then Time, then Aspect

**Prompt Emphasis**:
- Check Mood first (constrains other choices)
- Time relative to discourse frame
- Aspect from telicity and completion
- Genre affects all three

**Key Context**: Mood value, discourse genre, event type, narrative flow

### For Clause Features (Force, Demographics, Genre, etc.)

**Priority**: Discourse context and speech act

**Prompt Emphasis**:
- Who is speaking to whom?
- What is the genre/discourse type?
- What is the illocutionary force?
- How does this fit discourse structure?

**Key Context**: Speaker/listener roles, genre, discourse position, theological context

### For Phrase Features (Semantic Role, Relativization, etc.)

**Priority**: Syntactic structure and discourse function

**Prompt Emphasis**:
- What is the grammatical role?
- How prominent in discourse?
- What semantic relationship?
- How does phrase relate to head?

**Key Context**: Clause structure, case marking, word order, definiteness

---

## Anti-Patterns to Avoid

❌ **Don't**: Use Python/code for predictions
✅ **Do**: Use LLM context and prompt engineering

❌ **Don't**: Ignore the rarity principle
✅ **Do**: Use the dominant value as baseline (instant 80-90% accuracy)

❌ **Don't**: Analyze features in isolation
✅ **Do**: Check correlations with mood, genre, semantics, theology

❌ **Don't**: Look at actual data before making predictions (overfitting)
✅ **Do**: Blind testing with held-out data

❌ **Don't**: Force decisions on ambiguous cases
✅ **Do**: Flag ambiguity, provide multiple readings, lower confidence

❌ **Don't**: Skip error categorization
✅ **Do**: Systematic error analysis reveals fixable prompt gaps

❌ **Don't**: Treat all features equally
✅ **Do**: Tier by confidence, automate high-confidence only

---

## Template Usage Examples

**Example 1: Implementing "Voice" Feature**

1. **Phase 1**: Voice = Active/Passive/Middle, Tier A priority, affects 50+ languages
2. **Phase 2A**: Check if explicit in YAML → YES → Extract using LLM with YAML reading
3. **Phase 3**: Validate on 100 verses → 98% accuracy
4. **Phase 4**: Create prompts for query "find all passive divine passives"
5. **Phase 5**: Document with Tier 1 automation

**Example 2: Implementing "Definiteness" Feature**

1. **Phase 1**: Definite/Indefinite, Tier B priority, affects article languages
2. **Phase 2B**: Not explicit → Predict using LLM prompts
3. **Prompt Level 1**: Theological uniqueness ("THE Messiah") → Definite
4. **Prompt Level 2**: Discourse tracking (First Mention vs Routine) → guide decision
5. **Prompt Level 3**: Article presence in source language
6. **Phase 3**: 85% accuracy on 50 verses → Tier 2 automation with review

---

## Conclusion

This template provides a proven, systematic approach for implementing ANY TBTA feature using **LLM prompt engineering and context engineering** (NOT Python code).

**Key Success Factors**:
1. Check for explicit encoding first (Mood pathway)
2. Use rarity principle (baseline = 80-90% accuracy)
3. Hierarchical prompt strategy (theology → semantics → grammar)
4. Multi-method validation (require agreement across prompts)
5. Blind testing (prevents overfitting)
6. Error categorization (systematic improvement)
7. Tiered automation (confidence-based deployment)

**Critical Principle**: This is an **LLM-driven process**. Features are predicted by providing rich context to language models and using carefully crafted prompts, NOT by writing Python prediction algorithms.

Follow this template, adapt prompts to feature-specific needs, and you will achieve high-accuracy TBTA feature inference using the power of modern LLMs that already understand Biblical text, theology, and linguistics.
