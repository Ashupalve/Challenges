# Write a program to check whether a given year is a leap year or not.

year =  int (input("Enter Year which you want to check it is leap or not :"))

if (year%4==0 and year%100!=0 or year%400==0):
    print (f"{year} is leap year")
else :
    print (f"{year} is not an leap year ")