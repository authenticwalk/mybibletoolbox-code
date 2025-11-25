# Key Learnings: Surface Realization in Bible Translation

## Critical Discoveries

### 1. Pro-Drop is the Default for Most of the World's Spoken Languages

**Finding:** Approximately 70% of world languages allow some form of subject pro-drop. However, the degree and constraints vary dramatically.

**Impact:** Bible translators working into the majority of the world's languages must navigate pro-drop rules that don't exist in English or Greek source material.

**Pattern Recognition:**
- **East Asian languages** (Chinese, Japanese, Korean): Near-complete pro-drop
- **Romance languages** (Spanish, Portuguese, Italian): Subject pro-drop required
- **Slavic languages**: Limited to 3rd person or specific contexts
- **Germanic languages** (English, German, Dutch): Essentially no pro-drop
- **Pacific/Austronesian** (176 languages in our TSV): Highly variable, often focus-driven

### 2. Pro-Drop is About More Than Just Deleting Pronouns

**Finding:** Surface realization decisions involve a complex interaction of:
- Language-specific syntactic rules (what CAN drop)
- Discourse factors (what SHOULD drop)
- Pragmatic appropriateness (what FEELS natural)
- Register constraints (formal vs informal)
- Narrative flow requirements

**Critical Insight:** A translator cannot mechanically apply a "drop subjects when mentioned in prior clause" rule. Each language has unique conventions about when zero subjects feel natural vs awkward.

**Examples:**
- Spanish: Can drop all persons; "voy" = "I'm going" (1st person singular present)
- Russian: Only drops 3rd person; "pришли" = "they came" (3rd person plural past)
- Japanese: Drops all persons in appropriate discourse contexts, including objects
- English: Cannot drop subjects even with rich agreement markers

### 3. The Canonical Pro-Drop Hierarchy

**Finding:** When languages allow pro-drop, they follow predictable patterns:

```
Subject drop > Object drop
1st person > 2nd person > 3rd person (within subjects)
Main clauses > Embedded clauses
Animate > Inanimate subjects
```

**Application:** If a language allows object drop, it definitely allows subject drop. If it allows 2nd person drop, it allows 1st person drop.

**Translation Implication:** Understanding this hierarchy helps predict where pro-drop will be natural in untested languages.

### 4. Clitics Create New Translation Challenges

**Finding:** Romance languages with obligatory clitic pronouns (especially Spanish, French, Italian) require fundamentally different translation strategies than non-clitic languages.

**The Problem:**
```
English source: "He told them the truth"
English structure: [Subject Verb Object] = SVO

Spanish requirement: "Les dijo la verdad"
Spanish structure: [Clitic Verb Object] = CLV-O
```

The clitic is obligatory; you cannot say "Dijo a ellos la verdad" for this meaning. The clitic "les" (to-them) must appear on the verb.

**Impact on Bible Translation:**
- Word order changes from source language
- Clitics may be ambiguous in certain contexts
- Double clitics create stacking rules ("Se la dijo" = to-him/her-it-said)
- Reflexive vs non-reflexive clitics matter ("se" can mean "himself/herself/themselves")

**Data Point:** Spanish, Italian, Portuguese, French, Romanian, and Modern Greek all have obligatory clitic systems relevant to our TSV languages.

### 5. Information Structure Drives Surface Realization More Than Grammar

**Finding:** Whether something appears as noun, pronoun, or zero is ultimately about information structure:
- **Noun**: Used to introduce new, important information
- **Pronoun**: Used for accessible, non-salient information
- **Zero**: Used for highly salient, topical information

**The Discourse Trajectory:**
```
Introduction:    "A man came to the well"           [Noun - NEW]
Continued reference: "He drew water"               [Pronoun - GIVEN]
Established topic: "went home"                     [Zero - TOPIC - pro-drop only]
Return to story:  "Jesus asked the man about..."   [Noun - SHIFT FOCUS]
```

**Language-Specific Patterns:**
- **Topic-prominent languages** (Japanese, Korean, Chinese): Zero use is extensive and depends on topic status
- **Subject-prominent languages** (English, German): Limited zero; depend on subject role
- **Focus-prominent languages** (some Austronesian, Filipino): Realization depends on focus structure

**Translator Challenge:** Must understand both the grammar (what CAN happen) and the pragmatics (what SHOULD happen) of your language.

### 6. Bible Discourse Has Specific Characteristics That Affect Realization

**Finding:** Biblical narrative and epistolary discourse have patterns that interact uniquely with pro-drop systems:

#### Pattern A: Character Introduction Requires Nouns
- Genesis, gospels, epistles all introduce new characters
- These ALWAYS require noun forms initially
- Pro-drop languages accept zero after introduction
- Non-pro-drop languages must use pronouns after initial noun

