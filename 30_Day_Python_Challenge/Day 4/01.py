# Write a program to check whether a number is a prime number.

num = int(input("Enter a number: "))
is_prime = num > 1
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
print(num, "is Prime" if is_prime else "is Not Prime")