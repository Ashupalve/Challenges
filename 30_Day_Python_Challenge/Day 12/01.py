# Q1. Write a program to create a class `Student` with attributes name and marks, and a method to display them.

class student:
    def __init__(self ,name ,marks):
        self.name = name 
        self.marks = marks

s1 = student("Ashwed", 85)
print(f"Name {s1.name} , Marks {s1.marks}")
name = input("Enter student name :")
marks = int (input("Enter their marks :"))
s2 = student(name , marks)
print(f"Name {s2.name} , Marks {s2.marks}")