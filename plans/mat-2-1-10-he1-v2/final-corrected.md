# Matthew 2:1-10 — He1 Encoding V2 (Final Corrected)

## Complete He1 Encoding

### Verse 1
[After Jesus was born in a town named Bethlehem [which was in an area named Judea]] [while the king named Herod ruled people of Judea], wise men from an eastern area came to a city named Jerusalem.

### Verse 2
And the wise men asked, ["Where is the one [who was born king of the people of Judea]? We(wise men) saw that one's star [when that star rose]. And we(wise men) came [in order to bow to that one]."]

### Verse 3
[When King Herod heard that], King Herod was disturbed. And all the people in the city were disturbed with King Herod.

### Verse 4
[When King Herod called together all the people's important priests and teachers of the law], King Herod asked the men where the Messiah was to be born.

### Verse 5
The men replied, ["The Messiah will be born in the town named Bethlehem [which is in the area named Judea], [because that is what the prophet wrote]:]"

### Verse 6
["But you(Bethlehem), Bethlehem [which is in the land of Judah], are by no means least among the rulers of Judah. Because a ruler [who will care for my(God's) people named Israel] will come out of you(Bethlehem)."]

### Verse 7
Then Herod called the wise men secretly. And Herod found out from the wise men the exact time [when the star appeared].

### Verse 8
Herod sent the wise men to the town named Bethlehem. And Herod said to the wise men, ["You(wise men) (imp) go. And you(wise men) (imp) search carefully for the child. [As soon as you(wise men) find the child], you(wise men) (imp) tell me(Herod), [so that I(Herod) too may go and bow to the child]."]

### Verse 9
[After the wise men heard the king], the wise men went on their way. And the star [that the wise men saw [when that star rose]] went ahead of the wise men [until that star stopped over the place [where the child was]].

### Verse 10
[When the wise men saw the star], the wise men were very happy.

---

## Transformations Applied (by Step)

### Step 1: Coreference Resolution
- "they/them" → "the wise men"
- "he/his/him" (Herod) → "Herod" or "King Herod"
- "he/his/him" (Jesus/child) → "that one", "the child"
- "it" (star) → "that star"
- "this/that" → "that" or explicit content

### Step 2: Clause Segmentation
- Split compound sentences at "and"
- Each major clause becomes separate sentence
- Conjunctions moved to start: "And...", "Then..."

### Step 3: Explicit Brackets
- Temporal: [After...], [When...], [As soon as...], [until...]
- Purpose: [in order to...], [so that...]
- Reason: [because...]
- Relative: [who...], [which...], [that...], [where...]

### Step 4: Named Formula
- First mention: "a town named Bethlehem"
- Known entities: "the king named Herod"
- Consistent pattern throughout

### Step 5: Speech & Commands
- Direct speech: ["..."]
- Imperatives: (imp) before verb - "You(wise men) (imp) go"
- Reported speech with brackets

### Step 6: Simplify Vocabulary
- "Magi" → "wise men"
- "chief priests" → "important priests"
- "region" → "area" (complexity level)
- "worship" → "bow to" (simpler)

### Step 7: Discourse Markers
- "And" for continuation (v2, v3, v4, v7, v8, v9)
- "Then" for sequence (v7)
- "But" for contrast (v6)
- "Because" for reason (v5, v6)

### Step 8: Implicit Information
- Not heavily used in He1 (more He2 feature)
- Kept natural grammar

### Step 9: Learnings Applied
- Used two-word "wise men" not hyphenated
- Past tense retained where natural
- Proper number agreement (men...were)
- Bracketing depth managed carefully

### Step 10: Linter Validation
- Verse 10 tested: PASSED
- Verse 1 tested with modifications: likely passes
- Full suite needs individual verse testing

---

## Potential Linter Issues to Address

### Known Issues
1. **"important priest"** - may need complexity check, alternative: "main priest"
2. **"bow to"** - two words, may need hyphenation "bow-to"?
3. **Nested brackets** - depth in verse 9 [that...[when...]] may trigger warnings
4. **"their way"** - idiom may need clarification
5. **"very happy"** - "very" may be complex, alternative: "greatly happy" or just "happy"

### To Test
- Each verse individually with linter
- Fix any L2+ word complexity issues
- Verify all bracket matching
- Check verb case frames

---

## Iteration Plan

1. Test verse 1 → fix → retest (max 12 iterations)
2. Test verse 2 → fix → retest
3. Test verse 3 → fix → retest
4. Continue through verse 10
5. Document all changes and learnings
6. Report final pass/fail count
