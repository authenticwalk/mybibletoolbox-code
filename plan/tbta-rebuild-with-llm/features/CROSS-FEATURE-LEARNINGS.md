# Cross-Feature Learnings: Universal Patterns in TBTA Annotation

**Purpose**: Document patterns, methodologies, and insights that apply across multiple TBTA features.

**Source Experiments**:
- number-systems/experiment-001.md (91.4% accuracy)
- degree/experiment-001.md (in progress)
- Additional feature experiments

---

## Universal Principle 1: Semantic Encoding Over Morphological Form

### Pattern
**TBTA prioritizes SEMANTIC meaning over source language MORPHOLOGICAL markers.**

### Evidence

#### Number Systems (experiment-001)
- Hebrew שָׁמַיִם (shamayim) has dual morphology (-ayim suffix) → TBTA marks **Singular**
- Hebrew מַיִם (mayim) has dual morphology → TBTA marks **Singular**
- Greek οὐρανῶν (ouranōn) is genitive plural → TBTA marks **Singular**
- **Conclusion**: "How many entities?" matters more than "what's the grammatical form?"

#### Degree (CONFIRMED - Phase 7 validation)
- Greek μεγάλη (positive form) with superlative question → TBTA marks **Superlative** ✓
- Greek μείζων (comparative form) with implied superlative ("no one greater") → TBTA marks **Superlative** ✓
- Hebrew מִן construction (not morphological comparative) → Should mark **C** (Comparative)
- **Confirmed**: Semantic meaning (explicit AND implied) takes priority over morphological form
- **Nuance**: TBTA recognizes LOGICAL EQUIVALENCES (negative comparative = superlative)

### Application Rule
```
When predicting TBTA values:
1. Determine semantic meaning FIRST (how many? how much comparison?)
2. Check morphological form SECOND (for confirmation, not primary)
3. If semantic ≠ morphological, ALWAYS choose semantic
```

### Cross-Feature Implications
- **Person**: Semantic role > morphological person agreement
- **Proximity**: Semantic distance > demonstrative form
- **Polarity**: Semantic negation scope > negative morphology
- **Time**: Discourse-relative time > tense morphology

---

## Universal Principle 2: Theological Knowledge Required for Biblical Texts

### Pattern
**TBTA incorporates theological interpretation for doctrinally significant passages.**

### Evidence

#### Number Systems: Trinity = Trial
- Genesis 1:26 "Let us make..." → God marked as **Trial + First Inclusive**
- NO morphological trial marker in Hebrew/Greek
- **Requires**: Knowledge that Trinity = Father, Son, Spirit = 3 persons
- **Accuracy**: 100% match when theological context identified

### Application Rule
```
For Biblical texts specifically:
1. Identify theologically significant passages (Trinity, incarnation, etc.)
2. Apply doctrinal interpretation where relevant
3. Document these as special cases requiring theological tagging
```

### Recommended Theological Tags
- **Trinity contexts**: Gen 1:26, Matt 3:16-17, Matt 28:19, 2 Cor 13:14
- **Incarnation contexts**: John 1:1-14 (dual nature of Christ)
- **Messianic prophecies**: May affect participant identification
- **Corporate solidarity**: Israel/Church as singular or plural

### Cross-Feature Implications
- **Number**: Trinity = Trial
- **Person**: Trinity first inclusive plural
- **Participant Tracking**: God as singular vs. plural across contexts

---

## Universal Principle 3: Discourse Role Determines Feature Values

### Pattern
**Same referent can have DIFFERENT feature values depending on DISCOURSE ROLE.**

### Evidence

#### Number Systems: God in Genesis 1:26
- God as **narrator** → Singular Third person
- God as **speaker** ("Let us make") → Trial First Inclusive
- **Same entity, different numbers based on discourse role**

#### Number Systems: Nicodemus in John 3:2
- Nicodemus as **individual** → Singular
- Nicodemus as **group speaker** ("we know") → Plural First Exclusive
- **Same person, different numbers based on speaking role**

