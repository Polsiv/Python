class Calc:
    def __init__(self, num) -> None:
        self.num = num
            
    def __eq__(self, value: object) -> bool:
        return self.num == value.num
    
    def __mul__(self, value : object): # for multiplication
        return self.num * value.num
    
    def __sub__(self, value : object):
        return self.num - value.num
    
    def __truediv__(self, value: object):
        return self.num / value.num
    
    def __lt__(self, value):
        return self.num < value.num
    
    def __le__(self, value):
        return self.num <= value.num
    
    def __gt__(self, value):
        return self.num > value.num
    
    def __ge__(self, value):
        return self.num >= value.num
    
c1 = Calc(2)
c2 = Calc(3)

print(c1 == c2)
print(c1 * c2)
print(c1 - c2)
print(c1 / c2)
print(c1 < c2)
print(c1 <= c2)
print(c1 > c2)
print(c1 >= c2)