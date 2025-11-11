# Cross-Feature Learnings: Universal Patterns in TBTA Annotation

**Purpose**: Document patterns, methodologies, and insights that apply across multiple TBTA features.

**Source Experiments**:
- number-systems/experiment-001.md (91.4% training accuracy)
- number-systems/validation (Phase 7-8, 2025-11-09): 57% on 7 Genesis/Exodus verses
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

### When Mixed Annotations Are Appropriate

⚠️ **CRITICAL GUIDANCE**: Not all features should allow mixed annotations. This depends on the feature's semantic nature and target language constraints.

#### Features That SHOULD Allow Mixed Annotations:
- **Degree**: Same word can be BOTH intensified AND excessive (GEN 18:11: "old" = Intensified + 'too')
  - **Reason**: Multiple independent semantic dimensions (intensity vs capacity)
  - **Source language**: Both Hebrew and Greek show this pattern

#### Features Where Mixed May Be Target-Language Dependent:
- **Number**: Source may be ambiguous (collective), target must choose singular/plural
  - **Rule**: If target language FORCES a choice → Algorithm picks DOMINANT value
  - **Dominant value selection**: Based on discourse salience (group identity vs individual members)
  - **Language family consistency**: Romance languages consistently treat collectives as singular; Germanic varies

- **Person**: Discourse role may shift, but target language may force single pronoun
  - **Rule**: Pick dominant discourse role in that clause
  - **Exception**: Honorifics may require mixed (2nd person + plural for respect)

#### When to Choose Dominant Value (Not Mixed):

**Decision Tree**:
```
1. Does the TARGET language feature allow multiple simultaneous values?
   → YES: Preserve mixed annotation (e.g., Hebrew מִן with rising AND excessive meaning)
   → NO: Continue to step 2

2. Are the multiple values truly INDEPENDENT semantic dimensions?
   → YES: Flag as "requires target language choice" (e.g., collective number)
   → NO: Choose dominant value (e.g., most discourse-salient reading)

3. For target language choice scenarios:
   a. Identify language family of target
   b. Apply consistent family-wide rule (see Language Family Rules below)
   c. Exception: If context strongly favors non-default → Use context
   d. Document choice rationale in metadata
```

#### Language Family Consistency Rules

**For features requiring single value selection**:

**Number (Collective Entities)**:
- **Romance languages** (Spanish, French, Portuguese): Default SINGULAR
  - "La gente es" (the people is) → Singular
  - Exception: Explicit plurality markers override
- **Germanic languages** (English, German, Dutch): Context-dependent
  - English: "The people are" (plural), "The team is" (singular)
  - Apply discourse salience rule per context
- **Slavic languages**: Default PLURAL
  - Russian: "Люди" always takes plural agreement

**Person (Honorific/Polite Forms)**:
- **European languages**: V-form distinctions
  - French vous, German Sie → 2nd person + plural number
  - Mixed annotation appropriate (person=2, number=plural)
- **Asian languages**: Complex honorific systems
  - Korean, Japanese → Multiple independent dimensions
  - Preserve all dimensions in annotation

**Degree (When Target Lacks Multiple Expressibility)**:
- **English**: Can express multiple degrees ("too old" = excessive + old)
  - Preserve mixed annotation
- **Language lacking 'too' construction**: Choose DOMINANT
  - Dominant = capacity limitation (excessive) > simple intensity
  - "Too old to bear" → "very old" if 'too' unavailable

#### Exceptions to Dominant Value Rules

**Exception 1: Discourse Emphasis**
- If discourse strongly emphasizes the non-default reading → Choose contextual reading
- Example: Collective acting as individuals (distributive reading) → Use plural
- Document: "Contextual override: distributive action favors plural"

**Exception 2: Theological/Cultural Significance**
- Trinity contexts: Mixed annotation required (Trial + Inclusive)
- Honorific contexts: Mixed annotation required (person + formality)
- Document: "Theological/cultural significance requires mixed"

**Exception 3: Source Language Ambiguity Resolution**
- Hebrew dual morphology with unclear semantics → Check LXX or other ancient translations
- If ancient translations consistently choose one → Use that as dominant
- Document: "Cross-translation evidence favors [value]"

