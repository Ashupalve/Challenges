#  Write a program to check whether two strings are anagrams of each other.

s1 = input("String 1: ").replace(" ", "").lower()
s2 = input("String 2: ").replace(" ", "").lower()
if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")