# Participant Tracking: Patterns Learned from TBTA

**Purpose**: Extract decision rules from TBTA training analysis
**Date**: 2025-11-11
**Source**: TBTA-ANNOTATIONS.md analysis of 4 verses + 3,067 corpus annotations
**Goal**: Foundation for Algorithm v1.0 development (Phase 4)

---

## Decision Framework Overview

Participant tracking states are **hierarchical** and **contextual**. Higher-priority rules override lower ones.

**Priority Order** (check in this sequence):
1. **Interrogative (Q)** - Question context (most specific)
2. **Generic (G)** - Type/class reference (semantic)
3. **Frame Inferable (F)** - Scenario-expected participants
4. **First Mention (I) vs. Routine (D)** - Novel vs. established (default decision)

---

## Rule 1: Interrogative (Q) - HIGHEST PRIORITY

**When to apply**: Participant occurs in question context

### Sub-rules:

**1.1 Direct question referent**
- Participant is the questioned entity
- Occurs with interrogative words: who, what, which, whom, whose
- **Example**: "which **command** is greatest?" → command = Interrogative

**1.2 Identity questions**
- "Who are you?" → "you" = Interrogative
- "What is this?" → "this" = Interrogative

**1.3 Selection questions**
- "Which X?" → X = Interrogative
- "Whom do you seek?" → "whom" = Interrogative

**1.4 Transition after question**
- Same participant OUTSIDE question clause → revert to Routine
- **Example**: MAT 22:36 - "command" = Interrogative in question, then Routine in answer

### Surface form indicators:
- Interrogative pronouns (who, what, which, whom)
- Question clauses (illocutionary force = interrogative)
- Questioned referent position

### Frequency: 0.2% (7/3,067 annotations)

### Decision:
✅ If participant is questioned referent → **Interrogative**
✅ If same participant outside question → proceed to Rule 2

---

## Rule 2: Generic (G) - HIGH PRIORITY

**When to apply**: Participant refers to class/type, not specific individual

### Sub-rules:

**2.1 Universal quantifiers**
- Particles: whosoever, whoever, anyone, everyone, all
- **Example**: "**whosoever** believeth" → Generic (any person who believes)
- Pattern: Refers to class of believers, not specific individuals

**2.2 Negative existentials**
- Negative polarity: no one, no person, none, nothing
- **Example**: "**no person** was there" → Generic (absence of any individual)
- Pattern: Refers to class universally negated

**2.3 Abstract concepts as types**
- Abstract nouns: life, death, love, wisdom
- **Example**: "everlasting **life**" → Generic (life as concept, not specific instance)
- Pattern: Type reference, not token
- **Contrast**: "his life" (specific) = Routine

**2.4 Vocative/role titles**
- Address terms: Teacher, Master, Lord, Sir
- **Example**: "**Teacher**, which command...?" → Generic (role title, not individual reference)
- Pattern: Used to address, not to refer as participant
- **Note**: May overlap with Routine if used as referential (needs context)

**2.5 Hypothetical participants**
- Conditional/counterfactual contexts
- "If anyone...", "Suppose a man..."
- Pattern: Hypothetical scenarios, not actual participants

**2.6 Proverbial/wisdom statements**
- Wisdom literature generic "man", "fool", "wise"
- **Example**: "There is a way that seemeth right unto **a man**" (Proverbs) → Generic
- Pattern: Universal principle, not specific referent

### Surface form indicators:
- Bare nouns (person, man, life)
- Quantifiers (all, any, every, no)
- Indefinite in universal context ("a man" in proverbs)
- Abstract nouns
- Role titles/vocatives

### Frequency: 15.8% (485/3,067 annotations)

### Decision:
✅ If universal quantifier → **Generic**
✅ If negative existential → **Generic**
✅ If abstract type reference → **Generic**
✅ If vocative role title → **Generic**
✅ Otherwise → proceed to Rule 3

---

## Rule 3: Frame Inferable (F) - MEDIUM PRIORITY

**When to apply**: Participant is inferable from scene/frame, even if not previously mentioned

### Sub-rules:

