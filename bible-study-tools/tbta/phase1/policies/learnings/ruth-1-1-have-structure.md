# Learning: "have" verb with complex subject structures

## Original Text (NIV)
"In the days when the judges ruled, there was a famine in the land."

## My Initial Translation
```
[When judges ruled Israel] many people [who lived in Israel] did not have enough food.
```

## Error Received
"'have' cannot be used with a different-participant patient clause. Consult the Verb's Theta Grid usage."

## Correct/Working Translation
```
[When judges _noun ruled Israel] there was not enough food in Israel.
```

## Analysis

### Possible causes:
1. The parser interprets adverbial clauses before "have" as creating a "different-participant patient clause" structure
2. The relative clause modifying the subject of "have" may create parsing ambiguity
3. "have" verb senses have strict theta grid requirements that don't allow certain subordinate structures

### Most likely cause:
The combination of an adverbial clause `[When judges ruled...]` immediately preceding a verb "have" with object "food" creates an invalid argument structure where the parser interprets the adverbial clause as a patient clause.

### Solutions tried:
1. **Remove relative clause from subject** - Still failed (same error)
2. **Use existential "be"** - SUCCESS: "there was not enough food in Israel"
3. **Add `_noun` to clarify "judges"** - Helped reduce ambiguity warnings

### Result
Using existential "be-E" construction instead of "have" with complex clause structures avoids the validation error.

## Additional learnings from Ruth 1:1:
- Numbers: Use numerals (2) not words (two) - "two" is not recognized as adjective in ontology
- Part-of-speech markers: Add `_noun`, `_verb` etc. to clarify ambiguous words like "judges"
