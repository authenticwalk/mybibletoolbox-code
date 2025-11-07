# Age Relationship Calculation Guide

Comprehensive guide for determining Speaker's Age, Listener's Age, and calculating Speaker-Listener Age Relationship values.

---

## Overview

Age-based features are crucial for languages with age-sensitive honorific systems. This guide provides:
1. How to determine Speaker's Age and Listener's Age
2. How to calculate Speaker-Listener Age Relationship
3. Edge cases and special situations
4. Validation rules

---

## Part 1: Determining Speaker's Age

### Age Categories

| Code | Category | Age Range | Description |
|------|----------|-----------|-------------|
| N | Not Applicable | - | Divine beings, abstract, unknown |
| A | Child | 0-12 years | Pre-adolescent |
| B | Young Adult | 13-29 years | Adolescent to early adulthood |
| C | Adult | 30-59 years | Mature adult |
| D | Elder | 60+ years | Senior, elderly |

### Determination Method

#### Step 1: Check for Divine/Special Cases
```
IF Speaker = "M" (God) OR Speaker = "R" (Jesus, divine nature)
   → Age = "N" (Not Applicable)

IF Speaker = Angels, spiritual beings
   → Age = "N" (Not Applicable)

IF Speaker = "0" (Narrative)
   → Age = "N" (Not Applicable)
```

#### Step 2: Check Character Database for Known Ages

**Characters with Known Biblical Ages**:

