# Learnings: Reproducing TBTA's Verb TAM Annotation

## Initial Thesis

Based on comprehensive research into TBTA's verb annotation system and cross-linguistic TAM theory, this document outlines a methodology for reproducing TBTA's temporal, aspectual, and modal annotation decisions.

---

## Core Challenge

**The fundamental challenge**: Biblical source texts (Hebrew Old Testament, Greek New Testament) must be annotated with TAM features in a way that:

1. **Captures source language semantics** accurately
2. **Enables transfer** to 7,000+ target languages with diverse TAM systems
3. **Preserves discourse structure** and pragmatic meaning
4. **Is computationally tractable** for automatic generation

This requires creating a **language-neutral semantic representation** that abstracts away from source language morphology while preserving meaningful distinctions.

---

## Thesis: Four-Stage Annotation Process

### Stage 1: Source Language Analysis (Linguistic Analysis)

**Input**: Raw Greek/Hebrew verb form in context

**Process**: Apply source language grammar rules to extract:

- **Morphological features**: Tense/aspect form, mood, voice, person, number
- **Lexical semantics**: Aktionsart (lexical aspect) of verb root
- **Syntactic context**: Clause type, subordination, discourse role
- **Pragmatic context**: Genre (narrative, prophecy, law, wisdom, etc.), speaker perspective

**Example (Greek)**:
- Form: *ἐποίησεν* (epoiēsen)
- Morphology: Aorist indicative active, 3rd singular
- Lexis: ποιέω (poieō) = "make, do" (activity verb, telic)
- Syntax: Main clause, narrative backbone
- Pragmatics: Historical narrative, completed event

### Stage 2: Semantic Mapping (Universal Semantics)

**Input**: Source language analysis

**Process**: Map to TBTA's semantic features using linguistic theory:

#### 2.1 Time Feature Mapping

**Principle**: Determine temporal distance from discourse reference point

