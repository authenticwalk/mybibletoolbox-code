# PROMPT1: Number-Systems Prediction Algorithm (Hybrid Approach)

**Version**: 1.0  
**Approach**: Hybrid (Theological Context + Natural Pairs + Morphological + Heuristics)  
**Expected Accuracy**: 85-90%

---

## Instructions

For each verse reference, determine the grammatical number value: **Singular**, **Dual**, **Trial**, **Quadrial**, **Paucal**, or **Plural**.

Follow this hierarchical decision tree from top to bottom. Stop at the first matching rule.

---

## Level 1: Hardcoded Critical Verses (100% Confidence)

These verses have been pre-determined based on theological and linguistic analysis:

| Verse | Value | Rationale |
|-------|-------|-----------|
| GEN.001.026 | **Trial** | "Let us make" - Trinity reference (Father, Son, Spirit) |
| GEN.001.027 | **Trial** | "In the image of God he created them; male and female" - continues Trinity context, but also dual human pair |
| GEN.011.007 | **Trial** | "Let us go down" - Trinity in judgment |
| LUK.024.013 | **Dual** | "Two of them were going" - explicit two disciples |
| MAT.018.020 | **Paucal** | "Where two or three gather" - small group (2-3) |
| ACT.013.002 | **Dual** | "Set apart for me Barnabas and Saul" - two missionaries |
| ACT.015.025 | **Plural** | "It seemed good to us" - apostolic council (multiple leaders) |
| ACT.015.028 | **Plural** | "It seemed good to the Holy Spirit and to us" - apostolic decision (multiple) |
| MRK.006.007 | **Dual** | "He sent them out two by two" - explicit pairing |

**Action**: If verse matches above table, return the specified value immediately.

---

## Level 2: Natural Pairs (High Confidence)

### Rule 2.1: Hebrew Dual Body Parts
If verse refers to paired body parts in Hebrew dual form:
- **Eyes** (עֵינַיִם, einayim)
- **Ears** (אָזְנַיִם, oznayim)
- **Hands** (יָדַיִם, yadayim)
- **Feet** (רַגְלַיִם, raglayim)

→ Return **Dual**

### Rule 2.2: Biblical Character Pairs
If verse prominently features these paired characters:
- **Moses and Aaron** → **Dual**
- **Peter and John** → **Dual**
- **Barnabas and Saul/Paul** → **Dual**
- **Two disciples** (unnamed pair in Gospels) → **Dual**
- **Adam and Eve** → **Dual**
- **Father and mother** (when both mentioned together) → **Dual**
- **Two angels** (Genesis 19, other passages) → **Dual**
- **Two witnesses** (Revelation 11) → **Dual**

→ Return **Dual**

### Rule 2.3: Creation Pairs
If verse references these paired elements:
- **Heaven and earth** (שָׁמַיִם וָאָרֶץ) → **Dual**
- **Male and female** (Gen 1:27) → **Dual**
- **Day and night** → **Dual**

→ Return **Dual**

---

## Level 3: Theological Context (Medium-High Confidence)

### Rule 3.1: Trinity Contexts
If verse is in Genesis 1-3 OR Genesis 11:1-9 AND contains:
- First person plural ("us", "our")
- Divine creative action
- God speaking in council

→ Return **Trial** (Trinitarian interpretation)

**Examples**:
- Any "Let us" statements in Gen 1-11 → **Trial**
- Divine council language in creation → **Trial**

### Rule 3.2: Small Group Worship/Gathering
If verse describes small intimate gathering (NOT large assembly):
- **2-3 people** gathering for prayer
- **House church** context (small home gathering)
- **Jesus + a few disciples** (not all 12)

→ Return **Paucal**

**Examples**:
- Matthew 18:19-20 (prayer context)
- Acts 2:46 (breaking bread in homes) → **Paucal**
- Small prayer groups

### Rule 3.3: Large Assembly/Apostolic Plural
If verse describes:
- **Apostolic council** (multiple apostles/elders deciding)
- **Church as whole** (addressing congregation)
- **Large crowd** (explicitly many people)

→ Return **Plural**

**Examples**:
- Acts 15 (Jerusalem Council) → **Plural**
- Epistles addressing "you all" (church) → **Plural**
- Crowd scenes with "many" → **Plural**

---

## Level 4: Symbolic/Prophetic Patterns (Medium Confidence)

### Rule 4.1: Quadrial Patterns
If verse references:
- **Four living creatures** (Ezekiel 1, Revelation 4)
- **Four corners of the earth**
- **Four winds**
- **Four rivers** (Genesis 2:10-14)
- **Four horns** (prophetic symbolism)

→ Return **Quadrial**

### Rule 4.2: Seven or Other Symbolic Numbers
If verse references:
- **Seven** (churches, seals, bowls) → **Plural**
- **Twelve** (tribes, apostles) → **Plural**
- **Seventy** or **Seventy-two** → **Plural**

→ Return **Plural**

---

## Level 5: Genre and Book Patterns (Low-Medium Confidence)

### Rule 5.1: Epistles Default
If book is epistle (Romans, Corinthians, Ephesians, etc.):
- Most references to "you" (addressing church) → **Plural**
- Paul + co-authors ("we") → **Plural** or **Dual** (if Paul + Timothy/Silas)

