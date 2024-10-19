
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        return f"hi from {self.name} and {self.age}"
    
silv = Person("silv", 19)

print(silv)
    
print (f"\nCalc shit {'=' * 40}\n")
     
class Calcultor:
    def __init__(self, num) -> None:
        self.num = num
        
    def add(self, num):
        return self.num + num
    
    def double_add(self, num1, num2):
        return self.add(num1) + self.add(num2)
        

calc = Calcultor(5)
print(calc.add(1))
print(calc.double_add(3, 9))