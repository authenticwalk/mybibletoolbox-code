# TBTA Patterns - Detailed Examples Appendix

This appendix provides extensive examples for each of the 23 discovered patterns, organized by type.

---

## PART 1: UNDERSCORE-PREFIXED SEMANTIC MARKERS

### Pattern 1: _implicit
**Marks:** Information that is implied but not explicitly stated

```
Example 1: Matthew 27:6
"And the waves _frameInferable came over the sides of the boat
[so that the boat was almost full of water _implicit]."

Example 2: Mark 4:37
"Then a very strong wind started to blow over the lake _implicit."

Example 3: Matthew 24:38
"And people were eating good food _implicit.
And people were drinking alcohol _implicit."
```

**Why marked:** The verse doesn't explicitly state "the lake was there" or "they ate" in all details.

---

### Pattern 2: _paragraph
**Marks:** Paragraph-level structural divisions

```
Example 1: Matthew 27:6
"_paragraph The chief priests pick-up the coins."

Example 2: Matthew 26:17
"_paragraph On the first day of the Feast-of-Unleavened-Bread,
the followers/disciples came to Jesus."

Example 3: Matthew 12:22
"_paragraph Then people brought to Jesus a man
[who was controlled by a demon]."
```

**Why marked:** Translation structure indicator for paragraph-level processing.

---

### Pattern 3: _implicitActiveAgent
**Marks:** The implied active agent in passive voice constructions

```
Example 1: Mark 15:28
"The servant of the Lord-A was treated badly _implicitActiveAgent
by [people _implicitActiveAgent]."

Example 2: Matthew 27:6
"A person would be killed by people _implicitActiveAgent."

Example 3: Matthew 10:2
"[who were Jesus's followers/disciples] were _be-K Simon"
```

**Why marked:** Passive voice hides the agent; marking it helps AI identify actors.

---

### Pattern 4: _implicitNecessary
**Marks:** Information necessarily implied by context but not stated

```
Example 1: Matthew 9:5
"I(Jesus) _implicitNecessary might say,
['Your(man's) sins are forgiven by me(Jesus) _implicit']."

Example 2: Mark 15:15
"Pilate ordered [soldiers _implicitNecessary to whip Jesus]."

Example 3: Matthew 1:17
"The list has 14 fathers/generations
[who lived between _newSense the time [that Abraham lived at]]."
```

**Why marked:** Context makes these inferences necessary for understanding.

---

### Pattern 5: _dual
**Marks:** Dual number (exactly two entities)

```
Example 1: Mark 11:3
"Why are you(followers) _dual taking this young horse/donkey?"

Example 2: Mark 10:38
"You(James) _dual do not understand the thing"

Example 3: Matthew 8:32
"Jesus said, 'You(spirits) (imp) go into the group of pigs _implicit!'"
```

**Why marked:** Important for languages with grammatical dual number.

---

### Pattern 6: _frameInferable
**Marks:** Information inferable from the discourse frame/context

```
Example 1: Mark 4:37
"The waves _frameInferable came over the sides of the boat."

Example 2: Matthew 9:6
"The Son-of-Man _1stas3rd has authority on the earth _frameInferable
[in order to forgive sins]."

Example 3: Matthew 8:32
"[go into the group of pigs _implicit!] So those evil spirits/demon
come-out from the man. And those evil spirits/demon went into the pigs."
```

**Why marked:** Frame makes this information available without explicit statement.

---

### Pattern 7: _implicitType
**Marks:** Implicit type or category reference

```
Example 1: Matthew 7:22
"Did we(people) prophesy with your(Jesus's) name _implicitType?"

Example 2: Mark 3:23
"Will (rhetorical) Satan force [Satan's evil spirits/demons _implicitType
to leave people _implicit]?"

Example 3: Matthew 8:32
"I(God) make this covenant with all the animals
[that were with you(Noah) in the boat]."
```

**Why marked:** Type information guides semantic interpretation.

---

### Pattern 8: _generic
**Marks:** Generic/non-specific plural references

```
Example 1: Matthew 27:19
"When a ruler _generic judges people _generic"

Example 2: Matthew 22:13
"You(servants) (imp) tie this man's hands and this man's feet."

Example 3: Matthew 27:19
"[when a ruler _generic sits on [that a ruler _generic judges people _generic]]"
```

