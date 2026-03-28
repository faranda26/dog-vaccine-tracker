import json
import os

FILEPATH = "data.json"

def load():
    if not os.path.exists(FILEPATH):
        return {"users": [], "dogs": [], "vaccines": []}

    with open(FILEPATH, "r") as f:
        return json.load(f)

def save(data):
    with open(FILEPATH, "w") as f:
        json.dump(data, f, indent=2)
