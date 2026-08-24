#  Write a program to print a pyramid pattern of numbers using nested loops for N rows

n = int (input("Enter how many no of rows you want "))
for i in range(1, n + 1):
    print(" " * (n - i) ,end="")
    print(" ".join(str(j) for j in range(1, i + 1)))