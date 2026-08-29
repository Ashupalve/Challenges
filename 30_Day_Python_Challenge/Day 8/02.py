# Q2. Write a function to check if a number is an Armstrong number (e.g., 153 = 1^3 + 5^3 + 3^3).

def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == num
n = int(input("Enter a number: "))
print(is_armstrong(n))