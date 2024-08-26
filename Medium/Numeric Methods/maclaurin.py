from math import sqrt

def derivative(f, x, n, h=1e-4):
    if n == 0:
      return f(x)
    if n == 1:
      return (f(x + h) - f(x)) / h
  
    f_prime = lambda x: derivative(f, x, n-1, h)
    return (f_prime(x + h) - f_prime(x)) / h

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def maclaruin(times, f, x):

    count = f(0)
    for i in range(1, times):
        n_term = (x**(i) * derivative(f, 0, i)) / factorial(i)
        count += n_term

    return count
        
def f(x):
    return sqrt(x + 1)

x = -1/4

print(4 * maclaruin(4, f, x))