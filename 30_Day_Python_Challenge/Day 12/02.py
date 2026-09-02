# Q2. Write a program to demonstrate class inheritance: create a base class `Animal` and a derived class `Dog`.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        name = input("Enter the dog's name: ")

    def speak(self):
        return "Bhoo Bhoo!"
d1 = Dog("Raju")
print(f"{d1.name} says: {d1.speak()}")