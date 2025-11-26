# Edge Case Analysis: Number Systems Feature

**Analysis Date**: 2025-11-26
**Data Source**: train.jsonl (331 curated entries)

## Overview

This document analyzes the minority number values (Dual, Trial, Quadrial, Paucal) to understand
when grammatical number is NOT Singular or Plural.

**Training Data Distribution:**
- Singular: 85 entries (25.7%)
- Plural: 78 entries (23.6%)
- **Dual: 98 entries (29.6%)**
- **Trial: 24 entries (7.3%)**
- **Quadrial: 18 entries (5.4%)**
- **Paucal: 28 entries (8.5%)**

**Note**: The training data is intentionally skewed toward edge cases for learning purposes.
In the full corpus, Singular dominates at 66.2% and Plural at 32.4%.

## Dual

**Total Entries**: 98

### Patterns and Conditions

#### Pattern: PAIR_NARRATIVE
**Frequency**: 49 entries (50.0%)

**Condition**: References to narrative pairs (two officials, two men, two cities, etc.)
Explicit '2' appears in ~59% of dual cases.

**Examples:**

1. **GEN.040.006** - official (H5631 סָרִיס)
   - Simplified: when Joseph come 2 official in morning Joseph see 2 **official** be sad
   - NIV: "When Joseph came to them the next morning, he saw that they were dejected."

2. **GEN.040.008** - official (H5631 סָרִיס)
   - Simplified: then Joseph say 2 **official** God be able explain dream
   - NIV: ""We both had dreams," they answered, "but there is no one to interpret them." Then Joseph said to them, "Do not interpretations belong to God? Tell me your dreams.""

3. **JOS.002.022** - man (H376 אִישׁ)
   - Simplified: after 2 **man** leave 2 man go hill
   - NIV: "When they left, they went into the hills and stayed there three days, until the pursuers had searched all along the road and returned without finding them."

4. **JDG.011.026** - city (H5892 עִיר)
   - Simplified: Israelite live near 2 **city** for 300 year
   - NIV: "For three hundred years Israel occupied Heshbon, Aroer, the surrounding settlements and all the towns along the Arnon. Why didn't you retake them during that time?"

5. **1SA.006.007** - cow (H6510 פָּרָה)
   - Simplified: person put yoke on neck **cow**
   - NIV: ""Now then, get a new cart ready, with two cows that have calved and have never been yoked. Hitch the cows to the cart, but take their calves away and pen them up."


#### Pattern: NONE
**Frequency**: 34 entries (34.7%)

**Condition**: General dual number usage

**Examples:**

1. **EXO.004.009** - sign (H226 אוֹת)
   - Simplified: if not believe 2 **sign**
   - NIV: "But if they do not believe these two signs or listen to you, take some water from the Nile and pour it on the dry ground. The water you take from the river will become blood on the ground.""

2. **EXO.026.19** - socket (H134 אֶדֶן)
   - Simplified: 2 **socket** under each board
   - NIV: "and make forty silver bases to go under them--two bases for each frame, one under each projection."

3. **EXO.28.11** - stone (H68 אֶבֶן)
   - Simplified: engrave 2 **stone** names tribes
   - NIV: "Engrave the names of the sons of Israel on the two stones the way a gem cutter engraves a seal. Then mount the stones in gold filigree settings"

4. **EXO.28.21** - stone (H68 אֶבֶן)
   - Simplified: 12 **stone** according 12 tribes
   - NIV: "There are to be twelve stones, one for each of the names of the sons of Israel, each engraved like a seal with the name of one of the twelve tribes."

5. **EXO.31.18** - tablet (H3871 לוּחַ)
   - Simplified: gave Moses 2 **tablet** stone
   - NIV: "When the LORD finished speaking to Moses on Mount Sinai, he gave him the two tablets of the covenant law, the tablets of stone inscribed by the finger of God."


#### Pattern: BODY_PARTS
**Frequency**: 15 entries (15.3%)

**Condition**: Body parts that naturally come in pairs (hands, feet, sides)
Often implicit - Hebrew/Greek grammar marks duality even without explicit 'two'.

**Examples:**

