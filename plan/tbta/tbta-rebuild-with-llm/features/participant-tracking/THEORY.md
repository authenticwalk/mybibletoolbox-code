# Participant Tracking: Theoretical Foundations

This document provides detailed linguistic foundations for TBTA's participant tracking system.

## Core Theoretical Frameworks

### 1. Ariel's Accessibility Theory (1990)

**Principle**: Referring expressions vary along an accessibility scale from LOW to HIGH accessibility.

```
LOW ACCESSIBILITY                                    HIGH ACCESSIBILITY
│                                                                      │
Full name → Long definite description → Short definite description →
Last name → First name → Distal demonstrative → Proximate demonstrative →
Stressed pronoun → Unstressed pronoun → Clitic pronoun → ZERO (null)
```

**Key Insight**: High accessibility markers = less linguistic material, signal continued activation.

**Mapping to TBTA States**:
- First Mention → Full NP (low accessibility)
- Integration → Short definite description
- Routine → Unstressed pronoun / zero (high accessibility)
- Restaging → Full NP or demonstrative (reactivation = lower accessibility)
- Frame Inferable → Definite NP (accessible via frame, not prior mention)

**Reference**: Ariel, Mira (1990). *Accessing Noun-Phrase Antecedents*. Routledge.

---

### 2. Gundel's Givenness Hierarchy (1993)

**Six cognitive statuses for referents**:

```
IN FOCUS → ACTIVATED → FAMILIAR → UNIQUELY IDENTIFIABLE →
REFERENTIAL → TYPE IDENTIFIABLE
```

**Form-Status Correlations**:
- In focus: it, that, Ø (zero)
- Activated: this, that, this N
- Familiar: that N
- Uniquely identifiable: the N
- Referential: indefinite this N
- Type identifiable: a N

**Mapping to TBTA States**:
- Routine → In Focus / Activated
- Frame Inferable → Uniquely Identifiable (via frame)
- First Mention → Type Identifiable / Referential
- Restaging → Familiar (previously mentioned but not currently activated)

**Reference**: Gundel, Jeanette K., Nancy Hedberg, & Ron Zacharski (1993). "Cognitive Status and the Form of Referring Expressions in Discourse." *Language* 69: 274-307.

---

### 3. Givón's Topic Continuity (1983)

**Three quantitative measures**:

**Referential Distance (RD)**:
- Gap between current mention and previous mention of same referent
- Counted in number of clauses
- RD = 1 clause → Maximum continuity (TBTA "Routine")
- RD = 3+ clauses → Topic shift, requires reactivation (TBTA "Restaging")

**Potential Interference (PI)**:
- Counts competing referents in discourse between mentions
- More interference → More explicit marking needed

**Persistence (PS)**:
- How long referent remains topic after current mention
- Indicates topic importance and likely encoding

**Cross-linguistic Principle**:
> More continuous topics → Less linguistic material
> Less continuous topics → More linguistic material

**Languages studied**: English (written/spoken), Spanish (spoken), Biblical Hebrew, Amharic, Hausa, Japanese, Chamorro, Ute

**Biblical Hebrew Findings** (Floor 2010):
- Subject continuity is primary tracking mechanism
- Pronouns can be dropped (pro-drop language)
- Uses word order and verb morphology for tracking
- "Referential continuity predominantly hinges on subject continuity"

**References**:
- Givón, Talmy (ed.) (1983). *Topic Continuity in Discourse: A Quantitative Cross-language Study*. Amsterdam: John Benjamins.
- Floor, Sebastian J. (2010). "Participant Tracking in Biblical Hebrew and Obligatory Explicitation of Anaphors in Translation." *The Bible Translator* 61(4): 183-196.

---

### 4. Fillmore's Frame Semantics (1982)

**Core Concept**: Certain words evoke "frames" - structured knowledge about situations. When a frame is evoked, its typical participants become inferrable.

**Frame-Participant Relationships**:
- "Restaurant" frame → waiter, menu, food, check
- "Market" frame → vendors, customers, goods, prices
- "Wedding" frame → bride, groom, guests, ceremony
- "Well" frame → water, bucket, rope, drawing
- "Temple" frame → priest, altar, sacrifice, incense

**Bridging Anaphora**: Frame inferability relates to "bridging reference" (Clark 1977) where referents link to antecedents via:
- Lexico-semantic relations
- Frame relations
- Encyclopedic knowledge

**Example**: "John went to a restaurant. **The waiter** was rude."
→ "The waiter" is frame-inferable from "restaurant" despite not being previously mentioned.

**Biblical Context**: In Genesis 1:1, "sky" (heaven) and "earth" are frame-inferable from the "creation" frame evoked by "In the beginning."

**Computational Integration**: Modern NLP systems integrate FrameNet encyclopedic knowledge into discourse representation to resolve bridging anaphora (Hou 2013).

