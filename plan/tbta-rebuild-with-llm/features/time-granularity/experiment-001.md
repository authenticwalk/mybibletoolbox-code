# Experiment 001: TBTA Time/Tense Predictions

**Date**: November 4, 2025
**Focus**: Testing time granularity predictions across narrative and prophetic passages
**Key Distinctions**: Present vs Discourse (timeless), Immediate Future vs Remote Future, Historic Past vs Recent Past

---

## Objectives

Test TBTA's ability to predict fine-grained temporal distinctions in Bible translations across:
1. **Temporal distance** (immediate vs remote, hodiernal vs pre-hodiernal)
2. **Narrative context** (historic narrative vs discourse vs prophecy)
3. **Evidential tense** (witnessed/participated vs reported)
4. Language families with complex tense systems (Bantu, Quechuan, Trans-New Guinea)

---

## Hypothesis Framework

Based on the time-granularity research, we expect:

### Hypothesis 1: Narrative Past vs Prophetic Future
- Historic narrative passages should predict "remote past" or "narrative past" markers
- Prophetic future passages should distinguish "immediate future" (imminent) vs "remote future" (eschatological)
- This should appear in language families that grammaticalize temporal remoteness (Quechuan, Bantu, Trans-New Guinea)

### Hypothesis 2: Discourse vs Narrative Tense Shift
- Direct speech (e.g., parables, teachings) should shift to present/timeless tense
- Surrounding narrative frame should stay in past tense
- Languages with discourse tense markers should reflect this

### Hypothesis 3: Aspect-Based Systems
- Mayan and other aspect-based languages should mark completive/incompletive rather than temporal distance
- Prophecy should use incompletive/potential aspects to mark future unreality

---

## Test Cases

### TEST 1: Recent Past Narrative (Mark 1:21-28)
**Passage**: Mark 1:21-28 - Jesus teaching in synagogue, demon-possessed man

```
Verse 1:21 - "They went into Capernaum"
Verse 1:22 - "They were astonished at his teaching"
Verse 1:23 - "A man with an unclean spirit was in their synagogue"
Verse 1:24 - "What have you to do with us?"
Verse 1:27 - "He has authority over unclean spirits"
Verse 1:28 - "Immediately his fame spread"
```

