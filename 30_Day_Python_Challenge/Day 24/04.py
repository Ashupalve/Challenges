# Q4. Write a program to implement memoization manually using a decorator (without
# functools.lru_cache) and apply it to a Fibonacci function.

from functools import wraps
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper
@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
print(fib(35))