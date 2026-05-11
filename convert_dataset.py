import json
from collections import defaultdict

with open("chatbot_dataset/aaple_sarkar_chatbot_dataset_final.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

converted = defaultdict(lambda: {"queries": [], "responses": []})

for entry in raw_data:
    intent = entry["Intent"]
    converted[intent]["queries"].append({
        "text": entry["User Query"],
        "lang": "en" if entry["Language"].lower().startswith("en") else "mr"
    })
    converted[intent]["responses"].append({
        "text": entry["Response"],
        "lang": "en" if entry["Language"].lower().startswith("en") else "mr"
    })

with open("chatbot_dataset/converted_dataset2.json", "w", encoding="utf-8") as f:
    json.dump(converted, f, indent=2, ensure_ascii=False)
