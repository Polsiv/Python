import math
import random
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    d = random.random()
    #return 2 * math.exp(-0.25 * x) + 0.0024 * d
    return 2 * math.exp(-0.25 * x) 
    
    
xi = [i for i in range(1, 41)]
yi = [f(j) for j in xi]
n = len(xi)

# linear
y_gorro = [math.log(y) for y in yi]
a_1 = (n * sum(xi[z] * y_gorro[z] for z in range(n)) - sum(xi) * sum(y_gorro)) / (n * sum(xi ** 2 for xi in xi) - (sum(xi)) ** 2)
a_0 =  np.mean(y_gorro) - a_1 * np.mean(xi)

A = np.exp(a_0)
print(A)

fig, ax = plt.subplots()
ax.plot(xi, yi, 'o')
ax.plot(xi, y_gorro, 'o')
plt.grid()
plt.show()

