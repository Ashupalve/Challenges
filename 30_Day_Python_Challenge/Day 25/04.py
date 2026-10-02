# Q4. Write a program to simulate a simple quiz game that asks 3 questions, tracks the score, and
# prints the result at the end.

questions = [
    {"q": "Capital of France?", "a": "paris"},
    {"q": "2 + 2 = ?", "a": "4"},
    {"q": "Language of this challenge?", "a": "python"},
]
score = 0
for item in questions:
    answer = input(item["q"] + " ")
    if answer.strip().lower() == item["a"]:
        score += 1
print(f"You scored {score} out of {len(questions)}")