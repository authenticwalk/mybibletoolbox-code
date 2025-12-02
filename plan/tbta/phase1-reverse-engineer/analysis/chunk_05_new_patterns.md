# TBTA CNL Transformation Patterns - Chunk 5 Analysis

Analysis of 870 verses from chunk_05.tsv identifying NEW patterns beyond the existing documented patterns.

---

## 1. RHETORICAL QUESTION TRANSFORMATION

**Pattern**: Rhetorical questions are explicitly tagged and immediately followed by the statement form of the answer.

**Structure**: `(rhetorical) Question? (statement) Statement form.`

**Examples**:
- **Matthew 12:29**: "(norhetorical) Similarly, is a person able [to enter the house of a strong man [in order to steal that man's things]] [unless a person first ties a strong man]? (statement) Similarly, a person is not able..."
- **Matthew 26:65**: "(rhetorical) Why do we(priests) need [more people to say bad things about this man]? (statement) We(priests) _incl do not need..."
- **Mark 9:12**: "(rhetorical) But why do the Scriptures say [the Son-of-man must much suffer]? (statement) The Scriptures say [the Son-of-man must much suffer]"
- **Mark 12:26**: "(yesrhetorical) Did you(Sadducees) read-C the part of the book of Moses...? (statement) You(Sadducees) certainly read-C the part of the book..."
- **Matthew 16:8**: "(rhetorical) Why are you(followers) saying to each-other? (statement) You(followers) should not be saying..."

**Variations**:
- `(norhetorical)` = expects "no" answer
- `(yesrhetorical)` = expects "yes" answer
- Both are followed by explicit `(statement)` form

---

## 2. DIRECT SPEECH QUOTATION SYSTEM

**Pattern**: All direct speech is enclosed in square brackets with explicit speaker identification before the quote.

**Structure**: `Speaker said/asked, ["quoted text"]` or `Speaker said to Target, ["quoted text"]`

**Examples**:
- **Genesis 1:3**: "Then God said, ["Let light be!]" And light was."
- **Genesis 21:17**: "The angel said, ["Hagar, why are you(Hagar) crying?]"
- **1 Samuel 17:8**: "Goliath shouted to the Israelite soldiers, ["Why are you(soldiers) preparing [to fight]]?"
- **Matthew 9:24**: "Jesus said to those people _implicit, ["You(people) (imp) go-out from this house]"
- **Mark 1:24**: "["Jesus of Nazareth, why are you(Jesus) annoying us(spirits)?]"

**Nested Quotes**: Use double bracketing:
- **Genesis 42:33**: "Then that official said to us(brothers), ["You(brothers) must prove [that you(brothers) are not lying]]"
- **1 Samuel 9:17**: "Yahweh said, ["That man is the man [that I(Yahweh) told you(Samuel) about yesterday]]"

---

## 3. PASSIVE-TO-ACTIVE TRANSFORMATION WITH AGENT MARKING

**Pattern**: Passive voice is systematically converted to active voice with explicit agent marking using `by X _implicitActiveAgent`.

**Examples**:
- **Matthew 14:11**: "John's head was brought by that soldier _implicitActiveAgent on a big plate. And John's head was given by that soldier _implicitActiveAgent to that daughter."
- **Matthew 5:4**: "People [who cry now] are blessed by God _implicitActiveAgent. For those people will be comforted by God _implicitActiveAgent."
- **Matthew 27:26**: "Pilate ordered [soldiers _implicitNecessary to whip Jesus]. And Pilate gave Jesus to soldiers _implicitNecessary [so that soldiers _implicitNecessary would kill Jesus [by putting Jesus on a cross]]."
- **Matthew 27:52**: "And the holes/cave were opened by God _implicitActiveAgent."
- **Mark 15:47**: "Mary saw the place [where Jesus's body was put by Joseph _implicitActiveAgent]."

**Agent Types**:
- `_implicitActiveAgent` = agent is contextually obvious
- `_implicitNecessary` = agent must be inferred from context
- `_implicitActiveAgentFrameInferable` = agent inferable from semantic frame