**Why marked:** Distinguishes generic uses from specific group references.

---

### Pattern 9: _descriptive
**Marks:** Descriptive vs. identifying appositives

```
Example 1: Matthew 26:25
"[_descriptive who was the follower/disciple
[who will give Jesus to Jesus's enemies]]"

Example 2: Matthew 17:5
"And a voice spoke from that cloud."

Example 3: Matthew 10:2
"[who (implicit-situational) were Jesus's followers/disciples]
were _be-K Simon [who was called Peter]."
```

**Why marked:** Distinguishes whether appositive specifies or describes.

---

### Pattern 10: _metonymy
**Marks:** Metonymic language (part for whole, etc.)

```
Example 1: Matthew 26:17
"The followers/disciples asked, ['Where do you(Jesus) want
[us(followers) _excl prepare-B the Passover of the meal _metonymy'"

Example 2: Matthew 21:32
"God will punish Tyre of the people _metonymy
and Sidon of the people _metonymy"

Example 3: Matthew 11:22
"God will punish Tyre of the people _metonymy more-than
[God will punish Tyre of the people _metonymy]"
```

**Why marked:** Identifies figurative language for translation consideration.

---

### Pattern 11: _routinely
**Marks:** Routine, habitual, or characteristic actions

```
Example 1: Matthew 9:13
"I(God) want/desire [you(people) to learn the thing
[that the following words mean]."

Example 2: Matthew 17:24
"[After Jesus and Jesus's followers/disciples arrived in Capernaum,]
tax collectors came to Peter."

Example 3: Matthew 19:21
"You(man) (imp) sell all of your(man's) things/possessions."
```

**Why marked:** Distinguishes habitual from perfective aspect.

---

### Pattern 12: _morally
**Marks:** Actions evaluated from moral/ethical dimension

```
Example 1: Nehemiah 9:2
"Those people admitted [that those people had done bad _morally things]."

Example 2: Nehemiah 9:37
"[Because we(people's) did bad _morally things] the kings
[that you(God) allow [to rule us(people)]]"

Example 3: Genesis 49:6
"You(Simeon) hurt oxen [because you(Simeon) enjoy
[being cruel to animals]]."
```

**Why marked:** Flags theological/ethical significance.

---

### Pattern 13: _newSense
**Marks:** Word takes on new or different sense

```
Example 1: Matthew 1:17
"The list has 14 fathers/generations
[who lived between _newSense the time [that Abraham lived at]
and the time [that David lived at]]."

Example 2: (Implied in complex genealogical passages)

Example 3: (Semantically shifted contexts)
```

**Why marked:** Signals polysemy and semantic shift in word meanings.

---

## PART 2: PARENTHETICAL CLARIFICATION MARKERS

### Pattern 14: Role/Agent Markers
**Format:** `(role-name)` attached to pronouns

```
Example 1: Matthew 27:6
"The religious laws do not allow [us(priests) to put this money]"

Example 2: 2 Samuel 10:5
"The king said, ['(imp) You(officials) stay in Jericho
[until your(officials') beards grow]']"

Example 3: Genesis 23:11
"I(Ephron) will give the land to you(Abraham).
These people witness [that I(Ephron) give the land to you(Abraham)].
You(Abraham) (imp) bury your(Abraham's) wife"
```

**Common role types:**
- (priests), (officials), (man), (men), (woman), (women)
- (Jesus), (God), (David), (Abraham) - proper name roles
- (followers), (disciples), (servants), (soldiers), (people)
- (followers) _excl - exclusive marker

**Why marked:** Critical for pronoun resolution in multiple-character scenes.

---

### Pattern 15: (imp) - Imperative Mood
**Format:** `(imp)` prefix to imperative verb

```
Example 1: 2 Samuel 10:5
"The king said, ['(imp) You(officials) stay in Jericho
[until your(officials') beards grow]'].
Then (imp) you(officials) return to Jerusalem."

Example 2: 1 Samuel 23:4
"Yahweh answered, ['You(David) (imp) go to Keilah']."

Example 3: Genesis 23:11
"You(Abraham) (imp) bury your(Abraham's) wife in that cave."
```