**Expected Predictions**:
- **Quechuan languages** (South Conchucos Quechua): Should use "immediate past" (-rqa/-ra) for main narrative events, "remote past" (-sqa/-sha) for orientation
- **Bantu languages** (Gĩkũyũ): Should use closer past tenses (today's past / recent past grades)
- **Mayan languages**: Should use perfective aspect throughout (main narrative action completed)

**Prediction Test**:
- [ ] Does LLM recognize this as "recent narrative" rather than "ancient past"?
- [ ] Does it predict hodiernal/today-past markers in languages that distinguish them?
- [ ] Does it correctly identify main narrative events vs background/orientation?

---

### TEST 2: Ancient Historical Narrative (Genesis 1:1-5)
**Passage**: Genesis 1:1-5 - Creation account

```
Verse 1:1 - "In the beginning, God created the heavens and the earth"
Verse 1:2 - "The earth was formless and empty"
Verse 1:3 - "God said, 'Let there be light'"
Verse 1:4 - "God saw that the light was good"
Verse 1:5 - "God called the light day"
```

**Expected Predictions**:
- **Quechuan**: Should use "remote past" (-sqa/-sha) for these ancient events beyond speaker's lifetime
- **Bantu**: Should use "ancient past" / "remote past" grades
- **Mayan**: Perfective aspect same as recent narrative, but context markers might differ

**Prediction Test**:
- [ ] Does LLM distinguish ancient from recent past?
- [ ] Does it recognize this distinction should be marked in language families with graded pasts?
- [ ] Does it avoid confusing chronological distance with narrative distance?

---

### TEST 3: Discourse/Timeless Present (Matthew 5:3-10 - Beatitudes)
**Passage**: Matthew 5:3-10 - Jesus' teachings in direct speech

```
Verse 5:3 - "Blessed are the poor in spirit"
Verse 5:4 - "Blessed are those who mourn"
Verse 5:5 - "Blessed are the meek"
Verse 5:7 - "Blessed are the merciful"
Verse 5:9 - "Blessed are the peacemakers"
Verse 5:10 - "Blessed are those who are persecuted"
```

**Expected Predictions**:
- Should switch to **present tense** or **timeless aspect** (universal truths)
- NOT narrative past like surrounding context
- **Mayan languages**: Should shift to incompletive aspect
- **Turkish**: Might use present tense without -mIş (inferential) marker
- **Bantu**: May shift to present or gnomic aspect

**Prediction Test**:
- [ ] Does LLM recognize discourse markers should signal timeless/universal meaning?
- [ ] Does it predict present/gnomic tense despite historical distance?
- [ ] Does it handle the switch from narrative frame to direct speech correctly?

---

### TEST 4: Immediate Future - Prophecy (Matthew 24:29-31 - Olivet Discourse)
**Passage**: Matthew 24:29-31 - Jesus predicting near future

```
Verse 24:29 - "Immediately after the distress of those days... the sun will be darkened"
Verse 24:30 - "Then will appear the sign of the Son of Man in heaven"
Verse 24:31 - "He will send his angels... and gather his elect"
```

**Expected Predictions**:
- Should mark **immediate future** (imminent within reader's lifetime or generation)
- Quechuan & Bantu languages: May use special "proximal future" markers vs distant eschatology
- **Mayan**: Incompletive/potential aspect to mark unreality
- Language distinction: This future feels different from Test 5 (eschatological)

**Prediction Test**:
- [ ] Does LLM recognize "immediate future" tone?
- [ ] Does it predict different future marking than eschatological prophecy?
- [ ] Does context words like "immediately," "this generation" trigger proximal future prediction?

---

### TEST 5: Remote Future - Eschatology (Revelation 21:1-4)
**Passage**: Revelation 21:1-4 - New creation vision

```
Verse 21:1 - "I saw a new heaven and a new earth"
Verse 21:2 - "I saw the holy city... coming down"
Verse 21:3 - "God's dwelling place is now among the people"
Verse 21:4 - "There will be no more death or mourning"
```

**Expected Predictions**:
- Should mark **remote/distant future** (eschatological, beyond normal time experience)
- **Quechuan**: Different future marking than Test 4
- **Bantu**: Remote future grades
- **Mayan**: Potential aspect for counterfactual/hypothetical future
- May also show evidential marking (vision/revelation source)

**Prediction Test**:
- [ ] Does LLM distinguish this from immediate future?
- [ ] Does it recognize eschatological/visionary context affects temporal marking?
- [ ] Does it predict temporal remoteness proportional to theological distance?

---

### TEST 6: Indirect/Reported Past (Luke 24:34 - Resurrection Testimony)
**Passage**: Luke 24:34 - Disciples report resurrection

```
Verse 24:34 - "The Lord has risen and has appeared to Simon"
```

**Expected Predictions**:
- **Turkish**: Should predict -mIş (inferential) rather than -DI (witnessed), since disciples reporting what they didn't directly experience
- **Komi-Zyrian**: Indirect past marker
- Other languages: May use "reported" or "hearsay" evidential marking
- Different from direct narrative of actual events

**Prediction Test**:
- [ ] Does LLM recognize reported vs witnessed distinction?
- [ ] Does it predict evidential marking in languages that require it?
- [ ] Does context ("has appeared") hint at indirect evidence source?

---

## Experiment Design

### Method A: Blind Prediction
1. For each verse/passage, provide only:
   - The text
   - Target language information
   - Instruction: "What temporal markings would translate this correctly into [Language]?"
2. Record LLM prediction
3. Compare to expected temporal markers based on:
   - Known language tense systems (from time-granularity research)
   - Grammatical requirements of the language
   - Narrative/discourse context

### Method B: Contextual Reasoning
1. Provide verse + surrounding context (2-3 verses before/after)
2. Ask: "Why would [Language] mark this differently from the surrounding verses?"
3. Evaluate if reasoning correctly identifies temporal distinctions

### Method C: Feature Isolation
1. Test just temporal remoteness: "Is this immediate or remote past/future?"
2. Test just evidentiality: "Did the speaker participate or report this event?"
3. Test just aspect: "Is this action complete or ongoing?"
4. Combine predictions to see if they integrate properly

---

## Evaluation Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| **Temporal Accuracy** | Correctly distinguishes past/present/future | 85%+ |
| **Remoteness Precision** | Correctly identifies immediate vs remote | 80%+ |
| **Narrative vs Discourse** | Switches tense appropriately for direct speech | 90%+ |
| **Evidentiality** | Marks witnessed vs reported correctly | 75%+ (only in languages with obligatory marking) |
| **Context Sensitivity** | Uses surrounding verses to make decisions | 70%+ |

---

## Results

### Test 1: Recent Past Narrative (Mark 1:21-28)

**LLM Prediction Attempt 1**:
- [ ] (Pending execution)

**Status**: Not yet executed

---

### Test 2: Ancient Historical Narrative (Genesis 1:1-5)

**LLM Prediction Attempt 1**:
- [ ] (Pending execution)

**Status**: Not yet executed

---

### Test 3: Discourse/Timeless (Matthew 5:3-10)

**LLM Prediction Attempt 1**:
- [ ] (Pending execution)

**Status**: Not yet executed

---

### Test 4: Immediate Future (Matthew 24:29-31)

**LLM Prediction Attempt 1**:
- [ ] (Pending execution)

**Status**: Not yet executed

---

### Test 5: Remote Future (Revelation 21:1-4)

**LLM Prediction Attempt 1**:
- [ ] (Pending execution)

**Status**: Not yet executed

---

### Test 6: Reported Past (Luke 24:34)

**LLM Prediction Attempt 1**:
- [ ] (Pending execution)

**Status**: Not yet executed

---

## Lessons Learned

(To be updated as tests are executed)

---

## Next Steps

1. Execute blind predictions for each test case
2. Compile language-specific accuracy data
3. Identify patterns in failures (missing context? language knowledge gaps?)
4. Refine prompts to improve temporal distinction recognition
5. Test on languages with complex tense systems (Quechuan, Bantu, Trans-New Guinea examples)
6. Compare results to actual TBTA annotations if available

---

## References

- Time Granularity Research: `/plan/tbta-project-local/features/time-granularity/README.md`
- TBTA Feature Reproduction Framework: `/plan/tbta-project-local/experiments/FRAMEWORK.md`

