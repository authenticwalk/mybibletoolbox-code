# V3 Progressive Results (Unchurched Adults Source)

## Verse 1: Ruth 4:1

### Step 1: Download Unchurched Adults
text = "Boaz went to the town gate and sat down near it. Then that guardian-redeemer that Boaz talked about walked through the gate. So Boaz said to that man, "My friend, come here and sit down." So that man came to Boaz and sat down."

### Step 2: Fix Pronouns
Rules used: rules/pronouns.md - No 3rd person pronouns

Changes:
- "near it" → "near the gate" (resolve "it" to "the gate")

text = "Boaz went to the town gate and sat down near the gate. Then that guardian-redeemer that Boaz talked about walked through the gate. So Boaz said to that man, "My friend, come here and sit down." So that man came to Boaz and sat down."

### Step 3: Simplify Vocabulary
Rules used: rules/vocabulary.md - L2 pairings, hyphenated verbs never inflected

Changes:
- "guardian-redeemer" → "protector/guardian-redeemer" (L2 word needs pairing with simpler word)
- "sat down" → "sit-down" (3 occurrences - hyphenated verb, use base form)

text = "Boaz went to the town gate and sit-down near the gate. Then that protector/guardian-redeemer that Boaz talked about walked through the gate. So Boaz said to that man, "My friend, come here and sit-down." So that man came to Boaz and sit-down."

### Step 4: Group Participants
Changes:
- "that protector/guardian-redeemer that Boaz talked about" needs relative clause brackets

text = "Boaz went to the town gate and sit-down near the gate. Then that protector/guardian-redeemer [that Boaz talked about] walked through the gate. So Boaz said to that man, "My friend, come here and sit-down." So that man came to Boaz and sit-down."

### Step 5: Fix Clauses
Rules used: rules/clauses.md - One verb per clause; rules/quotes.md - Multi-sentence quotes bracket first sentence only; rules/special.md - Coordinate verbs very restricted

Changes:
- "went to the town gate and sit-down near the gate" → Split (coordinate verbs not allowed with destination arguments)
  - "Boaz went to the town gate. Boaz sit-down near the gate."
- Quote: "My friend, come here and sit-down" → Split into 2 sentences, bracket first only
  - Per quotes.md §17-20: `said, ["First sentence"]. Second sentence.`
  - "come here" has destination, can't coordinate with "sit-down"
  - `["My friend, come here"]. Sit-down.`
- "came to Boaz and sit-down" → Split (has destination)
  - "That man came to Boaz. That man sit-down."

text = "Boaz went to the town gate. Boaz sit-down near the gate. Then that protector/guardian-redeemer [that Boaz talked about] walked through the gate. So Boaz said to that man, ["My friend, come here"]. Sit-down. So that man came to Boaz. That man sit-down."

### Final He1
text = "Boaz went to the town gate. Boaz sit-down near the gate. Then that protector/guardian-redeemer [that Boaz talked about] walked through the gate. So Boaz said to that man, ["My friend, come here"]. Sit-down. So that man came to Boaz. That man sit-down."

---

## Verse 2: Ruth 4:5

### Step 1: Download Unchurched Adults
text = "Then Boaz said, 'On the day when you'll buy that land from Naomi, you have to also marry Ruth, who is from Moab. Ruth was Elimelech's son's wife. But Elimelech's son is dead. You'll protect the dead man's name and his property by marrying Ruth. <<When you and Ruth have children for Elimelech, his family will continue owning that land.>>'"

### Step 2: Fix Pronouns
Rules used: rules/pronouns.md - Mark 1st/2nd person pronouns with referents, resolve 3rd person pronouns

Changes:
- "you'll buy" → "you(protector/guardian-redeemer) will buy" (1st occurrence - need referent)
- "you have to" → keep as "you" (after 1st occurrence per He1 relaxation)
- "you'll protect" → keep as "you"
- "you and Ruth" → keep as "you"
- Note: After first `you(protector/guardian-redeemer)` the rest can be natural pronouns per He1 relaxation rule

