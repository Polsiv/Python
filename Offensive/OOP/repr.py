class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
        
    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(x={self.x}, y={self.y})'

p = Point(1, 2)

print(p)