### Dominant Value Selection Criteria

When forced to choose single value from multiple options:

**Priority Order**:
1. **Discourse salience**: What's being emphasized in this clause?
2. **Language family default**: Follow family-wide pattern
3. **Semantic compositionality**: Which value is derivable from context?
4. **Cross-translation consensus**: What do 3+ major translations do?
5. **Coin toss scenario**: If truly equal → Pick language family default

**Coin Toss Identification**:
- Multiple readings equally valid semantically
- No discourse emphasis on either
- Cross-translations split 50/50
- No theological/cultural factors

**For coin toss scenarios**:
- **Same language family → same choice** (consistency within family)
- Document: "Coin toss: [language family] default applied"
- Future consistency: All [family] languages use same rule

### Cross-Feature Implications
- **All features**: Determine if mixed annotations semantically valid
- **Target language constraints**: Some features force single value
- **Language family consistency**: Same families → same choices for coin tosses
- **Validation**: Partial match scoring when mixed appropriate; exact match when single value forced
- **Algorithm**: Output format depends on feature (list vs single value)
- **Accuracy metrics**:
  - Features allowing mixed: Precision/recall
  - Features forcing single: Exact match + "acceptable alternative" scoring
- **Testing**: Design verses with mixed annotations + verses requiring dominant value choice
- **Documentation**: Explicitly state which features allow mixed, which force single value

---

## Cross-Feature Algorithm Template

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

## Universal Principle 7: Part-of-Speech Specific Rules

### Pattern
**TBTA may apply different annotation logic for different parts of speech.**

### Evidence

#### Number Systems (validation 2025-11-09)

**Pronouns follow morphological number**:
- Hebrew אֹתָם (otam, plural suffix) → Plural (even with two referents)
- Gen 1:27 "them" (male and female = 2) → **Plural** (not Dual)
- Pattern: Morphological agreement takes priority for pronouns

**Nouns follow semantic count**:
- Hebrew שָׁמַיִם (shamayim, dual morphology) → **Singular** (one sky semantically)
- Fossilized dual forms lexicalized as singular
- Pattern: Semantic meaning takes priority for nouns

### Application Rule
```
For PRONOUNS:
1. Check morphological number FIRST
2. Plural suffix → Plural (regardless of referent count)
3. Semantic count secondary

For NOUNS:
1. Semantic meaning FIRST (how many entities?)
2. Morphology secondary (confirmation or conflict resolution)
```

### Cross-Feature Implications
- **Person**: Pronouns vs. nouns may differ in person-marking logic
- **Proximity**: Demonstrative pronouns vs. demonstrative determiners
- **Time**: Verbal morphology vs. adverbial time expressions
- **Surface Realization**: Pronoun vs. noun realization marked differently

---

## Universal Principle 8: Productive vs. Theoretical Values

### Pattern
**Some feature values are productive (used regularly), others are rare or theoretical.**

### Evidence

#### Number Systems (validation 2025-11-09)

**Productive values** (found in data):
- Singular: Very common ✅
- Plural: Very common ✅
- Trial: Used for explicit groups of three ✅

**Rare/uncertain values** (not found in limited sample):
- Dual: Expected in Gen 1:27, Gen 22:6 → **NOT found** ❌
- Quadrial: Not tested yet (NT data unavailable)
- Paucal: Not tested yet

**Critical finding**: Dual may be reserved for specific contexts only
- Not used for plural pronouns with two referents
- Not used for "both of them" (explicit dual)
- Possibly only for natural pairs (eyes, hands) - needs validation

### Application Rule
```
When predicting rare values:
1. Mark as LOW CONFIDENCE by default
2. Require strong evidence (explicit morphology + semantic match)
3. Consider that value may be theoretical but unused in Biblical corpus
4. Default to more common value (Plural instead of Dual, Plural instead of Paucal)
```

### Cross-Feature Implications
- **Degree**: Excessive "too" may be rare in Biblical register
- **Time**: Some granularities may not appear in ancient texts
- **Honorifics**: Some levels may not exist in Biblical cultures
- **All features**: Theoretical values ≠ productive values