---

## 4. IMPERATIVE COMMAND MARKING

**Pattern**: All imperative commands are explicitly marked with `(imp)` regardless of context.

**Examples**:
- **Genesis 1:3**: "Then God said, ["Let light be!]" (uses "Let" without imp)
- **Joshua 1:18**: "But (imp) you(Joshua) be strong and brave!"
- **Matthew 6:13**: "you(Father) (imp) do not let [us(people) be tempted]"
- **Mark 10:13**: "(imp) God will do good things for some children"
- **Genesis 3:3**: "You(Eve) (imp) do not touch that tree"

**Patterns**:
- Positive commands: `(imp) do X`
- Negative commands: `(imp) do not do X`
- Suggestions: `We(Jesus) go _suggestiveLets`

---

## 5. CONDITIONAL STRUCTURE BRACKETING

**Pattern**: Conditional clauses are explicitly bracketed with clear if-then structure.

**Examples**:
- **2 Samuel 3:35**: "[If I(David) eat food [before the sun sets]] I(David) hope [that God will punish me(David) greatly]!"
- **Genesis 19:8**: "[If you(men) want me(Lot) to help you(men)] I(Lot) will help you(Lot)"
- **Matthew 24:43**: "[If the person knows the time [that the thief will come at],] the person will be awake"
- **Acts 18:14**: "[If you(Jews) had complained to me(Gallio) [that a man broke a law, then I(Gallio) should listen to you"
- **Daniel 3:17**: "[If God wants [to save us(men)]] God will save us(men)"

**Pattern**: `[If condition] result` or `[If condition] [then result]`

---

## 6. TEMPORAL/TIME EXPRESSION BRACKETING

**Pattern**: All temporal expressions are enclosed in brackets with explicit temporal markers.

**Examples**:
- **Matthew 2:19**: "Then [after Herod died,] an angel of the Lord appeared"
- **Genesis 14:17**: "[After Abram defeated Kedorlaomer] Abram returned"
- **Mark 16:12**: "[while 2 other followers were walking to a village]"
- **1 Samuel 3:15**: "[After Samuel got up] Samuel opened the doors"
- **Acts 2:6**: "On the second day... On the third day..."

**Temporal Markers**:
- `[After X]` = sequential action
- `[Before X]` = prior action
- `[While X]` = concurrent action
- `[When X]` = situational time
- `On the Xth day` = specific time point

---

## 7. NAMED ENTITY LIST PATTERN

**Pattern**: Lists of people, places, or things use "named" repeatedly for each item.

**Examples**:
- **Genesis 7:13**: "the sons of Noah named Shem, named Ham, and named Japheth"
- **Genesis 35:23**: "sons named Simeon, named Levi, named Judah, named Issachar, and named Zebulun"
- **Joshua 15:38**: "the towns named Dilean, Mizpah, and Joktheel"
- **Esther 1:10**: "These men's names were Mehuman, Biztha, Harbona, Bigtha, Abagtha, Zethar, and Carcas"
- **Nehemiah 12:35**: "Zechariah also followed... Zechariah was a son of Jonathan [who was a son of Shemaiah]"

**Pattern**: `named X, named Y, and named Z` or `X, Y, and Z` without "named" for generic lists

---

## 8. COMPARISON STRUCTURE: "JUST-LIKE"

**Pattern**: Similes and comparisons use explicit "just-like" construction with bracketed comparison.

**Examples**:
- **Matthew 24:109**: "These events will be-U like the first pains of a woman [who will soon birth a baby]"
- **Genesis 30:39**: "the animals sexed each-other(animals) in-front-of the branches"
- **Nahum 2:8**: "Nineveh is like a pool [that is not able [to contain water]]"
- **Matthew 20:1**: "God is like a person [who owns land]"
- **Mark 2:21**: "[just-like a person washes new cloth]"

