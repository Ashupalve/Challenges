# Q4. Write a program to find the nth Fibonacci number using memoization (dynamic programming).

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
print(fib(30))
