# Q2. Write a program to implement a Python iterator class (with __iter__ and __next__) that
# generates the first N even numbers.

class EvenNumbers:
    def __init__(self, n):
        self.n = n
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        value = self.count * 2
        self.count += 1
        return value
for num in EvenNumbers(5):
    print(num, end=" ")