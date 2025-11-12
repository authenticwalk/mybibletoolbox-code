# Proximity Feature: Algorithm v1.0

**Feature**: Proximity (TBTA position 8 for nouns)
**Version**: 1.0
**Date Created**: 2025-11-12
**Phase**: 4 - Algorithm Development
**Status**: LOCKED (awaiting git commit SHA)
**Git Commit SHA**: [To be filled after commit]

## Algorithm Purpose

This algorithm predicts TBTA proximity codes (n, N, S, L, R, r, T, t, C, c) for nouns based on:
1. Source language demonstrative forms (Greek/Hebrew)
2. Semantic domain classification (temporal, spatial, discourse)
3. Contextual analysis (scene geometry, emphasis, visibility)

**Target Accuracy**: 75-80% on training set
**Expected Performance by Type**:
- Temporal (T/t): 85-90%
- Discourse (C/c): 75-85%
- Spatial Remote (R/r): 75-85%
- Spatial Proximal (N/S/L): 60-70%
- Not Applicable (n): 95%+

## High-Level Decision Flow

```
INPUT: Noun phrase with context

STEP 1: Check for demonstrative
  → NO demonstrative found? → OUTPUT: n (Not Applicable)
  → YES demonstrative found? → Continue to STEP 2

STEP 2: Classify semantic domain
  → Temporal noun? → Branch A (Temporal Proximity)
  → Concrete noun + physical scene? → Branch B (Spatial Proximity)
  → Otherwise? → Branch C (Discourse Proximity)

STEP 3: Map demonstrative form + context to proximity code
  → Apply domain-specific rules (see branches below)

OUTPUT: Proximity code (n, N, S, L, R, r, T, t, C, c)
```

## STEP 1: Demonstrative Detection

**Function**: `has_demonstrative(noun_phrase)`

**Check for Greek Demonstratives:**
```
Strong's Numbers to identify:
- G3778: οὗτος (houtos) - proximal/anaphoric
- G3778.1: ὅδε (hode) - immediate proximal [rare]
- G1565: ἐκεῖνος (ekeinos) - distal

Forms to match:
- ὅδε / ἥδε / τόδε (M/F/N nominative)
- οὗτος / αὕτη / τοῦτο (M/F/N nominative)
- ἐκεῖνος / ἐκείνη / ἐκεῖνο (M/F/N nominative)
- Plus all case forms (genitive, dative, accusative)

Also check:
- οὕτως (thus, so) - demonstrative adverb
- Definite article in deictic function (context-dependent)
```

**Check for Hebrew Demonstratives:**
```
Strong's Numbers to identify:
- H2088: זֶה (zeh) - this (masculine singular)
- H2063: זֹאת (zot) - this (feminine singular)
- H0428: אֵלֶּה (elleh) - these (plural)
- הַלָּז (hallaz) - that (medial, rare)

Common constructions:
- הַיּוֹם הַזֶּה (this day)
- הַדָּבָר הַזֶּה (this thing)
- בַּיּוֹם הַהוּא (in that day)

Also check:
- הִנֵּה (behold) - deictic particle (may trigger proximity)
- Definite article in anaphoric discourse function
```

**Decision:**
```python
if no_demonstrative_found(noun_phrase):
    # Check for implicit deixis (definite article with discourse function)
    if definite_article_anaphoric(noun_phrase):
        continue_to_step_2()  # May be discourse proximity (c)
    else:
        return "n"  # Not Applicable
else:
    continue_to_step_2()
```

---

## STEP 2: Domain Classification

**Function**: `classify_domain(noun, context)`

### Check 1: Temporal Noun?

**Temporal Noun List** (Common):
```
Greek:
- ἡμέρα (day), ὥρα (hour), χρόνος (time), καιρός (season)
- γενεά (generation), αἰών (age), νύξ (night)

Hebrew:
- יוֹם (day), עֵת (time), שָׁנָה (year), חֹדֶשׁ (month)
- דּוֹר (generation), עוֹלָם (eternity, age)
```

**Decision**:
```python
if noun.lemma in TEMPORAL_NOUNS:
    return "temporal"  # Branch A
```

### Check 2: Concrete Noun in Physical Scene?

**Concrete Noun Categories**:
```
- Person (man, woman, child, prophet, king)
- Object (stone, bread, cup, garment, sword)
- Place (mountain, city, land, house, well)
- Animal (lamb, sheep, donkey, bird)
```

