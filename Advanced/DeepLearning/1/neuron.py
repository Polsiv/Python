import numpy as np
from functions import sigmoid

# inputs
x = np.array([0.5, 0.3, 0.2])

# weights and bias
# the bias is a trainable scalar value that allows the neuron to shift the activation function left or right

w = np.array([0.4, -0.6, 0.1])
b = 0.2

# neuron output
z = np.dot(w, x) + b

# activation function
output = sigmoid(z)
print(output)