# Q4. Write a program using a tuple to store student (name, marks) pairs and print the topper

students = [("Ashwed", 88), ("Umesh", 95), ("Shubham", 79)]
topper = max(students, key=lambda s: s[1])
print("Topper:", topper[0], "with", topper[1], "marks")