text = "Then Boaz said, 'On the day when you(protector/guardian-redeemer) will buy that land from Naomi, you have to also marry Ruth, who is from Moab. Ruth was Elimelech's son's wife. But Elimelech's son is dead. You will protect the dead man's name and his property by marrying Ruth. <<When you and Ruth have children for Elimelech, his family will continue owning that land.>>'"

Wait, I need to check on "his" - is that 3rd person pronoun?
- "his property" - referring to "the dead man"
- "his family" - referring to "Elimelech"

These are possessive third person pronouns and need to be resolved.

Revised:
text = "Then Boaz said, 'On the day when you(protector/guardian-redeemer) will buy that land from Naomi, you have to also marry Ruth, who is from Moab. Ruth was Elimelech's son's wife. But Elimelech's son is dead. You will protect the dead man's name and the dead man's property by marrying Ruth. <<When you and Ruth have children for Elimelech, Elimelech's family will continue owning that land.>>'"

### Step 3: Simplify Vocabulary
Rules used: rules/vocabulary.md - L2 pairings, numbers as digits, simplify complex words

Changes:
- "protector/guardian-redeemer" → Already paired in previous verse
- "marry" → "marry" (checking if L2... likely L1, keep as is)
- "son's wife" → "son's wife" (already simplified from "daughter-in-law" in source)
- "property" → Checking if L2... may need "things/property" or "land/property"
- Actually, context shows "land" and "property" used separately, so "property" might mean possessions
- Let me use "things/property" for clarity
- "continue owning" → "continue" is L1, "owning" → "own" (simplify)
- Actually "continue owning" should become "continue [to own]" per clause structure

Changes applied:
- "property" → "things/property"
- "continue owning" → "continue [to own]"

text = "Then Boaz said, 'On the day when you(protector/guardian-redeemer) will buy that land from Naomi, you have to also marry Ruth, who is from Moab. Ruth was Elimelech's son's wife. But Elimelech's son is dead. You will protect the dead man's name and the dead man's things/property by marrying Ruth. <<When you and Ruth have children for Elimelech, Elimelech's family will continue [to own that land].>>'"

### Step 4: Group Participants
Changes:
- "Ruth, who is from Moab" → "Ruth [who is from Moab]" (relative clause)
- "the dead man's name" appears twice → consistency check OK
- "Elimelech's son's wife" → could be "Elimelech's son's wife" or create relative clause
  - Actually this is fine as possessive chain

text = "Then Boaz said, 'On the day when you(protector/guardian-redeemer) will buy that land from Naomi, you have to also marry Ruth [who is from Moab]. Ruth was Elimelech's son's wife. But Elimelech's son is dead. You will protect the dead man's name and the dead man's things/property by marrying Ruth. <<When you and Ruth have children for Elimelech, Elimelech's family will continue [to own that land].>>'"

### Step 5: Fix Clauses
Rules used: rules/clauses.md - Bracket subordinate clauses, max 4 nesting levels; rules/quotes.md - Bracket first sentence only; rules/special.md - Purpose clauses use "in order to"

Changes:
- This is a multi-sentence quote → bracket first sentence only
- "On the day when you will buy" → "when" is temporal adverbial clause, needs brackets
  - `[When you(protector/guardian-redeemer) will buy that land from Naomi]`
- "you have to also marry" → "have to" = obligation, should be "you must marry"
  - Actually "must" might not be in ontology, checking learnings... not found. Use "have to" as is.
- "by marrying Ruth" → This is a purpose/means clause
  - Should be "[by marrying Ruth]"? Or is this implicit purpose?
  - Actually "by" indicates means/method, not purpose
  - Keep structure but verify bracketing
- "When you and Ruth have children" → Temporal clause needs brackets
  - `[When you and Ruth have children for Elimelech]`
- The entire quote structure needs: `said, ["First sentence"]. Second...`

Let me structure this carefully:

Sentence 1: "On the day when you(protector/guardian-redeemer) will buy that land from Naomi, you have to also marry Ruth [who is from Moab]."
Sentence 2: "Ruth was Elimelech's son's wife."
Sentence 3: "But Elimelech's son is dead."
Sentence 4: "You will protect the dead man's name and the dead man's things/property by marrying Ruth."
Sentence 5: "<<When you and Ruth have children for Elimelech, Elimelech's family will continue [to own that land].>>"

