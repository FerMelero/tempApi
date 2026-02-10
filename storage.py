import json
from pathlib import Path

DB_FILE = Path("items.json")

def load_items():
    if not DB_FILE.exists():
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_items(items):
    with open(DB_FILE, "w") as f:
        json.dump(items, f, indent=4)
