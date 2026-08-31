#  Write a program to demonstrate a function using **kwargs that prints all key-value pairs passed to it.

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name="Ashwed", age=21, city="Nashk")