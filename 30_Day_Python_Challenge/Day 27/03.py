# Q3. Write a program to implement the Observer design pattern: a `Publisher` class that notifies
# multiple `Subscriber` objects when an event occurs.

class Publisher:
    def __init__(self):
        self.subscribers = []
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
    def notify(self, message):
        for sub in self.subscribers:
            sub.update(message)
class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        print(f"{self.name} received: {message}")
pub = Publisher()
pub.subscribe(Subscriber("Alice"))
pub.subscribe(Subscriber("Bob"))
pub.notify("New event occurred!")