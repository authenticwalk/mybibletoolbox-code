# Person Systems: 100-Verse Adversarial Test Set

**Date**: 2025-11-10
**Algorithm to Test**: v2.1 (validated at 90% on 21-verse set)
**Purpose**: Scale validation to 100 adversarial verses
**Target Accuracy**: 80%+ (production threshold)

---

## Test Set Design

### Stratification

**Total**: 100 verses across 4 challenge categories

1. **Prayer/Lament** (25 verses) - Testing Rule 2.1 priority
2. **Invitation/Exhortation** (25 verses) - Testing Rules 2.5a/2.5b distinction
3. **Quoted Speech** (25 verses) - Testing Rule 2.7 and nested analysis
4. **Role/Authority/Groups** (25 verses) - Testing Rules 3.1-3.3

### Difficulty Distribution

- **Easy**: ~15% (15 verses) - Clear-cut cases for baseline
- **Medium**: ~40% (40 verses) - Moderate ambiguity
- **Hard**: ~45% (45 verses) - Maximum challenge

### No Overlap

✅ Verified: None of these 100 verses appear in:
- Training set (20 verses)
- Original adversarial test (15 verses, 11 valid)
- Original random test (12 verses, 10 valid)

---

## Category 1: Prayer/Lament Contexts (25 verses)

**Testing**: Rule 2.1 (Speech TO deity → EXCLUSIVE)

### Psalms (10 verses)

1. **Psalm 14:7** - "Oh that salvation for Israel would come out of Zion! When the LORD restores the fortunes of his people"
   - Challenge: Corporate hope addressed implicitly to God
   - Difficulty: Medium

2. **Psalm 25:6-7** - "Remember your mercy, O LORD, and your steadfast love...Remember not the sins of my youth"
   - Challenge: Prayer with corporate/personal "our" mixed
   - Difficulty: Medium

3. **Psalm 33:20-22** - "Our soul waits for the LORD; he is our help and our shield. For our heart is glad in him"
   - Challenge: "Our" in prayer/praise context
   - Difficulty: Easy

4. **Psalm 45:10-11** - "Hear, O daughter, and consider, and incline your ear"
   - Challenge: Prophetic address within psalm
   - Difficulty: Hard

5. **Psalm 64:1** - "Hear my voice, O God, in my complaint; preserve my life from dread of the enemy"
   - Challenge: Individual prayer transitioning to "we"
   - Difficulty: Medium

6. **Psalm 79:8-9** - "Do not remember against us our former iniquities; let your compassion come speedily to meet us...Help us, O God of our salvation"
   - Challenge: Corporate lament with "our" possessive in prayer
   - Difficulty: Medium

7. **Psalm 80:3, 7, 19** - "Restore us, O God; let your face shine, that we may be saved"
   - Challenge: Refrain with "us" and "we" in prayer
   - Difficulty: Easy

8. **Psalm 85:4-7** - "Restore us again, O God of our salvation...Will you not revive us again"
   - Challenge: Corporate restoration prayer
   - Difficulty: Medium

9. **Psalm 89:50-51** - "Remember, O Lord, how your servants are mocked...with which your enemies mock, O LORD"
   - Challenge: Prayer mentioning "your servants" (third person shift)
   - Difficulty: Hard

10. **Psalm 106:4-6** - "Remember me, O LORD, when you show favor to your people...that we may rejoice in the gladness of your nation"
    - Challenge: Individual-to-corporate shift in prayer
    - Difficulty: Hard

### Prophets (10 verses)

11. **Isaiah 26:8-9** - "In the path of your judgments, O LORD, we wait for you...My soul yearns for you in the night"
    - Challenge: Corporate to individual prayer shift
    - Difficulty: Medium

12. **Isaiah 33:2** - "O LORD, be gracious to us; we wait for you. Be our arm every morning"
    - Challenge: Corporate plea with "our"
    - Difficulty: Easy

13. **Isaiah 40:27-28** - "Why do you say, O Jacob, and speak, O Israel, 'My way is hidden from the LORD'"
    - Challenge: God quoting Israel's complaint
    - Difficulty: Medium

14. **Jeremiah 14:7-9** - "Though our iniquities testify against us, act, O LORD, for your name's sake...Why should you be like a stranger in the land?"
    - Challenge: Corporate confession with questions TO God
    - Difficulty: Medium

