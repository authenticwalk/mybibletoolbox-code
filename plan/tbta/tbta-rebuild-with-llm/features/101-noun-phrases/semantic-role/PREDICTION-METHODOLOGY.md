# Semantic Role Prediction Methodology

This document provides the detailed 5-level hierarchical prompt template for predicting semantic roles in Biblical Greek and Hebrew texts.

---

## Overview

**Goal:** Assign semantic roles (Agent, Patient, Theme, Experiencer, Instrument, Beneficiary, Location, Goal, Source, Stimulus) to noun phrases based on syntactic position, verb semantics, morphology, and context.

**Approach:** Hierarchical decision tree (5 levels) from most reliable signals (syntax) to least reliable (context).

**Expected Accuracy:** 80-85% overall (higher for Agent/Patient, lower for ambiguous Experiencer)

---

## Level 1: Grammatical Role → Initial Role Hypothesis

**Principle:** Grammatical function provides the strongest initial signal for semantic role.

### Rule Set

**Subject of Transitive Verb:**
- **Default:** Agent (60% probability)
- **Alternative:** Experiencer (30% probability - if perception/psych verb)
- **Rare:** Theme (10% probability - if passive-like or unaccusative)

**Subject of Intransitive Verb:**
- **Default:** Theme (50% probability - motion/change verbs)
- **Alternative:** Agent (30% probability - volitional unergatives: "pray," "speak")
- **Alternative:** Experiencer (20% probability - psych/perception verbs)

**Direct Object:**
- **Default:** Patient (70% probability)
- **Alternative:** Stimulus (20% probability - perception verbs)
- **Alternative:** Theme (10% probability - creation/motion verbs)

**Indirect Object / Dative:**
- **Default:** Beneficiary (50% probability)
- **Alternative:** Experiencer (30% probability - psych verbs)
- **Alternative:** Goal (20% probability - motion verbs)

**Prepositional Phrases:**
- **Locative preps** (ἐν, εἰς, πρός, ב) → Location / Goal
- **Ablative preps** (ἀπό, ἐκ, מן) → Source
- **Instrumental preps** (ἐν [+instrument], διά, ב) → Instrument
- **Benefactive preps** (ὑπέρ, περί, ל) → Beneficiary

### Implementation

```python
def level_1_grammatical_role(np, clause_structure):
    """
    Assign initial semantic role based on grammatical position

    Args:
        np: Noun phrase data (case, position, modifiers)
        clause_structure: Parsed clause (subject, verb, objects, adjuncts)

    Returns:
        role_hypothesis: Initial role (e.g., "Agent", "Patient")
        confidence: 0.0-1.0
    """

    # Subject
    if np.grammatical_role == "Subject":
        if clause_structure.verb.transitivity == "Transitive":
            return "Agent", 0.6
        elif clause_structure.verb.transitivity == "Intransitive":
            return "Theme", 0.5

    # Direct Object
    elif np.grammatical_role == "DirectObject":
        return "Patient", 0.7

    # Indirect Object / Dative case
    elif np.grammatical_role == "IndirectObject" or np.case == "Dative":
        return "Beneficiary", 0.5

    # Prepositional Phrase
    elif np.grammatical_role == "PrepositionalPhrase":
        prep = np.preposition.lemma

        # Location
        if prep in ["ἐν", "εἰς", "πρός", "ב", "ל"]:
            if is_location_noun(np.head_noun):
                return "Location", 0.8
            elif is_person_noun(np.head_noun):
                return "Goal", 0.7

        # Source
        elif prep in ["ἀπό", "ἐκ", "מן"]:
            return "Source", 0.8

        # Instrument
        elif prep in ["ἐν", "διά", "ב"] and is_instrument_noun(np.head_noun):
            return "Instrument", 0.7

        # Beneficiary
        elif prep in ["ὑπέρ", "περί", "ל"]:
            return "Beneficiary", 0.7

    # Default fallback
    return "Unknown", 0.3
```

---

## Level 2: Verb Semantics → Role Refinement

**Principle:** Verb semantic class determines which roles are expected and how they map to syntactic positions.

### Verb Semantic Classes

**Action Verbs (hit, kill, send, build):**
- Subject → **Agent** (volitional actor)
- Object → **Patient** (affected entity)

**Perception Verbs (see, hear, smell, taste, touch):**
- Subject → **Experiencer** (perceiver, not volitional agent)
- Object → **Stimulus** (perceived entity)

**Cognition Verbs (know, think, believe, understand):**
- Subject → **Experiencer** (thinker)
- Object → **Stimulus** or **Theme** (content of thought)

**Emotion Verbs (love, fear, rejoice, mourn):**
- Subject → **Experiencer** (feeler)
- Object → **Stimulus** (cause of emotion)

