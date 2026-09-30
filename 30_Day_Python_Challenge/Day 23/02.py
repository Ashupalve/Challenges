# Q2. Write a program to serialize a Python object (dictionary) into a JSON file and read it back.

import json
data = {"course": "Python Challenge", "days": 30, "completed": False}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
with open("data.json", "r") as f:
    loaded = json.load(f)
print(loaded)