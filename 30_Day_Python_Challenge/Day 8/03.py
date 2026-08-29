# Write a function that takes a list of numbers and returns a new list containing only the prime numbers.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def filter_primes(nums):
    return [n for n in nums if is_prime(n)]
print(filter_primes([10, 11, 12, 13, 14, 15, 17]))
