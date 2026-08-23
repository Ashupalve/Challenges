#  Write a program to check whether a number is a palindrome

n = (input("Enter a number :"))

if (n== n[::-1]):
    print(f"Yes {n} is palindrome ")
else :
    print (f"{n} is not palindrome number")