**Physical Scene Indicators**:
```
Context markers:
- Perception verbs: see (רָאָה/ὁράω), behold (הִנֵּה/ἰδού)
- Location markers: here, there, in this place
- Participants present in narrative
- Direct speech with pointing/gesturing
- Action verbs with spatial participants
```

**Decision**:
```python
if is_concrete_noun(noun) and has_physical_scene(context):
    return "spatial"  # Branch B
else:
    return "discourse"  # Branch C (default for abstract/ambiguous)
```

---

## Branch A: Temporal Proximity (T vs. t)

**Input**: Temporal noun + demonstrative

### Rule A1: Formulaic Temporal Constructions

**Hebrew Formulas**:
```
Pattern 1: הַיּוֹם הַזֶּה ("this day")
  → OUTPUT: T (Temporally Near)
  → Confidence: 95%
  → Example: EXO 12:14

Pattern 2: בַּיּוֹם הַהוּא ("in that day")
  → OUTPUT: t (Temporally Remote)
  → Confidence: 90%
  → Example: ISA 2:11

Pattern 3: הַיּוֹם (ha-yom, without demonstrative)
  → Check context: present moment? → T
  → Check context: prophetic future? → t
```

**Greek Formulas**:
```
Pattern 1: ἡ ἡμέρα αὕτη / τῇ ἡμέρᾳ ταύτῃ ("this day")
  → OUTPUT: T (Temporally Near)
  → Confidence: 90%

Pattern 2: ἐκείνῃ τῇ ἡμέρᾳ ("that day")
  → OUTPUT: t (Temporally Remote)
  → Confidence: 90%

Pattern 3: ἐν ἐκείναις ταῖς ἡμέραις ("in those days")
  → OUTPUT: t (Temporally Remote)
  → Confidence: 85%
```

### Rule A2: Demonstrative Form Mapping (Non-Formulaic)

**Greek**:
```
if demonstrative == "οὗτος":
    # Proximal demonstrative
    if context_indicates_present_time():
        return "T"  # Confidence: 80%
    else:
        return "T"  # Default proximal temporal
elif demonstrative == "ἐκεῖνος":
    # Distal demonstrative
    return "t"  # Confidence: 85%
```

**Hebrew**:
```
if demonstrative == "זֶה/זֹאת":
    # Unmarked - check context
    if context_indicates_present_time():
        return "T"  # Confidence: 75%
    else:
        return "t"  # Default to remote if ambiguous
elif demonstrative == "הַהוּא" (that):
    return "t"  # Confidence: 85%
```

### Rule A3: Context-Based Refinement

**Temporal Near (T) Indicators**:
```
- "From now" (ἀπ' ἄρτι, מֵעַתָּה)
- "Today" (σήμερον, הַיּוֹם)
- "This very hour"
- Present tense verbs
- Immediate action context
```

**Temporal Remote (t) Indicators**:
```
- Eschatological language ("end times", "final judgment")
- Prophetic future ("in that day")
- Historical past ("in those days")
- Past tense narrative + distal demonstrative
- Temporal distance markers ("after many days")
```

**Decision Logic**:
```python
def temporal_proximity(demonstrative, noun, context):
    # Check formulaic first (highest confidence)
    if is_formulaic(noun + demonstrative):
        return formulaic_mapping[construction]

    # Check demonstrative form
    if demonstrative in ["οὗτος", "זֶה"]:
        if has_present_markers(context):
            return "T"
        else:
            return "T"  # Default proximal
    elif demonstrative in ["ἐκεῖνος", "הַהוּא"]:
        return "t"  # Distal

    # Default
    return "T"  # Proximal default
```

---

## Branch B: Spatial Proximity (N/S/L/R/r)

**Input**: Concrete noun + demonstrative + physical scene

### Rule B1: Greek Demonstrative Spatial Mapping

**ὅδε (hode)** - Immediate Proximal [RARE]:
```
if demonstrative == "ὅδε":
    if speaker_and_listener_both_present():
        return "N"  # Near Speaker and Listener
    else:
        return "S"  # Near Speaker
    # Confidence: 85%
```

**οὗτος (houtos)** - Proximal:
```
if demonstrative == "οὗτος":
    # Analyze scene geometry
    if speaker_and_listener_both_near_referent():
        return "N"  # Near both
        # Example: MAT 26:26 (bread at table)
    elif speaker_holding_or_near_referent():
        return "S"  # Near speaker
    elif listener_near_referent():
        return "L"  # Near listener [RARE]
        # Example: MAT 3:9 (stones near crowd)
    else:
        # May be discourse, not spatial
        return None  # Route to discourse (Branch C)
    # Confidence: 70-75% (scene analysis required)
```

