# TBTA Translation Protocol: From Bible to Target English

This document defines the standard process and rules for converting biblical source text (Hebrew/Greek/English) into TBTA Target English (TE). The TE is an unambiguous, SVO-structured intermediary language designed for downstream translation into any global language.

## The Process

### Step 1: Participant & Setting Analysis

- Identify all entities (people, groups, nations).
- **Rule**: New participants must be introduced with "A certain [noun]" or "A [noun]".
- **Rule**: If a participant has a static attribute (origin, relationship), split it into a "state-of-being" sentence before the main action.
  - _Src_: "A man from Bethlehem went..."
  - _TE_: "A certain man was from Bethlehem. That man went..."
- **Rule**: Define all proper nouns with their class.
  - _TE_: "town named Bethlehem", "country named Moab", "region named Judah".

### Step 2: Syntax Simplification

- **Rule**: Enforce strict SVO (Subject-Verb-Object) word order.
- **Rule**: Break complex sentences. One event per sentence.
- **Rule**: Convert all Passive verbs to Active voice.
  - _Src_: "She was left with two sons."
  - _TE_: "She lived with her two sons."
- **Rule**: Deconstruct complex predicates (Instrumental, Causative).
  - _Src_: "He helped them by providing food."
  - _TE_: "He was taking care of them. He was giving food to them."

### Step 3: Explicitation of Implicit Information

- **Rule**: Explicate logical bridges. If an event B follows A but implies a gap, fill it.
  - _Example_: `<<They grew up>>` before marrying. `<<People saw them>>` before reacting.
- **Rule**: Explicate the logic of rhetorical questions or arguments using `<<...>>`.
  - _Src_: "Why come? I have no sons."
  - _TE_: "Why come? <<I can't take care of you.>> I won't have sons."
- **Rule**: Resolve all pronouns to specific names or "That [noun]" references.

### Step 4: Metaphor & Idiom Concrete-ization

- **Rule**: Convert metaphors to their functional/physical meaning.
  - "Hand turned against" -> "Treated badly".
  - "Full" -> "Had many good things".
  - "Empty" -> "Took things away".
- **Rule**: Deconstruct idioms/formulas.
  - **Oath**: "May God do X if Y" -> "I swear [Promise]. If I break it, [God should punish me]."

### Step 5: Unchurched Audience Check

- **Rule**: Add footnotes for cultural puns (e.g., Naomi/Mara).
- **Rule**: Ensure no "Christianese" remains (e.g., "Sojourn" -> "Live for a while").

---

## Master Rule List (Prioritized)

| Priority     | Category        | Rule                                              | Example                                                                   |
| :----------- | :-------------- | :------------------------------------------------ | :------------------------------------------------------------------------ |
| **CRITICAL** | **Syntax**      | **One Event Per Sentence (SVO)**. No embedding.   | "Elimelech, her husband, died" -> "Elimelech, who was her husband, died." |
| **CRITICAL** | **Semantics**   | **No Ambiguity**. Define all pronouns and places. | "They went" -> "Naomi and Ruth went". "Moab" -> "country named Moab".     |
| **HIGH**     | **State/Event** | **Separate State from Event**.                    | "A man from Bethlehem went" -> "A man was from Bethlehem. He went."       |
| **HIGH**     | **Logic**       | **Explicate Implied Logic**. Use `<<...>>`.       | "Why come?" -> "Why come? <<I can't help you.>>"                          |
| **HIGH**     | **Metaphor**    | **Concretize Metaphors**.                         | "I went away full" -> "I had many good things."                           |
| **MED**      | **Lists**       | **Distribute Lists**.                             | "Sons A and B" -> "One son A. Other son B."                               |
| **MED**      | **Culture**     | **Footnote Names/Terms**.                         | Naomi means 'Sweet'.                                                      |
| **MED**      | **Action**      | **Active Voice Only**.                            | "Was left" -> "Lived".                                                    |

## Special Cases

- **Gentilics**: Convert "Moabite" to "who was from Moab".
- **Time**: Convert "In the days of..." to "When...".
- **Psychology**: Use simple verbs. "Stirred" -> "Excited". "Determined" -> "Decided".
- **Urgency**: Convert negative urgency ("Don't urge me") to positive permission ("Allow me to go").