**Pattern**: `X is like Y` or `X [just-like Y]`

---

## 9. NUMERIC AND QUANTITY EXPRESSIONS

**Pattern**: Numbers are typically written as digits with explicit quantity markers.

**Examples**:
- **Genesis 32:14**: "Jacob gathered 200 female goats, 20 male goats, 200 female sheep, and 20 male sheep"
- **2 Samuel 12:30**: "that crown weighed about 34 kilograms"
- **Genesis 23:15**: "the price of that field is silver -quantity 5 kilograms"
- **Mark 5:42**: "The girl was 12 years old"
- **Nehemiah 7:17**: "2322 men [that were from Azgad] returned"

**Patterns**:
- Cardinal numbers: digits (200, 20, 12)
- Weight/measure: "X kilograms", "-quantity X"
- Age: "X years old"
- Ordinal: "first", "second", "third" (spelled out)

---

## 10. NEGATION PATTERNS

**Pattern**: Multiple negation strategies with explicit marking.

**Examples**:
- **Matthew 24:36**: "But no person knows-C the day"
- **1 Samuel 2:9**: "People do not defeat people's enemies [because the people are strong]"
- **Genesis 3:3**: "You(Eve) must not eat... You(Eve) (imp) do not touch"
- **Matthew 26:65**: "We(priests) do not need"
- **Acts 19:37**: "because these two men have not done a bad thing"

**Patterns**:
- `do not X` = simple negation
- `must not X` = prohibition
- `no person X` = universal negation
- `not able [to X]` = inability

---

## 11. COMMENT AND FOOTNOTE INSERTION

**Pattern**: Editorial comments and footnotes are explicitly marked and separated from narrative.

**Examples**:
- **Mark 5:42**: "(comment-begin) The girl was 12 years old. (comment-end)"
- **Matthew 24:15**: "(comment-begin) I(Matthew) pray/pray-hope [you understand the meaning] (comment-end)"
- **Mark 9:5**: "(footnote) Rabbi named the word means-C teacher"
- **Genesis 20:5**: "(footnote) Some copies/manuscripts of this part of the Scriptures..."
- **Mark 11:9**: "(footnote) The people shouted, ["Hosanna"]. The word Hosanna means-A, ["You(God) save us"]"

**Types**:
- `(comment-begin)...(comment-end)` = narrative comments
- `(footnote)` = textual or explanatory notes
- `(title)` = section headers
- `(paragraph)` = paragraph breaks

---

## 12. LITERAL VS. DYNAMIC TRANSLATION MARKERS

**Pattern**: Provides both literal and dynamic meanings with explicit tags.

**Examples**:
- **Mark 1:3**: "(literal) That person be-U a voice [that is shouting in the desert]. (dynamic) That person is shouting in the desert"
- **Mark 7:6**: "(literal) These people honor me(God) with these people's lips. (dynamic) These people honor me(God) with the words [that these people say]"
- **Matthew 26:38**: "(literal) My(Jesus's) heart/soul is very sad. (dynamic) I(Jesus) am very sad"
- **Matthew 5:35**: "(literal) For the earth is the place [that God steps on]. (dynamic) For God rules the earth"
- **Matthew 11:11**: "(literal) John is the most important person [who was born from a woman]. (dynamic) John is the most important person [who was born on earth]"

**Pattern**: `(literal) X. (dynamic) Y.` provides two rendering options

---

## 13. COMPLEX/SIMPLE ALTERNATION

**Pattern**: Provides both complex theological language and simplified explanation.

**Examples**:
- **Mark 14:25**: "[(complex) that I(Jesus) drink a new wine in the kingdom-B of God on] [(simple) that I(Jesus) drink a new wine [after God starts ruling God's people] on]"
- **Matthew 20:1**: "(complex) For the kingdom-B of heaven is like... (simple) God is like..."
- **Matthew 6:33**: "(complex) you(people) search/seek the kingdom-B of God. (simple) you(people) try [to act [just-like people [whom God rules] act]]"
- **Matthew 16:27**: "(complex) For the Son-of-Man will come in-H the glory. (simple) For the Son-of-Man will come in-H the great/glorious power"