**Motion Verbs (go, come, enter, depart):**
- Subject → **Theme** (entity moving, not volitional agent)
- Prepositional phrase → **Goal** (destination) or **Source** (origin)

**Change-of-State Verbs (become, arise, grow, die):**
- Subject → **Theme** (entity changing)

**Communication Verbs (say, tell, speak, preach):**
- Subject → **Agent** (speaker)
- Object → **Theme** (message content) or **Goal** (addressee)

**Creation Verbs (make, create, build):**
- Subject → **Agent** (creator)
- Object → **Theme** (created entity, not affected patient)

### Implementation

```python
def level_2_verb_semantics(role_hypothesis, verb, np):
    """
    Refine semantic role based on verb semantic class

    Args:
        role_hypothesis: Initial role from Level 1
        verb: Verb data (lemma, semantic class)
        np: Noun phrase

    Returns:
        refined_role: Updated role
        confidence: Updated confidence
    """

    verb_class = get_semantic_class(verb.lemma)

    # Perception verbs: Subject = Experiencer (not Agent)
    if verb_class == "Perception":
        if np.grammatical_role == "Subject":
            return "Experiencer", 0.85
        elif np.grammatical_role == "DirectObject":
            return "Stimulus", 0.85

    # Cognition verbs: Similar to perception
    elif verb_class == "Cognition":
        if np.grammatical_role == "Subject":
            return "Experiencer", 0.8
        elif np.grammatical_role == "DirectObject":
            return "Stimulus", 0.75  # Could also be Theme

    # Motion verbs: Subject = Theme (not Agent)
    elif verb_class == "Motion":
        if np.grammatical_role == "Subject":
            return "Theme", 0.85

    # Change-of-state: Subject = Theme
    elif verb_class == "ChangeOfState":
        if np.grammatical_role == "Subject":
            return "Theme", 0.9

    # Action verbs: Subject = Agent (high confidence)
    elif verb_class == "Action":
        if np.grammatical_role == "Subject":
            return "Agent", 0.9
        elif np.grammatical_role == "DirectObject":
            return "Patient", 0.9

    # Creation verbs: Object = Theme (created, not affected)
    elif verb_class == "Creation":
        if np.grammatical_role == "DirectObject":
            return "Theme", 0.85

    # No refinement needed
    return role_hypothesis, 0.6
```

**Verb Class Lexicon (Sample):**
- **Perception:** ὁράω (see), ἀκούω (hear), ראה (see), שמע (hear)
- **Cognition:** γινώσκω (know), νοέω (think), ידע (know)
- **Emotion:** ἀγαπάω (love), φοβέω (fear), אהב (love)
- **Motion:** ἔρχομαι (come), πορεύομαι (go), הלך (walk), בוא (come)
- **Change-of-State:** γίνομαι (become), ἀνίστημι (arise), היה (become)
- **Action:** ποιέω (do), ἀποκτείνω (kill), πέμπω (send), עשה (do)
- **Creation:** κτίζω (create), ποιέω (make), ברא (create)

---

## Level 3: Voice and Case Marking → Role Adjustment

**Principle:** Morphological voice (active/middle/passive) and case marking provide additional constraints on role assignment.

### Voice Rules

**Passive Voice:**
- Subject → **Patient** (affected entity, not Agent)
- "by" phrase → **Agent** (demoted to oblique)
- Example: "The man was healed **by Jesus**"
  - "man" = Patient (subject)
  - "by Jesus" = Agent (oblique)

**Middle Voice (Greek):**
- Subject → **Agent + Patient** (reflexive: agent acts on self)
- Or Subject → **Beneficiary** (benefactive middle: action for oneself)
- Example: ἐβαπτίσαντο (they baptized themselves)
  - "they" = Agent + Patient (reflexive)

**Active Voice:**
- No change to default roles (Agent, Patient, Theme as predicted)

### Case Marking (Greek)

**Nominative:**
- Default for Subject → Agent / Theme / Experiencer (determined by verb)

**Accusative:**
- Default for DirectObject → Patient / Stimulus / Theme
- Can also mark Goal with motion verbs (εἰς + accusative)

**Genitive:**
- Often possessor (not semantic role of main clause)
- Can mark Source (ἐκ, ἀπό + genitive)

**Dative:**
- Beneficiary, Experiencer, Location, Instrument
- Requires Level 2 verb semantics to disambiguate

### Implementation