Now fixing clauses within each:
- Sentence 1: `[When you(protector/guardian-redeemer) will buy that land from Naomi] you have to also marry Ruth [who is from Moab].`
  - Wait, "On the day when" → checking if this should be restructured
  - "On the day when X, Y" = temporal structure
  - Should be: `On the day [when you(protector/guardian-redeemer) will buy that land from Naomi] you have to also marry Ruth [who is from Moab].`
  - Actually simpler: `When you(protector/guardian-redeemer) buy that land from Naomi you have to also marry Ruth [who is from Moab].`
  - Let me check determiners - "On the day [when...]" - "the day" is being restricted by "when" clause
  - Per determiners.md: "No 'that' with restrictive clause" - should be "the day [when...]"
  - But per clauses.md: "No 'when' as relativizer" - use "that" instead
  - So: "On the day [that you(protector/guardian-redeemer) will buy that land at] you have to marry Ruth [who is from Moab]."
  - Hmm, this is getting complex. Let me simplify: just start with "When" as adverbial
  - `[When you(protector/guardian-redeemer) buy that land from Naomi]` - "when" is OK for adverbial clauses per clauses.md line 41

Actually, I need to reconsider. The original uses future "you'll buy". Hebrew likely has a temporal structure. The sense is:
"When you buy the land from Naomi, you must also marry Ruth."

So: `[When you(protector/guardian-redeemer) buy that land from Naomi] you have to also marry Ruth [who is from Moab].`

Continuing with Sentence 4:
- "You will protect the dead man's name and the dead man's things/property by marrying Ruth"
- "by marrying Ruth" → means/manner clause, should be bracketed?
- Actually, checking clauses.md... "by doing X" is typically an adverbial modifier
- Could be: "You will protect the dead man's name and the dead man's things/property [by marrying Ruth]."
- But is "protect X by doing Y" a single predicate pattern? Or two clauses?
- Safer to keep it: "You will protect the dead man's name and the dead man's things/property [by marrying Ruth]."
- But wait - "protect name and property" has two objects. Is that OK?
- This might need splitting: "You will protect the dead man's name [by marrying Ruth]. You will protect the dead man's things/property."
- Actually, checking if "X and Y" objects are allowed... likely yes for simple coordination
- Keep as is with bracketed means clause

Final Sentence 5:
- `<<[When you and Ruth have children for Elimelech] Elimelech's family will continue [to own that land]>>`
- Wait, the whole sentence is in `<< >>` (regular implicit). So the structure is:
  - `<<[When...] sentence>>`

Checking implicit.md: "Sentence implicit: marker at front"

So the structure should be:
`(implicit-situational) [When you and Ruth have children for Elimelech] Elimelech's family will continue [to own that land].`

But in He1 notation (from implicit.md examples): `<<When you and Ruth have children for Elimelech, Elimelech's family will continue [to own that land].>>`

The `<< >>` wraps the whole sentence.

Now, checking the quote structure - multi-sentence quote, bracket first only:

text = "Then Boaz said, ['[When you(protector/guardian-redeemer) buy that land from Naomi] you have to also marry Ruth [who is from Moab]']. Ruth was Elimelech's son's wife. But Elimelech's son is dead. You will protect the dead man's name and the dead man's things/property [by marrying Ruth]. <<[When you and Ruth have children for Elimelech] Elimelech's family will continue [to own that land].>>"

Hmm wait, I'm using single quotes inside the structure. Let me fix that:

text = "Then Boaz said, ["[When you(protector/guardian-redeemer) buy that land from Naomi] you have to also marry Ruth [who is from Moab]"]. Ruth was Elimelech's son's wife. But Elimelech's son is dead. You will protect the dead man's name and the dead man's things/property [by marrying Ruth]. <<[When you and Ruth have children for Elimelech] Elimelech's family will continue [to own that land].>>"

