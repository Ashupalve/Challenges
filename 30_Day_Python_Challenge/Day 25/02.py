# Q2. Write a program to simulate a simple ATM machine class with deposit, withdraw, and
# balance-check operations, handling insufficient funds.

class ATM:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
atm = ATM(1000)
atm.deposit(500)
atm.withdraw(2000)
atm.withdraw(800)