#### Pattern B: Direct Speech Creates Pronoun/Noun Shifts
- Direct discourse ("He said: 'I will go'") has different realization patterns than reported discourse
- Within a speaker's words, they use pronouns/zero for themselves
- In reported speech attribution, the original speaker appears as noun/pronoun based on discourse context

#### Pattern C: Repeated Actions Favour Zero in Pro-Drop Languages
- Many biblical passages have repeated actions
- "He walked. [∅ Taught]. [∅ Healed]. [∅] spoke..." (in pro-drop languages)
- English must use pronouns: "He walked. He taught. He healed. He spoke..."
- Creates very different stylistic effects

#### Pattern D: Theological Emphasis Often Requires Explicit Forms
- When theology emphasizes an agent, pronouns/nouns are preferred
- When theology is subtle or ambiguous, zero realization can work
- Translators may need to choose between grammaticality and theological clarity

### 7. Zero Anaphora in Complex Clauses Creates Ambiguity

**Finding:** Pro-drop languages can create genuine ambiguity in complex clause structures where English requires explicit subjects.

**Example Problem:**
```
Greek/Source: "When John heard about Jesus, he went to tell Peter"
Ambiguity: Does "he" = John or someone else?

Spanish: "Cuando Juan oyó a Jesús, fue a decirle a Pedro"
Ambiguity: Does "fue" (went) = Juan or someone else?

English: "When John heard about Jesus, he went to tell Peter"
Clear: "he" = John

Pro-drop language solution: Context must make it clear from discourse.
```

**Translator Implication:** Pronoun resolution must be unambiguous, even in pro-drop languages. Sometimes an explicit pronoun is needed for clarity even though zero would be grammatical.

### 8. Language Families Show Consistent Patterns

#### Austronesian Pattern (176 languages in our TSV)
- Most allow subject drop
- Many have focus systems that interact with realization
- Some (like Tagalog) have verbal focus marking that affects what can drop
- Moderate to high variation within the family

#### Trans-New Guinea Pattern (141 languages in our TSV)
- Highly diverse
- Many use clause-chaining with medial-clause subjects that follow special rules
- Switch-reference systems interact with pro-drop
- High complexity; individual language analysis required

#### Indo-European Pattern (135 languages in our TSV)
- **Romance sub-family**: Subject drop required for naturalness
- **Slavic sub-family**: Limited drop; clitics common
- **Germanic sub-family**: Non-pro-drop is standard
- **Greek**: Subject drop allowed
- **Balkan languages**: Complex clitic systems

#### Niger-Congo Pattern (89 languages in our TSV)
- Highly variable
- Bantu languages: Generally non-pro-drop; noun class systems provide tracking
- Requires individual language investigation

### 9. The Agreement Morphology Connection

**Finding:** Languages with rich agreement morphology (many Slavic, Romance, many indigenous languages) can afford pro-drop because the verb carries person/number information.

**The Pattern:**
```
Spanish: (yo) hablo = I speak [1sg marker on verb]
         (tú) hablas = you speak [2sg marker]
         (él) habla = he speaks [3sg marker]
→ Subject pronouns are often redundant; pro-drop is natural

English: I speak, you speak, he speaks [SAME form "speak" for all]
→ Subject pronouns are necessary; pro-drop is ungrammatical
```

**Implication:** If your target language has rich verb agreement, pro-drop is likely natural. If verb morphology is impoverished, pro-drop may be ungrammatical or rare.

### 10. Clitic Systems Create Obligatory Realization

**Finding:** In clitic languages, objects have obligatory surface realization (as clitics), while subjects may optionally drop.

**Spanish Example:**
```
Verb: "dar" (to give)
"Doy" = I give (subject drops, implicit in agreement)
"Le doy" = (to-him) I-give (object is CLITIC, mandatory)

You cannot say "* Doy su libro a él" for the meaning "(I) give him the book"
You MUST say: "Le doy el libro" (literally: to-him I-give the book)
Or with double clitic: "Se lo doy" (to-him-it I-give)
```

**Bible Translation Problem:** Clitics must appear in certain positions (before or after verb, depending on language). This restricts word order and can create unusual emphasis patterns compared to source languages.

### 11. Narrative Discourse Conventions Vary

**Finding:** Different language communities have different conventions for how to narrate stories, and these affect surface realization choices.

**Pattern A: High-continuity Narrative** (common in pro-drop languages):
- Main character can remain zero across multiple clauses
- Readers expect topic continuity
- Frequent reintroduction of secondary characters as nouns
- Example: Classical Chinese, Old Japanese narrative style

**Pattern B: Low-continuity Narrative** (common in non-pro-drop languages):
- Every subject is explicit
- Creates less ambiguity
- More "breathing room" stylistically
- Example: English biblical narrative tradition

**Pattern C: Switching Narrative Style** (common in modern languages influenced by English):
- Young translations may overuse pronouns (influenced by English source translations)
- Mature translations develop pro-drop more naturally as native translator preferences emerge
- Spanish Bible translations show this evolution (earlier: more explicit subjects; modern: more natural pro-drop)

