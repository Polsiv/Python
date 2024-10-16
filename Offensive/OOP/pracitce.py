class Calculator:

    @staticmethod
    def sumy(a, b):
        return a + b
    
    @staticmethod
    def sub(a, b):
        return a - b
    
    @staticmethod
    def mult(a, b):
        return a * b
    
    @staticmethod
    def div(a, b):

        # return a / b if b != 0 else return "message"
        try:
            return a / b
        except ZeroDivisionError:
            return "imagine dividing by 0 lmao"
 

print (f"\nCalculator shit {'=' * 40}\n")

print(Calculator.sumy(1, 2))
print(Calculator.sub(1, 2))
print(Calculator.mult(1, 2))
print(Calculator.div(1, 12))



print (f"\nCar shit {'=' * 40}\n")
class Car:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    @classmethod
    def sports(cls, brand):
        
        return cls(brand, "Sport")


    def __str__(self) -> str: # this is literally the replacement for print(object) which prints the method instead of the object
        return f"brand: {self.brand} and model: {self.model}"
    
    @classmethod
    def sean(cls, brand):
        return cls(brand, "Sean")

sport = Car.sports("ferrari") #Car("ferrari", "sport")
print(sport.model)

sport2 = sport.sports("lmao")
print(sport2) # cals the __Str__ method
print(sport2.brand)

sean1 = Car.sean("Toyota")

print(sean1)