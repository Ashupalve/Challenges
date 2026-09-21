# Q4. Write a program to implement a Python class using `@staticmethod` and `@classmethod`
# decorators, e.g., a `Circle` class.

class Circle:
    pi = 3.14159
    def __init__(self, radius):
        self.radius = radius
    @staticmethod
    def is_valid_radius(radius):
        return radius > 0
    @classmethod
    def unit_circle(cls):
        return cls(1)
c = Circle.unit_circle()
print("Radius:", c.radius)
print("Valid radius check:", Circle.is_valid_radius(-2))