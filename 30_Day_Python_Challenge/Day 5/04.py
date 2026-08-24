# Write a program to find the LCM (Least Common Multiple) of two numbers.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
x = int(input("x: "))
y = int(input("y: "))
lcm = x * y // gcd(x, y)
print("LCM:", lcm)