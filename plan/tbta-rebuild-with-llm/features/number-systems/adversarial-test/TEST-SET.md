# Number Systems: Adversarial Test Set

**Purpose**: Test algorithm v1.0 on challenging edge cases
**Expected accuracy**: 60-70% (adversarial cases are intentionally difficult)
**Selection date**: 2025-11-08
**Status**: LOCKED - Do not modify after predictions begin

---

## Test Set Overview

**Total verses**: 10
**Selection criteria**: Designed to challenge the algorithm's learned patterns
**Training overlap**: None (all verses excluded from training set)

---

## Category 1: Theological Edge Cases (3 verses)

These test the algorithm's handling of Trinity and theological contexts beyond Genesis 1:26.

### 1. Matthew 28:19 - Trinity Baptismal Formula

**Reference**: Matthew 28:19
**Greek**: πορευθέντες οὖν μαθητεύσατε πάντα τὰ ἔθνη, βαπτίζοντες αὐτοὺς εἰς τὸ ὄνομα τοῦ Πατρὸς καὶ τοῦ Υἱοῦ καὶ τοῦ ἁγίου Πνεύματος
**English (ESV)**: "Go therefore and make disciples of all nations, baptizing them in the name of the Father and of the Son and of the Holy Spirit"

**Challenge**:
- Trinity explicitly mentioned (Father, Son, Holy Spirit)
- Singular "name" (τὸ ὄνομα) with three persons
- Does "name" get Trial marking? Or Singular (one name)?
- Does each person get Trial or Singular individual marking?

**Why adversarial**: Algorithm learned "Trinity = Trial" from Gen 1:26, but this passage has different grammatical structure (three separate referents vs. "us")

---

### 2. Matthew 3:16-17 - Trinity at Jesus' Baptism

**Reference**: Matthew 3:16-17
**Greek**: βαπτισθεὶς δὲ ὁ Ἰησοῦς εὐθὺς ἀνέβη ἀπὸ τοῦ ὕδατος· καὶ ἰδοὺ ἠνεῴχθησαν αὐτῷ οἱ οὐρανοί, καὶ εἶδεν τὸ πνεῦμα τοῦ θεοῦ καταβαῖνον ὡσεὶ περιστερὰν ἐρχόμενον ἐπ' αὐτόν· καὶ ἰδοὺ φωνὴ ἐκ τῶν οὐρανῶν λέγουσα· Οὗτός ἐστιν ὁ υἱός μου ὁ ἀγαπητός
**English (ESV)**: "And when Jesus was baptized, immediately he went up from the water, and behold, the heavens were opened to him, and he saw the Spirit of God descending like a dove and coming to rest on him; and behold, a voice from heaven said, 'This is my beloved Son'"

**Challenge**:
- Trinity present but not explicitly acting together
- Jesus (seen), Spirit (descending), Father (voice)
- Each acts separately - how to mark?
- Does "οἱ οὐρανοί" (plural "heavens") get Singular like Gen 1:1?

**Why adversarial**: Tests whether Trinity = Trial applies when persons act separately, not together

---

### 3. Isaiah 6:8 - "Who will go for us?"

**Reference**: Isaiah 6:8
**Hebrew**: וָאֶשְׁמַע אֶת־קוֹל אֲדֹנָי אֹמֵר אֶת־מִי אֶשְׁלַח וּמִי יֵלֶךְ־לָנוּ
**English (ESV)**: "And I heard the voice of the Lord saying, 'Whom shall I send, and who will go for us?'"

**Challenge**:
- "I" (first singular) vs. "us" (first plural) in same utterance
- Traditional Christian interpretation: Trinity ("us")
- Jewish interpretation: Royal plural or God + angels
- Does TBTA mark "us" as Trial (Trinity) or Plural First Inclusive (God + angels)?

**Why adversarial**: Tests algorithm's handling of debated theological passages where Trinity interpretation is not universally accepted

