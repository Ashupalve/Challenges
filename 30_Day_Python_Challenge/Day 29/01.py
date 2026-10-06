# Q1. Write a program to implement a simple in-memory Publish-Subscribe event system supporting
# multiple event types and handlers.
class EventBus:
    def __init__(self):
        self.handlers = {}
    def on(self, event_name, handler):
        self.handlers.setdefault(event_name, []).append(handler)
    def emit(self, event_name, *args, **kwargs):
        for handler in self.handlers.get(event_name, []):
            handler(*args, **kwargs)
bus = EventBus()
bus.on("user_signup", lambda name: print(f"Welcome email sent to {name}"))
bus.on("user_signup", lambda name: print(f"Logging signup for {name}"))
bus.emit("user_signup", "Aarav")