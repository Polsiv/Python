from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def area(self):
        return self.radius ** 2 * 3.14159265
    
    
        
def calculate_total_area(shapes: Shape):
    return sum(shape.area() for shape in shapes)


def main():
    shapes = [Rectangle(3, 4), Circle(10)]
    print("total area: ", calculate_total_area(shapes))
    
    
main()