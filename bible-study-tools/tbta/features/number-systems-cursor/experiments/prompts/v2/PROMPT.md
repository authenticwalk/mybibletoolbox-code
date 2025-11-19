# Number Systems Classification Algorithm - Version 2

**Created**: 2025-11-19
**Refined from**: v1 based on manual evaluation
**Key Improvements**: Fixed Paucal boundary, implicit participant counting, focus vs incidental distinction
**Training Data**: train.yaml (603 verses)

---

## TBTA Number Values

- **S** = Singular (one entity)
- **D** = Dual (exactly two entities)
- **T** = Trial (exactly three entities)
- **Q** = Quadrial (exactly four entities)
- **p** = Paucal (small countable group, typically 2-10, mentioned incidentally)
- **P** = Plural (large or indefinite group)

---

## Classification Algorithm (Hierarchical)

Apply rules in order from Level 1 → Level 7. **STOP at first matching rule.**

---

### **LEVEL 1: Theological Non-Arbitrary Contexts** (Highest Priority!)

**IMPORTANT**: These override all other rules because they have theological significance.

#### Rule 1.1: Divine First-Person Plural (Trinity)
**Pattern**: God speaking in first-person plural in creation/judgment contexts

**Indicators**:
- "Let us make" (creation context)
- "Let us go down" (judgment context)
- Divine first-person plural: "us", "our"
- NOT in dialogue with others (angels, council)

**Examples**:
- Gen 1:26: "Let us make mankind in our image"
- Gen 11:7: "Let us go down and confuse their language"
- Gen 3:22: "The man has now become like one of us"

**Theological basis**: Conservative Protestant interpretation of Trinity (Father, Son, Holy Spirit)

→ **Return: Trial**

**Note**: This is NON-ARBITRARY. Alternative interpretations exist but Christian orthodoxy understands these as trinitarian.

---

#### Rule 1.2: Explicit Trinity Formula
**Pattern**: Direct reference to all three persons of Trinity

**Indicators**:
- "Father, Son, and Holy Spirit"
- Baptismal formula (Matt 28:19)
- Trinitarian blessings (2 Cor 13:14)

**Examples**:
- Matt 28:19: "in the name of the Father and of the Son and of the Holy Spirit"
- 2 Cor 13:14: "grace of the Lord Jesus Christ, love of God, fellowship of the Holy Spirit"

→ **Return: Trial**

---

#### Rule 1.3: Monotheism Emphasis
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

### **LEVEL 2: Natural Pairs** (High Confidence, Universal)

#### Rule 2.1: Body Parts That Come in Pairs
**Pattern**: Reference to body parts that naturally occur in pairs

**Body part pairs**: hands, eyes, feet, ears, arms, legs, cheeks, shoulders, knees

**Examples**:
- "his bare hands"
- "their eyes were opened"
- "with your feet"
- "both ears"

**Rationale**: Natural pairs are inherently dual across all languages (universal semantic category)

→ **Return: Dual**

---

### **LEVEL 3: Explicit Numbers with FOCUS** (High Confidence)

**CRITICAL NEW INSIGHT**: Distinguish between numbers as MAIN FOCUS vs INCIDENTAL MENTION

#### Rule 3.1: "One" as Main Focus
**Pattern**: Verse is ABOUT the one entity/person

**Indicators**:
- "one man went"
- "a single loaf"
- "one of them"
- Entity is subject of main verb
- Emphasis on singularity/uniqueness

**NOT this rule**:
- "one day" (time reference, use Rule 3.6)
- "no one", "anyone", "someone" (see Rule 3.8)

→ **Return: Singular**

---

#### Rule 3.2: "Two" as Main Focus
**Pattern**: The TWO entities are the main actors or focus

**Indicators**:
- Two entities are subjects: "two disciples went"
- Direct focus: "both of them said"
- Paired action: "sent them two by two"
- Verse meaning depends on "twoness"

**Examples of MAIN FOCUS**:
- "two blind men shouted" - they are the actors
- "between you and me" - the two people ARE the point
- "both of them" - emphasis on the pair

**NOT this rule (use Paucal instead)**:
- "two boats at the water's edge" - boats are scene-setting, not main focus
- "two or three gathered" - indefinite small group

→ **Return: Dual**

---

#### Rule 3.3: "Three" as Main Focus (Non-Theological)
**Pattern**: The THREE entities are the main actors or focus

**Indicators**:
- Three named individuals as subjects
- "three men went"
- Verse is about these three specifically
- NOT theological (see Level 1 for Trinity)

**Examples of MAIN FOCUS**:
- "three men going up to worship" - they are the actors
- "Dishon, Ezer and Dishan" - specific three people named

**NOT this rule (use Paucal instead)**:
- "three days later" - time reference
- "about three thousand" - approximate

→ **Return: Trial**

---

#### Rule 3.4: "Four" as Main Focus or Symbolic
**Pattern**: The FOUR entities are main focus OR symbolically significant

**Indicators**:
- Four as subject: "four men carried"
- Symbolic fours: "four corners", "four living creatures", "four winds"
- Architectural/ritual: "four gold rings"
- Four named individuals

