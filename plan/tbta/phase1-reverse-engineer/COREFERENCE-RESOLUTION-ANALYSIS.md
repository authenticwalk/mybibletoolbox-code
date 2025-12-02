# TBTA Verse Column: Coreference Resolution Analysis

## Summary

TBTA employs **systematic coreference resolution** to make all referential relationships explicit. The primary strategy is adding explicit referents in parentheses after pronouns: `pronoun(referent)`. Secondary strategies include repeating proper names and using demonstrative+noun phrases instead of pronouns.

**Total examples found**: 3,184+ instances of explicit coreference marking

---

## Four Main Patterns

### Pattern A: Pronoun(Referent) — MOST COMMON
**Frequency**: 3,184+ occurrences across all books

**Description**: Pronouns are retained but followed by explicit referent in parentheses.

**Examples**:

| Reference | TBTA Verse | KJV Original |
|-----------|-----------|--------------|
| **Philemon 1:1** | I(Paul) am Paul. I(Paul) am in prison [because I(Paul) follow Christ Jesus]. | Paul, a prisoner of Jesus Christ... |
| **Philemon 1:9** | I(Paul) am now old. And I(Paul) am in prison | ...being such an one as Paul the aged, and now also a prisoner... |
| **2 John 1:1** | I(John) love all of you(people) much. | The elder...whom I love in the truth... |
| **Philemon 1:17** | you(Philemon) welcome Onesimus [just like you(Philemon) welcome me(Paul)] | If thou count me therefore a partner, receive him as myself |
| **Acts 3:26** | he(God) is able [to bless you(people)]. He(God) will cause... | God...sent him to bless you, in turning away... |

**Application**: First, second, and third person pronouns across all contexts.

---

### Pattern B: Repeated Proper Names
**Frequency**: Common in narrative passages (Genesis, Samuel, etc.)

**Description**: Instead of using pronouns after initial introduction, proper names are repeated.

**Examples**:

| Reference | TBTA Verse | KJV Original | Analysis |
|-----------|-----------|--------------|----------|
| **Genesis 2:20** | Adam named all the animals. Adam named the livestock...But Adam did not see an animal [that was able to help Adam]. | And Adam gave names to all cattle...but for Adam there was not found an help meet for **him**. | "him" → "Adam" |
| **Genesis 2:21** | God caused [Adam to sleep]. [While Adam was sleeping] God took one rib from Adam's body. Then God healed Adam's skin. | the LORD God caused a deep sleep to fall upon Adam, and **he** slept: and **he** took one of **his** ribs | "he/his" → "Adam/Adam's" (4x) |
| **Genesis 3:10** | I(Adam) heard [you(God) walking in the garden]. I(Adam) was afraid [because I(Adam) was naked]. So I(Adam) hid from you(God). | I heard thy voice...and I was afraid, because I was naked; and I hid myself | Explicit (Adam)/(God) added |
| **Genesis 3:16** | God said to the woman, "I(God) will cause [you(Eve) to hurt much [while you(Eve) birth the children of you(Eve)]]..." | Unto the woman he said, I will greatly multiply **thy** sorrow and **thy** conception | "thy" → "you(Eve)'s" (7x in verse) |

**Application**: Third-person narrative references, especially in Genesis.

---

### Pattern C: Demonstrative + Noun
**Frequency**: Common for class/generic references

**Description**: Pronouns replaced with "this/that/these/those + noun phrase."

**Examples**:

| Reference | TBTA Verse | KJV Original | Transformation |
|-----------|-----------|--------------|----------------|
| **Genesis 1:26** | God said, "These people will be like us(God). These people will rule the fish..." | Let us make man...and let **them** have dominion over the fish | "them" → "these people" |
| **Genesis 2:23** | God created the bones of this person with the bones of me(Adam)...I(Adam) will call this person woman | This is now bone of my bones...and **she** shall be called Woman | "she" → "this person" |
| **Genesis 3:22** | This man has become like us(God). This man knows the things [that are good]... | Behold, **the man** is become as one of us, to know good and evil | "the man" → "this man" (emphasizing deixis) |
| **Genesis 4:15** | [If a person kills you(Cain)] I(God) will punish that person much...that person 7 times | whosoever slayeth Cain, vengeance shall be taken on **him** sevenfold | "him" → "that person" |
| **Genesis 5:2** | God created a man and a woman. And God blessed those people. and God called those people human. | Male and female created he **them**; and blessed **them**, and called **their** name Adam | "them/their" → "those people" |

