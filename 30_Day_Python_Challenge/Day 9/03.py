# Q3. Write a program to merge two dictionaries. If a key exists in both, add their values.

d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 5, "c": 10, "d": 40}
merged = d1.copy()
for k, v in d2.items():
    merged[k] = merged.get(k, 0) + v
print(merged)