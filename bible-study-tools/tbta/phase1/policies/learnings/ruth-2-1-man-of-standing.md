# Ruth 2:1 - "Man of Standing" Analysis

## Original NIV
"Now Naomi had a relative on her husband's side, a man of standing from the clan of Elimelek, whose name was Boaz."

## My He1 Draft
"Naomi had a relative. That relative was from Elimelech's family/clan. That relative was an important man. That man's name was Boaz."

## Reference phase_1_encoding
"Ruth (title) meets Boaz. Naomi had a relative named Boaz. Boaz was in Elimelech's family/clan. People respected Boaz much. Boaz (implicit-info) lived in Bethlehem. And (implicit-info) Boaz was rich."

## Diagnosis

### Issue 1: "man of standing" simplified too much
- I translated "man of standing" as "important man"
- Reference expands to TWO concepts: respect + wealth
- "People respected Boaz much" (explicit)
- "Boaz was rich" (implicit)
- Hebrew אִישׁ גִּבּוֹר חַיִל (ish gibbor chayil) means wealthy/prominent/influential man

### Issue 2: "was from" vs "was in" for clan membership
- I used "was from Elimelech's family/clan"
- Reference uses "was in Elimelech's family/clan"
- "in" expresses membership/belonging, "from" expresses origin/departure
- For ongoing clan membership, use "in"

### Issue 3: Title missing
- Should include "(title) Ruth meets Boaz" for section headers
- NIV has section breaks that should be represented

### Issue 4: Name introduction pattern
- I used: "That relative...That man's name was Boaz"
- Reference uses: "a relative named Boaz"
- More concise to put "named X" directly with the noun

## Learnings Applied
1. "man of standing" → "People respected X much" + "(implicit-info) X was rich"
2. Use "was in X's family/clan" for membership, not "was from"
3. Include "(title)" for section headers
4. Prefer "a [noun] named [name]" over separate "X's name was [name]" sentence
