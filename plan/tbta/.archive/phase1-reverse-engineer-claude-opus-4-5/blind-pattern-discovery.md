# TBTA Blind Pattern Discovery - Claude Opus 4.5

**Analysis Date**: 2025-12-02
**Data Source**: `/workspace/plan/tbta/phase1-policy/data/chunk-ag.tsv` (400 verses)
**Method**: Pure pattern discovery from verse transformations without reference to existing rules

---

## Pattern 1: Participant Disambiguation with Parenthetical Names/Roles
**Description**: Adds person names or roles in parentheses after pronouns to clarify who is being referenced
**Examples**:
- Matthew 16:18: "I(Jesus) tell you(Simon)"
- 1 Samuel 12:20: "You(Israelites) (imp) do not be afraid"
- Matthew 26:3: "Eli said, ['I(Eli) hope [that you(Hannah) have peace]]"
- Joshua 22:22: "Yahweh is our(people's) God"
- 2 Samuel 22:22: "will you(Yahweh) help [me(David) defeat the Philistines]"
**Frequency**: Appears in 95%+ of verses (nearly universal pattern)

---

## Pattern 2: Imperative Marker "(imp)"
**Description**: Marks imperative/command forms of verbs
**Examples**:
- 1 Samuel 12:20: "You(Israelites) (imp) do not be afraid"
- Matthew 5:39: "you(person) (imp) turn your(person's) left cheek"
- 1 Samuel 15:6: "You(Kenites) (imp) leave this place now"
- Joshua 4:3: "(imp) you(Joshua) tell [each man to get a large stone]"
- Matthew 26:18: "You(followers) (imp) go into the city"
**Frequency**: 40-50% of verses (very common in narrative/discourse)

---

## Pattern 3: Embedded Clause Bracketing with Square Brackets
**Description**: Uses nested square brackets to show clause relationships and dependencies
**Examples**:
- Matthew 16:18: "[you(Simon) are Peter]"
- 1 Samuel 1:17: "[that the God of Israel will give to you(Hannah) the things [that you(Hannah) asked God for]]"
- Joshua 21:10: "families [that were Aaron's descendants] [and that were Kohath's descendants]"
- Matthew 13:32: "plant [that is bigger than all _hyperbolic other plants [that grow in a garden]]"
**Frequency**: 90%+ of verses (nearly universal for complex sentences)

---

## Pattern 4: Underscore-Prefixed Annotation Tags
**Description**: Linguistic/semantic annotations starting with underscore to mark various features
**Examples**:
- Matthew 26:3: "_paragraph", "_adj"
- Matthew 13:15: "_implicitActiveAgent", "_implicitNecessary"
- Mark 6:7: "_implicit", "_implicitNecessary"
- Matthew 13:32: "_hyperbolic"
- Mark 4:19: "_implicit", "_madeOf"
- Matthew 15:37: "_satisfied _adj"
**Frequency**: 70-80% of verses

---

## Pattern 5: Literal/Dynamic Dual Translations
**Description**: Provides both literal word-for-word and dynamic meaning translations marked with "(literal)" and "(dynamic)"
**Examples**:
- Matthew 16:18: "(literal) And the gates of hell-B will not defeat-A that church-A. (dynamic) And the power of Satan will not defeat-A that church-A"
- Mark 4:19: "(literal) Those people are deceived by wealth. (dynamic) Those people are deceived by the idea [that more wealth will cause [those people to become happy]]"
- Matthew 13:22: "(literal) That person is deceived by wealth. (dynamic) That person thinks [that person will be happy [if that person has much wealth]]"
**Frequency**: 10-15% of verses

---

## Pattern 6: Complex/Simple Dual Translations
**Description**: Provides both complex and simplified versions of the same content marked with "(complex)" and "(simple)"
**Examples**:
- Matthew 13:33: "(complex) Jesus said, ['The kingdom-B of heaven is-U like the substance...'] (simple) Jesus said, ['The number of people [who become God's children] increases...]"
- Matthew 19:8: "(complex) Jesus answered, ['Moses allowed [you(Jews) to divorce...'] (simple) Jesus answered, ['Moses allowed [you(Jews) to divorce...']"
- Mark 10:47: "(complex) When you(Jesus) come in your(Jesus's) glory (simple) When you(Jesus) rule people from your(Jesus's) great/glorious throne"
**Frequency**: 5-8% of verses