| Character | Code | Known Age Period | Category |
|-----------|------|------------------|----------|
| Jesus | R | 30-33 (ministry years) | C (Adult) |
| John Baptist | B | ~30 (ministry start) | C (Adult) |
| Moses | S | 80 (Exodus), 120 (death) | D (Elder) |
| David | D | 30 (becomes king), 70 (death) | C or D depending on context |
| Timothy | t | Young (Paul's protégé) | B (Young Adult) |
| Samuel | S | Called as child | A (Child in 1 Sam 3) |
| Mary (mother) | M | ~14-16 (betrothal) | B (Young Adult) |
| Abraham | A | 75-175 | D (Elder in most accounts) |
| Sarah | r | 65-127 | D (Elder) |
| Joseph | O | 17 (sold), 30 (Egypt ruler) | B then C |

#### Step 3: Infer from Context Clues

**Contextual Age Indicators**:

1. **Explicit age statements**:
   - "Jesus was about 30 years old" → C (Adult)
   - "Abraham was 75 when he left Haran" → D (Elder)

2. **Life stage descriptions**:
   - "young man" → B (Young Adult)
   - "child" / "boy" / "girl" → A (Child)
   - "elder" / "old man" → D (Elder)
   - No descriptor → likely C (Adult)

3. **Role indicators**:
   - Rabbi / Teacher / Apostle → typically C (Adult)
   - King / Judge (established) → typically C or D
   - Disciple / follower (learner) → often B (Young Adult)
   - Servant / child mentioned → A (Child) if specified

4. **Relational indicators**:
   - "Son" speaking to "father" → likely B or C to D
   - "Father" speaking to "son" → likely C or D to A or B
   - "Elder" in title → D (Elder)

#### Step 4: Default Assumptions

When no information is available:
- **Default for most speakers**: C (Adult)
- **Reason**: Biblical narratives primarily feature mature adults in active roles
- **Exception**: If context clearly suggests otherwise

---

## Part 2: Calculating Speaker-Listener Age Relationship

### Age Relationship Values

| Code | Relationship | Age Difference | Description |
|------|--------------|----------------|-------------|
| N | Not Applicable | - | Divine involved, unknown, or not relevant |
| O | Speaker Older (significant) | 15+ years | Large age gap, speaker older |
| o | Speaker Older (slight) | 5-14 years | Moderate gap, speaker older |
| S | Same Age | ±4 years | Peers, same generation |
| y | Speaker Younger (slight) | 5-14 years | Moderate gap, speaker younger |
| Y | Speaker Younger (significant) | 15+ years | Large age gap, speaker younger |

### Calculation Algorithm

```
Step 1: Check for Not Applicable cases
IF Speaker Age = "N" OR Listener Age = "N"
   → Age Relationship = "N" (Not Applicable)
   STOP

Step 2: Map age categories to approximate ages
A (Child) = ~8 years
B (Young Adult) = ~20 years
C (Adult) = ~45 years
D (Elder) = ~70 years

Step 3: Calculate difference
Age_Diff = Speaker_Age - Listener_Age

Step 4: Assign relationship code
IF Age_Diff >= 15
   → "O" (Speaker Older significant)
ELSE IF Age_Diff >= 5 AND Age_Diff < 15
   → "o" (Speaker Older slight)
ELSE IF Age_Diff >= -4 AND Age_Diff <= 4
   → "S" (Same Age)
ELSE IF Age_Diff >= -14 AND Age_Diff < -5
   → "y" (Speaker Younger slight)
ELSE IF Age_Diff < -14
   → "Y" (Speaker Younger significant)
```

### Calculation Examples

#### Example 1: Adult to Adult
- Speaker Age: C (Adult, ~45)
- Listener Age: C (Adult, ~45)
- Difference: 45 - 45 = 0
- **Result**: S (Same Age)

#### Example 2: Elder to Young Adult
- Speaker Age: D (Elder, ~70)
- Listener Age: B (Young Adult, ~20)
- Difference: 70 - 20 = 50
- **Result**: O (Speaker Older significant, 15+)

#### Example 3: Adult to Elder
- Speaker Age: C (Adult, ~45)
- Listener Age: D (Elder, ~70)
- Difference: 45 - 70 = -25
- **Result**: Y (Speaker Younger significant, -15 or less)

#### Example 4: Young Adult to Adult
- Speaker Age: B (Young Adult, ~20)
- Listener Age: C (Adult, ~45)
- Difference: 20 - 45 = -25
- **Result**: Y (Speaker Younger significant)

#### Example 5: Adult to Child
- Speaker Age: C (Adult, ~45)
- Listener Age: A (Child, ~8)
- Difference: 45 - 8 = 37
- **Result**: O (Speaker Older significant)

#### Example 6: Two Elders
- Speaker Age: D (Elder, ~70)
- Listener Age: D (Elder, ~68)
- Difference: 70 - 68 = 2
- **Result**: S (Same Age, within ±4 years)

#### Example 7: Young Adults (Close in Age)
- Speaker Age: B (Young Adult, ~22)
- Listener Age: B (Young Adult, ~18)
- Difference: 22 - 18 = 4
- **Result**: S (Same Age, at boundary)

---

## Part 3: Special Cases and Edge Cases

### Case 1: Divine to Human

**Rule**: Always "N" (Not Applicable)

**Examples**:
- God to Moses: N
- Jesus (divine aspect) to disciples: N
- Angel to Mary: N

**Reasoning**: Divine beings transcend age categories

**Exception**: Jesus in fully human aspect may use C (Adult) for age, but age relationship to humans still typically N

### Case 2: Narrative Voice

**Rule**: All age features = "N" (Not Applicable)

**Example**:
- Speaker: 0 (Narrator)
- Speaker Age: N
- Listener: N/A
- Age Relationship: N

### Case 3: Generic/Hypothetical Characters

**Rule**: Use typical age for role in parable

**Examples**:
- "A certain man" in parable → C (Adult) typical default
- "A king" → C or D (Adult or Elder)
- "A servant" → B or C (Young Adult or Adult)
- "A child" explicitly mentioned → A (Child)

### Case 4: Groups as Speaker or Listener

**Rule**: Use majority age or leader's age

**Examples**:
- Disciples (group) speaking: B or C (mix of young adults and adults) → use C (Adult)
- Crowd speaking: C (Adult) default for mixed group
- "The elders" speaking: D (Elder)
- Children (group) speaking: A (Child)

### Case 5: Same Character at Different Life Stages

**Rule**: Age changes across narratives

**Examples**:
- David as youth (vs Goliath): B (Young Adult)
- David as new king (age 30): C (Adult)
- David in old age: D (Elder)

**Important**: Within same episode/scene, keep age consistent

### Case 6: Uncertain Ages

**Rule**: Default to Adult (C) unless context clearly indicates otherwise

**Reasoning**: Most biblical dialogue involves mature adults in active roles

### Case 7: Peer Groups with Social Hierarchy

**Rule**: Age relationship can be "S" (Same Age) even when Speaker's Attitude differs

**Example**:
- Paul to Corinthian church elders
- Age: Paul = C (Adult), Elders = C (Adult)
- Age Relationship: S (Same Age/Generation)
- BUT Attitude: H (Honorable) due to apostolic authority
- **Lesson**: Age relationship ≠ social relationship

---

## Part 4: Language-Specific Considerations

### Japanese Age Sensitivity

**Japanese Keigo is highly age-sensitive**:
- Even 1 year difference can trigger keigo in school/work contexts
- Our categories are broader (5-year bands)
- Within "S" (Same Age), Japanese may still differentiate

**Mapping**:
- O/Y (significant) → Always use appropriate keigo
- o/y (slight) → Keigo expected in formal contexts
- S (same age) → May use casual among close friends, but teineigo common

### Korean Age Hierarchy

**Korean age reckoning differs**:
- Korean age = Birth year + 1 (all born in same year are "same age")
- Age relationship in TBTA uses biological age
- Korean translation must consider cultural age reckoning

**Mapping**:
- O/Y → Jondaemal (존댓말) required
- o/y → Jondaemal in most contexts
- S → Banmal (반말) possible if close friends

### Thai Age and Status

**Thai combines age with social status**:
- Age difference + social status determine register
- Monastic status overrides age (monk receives respect regardless)
- Royal status overrides age

**Mapping**:
- Use age relationship as baseline
- Apply status modifiers (Speaker's Attitude)
- Result determines particle selection (ครับ/คะ, formal particles)

### Vietnamese Pronouns

**Vietnamese pronouns encode age**:
- Older person: anh/chị (older brother/sister)
- Younger person: em (younger sibling)
- Elder: ông/bà (grandparent level)
- Age relationship determines pronoun, not just politeness

**Mapping**:
- O/o → Speaker uses em for listener
- Y/y → Speaker uses anh/chị for listener
- S → Peers use anh/em based on slight age difference
- Elder/Child distinctions use ông/bà or con

### Javanese Speech Levels

**Javanese has 10+ levels**:
- Age is one factor among many (status, familiarity, context)
- Age relationship + attitude determine level
- Elders can use ngoko (familiar) to youth; youth must use krama to elders

**Mapping**:
- O → Speaker can use lower register (ngoko/madya)
- Y → Speaker must use higher register (krama/krama inggil)
- S → Context and attitude determine level

---

## Part 5: Validation Rules for Age Features

### Critical Validations (Must Pass)

1. **Divine consistency**:
   ```
   IF Speaker = "M" (God) OR "R" (Jesus)
      THEN Speaker Age = "N"
   ```

2. **Narrative consistency**:
   ```
   IF Speaker = "0" (Narrative)
      THEN Speaker Age = "N"
      AND Age Relationship = "N"
   ```

3. **Age relationship matches ages**:
   ```
   IF Speaker Age = "A" (Child) AND Listener Age = "D" (Elder)
      THEN Age Relationship = "Y" (Speaker Younger significant)
      [Child to Elder = large gap]
   ```

### High-Priority Validations (80%+ Pass)

4. **Mathematical consistency**:
   ```
   Age categories to approximate years:
   A = 8, B = 20, C = 45, D = 70

   Calculate difference, verify relationship code matches
   ```

5. **Same character consistency**:
   ```
   IF Same character within same episode
      THEN Age should not change
   ```

6. **Age progression in narrative**:
   ```
   IF Same character, different books/decades later
      THEN Age should increase (B → C, C → D)
   ```

### Medium-Priority Validations (60%+ Pass)

7. **Role-age plausibility**:
   ```
   Teacher/Rabbi → typically not "A" (Child)
   Young disciple → typically not "D" (Elder)
   ```

8. **Relational plausibility**:
   ```
   "Father" speaking to "son" → likely O or o (speaker older)
   "Student" to "teacher" → likely Y or y (speaker younger)
   ```

---

## Part 6: Quick Reference Tables

### Age Category Decision Tree

```
Is speaker divine or spiritual being?
├─ YES → Age = "N"
└─ NO
    ├─ Is age explicitly stated or well-known?
    │   ├─ 0-12 → Age = "A"
    │   ├─ 13-29 → Age = "B"
    │   ├─ 30-59 → Age = "C"
    │   └─ 60+ → Age = "D"
    └─ Is age inferable from context?
        ├─ Child/boy/girl mentioned → "A"
        ├─ Young man/youth → "B"
        ├─ Teacher/leader/established role → "C"
        ├─ Elder/old explicitly → "D"
        └─ Unknown → Default "C" (Adult)
```

### Age Relationship Lookup Table

| Speaker Age | Listener Age | Difference (approx) | Relationship Code |
|-------------|--------------|---------------------|-------------------|
| A (Child) | A (Child) | 0 | S |
| A (Child) | B (Young Adult) | -12 | y |
| A (Child) | C (Adult) | -37 | Y |
| A (Child) | D (Elder) | -62 | Y |
| B (Young Adult) | A (Child) | +12 | o |
| B (Young Adult) | B (Young Adult) | 0 | S |
| B (Young Adult) | C (Adult) | -25 | Y |
| B (Young Adult) | D (Elder) | -50 | Y |
| C (Adult) | A (Child) | +37 | O |
| C (Adult) | B (Young Adult) | +25 | O |
| C (Adult) | C (Adult) | 0 | S |
| C (Adult) | D (Elder) | -25 | Y |
| D (Elder) | A (Child) | +62 | O |
| D (Elder) | B (Young Adult) | +50 | O |
| D (Elder) | C (Adult) | +25 | O |
| D (Elder) | D (Elder) | 0 | S |

**Note**: These are approximations. Adjust based on context if characters' exact ages are known.

---

## Part 7: Common Errors and Corrections

### Error 1: Age Relationship Doesn't Match Ages

**Problem**:
- Speaker Age: C (Adult)
- Listener Age: A (Child)
- Age Relationship: S (Same Age) ❌

**Correction**:
- Should be: O (Speaker Older significant)
- Adult to child = 45 - 8 = 37 years difference

### Error 2: Divine Being Assigned Age

**Problem**:
- Speaker: M (God)
- Speaker Age: C (Adult) ❌

**Correction**:
- Should be: N (Not Applicable)
- God is not in human age categories

### Error 3: Character Age Inconsistent in Same Scene

**Problem**:
- Verse 1: Peter's Age = C (Adult)
- Verse 5 (same scene): Peter's Age = B (Young Adult) ❌

**Correction**:
- Keep Peter's Age = C (Adult) consistently throughout scene
- Age only changes across decades, not within scenes

### Error 4: Age Relationship Backward

**Problem**:
- Speaker: Timothy (young)
- Listener: Paul (elder)
- Age Relationship: O (Speaker Older) ❌

**Correction**:
- Should be: Y (Speaker Younger significant)
- Timothy is significantly younger than Paul

### Error 5: Child Assigned Wrong Category

**Problem**:
- Samuel as boy (1 Sam 3)
- Age: C (Adult) ❌

**Correction**:
- Should be: A (Child)
- Explicitly described as boy/child in narrative

---

## Part 8: Practical Workflow

### Workflow for Annotating a Dialogue Clause

1. **Identify Speaker and Listener** (from SPEAKER-LISTENER-CODES.md)
2. **Determine Speaker's Age**:
   - Check if divine/narrative → N
   - Check character database → assign A/B/C/D
   - Infer from context → assign A/B/C/D
   - Default → C (Adult)
3. **Determine Listener's Age** (same process)
4. **Calculate Age Relationship**:
   - Use algorithm in Part 2
   - Cross-check with lookup table in Part 6
   - Verify mathematically consistent
5. **Validate**:
   - Run through critical validations
   - Check for common errors
   - Verify consistency with nearby clauses

---

## Summary

Age features (Speaker's Age, Listener's Age, Speaker-Listener Age Relationship) are essential for:
- **Japanese**: Keigo system selection
- **Korean**: Jondaemal vs banmal
- **Thai**: Pronoun and particle selection
- **Vietnamese**: Pronoun selection (anh/chị/em/ông/bà)
- **Javanese**: Speech level (ngoko/madya/krama)
- **All honorific languages**: Appropriate respect marking

Accurate age annotation enables culturally appropriate translations that reflect biblical social dynamics.
