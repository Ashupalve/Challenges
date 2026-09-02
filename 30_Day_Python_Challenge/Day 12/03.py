# Write a program demonstrating encapsulation using private attributes and getter/setter
# methods in a `BankAccount` class

class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
acc = BankAccount(1000)
acc.deposit(500)
print("Balance:", acc.get_balance())