**ἐκεῖνος (ekeinos)** - Distal:
```
if demonstrative == "ἐκεῖνος":
    # Check visibility
    if perception_verb_present(context):
        return "R"  # Remote within Sight
        # Indicators: "see", "behold", "look at"
    elif absence_markers(context):
        return "r"  # Remote out of Sight
        # Indicators: "not here", "far away", "in [distant place]"
    else:
        return "R"  # Default to visible if uncertain
    # Confidence: 80% (R), 75% (r)
```

### Rule B2: Hebrew Spatial Inference

**זֶה/זֹאת/אֵלֶּה (zeh/zot/elleh)** - Unmarked:
```
if demonstrative in ["זֶה", "זֹאת", "אֵלֶּה"]:
    # MUST analyze narrative context (no form-based prediction)

    # Step 1: Check for speaker/listener presence
    if speaker_alone_in_scene():
        return "S"  # Near speaker
        # Example: EXO 3:3 (Moses alone at bush)
    elif speaker_and_listener_both_present():
        if referent_between_them():
            return "N"  # Near both
        else:
            # Check which is closer
            return "S" or "L"  # Context-dependent

    # Step 2: Check for distant but visible
    elif perception_verb_present(context):
        return "R"  # Remote visible
        # Example: GEN 13:14 (Abraham viewing land)

    # Step 3: Check for absence
    elif absence_markers(context):
        return "r"  # Remote invisible
        # Example: GEN 19:31 (no man in the earth)

    # Step 4: Default to discourse if spatial unclear
    else:
        return None  # Route to Branch C

    # Confidence: 65-70% (requires good context)
```

**הַלָּז (hallaz)** - Medial [RARE]:
```
if demonstrative == "הַלָּז":
    return "R"  # Always remote within sight (medial)
    # Confidence: 95%
```

### Rule B3: Scene Geometry Analysis

**Function**: `analyze_spatial_scene(context)`

**N (Near Speaker and Listener)**:
```
Indicators:
- Shared space narrative (meal, gathering, conversation)
- Object between speaker and listener
- "Among us", "between us" language
- Both participants present and close
- Ritual context (bread, cup shared)

Example: MAT 26:26 (Last Supper)
Confidence: 70-75%
```

**S (Near Speaker)**:
```
Indicators:
- First-person possessive ("my", "with me")
- Speaker handling/holding object
- Speaker alone in scene
- "I will approach this" language
- Speaker-oriented perception verb

Example: EXO 3:3 (Moses and burning bush)
Confidence: 65-70%
```

**L (Near Listener)** [RARE - Use with caution]:
```
Indicators:
- Second-person possessive ("your", "with you")
- Object at listener's location
- Direct address + pointing ("Look at this [near you]")
- Listener-focused narrative

Example: MAT 3:9 (stones near crowd) [TENTATIVE]
Note: Greek L is very rare - may default to R
Confidence: 50-60%
```

**R (Remote within Sight)**:
```
Indicators:
- Perception verbs (see, behold, look)
- "Far away" + "visible" language
- Panoramic views
- Spatial separation WITH visual contact
- Pointing to distant visible object

Example: MAT 3:17 (voice from heaven about visible Jesus)
Example: GEN 13:14 (Abraham viewing distant land)
Confidence: 75-80%
```

**r (Remote out of Sight)**:
```
Indicators:
- Absence markers ("there is no", "not here")
- Non-visible locations ("in Jerusalem" from Samaria)
- Abstract spatial reference
- Distant without perception verbs
- "Far away" + no visual contact

Example: GEN 19:31 (absent men)
Example: JHN 4:21 (Jerusalem not visible)
Confidence: 80-85%
```

### Rule B4: Decision Priority for Ambiguous Cases

```python
def spatial_proximity(demonstrative, noun, context):
    # Priority 1: Clear formulaic or rare forms
    if demonstrative == "הַלָּז":
        return "R"
    elif demonstrative == "ὅδε":
        return "N" or "S"  # Both present or speaker-focused

    # Priority 2: Clear scene geometry
    if clear_spatial_indicators(context):
        return analyze_spatial_scene(context)  # N/S/L/R/r

    # Priority 3: Distal forms → check visibility
    if demonstrative in ["ἐκεῖνος"]:
        return "R" if visible else "r"

    # Priority 4: Proximal forms → analyze closely
    if demonstrative in ["οὗτος", "זֶה"]:
        scene = analyze_spatial_scene(context)
        if scene in ["N", "S", "L"]:
            return scene
        else:
            # Spatial unclear, may be discourse
            return None  # Route to Branch C

    # Default: If spatial not clear, likely discourse
    return None
```

