# TBTA Mood: Validation and Language Family Applications

This document describes validation workflows and language-specific applications for mood prediction.

---

## Validation Method

### How to Read TBTA Data (for validation only!)

TBTA encodes moods in verb phrase (VP) nodes:

```yaml
clause:
  children:
    - Part: VP
      children:
        - Constituent: look
          Mood: 'should' Obligation  # TBTA's label (for validation)
          Time: Later Today
          Aspect: Unmarked
```

### Validation Process

1. **Make prediction** using morphology + semantics + discourse (as described in mood-README.md)
2. **Read TBTA label** from Mood field in VP node
3. **Compare**: Do they match?
4. **Analyze mismatches**:
   - Did we miss a modal auxiliary?
   - Did we misinterpret discourse context?
   - Is TBTA possibly incorrect? (rare but possible)
   - Was Greek construction ambiguous?
5. **Refine method**: Update prediction rules based on systematic errors

### Accuracy Assessment

**Current Status**: Methodology defined based on Matthew 24 analysis

**Test Results (Matthew 24)**:
- Total Verbs: 316
- Mood Distribution:
  - Indicative: 299 (94.62%)
  - 'must' Obligation: 5 (1.58%)
  - 'might' Potential: 8 (2.53%)
  - 'should' Obligation: 1 (0.32%)
  - 'should not' Obligation: 1 (0.32%)
  - Forbidden Obligation: 2 (0.63%)

**Expected Accuracy by Mood Type**:
- **Indicative**: 90-95% (most common, clear morphology)
- **Imperative**: 95-100% (explicit morphology)
- **Subjunctive/Optative**: 85-90% (context-dependent)
- **Obligation**: 70-85% (requires semantic analysis)
- **Potential**: 70-80% (subtle distinctions)

**NOT 100% accuracy**: Prediction is harder than extraction; some cases are genuinely ambiguous even for expert linguists.

---

## Language-Specific Applications

### Languages with Rich Mood Systems

#### Turkish
**Mood System**: 5+ moods including evidential distinctions

| TBTA Mood | Turkish Construction | Notes |
|-----------|---------------------|-------|
| Indicative | -DI (past witnessed), -mIş (past unwitnessed) | Evidentiality required |
| 'must' Obligation | -mElI (necessity) | Strong obligation suffix |
| 'should' Obligation | -mElI (weak) or gerek | Context determines strength |
| 'might' Potential | -EbIlIr (possibility) | Can/might modal |
| Subjunctive | -E (optative-subjunctive) | Wishes, conditions |
| Imperative | Imperative suffixes | Direct commands |

**Challenge**: Map TBTA's 11 moods to Turkish's evidential + modal system
**Solution**: Combine TBTA mood + context to select Turkish evidential + modal marking

---

#### Japanese
**Mood System**: Politeness levels + modal particles

| TBTA Mood | Japanese Construction | Notes |
|-----------|---------------------|-------|
| Indicative | Plain/polite forms | です/だ endings |
| 'must' Obligation | なければならない (nakereba naranai) | Strong necessity |
| 'should' Obligation | べきだ (beki da), ほうがいい (hō ga ii) | Moderate advice |
| 'might' Potential | かもしれない (kamoshirenai) | Epistemic possibility |
| 'may' (permissive) | てもいい (te mo ii) | Permission granted |
| Imperative | Imperative forms + politeness | 行け (ike) vs 行ってください (itte kudasai) |

**Challenge**: Map TBTA obligation strength to Japanese keigo (politeness) levels
**Solution**: 'must' → plain obligation, 'should' → polite suggestion

---

#### Greek (Modern)
**Mood System**: Preserves some ancient distinctions

| TBTA Mood | Modern Greek | Notes |
|-----------|-------------|-------|
| Indicative | Οριστική | Direct preservation from Koine |
| Subjunctive | Υποτακτική (να + verb) | Used more broadly than ancient |
| 'must' Obligation | Πρέπει να (prepei na) | Strong necessity |
| 'should' Obligation | Θα έπρεπε (tha eprepe) | Conditional + prepei |
| 'might' Potential | Μπορεί να (borei na) | Possibility |
| Imperative | Προστακτική | Preserved from ancient |

**Advantage**: Close match to source language mood system
**Solution**: Nearly 1:1 mapping possible for most moods

---

#### Arabic
**Mood System**: Indicative, subjunctive, jussive

