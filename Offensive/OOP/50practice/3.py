class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, balance):
        self.__balance += balance

    def withdraw(self, money):
        if self.__balance <= 0:
            return f"Youre on 0's!"

        if money > self.__balance:
            return f"Cannot withdraw that amount"

        self.__balance -= money
        return f"Succeed!"

    def check_balance(self):
        return f"Current balance: {self.__balance}"

    

b1 = BankAccount(300)

print(b1.check_balance())

    
print(b1.withdraw(100))        
print(b1.check_balance())
print(b1.withdraw(100))
print(b1.check_balance())   
print(b1.withdraw(200))
print(b1.check_balance())       
print(b1.withdraw(100)) 
print(b1.check_balance())


b1.deposit(500)
print(b1.check_balance())

    