---

## Branch C: Discourse Proximity (C vs. c)

**Input**: Abstract noun OR spatial unclear + demonstrative

### Rule C1: Emphasis Detection

**C (Contextually Near with Focus)** - Emphatic:
```
Syntactic Indicators:
1. Subject position (fronted demonstrative)
   - "This is what..." constructions
   - זֹאת/οὗτος as sentence subject
   - Example: EZK 5:5 "This is Jerusalem"

2. Emphatic particles
   - Greek: γὰρ, οὕτως (thus/so)
   - Example: JHN 3:16 "For God thus loved" (οὕτως γὰρ)

3. Cataphoric introduction
   - Introduces new focal content
   - Forward-pointing reference
   - Discourse prominence

4. Predicate nominative with demonstrative
   - "This is X" formulas
   - Identificational clauses

Test: Can you emphasize "THIS, THIS is..."? → C
Confidence: 80-85%
```

**c (Contextually Near)** - Routine:
```
Functional Indicators:
1. Anaphoric reference
   - Refers back to previously mentioned entity
   - Discourse continuity
   - Example: JHN 7:16 (teaching mentioned in v. 15)

2. Normal word order
   - Not fronted or emphasized
   - Standard clause structure

3. Routine discourse tracking
   - Maintaining topic across clauses
   - "The aforementioned X"

4. Ritual formulas
   - Repeated phrases (Lord's Supper)
   - Example: 1CO 11:25 "This cup..." (routine)

Test: Can replace with "the aforementioned"? → c
Confidence: 75-80%
```

### Rule C2: Default Discourse Mapping

**Greek**:
```
if demonstrative == "οὗτος":
    if is_emphatic(context):
        return "C"
    else:
        return "c"  # Default routine
elif demonstrative == "ἐκεῖνος":
    # Rare in discourse, usually spatial/temporal
    return "c"  # If discourse, likely non-emphatic
```

**Hebrew**:
```
if demonstrative in ["זֶה", "זֹאת"]:
    if is_emphatic(context):
        return "C"
    else:
        return "c"  # Default routine
```

### Rule C3: Abstract Noun Handling

```
Abstract Noun Categories:
- Propositional: teaching, word, command, covenant
- Quality: righteousness, love, grace, truth
- Event: manner ("thus/so" = οὕτως)

Decision:
- Abstract nouns ALWAYS use discourse proximity (never spatial)
- Check emphasis for C vs. c
- Default to "c" if emphasis unclear
```

**Decision Logic**:
```python
def discourse_proximity(demonstrative, noun, context):
    # Check for abstract noun (force discourse domain)
    if is_abstract(noun):
        # Cannot be spatial
        if is_emphatic(context):
            return "C"
        else:
            return "c"

    # Check emphasis markers
    if is_emphatic(context):
        return "C"  # With focus
    else:
        return "c"  # Routine reference
```

---

## Algorithm Integration

**Complete Function**:
```python
def proximity_annotation(noun_phrase, context):
    """
    Main algorithm for TBTA proximity annotation

    Args:
        noun_phrase: Noun with potential demonstrative
        context: Narrative/syntactic/semantic context

    Returns:
        Proximity code: n, N, S, L, R, r, T, t, C, c
    """

    # STEP 1: Check for demonstrative
    if not has_demonstrative(noun_phrase):
        return "n"  # Not Applicable

    demonstrative = extract_demonstrative(noun_phrase)
    noun = extract_noun(noun_phrase)

    # STEP 2: Classify domain
    domain = classify_domain(noun, context)

    # STEP 3: Apply domain-specific rules
    if domain == "temporal":
        # Branch A
        return temporal_proximity(demonstrative, noun, context)

    elif domain == "spatial":
        # Branch B
        proximity = spatial_proximity(demonstrative, noun, context)
        if proximity is None:
            # Spatial unclear, route to discourse
            return discourse_proximity(demonstrative, noun, context)
        else:
            return proximity

    else:  # domain == "discourse"
        # Branch C
        return discourse_proximity(demonstrative, noun, context)
```

---

## Confidence Ratings and Expected Performance

### By Proximity Value:

