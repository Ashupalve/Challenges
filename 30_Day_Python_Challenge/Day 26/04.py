# Q4. Write a program to demonstrate the use of `functools.lru_cache` to optimize a recursive
# Fibonacci function, and compare with a non-cached version.

import time
from functools import lru_cache
@lru_cache(maxsize=None)
def fib_cached(n):
    if n <= 1:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)
def fib_plain(n):
    if n <= 1:
        return n
    return fib_plain(n - 1) + fib_plain(n - 2)
start = time.time()
print("Cached:", fib_cached(30), "time:", time.time() - start)
start = time.time()
print("Plain:", fib_plain(30), "time:", time.time() - start)