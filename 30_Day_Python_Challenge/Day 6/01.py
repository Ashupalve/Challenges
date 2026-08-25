# Write a program to count the number of vowels, consonants, digits, and spaces in a given string.

vowels = 0
consonants = 0
digits = 0
spaces = 0

v = ["a", "e", "i", "o", "u"]

string = input("Enter a string for checking : ")

for i in string.lower():
    if i in v:
        vowels += 1
    elif i.isalpha():
        consonants += 1
    elif i.isdigit():
        digits += 1
    elif i == " ":
        spaces += 1

print("Vowels :", vowels)
print("Consonants :", consonants)
print("Digits :", digits)
print("Spaces :", spaces)