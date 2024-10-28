

class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("All sub classes must implement this method   ") #error if subclass does not implement
    
class Cat(Animal):
    
    def talk(self):
        return f"Meow!"
    
class Dog(Animal):
    
    def talk(self):
        return f"Woof!"
    
    
def force_talk(obj):
    print(f"{obj.name} says {obj.talk()}")
    
    
cat = Cat("Luna")
dog = Dog("Pucky")

print(cat.talk())
print(dog.talk())

force_talk(cat)
force_talk(dog)