1. **EXO.009.029** - hand (H3027 יָד)
   - Simplified: after Moses leave city Moses lift **hand** Moses
   - NIV: "Moses replied, "When I have gone out of the city, I will spread out my hands in prayer to the LORD. The thunder will stop and there will be no more hail, so you may know that the earth is the LORD's."

2. **EXO.012.022** - side (H4201 מְזוּזָה)
   - Simplified: and Israelite put blood on both **side** door
   - NIV: "Take a bunch of hyssop, dip it into the blood in the basin and put some of the blood on the top and on both sides of the doorframe. None of you shall go out of the door of your house until morning."

3. **PSA.115.007** - hand (H3027 יָד)
   - Simplified: idol have **hand** but idol touch thing
   - NIV: "They have hands, but cannot feel, feet, but cannot walk, nor can they utter a sound with their throats."

4. **PSA.115.007** - foot (H7272 רֶגֶל)
   - Simplified: idol have **foot** but idol walk
   - NIV: "They have hands, but cannot feel, feet, but cannot walk, nor can they utter a sound with their throats."

5. **PRO.021.025** - hand (H3027 יָד)
   - Simplified: person refuse work **hand**
   - NIV: "The craving of a sluggard will be the death of him, because his hands refuse to work."


### Confidence & Concerns

- **High confidence**: 58/98 (59.2%) have explicit '2' in text
- **Implicit duality**: 40 cases rely on Hebrew/Greek grammar
- **Body parts**: Naturally dual items (hands, feet) often unmarked in English

---

## Trial

**Total Entries**: 24

### Patterns and Conditions

#### Pattern: TRIPLET_NARRATIVE
**Frequency**: 12 entries (50.0%)

**Condition**: References to groups of three in narratives

**Examples:**

1. **GEN.018.005** - man (H376 אִישׁ)
   - Simplified: 3 **man** say ok
   - NIV: "Let me get you something to eat, so you can be refreshed and then go on your way--now that you have come to your servant." "Very well," they answered, "do as you say.""

2. **GEN.018.005** - man (H376 אִישׁ)
   - Simplified: and Abraham bring food **man**
   - NIV: "Let me get you something to eat, so you can be refreshed and then go on your way--now that you have come to your servant." "Very well," they answered, "do as you say.""

3. **GEN.009.019** - man (H1121 בֵּן)
   - Simplified: 3 **man** be son Noah

4. **JDG.019.014** - person (H582 אֱנוֹשׁ)
   - Simplified: 3 **person** travel
   - NIV: "So they went on, and the sun set as they neared Gibeah in Benjamin."

5. **JDG.019.019** - person (H582 אֱנוֹשׁ)
   - Simplified: **person** have dry grass and food
   - NIV: "We have both straw and fodder for our donkeys and bread and wine for ourselves your servants--me, the woman and the young man with us. We don't need anything.""


#### Pattern: NONE
**Frequency**: 7 entries (29.2%)

**Condition**: References to three items/periods

**Examples:**

1. **EXO.019.015** - day (H3117 יוֹם)
   - Simplified: Moses say person prepare in 3 **day** to meet Yahweh
   - NIV: "Then he said to the people, "Prepare yourselves for the third day. Abstain from sexual relations.""

2. **JOS.022.009** - tribe (H7626 שֵׁבֶט)
   - Simplified: Yahweh command Moses give land **tribe**

3. **JDG.006.035** - tribe (H7626 שֵׁבֶט)
   - Simplified: person be **tribe** come Gideon
   - NIV: "He sent messengers throughout Manasseh, calling them to arms, and also into Asher, Zebulun and Naphtali, so that they too went up to meet them."

4. **DAN.012.007** - year (H4150 מוֹעֵד)
   - Simplified: event happen for 3.5 **year**

5. **NEH.002.011** - day (H3117 יוֹם)
   - Simplified: Nehemiah stay in Jerusalem 3 **day**
   - NIV: "I went to Jerusalem, and after staying there three days"


#### Pattern: TRINITY
**Frequency**: 5 entries (20.8%)

**Condition**: Theological references to the Trinity (God, holy-holy-holy)
Uses Hebrew אֱלֹהִים (Elohim) - plural form suggesting Trinity.