| TBTA Mood | Arabic Construction | Notes |
|-----------|---------------------|-------|
| Indicative | Muḍāriʿ مُضَارِع (present) or Māḍī مَاضِي (past) | Factual statements |
| Subjunctive | Manṣūb مَنْصُوب (subjunctive) | Purpose, result clauses |
| Jussive | Majzūm مَجْزُوم | Prohibitions, commands |
| 'must' Obligation | يَجِبُ (yajibu) + subjunctive | Strong necessity |
| 'should' Obligation | يَنْبَغِي (yanbaghī) + subjunctive | Moderate advice |
| 'might' Potential | قَد (qad) + imperfect | Epistemic possibility |
| Imperative | أَمْر (amr) | Direct commands |

**Challenge**: Map TBTA's semantic moods to Arabic's grammatical + modal system
**Solution**: Combine Arabic mood morphology with modal verbs

---

### Languages with Simple Mood Systems

#### English
**Mood System**: Primarily Indicative with modal verbs

| TBTA Mood | English Construction | Notes |
|-----------|---------------------|-------|
| Indicative | Simple verb forms | "he walks," "he walked," "he will walk" |
| 'must' Obligation | must, have to | Strong necessity |
| 'should' Obligation | should, ought to | Moderate advice |
| 'might' Potential | might, could, may (epistemic) | Weak possibility |
| 'may' (permissive) | may, can, allowed to | Permission |
| Forbidden Obligation | must not, cannot | Prohibition |
| Subjunctive | if... were (rare) | Mostly lost except formal |
| Imperative | Bare verb | "Go!", "Listen!" |

**Advantage**: TBTA mood values map almost directly to English modal verbs
**Challenge**: English "may" is ambiguous (permission vs possibility)
**Solution**: Use context to disambiguate

---

#### Mandarin Chinese
**Mood System**: Modal particles and auxiliary verbs

| TBTA Mood | Mandarin Construction | Notes |
|-----------|---------------------|-------|
| Indicative | Bare verb (no particle) | 他走 tā zǒu "he walks" |
| 'must' Obligation | 必须 bìxū, 得 děi | Strong necessity |
| 'should' Obligation | 应该 yīnggāi | Moderate advice |
| 'might' Potential | 可能 kěnéng, 也许 yěxǔ | Epistemic possibility |
| 'may' (permissive) | 可以 kěyǐ | Permission |
| 'cannot' | 不能 bù néng | Prohibition |
| Imperative | Bare verb (+ 吧 ba for polite) | 走！zǒu! "Go!" |

**Advantage**: Modal meanings expressed through separate words, not verb morphology
**Solution**: Map TBTA mood to appropriate Mandarin modal particle

---

#### Vietnamese
**Mood System**: Modal words, no verb morphology

| TBTA Mood | Vietnamese Construction | Notes |
|-----------|----------------------|-------|
| Indicative | Bare verb | Standard statements |
| 'must' Obligation | phải | Strong necessity |
| 'should' Obligation | nên | Advice |
| 'might' Potential | có thể | Possibility |
| 'may' (permissive) | được | Permission |
| Imperative | Particle hãy/đừng | Commands/prohibitions |

**Advantage**: Clear separation of modality from verb
**Solution**: Add appropriate modal word before verb

---

### Languages with No Obligatory Mood Marking

#### Indonesian/Malay
**Mood System**: Context-dependent, minimal grammatical marking

| TBTA Mood | Indonesian Construction | Notes |
|-----------|----------------------|-------|
| Indicative | Bare verb | dia pergi "he goes" |
| 'must' Obligation | harus | Strong necessity |
| 'should' Obligation | seharusnya | Advice |
| 'might' Potential | mungkin | Possibility |
| 'may' (permissive) | boleh | Permission |
| Imperative | Bare verb (+ -lah particle) | Pergi! "Go!" |

**Challenge**: Very minimal mood marking; relies on context
**Solution**: Use TBTA mood to decide when to add modal words

---

## Language Family Mapping Table

