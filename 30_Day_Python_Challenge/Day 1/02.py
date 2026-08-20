# Write a program that takes two numbers as input and prints their sum, difference, product, and quotient.

num1 = int (input ("Enter the first number :"))
num2 =  int (input ("Enter second number : "))

def calculate(num1, num2):

    sum = num1+ num2

    difference = num1 - num2

    product = num1 * num2 

    if num2!= 0 :
        quotiant = num1 / num2

    else:
        print (f" Second number is {num2} therefore divission is not possible")

    print (f"Sum of {num1} and {num2} is {sum} \n Difference of {num1} and {num2} is {difference} \n Product of {num1} and {num2} is {product}\n Quotiant of {num1} and {num2} is {quotiant}")
    print ("Thank you For using this program")

calculate(num1 ,num2)