**Examples:**

1. **GEN.001.026** - God (H430 אֱלֹהִים)
   - Simplified: then God say now **God** create person

2. **GEN.001.026** - God (H430 אֱלֹהִים)
   - Simplified: person have **God** image

3. **GEN.001.026** - God (H430 אֱלֹהִים)
   - Simplified: person be **God**

4. **GEN.003.022** - God (H430 אֱלֹהִים)
   - Simplified: then God Yahweh say man become one **God**
   - NIV: "And the LORD God said, "The man has now become like one of us, knowing good and evil. He must not be allowed to reach out his hand and take also from the tree of life and eat, and live forever.""

5. **ISA.006.003** - holy (H6918 קָדוֹשׁ)
   - Simplified: **holy** holy holy Lord
   - NIV: "And they were calling to one another: "Holy, holy, holy is the LORD Almighty; the whole earth is full of his glory.""


### Confidence & Concerns

- **Low explicit marking**: Only 5/24 (20.8%) have explicit '3' in text
- **Trinity cases**: Theologically significant - Elohim plural form
- **Narrative triplets**: Contextual (three men visiting Abraham)

---

## Quadrial

**Total Entries**: 18

### Patterns and Conditions

#### Pattern: QUADRIAL_GROUP
**Frequency**: 11 entries (61.1%)