---

## Pattern 7: Letter-Suffixed Semantic Disambiguation
**Description**: Adds letter suffixes (-A, -B, -C, etc.) to distinguish different senses or uses of the same word
**Examples**:
- Matthew 16:18: "church-A", "hell-B", "defeat-A"
- Mark 6:7: "called-A"
- Matthew 27:44: "heart-A" (likely metaphorical vs literal heart)
- Matthew 6:21: "heart-A", "treasure"
- Mark 11:33: "know-C", "gave-C", "tell-C", "Then-D"
**Frequency**: 25-30% of verses

---

## Pattern 8: Implicit Content Markers
**Description**: Marks content not explicitly stated but necessary for understanding, using various "_implicit" tags
**Examples**:
- Mark 6:7: "_implicitNecessary", "_implicit"
- Matthew 13:32: "_implicitActiveAgent"
- Matthew 5:39: "_implicit"
- Mark 4:19: "_implicit"
- Matthew 19:18: "_implicitDifferentNounIndex"
**Frequency**: 60-70% of verses

---

## Pattern 9: Footnote/Explanatory Notes
**Description**: Adds parenthetical footnotes to explain cultural, linguistic, or contextual details
**Examples**:
- Matthew 16:18: "(footnote) The Greek word named Peter means rock. The rock [that Jesus is talking about] means Peter, Jesus, or the words [that Peter said about Jesus]"
- Matthew 11:21: "(footnote) People _generic did these things _dual [in order to show those people [that people repented]]"
- Ruth 4:11: "(footnote) At that time people called Bethlehem Ephrathah"
**Frequency**: 5-10% of verses

---

## Pattern 10: Rhetorical/Statement Question Pairs
**Description**: Marks questions as rhetorical or provides both rhetorical and statement forms
**Examples**:
- Matthew 11:7: "(norhetorical) Jesus said, ['When you(people) went to the desert...'] (statement) Jesus said, ['you(people) did not go there...']"
- Matthew 6:27: "(rhetorical) Which person [that is among you(people)] is able... (statement) No person [who is among you(people)] is able..."
- Matthew 12:34: "(norhetorical) are you(Pharisees) [who _descriptive are evil] able [to say a good thing]? (statement) you(Pharisees) are not able..."
**Frequency**: 5-8% of verses

---

## Pattern 11: Metonymy Markers
**Description**: Marks metonymic expressions where one thing stands for another
**Examples**:
- Matthew 11:21: "Chorazin of people _metonymy"
- Matthew 14:1: "Herod of the soldiers _metonymy"
- Matthew 18:17: "the church of the leaders _metonymy"
- Matthew 23:37: "Jerusalem, Jerusalem, you(Jerusalem) kill the people/prophets"
**Frequency**: 3-5% of verses

---

## Pattern 12: Title Markers
**Description**: Uses "(title)" to mark section headings or narrative titles within the text
**Examples**:
- Acts 3:1: "Peter (title) helps a man [who is not able [to walk]]"
- Matthew 8:23: "(title) Jesus causes [a storm to end]"
- Mark 6:30: "(title) Jesus provides food for more than 5000 people"
- Genesis 47:24: "-Title Jacob wants [Joseph to bury Jacob in Canaan]"
**Frequency**: 8-12% of verses

---

## Pattern 13: Frame/Background Information Tags
**Description**: Marks information that provides contextual framing with "_frameInferable", "_frameInferable"
**Examples**:
- Mark 6:27: "you(followers) (imp) stay in that place [until you(followers) leave that town _frameInferable]"
- Mark 15:8: "the crowd _frameInferable came to Pilate _implicit"
- Matthew 27:17: "Pilate asked the people _frameInferable"
**Frequency**: 5-8% of verses