Actually I realize I need to reconsider "have children for Elimelech" - what does "for" mean here?
- Levirate marriage context: the children are legally considered Elimelech's descendants
- "for" might mean "on behalf of" or "to be considered as belonging to"
- This might need restructuring for clarity
- Possible: "have children [who will be Elimelech's descendants]"
- Or: "have children [to be Elimelech's family]"
- Let me check if "for" is a valid preposition in this context... it's implicit/cultural information
- I'll keep it as "for Elimelech" since it's already in implicit markers

Also checking: "have to also marry" - word order
- "also" placement: "you have to also marry" vs "you also have to marry"
- Better: "you also have to marry Ruth" (also modifies the whole verb phrase)

Revised:

text = "Then Boaz said, ["[When you(protector/guardian-redeemer) buy that land from Naomi] you also have to marry Ruth [who is from Moab]"]. Ruth was Elimelech's son's wife. But Elimelech's son is dead. You will protect the dead man's name and the dead man's things/property [by marrying Ruth]. <<[When you and Ruth have children for Elimelech] Elimelech's family will continue [to own that land].>>"

### Final He1
text = "Then Boaz said, ["[When you(protector/guardian-redeemer) buy that land from Naomi] you also have to marry Ruth [who is from Moab]"]. Ruth was Elimelech's son's wife. But Elimelech's son is dead. You will protect the dead man's name and the dead man's things/property [by marrying Ruth]. <<[When you and Ruth have children for Elimelech] Elimelech's family will continue [to own that land].>>"

---

## Verse 3: Ruth 4:13

### Step 1: Download Unchurched Adults
text = "So Boaz married Ruth. When Boaz slept with Ruth, the LORD caused her to become pregnant. Then Ruth gave birth to a son."

### Step 2: Fix Pronouns
Rules used: rules/pronouns.md - No 3rd person pronouns

Changes:
- "her" → "Ruth" (3rd person pronoun, resolve to noun)

text = "So Boaz married Ruth. When Boaz slept with Ruth, the LORD caused Ruth to become pregnant. Then Ruth gave birth to a son."

### Step 3: Simplify Vocabulary
Rules used: rules/vocabulary.md - L2 pairings, check complex words; learnings.md - "give birth" → "birth" as verb

Changes:
- "married" → checking if L2... likely L1, keep as is
- "slept with" → This is euphemism for sexual relations; check if needs simplification
  - "slept" alone means sleep; "slept with" is idiom
  - Consider: "had sex with" (more direct) or keep cultural euphemism?
  - For clarity and directness: "had sex with"
- "LORD" → "Yahweh" (per TBTA conventions for divine name)
- "caused Ruth to become pregnant" → simplify
  - "caused X to become Y" structure
  - Could be: "caused [Ruth to become pregnant]"
  - Or: "made Ruth pregnant"
- "gave birth to" → "birth" (per learnings.md: use "birth" as verb instead of "give birth")

text = "So Boaz married Ruth. When Boaz had sex with Ruth, Yahweh caused [Ruth to become pregnant]. Then Ruth birth a son."

Wait, "birth a son" doesn't sound right grammatically. Let me check learnings.md again...
- Line 39: "Use `birth` as verb instead of `give birth` (not in ontology)"

So it's "Ruth birth a son" - using "birth" as a verb in base form. This is correct per the hyphenated verb pattern (use base form).

But "birth" isn't hyphenated. So should it be conjugated? "Ruth birthed a son"?
Actually, the rule says "birth" is the verb form to use (not "give birth"). So in past tense: "Ruth birth a son" with base form, or "Ruth birthed a son"?

Checking vocabulary.md for non-hyphenated verbs... the rule about non-inflection is specific to hyphenated verbs.

So for regular verbs like "birth", I should use past tense: "birthed".

Revised:
text = "So Boaz married Ruth. When Boaz had sex with Ruth, Yahweh caused [Ruth to become pregnant]. Then Ruth birthed a son."

Actually, let me reconsider "caused [Ruth to become pregnant]" structure.
- "caused Ruth to become pregnant" - is this a patient clause?
- "cause" takes a patient clause describing what was caused
- So: "Yahweh caused [Ruth to become pregnant]" ✓

