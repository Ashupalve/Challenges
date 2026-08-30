# Q1. Write a program to create a dictionary from two lists (one of keys, one of values).

l1 = ["ashu" , "Palve" , "Tembhurwadi"]
l2 = ["Name", "Surname" , "Address"]
dict = {}
for key in l2:
    for value in l1:
        dict[key]= value
    
print(dict)