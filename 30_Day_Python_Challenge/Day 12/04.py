# Q4. Write a program demonstrating method overriding and polymorphism using a list of `Shape` objects.

class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
shapes = [Circle(5), Square(4)]
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")