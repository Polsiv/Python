class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, object):
        return Vector(self.x + object.x, self.y + object.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(9, 1)

print(v1)
print(v2)
print(v1 + v2)