---

## Pattern 14: Episode/Paragraph Structure Markers
**Description**: Marks narrative structure with "_paragraph", "-beginepisode", and similar markers
**Examples**:
- Matthew 26:3: "_paragraph Then the chief _adj priests..."
- Matthew 8:23: "(paragraph) Then Jesus entered the boat"
- Genesis 28:10: "-beginepisode Jacob left Beersheba"
**Frequency**: 15-20% of verses

---

## Pattern 15: Alternative Expressions with "(alt)"
**Description**: Provides alternative ways to express the same concept
**Examples**:
- Nehemiah 9:12: "During each day you(Yahweh) led... During each day (alt) you(Yahweh) led our(people's) people with a tall cloud"
**Frequency**: 1-2% of verses

---

## Pattern 16: Temporal/Situational Context Tags
**Description**: Marks temporal significance or situational context
**Examples**:
- Mark 5:31: "During the nights and during the days _significantTime"
- Matthew 2:14: "During that night _significantTime"
- Acts 19:10: "every day for two years"
**Frequency**: 5-8% of verses

---

## Pattern 17: Noun Index Disambiguation
**Description**: Uses "_nounIndex2", "_differentNounIndex" to distinguish between multiple referents
**Examples**:
- Matthew 14:13: "people _nounIndex2 heard about the place... people _nounIndex2 followed-A Jesus"
- Matthew 19:18: "You(person) (imp) do not kill/murder a person _implicitDifferentNounIndex"
**Frequency**: 3-5% of verses

---

## Pattern 18: Semantic Role Markers ("is-U", "is-X", "be-U", "be-V")
**Description**: Marks the type of "is/be" relationship (metaphorical, identificational, etc.)
**Examples**:
- Matthew 13:33: "The kingdom-B of heaven is-U like the substance"
- Matthew 13:38: "The field is-X the earth"
- Matthew 13:22: "A person... is _be-U like the seeds"
- Matthew 10:25: "It is _be-V good-A"
**Frequency**: 8-12% of verses

---

## Pattern 19: Action Iteration/Frequency Markers
**Description**: Marks repeated actions or routine behaviors with "_routinely", "-iteration"
**Examples**:
- Mark 8:34: "And that person must follow-B _routinely me(Jesus)"
- Joshua 6:4: "you(soldiers) must walk around the city -iteration 7 times"
**Frequency**: 2-3% of verses

---

## Pattern 20: Descriptive/Attributive Clause Markers
**Description**: Uses "_descriptive" to mark relative clauses that provide description rather than restriction
**Examples**:
- Mark 14:44: "Judas _implicitNecessary, [_descriptive who was the man [who planned [to give Jesus to Jesus's enemies]]]"
- Matthew 12:34: "You(Pharisees) [who _descriptive are evil]"
**Frequency**: 3-5% of verses

---

## Pattern 21: Adverbial Modifiers with "_adv" and "_adj"
**Description**: Marks adverbial and adjectival modifications
**Examples**:
- Mark 7:37: "Jesus does all things well _adv"
- Matthew 15:37: "all the people were satisfied _adj"
- Matthew 26:3: "the chief _adj priests"
**Frequency**: 10-15% of verses

---

## Pattern 22: Possessive Cascading
**Description**: Shows ownership chains explicitly through repeated possessive constructions
**Examples**:
- 2 Samuel 3:5: "David's sixth son's name was Ithream. Ithream's mother's name was Eglah"
- Nehemiah 4:20: "Our(Nehemiah's) God of will fight for us(Nehemiah)"
**Frequency**: 5-8% of verses

---

## Pattern 23: First-Person as Third-Person Shift "_1stas3rd"
**Description**: Marks when Jesus refers to himself in third person as "Son of man"
**Examples**:
- Mark 13:32: "the Son-of-man _1stas3rd will return-B"
- Matthew 20:19: "the Son-of-man _1stAs3rd will be whipped"
**Frequency**: 2-3% of verses (specific to Gospel narratives)

---

