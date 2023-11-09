from transport import Car, RaceCar, Plane, Boat

car = Car("Car1", 60, 4)
car.move()
car.honk()

race_car = RaceCar("RaceCar1", 150, 4, True)
race_car.move()
race_car.honk()
race_car.use_nitro()

plane = Plane("Plane1", 500, 2)
plane.move()
plane.fly()

boat = Boat("Boat1", 30, 1)
boat.move()
boat.sail()
