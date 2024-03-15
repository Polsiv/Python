import math
from functools import reduce


def basics():
    space_odyssey = 2001
    print(space_odyssey)
    print(type("Good night & Good luck"))
    print(type(True))
    result = 10 * 3.0
    print(result)

    x = int(input("enter the number 7, is no gay"))
    y= int(input("enter the number 7, is no gay"))

    print(x + y)
    print(x - y)
    print(x * y)
    try:
        x / y
    except:
        print("DIVISIOJ POR 0 MI BRO")

    print(x/y)    

def more_wrapper():

    #map
    mylist = range(1, 10)
    def area_circle(x):
        return math.pi * (x**2)
    map_gen = map(area_circle, mylist)
    print(list(map_gen))

    #filter
    filter_gen =  filter(lambda x: x % 2 == 0, mylist)
    print(list(filter_gen))

    #reduce
    reduce_gen = reduce(lambda x, y: (x / y), mylist)
    print(reduce_gen)


    #nested function
    def find_area(n):
        def find_area(m):
            return (m * n)/2
        return find_area

    preview = find_area(3)
    print(preview(4))

    #generator
    def collatz_conjeture(n):

        while True: 
            if n % 2 == 0:
                n //= 2
            else: n = 3 * n + 1
            yield n
            if n == 1: 
                break

    def example_collatz():
        n = 51
        seq = list(collatz_conjeture(n))
        print(seq)

    example_collatz()

def wrapper ():
    print(hex(4564789))
    print("XD", "XD2", sep='°°')

    the_string = "EIJI T IEJIGJER KEJIE JFIO ERI FIFDOF DNJGODN BODG NBODG"
    print(the_string.startswith("EIJI"))
    print(the_string.index("t"))
    print(the_string.find("EIJI"))

    print((3 *
        2 *
        4 *
        5))


def matching():
    x = 10
    match x:
        case 1: print("bruh")
        case 10: print("bruh2")
    
    my_tuple = 'bru', 'bru2s', 'bru3'
    print(my_tuple)

def operations_set() -> None:
    a = {1, 2, 3, 4}
    b = {4, 5, 6, 7}
    #intersection
    print(a & b) 
    print(a.intersection(b))
    #union
    print(a | b)
    print(a.union(b))
    #difference
    print(a - b)
    print(a.difference(b))
    #symmetric difference
    print(a ^ b)
    print(a.symmetric_difference(b))

def posicional_dominal_arguments():
    def myFunc(a, b, c, *, d, e, f):
        return a * b
    
    return myFunc

class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores) -> None:
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.numcores = num_cores
        self.apps = []
        self.status = False

    def power_on(self):
        self.status = True
        print(self.status)

    def power_off(self):
        if not self.status: print("phone already turned off")
        else:
            self.status = False
            print("turning off")
    
    def install_app(self, app):
        self.apps.append(app)

    def uninstall_app(self, app):
        self.apps.remove(app)

phone1 = MobilePhone("samsung", "idk", 9)

phone1.power_on()
