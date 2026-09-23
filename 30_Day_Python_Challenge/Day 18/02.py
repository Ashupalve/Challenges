# Q2. Write a program to find all permutations of a given string using recursion (without itertools).

def permutations(s):
    if len(s) <= 1:
        return [s]
    result = []
    for i, ch in enumerate(s):
        remaining = s[:i] + s[i+1:]
        for p in permutations(remaining):
            result.append(ch + p)
    return result
print(permutations("abc"))