---

## Category 2: Rare Number Values (2 verses)

These test whether the algorithm can identify rare values like trial, paucal, or quadrial.

### 4. Revelation 4:6-8 - Four Living Creatures

**Reference**: Revelation 4:6-8
**Greek**: καὶ ἐν μέσῳ τοῦ θρόνου καὶ κύκλῳ τοῦ θρόνου τέσσαρα ζῷα... καὶ τὰ τέσσαρα ζῷα
**English (ESV)**: "And around the throne, on each side of the throne, are four living creatures... And the four living creatures"

**Challenge**:
- Explicitly four entities (τέσσαρα)
- Does TBTA mark as Quadrial (if it exists)?
- Or Plural (4 falls into general plural)?
- Or Paucal (few, between trial and general plural)?

**Why adversarial**: Tests whether TBTA uses rare number values beyond singular/dual/trial/plural

---

### 5. John 20:24 - Thomas, One of the Twelve

**Reference**: John 20:24
**Greek**: Θωμᾶς δὲ εἷς ἐκ τῶν δώδεκα
**English (ESV)**: "Now Thomas, one of the twelve"

**Challenge**:
- "Thomas" = Singular (one person)
- "the twelve" = ? (Dozen? Paucal? Plural?)
- Twelve is a specific small group, might get paucal marking
- Or is 12 too many for paucal?

**Why adversarial**: Tests boundary between paucal (few) and plural (many) - where does TBTA draw the line?

---

## Category 3: Morphological Exceptions (3 verses)

These test the algorithm's handling of dual morphology beyond the learned cases.

### 6. Exodus 4:11 - "Who has made man's mouth?" (Hebrew dual forms)

**Reference**: Exodus 4:11
**Hebrew**: וַיֹּאמֶר יְהוָה אֵלָיו מִי שָׂם פֶּה לָאָדָם אוֹ מִי־יָשׂוּם אִלֵּם אוֹ חֵרֵשׁ אוֹ פִקֵּחַ אוֹ עִוֵּר
**English (ESV)**: "Then the LORD said to him, 'Who has made man's mouth? Who makes him mute, or deaf, or seeing, or blind?'"

**Challenge**:
- "deaf" (חֵרֵשׁ) - ear disability (related to אָזְנַיִם "ears", dual form)
- "seeing" (פִקֵּחַ) - eye function (related to עֵינַיִם "eyes", dual form)
- "blind" (עִוֵּר) - eye disability
- Do body parts in dual always → Singular when referring to the general faculty?

**Why adversarial**: Tests algorithm on body-part duals not in training set (eyes, ears)

---

### 7. Deuteronomy 28:65 - "Trembling heart, failing eyes"

**Reference**: Deuteronomy 28:65
**Hebrew**: וְנָתַן יְהוָה לְךָ שָׁם לֵב רַגָּז וְכִלְיוֹן עֵינַיִם וְדַאֲבוֹן נָפֶשׁ
**English (ESV)**: "And the LORD will give you there a trembling heart and failing eyes and a languishing soul"

**Challenge**:
- עֵינַיִם (einayim) "eyes" - dual morphology
- Context: Does "failing eyes" refer to both eyes (dual) or general sight faculty (singular)?
- Training had eyes in Matt 5:29 (pluck out one eye), but this is different usage

**Why adversarial**: Same Hebrew word (eyes) but different semantic context - tests context sensitivity

---

### 8. 1 Samuel 5:4 - "Only the trunk of Dagon was left"

**Reference**: 1 Samuel 5:4
**Hebrew**: רַק דָּגוֹן נִשְׁאַר עָלָיו... וּשְׁתֵּי כַפּוֹת יָדָיו כְּרֻתוֹת
**English (ESV)**: "Only the trunk of Dagon was left to him... both his hands were cut off"