---

## Universal Principle 9: Enumeration Triggers Specific Values

### Pattern
**Explicit enumeration (cardinal numbers) triggers specific feature values.**

### Evidence

#### Number Systems (validation 2025-11-09)

**Trial for explicit "three"**:
- Genesis 18:2: שְׁלֹשָׁה אֲנָשִׁים "three men" → **Trial** (not Plural)
- Genesis 7:13: Noah's three sons (named) → **Trial**
- Pattern: NOT limited to Trinity theology

**Key insight**: Enumeration is mechanical, not theological
- "Three X" → Trial (regardless of significance)
- Trinity is special case of general "three" rule
- Contrast with v1.0 assumption (Trial = Trinity only)

**Validation impact**:
- v1.0: Assumed Trial theology-specific → predicted Plural for Gen 18:2 ❌
- v2.0: Trial for all explicit three → correct prediction ✅

### Application Rule
```
For Number feature:
- "One X" → Singular
- "Two X" → Plural (Dual uncertain, needs more data)
- "Three X" → Trial
- "Four X" → Unknown (Quadrial? Paucal? Plural?) - needs data
- "Five-ten X" → Paucal? or Plural? - needs data
- Large numbers → Plural
```

### Cross-Feature Implications
- **Degree**: Explicit comparatives ("more than", "less than") vs. implicit
- **Time**: Explicit time markers ("three days") vs. relative time
- **Participant Tracking**: Explicit count of participants affects annotation

---

## Confidence Calibration Lessons (from Number Systems)

### Pattern
**Initial confidence predictions can be systematically wrong.**

### Evidence

**Number Systems v1.0 confidence vs. accuracy**:

| Confidence | Predictions | Correct | Actual Accuracy |
|------------|-------------|---------|-----------------|
| High | 5 | 2 | 40% ❌ |
| Medium | 2 | 2 | 100% ✅ |
| Low | 0 | - | - |

**Finding**: High confidence predictions UNDER-performed!

**Root cause**: Over-confidence in Dual predictions
- Dual (High confidence): 0/2 = 0% accuracy
- Singular (High confidence): 2/2 = 100% accuracy

### Calibration Fixes
```
High confidence should require:
1. Training validation (seen in training data)
2. Clear morphological + semantic alignment
3. Multiple confirming sources
4. NO conflicting evidence

Avoid High confidence for:
- Rare values without validation (Dual, Paucal, Quadrial)
- Newly learned patterns (Trial expansion - start Medium)
- Morphology-semantic conflicts
```

### Application Rule
```
Confidence levels:
HIGH (90%+): Only if training + validation confirmed
MEDIUM (70-90%): Newly learned patterns, good evidence
LOW (<70%): Rare values, insufficient data, conflicts
```

---

## Data Coverage Limitations

### Pattern
**TBTA data availability varies significantly by book and testament.**

### Evidence

**Number Systems validation (2025-11-09)**:
- Genesis/Exodus: Available ✅
- Other OT (Ezekiel, Daniel, Ruth, Psalms): Not available ❌
- NT (Matthew, Mark, John, Acts, Revelation): Not available ❌
- Coverage: 7/24 test verses = 29%

**Impact**:
- Cannot validate NT-specific patterns
- Cannot test Quadrial (appears in Revelation, Ezekiel)
- Cannot test Paucal boundary (needs diverse examples)
- Limited to early OT for validation

### Workaround Strategies
```
1. Design test sets weighted toward available data (Genesis, Exodus)
2. Use training data insights for unavailable books
3. Mark predictions for unavailable verses as "pending validation"
4. Document coverage gaps in methodology
5. Acquire more data (download more verses, request access)
```

### Cross-Feature Implications
- All features affected by OT-heavy coverage
- NT features (Greek-specific patterns) harder to validate
- Need to prioritize downloadable TBTA samples

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
- person-systems (100% translation validation, TBTA perspective insights)
**Next Feature**: [To be determined based on priority]

