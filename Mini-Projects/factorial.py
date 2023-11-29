file = open('numbers.txt', 'r')
f = file.readlines()

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

numbers = 0

for numbers in f:
    print (f'{str(numbers).strip()}!')
    print(factorial(int(numbers)))

