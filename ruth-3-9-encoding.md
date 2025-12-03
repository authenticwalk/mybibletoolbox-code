# Ruth 3:9 TBTA Phase 1 Encoding Process

## Step 1: NIV Source Text

**Exact NIV text from BibleGateway:**
```
"Who are you?" he asked. "I am your servant Ruth," she said. "Spread the corner of your garment over me, since you are a guardian-redeemer of our family."
```

## Step 2: Starting Point Documentation

I am starting with the exact NIV text as shown above. This verse contains:
- Dialogue between two people (Boaz and Ruth, based on context)
- Three quoted speech segments
- Two speech tags ("he asked", "she said")
- The name "Ruth" is mentioned
- Key terms: "servant", "garment", "guardian-redeemer"

---

## Step 3: Fix Pronouns & Split Sentences

**Input:**
```
"Who are you?" he asked. "I am your servant Ruth," she said. "Spread the corner of your garment over me, since you are a guardian-redeemer of our family."
```

**Changes:**
1. Identify speakers: "he" = Boaz (from context), "she" = Ruth
2. Ruth's third speech is one long sentence with a dependent clause - check if splitting is needed
3. "your servant Ruth" - "your" refers to Boaz
4. "you are a guardian-redeemer" - "you" = Boaz
5. "our family" - "our" = Ruth's family (Ruth and Naomi)

At this stage, I'm primarily identifying pronoun referents. Splitting: Ruth's final speech could be split at the "since" clause, but it's a reason clause that explains the request, so keeping it together makes sense initially.

**Output (with pronoun analysis, not yet in brackets):**
```
"Who are you?" Boaz asked. "I am your servant Ruth," Ruth said. "Spread the corner of your garment over me, since you are a guardian-redeemer of our family."
```

Note: I replaced pronouns in speech tags with proper names for clarity.

---

## Step 4: Simplify Vocabulary

**Input:**
```
"Who are you?" Boaz asked. "I am your servant Ruth," Ruth said. "Spread the corner of your garment over me, since you are a guardian-redeemer of our family."
```

**Changes:**
1. "servant" → keep (ontology-friendly, clear role)
2. "corner of your garment" → consider if this needs simplification. "Corner" is specific; "garment" is clear.
3. "guardian-redeemer" → This is a compound concept. Consider "family-redeemer" or "kinsman-redeemer" but "guardian-redeemer" is already clear enough.
4. "spread...over" → keep (clear action)

Actually, reviewing this: the phrase "corner of your garment" is idiomatic. In Hebrew culture, this refers to the wing/edge of the garment and is symbolic. For ontology purposes, we might keep it literal as "edge of your robe" or similar, but "corner of your garment" is already fairly clear.

**Output:**
```
"Who are you?" Boaz asked. "I am your servant Ruth," Ruth said. "Spread the corner of your garment over me, since you are a guardian-redeemer of our family."
```

(Minimal changes at this stage - NIV is already quite clear)

---

## Step 5: Add TBTA Notation

**Input:**
```
"Who are you?" Boaz asked. "I am your servant Ruth," Ruth said. "Spread the corner of your garment over me, since you are a guardian-redeemer of our family."
```

**Changes:**
1. Add brackets for dialogue attribution
2. Add pronoun referents in parentheses
3. Specify possessive pronoun referents
4. Consider implicit subjects

**Applying TBTA notation:**
- "[Boaz] Who are you(sg)?" → Boaz asking
- "[Ruth] I am your(sg/Boaz) servant Ruth" → Ruth identifying herself
- "[Ruth] Spread the corner of your(sg/Boaz) garment over me(Ruth)" → Ruth making request
- "since you(sg/Boaz) are a guardian-redeemer of our(Ruth+Naomi) family" → Ruth explaining

**Output:**
```
[Boaz] "Who are you(sg)?" [Ruth] "I am your(sg/Boaz) servant Ruth." [Ruth] "Spread the corner of your(sg/Boaz) garment over me(Ruth), since you(sg/Boaz) are a guardian-redeemer of our(Ruth+Naomi) family."
```

---

## Step 6: Validation with Checker

### Iteration 1: Initial Check

**Input:**
```
[Boaz] "Who are you(sg)?" [Ruth] "I am your(sg/Boaz) servant Ruth." [Ruth] "Spread the corner of your(sg/Boaz) garment over me(Ruth), since you(sg/Boaz) are a guardian-redeemer of our(Ruth+Naomi) family."
```

