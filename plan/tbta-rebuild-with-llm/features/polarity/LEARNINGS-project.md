# Polarity Feature: Initial Thesis for Reproduction

**Document Created**: 2025-11-05
**Status**: Initial thesis based on research findings
**Purpose**: Methodology for reproducing TBTA's polarity annotation decisions

---

## Executive Summary

TBTA's polarity system marks **semantic negation** on affected constituents (nouns and verbs) using binary **Affirmative/Negative** values. Reproduction requires:

1. **Source language negation analysis** (identify morphemes and scope)
2. **Semantic interpretation** (what is actually negated?)
3. **Target language consideration** (asymmetric effects, mood shifts, negative concord)
4. **Scope resolution** (in cases of ambiguity)

**Key Insight**: TBTA annotates **meaning** (semantics), not just **form** (syntax). The negation marker may appear on a verb, but if semantically the noun is negated ("nothing" = "no thing"), the noun gets marked "Negative".

---

## Core Principles

### 1. Semantic, Not Syntactic

**TBTA marks where negation applies semantically, not where negative morphemes appear.**

**Example (Genesis 1:2)**:
- English: "The earth had **no** form" / "The earth did **not** have form"
  - First translation: Negative on noun "no form"
  - Second translation: Negative on verb "did not have"
  - **TBTA captures both**: Verb gets "Negative" in one clause representation; noun gets "Negative" in another vocabulary alternate

**Example (Genesis 1:2, Clause 3)**:
- Simplified: "**Nothing** existed on earth"
- "Nothing" = "no thing" (negative quantifier)
- TBTA marks: Noun "thing" → **"Negative"**, Verb "exist" → **"Affirmative"**
- **Why**: Semantically, the negation applies to the noun (no thing), not to existence itself

### 2. Binary System (Currently)

TBTA uses **only two values**:
- **Affirmative**: Positive polarity
- **Negative**: Negative polarity

**Collapsed distinctions**:
- Hebrew לֹא (declarative) vs. אַל (imperative) → both "Negative"
- Greek οὐ (indicative) vs. μή (non-indicative) → both "Negative"
- Greek emphatic οὐ μή → still just "Negative"

**Implication**: TBTA prioritizes **broad applicability** over **fine-grained distinction**.

### 3. Applied to Nouns and Verbs

The `Polarity` field appears on:
- **Nouns** (SyntacticCategory 1)
- **Verbs** (SyntacticCategory 2)

**Not marked on**:
- Adjectives, Adverbs, Adpositions, Conjunctions (in observed data)

**Question**: Should other categories receive polarity marking?
- "John is **not happy**" - does adjective "happy" get "Negative"?
- Current data suggests: **No** (polarity marks the verb "is", not the adjective)

---

## Reproduction Methodology: 4-Phase Process

### Phase 1: Source Language Morphological Analysis

**Input**: Greek/Hebrew source text (or any source language)

**Steps**:

#### Step 1.1: Identify Negative Morphemes

Scan for:
- **Hebrew**: לֹא, אַל, אֵין, negative particles/prefixes
- **Greek**: οὐ, μή, οὐ μή (emphatic)
- **Other languages**: Consult family-specific patterns (see README.md)

#### Step 1.2: Identify Negative Semantics

Look for words with **inherent negative meaning**:
- **Negative quantifiers**: "nothing", "nobody", "never"
- **Negative verbs**: "lack", "fail", "refuse"
- **Negative nouns**: "absence", "void"

#### Step 1.3: Classify Negation Type

- **Sentential negation**: Negates entire proposition
- **Constituent negation**: Negates specific element
- **Emphatic negation**: οὐ μή, double negatives for emphasis

**Record**: Location of negative morphemes, type of negation, emphasis markers

---

### Phase 2: Semantic Scope Determination

**Input**: Morphological analysis from Phase 1

**Steps**:

#### Step 2.1: Determine Scope

**For each negative morpheme**, identify:
- What is the **semantic scope**?
- Which elements fall **under negation's c-command domain**?

**Tools**:
- Syntactic tree structure
- C-command relations
- Semantic entailment tests

#### Step 2.2: Resolve Ambiguities

If multiple interpretations exist:

**Example**: "I didn't find many valuable books"
- Interpretation 1: many > not (many books I failed to find)
- Interpretation 2: not > many (few books I found)

