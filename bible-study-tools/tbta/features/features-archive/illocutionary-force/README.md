# Illocutionary Force in TBTA

## Translation Impact

**Illocutionary force determines HOW a clause functions communicatively—whether asserting, questioning, commanding, or exhorting.** East Asian languages (Japanese, Mandarin, Korean) require sentence-final particles for every clause type; missing a question particle makes a sentence ungrammatical. Imperative register choices (direct vs. polite vs. honorific) encode speaker-hearer relationships that carry theological significance: Jesus commanding demons vs. teaching disciples requires different forms. Without correct force marking, translations become ambiguous or convey unintended authority dynamics.

---

## Complete Value Enumeration

| Value | Definition | Typical Marking | Bible Context | Language Examples |
|-------|-----------|-----------------|---------------|-------------------|
| **Declarative** | Statement of fact; assertion | Unmarked in many languages | "Jesus healed the sick", "God is love" | En: simple statement; Jp: falling pitch; Zh: optional 了 (le) |
| **Yes-No Interrogative** | Polar question expecting yes/no response | Inversion, particles, intonation | "Do you believe in Jesus?" | En: Do you...?; Jp: か (ka); Zh: 吗 (ma); Ko: -니 (ni) |
| **Wh-Interrogative** | Content question (who, what, when, where, why, how) | Fronted or in-situ wh-word | "Who is Jesus?", "When will He come?" | En: fronted wh-; Jp: in-situ + か (ka); Zh: in-situ wh- |
| **Imperative** | Command; directing hearer to act | Special verb forms or particles | "Repent!", "Follow me", "Love your enemies" | En: bare verb; Sp: special conjugation; Jp: -e/-ro/-nasai; Zh: 吧 (ba) |
| **Hortative** | Exhortation/invitation; first-person plural | "Let us..." structure | "Let us love one another" | En: Let us/Let's; Sp: Vamos; Qu: -yachun suffix |
| **Exclamative** | Expression of strong emotion/surprise | Intonation, special particles | "How great is God!", "O the depths!" | En: What/How + !; Sp: ¡Qué...!; Jp: -naa; Zh: 多 (duō) |

---

## Baseline Statistics

### Force Distribution by Genre

**Narrative** (expected):
- Declarative: ~60% (statements about actions/events)
- Interrogative: ~20% (questions in dialogue)
- Imperative: ~15% (commands, instructions)
- Other: ~5%

**Teaching/Epistles** (expected):
- Declarative: ~70% (doctrinal statements)
- Imperative: ~15% (exhortations, commands)
- Interrogative: ~10% (rhetorical questions)
- Other: ~5%

**Prophecy** (expected):
- Declarative: ~50% (future predictions)
- Imperative: ~25% (divine commands)
- Interrogative: ~15% (rhetorical questions)
- Other: ~10%

**Law** (expected):
- Imperative: ~60% (commandments)
- Declarative: ~30% (statutes, explanations)
- Interrogative: ~5% (rhetorical in teaching)
- Other: ~5%

### Rhetorical Question Frequency
- Approximately 20-30% of biblical "questions" are rhetorical (not information-seeking)
- Higher in prophetic books (~40%)
- Lower in historical narrative (~10%)

---

## Quick Translator Test

Answer these questions about your target language:

1. ☐ Does your language mark questions with particles or intonation only?
2. ☐ Does your language have distinct imperative verb forms?
3. ☐ Does your language use sentence-final particles for speech acts? (e.g., Japanese ne, yo, ka)
4. ☐ Does your language mark performatives specially? (I hereby declare, bless, curse)
5. ☐ How does your language distinguish direct from indirect commands?

**If you answered YES to #3 (sentence-final particles), illocutionary force annotation is CRITICAL for correct particle selection.**

**Languages requiring this**:
- East Asian: Japanese, Korean, Mandarin (sentence particles)
- Southeast Asian: Thai, Vietnamese, Malay (particles)
- Bantu: Many use tone/particles for illocutionary marking

---

## Examples

### Example 1: Declarative (JHN.003.016)
**Text**: "For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life."

**Force**: Declarative
- **Why**: Statement of theological fact
- **Marking**: No interrogative or imperative markers
- **Translation**: Use declarative word order; no question particles

### Example 2: Yes-No Interrogative (MAT.019.017)
**Text**: "Why do you ask me about what is good?"

**Force**: Yes-No Interrogative (though expects specific answer)
- **Why**: Question form seeking response
- **Marking**: Question word + interrogative structure
- **Translation**: En: "Why...?"; Jp: なぜ...か (naze...ka); Zh: 为什么...吗 (weishenme...ma)

### Example 3: Imperative (MAT.003.002)
**Text**: "Repent, for the kingdom of heaven is at hand."

**Force**: Imperative
- **Why**: Direct command from John the Baptist
- **Register**: Prophetic/urgent, not polite
- **Translation**: En: "Repent!"; Jp: 悔い改めなさい (kuiatarame-nasai); Zh: 悔改吧 (huigai ba)

### Example 4: Hortative (1JN.004.007)
**Text**: "Beloved, let us love one another, for love is from God."

**Force**: Hortative
- **Why**: First-person plural exhortation (inclusive)
- **Scope**: Community action, not individual command
- **Translation**: En: "Let us love"; Sp: "Amemos"; Qu: uses -yachun suffix

### Example 5: Rhetorical Interrogative (ROM.008.031)
**Text**: "If God is for us, who can be against us?"

