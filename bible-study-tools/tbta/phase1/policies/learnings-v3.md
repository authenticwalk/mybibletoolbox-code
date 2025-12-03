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

## Bracket Capitalization
- First word capitalized: `[When...]`, `[Because...]` (Phm 1:4)
