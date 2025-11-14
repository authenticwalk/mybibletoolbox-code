# TBTA Feature Structure & Relationships

⚠️ **Status**: Experimental - Based on early TBTA analysis (Nov 2025), not validated with TBTA team

## Purpose

This directory documents how TBTA linguistic features relate to each other in nested hierarchical structures. Understanding these relationships helps:
- Predict one feature based on others (e.g., illocutionary force constrains mood)
- Validate annotations for consistency
- Build dependency graphs for feature development order
- Design efficient annotation workflows

## Hierarchical Structure

### Document Hierarchy
```
Clause (Part: 105)
├─ NP (Part: 101) - Noun Phrase
│  ├─ Noun (Part: 1)
│  └─ Adjective (Part: 3)
├─ VP (Part: 102) - Verb Phrase
│  └─ Verb (Part: 2)
├─ AdjP (Part: 103) - Adjective Phrase
├─ AdvP (Part: 104) - Adverb Phrase
└─ Punctuation
```

### Part Codes
**Word-level**: 1=Noun, 2=Verb, 3=Adjective, 4=Adverb, 5=Adposition, 6=Conjunction, 7=Phrasal, 8=Particle
**Phrase-level**: 101=NP, 102=VP, 103=AdjP, 104=AdvP, 105=Clause

## Feature Dependencies

### Clause-Level Features

**Clause attributes affect all children:**
```
Clause
├─ Illocutionary Force → constrains Verb Mood
│  └─ Imperative force requires careful mood encoding
├─ Discourse Genre → affects Time interpretation
│  ├─ Narrative → historic/recent past codes
│  ├─ Theological → discourse time code
│  └─ Hortatory → future/obligation codes
├─ Salience Band → affects Participant Tracking
└─ Speaker/Listener Demographics
   ├─ Speaker Age → Honorifics, Register
   ├─ Listener Age → Formality
   └─ Relationship → Speech Style
```

### Verb Phrase Hierarchy

**Verb features build on each other:**
```
Verb
├─ Time (20+ values)
│  └─ Constrained by Discourse Genre
├─ Aspect (15+ values)
│  └─ Default: Unmarked (unless explicit marking)
├─ Mood (10+ values)
│  ├─ Default: Indicative
│  └─ Constrained by Illocutionary Force
├─ Polarity (Affirmative/Negative)
└─ Reflexivity (Reflexive/Reciprocal/N/A)
```

### Noun Phrase Hierarchy

**Noun features have internal dependencies:**
```
Noun Phrase
├─ Semantic Role (Agent-like, Patient-like, etc.)
├─ Topic Marking
└─ Head Noun
   ├─ Participant Tracking (5 states)
   │  └─ Affects Surface Realization
   ├─ Number System (S/D/T/Q/p/P)
   ├─ Person System (1st/2nd/3rd + derived)
   │  └─ Clusivity (only if Person = 1st)
   ├─ Polarity (Affirmative/Negative)
   ├─ Proximity (10 values, if demonstrative)
   │  ├─ Spatial (N/S/L/R/r)
   │  ├─ Temporal (T/t)
   │  └─ Discourse (C/c)
   └─ Surface Realization
      └─ Constrained by Participant Tracking
```

### Adjective/Adverb Features

**Modifier features:**
```
Adjective/Adverb
├─ Degree (11 values)
│  ├─ Default: N (No Degree)
│  ├─ Comparative (C/i)
│  ├─ Superlative (S/s)
│  ├─ Equality (q)
│  ├─ Intensified (I/E/V)
│  └─ Excessive (T)
├─ Usage (AdjP only: Attributive/Predicative)
└─ Sequence (coordination status)
```

## Cross-Feature Dependencies

### Validated Dependencies

**Strong constraints (high confidence):**
- Illocutionary Force → Mood
  - Imperative clauses → Verb mood stays Indicative (force at clause level)
- Person → Clusivity
  - Clusivity only applicable if Person = 1st
- Participant Tracking → Surface Realization
  - First Mention → indefinite forms
  - Frame Inferable → definite on first mention
  - Routine → pronouns or repeated NPs
- Participant Tracking → NounListIndex
  - Index assigned when tracking status requires it

### Suspected Dependencies (needs validation)

**Plausible but unconfirmed:**
- Speaker Demographics → Honorifics/Register
  - Age difference may affect formality encoding
- Discourse Genre → Time Granularity
  - Narrative may require more specific time codes
  - Theological may use broader time concepts
