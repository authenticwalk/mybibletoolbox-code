# Speaker Demographics Validation Checklist

Step-by-step validation procedures for the 6 speaker demographics features. Use this checklist to ensure consistent, accurate annotation of dialogue clauses.

---

## Overview

This checklist implements the 3-tier validation approach:
- **Tier 1 (Critical)**: Must pass 100% - data integrity issues
- **Tier 2 (High Priority)**: Should pass 80%+ - logical consistency
- **Tier 3 (Medium Priority)**: Should pass 60%+ - cultural plausibility

---

## Pre-Validation: Identify Scope

### Step 0: Determine if Validation Applies

**Checklist**:
- [ ] Is this a dialogue clause? (If no, skip to Narrative Check)
- [ ] Are there quote markers (-QuoteBegin/-QuoteEnd)?
- [ ] Is there a speaker identified?
- [ ] If ALL above are NO → This is narrative, proceed to Narrative Validation

### Narrative Validation (Quick Check)

For non-dialogue narrative clauses:
- [ ] Speaker = "0" (Not Applicable)
- [ ] Listener = "0" or not set
- [ ] Speaker's Attitude = "N" (Not Applicable)
- [ ] Speaker's Age = "N" (Not Applicable)
- [ ] Speaker-Listener Age = "N" (Not Applicable)
- [ ] Speech Style = "Not Applicable"

**If all 6 checks pass**: Narrative clause validated ✓

**If any check fails**: Fix to "Not Applicable" or "0" as appropriate

---

## TIER 1: Critical Validations (Must Pass)

### Validation 1.1: Non-Null Check

**Rule**: All 6 speaker demographics fields must have valid values (not null, not empty)

**Checklist**:
- [ ] Speaker field exists and has value
- [ ] Listener field exists and has value
- [ ] Speaker's Attitude field exists and has value
- [ ] Speaker's Age field exists and has value
- [ ] Speaker-Listener Age field exists and has value
- [ ] Speech Style field exists and has value

**If any field is null/empty**: Assign appropriate default or investigate missing data

---

### Validation 1.2: Divine/Spiritual Being Consistency

**Rule**: Divine beings must have Age = "N" (Not Applicable)

**Checklist**:
- [ ] IF Speaker = "M" (God) THEN Speaker's Age = "N"
- [ ] IF Speaker = "R" (Jesus, divine aspect) THEN Speaker's Age = "N" OR "C" (adult human aspect)
- [ ] IF Speaker = Angel codes THEN Speaker's Age = "N"
- [ ] IF Listener = "M" (God) THEN Listener's Age could be "N"

**If check fails**: Correct age to "N" for divine beings

**Note**: Jesus has dual nature - divine ("N") or human adult ("C") depending on context. Human ministry age typically "C" (Adult, 30-33 years).

---

### Validation 1.3: Narrative Consistency

**Rule**: Narrative clauses must have all demographics as "Not Applicable" or "0"

**Checklist**:
- [ ] IF Speaker = "0" THEN Speaker's Attitude = "N"
- [ ] IF Speaker = "0" THEN Speaker's Age = "N"
- [ ] IF Speaker = "0" THEN Speaker-Listener Age = "N"
- [ ] IF Speaker = "0" THEN Speech Style = "Not Applicable"

**If check fails**: Review whether this is truly narrative or dialogue. If narrative, set all to "Not Applicable".

---

### Validation 1.4: Code Validity

**Rule**: All codes must be from valid value sets

**Checklist - Speaker/Listener**:
- [ ] Speaker code is valid (0, M, R, T, or character codes A-Z, a-z, 1-9)
- [ ] Listener code is valid (same set)

**Checklist - Attitude**:
- [ ] Attitude value is valid: N, n, F, E, P, H, or other defined codes

**Checklist - Ages**:
- [ ] Speaker's Age is valid: N, A, B, C, D
- [ ] Speaker-Listener Age is valid: N, O, o, S, y, Y

**Checklist - Style**:
- [ ] Speech Style is valid: Not Applicable, Formal, Informal, Liturgical, Prophetic, Didactic, etc.

**If invalid code found**: Correct to nearest valid code or investigate data corruption

---

## TIER 2: High-Priority Validations (80%+ Pass)

### Validation 2.1: Age Relationship Mathematical Consistency

**Rule**: Age relationship must match calculated difference between speaker and listener ages