**Checker Results:**
- ERROR: Unknown words not recognized (Who, Spread, garment need ontology entries)
- ERROR: Malformed pronoun notation - using wrong syntax
- ERROR: `our(Ruth+Naomi)` - should use `/` not `+`
- ERROR: `I` needs explicit referent `I(Ruth)`
- ERROR: "guardian-redeemer" not in ontology (suggests "kinsman-redeemer")
- ERROR: `since` subordinate clause needs proper bracketing

### Iteration 2: Apply Correct TBTA Notation

Based on the TBTA rules:
- Pronouns: `I(Ruth)`, `you(Boaz)` format
- Quotes: bracket first sentence only
- No need for (sg) markers
- Use inclusive/exclusive only for "we/us/our"
- Third person pronouns must be replaced with names
- Multi-sentence quotes: bracket only the first sentence

**Revised encoding:**
```
Boaz asked, ["Who are you(sg)?"] Ruth answered, ["I(Ruth) am your(Boaz's) servant Ruth."] Ruth said, ["You(Boaz) (imp) spread the corner of your(Boaz's) garment over me(Ruth) [because you(Boaz) are a kinsman-redeemer of our(Ruth) _incl family]"].
```

Wait - checking the rules again:
1. "Who are you?" - no referent needed for question words
2. Ruth's response is actually three sentences in the dialogue, but logically two speech acts
3. "since" indicates a reason clause - should be bracketed within the request
4. Need to check if "guardian-redeemer" or "kinsman-redeemer" is in ontology

### Iteration 3: Simplify and Fix Structure

Looking at the verse structure more carefully:
- NIV has three quoted speeches
- Speech tags: "he asked" / "she said" / (implicit continuation)
- Ruth's third statement is one sentence with "since" clause

Following TBTA rules more carefully:
- "he asked" → "Boaz asked"
- "she said" → "Ruth said/answered"
- First sentence of quote gets brackets
- "guardian-redeemer" → need to simplify/pair if L2 word
- "since you are" → reason clause in brackets

**Attempt 3:**
```
Boaz asked, ["Who are you?"] Ruth answered, ["I(Ruth) am your(Boaz's) servant Ruth."] Ruth said, ["You(Boaz) (imp) spread the corner of your(Boaz's) garment over me(Ruth) [because you(Boaz) are a family-redeemer/kinsman of our(Ruth) _incl family]"].
```

Actually, reviewing the examples again - I notice:
- Multi-sentence quotes bracket only FIRST sentence
- But these are THREE separate speech acts (question, answer, request)
- Each should be its own quote with brackets
- "since" = "because" (reason clause)
- "spread...over" might need simplification
- "guardian-redeemer" is likely a compound that needs handling

### Iteration 4: With Ontology-Verified Words

**Ontology checks:**
- "spread" ✅ Level 1 (sense B: transitive "spread something")
- "corner" ✅ Level 1 (corner of robe/building)
- "garment" ❌ NOT in ontology → need alternative
- "cloth" ✅ Level 1 (cloth-A = small piece, cloth-B = large piece for wrapping)
- "servant" ✅ Level 1
- "redeemer" ❌ NOT in ontology
- "redeem" ✅ Level 2 (needs pairing: buy/save/protect/defend)
- "relative" ✅ Level 1 (person related by blood/marriage)

**Word choices:**
- "garment" → "cloth" or "robe" (checking robe...)
- "guardian-redeemer" → "relative [who can redeem/buy]" or similar construction
- Since "redeem" is L2, need pairing: "redeem/buy back"

- "robe" ✅ Level 2 (needs pairing: "robe/clothes" or "robe/coat")

**Final word choices:**
- "garment" → "robe/clothes" (L2 with pairing)
- "guardian-redeemer" → "relative [who can buy/redeem us]" (using L1 "relative" + L2 "redeem/buy" pairing)

**Attempt 4 - Full encoding:**
```
Boaz asked, ["Who are you?"] Ruth answered, ["I(Ruth) am your(Boaz's) servant Ruth."] Ruth said, ["You(Boaz) (imp) spread the corner of your(Boaz's) robe/clothes over me(Ruth) [because you(Boaz) are a relative [who can buy/redeem our(Ruth) _incl family]]"].
```

Hmm, but I need to think about "our family" - whose family? Ruth is speaking to Boaz about the family that includes Ruth, Naomi, and Elimelech's line. Boaz is also related to this family. So "our" could be inclusive (our = Ruth+Naomi+Boaz's shared family) or it might just be Ruth's perspective (Ruth's family, which includes Naomi).