**References**:
- Fillmore, Charles J. (1982). "Frame Semantics." In *Linguistics in the Morning Calm*, 111-137. Seoul: Hanshin.
- Clark, Herbert H. (1977). "Bridging." In *Thinking: Readings in Cognitive Science*, 411-420. Cambridge: Cambridge University Press.
- Hou, Yufang (2013). *Unrestricted Bridging Resolution*. Dissertation, Heidelberg University.
- Baker, Collin F., Charles J. Fillmore, & John B. Lowe (1998). "The Berkeley FrameNet Project." *COLING-ACL*.

---

### 5. Hopper's Grounding Theory (1979)

**Core Distinction**: Foreground vs. Background in narrative

**Foreground**:
- Events on the "main line" of narrative
- Moves the story forward
- Encoded with action verbs, perfective aspect
- TBTA: Routine participants typically in foreground

**Background**:
- Supportive material
- Sets scene, provides context, evaluates events
- Encoded with stative verbs, imperfective aspect
- TBTA: Offstage participants, frame inferables in background

**Application to Participant Tracking**:
- Foreground participants require active tracking (First Mention → Routine → Restaging)
- Background participants may remain offstage or frame-inferable
- Generic statements are often in background, providing supporting information

**References**:
- Hopper, Paul J. (1979). "Aspect and foregrounding in discourse." In T. Givón (ed.), *Discourse and Syntax*, 213-241. New York: Academic Press.
- Hopper, Paul J. & Sandra A. Thompson (1980). "Transitivity in grammar and discourse." *Language* 56: 251-299.

---

## Cross-linguistic Typology

### Switch-Reference Systems

**Geographic Distribution**: Primarily Papua New Guinea (40+ language families), also Amazonian languages

**Function**: Morphemes at clause junctures indicate whether subjects corefer:
- **SS (Same Subject)**: Subjects corefer → Participant continuity
- **DS (Different Subject)**: Subjects differ → Participant shift

**Example (Hypothetical)**:
> "John came-SS ate." → John came and [John] ate
> "John came-DS Mary ate." → John came and Mary ate

**Relevance to TBTA**:
- SS marking ≈ Routine participant tracking
- DS marking ≈ Shift to different participant (possibly Restaging or First Mention)

**Key Languages**:
- **Iatmul** (Papua New Guinea): Zero-marked switch-reference, primary function is participant tracking
- **Wojokeso** (Papua New Guinea)
- **Guanano** (Northern South America)
- **Cavineña** (Amazonian, Bolivia): Switch-reference participates in tail-head linkage for participant coherence

**References**:
- Roberts, John R. (1997). "Switch-reference in Papua New Guinea." In A. Pawley (ed.), *Papers in Papuan Linguistics* No. 3, 101-241. Canberra: Pacific Linguistics.
- Longacre, Robert E. (1983). "Switch reference systems in two distinct linguistic areas." In *Switch Reference and Universal Grammar*, 185-207. Amsterdam: John Benjamins.

---

### Zero Anaphora / Pro-drop Languages

**Two Pro-drop Types**:

**Type 1: Null subject languages with rich agreement** (Spanish, Italian, Portuguese)
- Verbal inflection identifies subject
- Pronouns dropped when recoverable from verb
- Example (Spanish): "Ø Habló" = "[He/She] spoke" (person marked on verb)

**Type 2: Discourse pro-drop languages** (Japanese, Korean, Chinese, Vietnamese)
- No verbal agreement
- Pronouns dropped based on discourse context
- Topic-prominent languages
- Extensive zero anaphora for both subjects and objects

**Relevance to TBTA**:
- Routine participants in these languages → Often zero anaphora
- Surface Realization would be "Ø" (null) rather than explicit pronoun/noun
- Tracking state (Routine) remains same, but linguistic encoding differs

**Chinese Example**:
> "张三来了。Ø 吃了饭。"
> "Zhang San came. [Ø] ate food."
> → Second sentence has zero subject referring to Zhang San (Routine tracking)

**Japanese Example**:
> "太郎が来た。Ø ご飯を食べた。"
> "Taro came. [Ø] ate meal."
> → Zero subject in second sentence (Routine tracking)

**Topic-Prominent vs Subject-Prominent**:
- **Subject-Prominent** (English, German, French): Require explicit subjects
- **Topic-Prominent** (Japanese, Chinese, Korean): Allow extensive ellipsis

**References**:
- Huang, Yan (2000). *Anaphora: A Cross-linguistic Study*. Oxford: Oxford University Press.
- Li, Charles N. & Sandra A. Thompson (1976). "Subject and Topic: A New Typology of Language." In C. Li (ed.), *Subject and Topic*, 457-489. New York: Academic Press.

---

### Definiteness and Article Systems

**English-type** (Definite/Indefinite distinction):
- First Mention: "a woman"
- Routine/Frame Inferable: "the woman"

**Mandarin Chinese** (No articles):
- Uses bare nouns
- Context and word order indicate referential status
- Topic markers (是 shì, 吗 ma) for emphasis

