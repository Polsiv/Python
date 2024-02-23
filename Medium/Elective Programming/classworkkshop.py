import math
from functools import reduce
#map//
#filter//
#reduce//
#nested function//
#generador//
#lambda//
#clausura//


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
    n = 100
    seq = list(collatz_conjeture(n))
    print(seq)

example_collatz()