15. **Jeremiah 31:18-19** - "I have heard Ephraim grieving, 'You have disciplined me, and I was disciplined...After I turned away, I repented'"
    - Challenge: God quoting Ephraim's prayer
    - Difficulty: Hard

16. **Ezekiel 20:32** - "What comes into your mind shall never happen—the thought, 'Let us be like the nations'"
    - Challenge: God quoting Israel's rebellious thought
    - Difficulty: Hard

17. **Hosea 14:2-3** - "Take away all iniquity; accept what is good...Assyria shall not save us; we will not ride on horses"
    - Challenge: Prophetic call to repentance with corporate "we"
    - Difficulty: Medium

18. **Micah 7:8-9** - "Rejoice not over me, O my enemy; when I fall, I shall rise; when I sit in darkness, the LORD will be a light to me"
    - Challenge: Individual-to-corporate lament
    - Difficulty: Hard

19. **Zephaniah 3:12-13** - "For I will leave in your midst a people humble and lowly...they shall do no injustice"
    - Challenge: God's promise about "your" people (possessive in prophecy)
    - Difficulty: Medium

20. **Daniel 9:5-8** - "We have sinned and done wrong...to us, O LORD, belongs open shame...because we have sinned against you"
    - Challenge: Daniel's intercessory prayer with "we"
    - Difficulty: Easy

### Other Books (5 verses)

21. **Lamentations 1:18-20** - "The LORD is in the right, for I have rebelled against his word...Hear, all you peoples, and see my suffering"
    - Challenge: Corporate to individual lament shift
    - Difficulty: Medium

22. **Lamentations 3:40-42** - "Let us test and examine our ways, and return to the LORD! Let us lift up our hearts and hands to God in heaven: 'We have transgressed and rebelled'"
    - Challenge: Exhortation transitioning to prayer
    - Difficulty: Hard

23. **Lamentations 5:16-22** - "The crown has fallen from our head; woe to us, for we have sinned!...But you, O LORD, reign forever"
    - Challenge: Corporate confession in lament
    - Difficulty: Medium

24. **Nehemiah 9:32-33** - "Now, therefore, our God, the great, the mighty, and the awesome God...you have been righteous in all that has come upon us"
    - Challenge: Prayer with "our God"
    - Difficulty: Easy

25. **Job 1:11** - "But stretch out your hand and touch all that he has, and he will curse you to your face"
    - Challenge: Satan speaking TO God (not human prayer)
    - Difficulty: Medium

---

## Category 2: Invitation/Exhortation (25 verses)

**Testing**: Rules 2.5a (joint action) vs 2.5b (join group)

### "Let us" Invitations - Testing 2.5a (10 verses)

26. **Isaiah 1:18** - "Come now, let us reason together, says the LORD"
    - Challenge: Divine invitation to joint cognitive action
    - Difficulty: Medium

27. **Isaiah 2:3** - "Come, let us go up to the mountain of the LORD"
    - Challenge: Pilgrimage with destination (action or location?)
    - Difficulty: Hard

28. **Isaiah 2:5** - "O house of Jacob, come, let us walk in the light of the LORD"
    - Challenge: Metaphorical walking (joint action or group membership?)
    - Difficulty: Hard

29. **1 John 4:7** - "Beloved, let us love one another"
    - Challenge: Reciprocal but with hierarchical undertone
    - Difficulty: Medium

30. **Hebrews 6:1** - "Therefore let us leave the elementary doctrine...and go on to maturity"
    - Challenge: Progressive journey metaphor
    - Difficulty: Medium

31. **Hebrews 13:13** - "Therefore let us go to him outside the camp"
    - Challenge: Social boundary crossing (spatial or relational?)
    - Difficulty: Hard

32. **John 14:31** - "Rise, let us go from here"
    - Challenge: Immediate spatial departure
    - Difficulty: Medium

33. **Jeremiah 6:4** - "Arise, let us attack at noon"
    - Challenge: Hostile military coalition
    - Difficulty: Medium

34. **Hosea 6:1** - "Come, let us return to the LORD"
    - Challenge: Return/restoration (movement or group identity?)
    - Difficulty: Hard

35. **Psalm 118:24** - "Let us rejoice and be glad in it"
    - Challenge: Liturgical exhortation with temporal reference
    - Difficulty: Medium

### "With/To Us" Invitations - Testing 2.5b (8 verses)

36. **Numbers 10:29** - "Come with us, and we will do you good"
    - Challenge: Explicit pre-group invitation
    - Difficulty: Easy