**3.1 Relational inference**
- Participant inferable from relationship
- **Example**: "God gave his only **son**" → son = Frame Inferable (inferable from "God" as father)
- Pattern: Kinship, social roles, possessive relationships
- **Common relations**: son/father, wife/husband, servant/master, disciple/teacher

**3.2 Frame-based inference (Creation frame)**
- Scene: Creation
- Frame-setting verb: "create"
- **Example**: "God created **the sky** and **the earth**" → sky, earth = Frame Inferable
- Pattern: Created objects inferable from creation act

**3.3 Frame-based inference (Other frames)**
- **Inn frame**: inn → innkeeper (inferable)
- **Household frame**: house → family members (inferable)
- **Legal/trial frame**: trial → scribes, elders, officials (inferable)
- **Travel frame**: journey → travelers, road (inferable)
- **Meal frame**: table → food, guests (inferable)

**3.4 Temporal frames**
- **Example**: "In **the beginning**..." → beginning = Frame Inferable (temporal frame setter)
- Pattern: Time references inferable as temporal setting

**3.5 Definite on first mention**
- Definite article ("the") on first occurrence of participant
- **Diagnostic**: Definite signals speaker assumes hearer can identify referent (frame makes it accessible)
- **Example**: "the sky" (Gen 1:1) - definite despite first mention because creation frame makes it inferable

### Surface form indicators:
- Definite NP on first mention ("the X" where X not previously mentioned)
- Relational nouns (son, father, wife, servant, master)
- Frame-specific vocabulary (sky/earth in creation, innkeeper at inn)

### Frequency: 6.3% (194/3,067 annotations)

### Decision:
✅ If relational noun (kinship, social role) → **Frame Inferable**
✅ If definite on first mention + frame-expected → **Frame Inferable**
✅ If scene-inferable participant (inn→innkeeper, trial→officials) → **Frame Inferable**
✅ Otherwise → proceed to Rule 4

---

## Rule 4: First Mention (I) vs. Routine (D) - DEFAULT DECISION

**When to apply**: After Rules 1-3 do not apply, decide between new vs. established participant

### Rule 4A: First Mention (I)

**When to apply**: Participant is NEW to discourse, not previously mentioned or inferable

**4A.1 Indefinite article on introduction**
- Indefinite "a/an" signals new, not-yet-identified referent
- **Example**: "**a woman** of Samaria" → First Mention (indefinite, new participant)
- **Example**: "**a solitary place**" → First Mention (new location, not inferable)

**4A.2 Proper names at narrative introduction**
- Genealogical introductions: "These are the generations of **Noah**"
- New narrative focus: First mention of character's name
- **Pattern**: Proper name introduced for first time in narrative

**4A.3 Truly novel participants**
- Not mentioned before
- Not inferable from frame or context
- Introduced as new information

**Surface form**:
- Indefinite article ("a", "an", "some")
- Proper names (first occurrence in narrative)
- Demonstrative + new referent ("this X" where X is new)

**Frequency**: 6.0% (185/3,067 annotations)

---

### Rule 4B: Routine (D)

**When to apply**: Participant is ESTABLISHED in discourse, ongoing presence

**4B.1 Repeated mentions**
- Second, third, fourth+ mentions of same participant
- **Example**: "Jesus...Jesus...Jesus...Jesus" (4x in Mark 1:35) → all Routine
- **Pattern**: Continuous narrative presence

**4B.2 Pronouns and zero anaphora**
- Pronouns (he, she, it, they) → Routine (refer to established participants)
- Zero anaphora (pro-drop): verb without subject → subject = Routine

**4B.3 Definite NPs for established referents**
- "the house" (mentioned earlier) → Routine
- "the town" (established context) → Routine
- **Contrast**: "the house" on first mention in household frame → Frame Inferable

**4B.4 Main narrative participants**
- Protagonist throughout extended narrative
- **Example**: Jesus in Gospels, God in creation narrative → Routine
- **Pattern**: Continuous tracking of central figures

