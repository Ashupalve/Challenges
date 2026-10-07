# Q4. Capstone: Build a complete `Student Result Management System` combining file I/O (CSV),
# classes, exception handling, and sorting — read student records, compute grades, and write a
# sorted results file.

import csv
class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.total = m1 + m2 + m3
        self.average = self.total / 3
        self.grade = self._compute_grade()
    def _compute_grade(self):
        if self.average >= 90:
            return "A"
        elif self.average >= 75:
            return "B"
        elif self.average >= 60:
            return "C"
        else:
            return "D"
def load_students(filename):
    students = []
    with open(filename, newline="") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            try:
                name, m1, m2, m3 = row[0], int(row[1]), int(row[2]), int(row[3])
                students.append(Student(name, m1, m2, m3))
            except (ValueError, IndexError):
                print(f"Skipping malformed row: {row}")
    return students
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "m1", "m2", "m3"])
    writer.writerows([["Aarav", 88, 92, 79], ["Riya", 95, 91, 89], ["Kabir", 60, 55, 70]])
students = load_students("students.csv")
students.sort(key=lambda s: s.average, reverse=True)
with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Average", "Grade"])
    for s in students:
        writer.writerow([s.name, round(s.average, 2), s.grade])
        print(f"{s.name}: Avg={s.average:.2f}, Grade={s.grade}")