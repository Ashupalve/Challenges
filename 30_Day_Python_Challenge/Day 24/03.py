# Q3. Write a program to demonstrate the use of `*args`, `**kwargs`, and unpacking together in a
# single flexible function.

def summarize(title, *items, **details):
    print(f"--- {title} ---")
    print("Items:", ", ".join(items))
    for key, value in details.items():
        print(f"{key}: {value}")
data = ("Python", "SQL", "Git")
info = {"level": "Intermediate", "duration": "30 days"}
summarize("Skills", *data, **info)