**Why marked:** Marks mood distinction for languages without morphological imperative marking.

---

### Pattern 16: Translation Type Markers
**Format:** `(literal)`, `(dynamic)`, `(rhetorical)`, etc.

```
Example 1: Mark 6:3
"(yesrhetorical) Is this man the person [who builds things with wood]?
(statement) This man is only-C _implicit the person
[who builds things with wood]."

Example 2: Matthew 24:38
"(literal) For before the time [that water completely covered-C the earth at]
people were eating good food _implicit.
(dynamic) For a person [who wants [to continue living on this earth _implicit]]"

Example 3: Mark 8:35
"(literal) For a person [who wants [to keep-B that person's life]] will die.
(dynamic) For a person [who wants [to continue living on this earth _implicit
[(implicit-situational) just-like that person is living now]]] will not live forever _implicit"
```

**Subtypes:**
- `(literal)` - word-for-word rendering
- `(dynamic)` - sense-for-sense rendering
- `(rhetorical)` - rhetorical question
- `(yesrhetorical)` - yes/no rhetorical question
- `(norhetorical)` - explicitly not rhetorical
- `(statement)` - statement following rhetorical question

**Why marked:** Tracks translation methodology and sentence pragmatics.

---

### Pattern 17: Context Markers
**Format:** `(implicit-situational)`, `(title)`, `(footnote)`, `(paragraph)`

```
Example 1: Matthew 24:38
"Then Noah entered the big boat
[that (implicit-situational) God told [Noah to build]]."

Example 2: Mark 8:35
"[just-like that person is living now (implicit-situational)]]"

Example 3: 2 Samuel 2:18
"(title) Abner kills Asahel. Zeruiah had three sons"

Example 4: Matthew 26:17
"(footnote) For _relation the meal of Passover
a young sheep was killed/sacrifice by each Jewish family."
```

**Subtypes:**
- `(implicit-situational)` - context implied by narrative situation
- `(title)` - section title
- `(footnote)` - explanatory note
- `(paragraph)` - paragraph marker
- `(complex)` - complex grammatical structure
- `(comment-begin)`, `(comment-end)` - annotation comments

**Why marked:** Distinguishes commentary types from content.

---

## PART 3: SYNTACTIC DELIMITER PATTERNS

### Pattern 18: Square Brackets for Embedded Clauses
**Format:** `[clause type + content]`

```
RELATIVE CLAUSES:
Example 1: Matthew 27:6
"[that people _generic put money [that is for the building/temple] into]"

Example 2: 2 Samuel 10:5
"[that Hanun treated David's officials badly]"

Example 3: Genesis 23:11
"[that is on the land]"

PURPOSE CLAUSES:
Example 1: Matthew 27:6
"[so that a person would be killed by people _implicitActiveAgent]"

Example 2: Matthew 26:17
"[us(followers) _excl prepare-B the Passover of the meal _metonymy
[so that you(Jesus) and we(followers) _implicit could eat that meal _implicit]]"

TEMPORAL CLAUSES:
Example 1: 2 Samuel 2:20
"[While Abner was run-away from Asahel]"

Example 2: Matthew 24:38
"[after that]"

CONDITIONAL CLAUSES:
Example 1: Mark 8:35
"[if a person is willing [to die for me(Jesus)]]"

CAUSAL CLAUSES:
Example 1: Genesis 49:6
"[because you(Simeon) enjoy [being cruel to animals]]"

NESTED MULTIPLE LEVELS:
Example 1: Matthew 27:6
"[us(priests) to put this money into the box
[that people _generic put money [that is for the building/temple] into]]"
```

**Why marked:** Syntactic delimiters enable parsing of complex nested structures.

---

## PART 4: WORD AND CONCEPT MODIFICATION PATTERNS

### Pattern 19: Slash-Separated Alternatives
**Format:** `word/alternative`

```
Example 1: Matthew 27:6
"The chief priests..." could be "The priests/leaders"

Example 2: Multiple translation equivalents
"followers/disciples" - two valid English renderings
"spirits/demons" - alternative terminology
"away/arrest" - translation variation
"garden/vineyard" - semantic alternatives
"good/righteous" - translation option pair

Common patterns:
- followers/disciples (role translation)
- spirits/demon (entity naming)
- away/arrest (action naming)
- cry/weep (emotion description)
- people/scribes (group identification)
```

