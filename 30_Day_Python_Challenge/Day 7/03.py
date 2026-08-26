#  Write a program to find the second largest number in a list

nums = [12, 45, 2, 89, 33, 7]
unique = list(set(nums))
unique.sort()
print("Second Largest:", unique[-2])