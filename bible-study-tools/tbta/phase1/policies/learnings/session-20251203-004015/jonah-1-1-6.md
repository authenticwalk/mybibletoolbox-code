# Jonah 1:1-6 — Learning Session

## Passage
1 The word of the LORD came to Jonah son of Amittai: 2 "Go to the great city of Nineveh and preach against it, because its wickedness has come up before me." 3 But Jonah ran away from the LORD and headed for Tarshish. He went down to Joppa, where he found a ship bound for that port. After paying the fare, he went aboard and sailed for Tarshish to flee from the LORD. 4 Then the LORD sent a great wind on the sea, and such a violent storm arose that the ship threatened to break up. 5 All the sailors were afraid and each cried out to his own god. And they threw the cargo into the sea to lighten the ship. But Jonah had gone below deck, where he lay down and fell into a deep sleep. 6 The captain went to him and said, "How can you sleep? Get up and call on your god! Maybe he will take notice of us so that we will not perish."

## Reference Encoding
**v1:** Jonah (title) run-away from Yahweh. One day Yahweh spoke to Jonah. Jonah was Amittai's son.
**v2:** You(Jonah) (imp) go to the great city named Nineveh. You(Jonah) (imp) tell [the people [who are living in Nineveh] to stop doing evil things]. I(Yahweh) know [that the people [who are living in Nineveh] do evil things often].
**v3:** But Jonah run-away from Yahweh. Jonah decided [to go to Tarshish]. So Jonah went to Joppa. And Jonah found a ship [that will go to Tarshish]. Jonah paid the man [that owned that ship]. Then Jonah entered that ship. Then the ship started going to Tarshish. Jonah was run-away from Yahweh.
**v4:** But Yahweh caused [a strong wind to blow on the Mediterranean Sea]. And that wind caused a very big storm. The men [who were on that ship] were afraid [that the storm might break the ship into pieces].
**v5:** All of The men [who worked on that ship] were afraid. Each man cried out to that man's god. Those men asked [the men's gods to help the men]. Some (implicit-info) heavy things were on that ship. Those men threw the heavy things from the ship into the sea [so that the ship would become lighter]. But Jonah had gone inside that ship [because Jonah wanted [to sleep]]. So Jonah was sleeping.
**v6:** The leader of the ship came to Jonah. And the leader said to Jonah, [Why are you(Jonah) sleeping]? You(Jonah) (imp) Get up. And you(Jonah) (imp) pray to your(Jonah's) god! You(Jonah) (imp) ask [your(Jonah's) god to help us(men)]. Perhaps your(Jonah's) god will hear your(Jonah's) prayer. Then we(men) will not die.

## Results
| Agent | Match | Errors | Iterations |
|-------|-------|--------|------------|
| V1 | Low | 0 | 12 |
| V2 | Low | 0 | 9 |
| V3 | Low | 12+ | 12 |

## Winner
None — All versions missed key structural patterns from reference

## Patterns Discovered
1. `(title)` marker used at start of narrative sections (Jon 1:1)
2. "One day" opener for narrative starts (Jon 1:1)
3. "caused [X to verb]" causative construction (Jon 1:4)
4. "decided [to verb]" for intent (Jon 1:3)
5. "the man [that owned X]" for ownership (Jon 1:3)
6. "heavy things" not "cargo" for ship goods (Jon 1:5)
7. "(implicit-info)" marker style in He1 (Jon 1:5)
8. "leader of the ship" not "captain" (Jon 1:6)
9. "Perhaps" not "Maybe" for possibility (Jon 1:6)
10. "Mediterranean Sea" explicit naming (Jon 1:4)
11. "men [who worked on that ship]" for sailors (Jon 1:5)
12. "[that will go to X]" future in relative clause (Jon 1:3)

## Issues Unresolved
- V3 linter API appears to have issues with nested brackets in quotes
- All versions over-simplified vocabulary instead of following reference patterns
