from functools import reduce

n = [1, 2, 4, 5, 6]

#map recieves a function and an iterable object
square = list(map(lambda x: x ** 2, n))

#filter also recieves a function and an iterable object and based on the lambda returned value (true/false) returns the number
odd = list(filter(lambda x: x % 2 == 0, n))
print(odd)


#mult

#weird behavior but understandable, same parameters as before
mul = reduce(lambda x, y: x * y, n)
print(mul)