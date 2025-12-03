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

## Military/Role Vocabulary (Gen 18, 1Sa 17, Mt 8)
- "shield bearer" → "man [who carried a big cover for X]" (1Sa 17:41)
- "centurion" → "army leader [who was in charge of 100 soldiers]" or "officer/centurion" (Mt 8:5)
- "armor bearer" → "man [who carried the weapons of X]"
- "captain" → "leader of the ship" (Jon 1:6)

## Spatial Relativizer Forbidden
- "where" cannot be relativizer → use "the place [that...]" (Act 9:2)
- "when" for temporal → use "the time [that...]" when needed

## Proper Name Marker
- Use `_properName` for special terms: "the Way _properName" (Act 9:2)
- Helps distinguish religious/historical proper nouns

## Hospitality Vocabulary (Gen 18)
- "bowed low" → "put X's face to the ground" (Gen 18:2)
- "refreshed" → "will be strong again" or "will have strength" (Gen 18:5)
- "knead" → "mix flour with water" (Gen 18:6)
- "finest flour" → "best flour" (Gen 18:6)

## "want" Verb Senses
- `want-A` for different-participant: "wanted [Jesus to help]"
- `want-B` for same-participant: "wanted [to take those people]" (Act 9:2)
- Careful sense selection required

## "ask" Verb Complexity
- Has 6+ senses with different argument structures (Act 9:2)
- When problematic, restructure to "wanted X from Y" construction
- Avoid complex "asked X for Y to do Z" patterns

## Prophetic/Poetic Simplification (Nah 1)
- "jealous" → "wants [all people to honor only Yahweh]"
- "avenging/vengeance" → "punishes"
- "wrath" → "anger"
- "fierce anger" → "strong anger"
- "poured out like fire" → "flows-out like fire"
- "shattered" → "break"

## Prophetic Metaphors
- Use simile marker: "like the dust of Yahweh's feet" (Nah 1:3)
- Convert passives to causatives: "causes [the sea to become dry]" (Nah 1:4)
- Double negative → positive: "will not leave unpunished" → "will certainly punish" (Nah 1:3)

## Epistle Vocabulary (2Jn, Tit 2)
- "deceiver" → "person [who tricks people]" (2Jn 1:7)
- "antichrist" → "enemy of Christ" (2Jn 1:7)
- "sound doctrine" → "healthy words/teaching" (Tit 2:1)
- "temperate/self-controlled" → "control [the mind of X]" (Tit 2:2)
- "reverent" → "honor God" (Tit 2:3)
- "slanderers" → "say bad things about people" (Tit 2:3)

## Reflexive Pronoun Handling
- "themselves" not recognized → repeat noun (Tit 2:2)
- "control themselves" → "control those men/women"

## Long Quote Management
- Split multi-sentence quotes into separate `said` statements (Jos 2, Mt 8)
- Pattern: `X said, ["A."] X said, ["B."]` not `X said, ["A. B. C."]`
- Reduces linter bracket-matching errors

## Gospel Dialogue Patterns (Mt 8, Mk 10)
- "lying" needs sense: "lying-A" for physical position (Mt 8:6)
- "paralyzed" → "not able [to move]" (Mt 8:6)
- "Teacher" is L2 → "Master" or "person [who teaches]" (Mk 10:17)
- "eternal life" → "life [that will not end]" (Mk 10:17)

## Conversion Narrative (Act 9)
- "breathing out threats" → "wanted [to kill X]" + "speaking angry words"
- "persecute" → "harm" (Act 9:4)
- "get up" → "stand-up" (hyphenated, base form) (Act 9:6)

## Time Expression Patterns (Mt 14, Jon 3)
- "shortly before dawn" → "[During the time [before the sun would come-up in the morning]]" (Mt 14:25)
- "shortly" not in ontology → use temporal bracket constructions
- Hyphenated verbs with modals still use base form: "would come-up" not "would came-up" (Mt 14:25)

## Aspect Verb Confirmation
- "started sinking" → NO bracket (Policy §0.19 confirmed) (Mt 14:30)
- "began walking" → NO bracket after aspect verbs (Jon 3:4)
- Aspect verbs (start, stop, begin, finish, continue) modify the following verb directly

## Ontology Vocabulary Gaps (Mk 2, Act 2)
- "opening" → "hole" (not in ontology) (Mk 2:4)
- "mat" → "bed" (not in ontology) (Mk 2:4)
- "Holy" not recognized → "Spirit of God" not "Holy Spirit" (Act 2:4)
- "together" → "in the same place" (Act 2:1)
- "bewildered/confused" → "surprised" (Act 2:6)

## Disability/Ability Expressions (Mk 2)
- "paralyzed" → "not able [to move]" or "[who was not able [to walk]]" (Mk 2:3)
- "could not" → "were not able [to...]" (modal verb ban) (Mk 2:4)

## Religious Group Vocabulary (Act 2)
- "believers" → "people [who believed in Jesus]" (Act 2:1)
- "God-fearing Jews" → "Jews [who honored God]" (Act 2:5)

## Discourse Markers (Act 2)
- "Now" as discourse marker → "At this time" (Act 2:5)
- TBTA has temporal "now" but not discourse marker "now"

## Fasting/Mourning Vocabulary (Jon 3)
- "proclaimed a fast" → "decided [to not eat food]" or "told people [to not eat]" (Jon 3:5)
- "sackcloth" → "cloth/sackcloth" or "clothes [that were made from goat hair]" (Jon 3:5)
- "greatest to least" → "most important to least important" or "Powerful people and weak people" (Jon 3:5)

## Epistle Relationship Language (Phm 1)
- "loved brother" triggers passive detection → use "loving brother" instead (Phm 1:16)
- "separate" has complex arguments → "caused [to be away from]" (Phm 1:15)
- "as" comparisons unsupported → restructure with "like" or explicit "[X is Y]" statements (Phm 1:16)
- "if" conditionals → "Perhaps" for hypothetical meanings (Phm 1:18)
- "partner" → "friend/partner" (L2 pairing) (Phm 1:17)
- "welcome" → "accept/welcome" or "receive/welcome" (Phm 1:17)
- "refresh my heart" → "make my heart strong" or "cause [me to be happy]" (Phm 1:20)
- "charge it to me" → "add that debt to my account" or "blame me" (Phm 1:18)

## "write" Verb Requirement
- "write" always needs explicit patient object (Phm 1:19)
- "am writing this" → "am writing this letter" or "make these marks"

## "give" Verb Constraints (Phm 1)
- "give" + predicate adjective fails → use "cause [X to be happy]" (Phm 1:20)
- "give joy/happiness" → "cause [X to have joy]" or "make X happy"
