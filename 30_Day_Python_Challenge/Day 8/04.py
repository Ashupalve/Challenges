#  Write a function that takes a sentence and returns a dictionary with the count of each word.

def word_count(sentence):
    words = sentence.lower().split()
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts
print(word_count(input("Enter a sentence :")))