But checking if "become pregnant" needs simplification:
- "become" = change of state verb (L1)
- "pregnant" = L2? Checking... likely L2, may need "pregnant/with-child" or similar
- Or could explain: "Yahweh caused [Ruth to have a baby in Ruth]" or "Yahweh caused [a baby to begin in Ruth]"
- Actually, simpler: "Yahweh made Ruth pregnant"

Let me revise:

text = "So Boaz married Ruth. When Boaz had sex with Ruth, Yahweh made Ruth pregnant. Then Ruth birthed a son."

### Step 4: Group Participants
Changes:
- No repeated noun phrases to collapse
- Participants clearly identified throughout

text = "So Boaz married Ruth. When Boaz had sex with Ruth, Yahweh made Ruth pregnant. Then Ruth birthed a son."

### Step 5: Fix Clauses
Rules used: rules/clauses.md - Bracket subordinate clauses; One verb per clause

Changes:
- "When Boaz had sex with Ruth" → temporal adverbial clause, needs brackets
  - `[When Boaz had sex with Ruth] Yahweh made Ruth pregnant.`
- Check "made Ruth pregnant" - is "made" + adjective a single predicate or two clauses?
  - "make X Y" is a causative construction, typically one clause
  - Keep as: "Yahweh made Ruth pregnant"
- Sentence structure looks good, no other changes needed

text = "So Boaz married Ruth. [When Boaz had sex with Ruth] Yahweh made Ruth pregnant. Then Ruth birthed a son."

### Final He1
text = "So Boaz married Ruth. [When Boaz had sex with Ruth] Yahweh made Ruth pregnant. Then Ruth birthed a son."

---

## COMPARISON

### Ruth 4:1

**My Encoding:**
"Boaz went to the town gate. Boaz sit-down near the gate. Then that protector/guardian-redeemer [that Boaz talked about] walked through the gate. So Boaz said to that man, ["My friend, come here"]. Sit-down. So that man came to Boaz. That man sit-down."

**Reference Encoding:**
"Boaz marries Ruth. Boaz went to the town gate. And Boaz sat down near that gate. Then the man/kinsman-redeemer [that Boaz talked about] walked through the gate. So Boaz said to that man, 'My friend, you come to this place. And you sit down.' So that man came to Boaz. And that man sat down."

**Differences:**
1. **Missing section title**: Reference has "(title) Boaz marries Ruth." - I missed this completely
2. **Verb form "sit-down" vs "sat down"**: I used base form "sit-down" (hyphenated), reference uses "sat down" (two words, conjugated)
   - This suggests "sit down" is NOT treated as a hyphenated verb in the ontology
3. **Connective "And"**: Reference uses "And" to connect some sentences, I omitted it
4. **Determiner "that gate" vs "the gate"**: Reference uses "that gate" (already mentioned), I used "the gate"
5. **Term "man/kinsman-redeemer" vs "protector/guardian-redeemer"**: Different L2 pairing choice
   - Reference pairs "man" with "kinsman-redeemer"
   - I paired "protector" with "guardian-redeemer"
6. **Quote structure - imperative form**:
   - Reference: "you come to this place. And you sit down." (explicit pronoun, two sentences with "And")
   - Mine: ["My friend, come here"]. Sit-down. (implicit pronoun in imperative, no "And")
7. **"this place" vs "here"**: Reference uses "this place", I used "here"
   - "here" might not be in ontology as standalone; needs to be "this place"

**Key Learnings:**
- "sit down" is TWO words and conjugated normally (not hyphenated)
- Section titles should be included when present in NIV
- "And" connectives are kept in many places
- "here" → "this place"
- Imperatives shown with explicit "you" pronoun: "you(X) come" not just "come"

---

### Ruth 4:5

**My Encoding:**
"Then Boaz said, ["[When you(protector/guardian-redeemer) buy that land from Naomi] you also have to marry Ruth [who is from Moab]"]. Ruth was Elimelech's son's wife. But Elimelech's son is dead. You will protect the dead man's name and the dead man's things/property [by marrying Ruth]. <<[When you and Ruth have children for Elimelech] Elimelech's family will continue [to own that land].>>"