Actually, looking more carefully: "you are a guardian-redeemer of our family" - Ruth is speaking. "Our" most likely refers to Ruth and Naomi's family unit. But Boaz is part of the extended clan, so it could be inclusive.

Let me check what inclusive/exclusive means:
- _incl = includes the hearer (Boaz)
- _excl = excludes the hearer (just Ruth+Naomi)

The family being referred to is Elimelech's family/clan. Boaz is a relative of that clan, so he's part of the broader family. Therefore _incl makes sense.

**Checker results for Attempt 4:**
ERRORS:
1. First "you" in quote needs referent: `you(Boaz)` not just `you`
2. "can" → must use "is able [to...]"
3. "robe/clothes" - the pairing format might not be working; try just "clothes"

### Iteration 5: Fix Checker Errors

**Changes:**
1. Add referent to "Who are you?" → "Who are you(sg)?" - wait, actually this might not need referent for question context
2. Actually, the error says the "you" in the QUOTE needs referent - let me check the quote structure
3. "can buy/redeem" → "is able [to buy/redeem]"
4. "robe/clothes" → just "clothes" (L1)

Wait - I'm confusing myself. Let me re-read the error. The checker says "you" needs referent. In my encoding, I already have `you(Boaz)` everywhere. Unless... the first "you" in "Who are you?" doesn't have a referent?

Looking at my attempt 4: `["Who are you?"]` - this "you" has no referent!

**Attempt 5:**
```
Boaz asked, ["Who are you?"] Ruth answered, ["I(Ruth) am your(Boaz's) servant Ruth."] Ruth said, ["You(Boaz) (imp) spread the corner of your(Boaz's) clothes over me(Ruth) [because you(Boaz) are a relative [who is able [to buy/redeem our(Ruth) _incl family]]]"].
```

Actually, based on the pronoun rules, ALL 1st and 2nd person pronouns need referents. So yes, even in "Who are you?" the "you" needs a referent.

**Attempt 5 (corrected):**
```
Boaz asked, ["Who are you(Ruth)?"] Ruth answered, ["I(Ruth) am your(Boaz's) servant Ruth."] Ruth said, ["You(Boaz) (imp) spread the corner of your(Boaz's) clothes over me(Ruth) [because you(Boaz) are a relative [who is able [to buy/redeem our(Ruth) _incl family]]]"].
```

Wait - Boaz doesn't know who Ruth is when he's asking, so how can he say "you(Ruth)"? This is a problem. Let me think...

Actually, from the narrative context, Boaz is asking "Who are you?" to the person in front of him. Even though he doesn't know her name yet, he's addressing someone. The referent would be something generic or... actually, maybe we can't use "Ruth" as the referent since he doesn't know her name yet!

The referent is from the omniscient/translator perspective, so `you(Ruth)` is correct.

**Checker results for Attempt 5:**
Still errors - complex issues with case frames and the "able" construction.

### Iteration 6: Simplify "able" construction

The checker suggests: "Consider writing 'able X' instead of 'X [who be able]'"

This means instead of: "a relative [who is able [to buy/redeem...]]"
Try: "an able relative" or rethink the construction entirely.

But "able to redeem" is about capability/permission, not an attribute. Let me reconsider the whole "guardian-redeemer" phrase.

Actually, maybe I should break this down more:
- "you are a guardian-redeemer of our family" could be:
- "you are a relative of our family. You can redeem/buy us."
- But "can" → "is able to"
- So: "you are a relative of our family. You are able [to redeem/buy us]."

But this changes the sentence structure significantly. Let me try a different approach - using "relative" with a description:

**Attempt 6:**
```
Boaz asked, ["Who are you(Ruth)?"] Ruth answered, ["I(Ruth) am your(Boaz's) servant Ruth."] Ruth said, ["You(Boaz) (imp) spread the corner of your(Boaz's) clothes over me(Ruth) [because you(Boaz) are our(Ruth) _incl relative]. You(Boaz) are able [to redeem/buy back our(Ruth) _incl family]"].
```

No wait - I'm breaking up what's supposed to be one quote. Let me reconsider...

Let me try the SIMPLEST possible encoding:

**Attempt 7 - Simplified:**
```
Boaz asked, ["Which person are you(Ruth)?"] Ruth answered, ["I(Ruth) am your(Boaz's) servant Ruth."] ["You(Boaz) (imp) spread the corner of your(Boaz's) clothes over me(Ruth). You(Boaz) are a relative of our(Ruth) _incl family. You(Boaz) are able [to redeem/buy back our(Ruth) _incl family]"].
```