**Calculation**:
```
Age values: A=8, B=20, C=45, D=70
Difference = Speaker_Age_Value - Listener_Age_Value

Expected Relationship:
  Diff >= 15 → "O" (Speaker Older significant)
  Diff 5-14 → "o" (Speaker Older slight)
  Diff -4 to +4 → "S" (Same Age)
  Diff -14 to -5 → "y" (Speaker Younger slight)
  Diff <= -15 → "Y" (Speaker Younger significant)
```

**Checklist**:
- [ ] Calculate expected age relationship
- [ ] Compare with actual Age Relationship value
- [ ] IF mismatch AND difference > 1 category → Flag for review
- [ ] IF Speaker Age = N OR Listener Age = N → Age Relationship should be "N"

**Example Checks**:
- Speaker=C (Adult,45), Listener=A (Child,8): Diff=37 → Should be "O" ✓
- Speaker=B (Young Adult,20), Listener=D (Elder,70): Diff=-50 → Should be "Y" ✓
- Speaker=C, Listener=C: Diff=0 → Should be "S" ✓

**Acceptable Exceptions**:
- Edge cases at boundaries (e.g., Diff=4 could be "S" or "o")
- Characters with known specific ages different from category averages

---

### Validation 2.2: Attitude-Style Coherence

**Rule**: Attitude and Style combinations should be culturally plausible

**Compatible Combinations**:

| Attitude | Compatible Styles | Incompatible Styles |
|----------|------------------|-------------------|
| H (Honorable) | Formal, Liturgical, Didactic | Informal (rare) |
| P (Polite) | Formal, Didactic | Very rare with Liturgical |
| n (Neutral) | Formal, Informal, Didactic | - |
| F (Familiar) | Informal, Casual | Formal (rare), Liturgical (never) |
| E (Endearing) | Informal | Formal (rare), Liturgical (never) |

**Checklist**:
- [ ] IF Attitude = "H" AND Style = "Informal" → Flag for review (unusual)
- [ ] IF Attitude = "F" AND Style = "Liturgical" → Error (incompatible)
- [ ] IF Attitude = "E" AND Style = "Formal" → Flag for review (unusual)
- [ ] Verify combination makes sense in context

**Acceptable Exceptions**:
- Prophetic speech may use Honorable + elevated register that looks informal
- Teaching can mix Honorable authority with accessible Didactic style

---

### Validation 2.3: Character Consistency Within Scene

**Rule**: Same character should maintain same age within same scene/episode

**Checklist**:
- [ ] Identify all clauses with same Speaker within nearby verses (same chapter or scene)
- [ ] Verify Speaker's Age is consistent across these clauses
- [ ] IF age changes within scene → Flag for review
- [ ] Acceptable changes: Across books, decades apart, clear time skip

**Example**:
- Peter in Acts 2:14 (Pentecost): Age = C (Adult)
- Peter in Acts 2:38 (same sermon): Age should still be = C
- IF Peter's Age suddenly = D (Elder) within same sermon → Error

**Exception**: Character aging across multiple books (e.g., John as young apostle in Gospels, aged apostle in Revelation)

---

### Validation 2.4: Divine/Human Address Patterns

**Rule**: Addressing God typically requires Honorable attitude and Liturgical/Formal style

**Checklist**:
- [ ] IF Listener = "M" (God) THEN Attitude should be = "H" (Honorable)
- [ ] IF Listener = "M" THEN Style typically = "Liturgical" or "Formal"
- [ ] IF Listener = "M" AND Attitude ≠ "H" → Flag for review (rare but possible)

**Examples**:
- Prayer to God: Listener=M, Attitude=H, Style=Liturgical ✓
- Jesus addressing Father: Listener=M, could be Attitude=H or n (intimate Son), Style=Liturgical ✓
- Human complaint to God (Psalms): Listener=M, Attitude=H (even if tone seems informal) ✓

**Exception**: Jesus as Son may use less formal attitude in intimate prayer (John 17), but still respectful

---

### Validation 2.5: Age-Based Respect Patterns

**Rule**: Younger speakers to significantly older listeners should show respect

**Checklist**:
- [ ] IF Age Relationship = "Y" (Speaker Younger significant) THEN Attitude typically = "H" or "P"
- [ ] IF Age Relationship = "Y" AND Attitude = "F" (Familiar) → Flag for review
- [ ] Exception: Very close family may use "E" (Endearing) even with age gap

