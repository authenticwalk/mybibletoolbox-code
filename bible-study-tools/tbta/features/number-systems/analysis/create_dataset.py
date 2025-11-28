#!/usr/bin/env python3
"""
Create balanced dataset for Number Systems feature.
Extracts samples with proper field enrichment.
"""

import json
import re
import random
from collections import defaultdict
from pathlib import Path

# Set random seed for reproducibility
random.seed(42)

# Strong's number to Hebrew/Greek word mappings
STRONGS_WORDS = {
    # Hebrew (H) common words
    "H0430": "אֱלֹהִים",  # Elohim/God
    "H3068": "יהוה",      # YHWH/LORD
    "H0120": "אָדָם",     # adam/man
    "H8064": "שָׁמַיִם",   # shamayim/heavens
    "H4325": "מַיִם",     # mayim/water
    "H3027": "יָד",       # yad/hand
    "H5869": "עַיִן",     # ayin/eye
    "H0776": "אֶרֶץ",     # eretz/earth
    "H1121": "בֵּן",      # ben/son
    "H0802": "אִשָּׁה",   # ishshah/woman/wife
    "H0376": "אִישׁ",     # ish/man
    "H0251": "אָח",       # ach/brother
    "H3117": "יוֹם",      # yom/day
    "H5146": "נֹחַ",      # Noah
    "H0085": "אַבְרָהָם", # Abraham
    "H3290": "יַעֲקֹב",   # Jacob
    "H3327": "יִצְחָק",   # Isaac
    "H4428": "מֶלֶךְ",    # melek/king
    "H5775": "עוֹף",      # oph/bird
    "H0929": "בְּהֵמָה",  # behemah/animal
    "H7307": "רוּחַ",     # ruach/spirit
    "H0216": "אוֹר",      # or/light
    "H2822": "חֹשֶׁךְ",   # choshek/darkness
    "H4397": "מַלְאָךְ",  # malak/angel
    "H0559": "אָמַר",     # amar/say
    "H6213": "עָשָׂה",    # asah/make
    "H1254": "בָּרָא",    # bara/create
    "H7225": "רֵאשִׁית",  # reshit/beginning
    "H3876": "לוֹט",      # Lot
    "H8283": "שָׂרָה",    # Sarah
    "H7354": "רָחֵל",     # Rachel
    "H1732": "דָּוִד",    # David
    "H4872": "מֹשֶׁה",    # Moses
    "H5467": "סְדֹם",     # Sodom
    "H8147": "שְׁנַיִם",  # shenayim/two
    "H7969": "שְׁלֹשָׁה", # sheloshah/three
    "H0702": "אַרְבָּעָה", # arbaah/four
    "H2568": "חָמֵשׁ",    # chamesh/five
    "H8337": "שֵׁשׁ",     # shesh/six
    "H7651": "שֶׁבַע",    # sheva/seven
    "H6240": "עָשָׂר",    # asar/ten (suffix)
    # Greek (G) common words
    "G2316": "θεός",      # theos/God
    "G444": "ἄνθρωπος",   # anthropos/man
    "G2424": "Ἰησοῦς",    # Iesous/Jesus
    "G5547": "Χριστός",   # Christos/Christ
    "G2962": "κύριος",    # kyrios/Lord
    "G4151": "πνεῦμα",    # pneuma/spirit
    "G3962": "πατήρ",     # pater/father
    "G5207": "υἱός",      # huios/son
    "G3101": "μαθητής",   # mathetes/disciple
    "G32": "ἄγγελος",     # angelos/angel
    "G1135": "γυνή",      # gyne/woman
    "G435": "ἀνήρ",       # aner/man
    "G80": "ἀδελφός",     # adelphos/brother
    "G2250": "ἡμέρα",     # hemera/day
    "G3056": "λόγος",     # logos/word
    "G4074": "Πέτρος",    # Petros/Peter
    "G2385": "Ἰάκωβος",   # Iakobos/James
    "G2491": "Ἰωάννης",   # Ioannes/John
    "G3972": "Παῦλος",    # Paulos/Paul
    "G2532": "καί",       # kai/and
    "G3588": "ὁ",         # the
}