**Examples**:
- "four gold rings" - specific architectural detail
- "four living creatures" - symbolic
- "four kings" - specific alliance

→ **Return: Quadrial**

---

#### Rule 3.5: Numbers 5-10 Mentioned (Usually Incidental)
**Pattern**: Specific numbers in 5-10 range, typically incidental

**Indicators**:
- "five loaves"
- "seven days"
- "eight people"
- "ten men"

**Usually incidental detail, not main focus**

→ **Return: Paucal**

---

#### Rule 3.6: "Few", "Several", "Some" + Countable
**Pattern**: Explicit mention of small indefinite quantity

**Examples**:
- "a few small fish"
- "several men"
- "some disciples"
- "two or three gathered"

→ **Return: Paucal**

---

#### Rule 3.7: Incidental Small Numbers
**Pattern**: Small numbers (2-4) mentioned but NOT the main focus

**How to identify INCIDENTAL**:
- Setting the scene: "two boats at the water's edge"
- Background detail: "after two days"
- Not the subject: "saw two people in the distance"
- Verse meaning doesn't depend on exact number

→ **Return: Paucal**

---

#### Rule 3.8: Indefinite Singular
**Pattern**: "someone", "anyone", "whoever", "no one"

**Indicators**:
- Indefinite pronouns referring to unspecified single person
- "someone said"
- "anyone who believes"
- "whoever comes"

→ **Return: Singular**

---

### **LEVEL 4: Named Individuals and Participants** (Medium Confidence)

**IMPORTANT v2 CHANGE**: Count ALL participants, not just named ones!

#### Rule 4.1: Count Total Participants
**Pattern**: Count ALL people involved (explicit and implicit)

**How to count**:
1. Count all proper names mentioned
2. Add pronouns that refer to OTHER people (he, she, they when subject)
3. Total = all participants

**Examples**:
- "he took Peter, John and James" = he (Jesus) + 3 names = **4 total** → Quadrial
- "Moses, Aaron, and Hur" = 3 names = **3 total** → Trial
- "Paul and Silas" = 2 names = **2 total** → Dual
- "To Titus" = 1 name = **1 total** → Singular

**Apply counts**:
- 1 total participant → Singular (Rule 4.2)
- 2 total participants → Dual (Rule 4.3)
- 3 total participants → Trial (Rule 4.4)
- 4 total participants → Quadrial (Rule 4.5)
- 5-10 total participants → Paucal (Rule 4.6)
- 10+ total participants → Plural (Rule 4.7)

---

#### Rule 4.2: One Named Person
**From Rule 4.1**: Total count = 1

→ **Return: Singular**

---

#### Rule 4.3: Two Named Participants
**From Rule 4.1**: Total count = 2

**Examples**:
- "Abram and Lot"
- "Peter and John"
- "you and me" (two specific people)

→ **Return: Dual**

---

#### Rule 4.4: Three Named Participants
**From Rule 4.1**: Total count = 3

**Examples**:
- "Dishon, Ezer and Dishan"
- "Peter, James and John" (without Jesus)
- "Abraham, Isaac and Jacob"

→ **Return: Trial**

---

#### Rule 4.5: Four Named Participants
**From Rule 4.1**: Total count = 4

**Examples**:
- "Jesus took Peter, James and John" = 1 + 3 = 4
- Four kings in alliance
- Four people specifically named

→ **Return: Quadrial**

---

#### Rule 4.6: Five to Ten Named Participants
**From Rule 4.1**: Total count = 5-10

**Examples**:
- List of seven deacons
- Small group of disciples

→ **Return: Paucal**

---

#### Rule 4.7: More Than Ten Named Participants
**From Rule 4.1**: Total count > 10

**Examples**:
- Twelve apostles listed
- Large genealogy

→ **Return: Plural**

---

### **LEVEL 5: Grammatical and Pronominal Cues** (Medium Confidence)

#### Rule 5.1: Singular Pronouns as Main Reference
**Pattern**: Singular pronoun is the main subject

**Indicators**:
- "he said"
- "she went"
- "it was"
- "you" addressing one person (context-dependent)

**Only apply if**:
- No plural references in verse
- Clear singular focus

→ **Return: Singular**

---

#### Rule 5.2: Dual Implications in Pronouns
**Pattern**: Pronouns or phrases implying exactly two

**Examples**:
- "between you and me"
- "the two of them"
- "they both" (with two referents)
- "we two"

→ **Return: Dual**

---

#### Rule 5.3: Small Group Pronouns
**Pattern**: Pronouns referring to small countable group

**Indicators**:
- "they" with context suggesting small group (not crowd)
- "those few"
- "the rest" (when small number)

**Only apply if**:
- Context suggests countable
- Not a large crowd
- Emphasis on group, not exact count

→ **Return: Paucal**

---

#### Rule 5.4: Generic Plural Pronouns
**Pattern**: Plural pronouns without specific count

**Indicators**:
- "they went" (no specific number given)
- "those who believe"
- "everyone who..."
- "all who..."

→ **Return: Plural**

---

### **LEVEL 6: Discourse Context and Collective Nouns** (Lower Confidence)