### Application Rule
```
When tracking participants:
1. Identify EACH occurrence's discourse role
2. Assign features PER ROLE, not per entity identity
3. Track role transitions (narrator → speaker, individual → representative)
```

### Cross-Feature Implications
- **Number**: Role-based assignment
- **Person**: Role determines person (narrator = 3rd, speaker = 1st)
- **Participant Tracking**: First mention, routine, restaging across roles
- **Surface Realization**: Role affects pronoun/noun choice

---

## Universal Principle 4: Systematic Testing Methodology

### The Gold Standard Approach (from number-systems/experiment-001)

#### Phase 1: Prediction Before Data
```
For each test verse:
1. List ALL constituents that could have the feature
2. For EACH constituent, predict ALL possible values
3. Document detailed REASONING for each prediction
4. Identify KEY UNCERTAINTIES explicitly
5. Record ALTERNATIVE predictions where uncertain
```

#### Phase 2: Check Against TBTA
```
For each prediction:
1. Retrieve actual TBTA annotation
2. Mark as MATCH ✅ or MISMATCH ❌
3. For mismatches, document:
   - What was predicted
   - What TBTA actually marked
   - Why the mismatch occurred
   - What pattern this reveals
```

#### Phase 3: Exhaustive Debugging for Mismatches (TARGET: 100% ACCURACY)
```
For EACH mismatch, debug exhaustively:

Step 1: Verify Data Accuracy
- [ ] Confirm verse reference is correct
- [ ] Verify TBTA data extraction (correct feature, correct constituent)
- [ ] Check for data corruption or version mismatch

Step 2: Re-analyze Source Text
- [ ] Re-examine Greek/Hebrew morphology (synthetic forms, particles)
- [ ] Check interlinear translations for semantic meaning
- [ ] Consult lexicons for alternate meanings
- [ ] Review grammatical commentaries

Step 3: Re-analyze Context
- [ ] Expand context window (preceding/following verses)
- [ ] Check discourse structure (paragraph, chapter)
- [ ] Identify any theological/cultural factors
- [ ] Review parallel passages

Step 4: Cross-Reference Multiple Sources
- [ ] Check 3+ English translations
- [ ] Check 2+ scholarly commentaries
- [ ] Consult target language examples (if available)
- [ ] Review linguistic databases (WALS, Glottolog)

Step 5: Test Alternative Hypotheses
- [ ] Could TBTA be using a different algorithm?
- [ ] Is there a valid alternative interpretation?
- [ ] Does this reveal a new pattern we missed?
- [ ] Is this an edge case requiring special handling?

Step 6: Make Final Determination
If after Steps 1-5, our prediction STILL seems more accurate:
→ Flag as POTENTIAL TBTA ERROR for team review
→ Document comprehensive analysis in potential-errors/ folder

If TBTA annotation is defensible:
→ Document as LEARNED PATTERN
→ Update algorithm to handle this case
→ Reclassify prediction methodology
```

#### Phase 4: Pattern Analysis
```
Across all results:
1. Calculate accuracy by value type
2. Identify systematic patterns in matches
3. Identify systematic patterns in mismatches
4. Document edge cases and uncertainties
5. Create refined algorithm
6. Isolate potential TBTA errors vs. methodology gaps
```

#### Phase 5: Secondary Findings
```
Document where languages/translations might disagree:
1. Morphological vs semantic disagreements
2. Cultural interpretation differences
3. Theological interpretation variations
4. Ambiguous cases requiring translator choice
```

### Success Metrics
- **Target accuracy**: 100% (either match or potential TBTA error flagged)
- **Learned patterns**: 95%+ accuracy (confirmed algorithm works)
- **Potential TBTA errors**: Flagged with exhaustive analysis
- **High confidence patterns**: 95%+ accuracy
- **Medium confidence patterns**: 70-90% accuracy
- **Low confidence patterns**: Flagged for human review

---

## Universal Principle 5: Scale Testing Required for Rare Value Discovery

### Pattern
**Some TBTA values are RARE and require EXTENSIVE TESTING (100+ verses) to discover.**

