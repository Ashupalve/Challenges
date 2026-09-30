# Q1. Write a program to fetch and parse a JSON string, then convert it into a Python dictionary and
# extract specific fields.

import json
json_data = '{"name": "Aarav", "age": 22, "skills": ["Python", "SQL"]}'
data = json.loads(json_data)
print("Name:", data["name"])
print("Skills:", ", ".join(data["skills"]))