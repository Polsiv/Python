import numpy as np
from functions import sigmoid 

# inputs
x = np.array([0.5, 0.3, 0.2])

W = np.array([
    [0.4, -0.6, 0.1],   # neuron 1
    [-0.2, 0.8, 0.5]    # neuron 2
])

# biases for each output neuron
b = np.array([0.2, -0.1])

# linear output z = wx + b
z = np.dot(W, x) + b

output = sigmoid(z)

print(" output each neuron:", output)
