# Matthew 2:1-10 — He1 Encoding (V2 Final)

## He1 Output (Iteration 1)

**Verse 1:**
[After Jesus born in Judea-Name region in Bethlehem-Name town, while Herod-Title king rule person of Judea], wise man travel eastern region Jerusalem-Name city.

**Verse 2:**
And wise man ask. Wise man ask, ["Where child [who born-Title king of person of Judea]? We(wise man) see that child's star [when that star rise]. And we(wise man) travel [in-order-to we(wise man) bow-to that child]."]

**Verse 3:**
[When Herod hear that], Herod disturb. And all person in city disturb with Herod.

**Verse 4:**
[When Herod call-together all important priest and teacher of law of person], Herod ask that man where Messiah to born.

**Verse 5:**
That man reply, ["Messiah to born in Bethlehem-Name town in Judea-Name region, [because that what prophet write]:]"

**Verse 6:**
["But you(Bethlehem), Bethlehem in region-Name land of Judah, not least among ruler of Judah by no means. Because ruler [who will care-for my(God's) people-Name Israel] will come from you(Bethlehem)."]

**Verse 7:**
Then Herod call wise man secretly. And Herod find-out from wise man exact time [when star appear].

**Verse 8:**
Herod send wise man to Bethlehem-Name town. And Herod say to wise man, ["You(wise man) (imp) go. And you(wise man) (imp) search carefully for child. [As-soon-as you(wise man) find child], you(wise man) (imp) tell me(Herod), [so-that I(Herod) too may go and bow-to child]."]

**Verse 9:**
[After wise man hear that king], wise man go on wise man's way. And star [that wise man see [when star rise]] go ahead wise man [until star stop above place [where child was]].

**Verse 10:**
[When wise man see star], wise man very happy.

---

## Notes on Transformations

1. **Coreference**: Resolved all pronouns to explicit nouns
2. **Named formula**: Using "-Name" adposition (e.g., "Bethlehem-Name town")
3. **Wise men**: "wise man" (plural, two words as in TBTA data)
4. **Deixis**: "I(Speaker)", "you(Addressee)", "we(Group)"
5. **Brackets**: All subordinate clauses in [...]
6. **Discourse**: "And", "Then", "But", "Because"
7. **Verbs**: Base forms (rise, not rose; go, not went)
8. **Speech**: ["..."] for quotes
9. **Imperatives**: (imp) marker before verb
10. **Titles**: "-Title" for roles (e.g., "Herod-Title king")

## Testing Plan

Test each verse individually with linter, iterate up to 12 times per verse until clean.
