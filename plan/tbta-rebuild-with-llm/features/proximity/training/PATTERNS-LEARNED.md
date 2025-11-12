# Proximity Feature: Patterns Learned from Training Analysis

**Feature**: Proximity (TBTA position 8)
**Date**: 2025-11-12
**Phase**: 3 - Training Analysis Complete
**Training Set**: 20 verses (2 per value × 10 values)
**Status**: Ready for Algorithm v1.0 development

## Executive Summary

Proximity annotation is reproducible through a **hierarchical decision process** combining:
1. **Source form analysis** (Greek/Hebrew demonstratives)
2. **Domain classification** (temporal → spatial → discourse)
3. **Context inference** (scene analysis, emphasis detection, visibility)

**Expected Accuracy**: 75-80% overall on initial algorithm
- Temporal (T/t): 85-90% (easiest, clear noun triggers)
- Discourse (C/c): 75-85% (medium, emphasis detection)
- Spatial Remote (R/r): 75-85% (medium, visibility inference)
- Spatial Proximal (N/S/L): 60-70% (hardest, perspective determination)

## Universal Pattern 1: Semantic Domain Determines Proximity Type

**Pattern**: Noun's semantic category predicts which proximity dimension applies

**Decision Hierarchy** (check in this order):
```
1. Is noun TEMPORAL? (day, time, hour, generation, age)
   → Use TEMPORAL proximity (T or t)

2. Is noun CONCRETE + in PHYSICAL SCENE? (person, object, place)
   → Use SPATIAL proximity (N/S/L/R/r)

3. Otherwise (abstract noun or no physical scene):
   → Use DISCOURSE proximity (C or c)

4. No demonstrative at all?
   → n (Not Applicable)
```

**Evidence from Training Set**:
- **Temporal nouns** (4/4 = 100%): EXO 12:14 (T), ISA 2:11 (t), MAT 24:3 (t), MAT 26:29 (T?)
- **Physical scenes** (8/20 = 40%): MAT 26:26, JHN 1:29, EXO 3:3, GEN 13:14, GEN 19:31, JHN 4:21, MAT 3:17, MAT 3:9
- **Abstract/discourse** (6/20 = 30%): JHN 3:16, EZK 5:5, JHN 7:16, 1CO 11:25
- **No demonstrative** (2/20 = 10%): GEN 1:1, JHN 1:1

**Accuracy Prediction**: 85-90% (clearest pattern)

## Universal Pattern 2: Greek Demonstrative Forms Strongly Predict Proximity

**Pattern**: Greek demonstrative morphology maps to proximity values with high reliability

**Greek Form Mappings**:

**ὅδε** (hóde) - Immediate Proximal:
- → **N** (Near Speaker and Listener) if both present
- → **S** (Near Speaker) if speaker-focused
- Frequency: Rare in NT (not in our training set)
- Confidence: 85-90%

**οὗτος** (houtos) - Proximal/Anaphoric:
- **Physical contexts** → **N** or **S** (sometimes **L**)
  - Example: MAT 26:26 "This is my body" → N
  - Example: MAT 3:9 "These stones" → L or R
- **Temporal nouns** → **T** (Temporally Near)
  - Example: MAT 26:29 "This fruit" → T (context: "from now")
- **Abstract/discourse** → **C** or **c**
  - Example: JHN 3:16 οὕτως → C (emphatic)
  - Example: 1CO 11:25 "This cup" → c (ritual formula)
- Frequency: Very common (~70% of NT demonstratives)
- Confidence: 70-80% (context-dependent)

**ἐκεῖνος** (ekeinos) - Distal:
- **Spatial** → **R** (Remote within Sight) or **r** (Remote out of Sight)
  - Visibility determines R vs. r
  - Example: MAT 3:17 "This is my Son" → R (heaven to earth, visible)
- **Temporal nouns** → **t** (Temporally Remote)
  - Example: "That day" → t (eschatological future)
- Frequency: Common (~30% of NT demonstratives)
- Confidence: 80-85% (R vs. r requires visibility check)

**Accuracy Prediction**: 75-80% for Greek verses

## Universal Pattern 3: Hebrew זֶה Requires Contextual Inference

