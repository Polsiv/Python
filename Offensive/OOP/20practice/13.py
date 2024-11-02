from math import pi

class Circle:
    def __init__(self, radius):
        self.__radius = self.check(radius)

    @staticmethod
    def check(radius):
        if radius >= 0:
            return radius

        else: 
            raise ValueError("Radius not negative ni")

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = self.check(radius)


    @property
    def area(self):    
        return self.__radius ** 2 * pi


    @property
    def circumference(self):
        return 2 * self.__radius * pi


c1 = Circle(3)

print(c1.area)
print(c1.circumference)
print(c1.radius)
c1.radius = 1        
print(c1.area)
print(c1.circumference)
print(c1.radius)
        