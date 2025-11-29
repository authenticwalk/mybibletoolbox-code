import json
import sys
from collections import Counter

import yaml

input_file = "bible-study-tools/tbta/features/number-systems/analysis-gemini/tbta-extract.jsonl"
output_file = "bible-study-tools/tbta/features/number-systems/analysis-gemini/distribution.yaml"

counts = Counter()
try:
    with open(input_file, 'r') as f:
        for line in f:
            data = json.loads(line)
            counts[data['label']] += 1

    with open(output_file, 'w') as f:
        yaml.dump(dict(counts), f)

    print(f"Distribution written to {output_file}")
    print(counts)

except FileNotFoundError:
    print(f"File not found: {input_file}")
    sys.exit(1)


