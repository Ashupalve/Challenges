# Write a program using a lambda function to sort a list of tuples by the second element.


pairs = [(1, 3), (4, 1), (2, 2)]
pairs.sort(key=lambda x: x[1])
print(pairs)