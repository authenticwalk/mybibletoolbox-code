# TBTA Reusable Patterns: Consolidated Learnings from Archive

**Purpose**: Accelerate new TBTA feature development by extracting proven patterns from archived experiments.

**Source**: 4 archived features (Illocutionary Force, Participant Tracking, Number System, Proximity System)

**Status**: Research consolidation complete - Ready for application to active features

---

## Top 10 Proven Approaches

### 1. **Check for Explicit Encoding FIRST (Tier 0)**
**Pattern**: Always verify if feature can be directly extracted before building prediction systems.

**Evidence**:
- Mood feature: 100% accuracy via direct YAML extraction on 316 verbs
- Avoids weeks of unnecessary prompt engineering

**Application**:
```
Step 0: Before designing algorithms, check TBTA YAML structure
- Sample 20-30 verses across books
- Look for explicit fields matching feature name
- If ALWAYS present → Extract directly
- If SOMETIMES present → Hybrid approach (extract when available, predict when missing)
- If NEVER present → Proceed to prediction methods
```

**Success Rate**: Saves 2-4 weeks of development when applicable

**When to Use**: **EVERY new feature** - First step of research phase

---

### 2. **Translation Validation as PRIMARY Discovery Method**
**Pattern**: Don't predict from scratch - discover answers by analyzing existing Bible translations in languages that grammatically encode the target feature.

**Evidence**:
- Person/Clusivity: 98% inter-translator agreement across 9 languages (Indonesian, Tagalog, Fijian, Hawaiian, Quechua, etc.)
- Number: Fijian/Hawaiian encode dual, validate predictions
- Aspect: Russian/Greek/Spanish mark perfective/imperfective

**Application**:
```
For implicit features:
1. Identify 3-9 languages that grammatically mark the feature
2. Gather translations for target verses
3. Extract feature values from each translation
4. Calculate consensus:
   - 9/9 agree → 99.9% confidence
   - 8/9 agree → 99% confidence
   - 7/9 agree → 97% confidence
   - 6/9 agree → 95% confidence (document both views)
   - <6/9 agree → Flag for theological review
5. Use consensus as ground truth, not LLM prediction
```

**Key Language Resources**:
- Person/Clusivity: Indonesian, Tagalog, Quechua, Fijian, Hawaiian, Aymara, Guarani, Bambara, Ewe
- Aspect: Russian, Greek Modern, Spanish, Ukrainian, Bulgarian, Czech, Polish
- Evidentiality: Turkish, Quechua, Bulgarian, Tibetan
- Number (Dual): Fijian, Hawaiian, Slovenian, Sorbian

**Success Rate**: 95-99% accuracy when 8+ translations agree

**When to Use**: Features that are implicit in TBTA, have 3+ encoding languages, high inter-translator agreement

**Pitfalls to Avoid**:
- Using single translation as authoritative (need consensus)
- Ignoring minority views without investigation
- Using translations in languages that DON'T encode the feature
- Predicting from scratch when translation consensus is available

---

### 3. **Hierarchical Prompting Framework**
**Pattern**: Use prompt hierarchy prioritizing meaning over form, leveraging LLM strengths in theological/semantic reasoning.

**Evidence**:
- Person feature: Resolved 60-70% with theological analysis alone
- Aspect feature: 98.1% accuracy using 5-level hierarchy
- Number feature: Theological level (Trinity) = 95%+ accuracy

**Hierarchy Template**:
```
Level 1: THEOLOGICAL/SEMANTIC (60-70% resolution)
  → Divine prerogatives, salvific experiences, authority structures

Level 2: CAPABILITY/RESTRICTION (20% more)
  → "Can the addressee perform this action?"

Level 3: DISCOURSE FUNCTION (10% more)
  → Frame semantics, participant tracking, topic continuity

Level 4: GRAMMATICAL CUES (5% more)
  → Morphology, syntax, explicit markers

Level 5: BASELINE/RARITY (remaining)
  → Corpus statistics, dominant value defaults
```