37. **Proverbs 1:11-12** - "Come along with us; let us set an ambush"
    - Challenge: Sinful recruitment to existing group
    - Difficulty: Medium

38. **Proverbs 7:18** - "Come, let us take our fill of love"
    - Challenge: Seduction with "our fill" possessive
    - Difficulty: Hard

39. **1 John 1:3** - "That you too may have fellowship with us"
    - Challenge: Apostolic group inviting fellowship
    - Difficulty: Hard

40. **Acts 9:38** - "Please come quickly to us"
    - Challenge: Urgent summons (locative or action?)
    - Difficulty: Medium

41. **Luke 15:28-29** - "Come, eat and celebrate with us"
    - Challenge: Family invitation with wealth distribution
    - Difficulty: Hard

42. **Song of Solomon 4:8** - "Come with me from Lebanon"
    - Challenge: Romantic summons with journey
    - Difficulty: Hard

43. **Revelation 22:17** - "The Spirit and the Bride say, 'Come!'"
    - Challenge: Participatory invitation chain
    - Difficulty: Hard

### Mixed/Ambiguous (7 verses)

44. **Judges 19:11** - "Come, let us turn into this city"
    - Challenge: Destination + action hybrid
    - Difficulty: Hard

45. **1 Samuel 9:6** - "Come, let us go to him"
    - Challenge: Journey to authority figure
    - Difficulty: Hard

46. **1 Samuel 14:1** - "Come, let us go over to the garrison"
    - Challenge: Military boundary crossing
    - Difficulty: Hard

47. **Lamentations 3:40** - "Let us lift up our hearts and hands to God"
    - Challenge: Spiritual-spatial hybrid in lament
    - Difficulty: Medium

48. **2 Chronicles 10:16** - "To your tents, O Israel!"
    - Challenge: Secession command
    - Difficulty: Hard

49. **John 4:40** - "They asked him to stay with them"
    - Challenge: Hospitality with religious boundary
    - Difficulty: Hard

50. **Luke 9:33** - "Master, it is good for us to be here"
    - Challenge: Request to remain in location
    - Difficulty: Medium

---

## Category 3: Quoted Speech (25 verses)

**Testing**: Rule 2.7 (outsider quoting in-group) and nested analysis

### Hostile/Outsider Quoting (10 verses)

51. **Numbers 20:3-5** - "Why have you brought us up out of Egypt?"
    - Challenge: Community complaint quoted in narrative
    - Difficulty: Medium

52. **1 Samuel 8:19-20** - "We also may be like all the nations"
    - Challenge: In-group defining self against authority
    - Difficulty: Medium

53. **Jeremiah 38:4** - "He is weakening the hands of the soldiers"
    - Challenge: Officials quoting effect on "our" group
    - Difficulty: Hard

54. **Lamentations 2:15-16** - "We have swallowed her!"
    - Challenge: Enemies celebrating with "we"
    - Difficulty: Hard

55. **1 Kings 12:16** - "What portion have we in David?"
    - Challenge: Rebellion speech defining boundaries
    - Difficulty: Medium

56. **Malachi 3:8** - "You say, 'How have we robbed you?'"
    - Challenge: God quoting people's defense
    - Difficulty: Medium

57. **Isaiah 36:7** - "If you say, 'We rely on the LORD'"
    - Challenge: Assyrian quoting hypothetical Jerusalem
    - Difficulty: Hard

58. **Jeremiah 42:20** - "Pray for us...declare to us"
    - Challenge: Three-level nesting (already tested but good baseline)
    - Difficulty: Hard

59. **Lamentations 3:48-51** - "Destruction of the daughter of my people"
    - Challenge: Speaker's grief over collective
    - Difficulty: Hard

60. **Job 11:2-3** - "Should a multitude of words go unanswered?"
    - Challenge: Outsider's rhetorical questions
    - Difficulty: Medium

### Nested Quotes (10 verses)

61. **Ezekiel 20:27-29** - "They said, 'We will go up and possess'"
    - Challenge: God quoting people quoting themselves
    - Difficulty: Hard

62. **Matthew 26:59-61** - "We heard him say, I am able to destroy"
    - Challenge: False witnesses quoting Jesus
    - Difficulty: Hard

63. **Mark 14:57-59** - "We heard him say, I will destroy this temple"
    - Challenge: Collective testimony quoting Jesus
    - Difficulty: Hard