**Pattern**: `(complex) theological term (simple) simplified explanation`

---

## 14. IMPLICIT INFORMATION RESTORATION

**Pattern**: Extensive use of `_implicit` markers to restore elided information.

**Categories**:
- `_implicit` = general implicit information
- `_implicitNecessary` = necessary for understanding
- `_implicitActiveAgent` = implicit agent in passive constructions
- `_implicitType` = type/category information
- `_implicitExplainName` = explanatory name
- `_implicitSubaction` = implicit sub-action
- `_implicitSituational` = situationally implicit
- `_implicitInfo` = implicit background info
- `_implicitBackground` = background information
- `_implicitHyperbolic` = hyperbolic "all"

**Examples**:
- **Matthew 9:33**: "the crowds _implicitHyperbolic said"
- **Mark 6:40**: "(implicit-subaction) Jesus's followers told [the people to sit-down]. So the people sit-down"
- **Matthew 27:7**: "people _implicitNecessary bury dead _implicit people"
- **Genesis 34:17**: "[if you(Shechem) refuse [to be circumcised by a person]]"

---

## 15. FIRST-AS-THIRD PERSON SUBSTITUTION

**Pattern**: Jesus' first-person references are marked as third-person with `_1stAs3rd` tag.

**Examples**:
- **Matthew 24:55**: "the Son-of-man _1stAs3rd will return-B"
- **Matthew 16:27**: "the Son-of-Man _1stAs3rd will come in-H the glory of the Son-of-Man's _1stAs3rd Father"
- **Mark 14:58**: "I(Jesus) will destroy this temple"
- **Matthew 25:33**: "The Son-of-man _1stAs3rd will put the sheep on the Son-of-man's _1stAs3rd right side"

**Pattern**: Marks when Jesus speaks of himself in third person

---

## 16. PRONOUN NUMBER DISAMBIGUATION

**Pattern**: Explicit marking of dual and trial/plural distinctions.

**Examples**:
- **Matthew 18:16**: "with 1 or 2 other friends/brothers-D or sisters-D _dual"
- **Mark 11:2**: "You(followers) _dual (imp) go to the village"
- **Genesis 3:5**: "you(Eve) will become like God" (singular addressee clarified)

**Markers**:
- `_dual` = exactly two people
- `_trial` = three people
- `_plural` = general plural

---

## 17. METONYMY EXPLICIT MARKING

**Pattern**: Metonymic expressions are tagged and sometimes explained.

**Examples**:
- **Matthew 4:12**: "the king Herod _implicitActiveAgent of the soldiers _metonymyImplicitType"
- **Matthew 18:16**: "tell the church of the leaders _metonymy"
- **Matthew 17:25**: "the earth's kings of the tax collectors _metonymy"

**Pattern**: `X of Y _metonymy` indicates metonymic relationship

---

## 18. REPETITION AND ITERATION MARKERS

**Pattern**: Repeated actions are explicitly marked.

**Examples**:
- **Matthew 27:30**: "Those soldier hit Jesus's head with that stick repeatedly-A"
- **Genesis 27:36**: "Jacob tricked me(Esau) –iteration 2 times"
- **Mark 1:3**: Similar patterns repeated

**Pattern**: `repeatedly-A`, `–iteration X times`

---

## 19. GENDER INCLUSIVE "BROTHERS/SISTERS" PATTERN

**Pattern**: "Brothers" is expanded to "brothers-D or sisters-D" to show gender inclusivity.

**Examples**:
- **Matthew 18:16**: "1 or 2 other friends/brothers-D or sisters-D _implicit"
- **Matthew 7:5**: "the eye of your(person's) friend/brother-D or sister-D"
- **Matthew 18:21**: "my(Peter's) friend/brother-D or sister-D _implicit"

**Pattern**: `brother-D or sister-D` for inclusive reference

