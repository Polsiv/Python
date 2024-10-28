print (f"Animal shit {'=' * 40}\n")

class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("All sub classes must implement this method") #error if subclass does not implement
    
class Cat(Animal):
    
    def talk(self):
        return f"Meow!"
    
class Dog(Animal):
    
    def talk(self):
        return f"Woof!"


#Polymorphism
#is when you can treat an object as a generic version of something, 
# but when you access it, the code determines which exact type it 
# is and calls the associated code.

#a method that behaves based on the class passed 
def force_talk(obj):
    print(f"{obj.name} says {obj.talk()}")
    
    
cat = Cat("Luna")
dog = Dog("Pucky")

print(cat.talk())
print(dog.talk())

force_talk(cat)
force_talk(dog)

print (f"\nCar  shit {'=' * 40}\n") #===================================

class Vehicle:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
        
    def describe(self):
        pass
    
    
class Car(Vehicle):
    
    def describe(self):
        return f"Car: {self.brand}, {self.model}"
    
    
class Motorbike(Vehicle):
    
    def describe(self):
        return f"Motorbike: {self.brand}, {self.model}"
    
    
def describe_vehicle(vehicle):
    print(vehicle.describe())

    
car = Car("Toyota", "Corolla")
motorbike = Motorbike("Honda", "CBR")


describe_vehicle(car)
describe_vehicle(motorbike)

print (f"\n Device  shit {'=' * 40}\n")#===================================


class Device:
    def __init__(self, model) -> None:
        self.model = model
        
        
    def scan_vulnerabilities(self):
        raise NotImplementedError("This methos should be used for all subclasses")
    
    
class Pc(Device):
    def scan_vulnerabilities(self):
        return f"[+] Vulnerabilities analysis complete: Software updated required"
    
class Router(Device):
    def scan_vulnerabilities(self):
        return f"[+] Vulnerabilities analysis complete: Multiple open ports, close them!"
    
class Mobile(Device):
    def scan_vulnerabilities(self):
        return f"[+] Vulnerabilities analysis complete: Detected multiple apps including excesive permissions"
    
#Polymorphism shit
def perform_scan(device):
    print(device.scan_vulnerabilities()) 
    
pc = Pc("Dell XPS")
router = Router("Tp-link Archer C50")
mobile = Mobile("Samsung Galaxi A52s")

perform_scan(pc)
perform_scan(router)
perform_scan(mobile)

print (f"\nABC shit {'=' * 40}\n")#===================================

class A:
    def __init__(self, x):
        self.x = x
        print(f"x: {x}")

class B(A):
    def __init__(self, x, y): #Rewriting method 
        self.y = y
        super().__init__(x) # We call the constructor from A using super 
        print(f"y: {y}")
        
        
b = B(2, 10)

print (f"\nGreeting shit {'=' * 40}\n")#===================================

class C: 
    def greet(self):
        return f"Greetings from C"
    
    
class D(C): 
    def greet(self):
        return f"Greetings from D, but also greeting from {super().greet()}"

d = D( )
print(d.greet())


print (f"\nPerson shit {'=' * 40}\n")#===================================

class Person:
    def __init__(self, name, age) -> None:
        self. name = name
        self.age = age
        
        
    def greeting(self):
        return f"Hi from {self.name}, im {self.age}"
        
        
class Employee(Person):
    def __init__(self, name, age, wage) -> None:
        self.wage = wage
        super().__init__(name, age)
        
    def greeting(self):
        return f"{super().greeting()} and my wage is: {self.wage}"
    
    
person = Employee("Bob", 20, 10000)

print(person.greeting())
