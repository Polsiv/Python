class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name}: ${self.price}, Stock: {self.stock}"


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]

    def update_product(self, product_name, price=None, stock=None):
        for product in self.products:
            if product.name == product_name:
                if price is not None:
                    product.price = price
                if stock is not None:
                    product.stock = stock
                break

    def search_product(self, product_name):
        return next((p for p in self.products if p.name == product_name), None)

    def sort_by_price(self):
        self.products.sort(key=lambda p: p.price)

    def __len__(self):
        return len(self.products)

    def __getitem__(self, index):
        return self.products[index]

    def __str__(self):
        return "\n".join(str(p) for p in self.products)


# Usage
inventory = Inventory()
p1 = Product("laptop", 1500, 10)
p2 = Product("phone", 800, 25)
p3 = Product("tablet", 600, 15)

inventory.add_product(p1)
inventory.add_product(p2)
inventory.add_product(p3)

inventory.update_product("phone", stock = 30)
print(inventory.search_product("laptop"))
inventory.sort_by_price()
print(inventory)
print(f"iventory count: {len(inventory)}")
print("first product:", inventory[0])