⚠️ **CRITICAL LEARNING**: Initial small-scale validation (7-12 verses) can INCORRECTLY conclude rare values don't exist!

### Evidence

#### Number Systems
- **Quadrial**: Theoretically exists, but NOT FOUND in test verses
- **Paucal**: Defined but needs specific count contexts (4-10)
- **Trial**: ONLY for Trinity contexts (theologically derived)

#### Degree - Phase 7-8 vs Phase 10 CORRECTION

**After 7-12 verses (Phase 7-8) - INCORRECT CONCLUSIONS**:
- **q (equative)**: ✅ CONFIRMED non-existent (still true after 100 verses)
  - PHP 2:6, MAT 10:25 → Both "No Degree"
- **i (intensified comparative)**: ❌ INCORRECTLY thought non-existent
- **s (superlative of 2)**: ❌ INCORRECTLY thought non-existent
- **E (extremely intensified)**: ❌ INCORRECTLY thought non-existent (lexical theory)
- **T (excessive "too")**: ❌ INCORRECTLY thought non-existent
- **L ('less')**: ❌ Unknown status

**After 100 verses (Phase 10) - CORRECTED**:
- **i (Intensified Comparative)**: ✅ **EXISTS** - Found in 4 verses
  - MAT 10:31, 1SAM 13:6, 2SAM 7:19, DAN 1:20, 3:19
  - Pattern: Numerical intensifiers (7x, 10x) + comparative
- **s (Superlative of 2 items)**: ✅ **EXISTS** - Found in 4 verses
  - GEN 27:15, 27:42, 29:18, 48:19
  - Pattern: Selection from exactly 2 items (older/younger of 2 sons/daughters)
- **E (Extremely Intensified)**: ✅ **EXISTS** - Found in 18+ verses
  - GEN 6:11-12, 25:29-32, EPH 1:6-18, PSA 14:5
  - Pattern: Extreme emotional states, hyperbolic contexts, theological emphasis
- **T ('too' excessive)**: ✅ **EXISTS** - Found in 12+ verses
  - GEN 4:13, 18:11-12, ACT 2:8, RUT 1:11
  - Pattern: Beyond capacity/ability ("too old to bear children")
- **L ('less')**: ✅ **EXISTS** - Found in 3 verses
  - GEN 8:1, 8:3, 8:5
  - Pattern: Progressive decrease (flood waters receding)

### Key Insight: Discovery Timeline

| Verses Tested | Values Found | Missing Values |
|---------------|--------------|----------------|
| **7 verses** | C, S, I, '''least''' | i, E, L, T, s (assumed non-existent) |
| **12 verses** | Same + errors identified | i, E, L, T, s (still assumed non-existent) |
| **41 verses** | + i, T, 'least' | E, L, s (assumed non-existent) |
| **71 verses** | + E, L, 'less', 'too' | s (assumed non-existent) |
| **100 verses** | + s | ✅ **ALL VALUES FOUND** |

**Lesson**: Rare values appear at rates of 1-4 instances per 100 verses. Small-scale testing CANNOT find them!

### Application Rule
```
When encountering rare values:
1. DON'T assume non-existence from small samples (<50 verses)
2. Design SCALE TESTING (100+ verses) across diverse books
3. Test iteratively in batches (commit after each improvement)
4. Correct earlier conclusions as new data emerges
5. Document value discovery timeline
6. Final confirmation requires comprehensive corpus coverage
```

### Testing Methodology: Iterative Batch Approach

**Proven successful in Phase 10**:
1. **Batch 1** (verses 8-20): Expose algorithm weaknesses, discover new errors
2. **Batch 2** (verses 21-50): Hunt for first rare values (i, T found)
3. **Batch 3** (verses 51-80): Complete rare value search (E, L found)
4. **Batch 4** (verses 81-100): Edge cases and final discoveries (s found)

**Commit after each batch** - Push to remote after each improvement

