# Q1. Write a program to implement a simple `Stack` class using a list, with push, pop, and peek
# methods.

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if self.items else None
    def peek(self):
        return self.items[-1] if self.items else None
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("Peek:", s.peek())
print("Pop:", s.pop())
print("Remaining:", s.items)

