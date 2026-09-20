# Q1. Write a program to create a generator function that yields the squares of numbers up to N.

def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2
for sq in square_generator(5):
    print(sq, end=" ")