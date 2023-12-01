import math

class Shape:
        pass

class _2DShape(Shape):
    def area(self):
      pass

class _3DShape(Shape):
    def volume(self):
        pass

class Square(_2DShape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Triangle(_2DShape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Cube(_3DShape):
    def __init__(self, side_length):
        self.side_length = side_length


    def volume(self):
        return self.side_length ** 3

class Cone(_3DShape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height


    def volume(self):
        return (1/3) * math.pi * (self.radius**2) * self.height

if __name__ == "__main__":
    square = Square(5)
    print("Square Area:", square.area())

    triangle = Triangle(4, 3)
    print("Triangle Area:", triangle.area())

    cube = Cube(3)
    print("Cube Volume:", cube.volume())

    cone = Cone(2, 4)
    print("Cone Volume:", cone.volume())
