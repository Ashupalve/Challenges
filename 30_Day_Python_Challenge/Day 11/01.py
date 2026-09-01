#  Write a program to read a text file and count the number of lines, words, and characters in it.

with open('Q1.txt', 'r') as file:
    content = file.read()
    lines = content.splitlines()
    num_lines = len(lines)
    num_words = len(content.split())
    num_characters = len(content)

print(f"Number of lines: {num_lines}")
print(f"Number of word in file are : {num_words}")
print(f"Number of character in file are : {num_characters}")