**Resolution strategies**:
1. **Context**: What does surrounding discourse suggest?
2. **Pragmatics**: What is the likely communicative intent?
3. **Cross-reference**: How do other translations interpret this?
4. **Default**: Choose narrow scope (negation affects immediately adjacent element)

#### Step 2.3: Mark Affected Elements

For each word in the verse:
- **Is it under negation's scope?** → Candidate for "Negative"
- **Is it outside scope?** → "Affirmative"

---

### Phase 3: Polarity Assignment

**Input**: Scope analysis from Phase 2

**Steps**:

#### Step 3.1: Mark Verbs

**Rule**: If verb is negated (morphologically or semantically) → **"Negative"**

**Examples**:
- *"John **did not** run"* → Verb "run" = **Negative**
- *"John **lacked** resources"* → Verb "lacked" = **Negative** (inherent negative meaning)
- *"John ran"* → Verb "ran" = **Affirmative**

#### Step 3.2: Mark Nouns

**Rule**: If noun is semantically negative → **"Negative"**

**Examples**:
- *"John saw **nothing**"* → Noun "nothing" = **Negative** (negative quantifier)
- *"The earth had **no form**"* → Noun "form" = **Negative** (under negation's scope)
- *"John saw **the book**"* → Noun "book" = **Affirmative**

**Special Case: Negative Concord**

In negative concord languages (Romance, Slavic), multiple negative elements = single negation:
- **Spanish**: *No veo nada* ("not see nothing" = "see nothing")
  - Verb "veo" → **Negative**
  - Noun "nada" → **Negative** (both marked, even though single semantic negation)

**Rationale**: Each element carries negative morphology/semantics, so each gets marked.

#### Step 3.3: Handle Serial Verb Constructions (Niger-Congo)

**Unity of Polarity**: If negation scopes over entire series, **all verbs** get same polarity.

**Example**:
- *"He **did not** take go sell"* (SVC: take-go-sell = take and go and sell)
  - Verb "take" → **Negative**
  - Verb "go" → **Negative**
  - Verb "sell" → **Negative**

(All three verbs under single negation scope)

#### Step 3.4: Default Assignment

All elements not marked "Negative" → **"Affirmative"**

---

### Phase 4: Target Language Validation

**Input**: Polarity assignments from Phase 3

**Purpose**: Ensure annotation accounts for target language requirements

**Steps**:

#### Step 4.1: Check Language Family

From our 1009-language dataset, identify target language family:
- **Austronesian** (176 languages)
- **Trans-New Guinea** (129 languages)
- **Niger-Congo** (94 languages)
- **Indo-European** (55 languages)
- **Other** (555 languages, 70+ families)

#### Step 4.2: Identify Family-Specific Negation Patterns

**Austronesian**:
- Does negation trigger **realis → irrealis** mood shift?
- Note: Mood is separate annotation, but check consistency

**Trans-New Guinea**:
- Will target language use ***ma-** or ***na-** reflex for negation?
- Does negation affect **switch-reference** marking?

**Niger-Congo**:
- **Bantu**: Multiple negative morphemes required?
- **Serial verbs**: All verbs in chain negated?
- **Tone**: Negative tones present (not marked in TBTA, but relevant for target)

**Indo-European**:
- **Slavic**: Does negation trigger **genitive of negation** on object nouns? (Separate from polarity marking)
- **Romance**: Negative concord requires **n-words + negative marker** coordination
- **Germanic**: Simple symmetric negation (usually)

#### Step 4.3: Validate Asymmetric Effects

If target language has **asymmetric negation** (Miestamo 2005):
- **TAM changes**: Verify polarity marking doesn't conflict with required TAM shifts
- **Case changes**: (Slavic genitive) - separate annotation, but note dependency
- **Word order**: Some languages reorder under negation - note for translation

#### Step 4.4: Check for Scope Consistency

Ensure:
- **Serial verbs** all have same polarity when under single negation scope
- **Negative concord n-words** properly coordinated with main negative marker
- **Quantifier scope ambiguities** resolved consistently across similar contexts

---

## Worked Examples

### Example 1: Genesis 1:1 (All Affirmative)

**Source (Simplified)**: "In beginning God create sky and earth"

**Step 1 (Morphology)**: No negative morphemes present

**Step 2 (Scope)**: No negation to scope over

**Step 3 (Assignment)**:
- Noun "beginning" → **Affirmative**
- Noun "God" → **Affirmative**
- Verb "create" → **Affirmative**
- Noun "sky" → **Affirmative**
- Noun "earth" → **Affirmative**

**Step 4 (Validation)**: No language-specific negation issues

**Result**: All elements **Affirmative** ✓

---

### Example 2: Genesis 1:2 (Mixed: Negative + Affirmative)

**Source (Simplified Vocab Alternate 1)**: "earth be formless and empty"

**Step 1 (Morphology)**:
- "formless" = negative semantics (absence of form)
- "empty" = negative semantics (absence of content)

**Step 2 (Scope)**:
- These are **predicative adjectives**, not negated verbs
- Semantic negation is inherent in the adjective meanings

**Step 3 (Assignment)**:
- Noun "earth" → **Affirmative** (earth itself not negated)
- Verb "be" → **Affirmative** (existence is affirmed)
- Adjective "formless" → (Not marked in TBTA data - adjectives don't receive polarity)
- Adjective "empty" → (Not marked in TBTA data)

**Alternative Clause (Simplified Vocab Alternate 2)**: "earth have form"

**Step 1 (Morphology)**:
- Hebrew: *לֹא* or equivalent negative marker on verb
- English gloss: "did not have" or "had no"

**Step 2 (Scope)**:
- Negation scopes over verb "have"

**Step 3 (Assignment)**:
- Noun "earth" → **Affirmative**
- Verb "have" → **Negative** ✓ (TBTA marks this)
- Noun "form" → **Affirmative** (object of verb)

**Alternative Clause (Simplified Vocab Alternate 3)**: "nothing exist on earth"

**Step 1 (Morphology)**:
- "nothing" = negative quantifier (no + thing)

**Step 2 (Scope)**:
- Semantic negation is on the noun "thing" (quantified as "no thing")
- Verb "exist" is not negated (existence is affirmed, but of nothing)

**Step 3 (Assignment)**:
- Noun "thing" → **Negative** ✓ (TBTA marks this)
- Verb "exist" → **Affirmative** ✓ (TBTA marks this)
- Noun "earth" → **Affirmative**

**Step 4 (Validation)**: Multiple vocabulary alternates show different structural realizations of same semantic content; polarity marks semantic negation consistently

**Result**: TBTA captures multiple ways to express negation ✓

---

### Example 3: John 11:26 (Greek Emphatic Negation οὐ μή)

**Source (Greek)**: ὁ πιστεύων εἰς ἐμὲ **οὐ μὴ** ἀποθάνῃ εἰς τὸν αἰῶνα
**Translation**: "Whoever believes in me will **certainly never** die forever"

**Step 1 (Morphology)**:
- **οὐ μή** (emphatic double negative) + subjunctive verb *ἀποθάνῃ* (die)
- This is the **strongest possible future negation** in Greek

**Step 2 (Scope)**:
- Negation scopes over verb "die"
- Wide scope over entire future time ("forever")

**Step 3 (Assignment)**:
- Verb "believe" → **Affirmative**
- Verb "die" → **Negative** ✓ (under emphatic negation)

**Step 4 (Validation)**:
- **Greek οὐ μή** = emphatic, but TBTA collapses to simple "Negative"
- Target languages with **emphatic negation forms** (e.g., some Austronesian, Niger-Congo) could benefit from extended annotation:
  - Current: "Negative"
  - Extended: "Emphatic Negative"
- **Recommendation**: Document emphatic source contexts in metadata for translators

**Result**: Basic polarity captured; emphasis requires additional commentary ✓

---

### Example 4: Slavic Genitive of Negation (Target Language Effect)

**Source (Simplified)**: "John **not** read book"

**Step 1-3**: Standard negation analysis
- Verb "read" → **Negative**
- Noun "book" → **Affirmative** (object, not negated itself)

**Step 4 (Validation - Target: Russian)**:
- Russian requires **genitive case** on direct object under negation
- Affirmative: *Я читаю **книгу*** (book-**ACC**)
- Negative: *Я не читаю **книги*** (book-**GEN**)

**Question**: Should TBTA mark noun "book" as "Negative" because it's affected by negation in target language?

**Answer**: **No** - TBTA marks **source semantics**, not target morphology
- Polarity: "Affirmative" (noun is not semantically negated)
- **Separate annotation**: Case assignment is distinct grammatical feature
- Target language morphology is **derivable** from source semantics + target grammar

**Rationale**: Polarity = semantic negation; case marking = syntactic requirement

**Result**: Polarity annotation remains source-semantic; target morphology handled separately ✓

---

## Decision Points and Trade-offs

### 1. Binary vs. Multi-valued Polarity

**Current TBTA**: Binary (Affirmative/Negative)

**Alternative**: Multi-valued system
- **Affirmative** (unmarked positive)
- **Emphatic Affirmative** (ἀμήν, particles)
- **Negative** (standard negation)
- **Emphatic Negative** (οὐ μή, double negation for emphasis)
- **Interrogative Negative** (negative questions with biased expectations)

**Trade-off**:
- **Binary**: Simple, universal, easy to apply consistently
- **Multi-valued**: Captures nuance, better for languages with emphatic/modal distinctions

**Recommendation**: **Start with binary** (matching TBTA); extend later if needed

---

### 2. Syntactic vs. Semantic Marking

**Current TBTA**: Semantic (marks what is negated semantically)

**Alternative**: Syntactic (mark where negative morpheme appears)

**Example**: "John saw **nothing**"
- **Semantic**: Noun "nothing" → Negative (TBTA's approach ✓)
- **Syntactic**: Verb "saw" could be marked Negative if "nothing" analyzed as triggering verbal negation

**Trade-off**:
- **Semantic**: Captures meaning, cross-linguistically more robust
- **Syntactic**: Easier to automate (parse tree analysis), language-specific

**Recommendation**: **Follow TBTA's semantic approach** - more useful for translation

---

### 3. Scope Ambiguity Resolution

**Challenge**: Some sentences have multiple possible negation scopes

**Example**: "I didn't find many valuable books"

**Approaches**:
1. **Default to narrow scope** (negation affects immediately adjacent element)
2. **Consult context** (what does discourse suggest?)
3. **Mark both interpretations** (create alternative annotations)
4. **Defer to human judgment** (flag for manual review)

**Recommendation**: **Context-based resolution** (Phase 2, Step 2.2), with **narrow scope as default** when ambiguous

---

### 4. Adjective/Adverb Polarity

**Current TBTA**: Does not mark polarity on adjectives or adverbs (observed data)

**Question**: Should we?

**Example**: "John is **not happy**"
- Verb "is" → Negative ✓ (TBTA approach)
- Adjective "happy" → ?? (currently unmarked)

**Arguments for marking**:
- Semantic: "happy" is negated (John's state is ¬happy)
- Some languages mark polarity on adjectives

**Arguments against**:
- TBTA focuses on **core semantic elements** (nouns, verbs)
- Adjectives/adverbs typically don't carry polarity morphology
- Keeps annotation simpler

**Recommendation**: **Follow TBTA's approach** (nouns and verbs only); extend if target languages require it

---

## Language Family Checklist

For each target language from our 1009-language dataset:

### Austronesian (176 languages)

- [ ] Does negation trigger **realis → irrealis** mood shift?
- [ ] What is the **negative morpheme** (particle/affix/auxiliary)?
- [ ] Does irrealis marking appear **separately from** negation marker?
- [ ] Are there **negative polarity items** (NPIs) that must co-occur with negation?

### Trans-New Guinea (129 languages)

- [ ] Which **Proto-TNG reflex** does this language use? (*ma-* or *na-*)
- [ ] Is negation **preverbal or prefixal**?
- [ ] Does negation affect **switch-reference marking** in clause chains?
- [ ] Are there **separate negative imperatives** or negative subjunctives?

### Niger-Congo (94 languages)

- [ ] **Bantu**: How many negative morphemes required? (preverbal, suffix, clause-final?)
- [ ] Does negation cause **tone changes** on verbs?
- [ ] **Serial verbs**: Confirm negation scopes over entire series
- [ ] Are there **negative auxiliary verbs** or inflected negative markers?
- [ ] Does negation affect **noun class agreement**?

### Indo-European (55 languages)

- [ ] **Slavic**: Does negation trigger **genitive of negation** on objects?
- [ ] **Slavic**: Is this language **strict/non-strict/optional** for negative concord?
- [ ] **Romance**: What is the **Jespersen's Cycle stage** (ne...pas, just pas, etc.)?
- [ ] **Romance**: Is negative concord **strict or non-strict** (preverbal n-word behavior)?
- [ ] **Germanic**: Simple symmetric negation? (usually yes)

### Other Families

- [ ] Consult **WALS Chapter 112** for negative morpheme type
- [ ] Consult **WALS Chapter 143** for position of negative morpheme
- [ ] Check for **asymmetric negation** patterns (TAM/case/word order changes)
- [ ] Identify **negative polarity items** if present
- [ ] Note any **emphatic affirmation/negation** markers

---

## Validation Criteria

A successful polarity annotation must satisfy:

### Semantic Consistency
- [ ] Semantically negated elements marked "Negative"
- [ ] Elements outside negation scope marked "Affirmative"
- [ ] Negative quantifiers ("nothing", "nobody") marked "Negative"
- [ ] Inherent negative verbs ("lack", "fail") marked "Negative"

### Syntactic Coverage
- [ ] All **verbs** have polarity assignment
- [ ] All **nouns** have polarity assignment
- [ ] No contradictory polarity marks (e.g., both Affirmative and Negative)

### Scope Coherence
- [ ] Scope ambiguities resolved consistently
- [ ] Serial verb constructions: all verbs share polarity when under single scope
- [ ] Negative concord: all n-words + negative marker properly marked

### Target Language Compatibility
- [ ] Language family negation pattern identified
- [ ] Asymmetric effects noted (TAM, case, word order)
- [ ] Emphatic contexts flagged for translator attention
- [ ] Negative polarity item licensing contexts identified

---

## Automation Strategy

### High Confidence (Automated)

Can be automated with **>90% confidence**:
1. **Morpheme detection**: Scan for known negative morphemes (οὐ, μή, לֹא, אַל, etc.)
2. **Negative quantifiers**: "nothing", "nobody", "never", etc. → mark noun "Negative"
3. **Simple negated verbs**: Verb immediately following negative particle → "Negative"
4. **Affirmative default**: Clauses without any negative morphemes → all "Affirmative"

### Medium Confidence (Semi-automated)

Requires **parse tree + heuristics**:
1. **Scope determination**: C-command analysis from syntax tree
2. **Constituent negation**: Identify narrow-scope negation
3. **Negative concord**: Recognize n-words + negative marker patterns
4. **Serial verb identification**: Mark all verbs in chain with same polarity

### Low Confidence (Manual Review Required)

Requires **human judgment**:
1. **Scope ambiguities**: Multiple interpretations possible
2. **Emphatic markers**: Distinguish regular from emphatic negation (for extended annotation)
3. **Inherent negative semantics**: Verbs like "lack", "fail", "refuse" (lexical judgment)
4. **Idiomatic negation**: Language-specific negative idioms

---

## Initial Thesis Summary

**Core Thesis**: TBTA's polarity annotation can be reproduced through **4-phase semantic analysis**:

1. **Morphological Analysis**: Identify negative morphemes and inherent negative words
2. **Scope Determination**: Analyze which elements fall under negation's semantic scope
3. **Polarity Assignment**: Mark affected nouns/verbs as "Negative"; rest as "Affirmative"
4. **Target Validation**: Check consistency with target language negation patterns

**Key Principles**:
- **Semantic, not syntactic**: Mark what is semantically negated
- **Binary system**: Affirmative/Negative (collapse fine-grained distinctions)
- **Nouns + Verbs**: Focus on core semantic elements
- **Scope-based**: Use c-command and semantic scope to determine affected elements

**Success Metrics**:
- 90%+ agreement with TBTA annotations on test set
- Semantic consistency across diverse constructions
- Target language compatibility for 1009 languages in our dataset
- Clear methodology for handling ambiguous cases

**Next Steps**:
1. **Create test set**: Sample 100 verses with diverse negation patterns from TBTA data
2. **Implement Phase 1-3**: Build automated pipeline for morphology → scope → polarity
3. **Validate against TBTA**: Compare automated output to TBTA gold standard
4. **Iterate**: Refine rules based on disagreements
5. **Extend to target languages**: Test Phase 4 validation for each language family
6. **Document edge cases**: Build reference guide for manual review scenarios

---

**Document Status**: Initial thesis complete
**Confidence Level**: High for basic cases; medium for ambiguous scope; requires testing
**Ready for**: Implementation and validation
**Date**: 2025-11-05
