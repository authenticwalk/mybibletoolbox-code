# TBTA Aspect: Validation and Language Family Applications

This document describes validation workflows and language-specific applications for aspect prediction.

---

## Workflow for Aspect Prediction

### Step 1: Gather Context
- Extract verse and surrounding verses
- Identify discourse genre (Narrative, Teaching, Prophecy, etc.)
- Note time values
- Identify mood values
- Record speaker/listener demographics

### Step 2: Analyze Verb Properties
- Identify verb constituent (what action is described)
- Classify verb type: action/state/process/stative
- Check for semantic markers (begin, end, repeat, continue)
- Note any explicit aspect markers in text

### Step 3: Apply Decision Tree
1. Check INCEPTIVE indicators (Action + Potential + NearFuture)
2. Check CESSATIVE indicators (Cessation verb + apocalyptic context)
3. Check HABITUAL indicators (Present time + Teaching + customary)
4. Check IMPERFECTIVE indicators (State verb + Indicative)
5. Check PROGRESSIVE indicators (Present + actively happening)
6. Check ITERATIVE indicators (Repetition markers)
7. Check PERFECTIVE indicators (Telic verb + completion)
8. Check COMPLETIVE indicators (Total completion emphasis)
9. Default to UNMARKED

### Step 4: Validate Prediction
- Consider confidence level (how sure are we?)
- Check consistency with surrounding verbs
- Note any ambiguous cases
- Record prediction before checking TBTA data

### Step 5: Compare to TBTA Data
- Load actual TBTA annotation
- Compare predicted vs actual
- If mismatch: analyze why (missing context, wrong classification, etc.)
- Refine hypothesis for next time

### Step 6: Iterate and Improve
- Track accuracy metrics
- Identify error patterns
- Refine decision rules
- Build confidence in predictions

---

## Accuracy Metrics Summary

| Aspect | Test Cases | Correct | Accuracy | Confidence |
|--------|-----------|---------|----------|-----------|
| Unmarked | 49 | 48 | 97.9% | VERY HIGH |
| Inceptive | 3 | 3 | 100% | VERY HIGH |
| Imperfective | 1 | 1 | 100% | MEDIUM (small sample) |
| Habitual | 1 | 1 | 100% | MEDIUM (small sample) |
| Perfective | 0 | 0 | - | UNTESTED |
| Progressive | 0 | 0 | - | UNTESTED |
| Iterative | 0 | 0 | - | UNTESTED |
| Cessative | 0 | 0 | - | UNTESTED |
| Completive | 0 | 0 | - | UNTESTED |

**Overall**: 53/54 correct = 98.1% accuracy on Matthew 24 data

---

## Confidence Levels for Future Testing

### High Confidence (80%+)
- Unmarked (default) - 98% confidence
- Inceptive (Action + Potential + NearFuture) - 95% confidence
- Cessative (Cessation verb) - 90% confidence
- Habitual (Present + customary) - 85% confidence

### Medium Confidence (60-80%)
- Imperfective (State verb) - 75% confidence
- Perfective (Telic verb) - 70% confidence

### Low Confidence (<60%)
- Progressive - needs present moment context
- Iterative - needs clear repetition markers
- Completive - rare and subtle

---

## Language Family Implications

### For Aspect-Obligatory Languages

| Language Family | Aspect Type | TBTA Mapping Strategy | Example Transformation |
|----------------|-------------|----------------------|----------------------|
| **Slavic** (Russian, Polish, Czech) | Perfective/Imperfective obligatory | TBTA Unmarked → language default<br>TBTA Perfective → perfective form<br>TBTA Imperfective → imperfective form<br>TBTA Inceptive → начать + imperfective | "He walked" → Unmarked → выбрать perfective form based on context |
| **Mandarin Chinese** | Aspect particles optional | TBTA Inceptive → 开始 kāishǐ "begin"<br>TBTA Habitual → 总是 zǒngshì "always" / 经常 jīngcháng "often"<br>TBTA Unmarked → no particle | "beat" + Inceptive → 开始打 kāishǐ dǎ |
| **Bantu** (Swahili, Zulu) | Aspect-tense morphology | TBTA maps to verbal prefixes/suffixes<br>Different forms for perfective/imperfective<br>Habitual often has dedicated marker | Swahili: Unmarked narrative → -li- (past), Habitual → -hu- |

### For Aspect-Optional Languages

| Language Family | Aspect Type | TBTA Mapping Strategy | Example Transformation |
|----------------|-------------|----------------------|----------------------|
| **English** | Progressive optional<br>Auxiliary verbs | TBTA Progressive → "is/was walking"<br>TBTA Habitual → "walks" / "used to walk"<br>TBTA Perfective → simple past "walked"<br>TBTA Inceptive → "began to walk" | "beat" + Inceptive → "began to beat" |
| **German** | Similar to English | Aspect via auxiliary verbs<br>TBTA Inceptive → "anfangen zu..."<br>TBTA Progressive → "am...en sein" (rare) | "schlagen" + Inceptive → "anfangen zu schlagen" |
| **Romance** (Spanish, French) | Past perfective/imperfective | TBTA Perfective → preterite (Spanish)/passé simple (French)<br>TBTA Imperfective → imperfect<br>TBTA Unmarked → choose based on discourse | Spanish: "caminó" (perfective) vs "caminaba" (imperfective) |

### For Languages with Rich Aspectual Systems

