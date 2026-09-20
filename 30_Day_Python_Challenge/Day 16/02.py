# Q2. Write a program to create a custom decorator that prints the execution time of a function.

import time
from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper
@timer
def compute_sum(n):
    return sum(range(n))
compute_sum(1000000)