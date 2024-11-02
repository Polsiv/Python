class Customer:
    def __init__(self, purchase, loyalty):
        self.__purchase_amount = purchase
        self.__loyalty =  loyalty / 100

    def discount(self):
        d = self.__purchase_amount * self.__loyalty
        return self.__purchase_amount - d

c1 = Customer(1000, 50)
print(c1.discount())