**Major Learnings from Degree Phase 7-9** (Initial validation):
- Universal Principle 1 EXPANDED: Semantic includes implied patterns (negative comparative = superlative)
- NEW Degree Principle 7: Lexical vs. Syntactic distinction (only syntactic gets marked)
- NEW Degree Principle 8: Dual value encoding (standardized + literal quoted values)
- NEW Degree Principle 9: Semantic compatibility constraint (gradability check)

**CRITICAL Learnings from Degree Phase 10** (100-verse scale testing):
- Universal Principle 5 REVISED: Scale testing required - small samples lead to INCORRECT conclusions about rare values
- NEW Degree Principle 10: Context-dependent feature assignment (Hebrew מִן → C, T, or L based on context)
- NEW Degree Principle 11: Mixed annotations are common (20+ instances in 100 verses, not exceptional)
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

**Major Learnings from Person-Systems** (Cross-linguistic validation):
- NEW Person-Systems Principle 7: Dual Perspective in Annotation (discourse-internal vs reader-oriented)
- NEW Person-Systems Principle 8: Cross-Linguistic Validation is Essential (5-10 real translations)
- NEW Person-Systems Principle 9: Confidence Calibration Through Validation (high confidence = 90%+ accuracy)
- NEW Person-Systems Principle 10: Lock Predictions Before Validation (git commit for audit trail)
- **Translation Validation**: 98%+ agreement across 9 Austronesian languages
- **Algorithm accuracy**: 100% (7/7) against real translations
- **Methodology proven**: Adversarial testing + real translation validation

---

## Universal Principle 7: Dual Perspective in Annotation (CRITICAL)

### Pattern
**TBTA uses DISCOURSE-INTERNAL perspective (speaker-listener within text), while translation guidance requires READER-ORIENTED perspective.**

### Evidence

#### Person Systems: Genesis 1:26 - The Defining Case
- **Text**: "Let us make man in our image"
- **TBTA Annotation**: "First Inclusive" + "Trial"
  - Speaker: "God"
  - Listener: "God"
  - Internal relationship: God (Trinity person) → God (other Trinity persons) = INCLUSIVE
- **Translation Guidance Prediction**: EXCLUSIVE
  - Ultimate addressees: Human readers
  - Relationship: Divine "us" → Human readers = EXCLUSIVE
- **Real Translations**: Use EXCLUSIVE forms (Indonesian kami, Tagalog kami/namin)
- **Result**: Both annotations CORRECT for different purposes

#### Person Systems: Genesis 42:21 - Agreement Case
- **Text**: Brothers saying "we are guilty" to one another
- **TBTA**: "First Inclusive" (brothers include each other)
- **Translation**: INCLUSIVE (same relationship for readers)
- **Result**: Perspectives ALIGN

### The Divergence Rule
```
Perspectives diverge when:
1. Speaker and listener are BOTH within the text
2. AND neither is the ultimate reader
3. AND there's an ontological/group boundary

Examples:
- God → God (divine council) vs. Human readers
- Prophet for God → People (within text) vs. Modern readers
- Quoted speech → Original addressee vs. Current readers

Perspectives align when:
- Readers identify with text's participants
- No ontological barriers
- Reciprocal or shared actions
```

### Application Rule
```
For all features:
1. Identify BOTH perspectives:
   - Discourse-internal (for TBTA comparison)
   - Reader-oriented (for translation guidance)
2. Predict BOTH when they may differ
3. Document when and why divergence occurs
4. NOT an error - both valid for different purposes
```

### Cross-Feature Implications
- **Person**: Discourse-internal vs. translation clusivity
- **Participant Tracking**: Text-internal salience vs. reader relevance
- **Illocutionary Force**: Original utterance vs. current application
- **Discourse Genre**: Text's genre vs. reader's interpretation frame
- **Honorifics**: Text-internal status vs. modern reader perspective

### Validation Method
```
Dual validation approach:
1. TBTA Validation:
   - Measures discourse understanding
   - Expect some divergence in specialized contexts
   - ~50% agreement in divine speech, ~95% elsewhere

2. Real Translation Validation:
   - Measures practical utility
   - Expect high agreement (~95%+)
   - Use 5-10 clusivity-marking languages

Report BOTH:
- "TBTA alignment: X% (perspective-aware)"
- "Translation validation: Y% (primary utility metric)"
```