```python
def level_3_voice_and_case(role, voice, case, verb_semantics):
    """
    Adjust semantic role based on voice and case marking

    Args:
        role: Current role hypothesis
        voice: Verb voice (Active, Middle, Passive)
        case: NP case (Nominative, Accusative, Genitive, Dative)
        verb_semantics: Verb semantic class

    Returns:
        adjusted_role: Updated role
        confidence: Updated confidence
    """

    # Passive: Subject is Patient
    if voice == "Passive":
        if case == "Nominative":  # Subject
            return "Patient", 0.95

    # Middle: Subject may be Agent+Patient (reflexive)
    elif voice == "Middle":
        if case == "Nominative":
            if verb_semantics in ["Action", "Grooming"]:
                return "Agent", 0.8  # Acts on self, but still agent

    # Case-specific adjustments
    if case == "Dative":
        # Dative + perception/emotion verb → Experiencer
        if verb_semantics in ["Perception", "Cognition", "Emotion"]:
            return "Experiencer", 0.85
        else:
            return "Beneficiary", 0.7

    # No adjustment
    return role, 0.7
```

---

## Level 4: Animacy and Word Order → Disambiguation

**Principle:** Animate entities are more likely to be Agents; inanimate entities more likely Patients/Themes/Instruments. Word order can also provide cues in flexible languages.

### Animacy Hierarchy

**High Animacy (strong Agent preference):**
- Personal names (Jesus, Peter, Mary)
- Personal pronouns (he, she, I, you)
- Titles (King, Lord, Prophet)
- Human nouns (man, woman, disciple, crowd)

**Medium Animacy:**
- Animals (sheep, fish, serpent)
- Collective groups (nation, people)
- Spiritual beings (angel, demon, spirit)

**Low Animacy (strong Patient/Theme preference):**
- Concrete objects (stone, bread, water)
- Abstract concepts (truth, love, sin)
- Natural phenomena (wind, fire, earthquake)

### Animacy Rules

**High Animacy + Transitive Verb:**
- If Subject → **Agent** (95% confidence)
- If Object → **Patient** (80% confidence, could be Theme)

**Low Animacy + Transitive Verb:**
- If Subject → **Theme** (70% confidence, likely passive or unaccusative)
- If Object → **Patient** or **Theme** (80% confidence)
- In prepositional phrase → **Instrument** (70% confidence if with action verb)

**Mixed Animacy (High Anim Subject + Low Anim Object):**
- Subject → **Agent** (95% confidence)
- Object → **Patient** (90% confidence)

**Mixed Animacy (Low Anim Subject + High Anim Object):**
- Likely passive or unusual construction
- Subject → **Theme** or **Instrument** (70% confidence)
- Object → **Patient** (80% confidence)

### Word Order (Greek/Hebrew)

**Greek:** Flexible word order, but VSO/SVO most common
- Pre-verbal subject → Topicalized (may indicate Agent emphasis)
- Post-verbal subject → New information (may be Theme in unaccusative)

**Hebrew:** VSO standard
- Verb-initial → Narrative continuation
- Subject-initial → Topicalization or clause boundary

**Word order provides weak signal; use only when other levels ambiguous.**

### Implementation

```python
def level_4_animacy_word_order(role, np, clause):
    """
    Refine role using animacy and word order

    Args:
        role: Current role hypothesis
        np: Noun phrase (with animacy score)
        clause: Clause structure (word order)

    Returns:
        refined_role: Updated role
        confidence: Updated confidence
    """

    animacy = get_animacy_score(np)  # 0.0 (inanimate) to 1.0 (human)

    # High animacy subject + transitive → Agent
    if np.grammatical_role == "Subject" and animacy > 0.8:
        if clause.verb.transitivity == "Transitive":
            return "Agent", 0.9

    # Low animacy subject + transitive → Theme (likely passive/unaccusative)
    elif np.grammatical_role == "Subject" and animacy < 0.3:
        if clause.verb.transitivity == "Transitive":
            return "Theme", 0.7

    # Low animacy + prepositional phrase + action verb → Instrument
    elif np.grammatical_role == "PrepositionalPhrase" and animacy < 0.3:
        if clause.verb.semantic_class == "Action":
            if np.preposition.lemma in ["ἐν", "διά", "ב"]:
                return "Instrument", 0.75

    # No refinement
    return role, 0.7
```

---

## Level 5: Context and Discourse → Final Disambiguation

**Principle:** Discourse context and co-reference can resolve remaining ambiguities.

### Context Clues

**Co-reference:**
- If NP refers to previously mentioned Agent → likely Agent again
- If NP refers to previously mentioned Patient → likely Patient again

**Discourse Role:**
- Main character (Jesus in Gospels) → high Agent probability
- Secondary characters → may be Patient or Beneficiary

**Parallel Structures:**
- "He healed the sick and **cleansed the lepers**"
- "lepers" parallel to "sick" → both Patient

**Negation:**
- Negation doesn't change semantic role
- "He did not heal the man" → "man" still Patient

### Implementation