### 12. Register and Formality Create Realization Variation

**Finding:** Within the same language, register affects surface realization choices significantly.

**Formal Written:**
- More explicit nouns
- More pronouns
- Fewer zeros (even in pro-drop languages)
- Clearer for non-native readers

**Informal Spoken:**
- More zeros
- More pronouns in some contexts
- Faster reference resolution
- More natural to native speakers

**Religious/Scriptural Register:**
- Varies by language and tradition
- Some languages use formal registers for Bible
- Others use natural spoken language
- Affects surface realization patterns

## Translation Implications and Strategies

### For Non-Pro-Drop Translators (English, German, etc.)
1. You cannot preserve source language zero subjects
2. You must explicitly state or pronominalize every subject
3. Use pronouns to maintain flow; avoid constant noun repetition
4. Track participants carefully to avoid ambiguity

### For Pro-Drop Translators (Spanish, Portuguese, Japanese, etc.)
1. You can use zero for established topics
2. Track when to introduce with nouns vs. maintain with zero
3. Use pronouns for emphasis or clarity
4. Watch for unintended ambiguity

### For Clitic-Based Translators (Spanish, French, Italian, etc.)
1. Obligatory clitics will change word order from source
2. Double clitics require special handling
3. Clitic placement rules (before/after verb) matter
4. Emphasis and word order may differ from source language

### For Complex Pro-Drop Translators (Japanese, Korean, Austronesian, etc.)
1. Study your language's topic vs. comment structure
2. Learn the distance constraints (how far can zero reach?)
3. Understand the interaction with focus/voice systems
4. Test naturalness with native speakers

## Common Translator Mistakes

### Mistake 1: Mechanical Pro-Drop Application
**Wrong:** "If a noun appears in the previous sentence, always drop the pronoun in the next"
**Right:** Follow your language's actual conventions for what "feels" natural

### Mistake 2: Over-Pronominalization in Pro-Drop Languages
**Wrong:** Translating English word-for-word, using pronouns instead of zeros
**Right:** Use zeros where your language naturally does; use pronouns for emphasis

### Mistake 3: Ignoring Register Differences
**Wrong:** Using casual pro-drop patterns in formal Bible text or vice versa
**Right:** Match your source text's register in your target language

### Mistake 4: Forgetting about Clitics
**Wrong:** Not using clitic forms in languages that require them
**Right:** Follow your language's clitic system rules for objects

### Mistake 5: Creating Ambiguity
**Wrong:** Using zero when the antecedent is unclear
**Right:** Use explicit nouns/pronouns when necessary for clarity, even if zero is grammatical

### Mistake 6: Inconsistent Participant Tracking
**Wrong:** Sometimes using noun, sometimes pronoun, sometimes zero with no pattern
**Right:** Develop a consistent strategy for each participant based on their discourse status

## Open Questions for Tool Development

1. **Automatic pro-drop detection**: How can we predict surface realization without language-specific rules?
2. **Ambiguity detection**: How can we identify where zero realization might create unwanted ambiguity?
3. **Language family generalization**: Can we use patterns from related languages to predict pro-drop?
4. **Register modeling**: How do we model formal vs. informal surface realization patterns?
5. **Clitic prediction**: Can we predict clitic placement across Romance languages?
6. **Discourse tracking**: How do we maintain accurate antecedent tracking across extended discourse?

## Experimental Direction

### Phase 1: Language-Specific Analysis
- Deep dive into 3-4 major language groups (Romance, East Asian, Austronesian, TNGLanguages)
- Document exact pro-drop rules and constraints
- Create verb form/agreement tables
- Test on sample Bible verses

### Phase 2: Cross-Language Patterns
- Compare patterns across language families
- Identify universal constraints (pro-drop hierarchy)
- Create predictive models for zero realization
- Test on previously unseen verses

### Phase 3: Tool Integration
- Integrate pro-drop prediction into translation workflow
- Test with actual translators
- Refine based on native speaker feedback
- Measure improvement in naturalness/accuracy

### Phase 4: Complex Cases
- Handle switch-reference interactions
- Model topic/focus interactions with pro-drop
- Develop clitic handling for Romance languages
- Create register-specific variants

## Key Metrics for Success

1. **Naturalness**: Native speakers rate translations as natural (7/10 or higher)
2. **Accuracy**: Zero/pronoun choices match native speaker expectations (80%+ agreement)
3. **Consistency**: Same participants use consistent realization patterns
4. **Clarity**: Ambiguity rates remain low even with extended pro-drop
5. **Register match**: Formal/informal choices match source text register

## Conclusion

Surface Realization is fundamentally about understanding how languages encode discourse, participant tracking, and information structure. Pro-drop is not just a grammatical feature; it's a window into how different languages think about information structure, participant tracking, and narrative flow. Successful Bible translation requires mastering these patterns in your specific language community.
