# TBTA Proximity Feature: Learnings and Reproduction Thesis

**Feature**: Proximity (Position 8 in Noun Semantic Strings)
**Date**: 2025-11-05
**Status**: Initial Research Complete - Ready for Experimentation

## Executive Summary

TBTA's proximity annotation system uses a 10-value code to capture demonstrative distinctions across three dimensions: spatial (5 values), temporal (2 values), and discourse (2 values), plus N/A. This feature is reproducible using a combination of source text analysis (Greek/Hebrew demonstratives), contextual inference (narrative scene analysis), and cross-linguistic knowledge (target language requirements).

## Initial Thesis: How to Reproduce Proximity Annotations

### Core Insight

**Proximity annotations are determinable through a three-step process:**

1. **Source Text Analysis**: Identify demonstrative forms in Greek/Hebrew
2. **Contextual Analysis**: Determine physical/temporal/discourse relationships from narrative
3. **Functional Classification**: Map to TBTA's 10-value system based on deictic function

### Confidence Level: HIGH (85%)

**Rationale**:
- Greek demonstratives (ὅδε/οὗτος/ἐκεῖνος) have well-defined spatial/discourse semantics
- Hebrew demonstratives (זֶה/הַלָּז), while less spatially specific, have clear discourse functions
- Narrative context provides spatial relationships (present/absent, visible/invisible)
- TBTA's value set systematically covers major cross-linguistic distinctions

**Uncertainty**:
- Hebrew זֶה unmarked for distance → Requires contextual inference (~15% uncertainty)
- Boundary cases between spatial and discourse proximity
- TBTA annotators may have made language-family-specific decisions not documented

## Detailed Reproduction Method

### Step 1: Identify Demonstrative Context

**Action**: Parse source text (Greek NT or Hebrew OT) for demonstrative markers

**Greek Demonstratives to Identify:**
- **ὅδε** (hóde, 3778.1) → Immediate proximal
- **οὗτος** (hoûtos, 3778) → Proximal/anaphoric
- **ἐκεῖνος** (ekeînos, 1565) → Distal

