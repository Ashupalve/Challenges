# Write a program to write a list of dictionaries to a CSV file and then read it back

import csv


with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'name': 'Ashu', 'age': 21, 'city': 'Nashik'})
    writer.writerow({'name': 'Rushi', 'age': 21, 'city': 'Nk'})
    writer.writerow({'name': 'Umesh', 'age': 21, 'city': 'Nk'})
with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)