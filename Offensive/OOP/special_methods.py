
from typing import Any


class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        
    
    def __str__(self) -> str:
        return f"title: {self.title}, author: {self.author}"
    
    def __eq__(self, value: object) -> bool:
        return self.author == value.author and self.title == value.title #just an example
    
         
book = Book("adventures", "silv")
book2 = Book("Hacker", "Pepe")
print(book)
print(book2)

print(book == book2)

print (f"\nBank shit {'=' * 40}\n") #---------------------------------------------------------------------


class BankAccount:
    def __init__(self, account_num, owner, initial_balance = 0) -> None:
        self.account_num = account_num
        self.onwer = owner
        self.__balance = initial_balance
        
    def deposit_money(self, money):
        if money > 0:
            
            self.__balance += money
            
            print(f"current balance: {self.__balance}")
        
    def withdraw_money(self, money):
        
        if self.__balance > 0 and self.__balance - money >= 0 and money > 0:
            self.__balance -= money
            print(f"current balance: {self.__balance}")
            
    @property
    def show_money(self):
        return self.__balance
        
manolo = BankAccount("12233", "manolo", 400)

manolo.deposit_money(500)
manolo.withdraw_money(100)


print(manolo.show_money)


print (f"\nFruit shit {'=' * 40}\n") #---------------------------------------------------------------------


class Box:
    def __init__(self, *fruit) -> None: # *, no matter how arguments we pass, it will recieve all of them as a tuple
        self.fruits = fruit
        
    def show_fruits(self):
        for fruit in self.fruits:
            print(fruit)
        print(type(self.fruits))
        
    def __len__(self): #when calling len(object), it goes to this method
        return len(self.fruits)
    
    
box = Box("Aple", "Banana", "Kiwi", "Pear", "Orange")

box.show_fruits()

print(len(box))


print (f"\nPizza shit {'=' * 40}\n") #---------------------------------------------------------------------


class Pizza:
    def __init__(self, size, *ingredients) -> None:
        self.size = size
        self.ingredients = ingredients
        
        
    def description(self):
        
        print(f"Pizza is {self.size} cm long, and its ingredients are: {', '.join(self.ingredients)}")
        
    
    
pizza = Pizza(12, "Pepperoni", "Ham", "Cheese", "Bacon")
pizza.description()


print (f"\n List shit {'=' * 40}\n") #---------------------------------------------------------------------


class MyList:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]
        
    def __getitem__(self, idx):
        return self.data[idx]
        
        
lists = MyList()
print(lists[2])


print (f"\n Greeting shit {'=' * 40}\n") #---------------------------------------------------------------------


class Greeting:
    def __init__(self, greeting) -> None:
        self.greeting = greeting
        
    def __call__(self, name):
        return f"{self.greeting} {name}!"
        
        
hi =  Greeting("¡hi")

print(hi("Luis"))
print(hi("Albert"))


print (f"\n Dot shit {'=' * 40}\n") #---------------------------------------------------------------------


class Dot:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        
        return Dot(self.x + other.x, self.y + other.y) #temp obj
    
    def __str__(self):
        return f"({self.x}, {self.y})"
        
    
p1 = Dot(2, 8)
p2 = Dot(4, 9)


print(p1 + p2) #(6, 17)


print (f"\n Counter shit {'=' * 40}\n") #---------------------------------------------------------------------

class Counter:
    def __init__(self, limit) -> None:
        self.limit = limit
    

    def __iter__(self):
        
        self.counter = 0
        return self
    
    
    def __next__(self):
        
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        
        else:
            raise StopIteration
    
    
c = Counter(15)

for i in c:
    print(i)