**Reference Encoding:**
"Then Boaz said, 'On the day that you(man) buy the land from Naomi on you(man) must also marry Ruth [who is from Moab]. Ruth was Elimelech's son's wife. But Elimelech's son is dead. You(man) will protect the dead man's name and the dead man's property [by marrying Ruth]. [When you(man) and Ruth have children for Elimelech] (implicit-info) Elimelech's family will continue owning that land.'"

**Differences:**
1. **Quote brackets**: I used ["..."] for first sentence, reference uses single quotes throughout (no brackets visible in fetched text)
   - This might be a display issue vs actual encoding
2. **Temporal clause structure**:
   - Mine: "[When you(protector/guardian-redeemer) buy that land from Naomi]"
   - Reference: "On the day that you(man) buy the land from Naomi on"
   - Reference keeps "On the day that... on" structure (note "on" appears twice - might be error in fetch)
3. **Referent in pronoun**:
   - Mine: "you(protector/guardian-redeemer)" (descriptive)
   - Reference: "you(man)" (simpler, shorter)
4. **"have to" vs "must"**: I kept "have to", reference uses "must"
5. **"things/property" vs "property"**: I added L2 pairing, reference keeps just "property"
   - Property may be L0-1, doesn't need pairing
6. **Implicit notation**:
   - Mine: `<<[When...]...>>`  (He1 style with angle brackets around whole sentence)
   - Reference: `[When...]` followed by `(implicit-info)` marker
   - Reference uses Phase 2 notation for clause implicit, not He1 notation
7. **"continue [to own]" vs "continue owning"**:
   - Mine: "continue [to own that land]" (bracketed infinitive)
   - Reference: "continue owning that land" (no bracket, gerund form)
   - This suggests "continue" + gerund is acceptable as single clause

**Key Learnings:**
- Simpler referents preferred: "you(man)" not "you(protector/guardian-redeemer)"
- "property" doesn't need L2 pairing
- "have to" → "must"
- "continue owning" is OK (continue + gerund acceptable pattern)
- Implicit clauses use `(implicit-info)` marker, not `<< >>`
- Keep temporal phrases like "On the day that... on" even if seeming redundant

---

### Ruth 4:13

**My Encoding:**
"So Boaz married Ruth. [When Boaz had sex with Ruth] Yahweh made Ruth pregnant. Then Ruth birthed a son."

**Reference Encoding:**
"So Boaz married Ruth. [When Boaz sexed Ruth] Yahweh caused [Ruth to become pregnant]. Then Ruth gave birth to a son."

**Differences:**
1. **"had sex with" vs "sexed"**:
   - Mine: "had sex with" (multi-word phrase)
   - Reference: "sexed" (single verb)
   - "sex" can be used as a verb directly (more concise)
2. **"made Ruth pregnant" vs "caused [Ruth to become pregnant]"**:
   - Mine: "made Ruth pregnant" (causative + adjective)
   - Reference: "caused [Ruth to become pregnant]" (caused + patient clause)
   - The reference structure is more explicit about the clause boundary
3. **"birthed" vs "gave birth to"**:
   - Mine: "birthed" (single verb form)
   - Reference: "gave birth to" (multi-word phrase)
   - Contrary to learnings.md which says use "birth" as verb, the reference uses "gave birth to"
   - This suggests learnings.md may be outdated or "gave birth to" is actually in ontology

**Key Learnings:**
- "sex" can be used as a verb: "sexed"
- "cause [X to Y]" with bracketed patient clause preferred over "made X Y"
- "gave birth to" is the correct form (not "birth" or "birthed")
- Learnings.md entry about "birth" as verb appears incorrect or outdated

---

## OBSERVATIONS

### V3 Progressive Disclosure Approach - Did Linking to Rule Files Help or Hurt?

**Helped:**
1. **Modular learning**: Each rule file focuses on one category (pronouns, vocabulary, clauses), making it easier to understand individual concepts
2. **Quick reference**: The skill file's quick reference table and rules summary helped identify which file to consult
3. **Detailed examples**: Rule files provided clear examples and common mistakes tables
4. **Reduced cognitive load**: Instead of one massive checklist, rules are grouped logically