- Semantic Role → Surface Realization
  - Agent-like roles may prefer certain realizations
- Proximity Type → Semantic Role
  - Spatial proximity for concrete participants
  - Discourse proximity for abstract/propositional

## Annotation Priority Order

Based on dependencies, suggested annotation sequence:

**1. Clause-level (establishes context):**
- Type, Illocutionary Force, Discourse Genre, Salience Band

**2. Phrase-level (establishes structure):**
- Semantic Role, Sequence, Relativized, Implicit

**3. Word-level - Nouns:**
- Participant Tracking (check presupposition first!)
- Number (semantic, not morphological)
- Person (enables Clusivity)
- Clusivity (if Person = 1st)
- Polarity
- Proximity (if demonstrative context)
- Surface Realization

**4. Word-level - Verbs:**
- Time (genre/discourse-driven)
- Aspect (default: Unmarked)
- Mood (default: Indicative, check clause force)
- Polarity
- Reflexivity

**5. Word-level - Modifiers:**
- Degree (default: N)
- Usage (if adjective)

## Special Case Patterns

### Presupposed Entities
**Always check first** - overrides normal tracking:
```
Presupposed: God, Yahweh, Lord, Jesus, sun, sky
→ Participant Tracking = Routine (even on first textual mention)
```

### Trinity Contexts
**Unique number/person combinations:**
```
Genesis 1:26 "Let us make..."
- God (narrator) → Number: Singular, Person: Third
- us (speaker) → Number: Trial, Person: First Inclusive
- Same referent, different discourse roles!
```

### Semantic vs. Morphological Number
**TBTA uses semantic count, not source morphology:**
```
Hebrew שָׁמַיִם (dual morphology) → TBTA: Singular (one sky)
Hebrew מַיִם (dual morphology) → TBTA: Singular (water as mass)
```

### Genre-Driven Time Codes
**Discourse context overrides morphology:**
```
Greek aorist:
- Narrative → Historic Past
- Theological (John 3:16) → Discourse
- Promissory (Beatitudes) → Immediate Future
```

## Validation Patterns

### Frequency Expectations

**Participant Tracking:**
- Routine: 60-80%
- Generic: 5-20% (higher in wisdom literature)
- Frame Inferable: 5-10%
- First Mention: 3-8%
- Interrogative: 0-2%

**Number:**
- Singular: most common
- Plural: common
- Dual/Trial/Paucal: rare (Trial mainly Trinity contexts)

**Verb Features:**
- Aspect Unmarked: 70%+
- Mood Indicative: 90%+
- Polarity Affirmative: 90%+

### Coherence Checks

**Valid referent chains:**
- First Mention → Routine → Routine ✓
- Frame Inferable → Routine → Routine ✓
- Presupposed → Routine (from start) ✓

**Invalid patterns:**
- Routine → First Mention (contradiction!)
- Generic → Routine (generic refs don't become tracked)

## Implementation Notes

### For Tool Developers

When building TBTA annotation tools:
1. Implement clause-level features first (they constrain children)
2. Check presupposition database before tracking states
3. Use genre/discourse to drive Time codes, not just morphology
4. Default to Unmarked/Indicative/N unless explicit evidence
5. Validate frequency distributions against expected ranges

### For Researchers

When analyzing TBTA features:
1. Extract dependency graphs from existing annotations
2. Test suspected dependencies with statistical measures
3. Build frame databases (common frames: creation, temple, well, shepherd, etc.)
4. Document exceptions and edge cases
5. Validate with TBTA team before treating as canonical

## Future Work

This analysis needs:
- [ ] Validation with TBTA team on dependency claims
- [ ] Statistical testing of suspected dependencies
- [ ] Expanded frame database for Frame Inferable detection
- [ ] Cross-genre frequency distribution baselines
- [ ] Integration with STAGES.md methodology
- [ ] Tool-specific validation patterns

## Sources

Based on analysis of:
- TBTA reproduction prompt experiments (Nov 2025)
- Genesis 1, Matthew 5, John 3 annotations
- Feature distribution studies
- Cross-linguistic typology patterns

⚠️ **Remember**: This is experimental analysis, not official TBTA documentation. Always consult TBTA team for authoritative guidance.

## See Also

- `/bible-study-tools/tbta/features/` - Individual feature documentation
- `/plan/tbta-rebuild-with-llm/combined/reproduction-prompt.md` - Original (outdated) analysis source
- `STAGES.md` - TBTA development methodology
