#  Write a program to check whether a given string is a palindrome (e.g., "madam").

string =  input ("Enter a string ")

if (string==string[::-1]):
    print (string , "is palindrom")
else:
    print(f"{string} is not palindrom String")