**Hurt:**
1. **Information scatter**: Had to jump between multiple files to understand full context
2. **Missing integration**: Some rules interact (e.g., imperatives in quotes, temporal clauses with determiners) but this isn't always clear when files are separate
3. **Incomplete learnings.md integration**: I followed learnings.md which had some outdated rules (e.g., "birth" as verb)
4. **Duplicated effort**: Had to mentally synthesize rules across files (e.g., quote structure + imperative form + pronoun marking)

**Key Issues Encountered:**
1. **Hyphenated verbs confusion**: Spent significant time determining if "sit down" is hyphenated (it's not)
2. **Implicit notation**: Rules showed He1 `<< >>` notation, but reference uses Phase 2 `(implicit-info)` - version mismatch?
3. **Continue + gerund**: Rules emphasized "one verb per clause" but "continue owning" is acceptable
4. **Section titles**: Not mentioned in rules I read, so I missed them
5. **Referent simplicity**: Rules didn't emphasize keeping pronoun referents short and simple

**Recommendations:**
1. Add **integration examples** showing how multiple rules interact
2. Include **worked examples** inline in SKILL.md (not just linked)
3. Update **learnings.md** to match current reference encodings
4. Add **vocabulary lookup** guidance (how to check if word is L0-1-2-3-4)
5. Clarify **He1 vs Phase 1 vs Phase 2** notation differences
6. Add **section title** rule to a relevant file
7. Create **common patterns** file showing accepted multi-word structures (e.g., "gave birth to", "continue owning")

**Overall**: Progressive disclosure is helpful for learning/reference, but needs better cross-linking and up-to-date learnings. The scatter of information made encoding slower initially, though having focused rules helped with specific questions once I knew where to look.

---

## SUMMARY

### Final He1 Encodings

**Ruth 4:1 (My Result):**
```
Boaz went to the town gate. Boaz sit-down near the gate. Then that protector/guardian-redeemer [that Boaz talked about] walked through the gate. So Boaz said to that man, ["My friend, come here"]. Sit-down. So that man came to Boaz. That man sit-down.
```

**Ruth 4:5 (My Result):**
```
Then Boaz said, ["[When you(protector/guardian-redeemer) buy that land from Naomi] you also have to marry Ruth [who is from Moab]"]. Ruth was Elimelech's son's wife. But Elimelech's son is dead. You will protect the dead man's name and the dead man's things/property [by marrying Ruth]. <<[When you and Ruth have children for Elimelech] Elimelech's family will continue [to own that land].>>
```

**Ruth 4:13 (My Result):**
```
So Boaz married Ruth. [When Boaz had sex with Ruth] Yahweh made Ruth pregnant. Then Ruth birthed a son.
```

### Key Differences from Reference

**Major Issues:**
1. Missing section title "(title) Boaz marries Ruth"
2. "sit-down" (hyphenated) should be "sat down" (two words, conjugated)
3. Imperatives need explicit pronouns: "you come" not just "come"
4. "here" should be "this place"
5. Pronoun referents should be simple: "you(man)" not "you(protector/guardian-redeemer)"
6. "had sex with" → "sexed" (verb form)
7. "made Ruth pregnant" → "caused [Ruth to become pregnant]" (patient clause)
8. "birthed" → "gave birth to"
9. Implicit notation: use `(implicit-info)` not `<< >>`
10. "continue [to own]" → "continue owning" (gerund acceptable)

**Minor Issues:**
- Some "And" connectives omitted
- "the gate" should be "that gate" (already mentioned)
- "man/kinsman-redeemer" vs "protector/guardian-redeemer" (pairing choice)
- "things/property" vs "property" (unnecessary L2 pairing)
- "have to" vs "must"

### V3 Progressive Approach Assessment

**Accuracy: ~70%** - Got structure mostly right but missed several important patterns and vocabulary choices

**Efficiency: Medium** - Multiple file lookups slowed initial work but provided good reference once located

**Learning Value: High** - Detailed rules with examples helped understand WHY each choice matters

**Recommended for:** Users learning TBTA who want detailed explanations and can tolerate information scatter across files. Not recommended for speed encoding without prior experience.