#### Rule 6.1: Small Groups in Context
**Pattern**: Phrases indicating small group movement or action

**Examples**:
- "I and all those with me" (military band)
- "his men" (in context of small force)
- "the company" (small group)

**Indicators**:
- Narrative context suggests countable group
- Not a large army or crowd
- Group moves/acts together

→ **Return: Paucal**

---

#### Rule 6.2: Large Indefinite Groups
**Pattern**: Mass nouns, crowds, nations

**Indicators**:
- "the people"
- "the nations"
- "whole households"
- "crowds"
- "multitudes"
- "everyone"

→ **Return: Plural**

---

#### Rule 6.3: Collective Nouns (Singular Treatment)
**Pattern**: Group treated as single entity

**Indicators**:
- "the church" (as institution)
- "the nation" (as unit)
- "the body" (of Christ)
- Singular verb with collective noun

→ **Return: Singular**

---

### **LEVEL 7: Default Fallback** (Conservative)

#### Rule 7.1: Ambiguous Cases → Plural
**When to use**:
- Cannot determine specific count
- Ambiguous between Paucal and Plural
- Collective with unclear treatment
- Uncertainty

→ **Return: Plural**

**Reasoning**: Plural is most conservative default. Better to mark general Plural than incorrectly claim specific number.

---

#### Rule 7.2: Very Small Ambiguous → Paucal
**When to use**:
- Clearly small group (not crowd)
- Countable but exact number unclear
- Context strongly suggests 2-10 range
- NOT large/indefinite

→ **Return: Paucal**

**Use sparingly**: Only when confident it's small group, not large

---

## Application Guidelines

### 1. Work Through Levels Sequentially
- Start at Level 1 (Theological - HIGHEST PRIORITY)
- Stop at first matching rule
- Don't skip levels

### 2. Theological Always Wins (Level 1)
- Trinity references → ALWAYS Trial (regardless of other patterns)
- Monotheism → ALWAYS Singular
- These are non-arbitrary, theologically significant

### 3. Focus vs Incidental (Level 3)
**KEY v2 IMPROVEMENT**:
- Ask: "Is the number the MAIN POINT of the verse?"
- YES → Use exact number (D/T/Q)
- NO → Consider Paucal

**Examples**:
- "two blind men shouted" - THEY are the focus → Dual
- "saw two boats at the water" - boats are background → Paucal

### 4. Count All Participants (Level 4)
**KEY v2 IMPROVEMENT**:
- Don't just count names
- Count implicit subjects too
- "he took X, Y, Z" = 4 people total

### 5. Context Awareness
- Read surrounding text if needed
- Consider genre (narrative vs epistle vs prophecy)
- Be aware of quoted speech vs narration

### 6. When in Doubt
- Between Paucal and Plural → choose Plural (Rule 7.1)
- Between exact number and Paucal → consider focus
- Truly ambiguous → Plural is safest

---

## Pattern-Based, Not Verse-Specific

✅ **Correct Approach** (pattern-based):
- "If divine first-person plural in creation → Trial"
- "If two entities are main actors → Dual"
- "If small number incidentally mentioned → Paucal"

❌ **WRONG Approach** (verse memorization):
- "If GEN.001.026 → Trial"
- "If MAT.020.031 → Dual"

**Why**: Pattern-based algorithms generalize to unseen verses.

---

## Known Limitations (v2)

### 1. Contextual References
- Some verses reference groups from prior verses
- Algorithm works on verse in isolation mostly
- May need broader context for some cases
- **Accept this as known limitation**

### 2. Pronoun Ambiguity
- "You" can be singular or plural in English
- Need context to disambiguate
- May get some wrong without context

### 3. Paucal Boundary Still Fuzzy
- Focus vs incidental can be subjective
- Improved in v2 but not perfect
- Edge cases will exist

### 4. Cultural/Linguistic Assumptions
- Algorithm based on English text analysis
- Original Greek/Hebrew may have different cues
- Cross-linguistic validity needs testing

---

## v1 → v2 Improvements

### Fixed in v2:
1. ✅ **Paucal boundary** - added "focus vs incidental" distinction
2. ✅ **Implicit counting** - Rule 4.1 counts all participants
3. ✅ **Theological priority** - Moved to Level 1 (highest priority)
4. ✅ **Natural pairs clarified** - Always Dual, universal category

### Expected Accuracy Improvement:
- v1: ~70-80% estimated
- v2: targeting 85-90%
- Goal: 95%+ (may need more versions)

---

## Testing Protocol

### On Training Data:
1. Apply v2 to sample verses
2. Compare with train.yaml values
3. Identify remaining errors
4. Create v3 if needed

### Particularly Test:
- LUK.005.002 "two boats" - should now be Paucal ✅
- LUK.009.028 "he took three" - should now be Quadrial (1+3=4) ✅
- GEN.001.026 "Let us make" - should remain Trial ✅
- Paucal category examples - verify focus distinction works

---

**Algorithm Status**: ✅ Version 2 Complete
**Key Innovation**: Focus vs incidental distinction for numbers
**Next Step**: Test v2 on training samples and measure improvement
**Data Source**: Patterns learned from train.yaml ONLY