**Prompt Structure**:
```
For {verse reference}, determine {feature_name}:

LEVEL 1 - Theological Analysis:
1. Does this involve divine action? (creation, judgment, omniscience)
2. Does this describe salvific experience? (justification, peace)
3. Is there an authority structure? (apostolic witness, divine command)
4. Does this express community identity? (unity, worship, shared faith)

Based on theological context: {value}
Confidence: High/Medium/Low
Reasoning: ...

If confidence < High, proceed to Level 2...
```

**Success Rate**: 85-90% with full 5-level hierarchy

**When to Use**: Any feature with ambiguity (Aspect, Mood, Voice, Number, Person)

---

### 4. **Capability Analysis as Primary Filter**
**Pattern**: The question "Can the addressee perform this action?" resolves most ambiguous cases.

**Evidence**:
- Person experiment: Filtered 60%+ of ambiguous situations
- Mood experiment: Distinguished authority levels
- Aspect experiment: Identified telicity differences

**Application**:
```
Capability Test:
1. Identify the specific action or state described
2. Can the addressee perform/participate in this action?

Questions:
- Is this within human capability? (walking, speaking, believing)
- Is this divine-only capability? (creating, omniscience, forgiving sins)
- Is this role-specific? (apostolic witness, priestly service)
- Is this shared experience? (suffering, joy, faith)

If NO (addressee cannot participate) → EXCLUSIVE
If YES (addressee can participate) → Continue to identity/group analysis
```

**Success Rate**: 90%+ when capability boundary is clear

**When to Use**: Person (clusivity), Mood (authority), Aspect (telicity), Voice (agent capability)

---

### 5. **The Rarity Principle (Baseline-First Approach)**
**Pattern**: Identify dominant value FIRST, then look for triggers to override. Only mark when semantically necessary.

**Evidence**:
- Aspect: 90.7% Unmarked (default), only 9.3% marked
- Number: ~70% singular, ~25% plural (baseline)
- Polarity: ~90% Affirmative (estimated)

**Application**:
```
For {verse}, predict {feature}:

Baseline: {dominant_value} (accounts for {X}% of cases)

Check for override triggers:
□ Theological factor? (e.g., divine action)
□ Discourse marker? (e.g., topic shift)
□ Grammatical trigger? (e.g., specific mood)
□ Semantic trigger? (e.g., action vs state)

If NO triggers → Use BASELINE with {X}% confidence
If 1 trigger → 60% confidence for override
If 2 triggers → 80% confidence
If 3+ triggers → 95% confidence

Never use rarity to guess unmarked values - use for baseline confidence only
```

**Success Rate**: 70-90% depending on baseline dominance

**When to Use**: Features with clear dominant value (Aspect, Polarity, Voice, Status, Mood)

**Critical Warning**: Do NOT use rarity principle to justify guessing at unmarked values. Use it to establish baseline confidence and prioritize analysis effort on marked cases.

---

### 6. **Gateway Features for Constraint Propagation**
**Pattern**: Check gateway feature FIRST to constrain predictions for dependent features.

**Evidence**:
- Mood → Aspect: Potential mood = 100% Inceptive aspect (6/6 cases)
- Mood → Time/Voice: Strong correlations observed
- Semantic Type → Person/Number: For nouns
- Genre → Structure/Force/Salience: For clauses

**Application**:
```
Gateway Analysis:

Step 1: Extract gateway value
Gateway: MOOD = {value}

Step 2: Apply known correlations
Correlations:
- Mood=Potential → Aspect=Inceptive (100% in sample)
- Mood=Indicative + Time=Historic Past → Aspect=Completive (high probability)

Step 3: Predict with gateway constraint
Based on gateway correlation:
- Strong (>90%) → High confidence prediction
- Moderate (70-89%) → Medium confidence
- Weak (<70%) → Cannot constrain, use other methods
```

**Gateway Features by Domain**:
- Verbs: MOOD → Aspect, Time, Voice
- Nouns: SEMANTIC TYPE → Person, Number
- Clauses: GENRE → Structure, Force, Salience

**Success Rate**: 90-100% when strong correlation exists

**When to Use**: Features that have known dependencies on other features

---