**Pattern**: Hebrew demonstratives are UNMARKED for distance, requiring narrative analysis

**Hebrew Form Characteristics**:

**זֶה / זֹאת / אֵלֶּה** (zeh/zot/elleh) - Unmarked:
- **No inherent distance marking** (unlike Greek)
- **Cannot predict proximity from form alone**
- **Must analyze**:
  1. Narrative scene (who is present? where?)
  2. Syntactic position (emphatic subject = C, routine = c)
  3. Co-occurring markers (הַיּוֹם הַזֶּה = T)

**Context-Based Mapping**:
```
IF temporal noun + זֶה:
  → T (Temporally Near)
  Example: EXO 12:14 הַיּוֹם הַזֶּה → T
  Confidence: 90% (formulaic construction)

ELSE IF emphatic subject position:
  → C (Contextually Near with Focus)
  Example: EZK 5:5 זֹאת יְרוּשָׁלִָם → C
  Confidence: 85%

ELSE IF physical scene + referent present:
  → N, S, or R (analyze speaker/listener positions)
  Example: EXO 3:3 הַמַּרְאֶה הַזֶּה → S (Moses alone, approaching)
  Confidence: 65-70%

ELSE IF no physical scene:
  → c (Contextually Near, routine discourse)
  Default for abstract contexts
  Confidence: 70%

ELSE IF referent absent/invisible:
  → r (Remote out of Sight)
  Example: GEN 19:31 (implied absence) → r
  Confidence: 75%
```

**הַלָּז** (hallaz) - Medial (Rare):
- Always → **R** (Remote within Sight)
- Not in our training set, but documented pattern
- Confidence: 95% (unambiguous form)

**Accuracy Prediction**: 65-75% for Hebrew verses (lower than Greek due to ambiguity)

## Universal Pattern 4: Temporal Proximity Has Formulaic Markers

**Pattern**: Temporal proximity (T vs. t) is highly predictable from fixed constructions

**Temporal Near (T)** - Present/Immediate Time:
```
Triggers:
- "This day" (הַיּוֹם הַזֶּה / ἡ ἡμέρα αὕτη)
- "This hour" (ἡ ὥρα αὕτη)
- "This generation" (ἡ γενεὰ αὕτη)
- "From now" (ἀπ' ἄρτι) + demonstrative

Examples from Training:
- EXO 12:14: הַיּוֹם הַזֶּה → T (Passover institution day)
- MAT 26:29: τούτου + ἀπ' ἄρτι → T (present moment)

Confidence: 90%+ (formulaic)
```

**Temporal Remote (t)** - Past/Future Distant:
```
Triggers:
- "That day" (בַּיּוֹם הַהוּא / ἐκείνῃ τῇ ἡμέρᾳ)
- "In those days" (ἐν ἐκείναις ταῖς ἡμέραις)
- Eschatological contexts (prophetic future)
- Historical past references

Examples from Training:
- ISA 2:11: בַּיּוֹם הַהוּא → t (prophetic future)
- MAT 24:3: ταῦτα ἔσται → t (eschatological future)

Confidence: 85-90% (formulaic)
```

**Key Insight**: Temporal proximity is **easiest to predict** - fixed constructions, clear noun triggers

**Accuracy Prediction**: 85-90% (highest of all proximity types)

## Universal Pattern 5: Spatial Proximity Requires Scene Analysis

**Pattern**: Spatial codes (N/S/L/R/r) depend on narrative scene geometry

**Spatial Near (N/S/L)** - Determining Who Is Near:

**N (Near Speaker and Listener)** - Both Present and Close:
```
Indicators:
- Shared space narrative (e.g., meal scene)
- Object accessible to both speaker and addressee
- "Between us" or "among us" language

Example: MAT 26:26 → N
- Jesus (speaker) and disciples (listeners) at table
- Bread physically between them
- Shared ritual space

Confidence: 70-75%
```

**S (Near Speaker)** - Speaker-Oriented:
```
Indicators:
- First-person possessive + demonstrative
- Speaker handling/holding object
- "With me" or "in my hand" language
- Speaker alone in scene

Example: EXO 3:3 → S
- Moses (speaker) alone
- "I will turn aside to see this"
- Bush near Moses specifically

Confidence: 65-70%
```

