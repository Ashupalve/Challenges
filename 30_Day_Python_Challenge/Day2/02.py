# Write a program to find the largest of three numbers using if-elif-else.

n1  = int(input("Enter 1st number :"))
n2 =  int (input("Enter 2nd Number :"))
n3 =  int (input("Enter 3rd Number :"))

if (n1 > n2 and n1>n3):
    print  (f"{n1} is Largest number")
elif(n2 > n1 and n2> n3):
    print(f"{n2} is largest number ")
else:
    print(f"{n3} is largest number")