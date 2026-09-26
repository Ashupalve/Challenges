# Q3. Write a program to implement a Min-Heap using the `heapq` module and demonstrate
# push/pop operations.

import heapq
heap = []
for num in [5, 1, 8, 3, 9, 2]:
    heapq.heappush(heap, num)
sorted_output = []
while heap:
    sorted_output.append(heapq.heappop(heap))
print(sorted_output)