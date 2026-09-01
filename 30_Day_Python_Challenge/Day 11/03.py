# Q3. Write a program to handle exceptions using try-except-else-finally while dividing two numbers.
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    else:
        print("Result:", result)
    finally:
        print("Division operation attempted")

a = int(input("Enter the numerator: "))
b = int(input("Enter the denominator: "))
divide(a, b)
divide(10, 0)