class Book:

    #class variables
    best_seller_value = 5000

    def __init__(self, title, author, price) -> None:
        self.title = title
        self.author = author
        self.price = price

    @staticmethod # When u dont need to pass the object to perform logic (references the class)
    def is_best_seller(sales: int) -> bool:
        return sales > Book.best_seller_value

b1 = Book("Kill", "Silv", 132.1)

print(Book.is_best_seller(11100))
print(Book.is_best_seller(11))


class Book2:

    IVA = 0.21

    def __init__(self, title, author, price) -> None:
        self.title = title
        self.author = author
        self.price = price

    @staticmethod
    def is_best_seller(sales: int) -> bool:
        return sales > 5000
    

    @staticmethod
    def include_iva(price: float) -> float:
        return price + price * Book2.IVA
    

    # THIS SHIT IS WEIRD
    def include_iva2(price) -> float:
        return price + price * Book2.IVA
    
    @classmethod #Recieves the class as argument
    def include_iva3(cls, price):
        return price + price * cls.IVA


class DigitalBook(Book2):

    IVA = 0.1


b2 = Book2("KillF", "Silv", 132.1)
b2_price = b2.price
print(b2.include_iva(b2_price))
 

print(Book2.include_iva2(b2_price))

print(Book2.include_iva3(b2_price))

digital_b = DigitalBook("KillF2", "Silv2",  132.1)

print(DigitalBook.include_iva3(digital_b.price))