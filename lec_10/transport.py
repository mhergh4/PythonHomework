from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, name, speed, num_wheels):
        super().__init__(name, speed)
        self.num_wheels = num_wheels

    def honk(self):
        print("Beep beep!")

class RaceCar(Car):
    def __init__(self, name, speed, num_wheels, nitro_boost):
        super().__init__(name, speed, num_wheels)
        self.nitro_boost = nitro_boost

    def use_nitro(self):
        print(f"{self.name} is using nitro boost!")

class Plane(Vehicle):
    def __init__(self, name, speed, num_engines):
        super().__init__(name, speed)
        self.num_engines = num_engines

    def fly(self):
        print(f"{self.name} is flying with {self.num_engines} engines.")

class Boat(Vehicle):
    def __init__(self, name, speed, num_propellers):
        super().__init__(name, speed)
        self.num_propellers = num_propellers

    def sail(self):
        print(f"{self.name} is sailing with {self.num_propellers} propellers.")