### 7. **Multi-Factor Convergence for High Confidence**
**Pattern**: Multiple independent factors agreeing dramatically increases confidence.

**Evidence**:
- Aspect Inceptive: 100% accurate (3/3) with 3-factor convergence:
  1. Action verb (semantic)
  2. Potential mood (grammatical)
  3. Near-future time (temporal)

**Confidence Formula**:
```
0 triggers → 30% (baseline only)
1 trigger → 60% (weak)
2 triggers → 80% (medium)
3+ triggers → 95%+ (strong)
```

**Application**:
```
Multi-Factor Analysis for {feature}:

FACTOR 1: {first factor type}
Analysis: ...
Prediction: {value_1}

FACTOR 2: {second factor type}
Analysis: ...
Prediction: {value_2}

FACTOR 3: {third factor type}
Analysis: ...
Prediction: {value_3}

CONVERGENCE:
- 3/3 agree → 95% confidence
- 2/3 agree → 80% confidence
- All disagree → Use baseline, flag for review (50%)
```

**Success Rate**: 95%+ when 3+ factors converge

**When to Use**: Marked values, edge cases, validation of predictions

---

### 8. **Adversarial Testing with 3-Phase Strategy**
**Pattern**: Design test sets to actively hunt for weaknesses, not confirm successes.

