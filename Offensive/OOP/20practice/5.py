class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        raise NotImplementedError("All sub classes must implement this method")


class Dog(Animal):
    def make_sound(self):
        return f"{self.name} barks!"

class Cat(Animal):
    def make_sound(self):
        return f"{self.name} hisses!"

class Bird(Animal):
    def make_sound(self):
        return f"{self.name} chirps!"


    
dog = Dog("Pucky")
print(dog.make_sound())

cat = Cat("Luna")
print(cat.make_sound())

bird = Bird("Paco")
print(bird.make_sound())
    