**Why marked:** Represents legitimate translation variation and semantic ambiguity.

---

### Pattern 20: Hyphenated Compound Expressions
**Format:** `word-word` or `word-word-word`

```
Spatial:
- in-front-of
- in-side-of
- on-top-of

Temporal:
- after-that
- before-that
- during-that

Action:
- get-up
- run-away
- pick-up
- take-away
- cut-off
- come-out

Abstract:
- each-other
- in-order-to
- so-that
- just-like
- more-than
- mother-in-law

Information Type:
- implicit-info
- implicit-situational
- implicit-subaction

Example Usage:
"[When Abner was run-away from Asahel]"
"[so that the boat was almost full of water _implicit]"
"You(men) may rest under the tree"
"[in order to forgive sins]"
```

**Why marked:** Treats multi-word expressions as semantic units.

---

### Pattern 21: Letter Suffixes (-A, -B, -C, -D, -U, etc.)
**Format:** `word-[A-Z]`

```
Example 1: Mark 14:65
"covered-A Jesus's eyes... beat Jesus... hit-A Jesus"

Example 2: Mark 6:3
"the brother-A of James... the sisters-B in this place"

Example 3: Matthew 24:38
"covered-C the earth... people's daughters... each-other(people)...
people's sons"

Example 4: Matthew 11:2
"John the Baptist heard-D about the things [that Christ was doing]."

Example 5: Mark 4:1
"(literal) That person/messenger be-U a voice
[that is shouting in the desert]"

Example 6: Matthew 25:40
"my(king's) least important sisters-D _implicit"

PURPOSE:
Track when the same concept/actor appears multiple times in a verse:
- covered-A (first instance)
- covered-B (second instance)
- covered-C (third instance, etc.)
```

**Why marked:** Disambiguates repeated concepts in complex narratives.

---

### Pattern 22: Possessive Pronoun Expansion
**Format:** `possessive(referent)'s`

```
Example 1: 2 Samuel 10:5
"your(officials') beards grow"
"your(Abraham's) wife"

Example 2: Matthew 24:38
"The wives of Jacob's sons also went to Egypt"
"those people's daughters"
"those people's sons"

Example 3: Genesis 23:11
"I(Ephron) will give the land...
I(Ephron) will give the land to you(Abraham).
These people witness [that I(Ephron) give the land to you(Abraham)].
You(Abraham) (imp) bury your(Abraham's) wife"

Example 4: 1 Samuel 27:3
"And David's two wives were with David in Gath.
One wife's name was Ahinoam.
Ahinoam was from Jezreel.
And the other wife's name was Abigail.
Abigail was from Carmel.
Abigail was previously Nabal's wife."

PURPOSE:
Expand possessive relationships to clarify:
- I(Jesus)'s body
- your(Abraham's) family
- his(David's) plans
- her(Mary's) son
```

**Why marked:** Critical for languages with different possessive systems.

---

## PART 5: DISCOURSE STRUCTURE MARKERS

### Pattern 23: Discourse Conjunctions
**Format:** Explicit connectives marking logical/temporal relationships

```
TEMPORAL SEQUENCE:
- Then (indicates temporal progression)
- After (specifies temporal order)
- While (concurrent action)
- Before (temporal precedence)

Example: "Then Simeon and Levi went to that town.
Then Simeon and Levi attacked all the men"

LOGICAL CONSEQUENCE:
- So (result)
- Thus (logical outcome)
- Therefore (deduction)

Example: "Those officials were very ashamed/humiliated.
So David sent messengers to those officials."

CONTRAST:
- But (opposes previous statement)
- Yet (emphasizes contrast)

Example: "For this money was used... But the prince will command..."

REASON/CAUSE:
- Because (explains why)
- Since (provides rationale)

Example: "[Because Pilate wanted [to satisfy that crowd],]
Pilate freed Barabbas"

EXPLICIT OCCURRENCE:
"So now this man is the king..."
"Thus the event [that the Scriptures described] happened"
"But those people do not have food"
"And David's two wives were with David"
```