| Language Family | Mood Encoding | TBTA Mapping Complexity | Key Challenge |
|----------------|---------------|------------------------|---------------|
| **Indo-European** | | | |
| - Greek | 4 grammatical moods | Low (1:1 for many) | Preserve source mood distinctions |
| - Romance | Indicative, Subjunctive, Imperative | Medium | Choose subjunctive vs indicative |
| - Germanic (English, German) | Indicative + modal verbs | Low | Map to modal verbs |
| - Slavic | Indicative, Imperative | Medium | Aspect-mood interaction |
| **Sino-Tibetan** | | | |
| - Mandarin | Modal particles | Low | Select appropriate particle |
| - Tibetan | Evidential + modal | Medium | Map mood to evidential system |
| **Turkic** | | | |
| - Turkish | Evidential + modal suffixes | High | Mood + evidentiality combined |
| **Afro-Asiatic** | | | |
| - Arabic | Indicative, Subjunctive, Jussive | Medium | Grammatical + semantic moods |
| - Hebrew (Modern) | Similar to Arabic | Medium | Preserve Biblical nuances |
| **Austronesian** | | | |
| - Indonesian/Malay | Minimal marking, modal words | Low | Context + modal words |
| - Tagalog | Focus + modal particles | Medium | Aspect-mood interaction |
| **Japonic** | | | |
| - Japanese | Politeness + modal particles | Medium | Map obligation to keigo levels |
| **Niger-Congo** | | | |
| - Swahili | TAM prefixes | Medium | Mood fused with tense-aspect |

---

## Translation Workflow by Language Type

### For Morphologically Rich Languages (Greek, Arabic, Turkish)

1. **Check source morphology**: Does Greek/Hebrew have explicit mood marking?
2. **Map to target morphology**: Select corresponding target language mood form
3. **Add modal auxiliaries if needed**: For semantic moods not morphologically encoded
4. **Consider aspect-mood interaction**: Some moods require specific aspects

**Example (Greek → Modern Greek)**:
- Source: ἀκούσῃς (aorist subjunctive "you might hear")
- Target: να ακούσεις (na akouseis - subjunctive)
- Nearly direct mapping

---

### For Modal-Verb Languages (English, German, Romance)

1. **Default to indicative forms**: Unless TBTA mood ≠ Indicative
2. **Add modal verbs for obligations/potentials**:
   - 'must' Obligation → must/have to
   - 'should' Obligation → should/ought to
   - 'might' Potential → might/could
3. **Use imperative forms for commands**
4. **Rarely use subjunctive**: English subjunctive mostly lost

**Example (Greek → English)**:
- Source: δεῖ ἀκοῦσαι (it is necessary to hear)
- TBTA: 'must' Obligation
- Target: "must hear" or "have to hear"

---

### For Particle-Based Languages (Mandarin, Vietnamese)

1. **Use bare verb as base**: Unless imperative
2. **Add modal particle before verb**:
   - 'must' → 必须 bìxū (Mandarin)
   - 'should' → 应该 yīnggāi (Mandarin)
   - 'might' → 可能 kěnéng (Mandarin)
3. **Consider particle placement**: Usually pre-verbal
4. **Add politeness markers if needed**: 吧 ba, 请 qǐng

**Example (Greek → Mandarin)**:
- Source: δεῖ ἀκοῦσαι (it is necessary to hear)
- TBTA: 'must' Obligation
- Target: 必须听 bìxū tīng "must hear"

---

### For Context-Dependent Languages (Indonesian, Some Creoles)

1. **Use bare verb as default**
2. **Add modal words only when necessary**: TBTA marked moods
3. **Rely on discourse context**: For unmarked indicative
4. **Use particles for emphasis**: Commands, strong obligations

**Example (Greek → Indonesian)**:
- Source: δεῖ ἀκοῦσαι (it is necessary to hear)
- TBTA: 'must' Obligation
- Target: "harus mendengar" "must hear"

---

## Testing Priorities

### Immediate Testing (Phase 1)

**Goal**: Validate methodology on diverse mood types

1. **Test Indicative accuracy** (100+ verbs)
   - Expected: 90-95% accuracy
   - Use narrative passages (Gospels, Acts)

2. **Test Imperative recognition** (20+ verbs)
   - Expected: 95-100% accuracy (clear morphology)
   - Use Jesus' commands, apostolic directives

3. **Test 'must' vs 'should' distinction** (10+ each)
   - Expected: 75-85% accuracy (semantic nuance)
   - Use legal texts (Leviticus), wisdom (Proverbs)

---

### Short-Term Testing (Phase 2)

**Goal**: Test across Biblical genres

4. **Test Prohibition structures** (10+ verbs)
   - Forbidden vs 'should not'
   - Use Ten Commandments, negative imperatives

