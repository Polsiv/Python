#strategy that allows restrict access to some object componentss

# agreement

# self._money <- protected
# self.__money <- private

 
class Example:
    def __init__(self) -> None:
        
        #protected
        self._protected_attribute = "Protected Attribute n u not allowed to c me!"
        
        #private
        self.__private_attribute = "Private Attribute n u not allowed to c me!" #name mangling, adds  _(classname) to the variable
        
        
example = Example()

print(example._protected_attribute)
print(example._Example__private_attribute)
# print(example.__private_attribute) <- not working since it cannot access to the variable



print (f"\nCar shit {'=' * 40}\n")#===================================

class Car:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
        self.__km = 0 #private
        
    def drive(self, km):
        if km > 0:
            self.__km += km
        else:
            print("\n[!] Not negative num!")
            
    def get_km(self):
        return self.__km
        
    
car = Car("Toyota", "Corolla")

car.drive(150)

print(car.get_km())
        
        



