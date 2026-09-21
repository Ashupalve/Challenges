# Q3. Write a program to demonstrate abstract base classes using the `abc` module with an abstract
# method `area`.

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
r = Rectangle(4, 5)
print("Area:", r.area())