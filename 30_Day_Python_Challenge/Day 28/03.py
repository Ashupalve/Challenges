# Q3. Write a program to implement a simple Markov chain text generator trained on a short piece of text.

import random
def build_markov_chain(text):
    words = text.split()
    chain = {}
    for i in range(len(words) - 1):
        chain.setdefault(words[i], []).append(words[i + 1])
    return chain
def generate_text(chain, start_word, length=10):
    word = start_word
    result = [word]
    for _ in range(length - 1):
        next_words = chain.get(word)
        if not next_words:
            break
        word = random.choice(next_words)
        result.append(word)
    return " ".join(result)
text = "the cat sat on the mat the cat ran away the dog chased the cat"
chain = build_markov_chain(text)
random.seed(1)
print(generate_text(chain, "the", 8))