| Value | Description | Expected Accuracy | Primary Challenge |
|-------|-------------|-------------------|-------------------|
| **n** | Not Applicable | 95%+ | Easy (absence of demonstrative) |
| **T** | Temporally Near | 90%+ | Easy (formulaic "this day") |
| **t** | Temporally Remote | 85-90% | Easy (formulaic "that day") |
| **C** | Discourse Focus | 80-85% | Medium (emphasis detection) |
| **c** | Discourse Routine | 75-80% | Medium (anaphoric tracking) |
| **R** | Remote Visible | 75-80% | Medium (visibility inference) |
| **r** | Remote Invisible | 80-85% | Medium (absence marking) |
| **N** | Near Both | 70-75% | Hard (scene geometry) |
| **S** | Near Speaker | 65-70% | Hard (speaker perspective) |
| **L** | Near Listener | 50-60% | Very Hard (rare, ambiguous) |

### By Source Language:

| Language | Expected Accuracy | Notes |
|----------|-------------------|-------|
| **Greek** | 75-80% | Forms are predictive (ὅδε/οὗτος/ἐκεῖνος) |
| **Hebrew** | 65-75% | Unmarked forms (זֶה), requires context |

### By Domain:

| Domain | Expected Accuracy | Notes |
|--------|-------------------|-------|
| **Temporal** | 85-90% | Formulaic constructions, clear triggers |
| **Discourse** | 75-85% | Emphasis detection, syntactic analysis |
| **Spatial** | 65-75% | Scene inference, perspective analysis |

### Overall:

**Target Accuracy on Training Set**: 75-80%
**Target Accuracy on Test Set**: 60-70% (adversarial), 80-90% (random)

---

## Known Limitations

### Limitation 1: L (Near Listener) Rarity
- L value is very rare in Greek/Hebrew source texts
- Often reanalyzed as R or S in TBTA
- Algorithm may over-predict L where TBTA uses R
- **Mitigation**: Use L sparingly, only with strong context

### Limitation 2: Hebrew Scene Inference
- זֶה is unmarked for distance
- Requires detailed narrative analysis
- Context may be ambiguous or absent
- **Mitigation**: Default to discourse (c) when spatial unclear

### Limitation 3: Discourse Emphasis Detection
- C vs. c distinction is gradient, not binary
- Syntactic emphasis markers not always reliable
- Subjectivity in "emphasis" determination
- **Mitigation**: Document confidence levels, flag borderline cases

### Limitation 4: Visibility Inference (R vs. r)
- Narrative doesn't always state visibility explicitly
- Must infer from context (perception verbs, absence markers)
- Cultural assumptions may differ from TBTA annotators
- **Mitigation**: Use perception verbs as strong indicators

### Limitation 5: Multimodal Deixis
- Gestures, pointing not preserved in text
- Physical deixis may have had gestural component
- Cannot recover from source text alone
- **Mitigation**: Annotate based on text only, document uncertainty

---

## Validation Strategy

### Phase 5: Test Set Design
- **Adversarial Test**: 10-15 verses challenging these rules
  - Focus on N/S/L ambiguity (hardest values)
  - Hebrew scene inference challenges
  - C vs. c borderline cases
  - R vs. r visibility ambiguity

- **Random Test**: 10-15 typical verses
  - Representative distribution of values
  - Should achieve 80-90% (higher than adversarial)

### Phase 6: Blind Predictions
- Apply this algorithm WITHOUT checking TBTA
- Lock predictions with git commit
- Document confidence and reasoning

### Phase 7: Validation
- Compare predictions to TBTA annotations
- Calculate accuracy overall and per-value
- Identify systematic errors

### Phase 8: Refinement
- Update algorithm based on errors (v2.0)
- Focus on lowest-performing rules
- Re-test on new verses

---

## Algorithm v1.0 Summary

**Locked Version**: 1.0
**Date**: 2025-11-12
**Git Commit**: [SHA to be recorded after commit]

**Key Strengths**:
- Temporal proximity highly predictable (85-90%)
- Greek forms provide strong signals (75-80%)
- Clear decision hierarchy (temporal → spatial → discourse)

**Key Weaknesses**:
- Hebrew spatial inference requires context (65-75%)
- L value rare and ambiguous (50-60%)
- Discourse emphasis detection subjective (C vs. c)

**Overall Confidence**: Algorithm v1.0 should achieve 75-80% accuracy on training set

**Next Steps**: Proceed to Phase 5 (Test Set Design)

---

**ALGORITHM LOCKED**: DO NOT MODIFY AFTER COMMIT
**All refinements go into Algorithm v2.0 after Phase 7 validation**
