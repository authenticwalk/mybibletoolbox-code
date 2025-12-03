# Learnings (ARCHIVED)

> **DEPRECATED**: This shared file has been replaced by version-specific learnings:
> - `learnings-v1.md` — V1 (Policy-First) patterns
> - `learnings-v2.md` — V2 (Evidence-Based) patterns
> - `learnings-v3.md` — V3 (Blended) patterns
>
> This file is kept for historical reference. Do not add new patterns here.

---

This file contains the learnings in short policy form statements linking to the full document for longer explanation

## Process to add to this file
 - **First** write your detailed diagnositic of what went wrong in ./learnings/{slug}.md
   - What you started with (original text)
   - What you translated it as and why
   - What was the the correct language
   - What are all the possible reasons you got it wrong?
   - Of those what was the most likely cause(s)
   - What are the all the ways you could solve it?
   - Pros and cons of each
   - Attempt 3 of them and measure which succeeded
 - **Second** write the learning in learnings.md (this file) as a single line bullet form grouped under an appropriate headers
 - **Third** Audit your edits, if they are too similar to other rules combine them together citing some of them as examples

## Verb Structure
- Avoid "have" with adverbial clauses preceding it; use existential "be" instead ("there was not enough food") - see [ruth-1-1-have-structure.md](./learnings/ruth-1-1-have-structure.md)

## Numbers and Adjectives
- Use numerals (2, 3, 10) not words (two, three, ten) - number words are not recognized as adjectives in ontology

## Ambiguous Words
- Add `_noun`, `_verb`, `_adj` etc. to clarify ambiguous words like "judges" which could be noun or verb

## Patient Clauses
- Never use "that" at the start of patient clauses; use `[God gave food...]` not `[that God gave food...]`
- Quote structure: `said, ["First sentence"]. Second sentence continues..."` - bracket closes after first sentence only

## Complex Word Pairings (L2 words)
- `worship` → `serve/worship`
- `swear` → `promise/swear`
- `harvest` (verb) → `gather/harvest`
- `barley` → `grain/barley`
- `daughter-in-law` → `son's wife` (or explicate)

## Verb-Specific Issues
- Use `gave birth to` (NOT "birth" or "birthed" as standalone verb)
- Use `sexed` not "slept with" or "had sex with" (use direct verb form)
- Use `came to X` instead of `arrived at X` (arrived has case frame issues)
- Use `lived` instead of `living` (living not recognized)

## Clan/Family Membership
- Use "was in X's family/clan" for membership, not "was from" - see [ruth-2-1-man-of-standing.md](./learnings/ruth-2-1-man-of-standing.md)

## Name Introduction
- Prefer "a [noun] named [name]" over separate "X's name was [name]" sentence

## Complex Phrase Expansions
- "man of standing" → "People respected X much" + "(implicit-info) X was rich" - see [ruth-2-1-man-of-standing.md](./learnings/ruth-2-1-man-of-standing.md)

## Section Structure
- Include "(title)" for section headers matching NIV section breaks
- Use "One day" to mark beginning of scene (Begin Scene relation)

## Quote Structure
- Multi-sentence quotes: `["First sentence]. Second sentence continues..."` - bracket only around first sentence
- See [ruth-2-2-quote-structure.md](./learnings/ruth-2-2-quote-structure.md)

## Request Patterns
- "Let me go" → `You(X) (imp) let [me(Y) go to...]` - imperative to listener
- See [ruth-2-2-quote-structure.md](./learnings/ruth-2-2-quote-structure.md)

## Nationality Expression
- "X the Moabite" → `X [who was from Moab]` - use relative clause

## Idiom Simplification
- "find favor in eyes" → `be kind to me`
- "leftover grain" → `grain/barley [that people left]`
- "The Lord be with you" → `I pray [that Yahweh will be with you]`
- "The Lord bless you" → `I pray [that Yahweh will do good things for you]`
- "May the Lord..." prayers → `I pray [that Yahweh will...]`

## Hyphenated Verbs (from Ruth 2)
- Hyphenated verbs (pick-up, pull-out) don't inflect: `pick-up` not `picked-up`
- But "sit down", "stand up" are TWO WORDS and DO inflect: `sat down`, `stood up`
- Rule: if it's hyphenated in ontology → don't inflect; if two words → inflect normally

## Verb Patterns
- "give X to Y" - destination marker required: `gave the food to Naomi`
- "showed" often needs rewriting to `gave` with destination

## Additional L2 Word Pairings (from Ruth 2)
- `workers` → `servants/workers`
- `mother-in-law` → `husband's mother` (explicate)
- `daughter-in-law` → `son's wife` (explicate)
- `bow` → `kneel/bow`

## Nested Quotes
- Structure: `["outer quote ["inner quote"]"]`
- Example: `said, ["Boaz said, ["Stay with my workers"]"]`