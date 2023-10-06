import math

def newmethod(funct, derivative, x, n):
    def f(x):
        f = eval(funct)
        return f
    
    def derivativef(x   ):
        df = eval(derivative)
        return df
    
    for i in range(1, n):
        i = x -(f(x)/derivativef(x))
        x = i

    print(f'the root was found to be at {x} after {n} iterations')

newmethod("2**x + x**2 - 1", "(2**x)*(math.log(2, math.e)) + 2*x", -0.6, 20)