**Condition**: References to groups of four (Daniel's four friends, four living creatures)

**Examples:**

1. **DAN.001.007** - man (H376 אִישׁ)
   - Simplified: chief give new name 4 **man**
   - NIV: "The chief official gave them new names: to Daniel, the name Belteshazzar; to Hananiah, Shadrach; to Mishael, Meshach; and to Azariah, Abednego."

2. **DAN.001.015** - man (H376 אִישׁ)
   - Simplified: body 4 **man** be strong
   - NIV: "At the end of the ten days they looked healthier and better nourished than any of the young men who ate the royal food."

3. **LUK.009.028** - man (G435 ἀνήρ)
   - Simplified: **man** go-up mountain to pray
   - NIV: "About eight days after Jesus said this, he took Peter, John and James with him and went up onto a mountain to pray."

4. **EZK.01.006** - face (H6440 פָּנִים)
   - Simplified: each had 4 **face**
   - NIV: "but each of them had four faces and four wings."

5. **EZK.01.006** - wing (H3671 כָּנָף)
   - Simplified: each had 4 **wing**
   - NIV: "but each of them had four faces and four wings."


#### Pattern: NONE
**Frequency**: 7 entries (38.9%)

**Condition**: References to four items

**Examples:**

1. **EXO.025.012** - ring (H2885 טַבַּעַת)
   - Simplified: Moses attach **ring** 4 leg ark-of-the-covenant
   - NIV: "Cast four gold rings for it and fasten them to its four feet, with two rings on one side and two rings on the other."

2. **EXO.025.027** - ring (H2885 טַבַּעַת)
   - Simplified: Moses put **ring** near top table
   - NIV: "The rings are to be close to the rim to hold the poles used in carrying the table."

3. **JOS.021.018** - town (H5892 עִיר)
   - Simplified: Israelite give 4 **town** tribe Benjamin
   - NIV: "Anathoth and Almon, together with their pasturelands--four towns."

4. **1SA.016.010** - man (H376 אִישׁ)
   - Simplified: Samuel say Yahweh choose **man**
   - NIV: "Jesse had seven of his sons pass before Samuel, but Samuel said to him, "The LORD has not chosen these.""

5. **DAN.007.001** - beast (H2423 חֵיוָא)
   - Simplified: Daniel dream 4 **beast**
   - NIV: "In the first year of Belshazzar king of Babylon, Daniel had a dream, and visions passed through his mind as he was lying in bed. He wrote down the substance of his dream."


### Confidence & Concerns

- **Moderate confidence**: 11/18 (61.1%) have explicit '4' in text
- **Common pattern**: Four living creatures (Ezekiel), four friends (Daniel)

---

## Paucal

**Total Entries**: 28

### Patterns and Conditions

#### Pattern: NONE
**Frequency**: 28 entries (100.0%)

**Condition**: References to small, indefinite quantities
Words like 'few', 'little', 'some' or contexts implying small amounts.

**Examples:**

1. **GEN.018.003** - hour (H4592 מְעַט)
   - Simplified: and Abraham say please Lord stay for **hour** with Abraham
   - NIV: "He said, "If I have found favor in your eyes, my lord, do not pass your servant by."

2. **GEN.029.020** - day (H3117 יוֹם)
   - Simplified: but 7 year seem **day** because Jacob love Rachel much
   - NIV: "So Jacob served seven years to get Rachel, but they seemed like only a few days to him because of his love for her."

3. **EXO.016.017** - flake (H4478 מָן)
   - Simplified: other person gather **flake**
   - NIV: "The Israelites did as they were told; some gathered much, some little."

4. **EXO.016.018** - flake (H4478 מָן)
   - Simplified: person gather **flake** have little food
   - NIV: "And when they measured it by the omer, the one who gathered much did not have too much, and the one who gathered little did not have too little. Everyone had gathered just as much as they needed."

5. **JOS.010.020** - man (H376 אִישׁ)
   - Simplified: but **man** Amorite be able run city
   - NIV: "So Joshua and the Israelites defeated them completely, but a few survivors managed to reach their fortified cities."


### Confidence & Concerns

- **Mostly implicit**: Only 2/28 (7.1%) have 'few/little' markers
- **Semantic inference**: Requires understanding context (manna gathering, remnant escaping)
- **Hebrew מְעַט (H4592)**: Explicitly means 'little/few'
- **Greek ὀλίγος (G3641)**: Explicitly means 'few/small'

---

## Summary of Edge Cases

### When to Use Dual
1. **Explicit pairs**: Text contains '2', 'two', 'both'
2. **Body parts**: Hands, feet, eyes, ears, sides (naturally paired)
3. **Narrative pairs**: Two officials, two men, two cities in stories
4. **Hebrew/Greek grammar**: Dual number marking even without English indicators

### When to Use Trial
1. **Trinity references**: Elohim (אֱלֹהִים) in creation/divine contexts
2. **Triple repetition**: Holy-holy-holy (Isaiah 6:3)
3. **Narrative triplets**: Three men, three days, three tribes
4. **Time periods**: Three days, three years, 3.5 years

### When to Use Quadrial
1. **Explicit fours**: Text contains '4', 'four'
2. **Symbolic fours**: Four living creatures (Ezekiel, Revelation)
3. **Narrative groups**: Four friends (Daniel 1), four kingdoms
4. **Structural elements**: Four rings, four corners

### When to Use Paucal
1. **Explicit 'few'**: Words like few, little, some
2. **Hebrew מְעַט (H4592)**: Explicitly means 'little/few'
3. **Greek ὀλίγος (G3641)**: Explicitly means 'few/small'
4. **Contextual smallness**: Remnants escaping, small gatherings
5. **Subjective few**: 'Seven years seemed like a few days' (Gen 29:20)

## Potential Labeling Issues

### Trial vs. Singular/Plural
- Trinity references (Elohim) are controversial
- Could be argued as plural rather than trial
- Current labeling reflects theological interpretation

### Paucal vs. Plural
- Boundary is subjective ('few' vs. 'many')
- Some Hebrew/Greek words explicitly mark paucal
- Others require semantic interpretation

### Implicit Dual
- Body parts in Hebrew/Greek may use dual forms
- English translation doesn't always show this
- May be challenging for ML without source language data

## Suspicious Patterns & Labeling Concerns

Based on analysis of the training data, several patterns warrant attention:

### 1. Trinity Interpretation (Trial + Elohim)

**Issue**: 4 instances of H430 (אֱלֹהִים - Elohim) labeled as Trial
- GEN.001.026 (3 instances): "Let us make mankind in our image"
- GEN.003.022: "The man has become like one of us"

**Concern**: This is a **theological interpretation** rather than grammatical number.
- Elohim is grammatically plural in Hebrew
- Labeling as "Trial" implies Trinity (Father, Son, Holy Spirit)
- Conservative approach: Could be labeled as "Plural" instead
- Current approach: Reflects Christian orthodox interpretation

**Recommendation**: Document this as a theological choice, not a linguistic rule.

### 2. Number Mismatches in Context

**Dual with "3" in text**: 2 cases
- DEU.19.15: "by 2 witness or 3 witnesses" - labeled Dual for the "2 witness" portion
- MAT.18.020: "where 2 or 3 person gathered" - labeled Dual for the "2 or 3 person"

**Trial with "2" in text**: 2 cases  
- MAT.25.015: "one 5 another 2 another 1 talent" - complex context with multiple numbers
- MAT.26.037: "took Peter and 2 sons Zebedee disciple" - labeled Trial for the group

**Assessment**: These appear correct - the number refers to the specific context being labeled, not all numbers in the verse.

### 3. Paucal with Large Numbers

**Issue**: Some Paucal entries mention specific large numbers
- GEN.029.020: "7 year seem **day**" - labeled Paucal because "seemed like a few days" (subjective)
- MAT.015.034: "7 loaf and small **fish**" - labeled Paucal for "small fish" (not the loaves)

**Assessment**: These are **contextually correct** - the Paucal label applies to the subjective/contextual smallness, not the explicit number.

### 4. Same Strong's Number, Multiple Labels

Several Strong's numbers appear with 3+ different labels:

**H376 (אִישׁ - man)**: Appears in ALL SIX categories
- Shows context dependency: "two men" (Dual), "few men" (Paucal), "man" (Singular), etc.
- **This is correct** - same word, different grammatical contexts

**H430 (אֱלֹהִים - Elohim)**: Singular, Plural, Trial
- Theologically complex word
- Singular: references to the one God
- Plural: generic use or grammatical plural  
- Trial: Trinity interpretation
- **Requires theological knowledge** to label correctly

**G3101 (μαθητής - disciple)**: Dual, Plural, Trial
- Context-dependent: "two disciples", "three disciples", "many disciples"
- **This is correct** - demonstrates natural language variation

**Assessment**: This variation is **expected and correct** - grammatical number depends on context, not just the word itself.

### 5. Low Confidence Areas

**Trial without explicit "3"**: Only 5/24 (20.8%) have explicit "three" in text
- Relies heavily on theological interpretation (Trinity)
- Or narrative context (three men visiting Abraham)
- **Risk**: May be harder for ML models to learn

**Paucal without "few" markers**: Only 2/28 (7.1%) have explicit "few/little"
- Relies on semantic understanding
- Hebrew מְעַט (H4592) and Greek ὀλίγος (G3641) are reliable indicators
- **Risk**: Contextual cases require deeper understanding

**Implicit Dual body parts**: 15/98 (15.3%) Dual entries are body parts
- Hebrew/Greek often use dual forms for paired body parts
- English may not show this grammatically
- **Risk**: ML may need source language features to detect

## Recommendations for ML Training

### High Confidence Features
1. **Explicit number words**: "two", "three", "four", "few" in text (59-61% accuracy for Dual/Quadrial)
2. **Specific Strong's numbers**: 
   - G1417 (δύο - two), H8147 (שְׁנַיִם - two) → always Dual
   - G3641 (ὀλίγος - few), H4592 (מְעַט - little) → always Paucal
3. **Body part patterns**: H3027 (יָד - hand), H7272 (רֶגֶל - foot) → often Dual

### Medium Confidence Features  
1. **Narrative context**: References to "officials", "men", "friends" may indicate specific numbers
2. **Structural elements**: "rings", "corners", "faces" often have specific counts
3. **Time periods**: "days", "years" with context clues

### Low Confidence / Requires Expert Judgment
1. **Theological interpretation**: Elohim as Trial (Trinity) vs. Plural
2. **Subjective Paucal**: "seemed like a few days" (contextual smallness)
3. **Implicit Dual**: Body parts without explicit "two" or "both"

### Edge Cases to Flag for Review
- Any Trial label without explicit "3" or theological context
- Any Paucal without explicit "few/little" or specific Strong's number
- Any Dual body part without source language data
- Mixed number contexts (verses mentioning 2, 3, and 4 simultaneously)