**Evidence**:
- All successful features used 3-phase testing
- Adversarial accuracy 60-70% expected (if higher, test wasn't hard enough)
- Random validation should exceed adversarial by 15-25 percentage points

**3-Phase Structure**:

**Phase 1: Pattern Discovery (15-20 verses)**
- All possible feature values (complete coverage)
- Clear, unambiguous cases (build confidence)
- 1-2 theological contexts
- Morphological diversity (Hebrew + Greek)
- Different genres (narrative, poetry, epistles)
- Analyze TBTA freely, document patterns, iterate to 90%+

**Phase 2: Adversarial Testing (10-15 verses)**
```
Actively hunt for edge cases:
- Theological edges (25%): Trinity, Incarnation, Messianic prophecies, corporate solidarity
- Rare values (25%): Values with 0-1 training occurrences, boundary cases
- Morphological exceptions (25%): Semantic ≠ morphological, fossilized forms
- Ambiguous cases (25%): Multiple valid readings, translation divergence

Process:
1. Design test set, commit to git
2. Make predictions WITHOUT checking TBTA
3. Document reasoning + confidence
4. Commit predictions with timestamp (lock, no modifications)
5. Check TBTA and calculate accuracy
6. Analyze failures in detail

Expected: 60-70% overall, 85%+ on high-confidence predictions
```

**Phase 3: Random Validation (10-15 verses)**
- Different books (not in training/adversarial)
- Stratified by feature value (representative distribution)
- No selection bias
- Expected: 80-90% (15-25 points higher than adversarial)

**Phase 4: Translation Validation** (when applicable)
- Test predictions against real Bible translations
- Languages that encode the feature
- Agreement levels validate confidence calibration

**Success Criteria**:
- Random > Adversarial by 15-25 points
- High-confidence predictions: 85%+
- State-level F1 > 0.85

**When to Use**: **EVERY feature** - Non-negotiable validation phase

---

### 9. **Discourse-Level Context Strategy (LLM Memory First)**
**Pattern**: For features requiring discourse memory, try LLM's built-in knowledge first before implementing full context tracking.

**Evidence**:
- Participant Tracking: 90% accuracy with LLM memory on well-known books
- Fast implementation: 2 weeks vs 4-6 weeks for full tracking
- Participant states: Routine (73%), Generic (14%), Frame Inferable (7.5%)

**Approach 1: LLM Memory (Recommended First)**
```
Based on your knowledge of {book} {chapter}:

DISCOURSE CONTEXT:
1. Who are the main participants in this chapter?
2. Where does each participant first appear?
3. Has "{entity}" been mentioned before?
   - If YES: In which verse? State (First Mention, Routine, Restaging)?
   - If NO: This is First Mention

For entity "{entity}" in current verse:
1. First mention? → First Mention (I)
2. Mentioned recently (3-5 verses)? → Routine (D)
3. Absent and now returns? → Restaging (R)

Confidence: High/Medium/Low (based on LLM memory strength)
```

**Expected**: 85-90% for well-known books, 2-week implementation

**Approach 2: Expanded Context Window (Fallback)**
- Load and process full chapters
- Maintain explicit entity registry
- Expected: 95-100%, 4-6 weeks implementation

**When to Use**: Participant Tracking, NounListIndex, Definiteness, Topic/Focus

**Decision Rule**: Try Approach 1 first (fast), add Approach 2 only where LLM memory insufficient

---

### 10. **Pattern Recognition Across Similar Contexts**
**Pattern**: Similar contexts produce consistent patterns. Once established, patterns reliably predict other cases.

**Evidence**:
- Divine Speech (creation/judgment) → EXCLUSIVE (100% in sample)
- Prayer to God → EXCLUSIVE of God (100%)
- Apostolic Witness → EXCLUSIVE (100%)
- Community Exhortation → INCLUSIVE (95%)

**Application**:
```
Established patterns from prior analysis:
[List patterns with reliability metrics]

For current verse:
Speaker: {speaker}
Addressee: {addressee}
Action: {action}

Questions:
1. Match any established pattern?
2. Which pattern?
3. Confidence based on pattern reliability?
4. Differences from pattern that might affect result?

Predicted value: ...
Confidence: {pattern_reliability}%
```

**Pattern Library Building**:
1. Document patterns during training phase
2. Track reliability across test sets
3. Note conditions for pattern applicability
4. Validate patterns on new contexts

**Success Rate**: 90-100% when pattern match is clear

**When to Use**: Features with recurring theological/discourse contexts

**Warning**: Validate ALL pattern conditions before applying - avoid overgeneralization

---

## Common Pitfalls to Avoid

### 1. **Theological Misunderstanding**
**Symptom**: Prediction doesn't match theological context
**Example**: Missing that creation is exclusively God's work in Gen 1:26
**Fix**: Add theological context questions to Level 1 prompts
**Critical Caution**: If theological concept is inferred from context but NOT morphologically present in source language, mark with metadata flag to avoid eisegesis. Document when interpretation goes beyond explicit marking.

### 2. **Morphological ≠ Semantic**
**Symptom**: Following morphology instead of meaning
**Example**: Hebrew dual suffix -ayim on "right hand" (singular in context due to injury/specificity)
**Fix**: Always check semantic analysis before morphological
**Frequency**: ~10% of errors in body part contexts

### 3. **Discourse Factor Missed**
**Symptom**: Ignoring context beyond single verse
**Example**: Marking "First Mention" when entity already introduced earlier in chapter
**Fix**: Add discourse context prompts, use LLM memory (Approach 1)
**Frequency**: ~15% of errors in participant tracking

### 4. **Gateway Feature Ignored**
**Symptom**: Predicting constrained feature without checking gateway
**Example**: Predicting Aspect without checking Mood first
**Fix**: Always check gateway features in prompt hierarchy

### 5. **Baseline Override Without Evidence**
**Symptom**: Predicting marked value without strong triggers
**Example**: Predicting Inceptive with only 1/3 triggers present
**Fix**: Require 2-3 converging factors before overriding baseline

### 6. **Pattern Overgeneralization**
**Symptom**: Applying pattern to dissimilar context
**Example**: Using "Apostolic Witness" pattern for non-apostolic speaker
**Fix**: Validate all pattern conditions before applying

### 7. **Missing TBTA Semantic Expansions**
**Symptom**: Forgetting that abstract/action nouns can be entities with number
**Example**: "all these things" → "things" is plural (multiple events/items)
**Fix**: Check if abstract/action nouns should have number marking
**Frequency**: ~15% of initial errors

### 8. **Generic vs Specific Confusion**
**Symptom**: Confusing generic categories with specific counted groups
**Example**: "people are like grass" (generic) vs "the people rejoiced" (specific group)
**Fix**: Check for definite articles, demonstratives, context specificity
**Frequency**: ~20% in collective noun contexts

---

## Feature-Specific vs Universal Patterns

### Universal Patterns (Apply to ALL Features)

1. **Tier 0 Check** (explicit encoding) - ALWAYS first step
2. **Translation Validation** (if 3+ encoding languages available) - Primary for implicit features
3. **Hierarchical Prompting** (theological → semantic → grammatical) - Core methodology
4. **3-Phase Adversarial Testing** - Non-negotiable validation
5. **Multi-Factor Convergence** - Confidence calibration
6. **Error Analysis Documentation** - Learning loop

### Feature-Specific Patterns

**Person/Clusivity**:
- Translation Validation PRIMARY (98% agreement across 9 languages)
- Capability Analysis essential
- Speaker-addressee relationship analysis

**Aspect**:
- Gateway Feature: Check Mood first
- Rarity Principle: 90.7% Unmarked baseline
- Telicity analysis (completability of action)

**Number**:
- Hierarchical: Theological (Trinity) → Semantic (counts) → Morphological (Hebrew -ayim)
- Body part context checking (injury/specificity overrides dual)
- Generic vs specific distinction

**Participant Tracking**:
- LLM Memory approach first (85-90% accuracy, 2 weeks)
- 5-state simplified system covers 100% of active annotations
- Frame semantics database for Frame Inferable

**Mood**:
- Tier 0: Explicit encoding (100% extraction accuracy)
- No prediction needed

**Illocutionary Force**:
- Particle systems analysis (East Asian languages)
- Register variation (imperative forms)
- Rhetorical vs information-seeking questions
- Honorific system interactions

**Proximity**:
- Demonstrative form analysis (Greek/Hebrew)
- Spatial vs temporal vs discourse classification
- Context clues for visibility, speaker/listener positions

---

## Recommended Agent Coordination Strategies

### Strategy 1: Sequential Pipeline (High Dependency Features)
**When**: Features have strong gateway relationships (Mood → Aspect)

```
Agent 1 (Researcher): Extract gateway feature (Mood)
  ↓
Agent 2 (Analyzer): Apply gateway constraints
  ↓
Agent 3 (Predictor): Predict target feature (Aspect) with constraints
  ↓
Agent 4 (Validator): Test predictions, analyze errors
```

**Coordination**: Memory-based handoffs, each agent stores results for next

### Strategy 2: Parallel with Consensus (Independent Factors)
**When**: Multi-factor convergence needed

```
Agent 1 (Theological Analyst): Analyze theological factors
Agent 2 (Semantic Analyst): Analyze semantic factors  } Parallel
Agent 3 (Grammatical Analyst): Analyze grammatical factors

Agent 4 (Synthesizer): Aggregate predictions, calculate convergence confidence
```

**Coordination**: All agents run concurrently, synthesizer checks agreement

### Strategy 3: Iterative Refinement (Complex Features)
**When**: Feature requires multiple rounds (Translation Validation + Hierarchical Prompts)

```
Round 1: Translation Validation Agent (discover consensus)
  ↓ (If low confidence or divergence)
Round 2: Hierarchical Prompt Agent (theological analysis)
  ↓ (If still ambiguous)
Round 3: Multi-Factor Agent (convergence checking)
```

**Coordination**: Each round stores findings, next round uses prior context

### Strategy 4: Swarm Testing (Adversarial Phase)
**When**: Adversarial test set design and execution

```
Agent 1: Theological Edge Case Hunter
Agent 2: Rare Value Hunter          } Design test set in parallel
Agent 3: Morphological Exception Hunter
Agent 4: Ambiguity Hunter

Agent 5 (Blind Predictor): Make predictions without checking TBTA
Agent 6 (Validator): Compare to TBTA, calculate metrics
Agent 7 (Error Analyst): Categorize failures, extract learnings
```

**Coordination**: Hunters contribute to shared test set, sequential prediction/validation

### Coordination Best Practices

1. **Memory Keys**: Use consistent namespace structure
   ```
   swarm/{feature}/gateway/{gateway_feature}
   swarm/{feature}/predictions/{verse_ref}
   swarm/{feature}/validation/{phase}
   swarm/{feature}/patterns/{pattern_name}
   ```

2. **Hooks Integration**:
   - pre-task: Restore prior session state
   - post-edit: Store intermediate results
   - post-task: Export metrics, update shared patterns

3. **Confidence Propagation**: Each agent must report confidence levels for downstream decisions

4. **Error Sharing**: Failed predictions stored in memory for all agents to learn from

---

## Quick Reference: High-Accuracy Formula

```
High Accuracy =
  Tier 0 Check (explicit extraction)
  + Translation Validation FIRST (discover from consensus, 95-99%)
  + Gateway Features (check dependencies)
  + Hierarchical Prompts (theology → semantics → grammar, 85-90%)
  + Rarity Principle (establish baseline, 70-90%)
  + Multi-Factor Convergence (2-3 triggers for marked values, 95%+)
  + Discourse Context (LLM memory when needed, 85-90%)
  + 3-Phase Adversarial Testing (find weaknesses early)
```

**Priority Order for Implicit Features**:
1. **Translation Validation** (if 3+ encoding languages): 95-99% accuracy
2. **Hierarchical Prompts** (if no encoding languages): 85-90% accuracy
3. **Multi-Factor Convergence** (validation): Confirm with 2-3 independent factors

---

## Integration with STAGES.md Workflow

**Stage 1 (Research)**:
- Use Tier 0 check, hierarchical prompts
- Check for explicit encoding
- Establish baseline via rarity principle
- Identify gateway features
- Research encoding languages for translation validation

**Stage 2 (Algorithm)**:
- Apply gateway features first
- Implement multi-factor convergence
- Build pattern recognition library
- Design translation validation workflow

**Stage 3 (Testing)**:
- 3-phase adversarial testing (training → adversarial → random)
- Translation validation against real Bibles
- Confidence calibration (high/medium/low accuracy by category)

**Stage 4 (Refinement)**:
- Error analysis by category
- Pattern updates based on failures
- Threshold tuning (convergence requirements)

**Stage 5 (Documentation)**:
- Document learnings for future features
- Update reusable patterns library
- Note feature-specific vs universal insights

**Stage 6 (Production)**:
- Deploy with confidence calibration
- Flag low-confidence predictions for review
- Monitor accuracy on new books

---

## Key Insights by Feature Type

### Explicit Features (Tier 0)
**Examples**: Mood, Part of Speech, some Time markers

**Approach**: Direct extraction from YAML
**Expected Accuracy**: 95-100%
**Time to Implement**: 1-2 days
**Key Learning**: Always check first - saves weeks of unnecessary work

### Implicit with Encoding Languages (Translation Validation)
**Examples**: Person (clusivity), Number (dual), Aspect (perfective/imperfective)

**Approach**: Translation consensus discovery
**Expected Accuracy**: 95-99% with 8+ translations
**Time to Implement**: 2-3 weeks (gathering translations + consensus algorithm)
**Key Learning**: Don't predict what translators have already decided

### Implicit without Encoding Languages (Hierarchical Prompts)
**Examples**: Some Aspect values, structural features

**Approach**: 5-level hierarchical prompting
**Expected Accuracy**: 85-90%
**Time to Implement**: 3-4 weeks (prompt development + validation)
**Key Learning**: Theology and semantics are more reliable than grammar alone

### Discourse-Dependent Features (LLM Memory)
**Examples**: Participant Tracking, Definiteness, Topic/Focus

**Approach**: LLM memory first, full tracking as fallback
**Expected Accuracy**: 85-90% (LLM), 95-100% (full tracking)
**Time to Implement**: 2 weeks (LLM) vs 4-6 weeks (full)
**Key Learning**: Fast implementation often sufficient; don't over-engineer

---

## Success Metrics and Targets

### Accuracy Targets by Confidence Level
```
High Confidence Predictions: 85%+ accuracy
Medium Confidence Predictions: 70-80% accuracy
Low Confidence Predictions: 50-65% accuracy
Overall System Accuracy: 80-85%
```

### Test Set Requirements
```
Training Set: 15-20 verses (complete coverage, clear cases)
Adversarial Set: 10-15 verses (edge cases, expected 60-70%)
Random Validation: 10-15 verses (representative, expected 80-90%)
Translation Validation: 3-9 languages (when applicable, 95-99% consensus)
```

### State-Level Metrics
```
Precision: TP / (TP + FP) → Target >0.85
Recall: TP / (TP + FN) → Target >0.85
F1 Score: 2 * (P * R) / (P + R) → Target >0.85
```

### Confidence Calibration Check
```
High confidence predictions should achieve 85%+ accuracy
If high confidence < 80% accurate → Recalibrate thresholds
If low confidence > 70% accurate → System is too conservative
```

---

## Implementation Timeline Estimates

**Tier 0 Feature** (Explicit extraction):
- Research: 1-2 days
- Implementation: 1-2 days
- Testing: 1-2 days
- **Total: 3-6 days**

**Translation Validation Feature** (Implicit with encoding languages):
- Research: 3-5 days (identify languages, sources)
- Implementation: 7-10 days (API integration, consensus algorithm)
- Testing: 5-7 days (3-phase + translation validation)
- **Total: 2-3 weeks**

**Hierarchical Prompting Feature** (Implicit without encoding languages):
- Research: 5-7 days (theological analysis, pattern discovery)
- Implementation: 10-14 days (prompt development, gateway features)
- Testing: 7-10 days (3-phase adversarial)
- **Total: 3-4 weeks**

**Discourse-Dependent Feature** (LLM Memory approach):
- Research: 3-5 days (understand discourse requirements)
- Implementation: 7-10 days (LLM memory prompts, state detection)
- Testing: 5-7 days (validation, coherence checking)
- **Total: 2-3 weeks**

**Complex Feature** (Multiple dependencies + discourse):
- Research: 7-10 days
- Implementation: 14-21 days
- Testing: 10-14 days
- **Total: 4-6 weeks**

---

## Notes on Unvalidated Claims

Patterns marked as "consider," "expected," or "estimated" have not been fully validated:

- Baseline percentages for features other than Aspect (Polarity ~90%, Voice ~70%) are theory-based estimates
- Discourse context accuracy (85-90% with LLM memory) are projections from limited testing
- Some cross-linguistic validation confidence levels based on Person experiment only
- Feature-specific patterns need validation before claiming reliability

**Always test patterns on your specific feature before claiming accuracy.**

---

## Critical Reminders for New Features

### DO:
- Check Tier 0 first (explicit encoding) - saves weeks
- Use translation validation when 3+ encoding languages available (95-99% accuracy)
- Start with theological/semantic analysis (Level 1 hierarchical prompts)
- Design adversarial test sets to find weaknesses (expect 60-70%)
- Make predictions blind before checking TBTA (lock with git commit)
- Document all errors and learnings for future features
- Report confidence levels honestly (high/medium/low)
- Use LLM memory first for discourse features (2 weeks vs 4-6 weeks)

### DON'T:
- Skip Tier 0 check - always verify explicit encoding first
- Predict from scratch when translation consensus available
- Skip hierarchical levels (always start at theological/semantic Level 1)
- Ignore gateway features (check dependencies first)
- Override baseline without 2-3 converging triggers
- Use rarity principle to justify guessing unmarked values
- Look at TBTA answers before making predictions (breaks validation)
- Claim 100% accuracy on small samples (<15 verses)
- Report only best-case accuracy (need adversarial + random + translation validation)
- Over-engineer discourse tracking (try LLM memory first)

---

**Status**: Consolidated from 4 archived features + central learnings README
**Last Updated**: 2025-11-16
**Next Action**: Apply patterns to active TBTA features in development

**Key Files Referenced**:
- `/workspace/bible-study-tools/tbta/learnings/README.md` (primary source)
- `/workspace/bible-study-tools/tbta/features/features-archive/illocutionary-force/LEARNINGS.md`
- `/workspace/bible-study-tools/tbta/features/features-archive/participant-tracking/experiments/LEARNINGS.md`
- `/workspace/bible-study-tools/tbta/features/features-archive/number-system/experiments/LEARNINGS.md`
- `/workspace/bible-study-tools/tbta/features/features-archive/proximity-system/experiments/LEARNINGS.md`
