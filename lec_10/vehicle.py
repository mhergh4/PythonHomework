class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        print(f"{self.name} is moving at a speed of {self.speed}.")
