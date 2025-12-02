# TBTA Name and Title Introduction Patterns

Analysis of Column 3 (Verse - CNL transformation) from TBTA CSV files.
Focus: How names, titles, and characters are introduced and referenced.

## 1. "(title)" MARKERS

The system uses explicit "(title)" markers to indicate chapter/section headings or major narrative transitions.

### Examples:

**Ruth 1:1**
```
"Elimelech (title) and Naomi move from Bethlehem to Moab."
```
- "(title)" appears immediately after the character name
- Marks a new narrative section
- Functions as a section header

**Ruth 2:1**
```
"Ruth (title) meets Boaz."
```

**Ruth 3:1**
```
"Ruth (title) meets Boaz at the place [that people separate the grain from the plants at]."
```

**Ruth 4:1**
```
"(title) Boaz marries Ruth."
```
- When "(title)" appears at the beginning, it marks the entire phrase as a section heading

**Matthew 2:1**
```
"Wise men (title) visit Jesus."
```

**Matthew 5:1**
```
"(title) Jesus teaches/preach about God's laws to people on a mountain."
```

**1 Samuel 1:1**
```
"(title) Samuel is born."
```

## 2. FIRST MENTION vs SUBSEQUENT MENTIONS

### Pattern A: Indefinite Introduction → Definite Reference

**Ruth 1:1-2** (First introduction pattern)
```
v1: "A certain man was from Bethlehem [which was in Judah]. That man..."
v2: "That man's name was Elimelech."
```
- **First mention**: "A certain man" (indefinite)
- **Immediate follow-up**: "That man" (definite reference)
- **Naming**: "That man's name was Elimelech" (explicit naming formula)

**Genesis 2:7-19** (Adam introduction)
```
v7: "[When God created man] God used the dust..."
v7: "God breathed into the nose of the man."
v19: "God called this man Adam. Adam means person."
```
- **First mention**: "man" (generic)
- **Subsequent**: "the man" (definite)
- **Official naming**: "God called this man Adam. Adam means person."

### Pattern B: Direct Introduction by Name

**Ruth 1:1**
```
"Elimelech (title) and Naomi move from Bethlehem to Moab."
```
- Characters introduced directly by name in narrative summary
- No indefinite introduction needed

**Genesis 1:1**
```
"God started creating the heavens and the earth."
```
- God introduced directly by name, no indefinite article

### Pattern C: Multiple Character Naming Sequence

**Ruth 1:2**
```
"That man's name was Elimelech. And that man's wife's name was Naomi.
One son's name was Mahlon. And the other son's name was Kilion."
```
- Uses formula: "[person/role]'s name was [Name]"
- Sequential introduction of family members
- Maintains parallel structure

**1 Samuel 1:1-2**
```
v1: "That man's name was Elkanah. He was a son of Jeroham..."
v2: "One wife's name was Hannah. And the other wife's name was Peninnah."
```

## 3. "A [ROLE] NAMED [NAME]" PATTERN

This is the most common pattern for introducing new characters mid-narrative.

### Examples:

**Ruth 1:4**
```
"One son married a woman named Orpah. The other son married a woman named Ruth."
```
- Formula: "a [role] named [Name]"
- Used for new character introductions within existing narrative

**Genesis 4:1** (from grep results)
```
"Adam sexed Adam's wife named Eve. Then Eve became pregnant.
Eve birthed a son named Cain."
```
- Pattern repeats: "wife named Eve", "son named Cain"

**1 Samuel 1:4**
```
"Elkanah gave some meat to Elkanah's wife named Peninnah."
```

**1 Samuel 1:9**
```
"The priest named Eli was at the tabernacle."
```

**1 Samuel 2:34**
```
"Your(Eli's) sons named Hophni and Phinehas will die on the same day."
```
- Can include multiple names in one phrase

**Ruth 4:18-22** (Genealogy pattern)
```
"Perez had a son named Hezron."
"Hezron had a son named Ram. Ram had a son named Amminadab."
"Amminadab had a son named Nahshon. Nahshon had a son named Salmon."
"Salmon had a son named Boaz. Boaz had a son named Obed."
"Obed had a son named Jesse. And Jesse had a son named David."
```
- Genealogies use consistent "X had a son named Y" formula
- Highly repetitive and predictable structure

**Genesis 4:17-18** (from grep results)
```
"Cain's wife birthed a son named Enoch."
"Enoch had a son named Irad. Then Irad had a son named Mehujael.
Mehujael had a son named Methushael. And Methushael had a son named Lamech."
```

