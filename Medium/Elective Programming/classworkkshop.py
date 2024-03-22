import math
from functools import reduce


def basics():
    space_odyssey = 2001
    print(space_odyssey)
    print(type("Good night & Good luck"))
    print(type(True))
    result = 10 * 3.0
    print(result)

    x = int(input("enter the number 7, L"))
    y= int(input("enter the number 10, W"))

    print(x + y)
    print(x - y)
    print(x * y)
    try:
        x / y
    except:
        print("div by 0 bitchahh")

    print(x/y)    

    #Inplicit conversion
    print(7 * True)
    print(25 + False)
    print(99 + True)
    big_number = 156737438
    print(round(big_number, 3))

    print(list("the pip is so good"))
    the_pip = 'LOW' if space_odyssey > 2003 else 'OMG SO HIGH'
    mylittlelist = [1,22, 34, 234, {3, 2}, 0]
    mylittlelist.insert(1, "OMG IM SO COOL")
    mylittlelisttext = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX", "YZ"]
    print("".join(mylittlelist))

def more_wrapper():

    #map - applies a function to a data set
    mylist = range(1, 10)
    def area_circle(x):
        return math.pi * (x**2)
    map_gen = map(area_circle, mylist)
    print(list(map_gen))

    #filter selects elements that satisfies such conditions
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

def comprehension_list():
    values = [1, 2, 3, 4, 5, 6, 7, 8]
    squared_values = [value ** 2 for value in values]
    print(squared_values)
    values2 = "12,13,145,21,123,412,1"
    int_values = [int(v) for v in values.split(",") if v.startwith("4")]
    print(values, int_values)

def wrapper ():
    print(hex(4564789))
    print("bruh", "bruh2", sep='°°')

    print("abc".isalpha())
    print("a-b-c".isalpha())
    print("1".isnumeric())
    print(f'the pip {10}')

    the_string = "EIJI T IEJIGJER KEJIE JFIO ERI FIFDOF DNJGODN BODG NBODG"
    print(the_string.startswith("EIJI"))
    print(the_string.index("t"))
    print(the_string.find("EIJI"))
    print(the_string.count("T") )

    print((3 *
        2 *
        4 *
        5))
    
    vowels = 'aeiou'
    enum_vowels = {}

    for i, vowel in enumerate(vowels, start = 1):
        enum_vowels[vowel] = i

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

#USEFUL SHT ABT FUNCTIONS ============================
    
#we pack the values into a list
def sum (*values):
    result = 0
    for value in values:
        result += value
    print(result)
sum(1, 3, 4, 5, 1, 3, 5)

#we pack the values into a dict
def best_student(**marks):
    max_mark = -1
    for student, mark in marks.items():
        if mark > max_mark:
            max_mark = mark
            student_best = student
    print(student_best)
best_student(yo = 2, yomama = 3, pip = 10)

#nominal arguments a positional arguments
def postional_args(a, b, c, *, sum = True):
    if sum: print( a + b + c)
    else: print(a - b - c)

postional_args(1, 2, 3, sum = False)
postional_args(4, 5, 6)

#functions as parameters
def success():
    print("YOURE SUCCESSFUL")

def doit(f):
    f()
doit(success)

#decorators (functions thtat recieves functions and returns functions)
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

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

class Fraction:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("not 0 bra")
        self.num = num
        self.den = den
        self.simplify()

    def simplify(self):
        common = self.gcd(self.num, self.den)
        self.num //= common
        self.den //= common

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        if other.num == 0:
            raise ValueError("not 0 again bra")
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __str__(self):
        return f"{self.num}/{self.den}"

fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

print("1st", fraction1)
print("2nd", fraction2)
print("sum", fraction1 + fraction2)
print("sub", fraction1 - fraction2)
print("mu1t", fraction1 * fraction2)
print("div", fraction1 / fraction2)



def handling_exceptions():
    def intdiv(a, b):
        try:
            result = a // b
        except TypeError:
            print( "what")
        except ZeroDivisionError:
            print( "not 0" )
        except Exception:
            print("bry")

def zip_function():
    a = ("elpepe", "elpepe2", "elpepe3")
b = ("thepip", "thepip2", "thepip3")

x = zip(a, b)

print(tuple(x))