from math import pi
class Shape:    
    def area(self):
        raise NotImplementedError("Implemet!")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return self.height * self.width

class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def area(self):
        return self.height * self.width / 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


r1 = Rectangle(2, 4)
print(r1.area())
r2 = Triangle(2, 4)
print(r2.area())
c1 = Circle(1)
print(c1.area())