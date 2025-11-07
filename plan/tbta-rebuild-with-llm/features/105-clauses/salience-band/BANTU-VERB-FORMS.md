# Bantu Verb Forms and Salience Band

This document provides detailed patterns for how Bantu languages encode salience band distinctions through verb morphology. The systematic split between foreground and background verb forms makes salience band annotation **CRITICAL** for accurate translation into Bantu languages.

## Overview

Bantu languages (89 in TBTA corpus) systematically distinguish:
- **Mainline/Foreground**: Main storyline events (Primary/Secondary salience)
- **Sequential/Consecutive**: Rapid-fire event chains (Primary salience)
- **Background/Circumstantial**: Setting, explanation, simultaneous actions (Background salience)

This is NOT optional stylistic variation—it is **grammatically required** for narrative coherence in Bantu languages.

## Swahili (swh) - Detailed Paradigm

### Past Tense Forms

| Form | Morphology | Discourse Function | Salience Band |
|------|------------|-------------------|---------------|
| **-li- past** | a-li-enda | Simple past, mainline OR setting | Primary OR Setting (context-dependent) |
| **-ka- narrative** | a-ka-enda | Sequential narrative, mainline | Primary (foreground chain) |
| **-ki- circumstantial** | a-ki-enda | Background, simultaneous, condition | Background |
| **-me- perfect** | a-me-enda | Resultant state, anterior | Background (stative result) |

### Usage Examples

**Genesis 1 in Swahili** (illustrating salience distinctions):

```
GEN 1:1 - Mwanzoni Mungu aliUMBA mbingu na nchi.
          "In beginning God CREATED heaven and earth"
          Form: a-li-umba (simple past)
          Salience: Setting (discourse frame)

GEN 1:2 - Nchi ILIKUWA bila umbo na tupu...
          "Earth WAS without form and void..."
          Form: i-li-kuwa (stative past)
          Salience: Background (descriptive state)

GEN 1:3 - Mungu AKASEMA, "Iwe nuru"
          "God SAID, 'Let there be light'"
          Form: a-ka-sema (narrative sequential)
          Salience: Pivotal (first creative word)

GEN 1:4 - Mungu AKAONA kuwa nuru ni njema,
          "God SAW that light was good"
          Form: a-ka-ona (narrative sequential)
          Salience: Primary (mainline evaluation)

          AKATENGANISHA nuru na giza.
          "HE-SEPARATED light from darkness"
          Form: a-ka-tenganisha (narrative sequential)
          Salience: Primary (mainline action)

GEN 1:5 - Mungu AKAITA nuru Mchana...
          "God CALLED light Day..."
          Form: a-ka-ita (narrative sequential)
          Salience: Secondary (consequential naming)
```

**Key Pattern**:
- **Setting** (v1): -li- (establishes frame)
- **Background** (v2): -li- stative (describes state)
- **Foreground chain** (v3-5): -ka- (sequential mainline)

### When -li- vs -ka-?

**Use -li- past** for:
1. Scene-setting (GEN 1:1 - "In beginning God created...")
2. First event after discourse break
3. Standalone events (not in rapid sequence)
4. Background states with stative verbs

**Use -ka- narrative** for:
1. Sequential event chains (v3 → v4 → v5)
2. Mainline foreground progression
3. "And then..." narrative flow
4. Primary/Secondary salience clauses

**Use -ki- circumstantial** for:
1. Simultaneous actions ("While X-ing, Y happened")
2. Conditional/temporal subordination ("When/If X...")
3. Background explanations
4. Manner ("By X-ing, he accomplished Y")

## Kinyarwanda (kin) - Related Patterns

Kinyarwanda has similar but distinct narrative forms:

| Form | Function | Salience |
|------|----------|----------|
| **a-ra-** present habitual | Background (general truth) | Background |
| **a-á-** remote past | Setting (distant events) | Setting |
| **-a-** near past | Mainline (recent events) | Primary |
| **-ara-** progressive | Background (ongoing) | Background |
| **-ca** consecutive | Sequential foreground | Primary |

**Key difference from Swahili**: Kinyarwanda has tense distance (remote vs near) as additional factor.

## Luganda (lug) - Narrative Forms

| Form | Function | Salience |
|------|----------|----------|
| **-a-...-a** simple past | Mainline | Primary |
| **ne-...-a** narrative past | Sequential foreground | Primary |
| **nga-** circumstantial | Background/simultaneous | Background |
| **-dde** perfect | Resultant state | Background |

**Example** (Genesis 1:3):
```
Katonda n'agamba nti, "Omusana gubeerewo"
God    NE-say  that  light    let-be
Form: ne-a-gamba (narrative past)
Salience: Pivotal
```

## Chichewa (nya) - Narrative Tenses

