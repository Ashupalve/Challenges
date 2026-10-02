# Q1. Write a program to build a simple command-line To-Do List manager that supports add,
# remove, and view tasks (in-memory).

class ToDoList:
    def __init__(self):
        self.tasks = []
    def add(self, task):
        self.tasks.append(task)
        print(f"Added: {task}")
    def remove(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Removed: {task}")
        else:
            print(f"Task not found: {task}")
    def view(self):
        if not self.tasks:
            print("No tasks pending")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
todo = ToDoList()
todo.add("Learn Python")
todo.add("Solve 4 questions")
todo.view()
todo.remove("Learn Python")
todo.view()