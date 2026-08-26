#  Write a program to remove duplicate elements from a list while preserving order

nums = [1, 2, 2, 3, 4, 4, 5, 1]
seen = set()
result = []
print(f"{nums}  is given list")
for n in nums:
    if n not in seen:
        seen.add(n)
        result.append(n)
print(result)