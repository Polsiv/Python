class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, object):
        return self.numerator / self.denominator + object.numerator / object.denominator

    def __sub__(self, object):
        return self.numerator / self.denominator - object.numerator / object.denominator

    def __mul__(self, object):
        return self.numerator / self.denominator * object.numerator / object.denominator

    def __truediv__(self, object):
        return (self.numerator / self.denominator) / (object.numerator / object.denominator)



f1 = Fraction(1, 2)
f2 = Fraction(1, 2)

print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1 / f2)