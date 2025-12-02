# Step-by-Step Process: NIV to Tabitha Target Format

**Purpose:** Convert NIV Bible text into Tabitha's intermediary format for translation to any language.

**Analysis Base:** Ruth 1:1-22 (complete chapter)

---

## Overview

This process transforms NIV text through systematic steps, applying rules in order of importance. Each step builds on the previous, ensuring consistency and accuracy.

---

## Process Steps

### Step 1: Get Source Text
- Fetch NIV text for the verse
- Reference Greek/Hebrew source for alignment
- Check other dynamic equivalent translations if needed

### Step 2: Add Title (if first verse of narrative section)
- **Rule R1**: Add title summarizing main event
- Format: "Title: [Summary]"
- Only for first verse of narrative sections

### Step 3: Resolve All Pronouns
- **Rule R9 (Critical)**: Resolve ALL third-person pronouns to nouns
  - "he/she/it/they" → proper nouns or descriptive phrases
  - "his/her/their" → possessive forms with explicit referents
- **Rule R28 (High)**: Mark first/second person referents in quotes
  - "I" → "I(Naomi)"
  - "you" → "you(daughters)"
  - "we" → "We(those women)"
- **Rule R10 (Medium)**: Resolve pronouns in lists
  - "a man... together with his" → "That man, his"

### Step 4: Split Compound Sentences
- **Rule R2 (High)**: Split compound sentences into separate sentences
  - "X, and Y" → "X. So Y" (or appropriate connector)
  - "X; Y" → "X. Y"
  - One event/action per sentence

### Step 5: Simplify Verbs and Voice
- **Rule R13 (High)**: Simplify verb phrases
  - "went to live" → "moved... to live"
  - "set out" → "started traveling"
  - Avoid compound verb phrases
- **Rule R14 (High)**: Convert passive to active
  - "was left with" → "lived with"
  - "was stirred" → "became excited"
- **Rule R23 (High)**: Simplify idioms
  - "come to the aid of" → "helped"
  - "show kindness" → "be kind to"
  - "deal with severely" → "punish severely"

### Step 6: Handle Clauses and Relationships
- **Rule R11 (High)**: Convert apposition to relative clauses
  - "X in Y" → "X, which was in Y"
  - "X, Y's Z" → "X, who was Y's Z"
  - "Ruth the Moabite" → "Ruth, [who was from Moab]"
- **Rule R12 (Medium)**: Convert adjectives to relative clauses
  - "Moabite women" → "women who were from Moab"
- Remove complementizer "that" in patient clauses
  - "knew that X" → "knew [X]"

### Step 7: Simplify Temporal and Connectors
- **Rule R3 (High)**: Simplify temporal phrases
  - "In the days when X" → "When X"
  - "Now" → "Later" (when indicating sequence)
- **Rule R4 (Medium)**: Restructure temporal clauses
  - "After they had lived" → "That family continued living"
- **Rule R5 (High)**: Select appropriate connectors
  - "And" → "But" (contrastive)
  - "and" → "or" (in negative contexts)
  - Choose based on semantic relationship

### Step 8: Handle Determiners and Reference
- **Rule R6 (High)**: Use referential determiners
  - "The man" → "That man" (after first mention)
- **Rule R7 (Medium)**: Character introduction
  - "a man" → "a certain man" (first mention)
- **Rule R8 (Low)**: Remove established numbers
  - "her two sons" → "her sons" (when "two" already mentioned)

### Step 9: Expand Geographic and Location References
- **Rule R17 (High)**: Use "named" construction
  - "country of X" → "country named X"
  - "town X" → "town named X"
- **Rule R15 (Medium)**: Geographic specificity
  - "the land" → "Israel" (when contextually clear)
- **Rule R16 (Medium)**: Geographic expansion
  - "from X, Y" → "living in a town named X, which was in Y"

### Step 10: Handle Special Constructions
- **Rule R31 (Medium)**: Expand contractions
  - "Don't" → "Do not"
  - "I'll" → "I will"