---

## Universal Principle 8: Cross-Linguistic Validation is Essential

### Pattern
**Real Bible translations in feature-specific languages provide the strongest validation.**

### Evidence

#### Person Systems: 9-Language Consensus
- **Languages validated**: Tagalog, Indonesian, Malay, Tok Pisin, Cebuano, Ilocano, Hiligaynon, Pangasinan, Waray
- **Accuracy**: 98%+ agreement across languages
- **Verses tested**: 7 training set verses
- **Algorithm accuracy**: 100% (7/7) against real translations

#### Pattern Recognition
- **100% consensus verses**: Prayer to God, worship invitation, reciprocal actions
- **98%+ consensus**: Apostolic witness, group distinctions
- **Insight**: High cross-linguistic agreement validates universal semantic patterns

### Application Rule
```
For each feature:
1. Identify languages with explicit marking:
   - Clusivity → Austronesian languages
   - Evidentiality → Quechua, Turkish
   - Honorifics → Korean, Japanese
   - Number systems → Arabic (dual), PNG languages (trial)

2. Validate against 5-10 real translations:
   - Access published Bible translations
   - Check professional translator decisions
   - Document cross-linguistic consensus

3. Calculate two accuracy metrics:
   - TBTA accuracy (discourse understanding)
   - Translation accuracy (practical utility)
```

### Finding Language-Specific Resources
```
For validation:
- Bible.com (YouVersion) - 2000+ translations
- eBible.org - Open source translations
- Biblegateway.com - Multiple versions
- SIL publications - Linguistic analyses

Priority: Languages with EXPLICIT GRAMMATICAL marking of feature
```

### Cross-Feature Implications
- **All features benefit** from real-world translation validation
- **TBTA coverage limited** (Genesis-Esther only as of 2025-11-09)
- **Translation validation more comprehensive** - can test entire Bible
- **Dual validation becomes standard** - report both metrics

---

## Universal Principle 9: Confidence Calibration Through Validation

### Pattern
**High confidence predictions should achieve 90%+ accuracy; validation data refines confidence ratings.**

### Evidence

#### Person Systems: Perfect High-Confidence Calibration
- **High confidence predictions** (85-95% rated): 7 verses tested
- **Actual accuracy**: 100% (7/7)
- **Rules with 100% validation**:
  - Prayer to God → EXCLUSIVE (Rule 2.1)
  - Reciprocal actions → INCLUSIVE (Rule 2.4) 
  - Worship invitation → INCLUSIVE (Rule 2.5)
  - Apostolic witness → EXCLUSIVE (Rule 2.6)
  - Group distinction → EXCLUSIVE (Rule 3.2)

#### Calibration Success Metrics
```
High Confidence (85-95%):
- Expected accuracy: 90%+
- Actual accuracy: 100% (7/7) ✅
- Status: Well-calibrated

Medium Confidence (70-85%):
- Expected accuracy: 75-85%
- Actual accuracy: 100% (1/1) - may be underconfident
- Status: Needs more data

Low Confidence (<70%):
- Expected accuracy: 50-70%
- Actual accuracy: Not yet tested
- Status: Awaiting validation
```

### Application Rule
```
For confidence ratings:
1. Initial ratings based on:
   - Rule clarity (absolute vs. context-dependent)
   - Training set consistency (100% vs. 80%)
   - Cross-linguistic agreement (unanimous vs. majority)
   - Theological ambiguity (clear vs. debated)

2. Refine after validation:
   - If high confidence < 90% actual → Lower threshold
   - If medium confidence > 90% actual → Raise to high
   - Track calibration across 20+ predictions

3. Report calibration metrics:
   - "High confidence predictions: X% accuracy"
   - "Medium confidence predictions: Y% accuracy"
   - "Confidence calibration: [well-calibrated/underconfident/overconfident]"
```

