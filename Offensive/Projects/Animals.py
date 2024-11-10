
class Animal:
    def __init__(self, name, specie):
        self.name = name
        self.specie = specie
        self.fed = False
    
    def feed(self):
        self.fed = True
        
        
    def __str__(self):
        return f"{self.name} ({self.specie}) - {'Fed' if self.fed else 'Not fed'}"
    
    
        
class AnimalShop:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
    
    def feed_animals(self):
        for animal in self.animals:
            animal.feed()

    def sell_animal(self, name):
        for animal in self.animals:
            if name == animal.name:
                self.animals.remove(animal) 
                return
        print(f"\n[!] {name} was not found in the list!")
            
    @property
    def show_animals(self):
        for animal in self.animals:
            print(animal)
        

def main():
    shop = AnimalShop("Rockys Shop")
    cat = Animal("Luna", "Cat")
    dog = Animal("Pucky", "Dog")

    shop.add_animal(cat)
    shop.add_animal(dog)
    
    shop.show_animals
    
    shop.feed_animals()
    shop.show_animals
    
    print("\n[+] Selling animals\n")
    
    shop.sell_animal("Luna")
    shop.show_animals

if __name__ == "__main__":
    main()