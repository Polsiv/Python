class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    
    @property #Makes the function below not a function anymore but rather a property, so u dont need the () when u call it
    def area(self):
        return self.length * self.width

    
    def __str__(self) -> str: #Seems like a default propertie when printing the object
        return  f"[+] Rectanle Properties: width: {self.width}, length: {self.length}, and area: {self.area} "

    def __eq__(self, value: object) -> bool: #Recieves two objets when u compare them (wtf is this logic)
        return self.width == value.width and self.length == value.length
    

    

r1 = Rectangle(10, 200)
r2 = Rectangle(20, 69)

print(r1.area)
print(r1)

print(f"is r1 = r2? -> {r1 == r2}")