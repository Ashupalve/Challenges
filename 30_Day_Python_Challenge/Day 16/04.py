# Q4. Write a program to demonstrate list, set, and dictionary comprehensions to build derived
# collections from a list of numbers

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [n ** 2 for n in nums if n % 2 == 0]
unique_remainders = {n % 3 for n in nums}
num_to_square = {n: n ** 2 for n in nums if n <= 5}
print("Squares of evens:", squares)
print("Unique remainders mod 3:", unique_remainders)
print("Num to square map:", num_to_square)