5. **Test Potential moods** (15+ verbs)
   - 'might' vs 'probable' vs 'definite'
   - Use prophetic texts (Isaiah, Revelation)

6. **Test Subjunctive/Optative** (10+ each)
   - Conditional clauses, wishes
   - Use epistles (Paul's prayers), prophecy

---

### Long-Term Testing (Phase 3)

**Goal**: Comprehensive validation and language transfer

7. **Test across genres**:
   - Narrative: Genesis, Gospels, Acts
   - Legal: Leviticus, Deuteronomy
   - Prophetic: Isaiah, Revelation
   - Wisdom: Proverbs, Ecclesiastes
   - Epistolary: Romans, Ephesians

8. **Measure inter-annotator agreement**:
   - Have multiple linguists predict moods independently
   - Calculate agreement rate
   - Document ambiguous cases

9. **Build language-specific transfer rules**:
   - Create mapping tables for 10+ target languages
   - Test translations with native speakers
   - Refine based on naturalness feedback

---

## Expected Challenges and Mitigations

### Challenge 1: Modal Auxiliary Ambiguity

**Issue**: δύναμαι can mean "I can" (ability) or "I might" (possibility)
**Mitigation**: Use context (ability → definite potential, possibility → 'might' potential)

### Challenge 2: Obligation Strength Continuum

**Issue**: δεῖ vs χρή distinction not always clear
**Mitigation**: Consider urgency, authority, consequences in context

### Challenge 3: Imperative vs Strong Indicative

**Issue**: "You will go" can be prediction OR command
**Mitigation**: Check IlLocutionary Force, speaker authority

### Challenge 4: Subjunctive vs Indicative in Conditionals

**Issue**: Greek uses both in conditional clauses
**Mitigation**: First-class conditions (εἰ + ind) = Indicative; third-class (ἐάν + subj) = Subjunctive

### Challenge 5: Language Lacks Mood Distinction

**Issue**: Target language can't encode TBTA mood grammatically
**Mitigation**: Use footnotes, study notes, or accept semantic loss

---

## Validation Checklist

When testing mood predictions:

- [ ] Document source text (Greek/Hebrew) with morphology
- [ ] Record English gloss
- [ ] Note verse reference and genre
- [ ] Make blind prediction using decision tree
- [ ] Record which gateway features triggered prediction
- [ ] Note confidence level (High/Medium/Low)
- [ ] Load TBTA data and extract actual mood
- [ ] Compare predicted vs actual
- [ ] If mismatch:
  - [ ] Check for missed modal auxiliaries
  - [ ] Verify Greek/Hebrew morphology parsing
  - [ ] Re-examine discourse context
  - [ ] Document as edge case if ambiguous
- [ ] Update accuracy metrics by mood type
- [ ] Refine decision rules if systematic error found

---

## Limitations and Edge Cases

### Limitation 1: Implicit Imperatives
**Pattern**: Commands phrased as questions
**Example**: "Should we not obey God?" (rhetorical → obligation)
**Solution**: Use clause-level IlLocutionary Force as secondary check

### Limitation 2: Mixed Moods in Coordination
**Pattern**: Multiple verbs with different moods coordinated
**Example**: "He should listen and must obey" (different obligation strengths)
**Solution**: Analyze each VP independently

### Limitation 3: Rare Moods (Optative)
**Pattern**: Optative rarely appears in Koine Greek
**Example**: Paul's benedictions, prayers
**Solution**: Expand test corpus to include epistles

### Limitation 4: Hebrew Modal Ambiguity
**Pattern**: Hebrew yiqtol can be future indicative OR jussive
**Example**: יִשְׁמַע "he will hear" vs "let him hear"
**Solution**: Rely on context, discourse markers

---

## Future Extensions

1. **Multi-translation validation**: Use 900+ translations to verify mood predictions
2. **Confidence scoring**: Develop quantitative confidence metrics per mood type
3. **Discourse patterns**: Analyze mood sequencing across verses/chapters
4. **Translation matrices**: Create comprehensive target language mapping guides
5. **Nested clause analysis**: How moods interact in embedded structures
6. **Exception handling**: Build catalog of edge cases with resolution strategies

---

**Document Version**: 2.0
**Last Updated**: 2025-11-07
**Test Data**: Matthew 24 (316 verbs, 51 verses)
**Methodology Status**: Defined, awaiting comprehensive validation