**Application**: Generic/class references, third-person plural, indefinite reference.

---

### Pattern D: Pronoun(Referent) for Third Person
**Frequency**: Rare (only 1 clear example found)

**Description**: Third-person pronouns with parenthetical referent (less common than Patterns B & C).

**Examples**:

| Reference | TBTA Verse | KJV Original |
|-----------|-----------|--------------|
| **Acts 3:26** | God sent God's servant to you(people) [so that he(God) is able [to bless you(people)]]. He(God) will cause... | Unto you first God...sent him to bless you |

**Note**: This pattern exists but is far less common than repeating names (Pattern B) or using demonstratives (Pattern C) for third-person references.

---

## Counter-Examples: Pronouns Retained

Not all pronouns are resolved. Some are kept without explicit annotation:

| Reference | TBTA Verse | KJV Original | Reason Retained |
|-----------|-----------|--------------|-----------------|
| **Genesis 1:2** | [After God had created the earth] no thing was on the earth...and **it** was dark in every place. | the earth was without form, and void; and darkness was upon the face of the deep | **Impersonal "it"** (weather/conditions) |
| **1 Samuel 1:1** | There was a certain man...**He** was in Zuph's clan. **He** lived in the hills... | there was a certain man...and he was an Ephrathite | **Narrative introduction** (initial reference is clear) |
| **Matthew 10:25** | **It** is good [a student becomes like that student's teacher]...**it** is good... | **It** is enough for the disciple that he be as his master | **Impersonal construction** (dummy "it") |

**Pattern**: Pronouns kept when:
- Impersonal/expletive "it" (weather, time, dummy subject)
- Immediately clear from context (narrative introduction)
- Possibly when cognitive load of annotation exceeds clarity benefit

---

## Coreference Resolution Hierarchy

Based on frequency and application:

```
1. First/Second Person → pronoun(referent)        [3,184+ examples]
   I(Paul), you(Philemon), we(John), your(people's)

2. Third Person (narrative) → Repeated Names      [20+ clear examples]
   Adam...Adam...Adam instead of Adam...he...he

3. Third Person (generic) → Demonstrative+Noun    [20+ clear examples]
   "these people" instead of "they"
   "this person" instead of "he/she"

4. Third Person (specific) → he/she(referent)     [Very rare: 1 example]
   he(God), she(woman)

5. Impersonal/Expletive → Keep as-is              [10 examples]
   "it" for weather, dummy subjects
```

---

## Linguistic Principle

**TBTA's Core Strategy**: **Eliminate referential ambiguity**

All referential relationships are made **explicit** through:
- **Parenthetical annotation**: `pronoun(referent)` — preserves syntax, adds semantics
- **Lexical replacement**: Repeat name or use demonstrative+noun — replaces pronoun entirely
- **Strategic retention**: Keep pronouns only when reference is trivial or impersonal

This supports the CNL goal of **unambiguous parsing** for machine translation and Bible translation support.

---

## Data Coverage

**Source**: 16 CSV files analyzed
- 2_John.csv, Philemon.csv, Titus.csv, Ruth.csv, Nahum.csv
- Acts.csv, Esther.csv, Nehemiah.csv, Daniel.csv
- 1_Samuel.csv, 2_Samuel.csv, Joshua.csv
- Genesis.csv, Jonah.csv, Mark.csv, Matthew.csv

**Analysis Date**: 2025-12-02

---

## Implications for Feature Extraction

When building TBTA-CNL feature system:

1. **Coreference tracking** is a core feature
2. Two representations needed:
   - **Syntactic**: Original pronoun form
   - **Semantic**: Explicit referent
3. Pattern recognition must handle:
   - `pronoun(referent)` annotation
   - Repeated name patterns
   - Demonstrative+noun replacements
4. Counter-example handling for impersonal pronouns