**Examples**:
- Youth to elder: Age Rel=Y, Attitude=H ✓
- Child to parent: Age Rel=Y, Attitude=H or E (endearing respect) ✓
- Youth to elder + Attitude=F (Familiar) → Unusual, review context

**Acceptable Exceptions**:
- Ruth to Naomi: Age=Y but Attitude=E (Endearing) due to intimate family bond ✓
- Timothy to Paul: Age=Y, Attitude=E acceptable due to spiritual father-son relationship

---

## TIER 3: Medium-Priority Validations (60%+ Pass)

### Validation 3.1: Genre-Style Alignment

**Rule**: Discourse genre should align with speech style

**Expected Patterns**:

| Discourse Genre | Typical Speech Styles | Unexpected Styles |
|----------------|----------------------|-------------------|
| Narrative (story) | Formal, Informal (dialogue) | Liturgical (unless prayer) |
| Expository | Formal, Didactic | Informal (rare) |
| Hortatory | Formal, Didactic | Very casual |
| Prophetic | Prophetic, Formal | Informal, Casual |
| Legal | Formal | Informal |
| Poetic | Elevated/Poetic | Casual (rare) |

**Checklist**:
- [ ] Verify Discourse Genre (from clause features)
- [ ] Check Speech Style alignment
- [ ] IF major mismatch → Flag for review
- [ ] Consider if mismatched style is intentional (rhetorical device)

---

### Validation 3.2: Statistical Distribution Check

**Rule**: Feature value frequencies should roughly match baseline distributions

**Baseline Distributions** (from SPEAKER-DEMOGRAPHICS-README.md):

**Speaker Distribution**:
- God (M): ~8%, Jesus (R): ~15%, Others: varies, Narrator (0): ~40%

**Attitude Distribution**:
- Neutral (n): ~45%, Polite (P): ~20%, Honorable (H): ~15%, Familiar (F): ~12%

**Age Distribution**:
- Adult (C): ~70%, Elder (D): ~20%, Young Adult (B): ~8%, Child (A): ~2%

**Checklist**:
- [ ] Calculate feature value frequencies in your dataset
- [ ] Compare with baseline distributions
- [ ] IF major deviation (>20% difference) → Investigate systematic bias
- [ ] Note: Some books will deviate naturally (e.g., Genesis has more Elder patriarchs)

**Example**:
- IF 50% of speakers are "Child" (A) → Investigate (baseline is only 2%)
- IF 0% Honorable attitude → Investigate (should be ~15%)
- IF 80% Narrator (0) in Gospels → Investigate (should be lower with dialogue)

---

### Validation 3.3: Cultural Plausibility

**Rule**: Relationships and attitudes should be culturally plausible in biblical context

**Checklist for Unusual Patterns**:
- [ ] Child addressing elder with Familiar (F) attitude → Flag (culturally unlikely)
- [ ] Subordinate to authority with Familiar (F) → Flag (unless very close relationship)
- [ ] Public teaching with very Informal style → Flag (formal contexts expect formality)
- [ ] Prayer with Casual style → Flag (liturgical expected)

**Acceptable Unusual Patterns**:
- Jesus using Familiar with disciples → Acceptable (intimate teacher-student)
- Ruth using Endearing to elder Naomi → Acceptable (family bond overrides formality)
- Paul using Neutral to churches despite authority → Acceptable (apostolic approach)

---

### Validation 3.4: Cross-Linguistic Plausibility

**Rule**: Feature combinations should make sense for target language honorific systems

**Checklist**:
- [ ] IF translating to Japanese → Verify attitude/age/style combination produces valid keigo
- [ ] IF translating to Korean → Verify age relationship determines valid jondaemal/banmal choice
- [ ] IF translating to Thai → Verify gender + attitude produces valid particle choice
- [ ] IF translating to Vietnamese → Verify age relationship produces valid pronoun choice

**Language-Specific Checks**:

**Japanese**:
- [ ] Honorable + Formal → Sonkeigo ✓
- [ ] Familiar + Informal + Same Age → Kudaketa ✓
- [ ] Neutral + Didactic → Teineigo ✓

**Korean**:
- [ ] Age Rel = Y (Younger) → Jondaemal required ✓
- [ ] Age Rel = O (Older) + Familiar → Banmal acceptable ✓
- [ ] Age Rel = S + Formal → Jondaemal polite form ✓

**Thai**:
- [ ] Male + Formal → ครับ (khrap) particle ✓
- [ ] Female + Formal → คะ/ค่ะ (kha) particle ✓

