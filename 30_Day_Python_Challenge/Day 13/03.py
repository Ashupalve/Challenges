# Q3. Write a program to check if a given string containing brackets (), {}, [] has balanced
# parentheses, using a stack

def is_balanced(s):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack
print(is_balanced("{[()()]}"))
print(is_balanced("{[(])}"))