64. **Jeremiah 34:15-16** - "You made a covenant...took back"
    - Challenge: God recounting Israel's actions
    - Difficulty: Hard

65. **Hosea 6:1-2** - "Come, let us return...he will revive us"
    - Challenge: Prophetic call with nested promises
    - Difficulty: Medium

66. **2 Corinthians 10:9-10** - "They say, 'His letters are weighty'"
    - Challenge: Paul quoting critics quoting him
    - Difficulty: Hard

67. **Judges 11:10-11** - "The LORD will be witness between us"
    - Challenge: Covenant with divine witness clause
    - Difficulty: Medium

68. **2 Samuel 3:33-34** - "Should Abner die as the fool dies?"
    - Challenge: David's lament with rhetorical questions
    - Difficulty: Hard

69. **Ezekiel 36:20-23** - "People said of them, 'These are the people of the LORD'"
    - Challenge: God quoting nations quoting about Israel
    - Difficulty: Hard

70. **Revelation 3:17** - "For you say, 'I am rich...and need nothing'"
    - Challenge: Jesus quoting church's self-assessment
    - Difficulty: Medium

### Unclear Boundaries (5 verses)

71. **Song of Solomon 1:4** - "We will exult and rejoice in you"
    - Challenge: Multiple speakers with shifting perspective
    - Difficulty: Hard

72. **Song of Solomon 8:12** - "My vineyard...is before me"
    - Challenge: Speaker identity unclear with pronoun shifts
    - Difficulty: Hard

73. **Proverbs 30:7-9** - "Lest I be full and deny you"
    - Challenge: First-person transitioning to self-quotation
    - Difficulty: Medium

74. **Ruth 3:11** - "If he will do the part...I will do it"
    - Challenge: Conditional legal statement
    - Difficulty: Hard

75. **Esther 7:5-6** - "Who is he, and where is he?"
    - Challenge: Accusation with personal/communal harm shift
    - Difficulty: Hard

---

## Category 4: Role/Authority/Groups (25 verses)

**Testing**: Rules 3.1 (shared experience), 3.2 (group distinction), 3.3 (authority)

### Rule 3.3: Role-Based "We" (8 verses)

76. **1 John 1:1-3** - "We declare...you may have fellowship with us"
    - Challenge: Apostolic testimony with dual audience
    - Difficulty: Medium

77. **1 John 4:6** - "We are from God...whoever knows God listens to us"
    - Challenge: Authority claim within same verse
    - Difficulty: Hard

78. **3 John 1:12** - "We also speak well of him"
    - Challenge: Corporate endorsement with role distinction
    - Difficulty: Medium

79. **1 Thessalonians 2:13** - "When you received the word...from us"
    - Challenge: Teacher-to-student relationship
    - Difficulty: Hard

80. **2 Thessalonians 2:15** - "Hold to the teachings we passed on"
    - Challenge: Apostolic tradition transmission
    - Difficulty: Medium

81. **1 Corinthians 2:6-7** - "We speak a message of wisdom"
    - Challenge: Esoteric teaching with initiates
    - Difficulty: Hard

82. **Hebrews 2:1-3** - "We must pay attention...confirmed to us"
    - Challenge: Author including readers with tradition
    - Difficulty: Medium

83. **Revelation 1:4** - "To him who loves us and has freed us"
    - Challenge: Communal blessing with prophetic authority
    - Difficulty: Hard

### Rule 3.2: Ethnic/Religious Groups (8 verses)

84. **Romans 3:28-29** - "For we hold...is God the God of Jews only?"
    - Challenge: Arguing for inclusive boundaries while maintaining "we"
    - Difficulty: Hard

85. **Galatians 2:14-15** - "We who are Jews by birth"
    - Challenge: Explicit ethnic identity claim
    - Difficulty: Easy

86. **Ephesians 2:14-16** - "He has made the two groups one"
    - Challenge: Merging ethnic groups with "our"
    - Difficulty: Medium

87. **1 Thessalonians 2:14-16** - "The Jews...drove us out"
    - Challenge: Ethnic/religious opposition
    - Difficulty: Hard

88. **Colossians 3:11** - "There is no Gentile or Jew"
    - Challenge: Corporate identity transcending boundaries
    - Difficulty: Medium

89. **Acts 26:4-5** - "Our religion...lived as a Pharisee"
    - Challenge: Paul claiming shared Jewish identity
    - Difficulty: Medium

