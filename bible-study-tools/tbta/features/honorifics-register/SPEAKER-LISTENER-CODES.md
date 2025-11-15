# Speaker and Listener Character Codes

Complete enumeration of all speaker and listener codes in TBTA. These codes identify who is speaking and who is being addressed in dialogue clauses.

---

## Usage

- **Speaker field**: Identifies who is speaking
- **Listener field**: Identifies who is being addressed
- Both fields use the same code set
- **Value "0"**: Special case for narrative (no dialogue)

---

## Special Divine/Generic Codes

| Code | Identity | Description | Usage Context |
|------|----------|-------------|---------------|
| 0 | Not Applicable | Narrative voice, no dialogue | All non-dialogue clauses |
| M | God | God the Father speaking | Divine speech in OT/NT |
| R | Jesus | Jesus Christ speaking | Gospel accounts, Revelation |
| T | Generic Man | Unspecified human, generic reference | Parables, hypothetical examples |

---

## Major Biblical Characters

### Old Testament Patriarchs

| Code | Character | Role | Example Verses |
|------|-----------|------|----------------|
| A | Abraham | Patriarch | Genesis 12-25 dialogue |
| I | Isaac | Son of Abraham | Genesis 21-35 |
| J | Jacob/Israel | Patriarch | Genesis 25-50 |
| O | Joseph | Son of Jacob | Genesis 37-50 |
| S | Moses | Prophet, Law-giver | Exodus-Deuteronomy |
| a | Aaron | High Priest | Exodus-Numbers |
| D | David | King | 1-2 Samuel, 1 Kings, Psalms |

### Old Testament Prophets

| Code | Character | Role | Example Books |
|------|-----------|------|---------------|
| E | Elijah | Prophet | 1-2 Kings |
| e | Elisha | Prophet | 2 Kings |
| I | Isaiah | Major Prophet | Isaiah |
| j | Jeremiah | Major Prophet | Jeremiah |
| z | Ezekiel | Major Prophet | Ezekiel |
| d | Daniel | Prophet | Daniel |

### Old Testament Kings and Leaders

| Code | Character | Role | Example Books |
|------|-----------|------|---------------|
| S | Saul | First King | 1 Samuel |
| D | David | King | 1-2 Samuel, 1 Kings |
| s | Solomon | King | 1 Kings, Proverbs |
| N | Nehemiah | Governor | Nehemiah |

### Old Testament Women

| Code | Character | Role | Example Books |
|------|-----------|------|---------------|
| E | Eve | First woman | Genesis 2-3 |
| r | Sarah | Abraham's wife | Genesis |
| h | Rebekah | Isaac's wife | Genesis |
| R | Ruth | Moabite convert | Ruth |
| n | Naomi | Ruth's mother-in-law | Ruth |
| H | Hannah | Samuel's mother | 1 Samuel |
| b | Bathsheba | David's wife | 2 Samuel |

---

## New Testament Characters

### Disciples and Apostles

| Code | Character | Role | Example Books |
|------|-----------|------|---------------|
| P | Peter/Simon | Chief Apostle | Gospels, Acts, Epistles |
| J | John | Beloved Disciple | Gospel of John, Epistles, Revelation |
| A | Andrew | Apostle | Gospels |
| j | James (son of Zebedee) | Apostle | Gospels, Acts |
| t | Thomas | Apostle | John (doubting Thomas) |
| M | Matthew | Apostle, Tax collector | Matthew |
| p | Philip | Apostle | John |
| n | Nathanael/Bartholomew | Apostle | John 1 |

### Paul and Associates

| Code | Character | Role | Example Books |
|------|-----------|------|---------------|
| P | Paul/Saul | Apostle to Gentiles | Acts, Epistles |
| B | Barnabas | Companion of Paul | Acts |
| t | Timothy | Paul's protégé | Acts, Epistles to Timothy |
| T | Titus | Paul's co-worker | Titus |
| S | Silas/Silvanus | Paul's companion | Acts |

### Gospel Characters

| Code | Character | Role | Example Books |
|------|-----------|------|---------------|
| M | Mary (mother of Jesus) | Mother of Christ | Gospels, Acts |
| m | Mary Magdalene | Follower of Jesus | Gospels |
| j | Joseph (earthly father) | Husband of Mary | Matthew, Luke |
| z | Zechariah | John Baptist's father | Luke 1 |
| E | Elizabeth | Mother of John Baptist | Luke 1 |
| B | John the Baptist | Forerunner | All Gospels |

### Antagonists and Officials

| Code | Character | Role | Example Books |
|------|-----------|------|---------------|
| P | Pontius Pilate | Roman Governor | Gospels |
| H | Herod | King | Gospels |
| A | Annas | High Priest | John |
| C | Caiaphas | High Priest | Gospels |
| S | Sanhedrin | Jewish Council | Gospels, Acts |
| p | Pharisees | Religious leaders | Gospels |
| s | Sadducees | Religious sect | Gospels, Acts |

### Other Notable NT Characters

| Code | Character | Role | Example Books |
|------|-----------|------|---------------|
| L | Lazarus | Friend of Jesus | John 11 |
| N | Nicodemus | Pharisee, secret follower | John |
| S | Samaritan woman | Woman at well | John 4 |
| z | Zacchaeus | Tax collector | Luke 19 |