# Book to literary type mapping
BOOK_TO_TYPE = {
    # Law (Torah/Pentateuch)
    "GEN": "law", "EXO": "law", "LEV": "law", "NUM": "law", "DEU": "law",
    # History (OT)
    "JOS": "history", "JDG": "history", "RUT": "history", "1SA": "history",
    "2SA": "history", "1KI": "history", "2KI": "history", "1CH": "history",
    "2CH": "history", "EZR": "history", "NEH": "history", "EST": "history",
    # Poetry/Wisdom
    "JOB": "poetry", "PSA": "poetry", "PRO": "poetry", "ECC": "poetry", "SNG": "poetry",
    # Major Prophets
    "ISA": "prophecy", "JER": "prophecy", "LAM": "prophecy", "EZK": "prophecy", "DAN": "prophecy",
    # Minor Prophets
    "HOS": "prophecy", "JOL": "prophecy", "AMO": "prophecy", "OBA": "prophecy",
    "JON": "prophecy", "MIC": "prophecy", "NAM": "prophecy", "HAB": "prophecy",
    "ZEP": "prophecy", "HAG": "prophecy", "ZEC": "prophecy", "MAL": "prophecy",
    # Gospels
    "MAT": "gospel", "MRK": "gospel", "LUK": "gospel", "JHN": "gospel",
    # Acts (NT History)
    "ACT": "history",
    # Epistles
    "ROM": "epistle", "1CO": "epistle", "2CO": "epistle", "GAL": "epistle",
    "EPH": "epistle", "PHP": "epistle", "COL": "epistle", "1TH": "epistle",
    "2TH": "epistle", "1TI": "epistle", "2TI": "epistle", "TIT": "epistle",
    "PHM": "epistle", "HEB": "epistle", "JAS": "epistle", "1PE": "epistle",
    "2PE": "epistle", "1JN": "epistle", "2JN": "epistle", "3JN": "epistle", "JUD": "epistle",
    # Apocalyptic
    "REV": "apocalyptic"
}

# OT books
OT_BOOKS = {"GEN", "EXO", "LEV", "NUM", "DEU", "JOS", "JDG", "RUT", "1SA", "2SA",
            "1KI", "2KI", "1CH", "2CH", "EZR", "NEH", "EST", "JOB", "PSA", "PRO",
            "ECC", "SNG", "ISA", "JER", "LAM", "EZK", "DAN", "HOS", "JOL", "AMO",
            "OBA", "JON", "MIC", "NAM", "HAB", "ZEP", "HAG", "ZEC", "MAL"}

# Theologically significant verses (Trinity contexts)
TRINITY_VERSES = {
    "GEN.001.026", "GEN.003.022", "GEN.011.007", "ISA.006.008"
}

# Body part words (natural duals)
BODY_PARTS = {"hand", "hands", "eye", "eyes", "ear", "ears", "foot", "feet",
              "arm", "arms", "leg", "legs", "nostril", "nostrils", "lip", "lips",
              "knee", "knees", "wing", "wings"}

# Lexical dual words in Hebrew
LEXICAL_DUAL_STRONGS = {"H8064", "H4325", "H5869", "H3027"}  # shamayim, mayim, ayin, yad

def extract_strongs_number(strongs_str: str, constituent: str) -> str:
    """Extract the strongs number that matches the constituent."""
    if not strongs_str:
        return ""

    # Look for patterns like H0430-God or G2316-God
    constituent_lower = constituent.lower()

    for code in strongs_str.split():
        if "-" in code:
            parts = code.split("-", 1)
            strongs_num = parts[0]
            word_hint = parts[1].lower() if len(parts) > 1 else ""

            # Check if word hint matches constituent
            if word_hint and (constituent_lower in word_hint or word_hint in constituent_lower):
                return strongs_num

    # Fallback: look for common mappings
    mappings = {
        "god": ["H0430", "G2316"],
        "yahweh": ["H3068"],
        "lord": ["H3068", "G2962"],
        "jesus": ["G2424"],
        "christ": ["G5547"],
        "man": ["H0120", "H0376", "G444", "G435"],
        "woman": ["H0802", "G1135"],
        "son": ["H1121", "G5207"],
        "brother": ["H0251", "G80"],
        "day": ["H3117", "G2250"],
        "water": ["H4325"],
        "heaven": ["H8064"],
        "sky": ["H8064"],
        "earth": ["H0776"],
        "light": ["H0216"],
        "darkness": ["H2822"],
        "angel": ["H4397", "G32"],
        "spirit": ["H7307", "G4151"],
        "king": ["H4428"],
        "father": ["G3962"],
        "disciple": ["G3101"],
    }

    for key, codes in mappings.items():
        if key in constituent_lower:
            for code in codes:
                if code in strongs_str:
                    return code

    return ""

def get_strongs_word(strongs_num: str) -> str:
    """Get Hebrew/Greek word for strongs number."""
    # Normalize the strongs number
    if strongs_num:
        # Remove suffix letters like 'a', 'b', etc.
        clean_num = re.sub(r'[a-z]$', '', strongs_num)
        return STRONGS_WORDS.get(clean_num, "")
    return ""

