#  Write a program to implement a function that returns the sum of all elements in a list using recursion.

def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])
print(recursive_sum([1, 2, 3, 4, 5]))