| Form | Function | Salience |
|------|----------|----------|
| **ana-** remote past | Setting/backstory | Setting |
| **a-** recent past | Mainline | Primary |
| **-ta-** anterior | Background (prior events) | Background |
| **-ka-** consecutive | Sequential foreground | Primary |

## Shona (sna) - Discourse Marking

| Form | Function | Salience |
|------|----------|----------|
| **aka-** narrative past | Mainline events | Primary |
| **-chi-** simultaneous | Background | Background |
| **-ka** perfect | Resultant state | Background |

## Cross-Bantu Patterns

### Universal Distinctions

All Bantu narrative systems distinguish:

1. **Mainline/Foreground** forms (Primary/Secondary salience)
   - Swahili: -ka-
   - Luganda: ne-
   - Chichewa: -ka-
   - Shona: aka-

2. **Background/Circumstantial** forms (Background salience)
   - Swahili: -ki-
   - Luganda: nga-
   - Kinyarwanda: -ara-
   - All: perfect/resultant forms

3. **Setting/Frame** forms (Setting salience)
   - Swahili: -li- (first in sequence)
   - Kinyarwanda: remote past -á-
   - Chichewa: remote past ana-

### Prototypical Narrative Structure

```
[SETTING: Simple past / Remote past]
  Once upon a time, there was a king...

[BACKGROUND: Stative / Circumstantial]
  He was wise and just. While ruling, he noticed...

[PIVOTAL: Narrative form]
  One day, an enemy approached!

[PRIMARY: Narrative consecutive chain]
  The king called his warriors.
  They gathered weapons.
  They marched to battle.

[SECONDARY: Narrative consecutive, lower prominence]
  Messengers announced the victory.
  People celebrated in streets.

[BACKGROUND: Circumstantial / Perfect]
  Peace had been restored.
  The kingdom prospered thereafter.
```

## Translation Strategy

### Step 1: Identify Salience Band
- Pivotal / Primary → Foreground forms
- Secondary → Foreground forms (may use non-consecutive)
- Background → Background forms (circumstantial, perfect)
- Setting → Frame forms (simple past, remote past)

### Step 2: Map to Target Verb Form

**For Swahili**:
- Pivotal → -ka- (if in sequence) OR -li- (if discourse break)
- Primary → -ka- (sequential) OR -li- (standalone)
- Secondary → -ka- OR -li- (depends on narrative flow)
- Background → -ki- (circumstantial) OR -me- (perfect)
- Setting → -li- (scene anchor)

**For Kinyarwanda**:
- Pivotal → -ca (consecutive) OR -a- (near past)
- Primary → -ca (consecutive) OR -a-
- Secondary → -a- (near past)
- Background → -ara- (progressive) OR -dde (perfect)
- Setting → -á- (remote past)

### Step 3: Check Narrative Coherence

**Red flags**:
- Foreground form (-ka-) used for Background salience
- Background form (-ki-) used for Primary mainline
- Breaking -ka- chain without discourse reason
- Using -li- mid-sequence (should be -ka-)

### Step 4: Native Speaker Validation

**Critical**: Have native Bantu speaker verify:
1. Does -ka- chain feel natural?
2. Are background forms appropriate?
3. Is discourse structure clear?
4. Are pivotal moments marked?

## John 9:1-7 Example (Swahili)

**Verse-by-verse salience and verb form mapping**:

```
v1: Alipopita Yesu, ALIMWONA mtu mmoja aliyezaliwa kipofu.
    "As-passing Jesus, HE-SAW man one who-was-born blind"
    Form: a-li-mwona (simple past, first event after setting)
    Salience: Primary (initiating event)

v2: Wanafunzi wake WAKAMUULIZA...
    "Disciples his ASKED-him..."
    Form: wa-ka-muuliza (narrative consecutive)
    Salience: Primary (mainline dialogue)

v3: Yesu AKAJIBU...
    "Jesus ANSWERED..."
    Form: a-ka-jibu (narrative consecutive)
    Salience: Primary (mainline response)

v6: Akisema hivi, AKATEMEA mate ardhini,
    "Having-said this, HE-SPAT saliva on-ground"
    Form: a-ki-sema (circumstantial, backgrounded temporal)
         a-ka-temea (narrative consecutive, mainline)
    Salience: Background (temporal frame) + Primary (main action)

    AKAFANYA udongo kwa mate,
    "HE-MADE mud with saliva"
    Form: a-ka-fanya (narrative consecutive)
    Salience: Primary (mainline sequence)

    AKAPAKA udongo huo machoni mwa huyo kipofu.
    "HE-SMEARED mud that on-eyes of that blind-one"
    Form: a-ka-paka (narrative consecutive)
    Salience: Primary (mainline sequence)

v7: AKAMWAMBIA...
    "HE-TOLD-him..."
    Form: a-ka-mwambia (narrative consecutive)
    Salience: Primary (mainline command)
```

