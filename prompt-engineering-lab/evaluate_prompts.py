import json

with open("prompt_dataset.json") as f:
    prompts = json.load(f)

for entry in prompts:
    print(f"Prompt: {entry['prompt']}")
    print("Model likely to fail? ->", entry['expected_failure'])
