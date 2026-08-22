# Write a program to print the multiplication table of a given number (1 to 10).

n =  int (input("Enter no. which you want make table :"))
for i in range (1,11):
    print(f"{n} X {i} = {i*n}")