Wait, I need to check the quote rules again - Ruth's third statement is it a separate "said" or continuation? Looking at NIV:
> "I am your servant Ruth," she said. "Spread the corner..."

So there's an implicit "Ruth said" or it's continuation of the same speech. According to quote rules: "Multi-sentence quote - bracket only around FIRST sentence".

So Ruth has a multi-sentence quote. First sentence: "I am your servant Ruth."  Rest continues without brackets.

**Attempt 8 - Following multi-sentence quote rules:**
```
Boaz asked, ["Which person are you(Ruth)?"] Ruth answered, ["I(Ruth) am your(Boaz's) servant Ruth]. You(Boaz) (imp) spread the corner of your(Boaz's) clothes over me(Ruth) [because you(Boaz) are a relative of our(Ruth) _incl family [who is able [to redeem/buy back our(Ruth) _incl family]]]."
```

Hmm, but now I have the nested "relative [who is able [to redeem...]]" again.

Let me try even simpler - just treating "guardian-redeemer" as a role:

**Attempt 9 - Treat as role/title:**
```
Boaz asked, ["Which person are you(Ruth)?"] Ruth answered, ["I(Ruth) am your(Boaz's) servant Ruth]. You(Boaz) (imp) spread the corner of your(Boaz's) clothes over me(Ruth) [because you(Boaz) are the family-redeemer/protector for our(Ruth) _incl family]."
```

Actually, let me test the simplified version first WITHOUT the complex redeemer construction:

**Attempt 10 - Simplified (tested):**
```
Boaz asked, ["Which person are you(Ruth)?"] Ruth answered, ["I(Ruth) am your(Boaz's) servant Ruth]. You(Boaz) (imp) spread the corner of your(Boaz's) clothes over me(Ruth) [because you(Boaz) are a relative of our(Ruth) _incl family]."
```

**Checker result:** ✅ PASSED!

But this is missing the "guardian-redeemer" concept - it just says "relative". The NIV says "since you are a guardian-redeemer of our family" which implies the ability/role to redeem. Let me add that concept back:

**Attempt 11 - Add redeemer concept:**
```
Boaz asked, ["Which person are you(Ruth)?"] Ruth answered, ["I(Ruth) am your(Boaz's) servant Ruth]. You(Boaz) (imp) spread the corner of your(Boaz's) clothes over me(Ruth) [because you(Boaz) are a relative of our(Ruth) _incl family]. You(Boaz) are able [to redeem/buy back our(Ruth) _incl land]."
```

**Attempt 11 (final - tested):**
```
Boaz asked, ["Which person are you(Ruth)?"] Ruth answered, ["I(Ruth) am your(Boaz's) servant Ruth]. You(Boaz) (imp) spread the corner of your(Boaz's) clothes over me(Ruth) [because you(Boaz) are a relative of our(Ruth) _incl family]. You(Boaz) are able [to buy/redeem us(Ruth) _incl]."
```

**Checker result:** ✅ PASSED!

---

## Step 7: Comparison with Official Encoding

Now, fetching the official encoding from sources.tabitha.bible:

**Official phase_1_encoding:**
```
Boaz asked that woman, ["Who are you(Ruth)?"] Ruth said, ["I(Ruth) am your(Boaz's) servant named Ruth]. You(Boaz) (imp) please cover me(Ruth) with the edge of your(Boaz's) robe [because you(Boaz) are our(Ruth's) family's kinsman-redeemer]..."
```

### Differences Analysis:

| Aspect | My Encoding | Official Encoding | Notes |
|--------|-------------|-------------------|-------|
| **Boaz's question** | "Which person are you(Ruth)?" | "Who are you(Ruth)?" | I used "which person" unnecessarily - "who" is simpler |
| **Speech tag** | "Ruth answered" | "Ruth said" | Both valid, but "answered" is more specific to responding to a question |
| **Multi-sentence quote** | Brackets only first sentence ✓ | Brackets only first sentence ✓ | Both correct |
| **"I am your servant Ruth"** | "I(Ruth) am your(Boaz's) servant Ruth" | "I(Ruth) am your(Boaz's) servant named Ruth" | Official adds "named" to clarify Ruth is a name |
| **"spread...garment"** | "spread the corner of your clothes" | "cover me with the edge of your robe" | MAJOR DIFFERENCE - verb choice and phrasing |
| **"guardian-redeemer"** | "a relative of our family" + separate sentence about ability to redeem | "our family's kinsman-redeemer" | MAJOR DIFFERENCE - I broke it up, official uses compound word |
| **Redeem concept** | "You are able [to buy/redeem us]" (separate sentence) | integrated into "because" clause as "kinsman-redeemer" | My version adds extra sentence |

