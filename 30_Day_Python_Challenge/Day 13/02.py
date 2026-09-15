# Q2. Write a program to implement a simple `Queue` class using collections.deque, with enqueue
# and dequeue methods.

from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.popleft() if self.items else None
q = Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
print("Dequeue:", q.dequeue())
print("Remaining:", list(q.items))