---

## Generic Groups and Roles

| Code | Character | Description | Usage |
|------|-----------|-------------|-------|
| D | Disciples | Generic reference to disciples | When not specifying individual |
| C | Crowd | Unspecified crowd/multitude | Public teachings |
| p | Pharisees | Group of Pharisees | Corporate opposition |
| s | Sadducees | Group of Sadducees | Religious disputes |
| S | Scribes | Teachers of the Law | Legal discussions |
| E | Elders | Jewish elders | Council scenes |
| P | Priests | Temple priests | Worship contexts |
| R | Romans | Roman soldiers/officials | Political contexts |
| G | Gentiles | Non-Jewish people | Mission contexts |
| W | Women | Group of women | Generic female collective |
| c | Children | Generic children | Teaching scenes |

---

## Angels and Spiritual Beings

| Code | Character | Description | Usage |
|------|-----------|-------------|-------|
| A | Angel | Unspecified angel | Announcements, visions |
| G | Gabriel | Archangel | Luke 1, Daniel |
| M | Michael | Archangel | Daniel, Jude, Revelation |
| S | Satan | The adversary | Job, Gospels, Revelation |
| d | Demons | Evil spirits | Exorcism accounts |

---

## Parable and Hypothetical Characters

| Code | Character | Description | Usage |
|------|-----------|-------------|-------|
| T | Generic Man | Hypothetical man in parable | "A certain man..." |
| F | Father | Generic father figure | Prodigal Son, family examples |
| S | Son | Generic son | Parable characters |
| s | Servant | Generic servant/slave | Many parables |
| M | Master | Generic master/lord | Parable authority figures |
| K | King | Hypothetical king | Kingdom parables |
| J | Judge | Generic judge | Parable of persistent widow |

---

## Special Case: Multiple Speakers

When multiple people speak in unison (e.g., a crowd responding together), the code represents the collective group:

- **Example**: Crowd shouting "Hosanna!" → Speaker = "C" (Crowd)
- **Example**: Disciples responding together → Speaker = "D" (Disciples)

---

## Code Assignment Guidelines

### Priority Order for Code Selection

1. **Named individuals**: Use specific character code (Peter = "P", Moses = "S")
2. **Identified role**: Use role code (Pharisees = "p", Priest = "P")
3. **Generic group**: Use group code (Crowd = "C", Children = "c")
4. **Unspecified human**: Use "T" (Generic Man)
5. **Narrative voice**: Use "0" (Not Applicable)

### Disambiguation Rules

When same code could represent multiple characters:
- **Context determines**: Code "P" = Peter (Gospels), Paul (Acts+), Pilate (trial scenes)
- **Use neighboring clauses**: Check who was speaking in previous dialogue
- **Use vocatives**: Check who is being addressed (listener) to identify speaker

### Edge Cases

**Quoted within quoted speech**: Use innermost speaker
```
Example: John says, "Jesus told me, 'Follow me.'"
- Outer clause: Speaker = John
- Inner clause: Speaker = Jesus (R)
```

**Narrator reporting speech act without quote**: Speaker = "0"
```
Example: "Then Jesus told them the parable"
- This is narrative, not quoted speech
- Speaker = "0"
```

**Collective divine speech (Trinity)**: Use "M" (God) for corporate divine action
```
Example: Genesis 1:26 "Let us make mankind"
- Speaker = "M" (God, corporate)
```

---

## Cross-Reference with Age and Attitude

### Typical Age Codes by Character

- **God (M)**: Age = "N" (Not Applicable)
- **Jesus (R)**: Age = "C" (Adult, 30-33 during ministry)
- **John Baptist (B)**: Age = "C" (Adult)
- **Children (c)**: Age = "A" (Child)
- **Elders (E)**: Age = "D" (Elder)

### Typical Attitude by Relationship

- **Speaker = M (God) → Listener = human**: Attitude often "H" (Honorable) or "n" (Neutral)
- **Speaker = human → Listener = M (God)**: Attitude typically "H" (Honorable), Style = "Liturgical"
- **Speaker = Jesus → Listener = Disciples**: Attitude varies "n" (Neutral teaching) to "F" (Familiar)
- **Speaker = Pharisees → Listener = Jesus**: Attitude ranges "P" (Polite, testing) to hostile

---

## Validation Checklist

When assigning Speaker/Listener codes:

- [ ] Is this a dialogue clause? (If no, use "0")
- [ ] Can you identify the speaker from context?
- [ ] Is there a quote marker (-QuoteBegin/-QuoteEnd)?
- [ ] Does the code match the character's identity in this verse?
- [ ] Is the code consistent with previous uses of this character?
- [ ] If group/generic, is there a more specific individual code available?

---

## References

- See **SPEAKER-DEMOGRAPHICS-README.md** for how Speaker/Listener integrate with other demographics features
- See **ATTITUDE-EXAMPLES.md** for verse examples showing speaker/listener in context
- See **VALIDATION-CHECKLIST.md** for complete validation procedures

---

**Note**: This enumeration covers the most common codes in TBTA. Additional codes may exist for minor characters. When encountering unknown codes, consult the TBTA database or infer from context.
