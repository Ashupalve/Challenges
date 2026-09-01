# Q4. Write a program to create and raise a custom exception when a number is negative.
class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Number is negative")
    return number

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(e)