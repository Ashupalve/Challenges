# Q3. Write a program to implement a simple recommendation engine that suggests items based on
# cosine similarity between user rating vectors.
import math
def cosine_similarity(v1, v2):
    dot = sum(a * b for a, b in zip(v1, v2))
    mag1 = math.sqrt(sum(a * a for a in v1))
    mag2 = math.sqrt(sum(b * b for b in v2))
    return dot / (mag1 * mag2) if mag1 and mag2 else 0
users = {
    "Alice": [5, 3, 0, 1],
    "Bob":   [4, 0, 0, 1],
    "Carol": [1, 1, 0, 5],
}
target = "Alice"
similarities = {
    user: cosine_similarity(users[target], vec)
    for user, vec in users.items() if user != target
}
best_match = max(similarities, key=similarities.get)
print("Most similar to Alice:", best_match)