**Challenge**:
- יָדָיו (yadav) "his hands" - dual morphology with dual meaning (two hands)
- כַפּוֹת (kappot) "palms" - also refers to hands
- Context makes clear: TWO hands were cut off
- Does TBTA mark as Dual (2) or Plural (body parts)?

**Why adversarial**: Unlike shamayim/mayim (dual form → singular meaning), this is genuine dual (actually two entities)

---

## Category 4: Ambiguous Cases (2 verses)

These test the algorithm's handling of context-dependent and ambiguous references.

### 9. Genesis 41:40 - "All my people shall order themselves as you command"

**Reference**: Genesis 41:40
**Hebrew**: עַל־פִּיךָ יִשַּׁק כָּל־עַמִּי
**English (ESV)**: "You shall be over my house, and all my people shall order themselves as you command"

**Challenge**:
- עַמִּי (ammi) "my people" - morphologically singular collective
- Semantic: Many people (plural) or one people group (singular)?
- Does TBTA mark collective nouns as semantic singular or semantic plural?

**Why adversarial**: Tests collective noun handling - algorithm trained mostly on countable entities

---

### 10. John 11:50 - Corporate Solidarity

**Reference**: John 11:50
**Greek**: οὐδὲ λογίζεσθε ὅτι συμφέρει ὑμῖν ἵνα εἷς ἄνθρωπος ἀποθάνῃ ὑπὲρ τοῦ λαοῦ καὶ μὴ ὅλον τὸ ἔθνος ἀπόληται
**English (ESV)**: "Nor do you understand that it is better for you that one man should die for the people, not that the whole nation should perish"

**Challenge**:
- "one man" (εἷς ἄνθρωπος) - clearly Singular
- "the people" (τοῦ λαοῦ) - singular collective
- "the whole nation" (ὅλον τὸ ἔθνος) - singular collective
- Do collectives get Singular or Plural marking?
- Corporate solidarity: one for many

**Why adversarial**: Tests algorithm on collective nouns and corporate representation concepts

---

## Exclusions from Training Set

**Confirmed excluded**: None of these 10 verses appear in the 35-verse training set (experiment-001.md)

**Training set recap** (for reference):
- Genesis 1:1, 1:2, 1:26
- Matthew 5:3, 5:29, 22:37, 22:40
- John 3:7, 3:11, 14:23, 17:11, 17:21
- [Plus 23 other verses from experiment-001]

---

## Expected Performance

**Realistic expectations**:
- **60-70% accuracy**: Algorithm handles most patterns but struggles with edge cases
- **50-60% accuracy**: Algorithm has significant gaps for rare/ambiguous cases
- **<50% accuracy**: Algorithm too simplistic, needs major revision

**Specific predictions about likely errors**:
1. **Trinity passages**: May over-apply Trial marking (expected 1-2 errors)
2. **Rare values**: May default to Plural instead of Paucal/Quadrial (expected 1 error)
3. **Body-part duals**: May inconsistently apply Singular vs. Dual (expected 1-2 errors)
4. **Collective nouns**: May inconsistently mark Singular vs. Plural (expected 1-2 errors)

**Success benchmark**: 6-7 correct out of 10 = 60-70% ✅

---

## Prediction Protocol

**Step 1**: Apply algorithm v1.0 to each verse WITHOUT checking TBTA
**Step 2**: Document reasoning for each prediction
**Step 3**: Rate confidence (High/Medium/Low)
**Step 4**: Commit predictions to git with timestamp
**Step 5**: LOCK predictions (no modifications after commit)
**Step 6**: Check TBTA and calculate accuracy

---

## Files to Create Next

After locking this test set:
1. `PREDICTIONS-locked.md` - Predictions before checking TBTA (with commit SHA)
2. `RESULTS.md` - Accuracy after checking TBTA
3. `ERROR-ANALYSIS.md` - Detailed analysis of failures

---

**Status**: ✅ Test set designed and locked
**Next step**: Make predictions using algorithm v1.0
**Target date**: 2025-11-10
