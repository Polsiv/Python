import time
from math import pi

#superior order function
def mi_decorator(function): # function -> original function
    
  
    def wrapper():
        print("greeting from wrapper before calling the fucntion")
        function() # -> calling "greeting()"
        print("greeting from wrapper after calling the fucntion")
        
    return wrapper

@mi_decorator
def greeting():
    print("HI THERE!")
    
greeting()

print (f"\nPerson shit {'=' * 40}\n") #---------------------------------------------------------------------

class Person:
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age
        
    @property 
    def age(self): #getter
        return self._age
    
    
    @age.setter #setter
    def age(self, age):
        if age > 0:
            self._age = age
        else:
            raise ValueError("[!] Age cant be negative")
    
manolo = Person("Manolo", 23)

manolo.age = 14 #setter
print(manolo.age) #getter 


print (f"\nTime {'=' * 40}\n") #---------------------------------------------------------------------

def chronometer(function):
    def wrapper(*args, **kwargs):
        
        start = time.time()
        function(*args, **kwargs)
        end = time.time()
        
        print(f"Total time passed in {function.__name__}: {end - start}")
        
        if args:
            print(args)
            
        if kwargs:
            print(kwargs)
        
    return wrapper

@chronometer
def short_pause(*args, **kwargs):
    time.sleep(1)
    
@chronometer    
def long_pause(*args, **kwargs):
    time.sleep(2)
    
    
long_pause(2, 3, 2, 4, 1, 9, imagine = "dragos", linkin = "park")
short_pause(name = "silva", age = 18, state = "New York")

print (f"\nArgs and kwargs {'=' * 40}\n") #---------------------------------------------------------------------


def add(*args):
    return sum(args)
    
print(add(1, 3, 4, 1, 3893, 3783, 21823, 18224, 2))


def presentation(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}: {j}") 
    
    
presentation(name = "silv", age = 28, state = "Huston") # <- dict

print (f"\nCircumference {'=' * 40}\n") #---------------------------------------------------------------------


class Circumference:
    def __init__(self, radious) -> None:
        self._radious = radious
    
    @property #getter
    def radious(self):
        return self._radious
    
    @property #getter
    def diameter(self):
        return self._radious * 2
    
    @property #getter
    def area(self):
        return (self._radious ** 2) * pi
    
    @radious.setter #setter
    def radious(self, radious):
        self._radious = radious
    
    
c = Circumference(5)

print(c.radious)
print(c.diameter)
print(round(c.area))

c2 = Circumference(32)
c2.radious = 12
print(c2.radious)
print(c2.area)
print(c2.diameter)