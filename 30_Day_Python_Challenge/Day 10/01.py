# Q1. Write a program to define a function with default and variable-length (*args) arguments to calculate the sum of numbers.

# n1  = int((input("Enter 1st no. :")))
# n2  = int(input("Enter 2nd no. :"))
# def sum(n1 , n2):
#     sum=n1+n2
#     print (sum)

# sum(10,20)
# sum(n1,n2)


def add_numbers(*args, start=0):
    return start + sum(args)
print(add_numbers(1, 2, 3))
print(add_numbers(1, 2, 3, start=10))