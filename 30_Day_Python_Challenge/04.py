# Write a program to find the sum of digits of a given number.

n = input ("enter a number which have minimum 2 digits :")
sum = 0
for i in range (0 , len(n)):
    sum +=int(n[i])
    i += 1
print (f"Sum of digits of given number is = {sum}")