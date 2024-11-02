class Computer:
    
    def get_specs(self):
        return f"ram, cpu, motherboard, psu, graphics card, psu"

class Smartphone:

    def get_specs(self):
        return f"ram, cpu, storage"


class SmartComputer(Computer, Smartphone):

    def get_specs(self):
        pc_specs = super(SmartComputer, self).get_specs()
        phone_specs = super(SmartComputer, self).get_specs()
        return f" {phone_specs}, {pc_specs}"


sc1 = SmartComputer()

print(sc1.get_specs())