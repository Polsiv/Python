class Square:
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2

s1 = Square(3)

print(s1.area)

