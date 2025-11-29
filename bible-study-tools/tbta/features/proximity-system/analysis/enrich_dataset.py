#!/usr/bin/env python3
"""
Enrich draft dataset with strongs_number and reason_group.
This script processes the draft dataset and adds required fields for training.
"""

import json
import sys
from pathlib import Path

# Reason groups based on THEOLOGICALLY-SIGNIFICANT-GROUPS.yaml and linguistic patterns
REASON_GROUPS = {
    # Theological contexts (non-arbitrary)
    "TRINITY": "Trinitarian references (Gen 1:26)",
    "CHRISTOLOGY": "Christological identifications (John 1:29, Acts 1:11)",
    "RESURRECTION": "Resurrection appearances (body parts)",
    "DIVINE-PRESENCE": "Divine presence and sacred space",
    "ESCHATOLOGY": "Eschatological timeframes (last days, beginning)",
    "COVENANTAL": "Covenantal language",
    "SACRAMENTAL": "Sacramental references",

    # Linguistic/contextual groups (mostly arbitrary)
    "BODY-PART": "Body parts (hands, feet, eyes) - speaker proximal",
    "PERSON-SINGULAR": "Individual persons (man, woman, servant)",
    "PERSON-PLURAL": "Groups of people (soldiers, disciples)",
    "PROPER-NAME": "Proper nouns (cities, mountains, people names)",
    "TEMPORAL-MARKER": "Time references (day, time, hour)",
    "SPATIAL-MARKER": "Place references (house, city, land, region)",
    "ABSTRACT-CONCEPT": "Abstract nouns (word, story, event, thing)",
    "NATURAL-OBJECT": "Natural objects (plant, water, mountain)",
    "ARTIFACT": "Man-made objects (bread, cloak, coins)",
    "ANAPHORIC-DISCOURSE": "Discourse demonstratives (this reason, such things)",
    "DEMONSTRATIVE-EMPHASIS": "Emphatic demonstratives (THIS Jesus)",
}

def infer_strongs_number(entry):
    """
    Infer the Strong's number for the constituent from the strongs list.

    Logic:
    1. Look for the constituent word in the strongs annotations
    2. Match by the glossed word (after the dash)
    3. Return the Strong's code
    """
    constituent = entry["constituent"].lower()

    # Handle entries without strongs field
    if "strongs" not in entry or not entry["strongs"]:
        return "MISSING"

    strongs_list = entry["strongs"].split()

    # Try to find matching Strong's number
    for strongs_item in strongs_list:
        if "-" in strongs_item:
            code, gloss = strongs_item.split("-", 1)
            # Match constituent to gloss
            gloss_lower = gloss.lower().strip("[]().")
            if constituent in gloss_lower or gloss_lower in constituent:
                return code
            # Handle plurals and variations
            if constituent.endswith('s') and constituent[:-1] in gloss_lower:
                return code
            if gloss_lower.endswith('s') and gloss_lower[:-1] in constituent:
                return code

    # If no match found, try without gloss filtering (just find the word in text)
    # This is a fallback - look for Strong's codes near the constituent in reconstructed text
    text = entry.get("text", "")
    if "**" in text:
        # The constituent is marked with **
        # Find nearby Strong's codes
        for strongs_item in strongs_list:
            if "-" in strongs_item:
                code, _ = strongs_item.split("-", 1)
                return code  # Return first strong's with gloss as best guess

    # Ultimate fallback - return first H/G code
    for strongs_item in strongs_list:
        if strongs_item.startswith(("H", "G")) and len(strongs_item) > 1:
            return strongs_item.split("-")[0]

    return "UNKNOWN"