**Vietnamese**:
- [ ] Age Rel = Y → Speaker uses em, Listener uses anh/chị ✓
- [ ] Age Rel = O → Speaker uses anh, Listener uses em ✓

---

## Validation Workflow: Step-by-Step Process

### Phase 1: Pre-Processing (Before Validation)

1. **Extract all clauses** with dialogue (Speaker ≠ "0")
2. **Group by scene/episode** for consistency checking
3. **Identify character list** (unique Speaker/Listener values)
4. **Prepare validation log** (spreadsheet or database)

### Phase 2: Tier 1 Critical Checks (100% Pass Required)

Run all Tier 1 validations:
1. Non-null check (1.1)
2. Divine consistency (1.2)
3. Narrative consistency (1.3)
4. Code validity (1.4)

**Action**: Fix all failures immediately before proceeding

### Phase 3: Tier 2 High-Priority Checks (Target 80%+)

Run all Tier 2 validations:
1. Age relationship math (2.1)
2. Attitude-style coherence (2.2)
3. Character consistency (2.3)
4. Divine address patterns (2.4)
5. Age-based respect (2.5)

**Action**:
- Review all failures
- Fix clear errors
- Document exceptions with reasoning
- Target 80%+ pass rate

### Phase 4: Tier 3 Medium-Priority Checks (Target 60%+)

Run all Tier 3 validations:
1. Genre-style alignment (3.1)
2. Statistical distribution (3.2)
3. Cultural plausibility (3.3)
4. Cross-linguistic plausibility (3.4)

**Action**:
- Review patterns
- Investigate systematic issues
- Fix obvious errors
- Document cultural/rhetorical exceptions

### Phase 5: Report and Iterate

1. **Generate validation report**:
   - Tier 1 pass rate (must be 100%)
   - Tier 2 pass rate (target 80%+)
   - Tier 3 pass rate (target 60%+)
   - List of exceptions with reasoning

2. **Review exceptions**:
   - Are they legitimate rhetorical devices?
   - Are they cultural patterns not in baseline?
   - Are they data errors?

3. **Iterate**:
   - Fix errors
   - Refine validation rules if needed
   - Re-run validation

---

## Automated Validation Script (Pseudocode)

```python
def validate_speaker_demographics(clause):
    """
    Validate all 6 speaker demographics features for a clause.
    Returns validation report with pass/fail for each check.
    """

    report = {
        'tier1': [],
        'tier2': [],
        'tier3': []
    }

    # TIER 1 CHECKS

    # 1.1 Non-null
    if not all([clause.Speaker, clause.Listener, clause.Attitude,
                clause.SpeakerAge, clause.AgeRelationship, clause.SpeechStyle]):
        report['tier1'].append('FAIL: Missing field(s)')
    else:
        report['tier1'].append('PASS: All fields present')

    # 1.2 Divine consistency
    if clause.Speaker in ['M', 'R'] and clause.SpeakerAge not in ['N', 'C']:
        report['tier1'].append('FAIL: Divine being has inappropriate age')
    else:
        report['tier1'].append('PASS: Divine age correct')

    # 1.3 Narrative consistency
    if clause.Speaker == '0':
        if clause.Attitude != 'N' or clause.SpeakerAge != 'N':
            report['tier1'].append('FAIL: Narrative has non-N values')
        else:
            report['tier1'].append('PASS: Narrative consistent')

    # 1.4 Code validity
    valid_speakers = ['0', 'M', 'R', 'T'] + list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789')
    if clause.Speaker not in valid_speakers:
        report['tier1'].append('FAIL: Invalid speaker code')
    else:
        report['tier1'].append('PASS: Valid codes')

    # TIER 2 CHECKS

    # 2.1 Age relationship math
    age_values = {'A': 8, 'B': 20, 'C': 45, 'D': 70, 'N': None}
    if clause.SpeakerAge != 'N' and clause.ListenerAge != 'N':
        speaker_age = age_values.get(clause.SpeakerAge)
        listener_age = age_values.get(clause.ListenerAge)
        if speaker_age and listener_age:
            diff = speaker_age - listener_age
            expected_rel = calculate_age_relationship(diff)
            if clause.AgeRelationship != expected_rel:
                report['tier2'].append(f'WARN: Age rel mismatch (expected {expected_rel}, got {clause.AgeRelationship})')
            else:
                report['tier2'].append('PASS: Age relationship correct')

    # 2.2 Attitude-style coherence
    incompatible = [
        ('F', 'Liturgical'),
        ('E', 'Liturgical'),
        ('F', 'Formal'),  # unusual
    ]
    if (clause.Attitude, clause.SpeechStyle) in incompatible:
        report['tier2'].append('WARN: Unusual attitude-style combination')
    else:
        report['tier2'].append('PASS: Attitude-style compatible')

    # 2.4 Divine address pattern
    if clause.Listener == 'M' and clause.Attitude not in ['H', 'h']:
        report['tier2'].append('WARN: Addressing God without Honorable attitude')
    else:
        report['tier2'].append('PASS: Divine address appropriate')

    # TIER 3 CHECKS

    # 3.3 Cultural plausibility
    if clause.AgeRelationship == 'Y' and clause.Attitude == 'F':
        report['tier3'].append('INFO: Younger speaker using Familiar to elder (review context)')
    else:
        report['tier3'].append('PASS: Culturally plausible')

    return report

def calculate_age_relationship(diff):
    """Calculate expected age relationship from age difference."""
    if diff >= 15:
        return 'O'
    elif diff >= 5:
        return 'o'
    elif diff >= -4:
        return 'S'
    elif diff >= -14:
        return 'y'
    else:
        return 'Y'
```

