# Q3. Write a program to implement Bubble Sort on a list of numbers

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
print(bubble_sort([5, 2, 9, 1, 5, 6]))