## 4. TITLE + NAME COMBINATIONS

### Pattern A: Role/Title before Name

**Ruth 2:1**
```
"Naomi had a relative named Boaz."
```
- Role identified first: "a relative"
- Then named: "named Boaz"

**Matthew 2:1** (from grep results)
```
"[when king Herod ruled the people _implicit of Judea]"
```
- Title "king" + name "Herod"
- Lowercase "king" suggests it's descriptive, not formal title

**1 Samuel 1:9**
```
"The priest named Eli was at the tabernacle."
```
- "The priest" (role) + "named Eli"

**1 Samuel 2:30** (from grep results)
```
"Therefore Israel's God named Yahweh says"
```
- Possessive + role + name: "Israel's God named Yahweh"

### Pattern B: Descriptive Clauses for Titles

**Ruth 1:3**
```
"Elimelech [who was Naomi's husband] died later."
```
- Brackets indicate descriptive/clarifying information
- Relationship stated in relative clause

**1 Samuel 2:10** (from grep results)
```
"the man [who Yahweh chose/appointed to be king]"
```
- Long descriptive clause instead of simple "king X"

### Pattern C: The + Role/Title (Definite Groups)

**Matthew examples:**
```
"the Pharisees"
"the scribes"
"the disciples"
"the priests"
"the Sadducees"
```
- Always definite article "the"
- Refers to established groups

## 5. GROUP INTRODUCTIONS

### Pattern A: The + Group Name

**Matthew 9:11**
```
"[When the Pharisees saw [those people eating]"
```
- "the Pharisees" - definite article, treated as known group

**Matthew 12:2**
```
"[When the Pharisees saw [the followers/disciples eat the grains"
```
- "the Pharisees" and "the followers/disciples"
- Both groups get definite article

**Matthew 12:38**
```
"Then some Pharisees and some scribes said to Jesus"
```
- "some Pharisees" - indefinite quantity from known group
- "some scribes" - parallel structure

### Pattern B: Possessive + Group

**Matthew 9:14**
```
"Then John the Baptist's followers/disciples came."
```
- Group defined by relationship: "John the Baptist's followers/disciples"

**Matthew 12:5**
```
"the priests [who work in the temple on the Sabbath]"
```
- Generic group + descriptive clause

### Pattern C: Generic People References

**Ruth 1:1**
```
"many people [who were living in Israel] did not have enough food"
```
- "many people" (indefinite quantity)
- Bracket adds descriptive clause

**Matthew 5:3**
```
"People [who have a poor spirit] are blessed by God"
```
- Generic "people" + descriptive bracket

## 6. SPECIAL NAMING PATTERNS

### Pattern A: Explicit Naming Formula

**Genesis 2:19**
```
"God called this man Adam. Adam means person."
```
- "God called [X] [Name]"
- Etymology/meaning provided: "Adam means person"

**Genesis 2:23** (from grep results)
```
"Adam named the wife of Adam Eve [because Eve was the mother of all the people
[that will live on the earth]]. Eve means live."
```
- Name + reason bracket + etymology

**Genesis 4:25** (from grep results)
```
"Eve named that son Seth. Eve said..."
```
- "[Person] named [object/person] [Name]"

### Pattern B: Place Name Pattern

**Ruth 1:2**
```
"a town named Bethlehem [which was in Judah]"
"a country named Moab"
```
- "a [place type] named [Name]"
- Optional location bracket

**Matthew 2:1**
```
"Bethlehem named the town _implicit in Judea named the region/province _implicit"
```
- Nested naming: town name + region name

**1 Samuel 1:1** (from grep results)
```
"a town named Ramathaim"
"the tribe named Ephraim"
```

### Pattern C: Name Changes and Clarifications

**Matthew 10:2** (from grep results)
```
"Simon [who was called Peter by people _implicitActiveAgent]"
```
- Original name + bracket with alternate name
- Passive construction: "was called Peter by people"

## 7. FIRST vs LATER REFERENCE TRACKING

### Example: Ruth in Ruth 1

**First Introduction (Ruth 1:4):**
```
"One son married a woman named Ruth."
```
- Indefinite: "a woman"
- Named: "named Ruth"

**Later Reference (Ruth 1:14):**
```
"But Ruth refused [to leave Naomi]."
```
- Direct name reference, no article
- Assumed known from previous introduction

**Further Reference (Ruth 2:2):**
```
"One day Ruth [who was from Moab] said to Naomi"
```
- Name used directly
- Optional clarifying bracket added

### Example: Elimelech in Ruth 1