**Pattern**:
- Unbroken -ka- chain (v2-v7) = Primary salience foreground
- -ki- subordinate (v6a) = Background temporal frame
- Each -ka- advances the story sequentially

## Common Translation Errors

### Error 1: Using -ka- for Background
**Wrong**:
```
Nchi ikawa bila umbo... (GEN 1:2)
"Earth -KA-was without form"
```
**Why wrong**: -ka- marks foreground, but this is background description
**Correct**:
```
Nchi ilikuwa bila umbo...
"Earth -LI-was without form"
```

### Error 2: Breaking -ka- Chain Mid-Sequence
**Wrong**:
```
Mungu akasema (v3), akaona (v4), alitenganisha (v4b)
"God said (KA), saw (KA), separated (LI)"
```
**Why wrong**: Switching to -li- mid-chain breaks narrative flow
**Correct**:
```
Mungu akasema (v3), akaona (v4), akatenganisha (v4b)
"God said (KA), saw (KA), separated (KA)"
```

### Error 3: Using Stative -ki- for Mainline
**Wrong**:
```
Akienda mjini, akifanya maajabu...
"He-KI-going to-town, he-KI-doing miracles"
```
**Why wrong**: -ki- marks background/simultaneous, not sequential mainline
**Correct**:
```
Akaenda mjini, akafanya maajabu...
"He-KA-went to-town, he-KA-did miracles"
```

### Error 4: Ignoring Genre Differences
**Problem**: Using narrative -ka- forms in epistles/teaching
**Wrong** (Romans 3:23):
```
Wote wakatenda dhambi, wakakosa utukufu wa Mungu.
"All -KA-sinned, -KA-fell-short of glory of God"
```
**Why wrong**: Epistles state theological facts, not narrative sequence
**Correct**:
```
Wote wametenda dhambi, na kukosa utukufu wa Mungu.
"All have-sinned (PERFECT), and to-fall-short of glory of God (INFINITIVE)"
```

## Implementation Notes

### For TBTA Data Generation

1. **Analyze Greek/Hebrew verb forms first**
   - Greek aorist indicative → likely Primary
   - Greek imperfect → likely Background
   - Hebrew wayyiqtol → likely Primary
   - Hebrew qatal → likely Background/Setting

2. **Check discourse structure**
   - Sequential events → Primary (-ka- in Swahili)
   - Descriptive states → Background (-ki- or stative)
   - Turning points → Pivotal (-ka- or -li-)

3. **Validate with published Bantu translations**
   - Compare TBTA annotations with Swahili Bible
   - Check if -ka- forms align with Primary salience
   - Check if -ki- forms align with Background salience

4. **Document mismatches**
   - Where does Swahili use -li- instead of -ka-?
   - Where does published translation disagree with annotation?
   - Are there genre-specific patterns?

### Quality Assurance

**Validation metrics**:
- **Primary salience** → 70%+ should use foreground forms (-ka-, ne-, consecutive)
- **Background salience** → 70%+ should use background forms (-ki-, -ara-, perfect)
- **Setting salience** → 80%+ should use frame forms (-li-, remote past)

**Red flags for review**:
- Primary salience with perfect/stative verb
- Background salience with narrative consecutive
- Unbroken -ka- chain >10 clauses (check if all truly foreground)
- Genre mismatch (narrative forms in epistles)

## Further Resources

**Published Grammars**:
- Ashton, E.O. (1944). *Swahili Grammar* - narrative tense system
- Kimenyi, Alexandre (1980). *A Relational Grammar of Kinyarwanda* - consecutive forms
- Nurse, Derek (2008). *Tense and Aspect in Bantu* - cross-Bantu patterns

**Discourse Studies**:
- Dahl, Östen (1985). *Tense and Aspect Systems* - foreground/background distinction
- Hopper, Paul (1979). "Aspect and Foregrounding in Discourse" - theoretical foundation
- Meeuwis, Michael (2010). *Lingala* - Bantu narrative structure (similar patterns)

**Bible Translation Resources**:
- SIL Bantu Bible translation workshops
- Biblica translation notes for Swahili, Kinyarwanda
- UBS translation handbook on discourse features

## Summary

Salience Band is **not optional** for Bantu translation. It directly determines verb morphology in 89 TBTA languages. Accurate annotation enables:

1. **Grammatically correct** verb form selection
2. **Discourse coherent** narrative structure
3. **Natural sounding** translation (not word-for-word)
4. **Culturally appropriate** information flow

**Critical success factor**: Validate TBTA annotations against published Bantu translations to ensure morphological patterns align with native discourse practices.
