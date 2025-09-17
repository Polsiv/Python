import numpy as np
import math

def step(x):
    if x < 0:
        return 0
    return 1

def sigmoid(x):
    return 1 / (1 + (1 / math.pow(math.e, x)))

def tahn(x):
    return math.tanh(x)

def relU(x):
    return np.maximum(0, x)