**4B.5 Theologically presupposed entities** ⭐
- **Special case**: "God" marked Routine even in Genesis 1:1 (first verse of Bible)
- **Reason**: TBTA treats God as always-accessible in Biblical discourse
- **Generalization**: Core theological concepts presupposed, not introduced
- **Other potential presuppositions**: Heaven, Satan, sin, law (needs validation)

**4B.6 Established context from prior discourse**
- Participants mentioned earlier in chapter/book
- Scene elements already established
- **Example**: "his disciples" (after disciples introduced) → Routine

**4B.7 Continued reference after question**
- Participant was Interrogative in question → becomes Routine afterward
- **Example**: "command" = Interrogative ("which command?") → Routine ("the greatest command")

**Surface form**:
- Proper nouns (continued reference)
- Definite article ("the X" for established X)
- Pronouns (he, she, it, they)
- Zero (pro-drop languages)

**Frequency**: 71.6% (2,196/3,067 annotations) - **DOMINANT STATE**

---

## Special Cases and Edge Cases

### Edge Case 1: God as Routine (Genesis 1:1)

**Pattern**: "God" marked Routine even at first mention in Bible

**Explanation**: Theological presupposition - God's existence/presence assumed, not introduced

**Algorithm handling**:
- Special rule: "God" (and variants: LORD, Yahweh, Elohim) → always Routine unless in Interrogative context
- **Rationale**: Biblical texts presuppose God's accessibility

---

### Edge Case 2: Definite Article Ambiguity

**Problem**: Definite article ("the") can mark three different states:
1. Routine: "the house" (established)
2. Frame Inferable: "the sky" (creation frame, first mention)
3. First Mention: "the Noah" (proper names, first mention)

**Solution**: Context-dependent decision:
1. Check if frame makes it inferable (Rule 3)
2. Check if mentioned before → Routine
3. Check if proper name → First Mention
4. Default → Routine (most common)

---

### Edge Case 3: Place Reference Inconsistency (Mark 1:35)

**Observed**: "place" marked First Mention, then First Mention again, then Routine

**Expected**: "place" → First Mention (1st), Routine (2nd+)

**Possible explanation**:
- TBTA error (annotation inconsistency)
- OR: Complex discourse rule (referent reintroduced?)
- OR: Different "places" (first place vs. second place?)

**Algorithm handling**: Use standard rule (First Mention → Routine on continuation)

---

### Edge Case 4: Interrogative Transition

**Pattern**: Participant = Interrogative in question, then Routine afterward

**Algorithm handling**:
1. Within question clause → Interrogative
2. After question resolved → Routine (or other applicable state)

---

## Hierarchical Decision Tree

```
START: Analyze participant referent

├─ Is participant in question context?
│  └─ YES → Rule 1: INTERROGATIVE
│     └─ Return: Interrogative (Q)
│
├─ Is participant universal/generic?
│  ├─ Universal quantifier (whosoever, all, any)? → GENERIC
│  ├─ Negative existential (no one, none)? → GENERIC
│  ├─ Abstract concept (life, wisdom)? → GENERIC
│  ├─ Vocative/role title (Teacher, Master)? → GENERIC
│  └─ If YES to any → Return: Generic (G)
│
├─ Is participant inferable from frame?
│  ├─ Relational inference (son from God)? → FRAME INFERABLE
│  ├─ Scene-expected (innkeeper at inn)? → FRAME INFERABLE
│  ├─ Definite on first mention + frame? → FRAME INFERABLE
│  └─ If YES to any → Return: Frame Inferable (F)
│
└─ Is participant new or established?
   ├─ Indefinite article ("a X")? → FIRST MENTION
   ├─ Proper name (first occurrence)? → FIRST MENTION
   ├─ Novel participant (not mentioned/inferable)? → FIRST MENTION
   │  └─ If YES to any → Return: First Mention (I)
   │
   └─ Otherwise (established, repeated, pronoun) → ROUTINE
      └─ Return: Routine (D)
```

---

## Surface Form Summary Table