**Arabic** (Definite article al-):
- Uses definite article more liberally than English
- Can mark both specific and generic reference with al-
- "al-mar'a" (the-woman) can be generic or specific

**Biblical Hebrew** (Definite article ha-):
- Similar to Arabic in some uses
- Can mark first mentions in narrative contexts
- Definiteness interacts with discourse tracking in complex ways

**Slavic Languages** (Russian, Polish - No articles):
- Use word order and case marking
- Definiteness implied by context
- Topic-comment structure indicates tracking status

---

## Generic Reference Theory

**Fundamental Distinction**: Generic vs. specific reference operates on different cognitive levels.

**Generic Reference Properties**:
- Makes claims about entire categories
- Not tracked as individual participants in narrative
- Timeless, not anchored to specific discourse contexts

**Generic Uses** (Krifka et al. 1995):
- Definitions and explanations
- Proverbial wisdom
- Scientific/technical descriptions
- Habitual or characteristic properties

**Cross-linguistic Variation**:

**English**: Three forms for generic reference:
- Definite singular: "The lion is a mammal"
- Indefinite singular: "A lion is a mammal"
- Bare plural: "Lions are mammals"

**Mandarin Chinese**: Uses bare nouns; generic noun phrases occur ~2.5x less frequently than in English (Cimpian 2012)

**French/Hungarian/Greek**: Classified as "DISCOURSE REFERENT-marking languages" which handle generics differently than English's "QUALITY-marking" system (Heyer 1990)

**References**:
- Krifka, Manfred et al. (1995). "The Generic Book" (Reference Manual).
- Cimpian, Andrei et al. (2012). "A cross-linguistic comparison of generic noun phrases in English and Mandarin." *Cognition* 124: 269-280.
- Heyer, Gerhard (1990). "Genericity from a Cross-Linguistic Perspective." In *Semantics and Contextual Expression*, 95-130.

---

## Complete Bibliography

1. **Ariel, Mira (1990)**. *Accessing Noun-Phrase Antecedents*. Routledge.

2. **Gundel, Jeanette K., Nancy Hedberg, & Ron Zacharski (1993)**. "Cognitive Status and the Form of Referring Expressions in Discourse." *Language* 69: 274-307.

3. **Givón, Talmy (ed.) (1983)**. *Topic Continuity in Discourse: A Quantitative Cross-language Study*. Amsterdam: John Benjamins.

4. **Hopper, Paul J. (1979)**. "Aspect and foregrounding in discourse." In T. Givón (ed.), *Discourse and Syntax*, 213-241. New York: Academic Press.

5. **Hopper, Paul J. & Sandra A. Thompson (1980)**. "Transitivity in grammar and discourse." *Language* 56: 251-299.

6. **Floor, Sebastian J. (2010)**. "Participant Tracking in Biblical Hebrew and Obligatory Explicitation of Anaphors in Translation." *The Bible Translator* 61(4): 183-196.

7. **Huang, Yan (2000)**. *Anaphora: A Cross-linguistic Study*. Oxford: Oxford University Press.

8. **Li, Charles N. & Sandra A. Thompson (1976)**. "Subject and Topic: A New Typology of Language." In C. Li (ed.), *Subject and Topic*, 457-489. New York: Academic Press.

9. **Fillmore, Charles J. (1982)**. "Frame Semantics." In *Linguistics in the Morning Calm*, 111-137. Seoul: Hanshin.

10. **Clark, Herbert H. (1977)**. "Bridging." In P.N. Johnson-Laird & P.C. Wason (eds.), *Thinking: Readings in Cognitive Science*, 411-420. Cambridge: Cambridge University Press.

11. **Hou, Yufang (2013)**. *Unrestricted Bridging Resolution*. Dissertation, Heidelberg University.

12. **Roberts, John R. (1997)**. "Switch-reference in Papua New Guinea." In A. Pawley (ed.), *Papers in Papuan Linguistics* No. 3, 101-241. Canberra: Pacific Linguistics.

13. **Longacre, Robert E. (1983)**. "Switch reference systems in two distinct linguistic areas." In J. Haiman & P. Munro (eds.), *Switch Reference and Universal Grammar*, 185-207. Amsterdam: John Benjamins.

14. **Cimpian, Andrei & Erika R. Cadena (2012)**. "A cross-linguistic comparison of generic noun phrases in English and Mandarin." *Cognition* 124: 269-280.

15. **Ferré, Gaïane et al. (2018)**. "Referential Choices in a Collaborative Storytelling Task: Discourse Stages and Referential Complexity Matter." *Frontiers in Psychology* 9: 176.

16. **Krifka, Manfred et al. (1995)**. "The Generic Book" (Reference Manual).

17. **Baker, Collin F., Charles J. Fillmore, & John B. Lowe (1998)**. "The Berkeley FrameNet Project." *COLING-ACL*.