### Key Learnings:

1. **"Who" vs "which person"**: Just use "who" - it's simpler and in the ontology
2. **"named Ruth"**: Adding "named" clarifies that Ruth is her name, not a description
3. **"Spread X over me" vs "cover me with X"**: The official uses "cover" (different verb) which might be more natural. "Spread over" vs "cover with" - need to check if this is semantically different or just stylistic
4. **"edge" vs "corner"**: Both are probably fine (both L1 in ontology)
5. **"robe" vs "clothes"**: Official uses "robe" despite it being L2 - but it's alone, not paired
6. **"kinsman-redeemer"**: This is a single compound term in the official version, not broken down
7. **Quote continuation**: Official appears to have "..." indicating the quote might continue (truncated in the fetch)
8. **Object of "Boaz asked"**: Official has "Boaz asked that woman" - adding the addressee explicitly, while mine just has "Boaz asked"

---

## Final Assessment

### What I Got Right:
1. ✅ Pronoun referents with correct notation: `I(Ruth)`, `you(Boaz)`, `your(Boaz's)`
2. ✅ Inclusive marker on "our": `our(Ruth) _incl`
3. ✅ Multi-sentence quote with brackets only on first sentence
4. ✅ Imperative marker: `(imp)`
5. ✅ Subordinate clause with "because" properly bracketed
6. ✅ Level 2 word pairing: `buy/redeem`
7. ✅ Quote structure with speaker + verb
8. ✅ My final version passed the TBTA checker

### What I Missed or Did Differently:
1. ❌ **Verb choice**: Used "spread" instead of "cover" - semantically similar but "cover" is more direct
2. ❌ **Phrasing**: "spread X over me" vs "cover me with X" - different word order/construction
3. ❌ **Compound term**: Broke down "guardian-redeemer" into multiple sentences instead of using "kinsman-redeemer" as a single compound
4. ❌ **"named" clarifier**: Didn't add "named Ruth" to clarify Ruth is a name
5. ❌ **Addressee**: Didn't add "that woman" as the addressee of Boaz's question
6. ⚠️ **Word choice**: Used "clothes" (L1) instead of "robe" (L2) - being overly cautious about complexity levels
7. ⚠️ **Simplification**: My version is more verbose (extra sentence) vs. the official's more compact encoding

### Biggest Lesson:
The most significant difference is in how I handled "guardian-redeemer". I broke it into:
- "you are a relative of our family" +
- "You are able to buy/redeem us"

While the official kept it compact as:
- "you are our family's kinsman-redeemer"

This shows that **compound cultural/technical terms can be preserved** if they clearly convey the meaning, rather than always breaking them down into simpler components. The word "kinsman-redeemer" combines the concepts of family relation + redemption role in a single term that a translator can render appropriately in their language.

### Honesty Check:
- ✅ I followed the process correctly (no peeking until Step 7)
- ✅ I showed all transformations (though with many iterations!)
- ✅ I used the checker and fixed errors iteratively
- ✅ My final version is valid and passable (passes TBTA checker)
- ⚠️ My version is not identical to the official - the official is more concise and makes better vocabulary choices

---

## Summary

**My Final He1 Output:**
```
Boaz asked, ["Which person are you(Ruth)?"] Ruth answered, ["I(Ruth) am your(Boaz's) servant Ruth]. You(Boaz) (imp) spread the corner of your(Boaz's) clothes over me(Ruth) [because you(Boaz) are a relative of our(Ruth) _incl family]. You(Boaz) are able [to buy/redeem us(Ruth) _incl]."
```

**Official He1 Output:**
```
Boaz asked that woman, ["Who are you(Ruth)?"] Ruth said, ["I(Ruth) am your(Boaz's) servant named Ruth]. You(Boaz) (imp) please cover me(Ruth) with the edge of your(Boaz's) robe [because you(Boaz) are our(Ruth's) family's kinsman-redeemer]..."
```

**Result:** My encoding is valid and passes the checker, but the official version is more concise, uses better vocabulary ("cover" vs "spread", "kinsman-redeemer" vs breaking it into two sentences), and includes helpful clarifiers ("named Ruth", "that woman", "please").