**Force**: Interrogative FORM, Declarative/Exclamative FUNCTION
- **Why**: Not seeking information; asserting "no one can oppose"
- **Rhetorical**: True (expects implied negative answer)
- **Translation**: Some languages convert to exclamative; others maintain question form with context

---

## Hierarchical Prompt Template

### Level 1: Check Morphological Marking
**Prompt**: "Does the verb form explicitly mark illocutionary force?"

- Greek: Imperative mood → **Imperative Force**
- Hebrew: Imperative, Jussive, Cohortative → **Imperative Force**
- Interrogative pronouns (who, what, why) → **Interrogative Force**
- If explicit → Done. If not → Continue Level 2

### Level 2: Syntactic Patterns
**Prompt**: "What syntactic pattern indicates the speech act?"

- Question word order (inversion) → **Interrogative Force**
- Standard SVO/VSO order → **Declarative Force** (default)
- Let us/Let's structure → **Hortative Force**

### Level 3: Discourse Context
**Prompt**: "What is the speaker trying to achieve?"

- Requesting information → **Interrogative Force**
- Commanding action → **Imperative Force**
- Stating facts → **Declarative Force**
- Expressing emotion/awe → **Exclamative Force**

### Level 4: Check for Indirect Speech Acts
**Prompt**: "Could this be indirect speech act?"

- Polite question functioning as command → Still **Imperative Force**
- Example: "Can you pass the salt?" (form=question, force=command)
- Rhetorical question making assertion → Mark as Interrogative with "Rhetorical: true"

---

## Gateway Features: Quick Prediction Rules

**If clause contains... → Then predict... (Confidence)**

| Condition | Predicted Force | Confidence |
|-----------|----------------|------------|
| Imperative verb form | **Imperative** | 95%+ |
| Interrogative pronoun (who, what, why) | **Interrogative** | 90%+ (unless rhetorical) |
| Question particle (Gk: ἆρα, οὐ, μή) | **Interrogative** | 95%+ |
| Optative mood (Greek) | **Optative/Hortative** | 95%+ |
| Standard indicative statement | **Declarative** | 85%+ (default) |

**Special Rules**:
- **If question word present → 90% Interrogative** (unless clearly rhetorical)
- **If "let us" present → 95% Hortative** (not imperative)
- **If exclamation about degree ("how", "what") → 80% Exclamative**

### Correlation with Mood
- Imperative Mood → 100% Imperative Force
- Optative Mood → 100% Optative/Hortative Force
- Subjunctive Mood → Mixed (check context)
- Indicative Mood → Usually Declarative Force (90%+)

---

## Common Errors

### Error 1: Confusing Grammatical Mood with Illocutionary Force
**Problem**: Assuming indicative mood = declarative force always
- Example: "You will honor your father" (form=indicative, force=imperative)
**Solution**: Check discourse function, not just verb form

### Error 2: Missing Indirect Speech Acts
**Problem**: Polite questions functioning as commands
- Example: "Would you mind closing the door?" (form=question, force=command)
**Solution**: Analyze speaker intent and context

### Error 3: Confusing Rhetorical vs Genuine Questions
**Problem**: Both use interrogative form
- Genuine: "What time is it?" (seeks information)
- Rhetorical: "Who can stand before God?" (asserts "no one")
**Solution**: Check if answer is expected or point is being made

### Error 4: Not Recognizing Hortatives
**Problem**: Treating "let us" as second-person imperative
- Wrong: "Love one another" (command to you)
- Right: "Let us love one another" (proposal for we together)
**Solution**: Check for first-person plural inclusion

### Error 5: Missing Register Distinctions in Imperatives
**Problem**: Using same imperative form for all contexts
- Jesus to demons: Direct/harsh register appropriate
- Jesus to disciples: Intimate/teaching register appropriate
**Solution**: Annotate register for all imperatives; note speaker-hearer relationship

---

## Validation Approach

### Experiment Status: COMPLETE
Experiment 001 tested force identification across multiple test cases (MAT.003.002, JHN.003.016, LUK.012.049, MAT.019.006, MAT.022.037-40).

**Findings**:
- Declarative prediction: 90%+ accuracy (most straightforward)
- Interrogative (yes/no vs wh-): 85%+ accuracy
- Imperative register prediction: 70%+ accuracy (highly language-dependent)
- Rhetorical question identification: ~75% accuracy (context-dependent)

### Validation Levels

**Critical (Must Pass)**:
1. Correct force category (Declarative, Interrogative, Imperative, etc.)
2. Rhetorical vs. genuine question distinction
3. Direct vs. indirect speech act identification

**High Priority (80%+)**:
1. Register appropriateness for imperatives
2. Hortative vs. imperative distinction
3. Yes-no vs. wh- interrogative distinction

**Medium Priority (60%+)**:
1. Particle suggestions for target languages
2. Politeness level recommendations
3. Exclamative force identification

### Testing Strategy
1. **Check morphological markers first** (imperative mood, interrogative pronouns)
2. **Analyze syntactic patterns** (word order, particles)
3. **Consider discourse context** (speaker intent, expected response)
4. **Validate against TBTA data** (when available)
5. **Document errors** for pattern refinement

---

## Related Files

- **LEARNINGS.md**: 10 critical discoveries about force in translation
- **experiment-001.md**: Detailed test cases with language-specific predictions
- **INDEX.md**: Quick reference for force feature

For detailed force descriptions, language family patterns, and cross-linguistic examples, see LEARNINGS.md.

---

**Feature Status**: Primary Documentation Complete
**Last Updated**: November 2025
**TBTA Version**: Current