## Pattern 24: Dual Gender/Number Forms "_dual"
**Description**: Marks when the text refers to two people or dual number
**Examples**:
- Matthew 20:23: "You(sons) _dual certainly will drink"
- Matthew 11:21: "these things _dual [in order to show...]"
**Frequency**: 1-2% of verses

---

## Pattern 25: Emphasis Markers "_emphasized"
**Description**: Marks emphatic constructions
**Examples**:
- Matthew 10:20: "the Holy-Spirit _emphasized of your(disciples') Father"
**Frequency**: 1-2% of verses

---

## Pattern 26: Time Unit Markers "(literalunits)" and "(modernunits)"
**Description**: Provides ancient and modern time equivalents
**Examples**:
- Matthew 27:45: "(literalunits) Between-C the 6th hour and the 9th hour (modernunits) Between-C 12PM and 3PM"
**Frequency**: 1-2% of verses

---

## Pattern 27: Slash-Separated Alternatives
**Description**: Shows alternative word choices or dual meanings with forward slashes
**Examples**:
- Matthew 16:18: "my(Jesus's) church-A... followers/disciples"
- Matthew 19:18: "steal things _implicit... say-B false things-C"
- Matthew 10:22: "follows _routinely me(Jesus)... saved by God _implicitActiveAgent from hell-A _implicit"
**Frequency**: 40-50% of verses

---

## Pattern 28: Passive Agent Marking "_implicitActiveAgent"
**Description**: Identifies the implicit agent in passive constructions
**Examples**:
- Matthew 13:32: "that seed is planted by a person _implicitActiveAgent"
- Matthew 11:21: "miracles were done by me(Jesus) _implicitActiveAgent"
- Matthew 27:22: "Jesus [who is called-C by people _implicitActiveAgent the Christ]"
**Frequency**: 20-25% of verses

---

## Pattern 29: Subaction/Background Action Tags
**Description**: Marks subsidiary or background actions with "(implicit-subaction)", "(implicit-background)"
**Examples**:
- Mark 10:49: "[(implicit-subaction) When Jesus heard Bartimaeus,] Jesus stopped walking"
- Matthew 2:1: "People (implicit-background) called that Herod the great Herod"
**Frequency**: 3-5% of verses

---

## Pattern 30: Situational/Contextual Implicature Tags
**Description**: Marks content inferable from situation/context with "(implicit-situational)", "(implicit-info)"
**Examples**:
- Mark 6:7: "[(implicit-situational) so that those groups... would teach God's message]"
- Matthew 5:39: "[(implicit-situational) so that that person could hit that cheek also]"
- 1 Samuel 30:63: "[After (implicit-info) David put-on those special clothes]"
**Frequency**: 25-30% of verses

---

## Pattern 31: Named Entity Clarifications
**Description**: Adds explanatory text for names and places with "named"
**Examples**:
- Matthew 26:18: "the city named Jerusalem _implicit"
- Genesis 28:10: "Esau [who was Esau's brother named Esau]"
- 1 Samuel 9:16: "the tribe named Benjamin"
**Frequency**: 50-60% of verses

---

## Pattern 32: Multiple Word-Sense Glosses
**Description**: Provides multiple meanings or cultural translations of the same term
**Examples**:
- Matthew 26:18: "celebrate-B Passover named the holiday/feast _implicitExplainName"
- Joshua 15:30: "People called Kiriath-Sannah Debir"
**Frequency**: 3-5% of verses

---

## Pattern 33: Pronoun Reflexive Marking "_reflexive"
**Description**: Explicitly marks reflexive pronoun usage
**Examples**:
- Mark 8:34: "that person must stop caring-B about only _implicit that person _reflexive"
- Mark 5:5: "that man was always _hyperbolic cutting that man _reflexive with stones"
**Frequency**: 2-3% of verses

---

## Pattern 34: Instrumental Argument Addition "_addInstrumentArg"
**Description**: Marks added instrumental role information
**Examples**:
- Mark 7:2: "eating food with _addInstrumentArg religious _implicit dirty/unclean hands"
**Frequency**: 1-2% of verses