→ Default: **Plural**

### Rule 5.2: Gospel Narratives
If book is Gospel (Matthew, Mark, Luke, John):
- References to disciples → Check if pair or group
  - If pair mentioned → **Dual**
  - If "the disciples" (all) → **Plural**
  - If Jesus alone → **Singular**

→ Default: **Plural** (unless specific context suggests otherwise)

### Rule 5.3: Genesis Patterns
If book is Genesis:
- Genesis 1-11 (primeval history) → Higher Trial probability (creation contexts)
- Genesis 12-50 (patriarchal narratives) → Higher Dual probability (paired characters)

→ Default: **Dual** or **Trial** depending on chapter

---

## Level 6: Testament and Testament-Wide Patterns

### Rule 6.1: Old Testament Default
If testament is OT:
- More Dual (Hebrew dual forms common for natural pairs)
- More corporate Singular (Israel as collective)

→ Default: **Dual** (60%), **Plural** (30%), **Singular** (10%)

### Rule 6.2: New Testament Default
If testament is NT:
- More Plural (addressing churches)
- More Dual (disciple pairs)

→ Default: **Plural** (50%), **Dual** (35%), **Singular** (15%)

---

## Level 7: Final Default (Low Confidence)

If no rules above match:

**Count most likely participants in verse**:
- 1 clear referent → **Singular**
- 2 clear referents → **Dual**
- 3 clear referents → **Trial**
- 4 clear referents → **Quadrial**
- Small group (2-5) → **Paucal**
- Many referents (6+) → **Plural**

If uncertain, use **genre-based prior**:
- Narrative → **Dual** (most common in stories: protagonist + companion)
- Epistle → **Plural** (addressing churches)
- Poetry → **Singular** (often about God) or **Plural** (about people of God)
- Prophecy → **Plural** (nations, peoples)

---

## Confidence Levels

Assign confidence to each prediction:

- **HIGH (95%+)**: Level 1 (hardcoded), Level 2 (natural pairs with clear morphology)
- **MEDIUM-HIGH (85-94%)**: Level 2 (biblical character pairs), Level 3 (theological contexts)
- **MEDIUM (75-84%)**: Level 4 (symbolic patterns), Level 5 (genre patterns)
- **LOW-MEDIUM (60-74%)**: Level 6 (testament defaults)
- **LOW (<60%)**: Level 7 (final default, uncertain)

---

## Output Format

For each verse, output:

```yaml
reference: "{BOOK}.{chapter:03d}.{verse:03d}"
predicted_value: "{Singular|Dual|Trial|Quadrial|Paucal|Plural}"
confidence: "{HIGH|MEDIUM-HIGH|MEDIUM|LOW-MEDIUM|LOW}"
rule_applied: "{Level X: Rule description}"
reasoning: "{Brief explanation of why this number was chosen}"
```

---

## Example Applications

### Example 1: Genesis 1:26
```yaml
reference: "GEN.001.026"
predicted_value: "Trial"
confidence: "HIGH"
rule_applied: "Level 1: Hardcoded Critical Verse"
reasoning: "'Let us make mankind in our image' - Trinity reference (Father, Son, Holy Spirit). Christian orthodox interpretation uses Trial to grammatically encode Trinity."
```

### Example 2: Luke 24:13
```yaml
reference: "LUK.024.013"
predicted_value: "Dual"
confidence: "HIGH"
rule_applied: "Level 1: Hardcoded Critical Verse"
reasoning: "'Two of them were going to a village' - explicit count of two disciples. Greek δύο (duo) confirms dual number."
```

### Example 3: Matthew 18:20
```yaml
reference: "MAT.018.020"
predicted_value: "Paucal"
confidence: "HIGH"
rule_applied: "Level 1: Hardcoded Critical Verse"
reasoning: "'Where two or three gather in my name' - small group (2-3), not large assembly. Paucal distinguishes intimate gathering from corporate worship."
```

### Example 4: Hypothetical - Genesis 32:7 (Jacob and company)
```yaml
reference: "GEN.032.007"
predicted_value: "Dual"
confidence: "MEDIUM-HIGH"
rule_applied: "Level 2.2: Biblical Character Pairs"
reasoning: "Verse likely references Jacob dividing people into two groups. Dual appropriate for paired entities."
```

### Example 5: Hypothetical - Revelation 4:6 (Four living creatures)
```yaml
reference: "REV.004.006"
predicted_value: "Quadrial"
confidence: "MEDIUM-HIGH"
rule_applied: "Level 4.1: Quadrial Patterns"
reasoning: "'Four living creatures' around the throne - explicit count of 4. Quadrial marking (if language has it) grammatically encodes this symbolic number."
```

---

## Error Analysis Notes

After testing PROMPT1 on training set:
- Track which rules are most/least accurate
- Identify verses that fall through to low-confidence defaults
- Note any systematic misclassifications
- Update PROMPT2 with refined rules based on error patterns

---

**Status**: Ready for testing on training set (494 verses)  
**Next Step**: Apply PROMPT1 to train.yaml, document predictions, analyze accuracy  
**Commit Before Testing**: Lock predictions with git commit before checking TBTA values

