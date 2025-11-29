import json
import random
import re
from collections import defaultdict

input_file = "bible-study-tools/tbta/features/number-systems/analysis-gemini/draft_datasets.jsonl"
output_file = "bible-study-tools/tbta/features/number-systems/analysis-gemini/datasets.jsonl"

# Theological Patterns
TRINITY_VERSES = {
    "GEN-001-026", "GEN-003-022", "GEN-011-007", "ISA-006-008", "MAT-028-019", "JHN-001-001"
}
CONTEXTUAL_PATTERNS = [
    (r"RUT-001", "Dual"), (r"LUK-024-013", "Dual"), 
    (r"MAT-017-001", "Trial"), (r"DAN-003", "Trial"),
    (r"ACT-013-002", "Dual"), (r"EXO-003", "Dual"), (r"EXO-004", "Dual")
]

def get_strongs_number(constituent, strongs_str):
    if not strongs_str:
        return ""
    
    parts = strongs_str.split(" ")
    best_match = ""
    
    # Try exact match on gloss
    constituent_clean = constituent.lower().strip(".,!?;:\"'")
    
    for part in parts:
        if "-" in part:
            code, gloss = part.split("-", 1)
            gloss_clean = gloss.replace("_", " ").lower()
            if constituent_clean == gloss_clean:
                return code
            if constituent_clean in gloss_clean.split(): # Partial match
                best_match = code
    
    if best_match:
        return best_match
        
    # Fallback: first code
    if parts:
        return parts[0].split("-")[0]
    return ""

def get_reason_group(verse, label, constituent):
    if verse in TRINITY_VERSES:
        return "TRINITY"
    
    for pattern, expected_label in CONTEXTUAL_PATTERNS:
        if verse.startswith(pattern):
            if label == expected_label:
                return "CONTEXTUAL-PRECISION"
            return "CONTEXTUAL-MISMATCH" # Interesting if TBTA differs
            
    if label in ["Dual", "Trial", "Quadrial", "Paucal"]:
        if constituent.lower() in ["us", "we", "they", "them", "you"]:
             return "PRONOUN-NUMBER"
        return "CONTEXTUAL-PRECISION"
        
    if constituent[0].isupper():
        return "PROPER-NAME"
        
    return "GENERAL"

def get_difficulty(reason_group, label):
    if reason_group == "TRINITY":
        return "adversarial"
    if reason_group == "CONTEXTUAL-PRECISION":
        return "hard"
    if label in ["Dual", "Trial", "Quadrial"]:
        return "medium"
    return "easy"

data = []
with open(input_file, 'r') as f:
    for line in f:
        item = json.loads(line)
        data.append(item)

enriched_data = []
counts = defaultdict(int)

# Prioritize interesting cases
priority_labels = ["Dual", "Trial", "Quadrial", "Paucal"]
other_labels = ["Singular", "Plural"]

# Separate buckets
buckets = defaultdict(list)

for item in data:
    # Enrich
    verse = item.get('verse', '')
    # Normalize verse to hyphen format (GEN-001-001) if it uses dots
    if '.' in verse:
        verse = verse.replace('.', '-')
        item['verse'] = verse
        
    label = item.get('label', '')
    constituent = item.get('constituent', '')
    strongs_str = item.get('strongs', '')
    
    item['strongs_number'] = get_strongs_number(constituent, strongs_str)
    item['dataset']['reason_group'] = get_reason_group(verse, label, constituent)
    item['dataset']['difficulty'] = get_difficulty(item['dataset']['reason_group'], label)
    
    # Reconstruction check (simple mock)
    if 'text' not in item:
        item['reconstructed_verse'] = f"... {constituent} ..." # Fallback if extract didn't work right
    else:
        item['reconstructed_verse'] = item['text']
        
    buckets[label].append(item)

# Selection Strategy
final_selection = []

# Take ALL from priority labels
for label in priority_labels:
    final_selection.extend(buckets[label])

# Sample from Singular/Plural (aim for ~200 each)
for label in other_labels:
    items = buckets[label]
    # Prioritize Trinity/Contextual/ProperName even in S/P
    high_pri = [x for x in items if x['dataset']['reason_group'] != "GENERAL"]
    low_pri = [x for x in items if x['dataset']['reason_group'] == "GENERAL"]
    
    selection = high_pri
    remaining_needed = 200 - len(selection)
    
    if remaining_needed > 0 and low_pri:
        if len(low_pri) > remaining_needed:
             selection.extend(random.sample(low_pri, remaining_needed))
        else:
             selection.extend(low_pri)
             
    final_selection.extend(selection)

# Shuffle final
random.shuffle(final_selection)

# Re-assign splits to ensure valid distribution
# 80% Train, 10% Val, 10% Test
total = len(final_selection)
t_end = int(total * 0.8)
v_end = t_end + int(total * 0.1)

for i, item in enumerate(final_selection):
    if i < t_end:
        split = "train"
    elif i < v_end:
        split = "validate"
    else:
        split = "test"
    item['dataset']['split'] = split

# Write output
with open(output_file, 'w') as f:
    for item in final_selection:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

print(f"Enriched dataset written to {output_file}")
print(f"Total items: {len(final_selection)}")

