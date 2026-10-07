# Q2. Capstone: Build a simple `Employee Payroll System` that calculates salary with tax deductions
# and bonuses using OOP and inheritance (Manager vs Developer).

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    def calculate_salary(self):
        tax = self.base_salary * 0.10
        return self.base_salary - tax
class Manager(Employee):
    def calculate_salary(self):
        base = super().calculate_salary()
        bonus = self.base_salary * 0.15
        return base + bonus
class Developer(Employee):
    def calculate_salary(self):
        base = super().calculate_salary()
        bonus = self.base_salary * 0.05
        return base + bonus
employees = [Manager("Aarav", 80000), Developer("Riya", 60000)]
for emp in employees:
    print(f"{emp.name} ({emp.__class__.__name__}): {emp.calculate_salary():.2f}")