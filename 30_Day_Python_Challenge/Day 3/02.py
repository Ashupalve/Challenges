# Write a program to calculate the factorial of a number using a while loop.

n = int (input("Enter the no. whose factorial you want :"))
i=1
fact=1
while i <(n+1):
    fact = i* fact
    i=i+1
print (f"Factorial of {n} is = {fact}")