---

## Validation Report Template

```
SPEAKER DEMOGRAPHICS VALIDATION REPORT
======================================
Date: YYYY-MM-DD
Dataset: [Book/Chapter/Verse Range]
Total Clauses: [N]
Dialogue Clauses: [N]

TIER 1 CRITICAL (100% Required)
--------------------------------
Non-null check: [PASS/FAIL] - [X/Y clauses]
Divine consistency: [PASS/FAIL] - [X/Y clauses]
Narrative consistency: [PASS/FAIL] - [X/Y clauses]
Code validity: [PASS/FAIL] - [X/Y clauses]

Overall Tier 1: [PASS/FAIL] - [X%]

TIER 2 HIGH-PRIORITY (80%+ Target)
-----------------------------------
Age relationship math: [PASS/WARN] - [X/Y clauses] ([Z%])
Attitude-style coherence: [PASS/WARN] - [X/Y clauses] ([Z%])
Character consistency: [PASS/WARN] - [X/Y clauses] ([Z%])
Divine address pattern: [PASS/WARN] - [X/Y clauses] ([Z%])
Age-based respect: [PASS/WARN] - [X/Y clauses] ([Z%])

Overall Tier 2: [PASS/WARN] - [X%]

TIER 3 MEDIUM-PRIORITY (60%+ Target)
-------------------------------------
Genre-style alignment: [PASS/INFO] - [X/Y clauses] ([Z%])
Statistical distribution: [PASS/INFO] - Within expected ranges
Cultural plausibility: [PASS/INFO] - [X/Y clauses] ([Z%])
Cross-linguistic plausibility: [PASS/INFO] - [X/Y clauses] ([Z%])

Overall Tier 3: [PASS/INFO] - [X%]

SUMMARY
-------
Validation Status: [PASS/FAIL]
Recommended Actions: [List]
Exceptions Documented: [N]
Errors Fixed: [N]

EXCEPTIONS LIST
---------------
[Verse] - [Issue] - [Reasoning for exception]
...
```

---

## Quick Reference: Validation Decision Tree

```
Start: Is this dialogue?
├─ NO → Narrative Check: All values = N/0?
│      ├─ YES → PASS ✓
│      └─ NO → FIX to N/0
│
└─ YES → Run Tier 1 Checks
         ├─ Any FAIL? → FIX immediately, restart
         └─ All PASS → Run Tier 2 Checks
                       ├─ <80% pass? → REVIEW, fix errors, document exceptions
                       └─ ≥80% pass → Run Tier 3 Checks
                                      ├─ <60% pass? → INVESTIGATE patterns
                                      └─ ≥60% pass → VALIDATED ✓
```

---

## Conclusion

This validation checklist ensures:
1. **Data Integrity** (Tier 1): No corrupted or invalid data
2. **Logical Consistency** (Tier 2): Features align mathematically and culturally
3. **Cultural Plausibility** (Tier 3): Annotations reflect biblical social dynamics

Use this checklist iteratively during annotation and before finalizing datasets for translation applications.

---

**Note**: Validation should be automated where possible, with human review for flagged items. Language-specific validation may require native speaker consultation for Tier 3 checks.
