# Discourse Genre: TBTA Annotations

**Feature**: Discourse Genre
**Date**: 2025-11-11
**TBTA Access**: Partial (GEN 1, MAT 5, JHN 3 available)
**Coverage**: 4/18 training verses (22%)

---

## Data Access Limitation

**Available books** in TBTA data: GEN, MAT, JHN
**Missing books** for training set: LEV, EXO, DEU, PSA, ISA, JER, ROM, 1CO, PHP, HEB, LUK

**Impact**: Cannot access TBTA annotations for:
- Procedural (LEV 1:3, EXO 12:3)
- Legal (EXO 20:13, DEU 5:16)
- Poetic (PSA 23:1)
- Hortatory (HEB 12:1, PHP 2:5)
- Prophetic (ISA 7:14, JER 1:5)
- Epistolary (ROM 1:1, 1CO 1:1)
- Some Expository and Background Narrative (LUK 2:1, LUK 1:46-47)

**Workaround**: Analyze patterns from available data (GEN 1, MAT 5, JHN 3), build initial algorithm, await more TBTA data for full validation

---

## Accessible Training Verses (4/18)

### 1. GEN 1:3 - Climactic Narrative Story ✅

**Verse**: "And God said, 'Let there be light,' and there was light."

**Prediction**: Climactic Narrative Story (Main storyline action)
**TBTA Result**: **Climactic Narrative Story** ✅

**Analysis**:
- **All 3 clauses** marked as "Climactic Narrative Story"
  - Clause 1: Main clause "God said..." (line 93)
  - Clause 2: Quoted clause "Let there be light" (line 82)
  - Clause 3: Result clause "there was light" (line 137)

**Pattern Observed**:
- Creation narrative action sequence
- Divine speech frame + quoted command
- Result clause following command
- All marked uniformly as climactic narrative (no background/expository distinction within verse)

**TBTA Features**:
- Illocutionary Force: Declarative (main clause), Jussive (quoted command)
- Time: Discourse (narrative past)
- All constituents treated as narrative advancement

---

### 2. GEN 1:2 - NOT ACCESSIBLE

**Status**: GEN 1:2 TBTA file not found in sparse checkout
**Predicted**: Background Narrative
**Cannot Validate**: Missing from available data

---

### 3. MAT 14:25 - NOT ACCESSIBLE

**Status**: MAT chapter 14 not in sparse checkout (only MAT 5 available)
**Predicted**: Climactic Narrative Story
**Cannot Validate**: Missing from available data

---

### 4. MAT 5:14 - Climactic Narrative Story ❌

**Verse**: "You are the light of the world. A town built on a hill cannot be hidden."

