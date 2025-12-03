# V3 Learnings (Blended)

Patterns learned from encoding with the blended policy + evidence approach.

## Process
Add learnings here when V3 wins or discovers a new pattern.

---

## Verb Case Frames
- `see` — needs specific Patient argument structure (Mt 2:2)
- `go` — needs directional/location argument format (Mt 2:8)
- `search` — "search for X" construction may be wrong (Mt 2:8)
- `say` — "say things to X" doesn't match ontology (Mt 2:2)
- `see-A` — explicit patient needed (Ac 10:3)
- `experience` — works for visions/dreams (Ac 10:3)
- `give-A` — handles "to" destination (Ac 10:4)
- `send-B` — for sending people to places (Ac 10:5)
- `near-A` — for proximity (Ac 10:6)

## Bracket Balance
- Linter reports "missing bracket" despite correct nesting — may be context-sensitive (Mt 2:5)

## Patterns That Worked Well
- Deixis: `I(Herod)`, `you(wisemen)`, `my(God's)` (Mt 2:3)
- Named entity: "a baby named Jesus" (Mt 2:1)
- Temporal brackets: `[After...]`, `[When...]` (Mt 2:1)
- Purpose: `[in order to...]` (Mt 2:8)
- Imperative: `(imp) verb` (Mt 2:8)
- Base verb forms: "give", "be", "go" — not "gave", "was", "went" (Mt 2:11)

## Nested Deixis Bug
- Pattern `["... your(Name) ..."]` inside nested brackets causes linter parsing errors (Ac 10:4)
- Workaround: Use third person ("God remember Cornelius" not "your prayers")

## "give" Case Frame Issue
- ERROR: "patient must immediately follow verb" (Tit 1:3)
- "give X to Y" fails → may need "give Y X" (ditransitive)
- Need clarification on give's theta grid

## Command/Order Constructions
- "command [to...]" → same-participant error (Tit 1:3)
- "order [AGENT to VERB]" → works (Tit 1:5)
- "told [that...]" → wrong case frame (Tit 1:3)

## Theological Vocabulary
- rescuer/savior (Tit 1:4)
- watches-over/oversees (Tit 1:7)
- set-apart/holy (Tit 1:8)
- select/appoint (Tit 1:5)

## Epistle Complexity
- Dense passages may need aggressive segmentation (Tit 1:1-3)

## Compound Deixis Not Supported
- `we(Paul-and-Timothy)` FAILS → use generic `we(people)` (Phm 1:1)
- Deixis prefers simple generic labels

## "give" Argument Order
- Patient must immediately follow verb (Phm 1:3)
- `give a gift/grace to you(people)` — patient first, then destination

## "thank" Cannot Take Temporal Clauses
- `thank God [when I remember you]` FAILS (Phm 1:4)
- Split into separate sentences

## "order" Requires Full Construction
- Even in negatives: `do not order [you(Philemon) to help me(Paul)]` (Phm 1:8)

## Possessive Structures (Narrative)
- For narrative family: "that man's wife/sons" is correct and clearer (Ru 1:1) ✓ V3 SUCCESS
- Clearer than restructured forms like "the wife of that man"

## Bracket Capitalization
- First word capitalized: `[When...]`, `[Because...]` (Phm 1:4)
- Bracketed temporal clauses: `[During the time [that...]]` — nested brackets work well (Ru 1:1) ✓ V3 SUCCESS

## Conjunction Spacing
- Multi-word conjunctions: "[in order to" not "[in-order-to" ✓ V3 SUCCESS (Ru 1:1)
- Linter accepts both but spaced is clearer and matches policy formatting

## Narrative Structure
- Use `(title)` marker at narrative section starts (Jon 1:1)
- Use "One day" opener for narrative beginnings (Jon 1:1)
- "decided [to verb]" for intent/purpose (Jon 1:3)

## Causative Constructions
- "caused [X to verb]" for divine actions on nature (Jon 1:4)

## Vocabulary Patterns
- "heavy things" not "cargo" for ship goods (Jon 1:5)
- "leader of the ship" not "captain" (Jon 1:6)
- "Perhaps" not "Maybe" for possibility (Jon 1:6)
- "men [who worked on that ship]" for sailors (Jon 1:5)

## Geographic Names
- Name seas explicitly: "Mediterranean Sea" (Jon 1:4)

## Implicit Markers (He1)
- Use `(implicit-info)` for implicit information (Jon 1:5)

## Famine/Scarcity Expression
- "there was a famine" → "many people [who were living in X] did not have enough food" (Ru 1:1)
- Use active subject with relative clause, not existential "there was"

## Determiner Patterns
- First mention of specific individual: "A certain man" (Ru 1:1) ✓ V3 SUCCESS
  - Blended approach correctly prioritizes policy "a certain man" over evidence variations
  - V1 produced "A man", V2 produced "one man" — V3's "a certain man" matches reference
- Subsequent reference: "That man" not "the man" (Ru 1:1)

## Title Clause Names
- Title clause may use character names from later verses (Ru 1:1)
- Pattern: `Name (title) and Name verb from Place to Place.` (Ru 1:1)

## Speech Introduction
- Add `(implicit-info) walked to X` before speech when motion implicit (Ru 2:8)

## Relative Clause Relativizers
- Use "that" for people in He1, not "who": "women [that work for...]" (Ru 2:8)

## State Changes
- "become thirsty" not "are thirsty" for state changes (Ru 2:9)

## Object Vocabulary
- "containers" not "jars" for water vessels (Ru 2:9)

## Indirect Commands
- "told [X to not verb Y]" structure for reported commands (Ru 2:9)

## Body Movement
- "moved X's face to the ground" for prostration (Ru 2:10)

## Location Descriptions
- "the land [that you were born in]" for "homeland" (Ru 2:11)

## Prayer Expressions
- "I(X) will pray [that Yahweh will verb...]" for blessings (Ru 2:12)

## Simile Structure
- "[just like X verbs Y]" then separate explanation sentence (Ru 2:12)

## Section Markers
- `_paragraph` at section starts (Ac 16:25)

## Dual Translations
- "(complex)/(simple)" for difficult concepts (Ac 16:26)

## Implicit Agents
- `_implicitActiveAgent` for passive agents (Ac 16:26)
- "opened by this event" - event as agent (Ac 16:26)

## Role Descriptions
- "the man [who was responsible for the prisoners]" for jailer (Ac 16:27)

## Causal Connectors
- "For" instead of "Because" at sentence start (Ac 16:27)

## Request Structure
- "asked-B [X to bring Y]" for requests (Ac 16:29)

## Posture Verbs
- "knelt in front of" not "fell before" (Ac 16:29)

## Movement Verbs
- "led...from that room" not "brought out" (Ac 16:30)

## Title/Honorific L2
- "Masters-B/lords" for "Sirs" (Ac 16:30)

## Interrogative
- "which things-B" not "what" (Ac 16:30)

## Modal Obligations
- "must die/pay" are modals NOT marked with (imp) (2Sa 12:5)

## Emotion Expressions
- "became very angry" for "burned with anger" (2Sa 12:5)

## Word Disambiguation
- "anything_noun", "living_verb" for ambiguous words (2Sa 12:1, 12:3)

## Transformative Actions
- "make X into Y" for preparing/cooking (2Sa 12:4)
