class Pizza:
    def __init__(self, size, crust, toppings):
        self.size = size
        self.crust = crust
        self.toppings = toppings

    def set_size(self, size):
        self.size = size
        return self

    def set_crust(self, crust):
        self.crust = crust
        return self

    def set_toppings(self, topping):
        self.toppings.append(topping)
        return self


    def __str__(self):
        return f"size: {self.size}, crust: {self.crust}, toppings: {self.toppings}"



p1 = Pizza(30, "thin", ["cheess"])
print(p1)
p1.set_size(23).set_crust("stuffed").set_toppings("pepperoni")
print(p1)