def classify_reason_group(entry: dict) -> str:
    """Classify the reason for the number value."""
    verse = entry.get("verse", "")
    constituent = entry.get("constituent", "").lower()
    label = entry.get("label", "")
    strongs = entry.get("strongs", "")
    text = entry.get("text", "").lower()

    # Trinity contexts
    if verse in TRINITY_VERSES:
        return "TRINITY"

    # Check for lexical duals (shamayim, mayim)
    for dual_strongs in LEXICAL_DUAL_STRONGS:
        if dual_strongs in strongs:
            if constituent in ["water", "heaven", "sky", "heavens", "waters"]:
                return "LEXICAL_DUAL"

    # Body parts (natural duals)
    for body_part in BODY_PARTS:
        if body_part in constituent or body_part in text:
            if label == "Dual":
                return "BODY_PARTS"

    # Pairs (exactly 2)
    if label == "Dual":
        # Check for pair indicators
        pair_indicators = ["2 ", "two ", "both ", "angel", "son", "brother", "wife"]
        for indicator in pair_indicators:
            if indicator in text:
                return "PAIR"
        return "PAIR"  # Default dual is pair

    # Triplets (exactly 3)
    if label == "Trial":
        # Check for Trinity context
        if "god" in constituent.lower() and verse.startswith("GEN"):
            return "TRINITY"
        # Check for named triplets (Peter, James, John etc.)
        triplet_indicators = ["3 ", "three ", "shem", "ham", "japheth"]
        for indicator in triplet_indicators:
            if indicator in text.lower():
                return "TRIPLET"
        return "TRIPLET"

    # Quadrial (exactly 4)
    if label == "Quadrial":
        return "GROUP"  # Groups of 4

    # Paucal (few)
    if label == "Paucal":
        return "GROUP"

    # Singular classifications
    if label == "Singular":
        # Check if it's a person
        person_indicators = ["god", "yahweh", "lord", "jesus", "christ", "moses",
                           "abraham", "jacob", "isaac", "david", "noah", "peter",
                           "paul", "john", "james", "mary", "sarah", "rachel"]
        for person in person_indicators:
            if person in constituent.lower():
                return "PERSON"

        # Objects
        object_indicators = ["earth", "sky", "light", "darkness", "water", "day",
                           "night", "sun", "moon", "star", "tree", "stone", "tomb",
                           "house", "tent", "city", "land", "ground", "food"]
        for obj in object_indicators:
            if obj in constituent.lower():
                return "OBJECT"

        return "PERSON" if any(c.isupper() for c in constituent) else "OBJECT"

    # Plural classifications
    if label == "Plural":
        # Check for crowds/multitudes
        crowd_indicators = ["crowd", "people", "nation", "multitude", "many"]
        for crowd in crowd_indicators:
            if crowd in text.lower():
                return "CROWD"
        return "GROUP"

    return "OTHER"

def get_difficulty(entry: dict) -> str:
    """Classify difficulty based on context."""
    verse = entry.get("verse", "")
    label = entry.get("label", "")
    constituent = entry.get("constituent", "").lower()

    # Trinity verses are medium difficulty (theological significance)
    if verse in TRINITY_VERSES:
        return "medium"

    # Rare number categories are harder
    if label in ["Paucal", "Quadrial"]:
        return "hard"

    # Trial with clear context is medium
    if label == "Trial":
        return "medium"

    # Dual with body parts is easy
    if label == "Dual":
        for part in BODY_PARTS:
            if part in constituent:
                return "easy"
        return "medium"

    # Common singular/plural are easy
    if label in ["Singular", "Plural"]:
        return "easy"

    return "medium"

def process_entry(entry: dict, split: str) -> dict:
    """Process a single entry to the required output format."""
    verse = entry.get("verse", "")
    book = verse.split(".")[0] if verse else ""

    section = "OT" if book in OT_BOOKS else "NT"
    literary_type = BOOK_TO_TYPE.get(book, "history")

    strongs_number = extract_strongs_number(entry.get("strongs", ""), entry.get("constituent", ""))
    strongs_word = get_strongs_word(strongs_number)

    reason_group = classify_reason_group(entry)
    difficulty = get_difficulty(entry)

    return {
        "verse": verse,
        "label": entry.get("label", ""),
        "constituent": entry.get("constituent", ""),
        "part": entry.get("part", ""),
        "text": entry.get("text", ""),
        "strongs": entry.get("strongs", ""),
        "strongs_number": strongs_number,
        "strongs_word": strongs_word,
        "dataset": {
            "split": split,
            "section": section,
            "literary_type": literary_type,
            "difficulty": difficulty,
            "reason_group": reason_group
        }
    }

