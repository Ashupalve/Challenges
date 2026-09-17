# Q1. Write a program to implement Linear Search on a list and return the index of the target
# element

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
nums = [4, 2, 9, 6, 5]
print(linear_search(nums, 6))