| State | Primary Surface Forms | Secondary Indicators |
|-------|----------------------|----------------------|
| **Routine (D)** | Proper nouns, definite NPs, pronouns | Zero anaphora, repeated mentions |
| **Generic (G)** | Bare nouns, quantifiers (all/any/no) | Abstract nouns, vocatives, conditional |
| **Frame Inferable (F)** | Definite on first mention, relational nouns | Frame-specific vocabulary |
| **First Mention (I)** | Indefinite article (a/an), proper names (1st) | Demonstratives (this X - new) |
| **Interrogative (Q)** | Interrogative pronouns (who/what/which) | Question clause context |

**WARNING**: Surface form is NOT sufficient alone - context determines final state!

---

## Cross-Linguistic Validation (Future)

**Method**: Compare TBTA annotations with translation patterns in languages with explicit participant tracking

**Candidate languages**:
- Koine Greek: Article usage patterns (definite/indefinite)
- Hebrew: Waw-consecutive vs. independent clauses (tracking continuity)
- Modern tracking languages: Some Papuan languages mark new/given explicitly

**Goal**: Validate TBTA tracking states match linguistic theory across languages

---

## Rare States (Not in Current Training)

### Restaging (R) - Returning after absence

**Expected pattern**:
- Participant mentioned earlier
- Drops out of narrative focus (absence)
- Returns explicitly ("X came back", "X returned")
- Marked as Restaging on return

**Search strategy (Phase 5)**:
- Long narratives with scene changes
- Characters who leave and return (Genesis, Samuel, Kings)

---

### Integration (i) - Peripheral to central

**Expected pattern**:
- Participant mentioned as background/minor
- Suddenly becomes central/focal
- Shift from offstage → onstage

**Search strategy (Phase 5)**:
- Minor characters taking central role (Judas in betrayal)
- Background figures suddenly acting (centurion at crucifixion)

---

### Exiting (E) - Departing narrative

**Expected pattern**:
- Participant explicitly leaves ("he departed", "went away")
- Marked linguistically as departure
- May not return

**Search strategy (Phase 5)**:
- Explicit departure statements
- Characters leaving scene

---

### Offstage (O) - Background modifiers

**Expected pattern**:
- Ethnic/locational attributes ("the Canaanite", "of Nazareth")
- Background only, not active participants
- Extremely rare (<0.001%)

**Search strategy**:
- May not be worth targeting
- If found, document as edge case

---

## Algorithm Development Checklist (Phase 4)

- [ ] Implement Rule 1 (Interrogative detection)
  - [ ] Question clause identification
  - [ ] Interrogative pronoun matching
  - [ ] Transition logic (Interrogative → Routine)

- [ ] Implement Rule 2 (Generic detection)
  - [ ] Universal quantifier list (whosoever, all, any, every)
  - [ ] Negative existential list (no one, none, nothing)
  - [ ] Abstract noun identification
  - [ ] Vocative/role title list (Teacher, Master, Lord)

- [ ] Implement Rule 3 (Frame Inferable detection)
  - [ ] Frame vocabulary (creation, inn, household, trial, travel, meal)
  - [ ] Relational noun list (son, father, wife, husband, servant, master)
  - [ ] Definite-on-first-mention detection + frame check

- [ ] Implement Rule 4 (First Mention vs. Routine)
  - [ ] Indefinite article detection ("a", "an")
  - [ ] Proper name first occurrence tracking
  - [ ] Mention counting per participant
  - [ ] Pronoun resolution (pronoun → Routine)

- [ ] Special cases
  - [ ] God presupposition rule
  - [ ] Definite article disambiguation logic
  - [ ] Interrogative transition handling

- [ ] Validation
  - [ ] Test on 4 training verses (JHN 3:16, MRK 1:35, GEN 1:1, MAT 22:36)
  - [ ] Calculate training accuracy (target: 90%+)
  - [ ] Document any unresolved cases

- [ ] Git-lock Algorithm v1.0
  - [ ] Commit locked version
  - [ ] Add commit SHA to algorithm document
  - [ ] Proceed to Phase 5 (test set design)

---

**Created**: 2025-11-11
**Status**: Pattern extraction complete, ready for Algorithm v1.0 implementation
**Next Phase**: Phase 4 - Algorithm v1.0 development and git-locking
**Training accuracy target**: 90%+ on 4 TBTA-validated verses