```python
def level_5_context_discourse(role, np, discourse_context):
    """
    Final role refinement using discourse context

    Args:
        role: Current role hypothesis
        np: Noun phrase
        discourse_context: Previous mentions, main characters

    Returns:
        final_role: Final semantic role
        confidence: Final confidence
    """

    # Check if NP co-refers with previous mention
    previous_role = discourse_context.get_previous_role(np.referent)

    if previous_role:
        # Strong preference to maintain role across mentions
        return previous_role, 0.85

    # Check if NP is main discourse character
    if np.referent in discourse_context.main_characters:
        # Main characters more likely to be Agents
        if role in ["Agent", "Experiencer"]:
            return role, 0.85

    # No refinement needed
    return role, 0.75
```

---

## Complete Pipeline

```python
def predict_semantic_role(np, clause, discourse_context):
    """
    Complete 5-level hierarchical semantic role prediction

    Args:
        np: Noun phrase data
        clause: Clause structure (verb, arguments, adjuncts)
        discourse_context: Discourse history

    Returns:
        semantic_role: Predicted role (Agent, Patient, Theme, etc.)
        confidence: 0.0-1.0
    """

    # Level 1: Grammatical role
    role, conf = level_1_grammatical_role(np, clause)

    # Level 2: Verb semantics
    role, conf = level_2_verb_semantics(role, clause.verb, np)

    # Level 3: Voice and case
    role, conf = level_3_voice_and_case(
        role,
        clause.verb.voice,
        np.case,
        clause.verb.semantic_class
    )

    # Level 4: Animacy and word order
    role, conf = level_4_animacy_word_order(role, np, clause)

    # Level 5: Context and discourse
    role, conf = level_5_context_discourse(role, np, discourse_context)

    return role, conf
```

---

## Validation and Testing

### Test Set Construction

**50-verse test set:**

| **Verb Class** | **Verses** | **Target Roles** |
|----------------|-----------|------------------|
| Action (transitive) | 15 | Agent, Patient |
| Perception | 8 | Experiencer, Stimulus |
| Motion | 8 | Theme, Goal, Source |
| Change-of-state | 5 | Theme |
| Emotion/Cognition | 7 | Experiencer, Stimulus |
| Passive voice | 7 | Patient (subject), Agent (oblique) |

**Ground Truth:**
- Manual annotation by linguist
- Cross-checked against published grammars and translations
- Focus on ambiguous cases (Experiencer vs. Agent)

### Expected Accuracy by Role

| **Role** | **Expected Accuracy** | **Difficulty** |
|----------|-----------------------|----------------|
| Agent | 85-90% | Moderate (confusion with Experiencer) |
| Patient | 85-90% | Low (clear syntactic position) |
| Theme | 75-85% | Moderate (confusion with Patient) |
| Experiencer | 70-80% | High (hard to distinguish from Agent) |
| Instrument | 75-80% | Moderate (depends on preposition) |
| Beneficiary | 70-75% | Moderate (ambiguous dative) |
| Location/Goal/Source | 80-85% | Low (clear prepositional marking) |
| Stimulus | 75-80% | Moderate (depends on verb class) |

**Overall Expected:** 80-85%

---

## Error Analysis

**Common Errors:**

1. **Experiencer ↔ Agent confusion**
   - Perception/cognition verbs
   - Solution: Strengthen Level 2 verb semantic lexicon

2. **Theme ↔ Patient confusion**
   - Creation verbs, motion verbs
   - Solution: Distinguish affected (Patient) from created/moved (Theme)

3. **Beneficiary ↔ Experiencer with dative**
   - Ambiguous dative case
   - Solution: Level 2 verb semantics (psych verbs → Experiencer)

4. **Instrument ↔ Location with ἐν**
   - ἐν "in/with" ambiguous
   - Solution: Level 4 animacy (inanimate → Instrument)

**Mitigation:**
- Expand verb semantic lexicon (Level 2)
- Add animacy lexicon (Level 4)
- Use discourse history more aggressively (Level 5)

---

## Output Schema

```yaml
verse: JHN.003.016
noun_phrases:
  - text: "God"
    lemma: "θεός"
    case: "Nominative"
    grammatical_role: "Subject"
    semantic_role: "Agent"
    confidence: 0.90
    prediction_levels:
      level_1: "Agent (0.60)"
      level_2: "Agent (0.90) - action verb"
      level_3: "Agent (0.90) - active voice"
      level_4: "Agent (0.90) - high animacy"
      level_5: "Agent (0.90) - main character"

  - text: "the world"
    lemma: "κόσμος"
    case: "Accusative"
    grammatical_role: "DirectObject"
    semantic_role: "Patient"
    confidence: 0.90
    prediction_levels:
      level_1: "Patient (0.70)"
      level_2: "Patient (0.90) - action verb"
      level_3: "Patient (0.90) - active voice, accusative"
      level_4: "Patient (0.90) - low animacy object"
      level_5: "Patient (0.90) - no discourse override"
```

---

**Document Status:** Production-ready prediction methodology
**Last Updated:** 2025-11-07
**Next Steps:** Implement prediction pipeline and validate on 50-verse test set
