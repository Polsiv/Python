class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year
    
    @property    
    def vehicle_info(self):
        return f"make: {self.make}, model: {self.model}, year: {self.year}"
    
car = Vehicle("make", "Toyota", 2003)
motorbyke = Vehicle("make2", "Honda", 2021)

print(car.vehicle_info)
print(motorbyke.vehicle_info)
