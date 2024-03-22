import math

class Square:
    def __init__(self, length):
        self.length = length
    
    def perimter(self):
        return self.length * 4
    
    def area(self):
        return self.length ** 2
    
    def diagonals(self):
        return math.sqrt(2) * self.length
    
    def inscribed_circle(self) -> None:
        print(f'the radius of the circumscribed circle is {self.diagonals(self.length) / 2}')

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def diameter(self):
        return self.radius * 2
    
    def circumference(self):
        return self.raidus * 2 * math.pi
    
    def area(self):
        return (self.radius ** 2) * math.pi

class Triangle:
    def __init__(self, base, heigth):
        self.base = base
        self.heigth = heigth

    def area(self):
        return self.base * self.heigth / 2
    
    def perimeter(self):
        return self.base + self.heigth + math.sqrt(math.pow(self.base, 2) + math.pow(self.heigth, 2))

