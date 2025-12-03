# Number Systems Classification Algorithm - Version 1

**Created**: 2025-11-19
**Training Data**: train.yaml (603 verses)
**Purpose**: Classify grammatical number for TBTA annotations
**Status**: Initial version based on training pattern analysis

---

## TBTA Number Values

- **S** = Singular (one entity)
- **D** = Dual (exactly two entities)
- **T** = Trial (exactly three entities)
- **Q** = Quadrial (exactly four entities)
- **p** = Paucal (small countable group, typically 5-10)
- **P** = Plural (large or indefinite group)

---

## Classification Algorithm (Hierarchical)

Apply rules in order from Level 1 → Level 7. **STOP at first matching rule.**

---

### **LEVEL 1: Explicit Cardinal Numbers** (Highest Confidence)

Pattern: Direct mention of specific numbers in the verse text.

#### Rule 1.1: Cardinal "One"
**Pattern**: Verse contains "one", "a single", "alone"
**Examples**:
- "one man went"
- "a single loaf"
- "alone in the wilderness"

→ **Return: Singular**

---

#### Rule 1.2: Cardinal "Two"
**Pattern**: Verse contains "two", "both", "pair of"
**Examples**:
- "two disciples"
- "both of them"
- "a pair of sandals"

→ **Return: Dual**

---

#### Rule 1.3: Cardinal "Three"
**Pattern**: Verse contains "three" (but not theological context - see Level 3)
**Examples**:
- "three days"
- "three men"
- "three loaves"

→ **Return: Trial**

---

#### Rule 1.4: Cardinal "Four"
**Pattern**: Verse contains "four"
**Examples**:
- "four corners"
- "four living creatures"
- "four gold rings"

→ **Return: Quadrial**

---

#### Rule 1.5: Small Specific Numbers (5-10)
**Pattern**: Verse contains specific numbers in 5-10 range
**Examples**:
- "seven loaves"
- "five thousand men"
- "eight days"

→ **Return: Paucal**

---

#### Rule 1.6: "Few", "Several", "Some" + Countable
**Pattern**: Explicit mention of small indefinite quantity
**Examples**:
- "a few small fish"
- "several men"
- "some disciples"

→ **Return: Paucal**

---

### **LEVEL 2: Natural Pairs and Body Parts** (High Confidence)

Pattern: Universal semantic categories that naturally occur in pairs.

#### Rule 2.1: Natural Pairs
**Pattern**: Reference to body parts or natural pairs
**Examples**:
- "his hands"
- "their eyes"
- "with your feet"
- "both ears"
- "his bare hands"

**Body part pairs**: hands, eyes, feet, ears, arms, legs, cheeks, shoulders

→ **Return: Dual**

---

### **LEVEL 3: Theological Non-Arbitrary Contexts** (High Confidence)

Pattern: Theologically significant contexts where number choice matters.

#### Rule 3.1: Divine First-Person Plural (Trinity)
**Pattern**: God speaking in first-person plural in creation/judgment contexts

**Indicators**:
- "Let us make" (creation context)
- "Let us go down" (judgment context)
- Divine first-person plural: "us", "our"
- NOT in dialogue with others (angels, council)

**Examples**:
- Gen 1:26: "Let us make mankind in our image"
- Gen 11:7: "Let us go down and confuse their language"

**Theological basis**: Conservative Protestant interpretation of Trinity (Father, Son, Holy Spirit)

→ **Return: Trial**

**Note**: This is NON-ARBITRARY. Alternative interpretations exist (divine council, majestic plural) but Christian orthodoxy understands these as trinitarian references.

---

#### Rule 3.2: Explicit Trinity Formula
**Pattern**: Direct reference to all three persons of Trinity

**Indicators**:
- "Father, Son, and Holy Spirit"
- "Father and Son and Spirit"
- Baptismal formula (Matt 28:19)
- Trinitarian blessings (2 Cor 13:14)

**Examples**:
- Matt 28:19: "baptizing them in the name of the Father and of the Son and of the Holy Spirit"
- 2 Cor 13:14: "May the grace of the Lord Jesus Christ, and the love of God, and the fellowship of the Holy Spirit"

→ **Return: Trial**

---

#### Rule 3.3: Monotheism Emphasis
**Pattern**: Strong emphasis on God's singularity/oneness

**Indicators**:
- "The LORD is one"
- "one God"
- "God alone"
- Shema contexts (Deut 6:4)

**Examples**:
- Deut 6:4: "Hear, O Israel: The LORD our God, the LORD is one"
- 1 Tim 2:5: "For there is one God"

→ **Return: Singular**

---

### **LEVEL 4: Named Individuals** (Medium Confidence)

Pattern: Count specific individuals mentioned by proper name.

#### Rule 4.1: One Named Person
**Pattern**: One proper name (person/place)
**Examples**:
- "To Titus"
- "Moses went up"
- "David said"

→ **Return: Singular**

---

#### Rule 4.2: Two Named Individuals
**Pattern**: Two proper names connected by "and" or in parallel
**Examples**:
- "Abram and Lot"
- "Peter and John"
- "you and me" (specific two people)

→ **Return: Dual**

---

#### Rule 4.3: Three Named Individuals
**Pattern**: Three proper names in series
**Examples**:
- "Dishon, Ezer and Dishan"
- "Peter, James and John"
- "Abraham, Isaac and Jacob"

