# A sub class should be able to replace the parent/super class when needed

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

def print_area(rectangle):
    rectangle.set_width(4)
    rectangle.set_height(5)
    print("Area: ", rectangle.area())


def main():
    rectangle = Rectangle(0, 0)
    square = Square(0, 0)
    print_area(rectangle)
    print_area(square)

main()


