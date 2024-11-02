class Computer:
    
    def get_specs(self):
        return f"ram, cpu, motherboard, psu, graphics card, psu"

class Smartphone:

    def get_specs(self):
        return f"ram, cpu, storage"


class SmartComputer(Computer, Smartphone):

    def get_specs(self):
        phone_specs = Computer().get_specs()
        pc_specs = Smartphone().get_specs()
        return f" {phone_specs}, {pc_specs}"


sc1 = SmartComputer()

print(sc1.get_specs())