→ **Return: Trial**

---

#### Rule 4.4: Four Named Individuals
**Pattern**: Four proper names listed
**Examples**:
- "Matthew, Mark, Luke and John"
- Four kings in alliance

→ **Return: Quadrial**

---

#### Rule 4.5: Five or More Names
**Pattern**: Five or more proper names listed
**Examples**:
- List of seven deacons
- Twelve apostles listed

→ **Return: Paucal** (if ~5-10) or **Plural** (if >10)

---

### **LEVEL 5: Grammatical and Pronominal Cues** (Medium Confidence)

Pattern: Grammatical markers of number in the language.

#### Rule 5.1: Singular Pronouns
**Pattern**: Singular pronoun as main reference
**Examples**:
- "he said"
- "she went"
- "it was"
- "you" (addressing one person - context dependent)

→ **Return: Singular**

---

#### Rule 5.2: Dual Implications
**Pattern**: Pronouns or phrases implying exactly two
**Examples**:
- "between you and me"
- "the two of them"
- "they both" (with two referents)

→ **Return: Dual**

---

#### Rule 5.3: Plural Pronouns (Indefinite)
**Pattern**: Plural pronouns without specific count
**Examples**:
- "they went" (no specific number given)
- "those who believe"
- "everyone who..."

→ **Return: Plural**

---

### **LEVEL 6: Small Groups and Discourse Context** (Lower Confidence)

Pattern: References to groups with contextual information.

#### Rule 6.1: Small Military/Travel Bands
**Pattern**: Phrases indicating small group movement
**Examples**:
- "I and all those with me"
- "his men"
- "the company"

**Context**: If narrative suggests small band (not army), and countable

→ **Return: Paucal**

---

#### Rule 6.2: Large Indefinite Groups
**Pattern**: Mass nouns, crowds, nations
**Examples**:
- "the people"
- "the nations"
- "whole households"
- "crowds"

→ **Return: Plural**

---

### **LEVEL 7: Default Fallback** (Conservative)

If no rules above match clearly:

#### Rule 7.1: Generic Plural Default
**When to use**:
- Ambiguous reference
- Cannot determine specific count
- Collective nouns
- Uncertainty

→ **Return: Plural**

**Reasoning**: Plural is the most conservative default. It's better to mark as general Plural than to incorrectly claim Dual, Trial, or Quadrial specificity.

---

## Application Guidelines

### 1. Work Through Levels Sequentially
- Start at Level 1
- Stop at first matching rule
- Don't skip levels

### 2. Look for Explicit Before Implicit
- Explicit numbers trump grammatical cues
- Direct statements trump inference

### 3. Context Awareness
- Read surrounding verses if needed (esp. for Rule 4 and 6)
- Consider genre (narrative vs epistle vs prophecy)
- Be aware of quoted speech vs narration

### 4. Theological Sensitivity
- Level 3 rules are NON-ARBITRARY
- These have theological implications
- Document when using these rules

### 5. When in Doubt → Plural
- If truly ambiguous, default to Plural (Rule 7.1)
- Don't force a specific number if uncertain

---

## Pattern-Based, Not Verse-Specific

**CRITICAL**: This algorithm is based on PATTERNS, not memorization of specific verses.

✅ **Correct Approach**:
- "If verse contains divine first-person plural in creation context → Trial"
- "If verse mentions 'two' → Dual"
- "If three proper names listed → Trial"

❌ **WRONG Approach (Overfitting)**:
- "If verse is GEN.001.026 → Trial"
- "If verse is MAT.020.031 → Dual"
- Memorizing specific verse references

**Why This Matters**: Pattern-based algorithms generalize to unseen verses. Verse memorization fails on new data.

---

## Known Limitations (v1)

1. **Paucal Boundary Unclear**
   - Where does Paucal end and Plural begin?
   - Current rule: 5-10 range, but may need refinement

2. **Collective Nouns**
   - "Nation", "household", "church" - singular entity or plural individuals?
   - Current default: Plural, but may need case-by-case

3. **Contextual References**
   - Some verses reference groups mentioned in prior verses
   - May need to read broader context (not just verse in isolation)

4. **Trial Category Size**
   - Training data has 44.3% Trial verses
   - Seems high - may indicate over-marking in training set
   - Algorithm may over-predict Trial

5. **Pronoun Ambiguity**
   - "You" can be singular or plural in English
   - Need context to disambiguate

---

## Testing Protocol

### On Training Data
1. Apply algorithm to all 603 training verses
2. Compare predictions with train.yaml TBTA values
3. Measure accuracy overall and per category
4. Identify systematic errors
5. Document failure patterns

### Refinement Process
- If accuracy < 95%: identify error patterns → revise rules → test again
- If accuracy ≥ 95%: proceed to blind testing on test.yaml

### IMPORTANT
- ✅ CAN see train.yaml values (this is training data)
- ❌ CANNOT see test.yaml values (that's for blind testing)
- ❌ CANNOT see validate.yaml values (that's for final validation)

---

**Algorithm Status**: ✅ Version 1 Complete
**Next Step**: Apply to training data and measure accuracy
**Data Source**: Patterns learned from train.yaml ONLY

