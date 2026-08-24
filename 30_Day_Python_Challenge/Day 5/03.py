# Write a program to find the GCD (Greatest Common Divisor) of two numbers using the Euclidean algorithm

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
x = int(input("x: "))
y = int(input("y: "))
print("GCD:", gcd(x, y))