**Hebrew Demonstratives to Identify:**
- **זֶה** (zeh, H2088) → Neutral/unmarked
- **זֹאת** (zo't, H2063) → Feminine singular
- **אֵלֶּה** ('elleh, H0428) → Plural
- **הַלָּז** (hallaz, rare) → Medial spatial

**Implementation**:
```python
def identify_demonstrative(word):
    """
    Check if word has demonstrative function
    Returns: demonstrative_type, source_form
    """
    # Check Strong's numbers or lemma
    if word.strongs in ['G3778', 'G3778.1', 'G1565']:
        return 'greek_demonstrative', word.lemma
    elif word.strongs in ['H2088', 'H2063', 'H0428']:
        return 'hebrew_demonstrative', word.lemma
    # Check for demonstrative articles or modifiers
    elif word.role == 'demonstrative':
        return 'demonstrative_modifier', word.lemma
    else:
        return None, None
```

**Outcome**: List of nouns with demonstrative context

### Step 2: Classify Proximity Type

**Action**: Determine whether proximity is spatial, temporal, or discourse-based

**Classification Heuristics:**

**A. Temporal Proximity Markers**
```python
TEMPORAL_MARKERS = {
    'greek': ['ἡμέρα', 'ὥρα', 'χρόνος', 'καιρός', 'αἰών'],  # day, hour, time, season, age
    'hebrew': ['יוֹם', 'עֵת', 'שָׁנָה', 'חֹדֶשׁ']  # day, time, year, month
}

def is_temporal_proximity(noun):
    """Check if noun is a time word requiring temporal proximity"""
    return noun.lemma in TEMPORAL_MARKERS[noun.language]
```

**B. Spatial Proximity Markers**
```python
def is_spatial_proximity(noun, context):
    """
    Check if noun refers to physically present entity in narrative scene
    """
    # Check for:
    # 1. Concrete nouns (person, object, place)
    # 2. Narrative describes physical scene (not abstract discourse)
    # 3. Speaker/listener physically present
    if noun.semantic_domain in ['person', 'object', 'place']:
        if context.has_physical_scene:
            return True
    return False
```

**C. Discourse Proximity (Default)**
```python
def is_discourse_proximity(noun):
    """
    Check if demonstrative serves anaphoric/cataphoric discourse function
    """
    # Default for abstract nouns, propositions, or ambiguous contexts
    if noun.is_abstract or noun.referent_type == 'proposition':
        return True
    return False
```

**Decision Priority**:
1. If temporal noun + demonstrative → **Temporal Proximity**
2. Else if concrete noun + physical scene → **Spatial Proximity**
3. Else → **Discourse Proximity**

### Step 3: Assign TBTA Code

**Action**: Map demonstrative + context to specific TBTA proximity value

#### 3A. Spatial Proximity Assignment

```python
def assign_spatial_proximity(demonstrative_form, context):
    """
    Map Greek/Hebrew demonstrative to spatial proximity code

    Returns: 'N', 'S', 'L', 'R', or 'r'
    """

    # Greek mappings
    if demonstrative_form == 'ὅδε':
        # Immediate proximal → Near speaker or both
        if context.speaker_and_listener_present():
            return 'N'  # Near Speaker and Listener
        else:
            return 'S'  # Near Speaker

    elif demonstrative_form == 'οὗτος':
        # Proximal → Check for speaker/listener distinction
        if context.near_both():
            return 'N'  # Near both
        elif context.near_speaker():
            return 'S'  # Near speaker
        elif context.near_listener():
            return 'L'  # Near listener (rare in Greek, but possible)
        else:
            # Anaphoric use, not truly spatial
            return None  # Route to discourse proximity instead

    elif demonstrative_form == 'ἐκεῖνος':
        # Distal → Check visibility
        if context.referent_visible():
            return 'R'  # Remote within Sight
        else:
            return 'r'  # Remote out of Sight

    # Hebrew mappings
    elif demonstrative_form in ['זֶה', 'זֹאת', 'אֵלֶּה']:
        # Unmarked → Infer from context
        if context.referent_present_in_scene():
            if context.near_both():
                return 'N'
            elif context.near_speaker():
                return 'S'
            else:
                return 'R'  # Present but not specifically near
        else:
            if context.referent_visible():
                return 'R'
            else:
                return 'r'

    elif demonstrative_form == 'הַלָּז':
        # Always medial spatial
        return 'R'  # Remote within Sight

    return 'n'  # Not Applicable if no clear spatial context
```

**Context Clues for Spatial Assignment:**

**Indicator: "Near Speaker and Listener" (N)**
- Narrative: "This [object] between us"
- Both speaker and listener present in scene
- Object accessible to both

**Indicator: "Near Speaker" (S)**
- Narrative: "This [object] with me," "This [person] speaking"
- Speaker handling or possessing object
- First-person possessive with proximal demonstrative

**Indicator: "Near Listener" (L)**
- Narrative: "This [object] you have," "Look at this [near you]"
- Second-person possessive with proximal demonstrative
- Direct address with pointing

**Indicator: "Remote within Sight" (R)**
- Narrative describes visible but distant referent
- "Look at that [mountain/building/person]" (can be seen)
- Distal demonstrative + visual perception verb

**Indicator: "Remote out of Sight" (r)**
- Narrative describes absent or non-visible referent
- "That [place] far away" (cannot be seen)
- Distal demonstrative + absence markers

#### 3B. Temporal Proximity Assignment

```python
def assign_temporal_proximity(demonstrative_form, noun):
    """
    Map demonstrative + time noun to temporal proximity code

    Returns: 'T' or 't'
    """

    # Greek
    if demonstrative_form == 'οὗτος':
        # "This day," "this time," "this generation"
        return 'T'  # Temporally Near

    elif demonstrative_form == 'ἐκεῖνος':
        # "That day," "in that time"
        return 't'  # Temporally Remote

    # Hebrew
    elif demonstrative_form in ['זֶה', 'זֹאת']:
        # Check for "הַיּוֹם הַזֶּה" (this day) constructions
        if noun.phrase_type == 'this_day':
            return 'T'
        else:
            # "בַּיּוֹם הַהוּא" (in that day)
            return 't'

    # Default heuristic: proximal forms → T, distal forms → t
    return 'T' if demonstrative_form in ['οὗτος', 'זֶה'] else 't'
```

**Examples:**
- "This generation" (ἡ γενεὰ αὕτη) → `T`
- "That day" (ἐκείνῃ τῇ ἡμέρᾳ) → `t`
- "This very hour" → `T`
- "In those days" → `t`

#### 3C. Discourse Proximity Assignment

```python
def assign_discourse_proximity(demonstrative_form, context):
    """
    Map demonstrative to discourse proximity code

    Returns: 'C' or 'c'
    """

    # Check for emphasis markers
    if context.has_emphasis():
        # Emphatic position (subject position, fronted)
        # Cataphoric "This is what..."
        # Highlighted discourse referent
        return 'C'  # Contextually Near with Focus

    else:
        # Routine anaphoric reference
        # "This thing mentioned earlier"
        # Non-emphatic discourse deixis
        return 'c'  # Contextually Near

    # Note: Greek οὗτος and Hebrew זֶה both commonly anaphoric → default 'c'
```

**Emphasis Indicators:**
- **Subject position**: Demonstrative as sentence subject (Ezek 5:5 זֹאת)
- **Fronting**: Demonstrative + noun fronted for emphasis
- **Cataphoric constructions**: "This is what..." introducing new content
- **Focused NPs**: Demonstrative in focused/contrastive position

**Routine Reference Indicators:**
- **Anaphoric chains**: Referring back to previously mentioned entity
- **Non-focused**: Normal word order, no emphasis
- **Discourse continuity**: Maintaining topic across clauses

### Step 4: Validation and Edge Cases

**Validation Checklist:**

1. **Consistency with source language**:
   - Greek ἐκεῖνος should rarely map to 'N' or 'S' (proximal codes)
   - Hebrew זֶה can map to any spatial code (unmarked)

2. **Narrative coherence**:
   - Characters described as "present" → Use N/S/L/R (not r)
   - Absent characters → Use r or discourse codes

3. **Cross-linguistic plausibility**:
   - If target language is 2-way (this/that), can it distinguish this annotation?
   - If target language is 3-way person-oriented, is speaker/hearer clear?

**Edge Case Handling:**

**Case 1: Ambiguous Demonstratives**
- Greek οὗτος: Both spatial and discourse functions
- **Solution**: Prioritize discourse (`c` or `C`) if no clear physical scene

**Case 2: Hebrew זֶה Ambiguity**
- Unmarked for distance
- **Solution**: Default to `c` (discourse) unless narrative explicitly describes spatial scene

**Case 3: Abstract Nouns with Demonstratives**
- "This righteousness," "that hope"
- **Solution**: Always use discourse codes (`C` or `c`), never spatial

**Case 4: Quoted Speech**
- Must encode from speaker's perspective
- **Solution**: Re-center deixis on quoted speaker, not narrator

## Expected Accuracy

**High Confidence Cases** (90-95% accuracy):
- Greek ἐκεῖνος with clear narrative context → `R` or `r`
- Greek οὗτος in anaphoric discourse → `c` or `C`
- Temporal nouns with demonstratives → `T` or `t`
- Hebrew הַלָּז (rare) → Always `R`

**Medium Confidence Cases** (70-85% accuracy):
- Greek οὗτος in physical scenes → `N`, `S`, or `L` (requires speaker/hearer inference)
- Hebrew זֶה in spatial contexts → Must infer from narrative (ambiguous)
- Discourse emphasis detection → `C` vs `c` (requires syntactic analysis)

**Low Confidence Cases** (50-70% accuracy):
- Boundary between spatial and discourse → May differ from TBTA annotators
- Visibility (R vs r) when not explicitly stated → Inference required
- Near listener (L) in Greek → Rare, context-dependent

**Overall Expected Accuracy**: 80-85% exact match with TBTA annotations

**Variance Sources**:
- Annotator subjectivity in ambiguous contexts
- Different interpretations of narrative scenes
- Undocumented TBTA decision rules

## Implementation Strategy

### Phase 1: Rule-Based Baseline

**Goal**: Implement deterministic rules based on demonstrative forms

```python
def tbta_proximity_baseline(word, context):
    """
    Baseline proximity assignment using source form only
    """
    demo_type, demo_form = identify_demonstrative(word)

    if not demo_type:
        return 'n'  # Not Applicable

    # Simple form-based mapping
    if demo_form == 'ὅδε':
        return 'N'
    elif demo_form == 'οὗτος':
        return 'c'  # Default to discourse
    elif demo_form == 'ἐκεῖνος':
        return 'R'  # Default to remote visible
    elif demo_form in ['זֶה', 'זֹאת']:
        return 'c'  # Default to discourse for Hebrew
    elif demo_form == 'הַלָּז':
        return 'R'
    else:
        return 'n'
```

**Expected Baseline Accuracy**: 60-70%

### Phase 2: Context-Enhanced Rules

**Goal**: Add narrative and syntactic context analysis

**Enhancements**:
1. **Parse narrative scene**: Identify speaker, listener, present participants
2. **Detect temporal nouns**: Route to temporal proximity
3. **Analyze emphasis**: Detect fronting, subject position → `C`
4. **Check visibility**: Infer from perception verbs, location markers

**Expected Phase 2 Accuracy**: 75-80%

### Phase 3: Machine Learning Refinement (Optional)

**Goal**: Train classifier on TBTA examples to learn edge case patterns

**Features**:
- Demonstrative form
- Noun semantic class (person/object/place/time/abstract)
- Sentence position (subject/object/modifier)
- Presence of perception verbs
- Discourse distance (clauses since last mention)
- Speaker/listener markers in context

**Expected Phase 3 Accuracy**: 85-90%

## Validation Experiments

### Experiment 1: Greek Demonstrative Mapping

**Hypothesis**: Greek demonstrative forms predict TBTA proximity at >75% accuracy

**Method**:
1. Extract all nouns with Greek demonstratives from TBTA data
2. Map ὅδε→N, οὗτος→c, ἐκεῖνος→R
3. Compare to TBTA annotations
4. Analyze mismatches

**Success Criteria**: >75% exact match

### Experiment 2: Temporal Proximity Detection

**Hypothesis**: Time nouns + demonstratives map to T/t at >85% accuracy

**Method**:
1. Extract nouns in time semantic domain
2. Check for demonstratives
3. Assign T (proximal demo) or t (distal demo)
4. Compare to TBTA

**Success Criteria**: >85% exact match

### Experiment 3: Discourse Emphasis Detection

**Hypothesis**: Syntactic position predicts C vs c at >70% accuracy

**Method**:
1. Extract discourse proximity codes (C and c)
2. Analyze sentence position, fronting, subject role
3. Predict C if emphatic position, else c
4. Compare to TBTA

**Success Criteria**: >70% exact match

### Experiment 4: Hebrew Contextual Inference

**Hypothesis**: Narrative context clues enable Hebrew proximity assignment at >65% accuracy

**Method**:
1. Extract Hebrew nouns with זֶה
2. Analyze narrative for:
   - Present/absent markers
   - Visual perception verbs
   - Speaker/object proximity language
3. Assign spatial code based on context
4. Compare to TBTA

**Success Criteria**: >65% exact match (Hebrew is harder due to unmarked forms)

## Cross-Linguistic Validation

### Target Language Testing

**Goal**: Verify TBTA codes enable correct demonstrative choice in diverse target languages

**Test Languages**:
1. **Japanese** (3-way person-oriented): これ/それ/あれ
2. **Swahili** (2-way + noun class): huyu/yule, etc.
3. **Spanish** (3-way person-oriented): este/ese/aquel
4. **Yupno** (TNG elevation): Uphill/downhill + distance

**Method**:
1. Select test verses with clear proximity marking
2. Generate demonstrative choices using TBTA codes
3. Have native speakers evaluate naturalness
4. Identify mismatches

**Success Criteria**: >80% native speaker acceptance

## Key Unknowns and Research Questions

### Unknown 1: TBTA Annotator Guidelines

**Question**: What specific guidelines did TBTA annotators follow for edge cases?

**Impact**: High - May explain systematic differences in our reproductions

**Resolution**:
- Seek original TBTA documentation
- Interview TBTA creators if possible
- Infer rules from consistent patterns in data

### Unknown 2: Language-Family-Specific Decisions

**Question**: Did TBTA annotators consider specific target language families when assigning codes?

**Example**: Were Trans-New Guinea languages' needs (elevation) considered differently than Austronesian (visibility)?

**Impact**: Medium - May affect code choice in ambiguous contexts

**Resolution**:
- Analyze TBTA decisions for language-specific patterns
- Test reproduction against diverse target language requirements

### Unknown 3: Discourse Prominence Thresholds

**Question**: What level of emphasis qualifies for `C` (focused) vs `c` (routine)?

**Impact**: Medium - Affects 20-30% of discourse proximity annotations

**Resolution**:
- Analyze syntactic patterns in TBTA `C` vs `c` annotations
- Develop quantitative emphasis scoring

### Unknown 4: Visibility Inference Rules

**Question**: How did TBTA infer visibility (R vs r) when not explicit in text?

**Example**: "That city" - visible or not?

**Impact**: Medium - Affects distal spatial proximity annotations

**Resolution**:
- Examine TBTA patterns for visibility inference
- Develop heuristics based on location types, narrative distance

## Next Steps for Experimentation

1. **Implement baseline rule-based system** (Phase 1)
2. **Extract TBTA proximity annotations** from sample books (Genesis, John)
3. **Run Experiment 1** (Greek demonstrative mapping)
4. **Analyze errors** and refine rules
5. **Add context features** (Phase 2)
6. **Run Experiments 2-4** (temporal, emphasis, Hebrew)
7. **Iterate on edge cases**
8. **Validate with target languages**
9. **Document final reproduction method**

## Thesis Summary

**Proximity annotations can be reproduced at 80-85% accuracy through:**

1. **Demonstrative form analysis** (Greek/Hebrew source)
2. **Contextual classification** (spatial/temporal/discourse)
3. **Rule-based mapping** with context-aware refinements
4. **Edge case handling** for ambiguous Hebrew and discourse emphasis

**Key Success Factors:**
- Greek forms are highly predictive (ὅδε/οὗτος/ἐκεῖνος → clear mappings)
- Temporal nouns easy to detect and classify
- Discourse proximity most common, serves as reasonable default
- Hebrew requires narrative context analysis (more challenging)

**Primary Challenge:**
- Hebrew זֶה unmarked for distance → Requires sophisticated context inference
- Discourse emphasis detection (C vs c) → Needs syntactic analysis
- Visibility inference (R vs r) → Often ambiguous without explicit markers

**Confidence**: HIGH that method will achieve 80-85% accuracy
**Timeline**: 2-3 experimentation cycles to refine rules and validate

---

**Document Status**: Ready for Experimentation
**Next Action**: Implement Phase 1 baseline and run Experiment 1