**For Greek/Hebrew narrative**:
- Source verb in narrative past → Determine event distance from narrative "now"
- Cross-reference with temporal adverbs, discourse markers
- Consider genre:
  - Historical narrative → likely codes h (Historic Past) or g (Speaker's Lifetime)
  - Creation accounts → likely code i (Eternity Past)
  - Prophetic perfect → may be r (Discourse) or near future codes
  - Gnomic statements → code T (Timeless)

**For Greek/Hebrew direct discourse**:
- Establish deictic center (speaker's "now")
- Calculate temporal distance from deictic center
- Use adverbial cues: "today" → A/r/F, "tomorrow" → j, "yesterday" → a
- Default: If unspecified past → q (Unknown Past), if unspecified future → p (Unknown Future)

**Key insight**: Greek/Hebrew often DON'T specify fine temporal distinctions (they're aspect-prominent), so TBTA must **infer** from context. This requires:
- Lexical database of temporal adverbs and their meanings
- Discourse analysis to track timeline
- Genre-specific defaults

#### 2.2 Aspect Feature Mapping

**Principle**: Interpret source aspect + Aktionsart in context

**Greek aorist** in narrative:
- Default → U (Unmarked) or C (Completive) depending on verb class
- Ingressive aorist → N (Inceptive) - "began to do"
- Effective aorist → C (Completive) - "accomplished, completed"
- Constative aorist → U (Unmarked) - simple past

**Greek present**:
- Progressive → o (Continuative) - "is doing"
- Habitual → H (Habitual) - "does regularly"
- Gnomic → G (Gnomic) - "always true"
- Historical present → context-dependent (likely U or o)

**Greek perfect**:
- Typically → C (Completive) with resulting state
- May interact with time coding (recent past?)

**Greek imperfect**:
- Typically → I (Imperfective) or o (Continuative)
- Iterative imperfect → H (Habitual) or R (Routinely)
- Inceptive imperfect → N (Inceptive) - "was beginning to"

**Hebrew Qatal**:
- In narrative sequential chain → likely U (Unmarked) perfective
- Stative verbs → may be o (Continuative) or H (Habitual)
- With temporal adverbs → adjust based on context

**Hebrew Yiqtol**:
- Modal contexts → maps to mood, aspect may be U
- Habitual → H (Habitual)
- Future → aspect depends on Aktionsart

**Aktionsart (lexical aspect) considerations**:

| Verb Class | Examples | Typical Aspect Coding |
|------------|----------|----------------------|
| States | "know," "love," "be" | I (Imperfective), o (Continuative), or U |
| Activities | "walk," "sing" | o (Continuative), I (Imperfective) |
| Accomplishments | "build a house" | C (Completive) when done, o (Continuative) ongoing |
| Achievements | "arrive," "die," "notice" | N (Inceptive) or U (Unmarked) |
| Semelfactives | "knock," "cough" | U (Unmarked) for single, R/H for repeated |

**Phasal marking**:
- Verbs with "begin to" → N (Inceptive)
- Verbs with "finish," "complete" → C (Completive)
- Verbs with "stop," "cease" → c (Cessative)

**Key insight**: Source languages DON'T always distinguish all these aspects morphologically. TBTA must use:
- Verb lexicon with Aktionsart classification
- Compositional semantics (verb + object + adverbs)
- Discourse context (narrative progression, background info)

#### 2.3 Mood Feature Mapping

**Principle**: Distinguish realis (indicative) from irrealis (potential, obligation, etc.)

**Greek indicative** → I (Indicative) - assertion of fact

**Greek subjunctive**:
- Conditional protasis → epistemic potential (likely c 'might')
- Purpose clauses → may map to obligation or potential depending on strength
- Deliberative subjunctive → b or c (potential)
- Hortatory subjunctive → g or f (obligation)

**Greek optative**:
- Wishes → typically d (Unlikely Potential) or c (Might)
- Potential optative → c or d depending on context

**Greek imperative**:
- Positive command → f ('must' Obligation) or g ('should' Obligation)
- Negative command (μή + subjunctive) → h ('should not') or i (Forbidden)
- Permission granted → l ('may' Permissive)

**Hebrew Jussive/Cohortative**:
- Strong obligation → f or g
- Weak suggestion → c (potential) or g (should)

**Modal verbs and particles**:
- Hebrew אָבָה ('ābâ, "be willing") → bouletic modality
- Greek δύναμαι (dynamai, "be able") → dynamic modality, maps to potential
- Greek δεῖ (dei, "it is necessary") → f ('must' Obligation)
- Greek ἐξέστιν (exestin, "it is lawful/permitted") → l ('may' Permissive)

**Epistemic strength gradation**:

| Context Clues | TBTA Code | Strength |
|---------------|-----------|----------|
| "Certainly, definitely, must be" | a | Definite Potential |
| "Probably, likely" | b | Probable Potential |
| "Perhaps, might, could" | c | 'might' Potential |
| "Might not, perhaps not" | j | 'might not' Potential |
| "Unlikely, doubtful" | d | Unlikely Potential |
| "Cannot, impossible" | e | Impossible Potential |

**Deontic strength gradation**:

| Context Clues | TBTA Code | Strength |
|---------------|-----------|----------|
| "Must, have to, required" | f | 'must' Obligation |
| "Should, ought to" | g | 'should' Obligation |
| "Should not, ought not" | h | 'should not' Obligation |
| "Must not, forbidden" | i | Forbidden Obligation |
| "May, allowed, permitted" | l | 'may' Permissive |

**Key insight**: Modal meaning often comes from:
- **Context** (genre, speech act, authority of speaker)
- **Modal particles/verbs** in clause
- **Conditional structures** (if-then logic)
- **Negation** (negative modality differs from positive)

TBTA requires:
- Lexicon of modal expressions
- Syntactic pattern recognition (conditional protasis/apodosis)
- Discourse role analysis (is this command from God, suggestion from human, etc.?)

#### 2.4 Reflexivity Feature Mapping

**Principle**: Identify argument structure and coreference

**Greek middle voice**:
- True reflexive ("he washed himself") → r (Reflexive)
- Reciprocal ("they greeted each other") → R (Reciprocal)
- Other middle uses (anticausative, dispositional) → N (Not Applicable), encode elsewhere

**Greek active voice with reflexive pronoun** (ἑαυτόν heauton):
- → r (Reflexive)

**Greek reciprocal pronoun** (ἀλλήλων allēlōn):
- → R (Reciprocal)

**Hebrew Niphal/Hithpael**:
- Reflexive uses → r
- Reciprocal uses → R
- Passive/middle uses → N

**Default**: N (Not Applicable) unless explicit reflexive/reciprocal marking or context

**Key insight**: Many middle voice uses in Greek are NOT reflexive in the strict sense. TBTA's `r`/`R` codes should be reserved for TRUE reflexive/reciprocal, where subject and object are coreferential.

### Stage 3: Contextual Refinement (Discourse Analysis)

**Input**: Initial semantic annotation

**Process**: Refine based on:

#### 3.1 Discourse Structure

- **Narrative backbone** (foreground events): Often aorist in Greek → U or C, with specific time codes
- **Background information**: Often imperfect in Greek → I or o (Continuative)
- **Discourse peaks**: May affect aspect/mood encoding
- **Participant tracking**: Affects reflexivity coding

#### 3.2 Genre Conventions

- **Historical narrative**: Favor historic past codes, completive aspect
- **Prophetic texts**: Complex modal distinctions (certain vs. conditional futures)
- **Wisdom literature**: Extensive use of gnomic (G) aspect, timeless (T) tense
- **Legal texts**: Deontic modality (obligations, prohibitions)
- **Poetry**: May have marked tense/aspect uses (e.g., prophetic perfect)

#### 3.3 Co-textual Constraints

- **Temporal adverbs**: "today" constrains time coding
- **Aspectual adverbs**: "always," "never," "often" constrain aspect coding
- **Modal adverbs**: "certainly," "perhaps" constrain mood coding
- **Discourse connectives**: "then," "while," "when" affect temporal relations

#### 3.4 Cross-Reference Verification

- Check parallel passages (Synoptic Gospels, parallel historical accounts)
- Verify consistency in similar contexts
- Learn from existing annotations (if available)

### Stage 4: Target Language Validation (Translation Testing)

**Input**: Annotated semantic representation

**Process**: Test whether annotation supports good translation to diverse target languages

#### 4.1 Test Cases

Select typologically diverse languages:
- **Tense-prominent**: English, Spanish (require clear time coding)
- **Aspect-prominent**: Russian, Mandarin (require clear aspect coding)
- **Remoteness-based**: Zulu, Yagua (benefit from fine temporal distinctions)
- **Mood-rich**: Turkish, Greenlandic (require clear modal distinctions)

#### 4.2 Transfer Rules

For each target language, specify:
- How TBTA time codes map to target tenses
- How TBTA aspect codes map to target aspects
- How TBTA mood codes map to target moods/modals
- What information is preserved, lost, or added

#### 4.3 Iterative Refinement

If translations are:
- **Unnatural**: Annotation may be too source-oriented; adjust toward target pragmatics
- **Inaccurate**: Annotation may miss source semantics; refine analysis
- **Inconsistent**: Annotation rules may need clarification

---

## Key Principles for Reproducibility

### Principle 1: Maximize Semantic Information

When in doubt, **annotate with maximum specificity** if it can be justified from source text and context. Target languages can always simplify, but they cannot add information that wasn't encoded.

Example: If context suggests "yesterday" (hesternal), code it as `a` rather than generic past `q`.

### Principle 2: Balance Source and Target

Annotation should be:
- **Faithful to source**: Don't impose target language categories on source
- **Useful for targets**: Don't use distinctions that can't be systematically transferred

Example: Greek aorist is not inherently past tense in all moods, but in indicative mood in narrative, coding it as past is justified and useful.

### Principle 3: Lexicon + Context + Discourse

No single level determines annotation:
- **Lexical**: Verb Aktionsart, inherent semantics
- **Morphological**: Source language forms
- **Syntactic**: Clause structure, voice, subordination
- **Contextual**: Adverbs, arguments, co-text
- **Discourse**: Genre, narrative structure, speech acts

All must be considered together.

### Principle 4: Consistency Over Perfection

For machine generation to work, **consistent rules** matter more than perfect linguistic analysis. Establish clear decision procedures:

- If source aspect is ambiguous → use default for verb class
- If temporal distance is unspecified → use "unknown" codes (q/p)
- If modality strength is unclear → use middle value (c for potential, g for obligation)

Document exceptions and special cases.

### Principle 5: Learn from Data

If annotating a corpus:
- Track frequent patterns (e.g., "aorist + narrative = U/C + h/g")
- Note exceptions and special constructions
- Build statistical models for ambiguous cases
- Validate against native speaker translations (LXX Greek → target vernaculars)

---

## Practical Workflow

### For Manual Annotation

1. **Read passage** in source language, understand context
2. **Identify each verb** and its clause/discourse role
3. **Consult lexicon** for Aktionsart and modal meanings
4. **Apply morphological analysis** (parse form)
5. **Map to TBTA codes** using decision trees (below)
6. **Check consistency** with surrounding context
7. **Validate** with parallel translations
8. **Document** any difficult decisions

### For Automated Annotation

1. **Morphological parsing**: Use existing parsers (OpenText.org for Greek, ETCBC for Hebrew)
2. **Lexical database**: Build/augment with Aktionsart and modal features
3. **Syntax parsing**: Identify clause types, voice, subordination
4. **Discourse annotation**: Genre detection, narrative structure, speech acts
5. **Rule-based mapping**: Apply decision rules (if X then Y)
6. **Statistical modeling**: Train ML models on annotated data for ambiguous cases
7. **Validation**: Human review of sample, inter-annotator agreement
8. **Iteration**: Refine rules and models based on errors

---

## Decision Trees (Simplified)

### Time Feature Decision Tree

```
Is the verb expressing a universal truth (gnomic)?
├─ YES → T (Timeless)
└─ NO
   └─ Is there a temporal adverb/phrase?
      ├─ YES
      │  ├─ "today" → A (Earlier Today) or r (Discourse) or F (Later Today)
      │  ├─ "yesterday" → a (Yesterday)
      │  ├─ "tomorrow" → j (Tomorrow)
      │  ├─ "last week" → d (A Week Ago)
      │  └─ etc. (map specific adverbs to codes)
      └─ NO
         └─ What is the genre?
            ├─ Historical narrative
            │  ├─ Is event within living memory? → g (Speaker's Lifetime)
            │  ├─ Is event documented history? → h (Historic Past)
            │  └─ Is event ancient/primordial? → i (Eternity Past)
            ├─ Prophetic
            │  ├─ Future prediction → p (Unknown Future) or specific future code
            │  └─ Prophetic perfect → may be r (Discourse) or near future
            └─ Direct discourse
               ├─ Can temporal distance be inferred? → use specific code
               └─ Otherwise → q (Unknown Past) or p (Unknown Future)
```

### Aspect Feature Decision Tree

```
What is the source verb form?
├─ Greek Aorist
│  ├─ Ingressive context ("began to")? → N (Inceptive)
│  ├─ Effective context ("succeeded in")? → C (Completive)
│  └─ Otherwise → U (Unmarked)
├─ Greek Present
│  ├─ Gnomic statement? → G (Gnomic)
│  ├─ Habitual context ("regularly does")? → H (Habitual)
│  ├─ Progressive context ("is doing now")? → o (Continuative)
│  └─ Otherwise → U (Unmarked)
├─ Greek Imperfect
│  ├─ Iterative context? → H (Habitual) or R (Routinely)
│  ├─ Progressive past? → I (Imperfective) or o (Continuative)
│  └─ Inceptive imperfect? → N (Inceptive)
├─ Greek Perfect
│  └─ → C (Completive) with resultant state
└─ Hebrew verb forms
   └─ (Similar logic, adjusted for Hebrew aspectual system)

Also check:
- Aktionsart of verb (stative → I/o, achievement → N/U, accomplishment → C)
- Aspectual adverbs ("always" → G/H, "continuously" → o)
- Phasal verbs ("begin" → N, "stop" → c, "finish" → C)
```

### Mood Feature Decision Tree

```
What is the source mood?
├─ Indicative
│  └─ → I (Indicative)
├─ Subjunctive
│  ├─ In conditional protasis? → c ('might' Potential)
│  ├─ Deliberative question? → c ('might' Potential)
│  ├─ Hortatory ("let us")? → g ('should' Obligation)
│  └─ Purpose clause? → depends on strength
├─ Optative
│  ├─ Wish? → d (Unlikely) or c ('might')
│  └─ Potential? → c or d
└─ Imperative
   ├─ Strong command? → f ('must' Obligation)
   ├─ Moderate command? → g ('should' Obligation)
   ├─ Prohibition? → h ('should not') or i (Forbidden)
   └─ Permission? → l ('may' Permissive)

Also check:
- Modal verbs/particles in clause
- Authority of speaker (divine command → stronger obligation)
- Context (legal text → deontic, epistemic reasoning → epistemic)
- Negation (affects strength and type)
```

### Reflexivity Decision Tree

```
Does the verb have reflexive/reciprocal marking?
├─ Greek middle voice
│  ├─ Subject = Object (reflexive)? → r (Reflexive)
│  ├─ Mutual action (reciprocal)? → R (Reciprocal)
│  └─ Other middle uses? → N (Not Applicable)
├─ Reflexive pronoun present?
│  └─ → r (Reflexive)
├─ Reciprocal pronoun present?
│  └─ → R (Reciprocal)
├─ Hebrew reflexive/reciprocal form?
│  ├─ True reflexive? → r
│  ├─ Reciprocal? → R
│  └─ Otherwise → N
└─ Otherwise
   └─ → N (Not Applicable)
```

---

## Resources Needed for Reproduction

### Linguistic Databases

1. **Morphologically parsed texts**
   - OpenText.org (Greek NT)
   - ETCBC database (Hebrew Bible)
   - Tischendorf/Nestle-Aland Greek text with parsings

2. **Lexicons with semantic features**
   - BDAG (Greek lexicon)
   - BDB, HALOT (Hebrew lexicons)
   - Louw-Nida semantic domains (Greek)
   - Augment with:
     - Aktionsart classifications
     - Modal verb semantics
     - Temporal adverb mappings

3. **Discourse-annotated corpora**
   - Genre labels (narrative, prophecy, law, poetry, wisdom, epistle)
   - Narrative structure (foreground/background, participant tracking)
   - Speech act annotations

### Computational Tools

1. **Parsers**: Morphological analyzers for Greek/Hebrew
2. **Syntax tools**: Dependency or constituency parsers
3. **Annotation interface**: For manual annotation and validation
4. **Rule engine**: To apply mapping rules consistently
5. **Machine learning**: For resolving ambiguous cases
6. **Validation tools**: Inter-annotator agreement, consistency checking

### Human Expertise

1. **Biblical language scholars**: For source analysis
2. **Typologists**: For cross-linguistic validation
3. **Translation consultants**: To verify target language adequacy
4. **Computational linguists**: For automation

---

## Open Questions and Future Research

### Question 1: Granularity of Time Codes

**Issue**: Greek/Hebrew rarely specify fine temporal distinctions. How often should codes like "2 days ago" vs "a week ago" be used?

**Hypothesis**: Use fine distinctions ONLY when:
- Explicit temporal adverbs/phrases present
- Narrative timeline clearly establishes distance
- Genre conventions require it (e.g., legal witness testimony)

Otherwise, use broader categories (q/p for unknown, g/h for general past).

**Test**: Annotate sample corpus with fine vs. coarse distinctions; compare resulting translations.

### Question 2: Aspect vs. Aktionsart

**Issue**: How much does lexical aspect (Aktionsart) determine TBTA aspect code vs. grammatical aspect (source morphology)?

**Hypothesis**: Both contribute:
- Grammatical aspect sets range of possibilities
- Aktionsart + context selects within range
- Example: Greek aorist + stative verb → U; Greek aorist + achievement verb + "began to" context → N

**Test**: Annotate verbs with different Aktionsart classes in same grammatical aspect; track which TBTA codes emerge.

### Question 3: Modal Strength Gradation

**Issue**: How to consistently assign six levels of potential and four levels of obligation?

**Hypothesis**: Requires:
- Lexical strength ratings for modal expressions
- Contextual modulation (e.g., negation, conditional embedding)
- Genre conventions (prophetic certainty vs. wisdom probability)

**Test**: Inter-annotator agreement on modal strength; correlation with translation equivalents.

### Question 4: Unmarked vs. Specific

**Issue**: When to use U (Unmarked) aspect vs. specific aspect codes?

**Hypothesis**: Use U when:
- Source language doesn't specify
- Multiple interpretations are equally valid
- Target languages would diverge in their encoding

Use specific codes when:
- Clear contextual evidence
- Discourse function requires it
- Cross-linguistically stable patterns

**Test**: Compare translation naturalness with U vs. specific codes.

---

## Validation Metrics

To evaluate annotation quality:

1. **Inter-annotator agreement**: Cohen's kappa, Krippendorff's alpha
2. **Consistency**: Same verb in same context → same code
3. **Coverage**: All verbs annotated, no missing values
4. **Transfer adequacy**: Resulting translations rated by native speakers
5. **Typological validity**: Codes align with cross-linguistic patterns (Comrie, Bybee, etc.)

---

## Conclusion: Path Forward

Reproducing TBTA's annotation requires:

1. **Deep linguistic analysis** of source texts (Greek/Hebrew)
2. **Principled semantic mapping** using typological frameworks
3. **Contextual refinement** at lexical, syntactic, discourse levels
4. **Target language validation** across diverse typologies
5. **Iterative improvement** based on translation testing

This is **feasible but labor-intensive**. Automation can assist, but human expertise remains essential for:
- Ambiguous cases
- Genre-specific conventions
- Discourse pragmatics
- Validation and refinement

The result: A rich semantic annotation that enables accurate Bible translation across the world's linguistic diversity.

---

*Document compiled: 2025-11-05*
*Author: Claude (Anthropic)*
*Status: Initial thesis - requires empirical testing*
