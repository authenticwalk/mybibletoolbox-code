# STAGES.md Integration Complete - Arbitrary/Non-Arbitrary Framework

**Date**: 2025-11-16
**Status**: ✅ COMPLETE - Official methodology updated
**Impact**: Critical theological safeguards now integrated into TBTA workflow

---

## Summary

The arbitrary/non-arbitrary framework has been successfully integrated into the official STAGES.md methodology file. This ensures all future TBTA feature development will properly identify and handle theologically significant lexical choices.

---

## Changes Incorporated into STAGES.md

### **Stage 2: Language Study** (Lines 17-23)

**Added**: Cultural distinctives consideration

```markdown
- Consider: Which language families grammatically encode this feature? Are there any unique
  cultural distinctives in any language families or languages where they treat this feature
  differently than others with this feature. For instance in North America there has grown a
  sensitivity towards inclusive language so cases where brothers is said but refers to the
  whole church some would be offended it did not say brothers and sisters.
```

**Purpose**: Identify cultural sensitivities early in the process

---

### **Stage 3: Scholarly Research** (Lines 31-74)

**Added**: Complete "Identify Arbitrary vs Non-Arbitrary Contexts" section

**Key Components**:
1. **Classification Criteria** - 5 criteria for non-arbitrary:
   - Doctrine (Trinity, salvation, God's nature)
   - Divine speech (commands, promises, judgments)
   - Interpretation (literal vs figurative, theological ambiguity)
   - Church practice (authority, worship, ethics)
   - Denominational differences

2. **Required Analysis** - Create `ARBITRARITY-CLASSIFICATION.md`:
   ```yaml
   feature: {feature-name}
   default_classification: arbitrary

   non_arbitrary_contexts:
     - verse_pattern: "Gen 1:26 (Trinity references)"
       affected_values: [trial, plural]
       theological_stakes: high
       affected_doctrines: [Trinity, nature of God]
       denominational_implications: true
       cultural_sensitivity: [monotheistic contexts]

   arbitrary_contexts:
     - pattern: "Crowd sizes, travel narratives"
       rationale: "Theology unchanged by specific number"
       percentage_of_feature: 85%
   ```

3. **Space-Saving Principle**: Default is arbitrary, only mark non-arbitrary

**Purpose**: Classify contexts before generating test sets

---

### **Stage 4: Generate Test Set** (Lines 89, 97-127)

**Added Three Components**:

#### 1. Sample Size Requirement (Line 89)
```markdown
- Include at least 2 cases of each kind of non-arbitrary reason group.
```

#### 2. Non-Arbitrary Reason Groups Section (Lines 97-104)
```markdown
## Non-arbitrary reason groups

Some decisions are arbitrary (there where 3 or 4 maybe 5 people in a group, we don't know,
the original text does not say, something just needs to be picked). Others are non-arbitrary.
Gen 1:1 let "us" (how many people is us; making the wrong choice could greatly influence theology.

 - Think deeply about all the verses determining which are arbitrary/non-arbitrary
 - For all arbitrary group them into reasons (ex. Trinity)
 - Include at least 2 occurances (or more) for each group.
```

#### 3. Theological Stratification Section (Lines 105-127)
```markdown
### Theological Stratification (Non-Arbitrary Features)

For features with non-arbitrary contexts:

**Sample Requirements**:
- ✅ Include ALL identified non-arbitrary verses (Trinity, divine commands, etc.)
- ✅ Mark with theological metadata: `arbitrarity: non-arbitrary`
- ✅ Note affected doctrines and cultural sensitivities
- ✅ Ensure balanced representation across theological contexts

**Example**:
```yaml
verses:
  - reference: "GEN.001.026"
    tbta_value: "trial"
    arbitrarity: non-arbitrary
    theological_stakes: high
    affected_doctrines: [Trinity, creation]
    requires_multi_answer: true
    notes: "Trinity doctrine - prefer trial but document plural alternative"
```

**Arbitrary verses**: Don't add metadata (space-saving - default is arbitrary)
```

#### 4. Adversarial Selection Update (Line 131)
```markdown
For the **test set** (30%), deliberately include challenging non-arbitrary cases:
```

**Purpose**: Ensure non-arbitrary cases are properly represented in test data

---

### **Stage 5: Analyze Translations & Develop Algorithm** (Lines 379-531)

**Added Two Major Sections**:

#### 1. Ramification Analysis for Non-Arbitrary Contexts (Lines 379-488)

**Complete framework including**:
- Detailed YAML template for THEOLOGICAL-ANALYSIS.md
- Preferred answer with theological/translation support
- Alternative answers with theological problems documented
- Cultural considerations (monotheistic, polytheistic, honor/shame)
- Translator guidance (critical warnings, safe/unsafe choices)
- Denominational flexibility

**Example**: Genesis 1:26 Trinity analysis showing:
- Preferred: trial (Trinity doctrine)
- Alternative 1: plural (divine council) - rejected (contra Isa 44:24)
- Alternative 2: majestic plural - rejected (weak evidence)
- Cultural sensitivities documented
- Translator warnings provided

#### 2. Multi-Path Prompts for Non-Arbitrary Features (Lines 492-531)

**Three-step process**:
1. Detect arbitrarity (check theological significance)
2. Branching logic (single answer vs multi-answer)
3. Output format (arbitrary vs non-arbitrary)

**Output Format**:
```yaml
arbitrarity: arbitrary | non-arbitrary

# If arbitrary:
answer: {single value}
confidence: {high/medium/low}

# If non-arbitrary:
preferred: {value}
preferred_rationale: "{why}"
alternatives:
  - value: {alternative}
    problems: ["{issue1}", "{issue2}"]
    when_appropriate: "{context where this might be used}"
translator_warning: "{critical guidance}"
```

**Purpose**: Develop prompts that handle both types appropriately

---

### **Stage 6: Peer Review** (Lines 676-697, 915-924)

**Added Two Components**:

#### 1. Enhanced Theological Reviewer (Lines 676-697)

**Additional checks for non-arbitrary features**:
- [ ] All non-arbitrary contexts identified correctly?
- [ ] Preferred answer theologically sound?
- [ ] Alternative answers fairly represented?
- [ ] Theological problems with alternatives documented?
- [ ] Denominational flexibility respected?
- [ ] False teaching risks identified and prevented?
- [ ] Cultural ramifications considered?
- [ ] Translator warnings clear and actionable?
- [ ] Multi-answer output format correct?

**Test cases**:
- Gen 1:26 (Trinity) - should output trial + alternatives
- Matt 6:9 (prayer) - should flag cultural sensitivity
- Deut 6:4 (monotheism) - should not introduce polytheism

#### 2. Production Readiness Checklist (Lines 915-924)

**New requirement**:
```markdown
- ✅ **Arbitrarity handling** (if feature has non-arbitrary contexts):
  - All non-arbitrary contexts identified (ARBITRARITY-CLASSIFICATION.md)
  - Ramification analysis complete (THEOLOGICAL-ANALYSIS.md)
  - Multi-answer output format implemented
  - Preferred + alternatives documented
  - Theological problems identified
  - Cultural considerations addressed
  - Translator guidance provided
  - Denominational flexibility respected
  - No false teaching enabled
```

**Purpose**: Ensure theological safety before production

---

## Key Principles Established

### 1. **Default is Arbitrary**
- Space-saving design
- Only mark non-arbitrary when theologically significant
- Reduces data bloat

### 2. **Multiple Perspectives for Non-Arbitrary Cases**
- Preferred answer with rationale
- Alternative answers with problems documented
- Denominational flexibility respected
- Cultural sensitivities addressed

### 3. **Translator Empowerment**
- Clear guidance on safe vs unsafe choices
- Critical warnings for false teaching risks
- Denominational flexibility where appropriate
- Cultural context considered

### 4. **Theological Safety**
- Prevents eisegesis (reading meaning IN)
- Enables exegesis (drawing meaning OUT)
- Documents ramifications of all choices
- Flags risks before they become problems

---

## Required New Files Per Feature

Features with non-arbitrary contexts must create:

1. **`experiments/ARBITRARITY-CLASSIFICATION.md`** (Stage 3)
   - Lists all non-arbitrary contexts
   - Documents affected doctrines
   - Notes cultural sensitivities

2. **`experiments/THEOLOGICAL-ANALYSIS.md`** (Stage 5)
   - Complete ramification analysis
   - Preferred + alternative answers
   - Theological problems documented
   - Cultural considerations
   - Translator guidance

3. **Updated prompt output** (Stage 5)
   - Detects arbitrarity
   - Branches logic appropriately
   - Outputs multi-answer for non-arbitrary

---

## Impact on Feature Development

### **Arbitrary Features** (85-90% of cases)
- **Minimal change**: Single answer output as before
- **Space saved**: No metadata stored (default=arbitrary)
- **Development time**: Same as before

### **Non-Arbitrary Features** (10-15% of cases)
- **Additional work**: 2 new files + multi-answer prompts
- **Theological analysis**: Deep analysis required
- **Development time**: +20-30% for theological rigor
- **Value**: Prevents false teaching, respects diversity

### **Mixed Features** (most features)
- **Some arbitrary, some non-arbitrary contexts**
- **Example**: Number system
  - Arbitrary: crowd sizes (85%)
  - Non-arbitrary: Trinity contexts (15%)
- **Approach**: Handle both types appropriately

---

## Validation & Quality Assurance

### **New Validation Points**:
1. Stage 3: Arbitrarity classification verified
2. Stage 4: Non-arbitrary contexts included in test sets
3. Stage 5: Multi-answer prompts tested
4. Stage 6: Theological reviewer checks 9 new criteria
5. Production: 9-point arbitrarity handling checklist

### **Quality Gates**:
- Cannot proceed to Stage 4 without arbitrarity classification
- Cannot proceed to Stage 6 without theological analysis (if non-arbitrary)
- Cannot mark production-ready without all checks passing

---

## Examples of Non-Arbitrary Contexts

### **High Stakes** (Must handle carefully):
- **Genesis 1:26** - Trinity doctrine
- **Matthew 6:9** - Prayer theology
- **1 Corinthians 1:23** - Apostolic authority
- **Deuteronomy 6:4** - Monotheism

### **Medium Stakes** (Should handle):
- **Divine commands** - Obedience requirements
- **Prophetic fulfillment** - Eschatological timeline
- **Salvation statements** - Soteriology debates

### **Cultural Sensitivity**:
- **Inclusive language** - North American sensitivity
- **Honor/shame** - East Asian cultures
- **Monotheistic** - Jewish/Islamic contexts
- **Polytheistic** - Backgrounds requiring clarity

---

## Next Steps for Implementation

### **Immediate**:
1. ✅ STAGES.md updated (COMPLETE)
2. ⏳ Update CORRECTED-INSTRUCTIONS.md to reference new STAGES.md
3. ⏳ Update planning documents to reflect official methodology
4. ⏳ Create example feature demonstrating framework

### **Before Next Feature Development**:
1. Review STAGES.md Section 3 (arbitrarity classification)
2. Review STAGES.md Section 5 (ramification analysis)
3. Review STAGES.md Section 6 (enhanced peer review)
4. Understand multi-answer output format

### **During Feature Development**:
1. Stage 3: Create ARBITRARITY-CLASSIFICATION.md
2. Stage 4: Include non-arbitrary cases in test sets
3. Stage 5: Create THEOLOGICAL-ANALYSIS.md (if needed)
4. Stage 5: Implement multi-path prompts (if needed)
5. Stage 6: Complete enhanced theological review
6. Production: Verify arbitrarity handling checklist

---

## Success Criteria

**This framework succeeds when**:
1. ✅ No false teaching enabled by TBTA predictions
2. ✅ Legitimate theological diversity respected
3. ✅ Translators empowered with clear guidance
4. ✅ Cultural sensitivities acknowledged
5. ✅ Denominational flexibility maintained
6. ✅ Theological stakes clearly communicated
7. ✅ Space-efficient (only mark non-arbitrary)
8. ✅ Production-ready methodology documented

---

## Conclusion

The arbitrary/non-arbitrary framework is now **fully integrated** into the official TBTA methodology. This ensures:

- **Theological safety**: Prevents false teaching
- **Cultural sensitivity**: Respects diverse contexts
- **Denominational respect**: Acknowledges legitimate differences
- **Translator guidance**: Empowers informed decisions
- **Space efficiency**: Only marks significant cases
- **Quality assurance**: Multiple validation points

**All future TBTA feature development must follow this updated STAGES.md methodology.**

---

**Status**: ✅ INTEGRATION COMPLETE
**Next**: Update planning documents and begin feature development with new framework