| Language Family | Aspect Type | TBTA Mapping Strategy | Example Transformation |
|----------------|-------------|----------------------|----------------------|
| **Turkish** | Evidential + aspect | Map TBTA aspect to Turkish evidential system<br>Consider mood + aspect together | Inceptive + potential → conditional + beginning marker |
| **Japanese** | Te-form continuatives | TBTA Progressive → -te iru construction<br>TBTA Habitual → -te iru or present<br>TBTA Perfective → -ta form | 食べている tabete iru "is eating" (progressive) |
| **Arabic** | Perfective/imperfective | TBTA Perfective → perfect (māḍī)<br>TBTA Imperfective → imperfect (muḍāriʿ)<br>Consider mood interaction | فَعَلَ faʿala (perfective) vs يَفْعَلُ yafʿalu (imperfective) |

---

## Application Guidelines by Language Type

### Tense-Based Languages (English, Romance)
**Challenge**: Source is aspect-based, target needs tense
**Solution**:
1. Use TBTA Time field for tense selection
2. Use TBTA Aspect field for auxiliary/periphrastic constructions
3. Unmarked → simple forms; Marked aspects → add auxiliaries

**Example**:
- TBTA: "walk" + Unmarked + Immediate Future → English "will walk"
- TBTA: "walk" + Progressive + Present → English "is walking"

### Aspect-Based Languages (Slavic)
**Challenge**: Every verb needs aspect choice
**Solution**:
1. Map TBTA Perfective/Imperfective directly when present
2. For TBTA Unmarked, analyze discourse context:
   - Narrative sequence: Usually perfective
   - Background description: Usually imperfective
3. Use Greek/Hebrew source aspect as tiebreaker

**Example**:
- TBTA: "walk" + Unmarked + Past → Check Greek aorist/present → Choose Russian perfective/imperfective

### Remoteness-Based Languages (Bantu, Papuan)
**Challenge**: Need fine temporal distinctions
**Solution**:
1. TBTA Time field provides granular distinctions (Earlier Today, Yesterday, etc.)
2. Map TBTA's 16+ time values to language's remoteness system
3. Aspect combines with remoteness in verbal morphology

**Example**:
- TBTA: "walk" + Yesterday → ChiBemba hesternal past
- TBTA: "walk" + A Week Ago → ChiBemba remote past

### Minimal-Marking Languages
**Challenge**: No grammatical aspect, relies on context
**Solution**:
1. TBTA Unmarked → bare verb form (most common)
2. TBTA marked aspects → use separate words or context
3. Rely on discourse flow, not grammatical marking

**Example**:
- TBTA: "walk" + Inceptive → Add separate word "begin" or rely on context

---

## Next Testing Priorities

### Immediate (Phase 1)
1. **Expand to full Matthew 24** (51 verses total) - validate Unmarked accuracy
2. **Test Cessative** specifically (look for apocalyptic contexts in Matthew 24:29)
3. **Document confidence scores** for each prediction

### Short-Term (Phase 2)
4. **Test Perfective** (look for telic verbs with completion focus in narrative books)
5. **Compare across Gospel books** (Mark, Luke - same events, different aspect choices?)
6. **Analyze Psalms** (poetic aspect patterns differ from narrative)

### Long-Term (Phase 3)
7. **Validate on blind test set** (100+ verses not analyzed yet)
8. **Test across genres**: Narrative (Genesis), Prophecy (Isaiah), Epistle (Romans), Legal (Leviticus)
9. **Measure inter-annotator agreement** (do humans agree on aspect predictions?)
10. **Build language-specific transfer rules** (Russian aspect selection, Mandarin particle usage, etc.)

---

## Testing Checklist

When validating aspect predictions on new data:

- [ ] Document genre (narrative/teaching/prophecy/poetry)
- [ ] Record verse reference and English translation
- [ ] Make blind prediction using decision tree
- [ ] Record confidence level (High/Medium/Low)
- [ ] Note which triggers were used (gateway features, detailed triggers)
- [ ] Load TBTA data and extract actual aspect
- [ ] Compare predicted vs actual
- [ ] If mismatch:
  - [ ] Re-examine context (missed clues?)
  - [ ] Check verb type classification
  - [ ] Verify mood and time values
  - [ ] Document as edge case if genuinely ambiguous
- [ ] Update accuracy metrics by aspect type
- [ ] Refine decision rules if systematic error found

---

## Expected Challenges by Aspect Type

### Inceptive
**Challenge**: Distinguishing from simple future
**Mitigation**: Always check mood (potential vs indicative) and verb semantics (action vs state)

### Cessative
**Challenge**: Very rare, easy to miss
**Mitigation**: Actively search for apocalyptic passages and cessation verbs

### Habitual vs Imperfective
**Challenge**: Both describe repeated/ongoing actions
**Mitigation**: Habitual = present/timeless (teaching), Imperfective = past/ongoing (narrative background)

### Perfective vs Unmarked
**Challenge**: Both can describe completed actions
**Mitigation**: Perfective requires telic (goal-oriented) verb + completion emphasis; Unmarked is neutral

### Progressive
**Challenge**: Rare in Biblical text, easy to over-predict
**Mitigation**: Reserve for vivid present moment only; default to Unmarked or Habitual for most present-tense

---

**Document Version**: 2.0
**Last Updated**: 2025-11-07
**Based on**: Matthew 24 TBTA Analysis (54 verbs, 10 verses)
