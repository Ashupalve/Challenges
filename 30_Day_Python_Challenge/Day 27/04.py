# Q4. Write a program to implement the Singleton design pattern in Python using a metaclass or a

# class method
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    def __init__(self, value=None):
        if not hasattr(self, "initialized"):
            self.value = value
            self.initialized = True
a = Singleton("first")
b = Singleton("second")
print(a is b)
print(a.value, b.value)