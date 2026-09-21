# Q2. Write a program to demonstrate operator overloading by creating a `Vector` class that
# supports the + operator.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
v1 = Vector(2, 3)
v2 = Vector(4, 1)
print(v1 + v2)