90. **2 Corinthians 11:22** - "Are they Hebrews? So am I"
    - Challenge: Apostolic identity within Jewish group
    - Difficulty: Easy

91. **Philippians 3:5-6** - "Of the people of Israel...a Hebrew"
    - Challenge: Renounced ethnic identity
    - Difficulty: Medium

### Rule 3.1: Shared Experience (9 verses)

92. **Romans 6:3-4** - "All of us who were baptized"
    - Challenge: Shared sacramental experience
    - Difficulty: Medium

93. **1 Corinthians 10:1-4** - "Our ancestors were all under the cloud"
    - Challenge: Identifying with ancestral experience
    - Difficulty: Hard

94. **1 Corinthians 12:12-13** - "We were all baptized by one Spirit"
    - Challenge: Shared incorporation across divides
    - Difficulty: Medium

95. **2 Corinthians 5:1-5** - "If the earthly tent we live in is destroyed"
    - Challenge: Shared eschatological condition
    - Difficulty: Hard

96. **Ephesians 4:3-6** - "There is one body and one Spirit"
    - Challenge: Asserting shared corporate identity
    - Difficulty: Medium

97. **Colossians 1:15-20** - "He is the head of the body, the church"
    - Challenge: Corporate inclusion in cosmic body
    - Difficulty: Medium

98. **1 Peter 2:4-9** - "You are a chosen people...royal priesthood"
    - Challenge: Shared priestly identity claim
    - Difficulty: Medium

99. **Revelation 1:9** - "Your brother and companion in the suffering"
    - Challenge: Author claiming shared experience
    - Difficulty: Medium

100. **Titus 3:4-7** - "He saved us...through the washing of rebirth"
     - Challenge: Shared salvation history
     - Difficulty: Medium

---

## Test Set Statistics

### By Category

| Category | Verses | % of Total | Primary Rule Tested |
|----------|--------|------------|---------------------|
| Prayer/Lament | 25 | 25% | Rule 2.1 |
| Invitation/Exhortation | 25 | 25% | Rules 2.5a/2.5b |
| Quoted Speech | 25 | 25% | Rule 2.7 |
| Role/Authority/Groups | 25 | 25% | Rules 3.1-3.3 |

### By Difficulty

| Difficulty | Count | % of Total | Expected Accuracy |
|------------|-------|------------|-------------------|
| Easy | 9 | 9% | 95%+ |
| Medium | 44 | 44% | 80-90% |
| Hard | 47 | 47% | 60-75% |

### By Testament

| Testament | Verses | % of Total |
|-----------|--------|------------|
| Old Testament | 55 | 55% |
| New Testament | 45 | 45% |

### By Genre

| Genre | Verses | % of Total |
|-------|--------|------------|
| Psalms | 11 | 11% |
| Prophets | 21 | 21% |
| Wisdom/Poetry | 8 | 8% |
| OT Narrative | 15 | 15% |
| Gospels | 10 | 10% |
| Acts | 3 | 3% |
| Epistles | 30 | 30% |
| Revelation | 2 | 2% |

---

## Expected Performance

### Based on v2.1's 90% on 21-verse set

**Optimistic**: 85-90% (85-90/100 correct)
- v2.1 achieved 100% on adversarial, 80% on random
- This 100-verse set is ALL adversarial (harder)
- But rules are refined, so might maintain high performance

**Realistic**: 80-85% (80-85/100 correct)
- More edge cases and harder verses
- Some legitimate translation variation expected
- Still exceeds 80% production threshold

**Pessimistic**: 75-80% (75-80/100 correct)
- If scale reveals new systematic blind spots
- Still respectable for adversarial set
- Would indicate need for v2.2 iteration

---

## Validation Plan

### Phase 1: Make Predictions (Next)

1. Apply algorithm v2.1 to all 100 verses
2. Lock predictions with git commit before validation
3. Document reasoning and confidence for each

### Phase 2: Validate (After Predictions Locked)

1. Validate all 100 verses against Tagalog/Indonesian translations
2. Use parallel agents to validate 25 verses each
3. Compile results and calculate accuracy

### Phase 3: Analyze

1. Calculate overall accuracy
2. Break down by category, difficulty, rule
3. Identify any new error patterns
4. Decide: Production ready OR iterate to v2.2

---

**Status**: Test set designed and documented
**Next Step**: Make blind predictions using algorithm v2.1
**Target**: Lock predictions within same session, validate in parallel