---

## Pattern 35: Quantifier Scope Marking "_hyperbolic", "_modifiesOne"
**Description**: Marks hyperbolic quantifiers and scope of modification
**Examples**:
- Matthew 13:32: "smaller than all _hyperbolic other seeds"
- Mark 1:37: "All _hyperbolic the people are searching for you"
- Matthew 6:27: "even _modifiesOne one hour"
**Frequency**: 8-10% of verses

---

## Pattern 36: Gnomic/Generic Reference "_gnomic", "_generic"
**Description**: Marks generic or timeless statements
**Examples**:
- Nehemiah 9:5: "Yahweh [who is _gnomic wonderful/glorious]"
- Matthew 11:21: "People _generic did these things"
**Frequency**: 2-3% of verses

---

## Pattern 37: Exclusivity/Inclusivity Markers "_excl", "_incl"
**Description**: Marks whether "we" includes or excludes the addressee
**Examples**:
- Mark 10:47: "us(James) _excl sit beside you(Jesus)"
- Mark 4:38: "we(disciples) _incl will die soon"
- Matthew 25:39: "we(people) _excl care-A for you(Lord)"
**Frequency**: 8-12% of verses

---

## Pattern 38: LDV (Lexical Decomposition Vector) Markers "_inLDV", "_supplyInLDV"
**Description**: Marks lexically decomposed elements or supplies
**Examples**:
- Matthew 11:21: "ashes _inLDV on themselves"
- Mark 6:8: "things/supplies _supplyInLDV, except a stick/staff"
**Frequency**: 2-3% of verses

---

## Pattern 39: Adposition Time Markers "_Adp"
**Description**: Marks temporal adpositions
**Examples**:
- Mark 9:21: "These things started happening [when _Adp this boy was very young]"
**Frequency**: 1% of verses

---

## Pattern 40: Yes-Rhetorical Question Markers
**Description**: Marks rhetorical questions that expect "yes" answers vs those expecting "no"
**Examples**:
- Mark 4:38: "(yesrhetorical) are you(Jesus) worried [that we(disciples) _incl will die soon_implicit]?"
- Matthew 11:23: "(yesrhetorical) do you(people) think [you(people) will be brought by God...]?"
**Frequency**: 2-3% of verses

---

## Pattern 41: Suggestive "Let's" Constructions
**Description**: Marks suggestions with "_suggestiveLets"
**Examples**:
- Matthew 26:5: "we(priests) do not _suggestiveLets take-away/arrest Jesus during the holiday"
**Frequency**: <1% of verses

---

## Pattern 42: Moral/Religious Qualification "_morally", "_ritually"
**Description**: Distinguishes moral vs ritual concepts
**Examples**:
- Mark 2:7: "Who is able [to forgive bad _morally actions]"
- Mark 7:2: "religious _implicit dirty/unclean hands"
**Frequency**: 3-5% of verses

---

## Summary Statistics

**Universal Patterns (90%+ of verses):**
1. Participant disambiguation with parenthetical names/roles
2. Embedded clause bracketing

**Very Common Patterns (50-80% of verses):**
3. Underscore-prefixed annotation tags
4. Implicit content markers
5. Named entity clarifications
6. Slash-separated alternatives

**Common Patterns (20-50% of verses):**
7. Imperative markers
8. Letter-suffixed semantic disambiguation
9. Passive agent marking
10. Situational/contextual implicature tags

**Occasional Patterns (5-20% of verses):**
11. Adverbial/adjectival modifiers
12. Literal/dynamic dual translations
13. Title markers
14. Semantic role markers (is-U, is-X, be-U)
15. Paragraph/episode structure markers
16. Possessive cascading
17. Temporal/situational context tags

**Rare Patterns (<5% of verses):**
18. Complex/simple dual translations
19. Rhetorical/statement question pairs
20. Metonymy markers
21. Multiple remaining specialized tags

**Total Distinct Patterns Identified**: 42 major patterns with numerous sub-variations