### Cross-Feature Implications
- **All features need confidence ratings** on predictions
- **Validation refines ratings** over time
- **Well-calibrated confidence builds trust** in algorithm
- **Users can act on high confidence** without checking every case

---

## Universal Principle 10: Lock Predictions Before Validation (Methodology)

### Pattern
**To avoid data leakage and maintain validation integrity, predictions MUST be locked (git committed) BEFORE accessing validation data.**

### Evidence

#### Person Systems: Proper Methodology
- **Predictions locked**: Commit 77010a4 (2025-11-09)
- **TBTA access**: AFTER lock
- **Real translation check**: AFTER lock
- **Result**: True blind validation, no retroactive fitting
- **SHA recorded**: Immutable proof of prediction timing

#### What Proper Locking Prevents
- **Retroactive accuracy inflation**: Can't adjust predictions after seeing answers
- **Cherry-picking**: Can't select only successful predictions
- **Unconscious bias**: Can't be influenced by validation data
- **Data leakage**: Training and test data remain separate

### Application Rule (MANDATORY)
```
Prediction Protocol:
1. Design test set → Commit to git
2. Make predictions using locked algorithm → Document reasoning
3. Lock predictions → Git commit with SHA
4. Access validation data (TBTA or real translations)
5. Calculate accuracy → Compare with locked predictions
6. Error analysis → Document mismatches
7. Algorithm update → Create v2.0 (do NOT retest on same verses)

NEVER:
- Modify predictions after seeing validation data
- Omit failed predictions from reporting
- Update algorithm then claim validation on same data
```

### Cross-Feature Implications
- **All features must follow** this protocol
- **Git commits provide** audit trail
- **Adversarial methodology requires** immutable predictions
- **Publication credibility depends** on proper validation

---

## Methodology Insights: Adversarial Testing at Early Phase

### Pattern
**Small adversarial test sets (10-15 verses) find weaknesses faster than large random samples, especially during algorithm development.**

### Evidence

#### Person Systems Test Design
- **Adversarial set**: 15 challenging edge cases
- **Random set**: 12 typical cases  
- **Expected gap**: 20-25 percentage points
- **Purpose**: Adversarial reveals algorithm limits, random shows typical performance

#### Why Adversarial Works
```
Adversarial advantages:
1. Deliberate challenge → Finds edge cases quickly
2. Targeted weakness → Each verse tests specific vulnerability
3. Small sample → Can complete in days not months
4. Clear diagnostic → Failures reveal specific gaps

Random advantages:
1. Unbiased sample → Shows typical performance
2. Baseline metric → Expected real-world accuracy
3. Comparison point → Validates that adversarial is actually hard
```

### Application Rule
```
For each feature (during algorithm development):
1. Training set: 15-20 verses (learn patterns)
2. Adversarial test: 10-15 verses (find weaknesses)
3. Random test: 10-15 verses (measure typical performance)
4. Success metrics:
   - Adversarial: 60-70% (challenging)
   - Random: 80-90% (should be higher)
   - Gap: 15-25 points (validates test design)

AFTER all features complete:
- Comprehensive validation: 200+ verses per feature
- Cross-validation, confidence intervals
- Statistical rigor for publication
```

### Cross-Feature Implications
- **Use adversarial for rapid iteration** (weeks not months)
- **Save comprehensive validation** for production readiness
- **Both test types needed** - adversarial finds gaps, random measures baseline
- **Gap metric critical** - if random ≤ adversarial, test design failed

---

## Source Metadata Updated

**Features Contributing to Cross-Learnings**:
1. number-systems (complete - 91.4% accuracy, comprehensive analysis)
2. **degree (Phase 10 complete - 100 verses, complete value inventory)** ← UPDATED
3. **person-systems (100% translation validation, TBTA perspective insights)** ← NEW

**Validation Status**:
- 11+ degree-specific principles validated (Principles 7-11 from comprehensive testing)
- 10+ person-systems principles validated (Principles 7-10 from cross-linguistic validation)
- 9+ number-systems principles validated
- Methodology proven effective across different feature types
- Iterative batch testing validated (4 batches to discover all rare values)

**Last Updated**: 2025-11-11

---
