# Q2. Write a program to implement Binary Search on a sorted list (iteratively)

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
nums = [2, 4, 5, 6, 9, 11, 15]
print(binary_search(nums, 9))