**L (Near Listener)** - Hearer-Oriented:
```
Indicators:
- Second-person possessive + demonstrative
- "That [thing] you have" or "near you"
- Direct address with pointing
- Object/person at listener's location

Example: MAT 3:9 → L (tentative)
- John pointing to stones near crowd
- "From these stones [near you]"
- But Greek L is rare - may default to R

Confidence: 50-60% (L is rare, often reanalyzed as R)
```

**Spatial Remote (R vs. r)** - Visibility Determines:

**R (Remote within Sight)** - Visible but Distant:
```
Indicators:
- Perception verbs (see, behold, look at)
- "Far away" + "visible"
- Panoramic views, distant objects pointed out
- Spatial separation with visual contact

Examples:
- MAT 3:17 → R (voice from heaven about visible Jesus)
- GEN 13:14 → R (Abraham viewing visible land)
- JHN 1:29 → R or S (John seeing Jesus at distance)

Confidence: 75-80%
```

**r (Remote out of Sight)** - Not Visible:
```
Indicators:
- Absence markers ("there is no...", "not here")
- Non-visible locations ("in Jerusalem" when not there)
- Abstract spatial reference
- Distant + no perception verbs

Examples:
- GEN 19:31 → r ("There is not a man" - absent, invisible)
- JHN 4:21 → r (Jerusalem, not visible from Samaria)

Confidence: 80-85%
```

**Challenge**: Scene analysis requires inference from narrative context - harder than form-based prediction

**Accuracy Prediction**: 65-75% for proximal (N/S/L), 75-85% for distal (R/r)

## Universal Pattern 6: Discourse Proximity Depends on Emphasis

**Pattern**: Discourse demonstratives (C vs. c) distinguished by emphasis level

**C (Contextually Near with Focus)** - Emphatic:
```
Indicators:
- Subject position (fronted demonstrative)
- Cataphoric "This is what..." constructions
- Emphatic particles (γὰρ, οὕτως "thus/so")
- Highlighted discourse referent
- Predicate nominative with זֹאת/οὗτος

Examples:
- JHN 3:16 οὕτως → C (emphatic "thus/so")
- EZK 5:5 זֹאת יְרוּשָׁלִָם → C (emphatic subject)

Syntactic Test: Can you say "This, THIS is..."? → C
Confidence: 80-85%
```

**c (Contextually Near)** - Routine Reference:
```
Indicators:
- Anaphoric (referring back to previous mention)
- Normal word order (not fronted)
- Routine discourse tracking
- "The aforementioned X"
- Definite article with discourse function

Example:
- JHN 7:16 → c (teaching mentioned in v. 15)
- 1CO 11:25 → c (ritual formula, routine)

Syntactic Test: Can be replaced with "the aforementioned"? → c
Confidence: 75-80%
```

**Challenge**: Emphasis is gradient, not binary - C vs. c boundary is fuzzy

**Accuracy Prediction**: 75-85% (medium difficulty, requires syntactic analysis)

## Universal Pattern 7: "Not Applicable" (n) Is Easy to Identify

**Pattern**: Absence of demonstrative → n (Not Applicable)

**Triggers**:
```
- No demonstrative word in Greek/Hebrew
- Definite article only (not functioning as demonstrative)
- No deictic function in context
```

**Examples**:
- GEN 1:1 "the heavens" → n (no demonstrative)
- JHN 1:1 "the Word" → n (no demonstrative)

**Caveat**: Definite article CAN have demonstrative function in context
- Check if article is anaphoric/deictic
- If discourse tracking, may be → c (not n)

**Accuracy Prediction**: 95%+ (easiest value)

## Cross-Feature Connections

**Connection to Person Systems**:
- Person-oriented demonstratives (Spanish este/ese/aquel) parallel person deixis
- Near speaker (S) ↔ First person
- Near hearer (L) ↔ Second person
- Remote (R/r) ↔ Third person

**Connection to Participant Tracking**:
- First mention + demonstrative = unusual (check recognitional use)
- Routine mention + demonstrative = c (Contextually Near)
- Discourse proximity (C/c) tracks participant salience