**Why marked:** Makes discourse structure explicit for logical flow analysis.

---

## COMBINED PATTERN EXAMPLES

### Complex Example 1: Multiple Patterns Interacting
```
"[Because Pilate wanted [to satisfy that crowd],] Pilate freed Barabbas for-C that crowd.
Then Pilate ordered [soldiers _implicitNecessary to whip Jesus].
And Pilate gave Jesus to soldiers _implicit [so that soldiers _implicitNecessary
would kill Jesus [by putting Jesus on a cross]]."
```

**Patterns used:**
- Square brackets (nested clauses)
- Letter suffix (-C for "for-C")
- _implicitNecessary markers
- _implicit markers
- Role markers (implied soldiers)
- Discourse conjunction (Because, Then, And, so)
- Purpose clause markers

### Complex Example 2: Role and Pronoun Clarity
```
"[When the evil spirit [that comes from Yahweh] enters you(Saul)]
that person will play the harp. Then the evil spirit will leave you(Saul).
And you(Saul) will feel good. So you(Saul) (imp) command
[us(servants) to look for a person [who will play the harp for you(Saul)]]."
```

**Patterns used:**
- Role markers (you(Saul), us(servants))
- Square brackets (nested clauses)
- Temporal markers (When, Then)
- Discourse conjunctions (Then, So)
- Imperative (imp) marker

### Complex Example 3: Translation Type and Implicit Info
```
"(literal) For a person [who wants [to keep-B that person's life]] will die.
(dynamic) For a person [who wants [to continue living on this earth _implicit
[(implicit-situational) just-like that person is living now]]]
will not live forever _implicit with God _implicit."
```

**Patterns used:**
- Translation type markers (literal/dynamic)
- Square brackets (nested clauses)
- Letter suffix (-B for "keep-B")
- _implicit markers
- (implicit-situational) context marker
- Possessive expansion (that person's life)

---

## Pattern Frequency Distribution Table

| Rank | Pattern | Count | % | Category |
|------|---------|-------|---|----------|
| 1 | Square brackets | 454 | 90.8% | Syntax |
| 2 | Role markers | 214 | 42.8% | Clarification |
| 3 | Discourse conjunctions | 195 | 39.0% | Discourse |
| 4 | Possessive expansion | 138 | 27.6% | Clarification |
| 5 | _implicit | 118 | 23.6% | Semantic |
| 6 | Slash alternatives | 115 | 23.0% | Lexical |
| 7 | Hyphenated compounds | 109 | 21.8% | Lexical |
| 8 | (imp) marker | 79 | 15.8% | Grammatical |
| 9 | Letter suffixes | 61 | 12.2% | Disambiguation |
| 10 | _paragraph | 36 | 7.2% | Structural |
| 11 | Translation type | 26 | 5.2% | Meta |
| 12 | _implicitActiveAgent | 28 | 5.6% | Semantic |
| 13 | _implicitNecessary | 25 | 5.0% | Semantic |
| 14 | (implicit-situational) | 22 | 4.4% | Context |
| 15 | _dual | 15 | 3.0% | Grammatical |
| 16 | _frameInferable | 12 | 2.4% | Semantic |
| 17 | _implicitType | 11 | 2.2% | Semantic |
| 18 | _generic | 10 | 2.0% | Semantic |
| 19 | _descriptive | 10 | 2.0% | Semantic |
| 20 | _metonymy | 6 | 1.2% | Rhetorical |
| 21 | _routinely | 6 | 1.2% | Aspectual |
| 22 | _morally | 3 | 0.6% | Evaluative |
| 23 | _newSense | 3 | 0.6% | Semantic |

---

## Conclusion

The 23 patterns discovered in the TBTA corpus represent a comprehensive, multi-modal annotation system designed to:
1. Make implicit information explicit for AI processing
2. Clarify ambiguous referents and pronouns
3. Represent translation complexity and variation
4. Mark semantic and grammatical distinctions
5. Establish explicit discourse structure
6. Enable precise syntactic parsing

All patterns work together in a layered system where multiple patterns can apply to the same element, enabling richly annotated text suitable for training advanced AI language models on Biblical text.
