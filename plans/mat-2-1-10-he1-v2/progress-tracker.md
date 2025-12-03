# Matthew 2:1-10 He1 Encoding Progress

## Status Summary

| Verse | Status | Iterations | Notes |
|-------|--------|------------|-------|
| 1 | ✅ PASS | 2 | Changed to "wise men", "area" not "region" |
| 2 | ⏳ TESTING | - | Need to test |
| 3 | ✅ PASS | 4 | "Herod the king", "afraid", "all of" |
| 4 | ✅ PASS | 5 | "leaders" not "teachers", bracketed indirect Q, "the place [that...in]" |
| 5 | ⏳ TESTING | - | Need to test |
| 6 | ⏳ TESTING | - | Need to test |
| 7 | ✅ PASS | 3 | "learned...from", "the time [that...]" |
| 8 | ⏳ TESTING | - | Need to test |
| 9 | ⏳ TESTING | - | Need to test |
| 10 | ✅ PASS | 1 | Simple sentence, passed first try |

## Current Pass Rate: 4/10 (40%)

## Final Versions (Passing)

### Verse 1
[After Jesus was born in a town named Bethlehem [which was in an area named Judea]] [while the king named Herod ruled people of Judea], wise men from an eastern area came to a city named Jerusalem.

### Verse 3
[When Herod the king heard those words], Herod the king was afraid. And all of the people in the city were also afraid.

### Verse 4
[When Herod the king called all of the people's important priests and leaders of the law], Herod the king asked the men about the place [that the Messiah was to be born in].

### Verse 7
Then Herod called the wise men secretly. And Herod learned the time [that the star appeared] from the wise men.

### Verse 10
[When the wise men saw the star], the wise men were very happy.

## Next to Test

- Verse 2 (complex quote with nested questions)
- Verse 5 (reply with quote and nested prophecy)
- Verse 6 (quoted prophecy with personification)
- Verse 8 (commands with purpose clauses)
- Verse 9 (nested relative clauses)

## Key Learnings

1. **"King" not recognized**: Use "the king" not "King X" or "X the king"
2. **"where" not allowed**: Use "the place [that...]"
3. **"when" not allowed as relativizer**: Use "the time [that...]"
4. **"all of"**: Required before definite nouns
5. **Indirect questions**: Must be bracketed but use "the place/time [that...]" patterns
6. **L2+ words**: "region", "teachers", "troubled", "disturbed" all failed
7. **Phrasal verbs**: "found out" → "learned"
8. **"together"**: Not recognized, omit
9. **Verb case frames**: Objects must be in correct position for parser