**Connection to Discourse Genre**:
- Narrative: Higher spatial proximity (N/S/R/r)
- Epistles/teaching: Higher discourse proximity (C/c)
- Prophecy: Higher temporal remote (t)

## Algorithm Development Strategy (Phase 4)

**Step 1: Domain Classification**
```python
def classify_domain(noun, context):
    if is_temporal_noun(noun):
        return "temporal"
    elif is_concrete_noun(noun) and has_physical_scene(context):
        return "spatial"
    else:
        return "discourse"
```

**Step 2: Greek Demonstrative Mapping**
```python
def map_greek_demonstrative(form, domain, context):
    if form == "ὅδε":
        return "N" if both_present(context) else "S"
    elif form == "οὗτος":
        if domain == "temporal":
            return "T"
        elif domain == "spatial":
            return analyze_spatial_scene(context)  # N/S/L
        else:  # discourse
            return "C" if is_emphatic(context) else "c"
    elif form == "ἐκεῖνος":
        if domain == "temporal":
            return "t"
        else:  # spatial
            return "R" if is_visible(context) else "r"
```

**Step 3: Hebrew Contextual Inference**
```python
def map_hebrew_demonstrative(form, domain, context):
    if form in ["זֶה", "זֹאת", "אֵלֶּה"]:
        if domain == "temporal":
            return "T" if is_present_time(context) else "t"
        elif domain == "spatial":
            return infer_spatial_proximity(context)  # Complex analysis
        else:  # discourse
            return "C" if is_emphatic(context) else "c"
    elif form == "הַלָּז":
        return "R"  # Always medial
```

**Step 4: Validation and Refinement**
- Test on training set (target: 75-80% accuracy)
- Identify systematic errors
- Refine context analysis rules

## Key Unknowns for Algorithm v1.0

**High Priority Questions**:
1. **L (Near Listener) frequency**: Is it as rare as predicted? (Expected: <5% of spatial)
2. **Hebrew scene inference accuracy**: Can we achieve >65% for spatial proximity with זֶה?
3. **C vs. c emphasis threshold**: What syntactic features best predict C?
4. **Visibility inference**: How reliable is R vs. r prediction without explicit markers?

**Medium Priority Questions**:
1. **Multimodal deixis**: Do gestures affect TBTA coding? (Not preservable in text)
2. **Elevation marking**: Does TBTA use R/r for up/down, or a separate system?
3. **Quoted speech perspective**: Whose viewpoint determines proximity in dialogue?

## Success Metrics for Algorithm v1.0

**Overall Target**: 75-80% exact match accuracy on training set

**Per-Value Targets**:
| Value | Target Accuracy | Priority |
|-------|-----------------|----------|
| n | 95%+ | High |
| T | 85-90% | High |
| t | 85-90% | High |
| C | 80-85% | High |
| c | 75-80% | Medium |
| R | 75-80% | Medium |
| r | 80-85% | Medium |
| N | 70-75% | Medium |
| S | 65-70% | Medium |
| L | 50-60% | Low (rare) |

**If Algorithm v1.0 achieves these targets:**
- Proceed to Phase 5 (Test Set Design)
- Focus adversarial test on low-accuracy values (N/S/L)
- Include Hebrew scene inference challenges

**If Below Targets:**
- Iterate on context analysis rules
- Add more training examples for weak values
- Consult additional linguistic resources

## Next Steps (Phase 4)

1. **Codify patterns** into algorithmic rules
2. **Implement domain classifier** (temporal → spatial → discourse)
3. **Implement form mappers** (Greek and Hebrew)
4. **Implement context analyzers** (scene, emphasis, visibility)
5. **Test on training set** and calculate accuracy
6. **Document Algorithm v1.0** with locked version (git commit)
7. **Proceed to Phase 5** (Test Set Design)

---

**Status**: Patterns learned, ready for algorithm development
**Confidence**: High (75-80% accuracy achievable)
**Primary Challenge**: Hebrew spatial inference (scene analysis)
**Key Strength**: Temporal proximity (formulaic, 85-90% accuracy)
