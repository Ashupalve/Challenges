# Q1. Write a program to implement a decorator that limits how many times a function can be called
# (a simple rate limiter).

from functools import wraps
def limit_calls(max_calls):
    def decorator(func):
        calls = {"count": 0}
        @wraps(func)
        def wrapper(*args, **kwargs):
            if calls["count"] >= max_calls:
                print(f"Call limit of {max_calls} reached for {func.__name__}")
                return None
            calls["count"] += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator
@limit_calls(2)
def greet(name):
    print(f"Hello, {name}!")
greet("Aarav")
greet("Riya")
greet("Kabir")