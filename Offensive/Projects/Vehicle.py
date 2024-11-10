class Vehicle:
    def __init__(self, plate, model):
        self.plate = plate
        self.model = model
        self.available = True
        
    def rent(self):
        if self.available:
            self.available = False
        else:
            print(f"Vehicle with plate: {self.plate} not available!")
            
    def return_vehicle(self):
        self.available = True

    def __str__(self):
        return f"Vehicle(Plate: {self.plate}, Model: {self.model}, Available: {self.available})"

class DealerShip:
    
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def rent_vehicle(self, plate):
        for vehicle in self.vehicles:
            if vehicle.plate == plate:
                vehicle.rent()
                
    def return_vehicle(self, plate):
        for vehicle in self.vehicles:
            if vehicle.plate == plate:
                vehicle.return_vehicle()

    def __str__(self):
        return "\n".join(str(vehicle) for vehicle in self.vehicles)
    
    

def main():
    dealership = DealerShip() 
    dealership.add_vehicle(Vehicle("EGI381", "Toyota Corolla"))
    dealership.add_vehicle(Vehicle("JEG348", "Honda Civic"))
    
    print("Initial:\n")
    print(dealership)
    dealership.rent_vehicle("JEG348")
    
    print("State:\n")
    print(dealership) 
    
    print("State:\n")
    dealership.return_vehicle("JEG348")
    print(dealership) 
    

if __name__ == "__main__":
    main()