def infer_reason_group(entry):
    """
    Infer the reason_group based on constituent type, label, and context.

    Logic:
    1. Check for theological contexts (verse-specific)
    2. Check for linguistic patterns (constituent + label)
    3. Default to appropriate category
    """
    constituent = entry["constituent"].lower()
    label = entry["label"]
    verse = entry["verse"]
    part = entry.get("part", "")

    # Theological contexts (specific verses)
    if verse == "GEN-001-026" and "us" in constituent.lower():
        return "TRINITY"
    if "john-001-029" in verse.lower() and "lamb" in constituent.lower():
        return "CHRISTOLOGY"
    if "luke-024-039" in verse.lower() and constituent in ["hand", "hands", "feet", "foot"]:
        return "RESURRECTION"
    if "exod-003-005" in verse.lower() and "place" in constituent:
        return "DIVINE-PRESENCE"
    if "heb-001-002" in verse.lower() and "day" in constituent:
        return "ESCHATOLOGY"
    if "gen-001-001" in verse.lower() and "beginning" in constituent:
        return "ESCHATOLOGY"
    if "acts-001-011" in verse.lower() and "jesus" in constituent.lower():
        return "CHRISTOLOGY"

    # Body parts (always Near Speaker)
    if constituent in ["hand", "hands", "foot", "feet", "eye", "eyes", "ear", "ears",
                       "head", "mouth", "heart", "face", "arm", "leg", "finger", "toe"]:
        return "BODY-PART"

    # Person references
    if constituent in ["man", "woman", "person", "servant", "slave", "child", "son",
                       "daughter", "father", "mother", "brother", "sister", "king",
                       "prophet", "priest"]:
        return "PERSON-SINGULAR"

    if constituent in ["soldiers", "soldier", "disciple", "disciples", "people", "crowd",
                       "men", "women", "children", "servants", "priests"]:
        return "PERSON-PLURAL"

    # Proper names
    if constituent[0].isupper() or part == "Proper Noun":
        return "PROPER-NAME"

    # Temporal markers
    if constituent in ["day", "days", "time", "hour", "year", "month", "week",
                       "morning", "evening", "night", "moment"]:
        return "TEMPORAL-MARKER"

    # Spatial markers
    if constituent in ["place", "house", "city", "land", "region", "town", "village",
                       "mountain", "hill", "valley", "desert", "field", "room"]:
        return "SPATIAL-MARKER"

    # Abstract concepts
    if constituent in ["word", "words", "thing", "things", "story", "event", "reason",
                       "way", "manner", "kind", "type", "matter"]:
        return "ABSTRACT-CONCEPT"

    # Natural objects
    if constituent in ["plant", "plants", "tree", "trees", "water", "waters", "stone",
                       "stones", "rock", "rocks", "animal", "animals", "bird", "fish"]:
        return "NATURAL-OBJECT"

    # Artifacts
    if constituent in ["bread", "wine", "cup", "garment", "cloak", "sandal", "coin",
                       "coins", "vessel", "jar", "basket"]:
        return "ARTIFACT"

    # Check for emphatic demonstratives
    if label == "Contextually Near with Focus":
        return "DEMONSTRATIVE-EMPHASIS"

    # Anaphoric discourse
    if label in ["Contextually Near", "Contextually Near with Focus"]:
        return "ANAPHORIC-DISCOURSE"

    # Default fallback
    return "SPATIAL-MARKER"

def add_difficulty(entry, reason_group):
    """
    Add difficulty level based on reason_group and context.
    """
    # Adversarial cases (theologically critical)
    if reason_group in ["TRINITY", "CHRISTOLOGY", "RESURRECTION", "DIVINE-PRESENCE",
                        "ESCHATOLOGY", "COVENANTAL", "SACRAMENTAL"]:
        return "adversarial"

    # Tricky cases
    if reason_group in ["DEMONSTRATIVE-EMPHASIS", "BODY-PART"]:
        return "hard"

    # Default - leave blank for arbitrary/easy
    return ""

def process_entry(entry):
    """Process a single entry and add required fields."""
    # Infer strongs_number
    strongs_number = infer_strongs_number(entry)

    # Infer reason_group
    reason_group = infer_reason_group(entry)

    # Add difficulty
    difficulty = add_difficulty(entry, reason_group)

    # Update dataset section
    if "dataset" not in entry:
        entry["dataset"] = {}

    entry["dataset"]["reason_group"] = reason_group
    if difficulty:
        entry["dataset"]["difficulty"] = difficulty

    # Add strongs_number at top level (not in dataset)
    entry["strongs_number"] = strongs_number

    # Ensure we have reconstructed_verse (use text field)
    if "reconstructed_verse" not in entry and "text" in entry:
        entry["reconstructed_verse"] = entry["text"]

    return entry

def main():
    input_file = Path("/workspace/bible-study-tools/tbta/features/proximity-system/analysis/draft_datasets.jsonl/datasets.jsonl")
    output_file = Path("/workspace/bible-study-tools/tbta/features/proximity-system/analysis/datasets.jsonl")

    print(f"Processing {input_file}...")

    processed = []
    with open(input_file, 'r') as f:
        for line_num, line in enumerate(f, 1):
            if line.strip():
                entry = json.loads(line)
                processed_entry = process_entry(entry)
                processed.append(processed_entry)

                if line_num % 100 == 0:
                    print(f"Processed {line_num} entries...")

    print(f"Writing {len(processed)} entries to {output_file}...")
    with open(output_file, 'w') as f:
        for entry in processed:
            f.write(json.dumps(entry) + '\n')

    print("Done!")

    # Print statistics
    reason_groups = {}
    for entry in processed:
        rg = entry["dataset"].get("reason_group", "UNKNOWN")
        reason_groups[rg] = reason_groups.get(rg, 0) + 1

    print("\nReason Group Distribution:")
    for rg, count in sorted(reason_groups.items(), key=lambda x: -x[1]):
        print(f"  {rg}: {count}")

if __name__ == "__main__":
    main()