- **Rule R33 (Medium)**: Add implicit subjects
  - "Why call me" → "Why do you call me"
- **Rule R30 (Medium)**: Handle metaphors
  - Keep if understandable, expand if not
  - Reference: notation.md §143-149

### Step 11: Add Implicit Information (Audience-Dependent)
- **Rule R21 (Medium)**: Add implicit cultural/situational info
  - "<<Naomi's sons grew up and became men.>>" (for unchurched)
  - Mark with <<...>> or <...> notation
  - Reference: implicit.md

### Step 12: Final Cleanup
- **Rule R22 (Low)**: Remove redundant words
  - "both X and Y" → "X and Y"
- **Rule R19 (Medium)**: Decompose lists if needed
  - "X and Y were A and B" → "X was A. And Y was B."
- **Rule R18 (Medium)**: Expand ethnicity terms
  - "Ephrathites" → "in Ephrah's clan"

### Step 13: Add Quote Brackets
- Bracket first sentence of quotes only
- Format: `Speaker said, ["First sentence]. Second sentence."`
- Reference: quotes.md

### Step 14: Validate
- Check all pronouns resolved
- Verify sentence structure
- Ensure clarity for translation
- Compare with target format if available

---

## Rule Application Order Summary

1. **Critical**: R9 (Pronoun Resolution)
2. **High Priority** (in order):
   - R1: Title Addition
   - R9: Pronoun Resolution (all instances)
   - R28: First/Second Person Referents
   - R2: Sentence Splitting
   - R13: Verb Simplification
   - R14: Passive to Active
   - R23: Idiom Simplification
   - R11: Apposition to Relative Clause
   - R17: Named Construction
   - R3: Temporal Simplification
   - R5: Connector Selection
   - R6: Referential Determiner
3. **Medium Priority** (as needed):
   - R4, R7, R10, R12, R15, R16, R18, R19, R21, R30, R31, R33
4. **Low Priority** (sparingly):
   - R8, R20, R22

---

## Quick Reference Checklist

After applying the process, verify:

- [ ] All third-person pronouns resolved
- [ ] First/second person referents marked in quotes
- [ ] Compound sentences split
- [ ] Passive voice converted to active
- [ ] Idioms simplified
- [ ] Apposition converted to relative clauses
- [ ] Geographic references use "named" construction
- [ ] Temporal phrases simplified
- [ ] Appropriate connectors selected
- [ ] Contractions expanded
- [ ] Quote brackets added (first sentence only)
- [ ] Implicit information marked (if needed)

---

## Common Patterns

### Pattern 1: Character Introduction
```
NIV: "A man from Bethlehem..."
Step 1: "A certain man from Bethlehem..."
Step 2: "A certain man was from Bethlehem, which was in Judah."
```

### Pattern 2: Pronoun Resolution
```
NIV: "She said to them..."
Step 1: "Naomi said to those women..."
```

### Pattern 3: Sentence Splitting
```
NIV: "X, and Y."
Step 1: "X. So Y."
```

### Pattern 4: Passive to Active
```
NIV: "She was left with her sons."
Step 1: "Naomi lived with Naomi's sons."
```

### Pattern 5: Geographic Expansion
```
NIV: "from Bethlehem, Judah"
Step 1: "from a town named Bethlehem, which was in Judah"
```

---

## Notes

- **Think beyond Ruth**: These rules apply to all Bible books
- **Consolidate similar rules**: Rules that overlap should be merged
- **Reference existing policies**: Use compression technique - reference TBTA policies rather than explaining
- **Priority matters**: Apply critical and high-priority rules first
- **Context matters**: Some rules are audience-dependent (e.g., implicit information)

---

## File References

- **rules.md**: Complete rule set with details
- **synthesis.md**: Pros/cons evaluation
- **verse-analysis/**: Individual verse analyses
- **TBTA policies**: pronouns.md, clauses.md, determiners.md, implicit.md, notation.md, quotes.md