def load_entries(filepath: str) -> list:
    """Load all entries from JSONL file."""
    entries = []
    with open(filepath, 'r') as f:
        for line in f:
            try:
                entries.append(json.loads(line.strip()))
            except json.JSONDecodeError:
                continue
    return entries

def stratified_sample(entries: list, n: int, label: str) -> list:
    """Sample entries with stratification by verse to avoid leakage."""
    # Group by verse
    by_verse = defaultdict(list)
    for entry in entries:
        by_verse[entry["verse"]].append(entry)

    # Sample verses, then pick one entry per verse
    verses = list(by_verse.keys())
    random.shuffle(verses)

    sampled = []
    for verse in verses:
        if len(sampled) >= n:
            break
        # Pick one random entry from this verse with matching label
        matching = [e for e in by_verse[verse] if e.get("label") == label]
        if matching:
            sampled.append(random.choice(matching))

    return sampled

def main():
    input_file = Path("/workspace/bible-study-tools/tbta/features/number-systems/analysis/tbta-extract.secret.jsonl")
    output_file = Path("/workspace/bible-study-tools/tbta/features/number-systems/analysis/datasets.jsonl")

    print("Loading entries...")
    all_entries = load_entries(input_file)
    print(f"Loaded {len(all_entries)} entries")

    # Group by label
    by_label = defaultdict(list)
    for entry in all_entries:
        by_label[entry.get("label", "Unknown")].append(entry)

    print("\nDistribution:")
    for label, entries in sorted(by_label.items(), key=lambda x: -len(x[1])):
        print(f"  {label}: {len(entries)}")

    # Target sampling strategy
    # Total ~500 entries: 300 train, 100 validate, 100 test

    sampling_targets = {
        # Rare categories - take all or most
        "Paucal": {"total": 52, "train": 30, "validate": 11, "test": 11},
        "Quadrial": {"total": 185, "train": 100, "validate": 42, "test": 43},
        "Trial": {"total": 100, "train": 60, "validate": 20, "test": 20},
        "Dual": {"total": 80, "train": 48, "validate": 16, "test": 16},
        "Singular": {"total": 100, "train": 60, "validate": 20, "test": 20},
        "Plural": {"total": 100, "train": 60, "validate": 20, "test": 20},
    }

    final_entries = []
    verse_to_split = {}  # Track which split each verse is in

    for label, targets in sampling_targets.items():
        label_entries = by_label.get(label, [])
        if not label_entries:
            print(f"Warning: No entries for {label}")
            continue

        total_target = min(targets["total"], len(label_entries))

        # Filter entries whose verses are already assigned
        available = [e for e in label_entries if e["verse"] not in verse_to_split]

        # Shuffle for random sampling
        random.shuffle(available)

        # Take samples for each split
        train_n = min(targets["train"], len(available))
        train_entries = available[:train_n]

        remaining = [e for e in available[train_n:] if e["verse"] not in verse_to_split]
        validate_n = min(targets["validate"], len(remaining))
        validate_entries = remaining[:validate_n]

        remaining = [e for e in remaining[validate_n:] if e["verse"] not in verse_to_split]
        test_n = min(targets["test"], len(remaining))
        test_entries = remaining[:test_n]

        # Assign splits and track verses
        for entry in train_entries:
            verse_to_split[entry["verse"]] = "train"
            final_entries.append(process_entry(entry, "train"))

        for entry in validate_entries:
            verse_to_split[entry["verse"]] = "validate"
            final_entries.append(process_entry(entry, "validate"))

        for entry in test_entries:
            verse_to_split[entry["verse"]] = "test"
            final_entries.append(process_entry(entry, "test"))

        print(f"\n{label}: train={len(train_entries)}, validate={len(validate_entries)}, test={len(test_entries)}")

    # Write output
    print(f"\nWriting {len(final_entries)} entries to {output_file}")
    with open(output_file, 'w') as f:
        for entry in final_entries:
            f.write(json.dumps(entry) + "\n")

    # Print summary statistics
    print("\n=== Final Dataset Summary ===")
    split_counts = defaultdict(lambda: defaultdict(int))
    reason_counts = defaultdict(int)

    for entry in final_entries:
        split = entry["dataset"]["split"]
        label = entry["label"]
        reason = entry["dataset"]["reason_group"]
        split_counts[split][label] += 1
        reason_counts[reason] += 1

    print("\nBy Split and Label:")
    for split in ["train", "validate", "test"]:
        counts = split_counts[split]
        print(f"  {split}: {dict(counts)}")

    print("\nBy Reason Group:")
    for reason, count in sorted(reason_counts.items(), key=lambda x: -x[1]):
        print(f"  {reason}: {count}")

    print("\nDone!")

if __name__ == "__main__":
    main()
