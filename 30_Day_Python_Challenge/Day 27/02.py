# Q2. Write a program to implement a simple state machine for a traffic light system using a class,
# cycling through Red -> Green -> Yellow.

class TrafficLight:
    def __init__(self):
        self.states = ["Red", "Green", "Yellow"]
        self.current = 0
    def next_state(self):
        self.current = (self.current + 1) % len(self.states)
        return self.states[self.current]
light = TrafficLight()
print(self_state := light.states[light.current])
for _ in range(3):
    print(light.next_state())