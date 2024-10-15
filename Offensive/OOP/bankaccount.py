class BankAccount:
    
    #default amount 0 if not indicated
    def __init__(self, id, name, amount = 0) -> None:
        self.id = id
        self.name = name
        self.amount = amount

    def add(self, money):
        self.amount += money
        return f"current amount: {self.amount}"
    
    def subtract(self, money):
    
        if money > self.amount:
            return f"[!] Nope!"
        
        self.amount -= money
        return f"current amount: {self.amount}"

manolito = BankAccount("39481", "Manolito Gonzalez", 10000)


print(manolito.add(300))
print(manolito.subtract(1000000))