**Prediction**: Expository (Jesus's teaching)
**TBTA Result**: **Climactic Narrative Story** ❌

**Analysis**:
- **All clauses** marked as "Climactic Narrative Story"
  - Main clause: "You are the light..." (line 76)
  - Relative clause: "A town...cannot be hidden" (line 238)
  - Nested relative: "built on a hill" (line 213)

**CRITICAL DISCOVERY**:
TBTA marks **teaching content within narrative frame** as "Climactic Narrative Story", NOT "Expository"

**Context**:
- Part of Sermon on the Mount (Matthew 5-7)
- Jesus teaching disciples
- Metaphorical/didactic content
- Timeless present tense

**Why Narrative? (Hypothesis)**:
1. **Narrative frame dominates**: Gospel treats teaching scenes as part of story progression
2. **Speaker-event focus**: Emphasis on Jesus-as-speaker (narrative participant) rather than content abstraction
3. **Discourse structure**: Teaching embedded within larger narrative discourse
4. **Genre hierarchy**: Outer frame (narrative) > inner content (teaching)

**Implication**:
Need to distinguish:
- Teaching AS EVENT (narrative) ← TBTA marks this
- Teaching CONTENT (expository) ← My initial assumption

---

### 5. JHN 3:3 - Climactic Narrative Story ❌

**Verse**: "Jesus answered him, 'Very truly I tell you, no one can see the kingdom of God unless they are born again.'"

**Prediction**: Expository (Jesus's teaching to Nicodemus about born again)
**TBTA Result**: **Climactic Narrative Story** ❌

**Analysis**:
- **All clauses** marked as "Climactic Narrative Story"
  - Narrative frame: "Jesus answered" (line 115)
  - Quoted teaching: "I tell you the truth" (line 107)
  - Teaching content: "unless born again..." (line 169)

**Pattern Confirmation**:
Same pattern as MAT 5:14 - teaching within narrative frame = "Climactic Narrative Story"

**Features**:
- Illocutionary Force: Declarative
- Time: Present (timeless teaching), but within Discourse (narrative past frame)
- Quoted speech markers present (-QuoteBegin)

**Additional Evidence**:
- Dialogue structure (Jesus ↔ Nicodemus)
- Narrative progression (conversation as event)
- Gospel narrative genre dominates content type

---

## Summary of TBTA Annotations

| Verse | Predicted Genre | TBTA Genre | Match | Notes |
|-------|----------------|------------|-------|-------|
| GEN 1:3 | Climactic Narrative | **Climactic Narrative Story** | ✅ | Correct |
| GEN 1:2 | Background Narrative | *Not accessible* | ? | Missing data |
| MAT 14:25 | Climactic Narrative | *Not accessible* | ? | Missing data |
| MAT 5:14 | Expository | **Climactic Narrative Story** | ❌ | Teaching-in-narrative |
| JHN 3:3 | Expository | **Climactic Narrative Story** | ❌ | Teaching-in-narrative |

**Accuracy on Accessible Data**: 1/3 = 33%
**Matches**: 1 (GEN 1:3)
**Mismatches**: 2 (MAT 5:14, JHN 3:3)

---

## Key Patterns Discovered

### Pattern 1: Narrative Frame Dominates Content Type

**Discovery**: TBTA marks **teaching embedded in narrative** as "Climactic Narrative Story", not "Expository"

**Evidence**:
- MAT 5:14 (Sermon on the Mount teaching) → Climactic Narrative
- JHN 3:3 (Jesus teaching Nicodemus) → Climactic Narrative

**Rule**:
```
IF text is Gospel narrative THEN:
  IF teaching occurs within narrative scene THEN:
    Genre = Climactic Narrative Story
  ELSE:
    # Pure teaching without narrative frame - NOT YET OBSERVED
```

**Question for Further Research**:
- When (if ever) do Gospels use "Expository"?
- Are Gospels **entirely** "Climactic Narrative" regardless of content?
- Does "Expository" only appear in epistles (Romans, Corinthians)?

---

### Pattern 2: Clause-Level Uniform Assignment

**Discovery**: All clauses within a verse receive the **same genre** (in observed data)

**Evidence**:
- GEN 1:3: 3 clauses, all "Climactic Narrative Story"
- MAT 5:14: 4 clauses, all "Climactic Narrative Story"
- JHN 3:3: 3+ clauses, all "Climactic Narrative Story"

**Rule**:
```
Within single verse:
- Genre is UNIFORM across all clauses
- No mixed genres within verse boundaries
- Genre changes likely occur at verse/paragraph boundaries
```

**Caveat**: Limited data - need to check if this holds across more verses

---

### Pattern 3: Quote Boundaries Do NOT Change Genre

**Discovery**: Quoted speech within narrative maintains **same genre** as narrative frame

**Evidence**:
- GEN 1:3: God's quoted command "Let there be light" = Climactic Narrative (same as frame)
- JHN 3:3: Jesus's quoted teaching = Climactic Narrative (same as frame)

**Rule**:
```
IF narrative frame = Climactic Narrative THEN:
  Quoted speech ALSO = Climactic Narrative
  (Quote does NOT trigger Expository, Hortatory, or other genre)
```

**Implication**: Quotation markers (-QuoteBegin, -QuoteEnd) are structural, not genre-changing

---

## Limitations and Next Steps

### Current Limitations

1. **Limited Genre Coverage**: Only observed "Climactic Narrative Story" (1 of 9 genres)
2. **Limited Book Coverage**: Only GEN 1, MAT 5, JHN 3 (all narrative books)
3. **No Contrast Data**: Haven't seen Background Narrative, Expository, Legal, etc. to compare

### Questions Requiring More Data

1. **When does "Background Narrative" appear?**
   - Hypothesis: Setting descriptions, genealogies, scene transitions
   - Need: GEN 1:2, LUK 2:1 TBTA data

2. **When does "Expository" appear?**
   - Hypothesis: Epistles (Romans, Corinthians) doctrinal sections
   - Need: ROM 3:23, ROM 1:1 TBTA data

3. **When does "Legal" appear?**
   - Hypothesis: Commandments, laws, ordinances
   - Need: EXO 20:13, DEU 5:16 TBTA data

4. **When does "Procedural" appear?**
   - Hypothesis: Step-by-step instructions (sacrifices, rituals)
   - Need: LEV 1:3, EXO 12:3 TBTA data

5. **When does "Poetic" appear?**
   - Hypothesis: Psalms, hymnic passages
   - Need: PSA 23:1, LUK 1:46-47 TBTA data

6. **When does "Prophetic" appear?**
   - Hypothesis: "Thus says the Lord", prophecies, divine utterances
   - Need: ISA 7:14, JER 1:5 TBTA data

7. **When does "Hortatory" appear?**
   - Hypothesis: Appeals, exhortations, "let us" constructions
   - Need: HEB 12:1, PHP 2:5 TBTA data

8. **When does "Epistolary" appear?**
   - Hypothesis: Letter openings, closings, formulaic greetings
   - Need: ROM 1:1, 1CO 1:1 TBTA data

### Next Steps

1. **Expand TBTA data access**: Download more books (LEV, EXO, DEU, PSA, ISA, ROM, etc.)
2. **Analyze contrast examples**: Find verses with non-narrative genres
3. **Build genre decision tree**: Based on book type, content type, discourse structure
4. **Refine algorithm**: Incorporate narrative-frame-dominance pattern
5. **Test on full training set**: Once all 18 verses accessible

---

**Status**: Partial analysis complete (3/18 verses)
**Critical Finding**: Teaching-in-narrative = Climactic Narrative (not Expository)
**Blocking Issue**: Need TBTA data for 8 additional genres
**Ready For**: Pattern documentation and algorithm v0.1 (partial)