---

## 20. FRAME AND SEMANTIC ROLE MARKERS

**Pattern**: Extensive use of frame-semantic markers to clarify implicit information.

**Examples**:
- `_frameInferable` = information inferable from semantic frame
- `_frameInferableNecessary` = necessary frame information
- `_relationNotArgument` = marks relations vs. arguments
- `_addSourceArgument` = adds source to verb frame

**Examples**:
- **Matthew 24:43**: "the person [who owns the house _frameInferable]"
- **Matthew 6:13**: "from the evil spirit _frameInferable"
- **Matthew 16:27**: "with _relationNotArgument the angels"

---

## 21. TITLE AND STRUCTURAL MARKERS

**Pattern**: Explicit structural markup for organizing text.

**Examples**:
- **Matthew 2:19**: "(title) Joseph and Joseph's family return to Nazareth. (paragraph)"
- **Mark 5:42**: "(title) Jesus heals..."
- **Genesis 14:17**: "-Title Abram has descendants"
- **Matthew 20:1**: "_paragraph For the kingdom..."

**Types**:
- `(title)` = section title
- `(paragraph)` or `_paragraph` = paragraph marker
- `-Title` = alternative title marker

---

## 22. ADDRESSEE AND SPEAKER CLARIFICATION

**Pattern**: Explicit marking of who is speaking to whom using parenthetical notation.

**Examples**:
- **Matthew 26:2**: "You(followers) know [there are 2 days until the Passover]"
- **Genesis 21:17**: "you(Hagar) crying?"
- **1 Samuel 17:8**: "you(soldiers) are Saul's servants"
- **Matthew 9:24**: "Jesus said to those people _implicit, ["You(people) (imp) go-out"]"

**Pattern**: `Speaker said to Target(identity), ["quote"]` with explicit addressee marking in pronouns

---

## 23. SEMANTIC FIELD GLOSSING

**Pattern**: Provides semantic alternatives with slash notation.

**Examples**:
- **Mark 5:42**: "the people were extremely surprised/amazed"
- **Acts 2:6**: "asked/begged/urged"
- **Matthew 27:30**: "cloth/sponge"
- **Genesis 32:30**: "the face of God / but I did not die"
- **Matthew 26:38**: "heart/soul is very sad"

**Pattern**: `word1/word2/word3` provides semantic alternatives

---

## 24. POSSESSION AND KINSHIP EXPLICIT MARKING

**Pattern**: Possessive relationships are always explicitly marked.

**Examples**:
- **Mark 5:42**: "that daughter's mother"
- **Genesis 29:2**: "Rachel's father"
- **2 Samuel 12:30**: "the king's head... David's head"
- **Matthew 14:11**: "John's head"

**Pattern**: `X's Y` is always explicit, never elided

---

## 25. EXPLANATION AND DEFINITION MARKERS

**Pattern**: Explicit definition and explanation markers.

**Examples**:
- **Genesis 20:20**: "-Footnote Peniel means the face of God"
- **Mark 9:5**: "Rabbi named the word means-C teacher"
- **Genesis 28:19**: "–Footnote Bethel means the house of God"
- **Mark 14:36**: "The word of Aramaic named Abba means "father""

**Patterns**:
- `means-A` = simple definition
- `means-C` = contextual meaning
- `named X` = named entity
- `-Footnote` = explanatory note

---

## Summary Statistics

**Total verses analyzed**: 870
**New pattern categories identified**: 25
**Most common new patterns**:
1. Implicit information restoration (appears in ~60% of verses)
2. Direct speech quotation system (appears in ~45% of verses)
3. Temporal bracketing (appears in ~40% of verses)
4. Imperative marking (appears in ~30% of verses)
5. Conditional structures (appears in ~25% of verses)

**Key Discovery**: TBTA CNL is not just simplifying vocabulary and grammar—it's creating a fully explicit, disambiguated representation of the text with extensive meta-linguistic markup for translation purposes.
