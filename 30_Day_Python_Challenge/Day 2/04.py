# Write a program that takes marks as input and prints the grade (A/B/C/D/F) based on given ranges.
n =  int (input("Enter no. of subjesct you have"))
for i in range (1,n+1):
    marks= int(input (f"Enter Marks of {i} sub :"))
    i = i+1
    if marks >=80:
        print(f"Grade of Sub {i} is A+")
    elif (marks >=70 and marks <80):
        print(f"Grade of Sub {i} is A")
    elif (marks >=50 and marks<70):
        print(f"marks of Sub {i} is B")
    elif (marks >=40 and marks<50):
        print(f"marks of Sub {i} is C")        
    elif (marks >=35 and marks<40):
        print(f"marks of Sub {i} is P")
    else:
        print (f"You are fail in {i} th sub ")

    