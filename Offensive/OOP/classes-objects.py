class Person:
    #class variables defined here

    def __init__(self, name, age) -> None: 

        #object variables
        self.name = name
        self.age = age
        

    def greeings(self): #self is the class instance (object)
        return f"hi n {self.name}"


p1 = Person("Silv", 19)

print(p1.greeings())

class Animal:
    def __init__(self, name, type_a, color) -> None:
        self.name = name
        self.type = type_a
        self.color = color
    
    def description(self): #Animal.description(cat)
        return f"{self.name} is a {self.type}, and their color is {self.color}"


cat = Animal("Uni", "Cat", "Black")
dog = Animal("Pucky", "Dog", "Black")


print(cat.description())
print(dog.description())