**First Introduction (Ruth 1:1-2):**
```
v1: "A certain man was from Bethlehem"
v2: "That man's name was Elimelech."
```
- Indefinite → definite → named

**Later Reference (Ruth 1:3):**
```
"Elimelech [who was Naomi's husband] died later."
```
- Direct name
- Relationship clarified in bracket

**Later Reference (Ruth 2:1):**
```
"Boaz was in Elimelech's family/clan."
```
- Used in possessive form
- No reintroduction needed

### Example: Naomi in Ruth 1

**First Introduction (Ruth 1:1-2):**
```
v1: "Elimelech (title) and Naomi move..."
v2: "that man's wife's name was Naomi"
```
- Named in title header
- Then formally introduced with naming formula

**Subsequent Uses:**
- "Naomi lived with..." (Ruth 1:3)
- "Naomi's sons" (Ruth 1:4)
- "Naomi was alone" (Ruth 1:5)
- "Naomi prepared" (Ruth 1:6)
- Consistently uses bare name, no article

### Example: God in Genesis 1

**First Mention (Genesis 1:1):**
```
"God started creating the heavens and the earth."
```
- Direct name, no introduction

**Subsequent Mentions:**
```
"And the Spirit of God moved over the water" (1:2)
"Then God said" (1:3)
"God saw the light" (1:4)
"And God thought" (1:4)
"Then God separated" (1:4)
"God called the light day. And God called the darkness night" (1:5)
```
- Always "God" (bare name)
- Never "the God" or "a God"
- Treated as proper name from first use

## 8. IMPLICIT INFORMATION MARKERS

### Pattern: Parenthetical Implicit Markers

**Ruth 2:1**
```
"Boaz (implicit-info) lived in Bethlehem. And (implicit-info) Boaz was rich."
```
- "(implicit-info)" marks information inferred from context
- Not explicitly stated in source text

**Matthew 2:1**
```
"Bethlehem named the town _implicit in Judea named the region/province _implicit"
```
- "_implicit" marks information added for clarity

**Matthew 8:21**
```
"And another follower/disciple of Jesus _implicit said to Jesus"
```
- Relationship inferred: "_implicit"

## 9. ROLE/RELATIONSHIP MARKERS

### Pattern: Brackets for Relationships

**Ruth 1:3**
```
"Elimelech [who was Naomi's husband]"
```

**Ruth 1:4**
```
"women [that were from Moab]"
```

**Ruth 2:3**
```
"a field [that belonged to Boaz]"
```

**Matthew 10:2** (from grep results)
```
"Simon's brother named Andrew"
```
- Possessive shows relationship

## 10. SUMMARY OF KEY PATTERNS

### First Introduction Patterns:

1. **Indefinite + Named**: "A certain man... That man's name was X"
2. **Role + Named**: "a woman named X", "a son named Y"
3. **Direct Name**: "God started...", "Elimelech and Naomi..."
4. **Title + Named**: "king Herod", "the priest named Eli"

### Subsequent Reference Patterns:

1. **Bare Name**: "Elimelech died", "Naomi prepared"
2. **Name + Clarification**: "Ruth [who was from Moab]"
3. **Possessive**: "Naomi's sons", "Elimelech's family"
4. **Pronoun**: After establishing referent

### Group Patterns:

1. **Definite Groups**: "the Pharisees", "the disciples"
2. **Indefinite Quantity**: "some Pharisees and some scribes"
3. **Generic**: "many people [who...]", "People [who...]"

### Special Markers:

1. **Section Headers**: "(title)" at start or after name
2. **Implicit Info**: "(implicit-info)", "_implicit"
3. **Relationship**: Brackets with "who" clauses
4. **Etymology**: "Adam means person", "Eve means live"

## PATTERNS BY BOOK

### Genesis
- Heavy use of "X named Y" for genealogies
- Explicit naming formulas: "God called X Y"
- Etymology notes: "Adam means person"
- Direct name usage for God (no articles)

### Ruth
- "(title)" markers for section headers
- "A certain man" → "That man's name was X" pattern
- "a [role] named [Name]" for new characters
- Extensive use of clarifying brackets

### Matthew
- "(title)" for teaching sections
- Group references: "the Pharisees", "the disciples"
- Title + name: "king Herod"
- Implicit information markers
- "a man [who had...]" pattern for unnamed individuals

### 1 Samuel
- Heavy use of "named X" pattern
- Possessive constructions: "Israel's God named Yahweh"
- Title + named pattern: "the priest named Eli"
- Genealogical formulas similar to Genesis