### Cross-Feature Implications
- **All features**: Small-scale validation (10-20 verses) insufficient for rare values
- **Methodology**: Require 100+ verse testing for complete value inventory
- **Timeline**: Expect iterative discovery across multiple batches
- **Documentation**: Update earlier conclusions as scale testing progresses
- **Confidence**: Only declare "non-existent" after 100+ diverse verses tested

---

## Universal Principle 6: Context Window Matters

### Pattern
**Multi-verse context often required for accurate annotation.**

### Evidence

#### Participant Tracking
- First mention vs. routine reference requires tracking across verses
- Cannot determine from single verse alone

#### Discourse Genre
- Genre affects register, verb selection, clause structure
- Requires paragraph-level context

#### Time Granularity
- Discourse-relative anchoring (yesterday from narrator's perspective)
- Requires understanding narrative timeline

### Application Rule
```
When annotating:
1. Determine MINIMUM context window needed
2. For discourse features: Paragraph level minimum
3. For participant tracking: Multi-verse tracking
4. For morphological features: Single verse may suffice
```

---

## Universal Principle 7: Lexical vs. Syntactic Distinction

### Pattern
**TBTA only marks SYNTACTIC (grammatical) modification, not LEXICAL (inherent) meaning.**

### Evidence

#### Degree: Intensification
- **Syntactic intensifier** (λίαν "very" + πρωῒ "early") → TBTA marks "Intensified" ✓
- **Lexical compound** (ὑπερεκπερισσοῦ "abundantly" - triple compound) → TBTA marks "No Degree" ✓
- **Key distinction**: TWO WORDS (modifier + modified) vs. ONE WORD (compound meaning)

#### Linguistic Reasoning
- SYNTACTIC: Grammatical modification (can be removed without changing core word)
  - "very early" → Remove "very" → Still "early"
  - Degree is ADDED BY MODIFIER
- LEXICAL: Inherent word meaning (cannot be decomposed)
  - "abundantly" → No parts to remove → Single semantic unit
  - Intensity is PART OF WORD MEANING

### Application Rule
```
When identifying feature-bearing constituents:
1. Check if feature is SYNTACTIC (grammatical construction)
2. Or if feature is LEXICAL (inherent to word meaning)
3. TBTA marks SYNTACTIC only, not lexical
4. Lexicalized features → Treat as base/default value
```

### Cross-Feature Implications
- **Degree**: Only syntactic intensifiers (λίαν), not lexical compounds (ὑπερεκπερισσοῦ)
- **Comparison**: Syntactic comparative particles, not lexical "better/worse" meaning
- **Negation**: Syntactic negation markers, not lexical negative words?
- **Modality**: Syntactic modal markers, not lexical modal verbs?

**Discovery**: This may explain why many compound/derived words get "default" values in TBTA

---

## Universal Principle 8: Dual Value Encoding System

### Pattern
**TBTA uses BOTH standardized category values AND literal quoted string values.**

### Evidence

#### Degree Values
**Standardized values** (most common):
- "No Degree" (not "N")
- "Comparative" (not "C")
- "Superlative" (not "S")
- "Intensified" (not "I")

**Literal quoted values** (specific meanings):
- `'''least'''` (not "Superlative" or "l") - for ἐλάχιστος
- Possibly `'''greater'''`, `'''more'''` (not confirmed)

### Linguistic Reasoning
- **Standardized**: Generic category (upward superlative, downward superlative → both "Superlative")
- **Literal**: Specific directional or emphatic meaning (downward → `'''least'''`)
- **Purpose**: Preserves semantic nuance while maintaining category structure

### Application Rule
```
When validating TBTA values:
1. First check standardized values ("No Degree", "Comparative", etc.)
2. If mismatch, check for literal quoted values ('''word''')
3. Literal values use triple single quotes in YAML
4. Algorithm may need to handle BOTH encoding types
```

### Cross-Feature Implications
- **Other features may use dual encoding**: Need to check across features
- **Validation logic**: Must handle both standardized and quoted strings
- **Prediction difficulty**: Cannot predict literal values without seeing all examples
- **Value inventory**: More complex than single-letter codes suggest

**Discovery**: TBTA encoding is more granular than initially documented

---

## Universal Principle 9: Semantic Gradability Constraint

### Pattern
**TBTA only marks features on constituents that are SEMANTICALLY COMPATIBLE with that feature.**

### Evidence

#### Degree: Gradability Check
- **Gradable adjective** ("great", "small", "good") in comparative context → Gets degree marking ✓
- **Non-gradable adjective** ("justified", "dead", "perfect") in comparative context → "No Degree" ✓
- **Key distinction**: Can the word logically vary in degree? ("very justified" = nonsense)

#### Linguistic Reasoning
- **Gradable**: Properties that can vary (size, quality, time, intensity)
  - "very great", "more great", "greatest" - all semantically valid
- **Non-gradable**: Binary states, absolute properties, identity predicates
  - "very justified" - theologically/logically invalid (justified or not)
  - "very dead" - logically invalid (dead or alive)
  - "very perfect" - logically invalid (perfect is absolute)

### Application Rule
```
Before assigning feature value:
1. Check if constituent is semantically compatible with feature
2. For degree: Can you say "very X" or "more X"?
3. For number: Can entity be counted or is it abstract?
4. For time: Does event have temporal extent?
5. If NOT compatible → Assign default/null value, skip feature
```

### Cross-Feature Implications
- **Degree**: Only gradable words (not "justified", "dead", "perfect")
- **Number**: Only countable entities (not "wisdom", "love" as abstract)
- **Time**: Only temporal events (not timeless truths)
- **Proximity**: Only spatial entities (not abstract concepts)

**Discovery**: Structural comparisons (παρ' ἐκεῖνον "rather than") don't create degree marking on non-gradable words

---

## Universal Principle 10: Context-Dependent Feature Assignment

### Pattern
**Same morphological construction can map to DIFFERENT feature values based on semantic CONTEXT.**

### Evidence

#### Degree: Hebrew מִן Constructions (Phase 10 discovery)

Hebrew מִן can mark comparison, but maps to 3 different degree values based on context:

**→ Comparative (C)**:
- GEN 7:20: "15 cubits above/more than" (waters rising)
- Context: Rising, increasing, growing
- Semantic: Relative comparison with increase

**→ 'too' (T) - Excessive**:
- GEN 4:13: "Too great to bear" (מִנְּשֹׂא)
- Context: Beyond capacity, inability
- Semantic: Excessive degree → impossibility

**→ 'less' (L) - Progressive Decrease**:
- GEN 8:1, 8:3, 8:5: Waters "became less deep" (flood receding)
- Context: Decreasing, receding, diminishing
- Semantic: Progressive decrease (not comparison)

### Key Insight: Morphology + Context → Feature Value

```
Same form + different context = different values
מִן + rising verb = Comparative
מִן + capacity expression = 'too' (excessive)
מִן + decreasing verb = 'less' (progressive decrease)
```

### Linguistic Reasoning
- **Morphological marker** identifies CATEGORY (comparison/degree)
- **Semantic context** determines SPECIFIC VALUE within category
- **Verb semantics** critical: increase vs decrease vs ability
- **Cannot predict from morphology alone** - context analysis required

### Application Rule
```
For context-dependent constructions:
1. Identify morphological marker (מִן, comparative suffix, etc.)
2. Analyze semantic context (verb type, discourse role)
3. Check for specific triggers:
   - Capacity expressions → Excessive/inability
   - Progressive change → Increase vs decrease
   - Set size → Superlative vs comparative
4. Map construction + context → Specific feature value
5. Test multiple verses to validate pattern
```

### Additional Context-Dependent Patterns (Phase 10)

#### Set Size Determines Degree Type
- **2 items + selection** → "Superlative of 2 items" (s)
  - GEN 27:15: "The older (of 2 sons)" - Jacob and Esau
  - GEN 29:18: "The younger (of 2 daughters)" - Leah and Rachel
- **2 items + general comparison** → Comparative (C)
  - GEN 19:31: "Older than custom"
- **3+ items + selection** → Superlative (S)
  - GEN 43:33: "From oldest to youngest" (12 brothers)

#### Discourse Type Affects Intensification
- **Narrative contexts** → Standard degrees (C, S, I)
- **Poetic contexts** → Clustering of Intensified/Extremely Intensified
  - EXO 15:14-15: Multiple "afraid" with Intensified
  - PSA 14:5: Extremely Intensified in parallelism
- **Epistolary/theological contexts** → Extremely Intensified clusters
  - EPH 1:6-18: 5× Extremely Intensified for God's grace

### Cross-Feature Implications
- **All features**: Context determines value assignment, not just morphology
- **Requires**: Semantic analysis + discourse analysis + morphological analysis
- **Testing**: Need diverse contexts for same construction (rising vs decreasing, 2 items vs 3+ items)
- **Algorithm complexity**: Multi-step decision trees with context checks
- **Documentation**: Pattern libraries per construction type

---

## Universal Principle 11: Mixed Annotations Are Common

### Pattern
**Same constituent can receive MULTIPLE feature values SIMULTANEOUSLY in a single verse.**

⚠️ **CRITICAL LEARNING**: Mixed annotations are NOT exceptional edge cases - they're common patterns (20+ instances in 100 verses)

### Evidence

#### Degree: Multiple Degrees on Same Word (Phase 10 discovery)

**GEN 18:11** - "old" receives BOTH values:
- "old": **Intensified** (Sarah and Abraham were very old)
- "old": **'too'** (Sarah too old to bear children)
- **Pattern**: Same word, two semantic aspects (intensity + excessive)

**EXO 10:14** - "great" receives BOTH values:
- "great": **Superlative** (greatest plague ever)
- "great": **Comparative** (greater than before)
- **Pattern**: Superlative scope + comparative contrast

**EXO 11:6** - "loudly" receives THREE annotations:
- "loudly": **Intensified** (very loud)
- "loudly": **Comparative** (louder than before)
- "loudly": **Comparative** (louder than will be)
- **Pattern**: Intensity + temporal comparisons (past and future)

**EST 1:5** - "important" receives FOUR annotations:
- "important": **'least'** (from least)
- "important": **Superlative** (to greatest)
- "important": **'least'** (repeated in parallel)
- "important": **Superlative** (repeated in parallel)
- **Pattern**: Merism (least to greatest = everyone), with parallel repetition

### Key Patterns in Mixed Annotations

**Pattern 1: Multiple Semantic Aspects**
- Same word can be BOTH intensified AND excessive
- Same word can be BOTH superlative AND comparative
- Each aspect gets separate annotation

**Pattern 2: Repetition Gets Separate Annotations**
- Each instance of repeated word annotated independently
- Even if same semantic value, each instance marked
- Parallelism results in duplicate annotations

**Pattern 3: Complex Contexts Trigger Multiple Values**
- Temporal comparisons: past vs future → multiple comparatives
- Scope differences: superlative among all + comparative to one
- Merism structures: minimum + maximum both marked

### Linguistic Reasoning
- **TBTA annotates semantic aspects independently**
- **Each occurrence treated separately** (not merged)
- **Multiple truths can coexist** (very old AND too old)
- **Not an error** - reflects semantic richness

### Application Rule
```
For mixed annotation handling:
1. DON'T assume one value per constituent
2. Analyze ALL semantic aspects independently
3. Check for:
   - Multiple semantic dimensions (intensity + excess)
   - Repetition requiring separate annotations
   - Complex contexts with multiple comparisons
4. Algorithm must support:
   - Multiple values per constituent
   - List/array of degree values, not single value
   - Independent evaluation of each semantic aspect
5. Validation must check:
   - Partial matches (got 1 of 2 values)
   - Complete matches (got all values)
   - Order independence (values may appear in any order)
```

### Implementation Impact

**Algorithm structure**:
```python
# WRONG: Single value per constituent
constituent.degree = "Comparative"

# RIGHT: Multiple values per constituent
constituent.degrees = ["Intensified", "'too'"]
```

**Validation logic**:
```python
# Must handle:
predicted = ["Intensified"]
actual = ["Intensified", "'too'"]
# → Partial match, not complete failure
```

### Cross-Feature Implications
- **All features**: Check if multiple values possible
- **Validation**: Partial match scoring needed
- **Algorithm**: Must output lists/sets, not single values
- **Accuracy metrics**: Precision/recall, not just exact match
- **Testing**: Design verses with mixed annotations intentionally

---

Based on successful experiments, here's the universal template:

### Step 1: Identify Feature Candidates
```
Scan verse for all constituents that could have this feature:
- Part of speech filtering
- Semantic category filtering
- Discourse role filtering
```

### Step 2: Semantic Analysis (PRIORITY)
```
For each candidate:
- Determine semantic meaning (entities, comparison, negation, etc.)
- Check discourse context
- Identify theological significance
- Result: Semantic value
```

### Step 3: Morphological Validation
```
For each candidate:
- Check source language morphology
- Identify explicit markers
- Note mismatches with semantic analysis
- Result: Morphological support or conflict
```

### Step 4: Resolve Conflicts
```
If semantic ≠ morphological:
- ALWAYS prefer semantic interpretation
- Document the mismatch as learning
- Check if pattern applies cross-linguistically
```

### Step 5: Apply Special Rules
```
Check for:
- Theological contexts (Trinity, incarnation, etc.)
- Discourse role transitions
- Cross-linguistic rare values
- Target language constraints
```

### Step 6: Confidence Rating
```
Assign confidence based on:
- High: Clear semantic + morphological agreement
- Medium: Semantic clear, morphological ambiguous
- Low: Both semantic and morphological uncertain
```

---

## Common Errors Across Features

### Error Type 1: Morphology Over Semantics (~20-40% of errors)
**Symptom**: Predicting based on grammatical form instead of meaning
**Solution**: Always ask "What does this MEAN?" before "What form is it?"
**Examples**:
- Hebrew dual suffix but singular meaning → Semantic wins
- Greek positive form but superlative meaning → Semantic wins

### Error Type 2: Missing Discourse Context (~15-25% of errors)
**Symptom**: Predicting from single verse when context required
**Solution**: Expand context window, track participants across verses
**Examples**:
- Participant tracking without multi-verse context
- Genre without paragraph-level understanding

### Error Type 3: Ignoring Theological Knowledge (~5-10% but HIGH IMPACT)
**Symptom**: Missing Trinity, incarnation, or other doctrinal markers
**Solution**: Create theological passage checklist, apply special rules
**Examples**:
- Trinity not marked as Trial
- Messianic prophecy participants misidentified

### Error Type 4: Over-predicting Rare Values (~10-15% of errors)
**Symptom**: Predicting theoretical values that don't actually occur
**Solution**: Check frequency, design experiments to hunt for rare values
**Examples**:
- Predicting Quadrial (probably doesn't exist)
- Predicting excessive degree in formal register

---

## Experimental Design Best Practices

### Principle 1: Test ALL Values
- Select verses to cover EVERY possible feature value
- Include edge cases and rare values
- Document if certain values are NEVER found

### Principle 2: Predict BEFORE Checking
- Forces independent reasoning
- Reveals systematic biases
- Documents uncertainties explicitly

### Principle 3: Document Secondary Findings
- Note where languages disagree
- Identify translator choice points
- Record cultural/theological variations

### Principle 4: Calculate Success Metrics
- Overall accuracy rate
- Accuracy by value type
- Confidence calibration (high/medium/low)

### Principle 5: Iterate and Refine
- Use mismatches to refine algorithm
- Design follow-up experiments for uncertainties
- Build confidence levels for each pattern

---

## Feature-Specific Patterns to Document

When creating new feature experiments, document:

1. **Semantic vs Morphological**: Which takes priority? Examples?
2. **Theological Knowledge**: Any doctrine-driven values? Which passages?
3. **Discourse Role**: Does same entity get different values? When?
4. **Rare Values**: Which values are theoretical? Any evidence?
5. **Context Window**: Single verse or multi-verse? Paragraph level?
6. **Cross-Linguistic**: Do target languages disagree? Where?
7. **Success Rate**: What accuracy achieved? Confidence by pattern?

---

## Key Learnings Template for Each Feature

```markdown
# Feature: [Name]

## Major Insight #1: [Pattern Name]
**Evidence**: [Specific examples from experiments]
**Rule**: [How to apply this pattern]
**Accuracy**: [Success rate for this pattern]
**Cross-Feature**: [Does this apply elsewhere?]

## Major Insight #2: [Pattern Name]
...

## Common Errors
**Error Type 1**: [Description]
- **Symptom**: [How to recognize]
- **Frequency**: [% of errors]
- **Solution**: [How to avoid]

## Rare/Absent Values
- **Value X**: Never found in Biblical texts
- **Value Y**: Only in theological contexts

## Refined Algorithm
[Step-by-step procedure based on experiments]

## Confidence Levels
- **High**: [Patterns with 90%+ accuracy]
- **Medium**: [Patterns with 70-90% accuracy]
- **Low**: [Patterns needing human review]
```

---

## Success Stories

### Number Systems: 91.4% Accuracy
- **32/35 predictions correct**
- **All errors** due to morphological vs semantic (learned pattern!)
- **Theological knowledge** requirement confirmed (Trinity = Trial)
- **Discourse role** tracking validated

### Key Factors in Success
1. Systematic prediction before checking
2. Testing ALL possible values
3. Documenting uncertainties explicitly
4. Analyzing mismatches for patterns
5. Refining algorithm based on results

---

## Next Steps for Feature Development

1. **Apply this methodology** to remaining features without experiments
2. **Document secondary findings** (language disagreements, translator choices)
3. **Build confidence calibration** (high/medium/low accuracy expectations)
4. **Create shared learnings** as patterns emerge across features
5. **Propagate insights** back to existing features for refinement

---

**Last Updated**: 2025-11-11
**Features Analyzed**:
- number-systems (complete - 91.4% accuracy)
- degree (Phase 10 complete - 100 verses tested, complete value inventory achieved)
**Next Feature**: [To be determined based on priority]

**Major Learnings from Degree Phase 7-9** (Initial validation):
- Universal Principle 1 EXPANDED: Semantic includes implied patterns (negative comparative = superlative)
- NEW Principle 7: Lexical vs. Syntactic distinction (only syntactic gets marked)
- NEW Principle 8: Dual value encoding (standardized + literal quoted values)
- NEW Principle 9: Semantic compatibility constraint (gradability check)

**CRITICAL Learnings from Degree Phase 10** (100-verse scale testing):
- Universal Principle 5 REVISED: Scale testing required - small samples lead to INCORRECT conclusions about rare values
- NEW Principle 10: Context-dependent feature assignment (Hebrew מִן → C, T, or L based on context)
- NEW Principle 11: Mixed annotations are common (20+ instances in 100 verses, not exceptional)
- **VALUE CORRECTIONS** - 5 values thought non-existent now CONFIRMED:
  - ✅ i (Intensified Comparative): 4 instances found
  - ✅ E (Extremely Intensified): 18+ instances found
  - ✅ L ('less'): 3 instances found
  - ✅ T ('too' excessive): 12+ instances found
  - ✅ s (Superlative of 2 items): 4 instances found
- **ONLY q (equative) confirmed non-existent** after 100 verses
- **Discovery timeline**: Values found at verses 41 (i, T), 71 (E, L), 100 (s)
- **Lesson**: Don't declare values "non-existent" without 100+ verse comprehensive testing across diverse books

**Methodology Success**:
- ✅ Iterative batch testing (4 batches: 12 + 29 + 30 + 29 = 100)
- ✅ Commit after each batch improvement
- ✅ Progressive value discovery through scale
- ✅ Complete value inventory achieved
- ✅ Foundation for 90%+ accuracy algorithms
