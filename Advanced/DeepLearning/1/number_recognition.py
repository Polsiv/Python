import numpy as np
from functions import step

def step(z):
    return 1 if z >= 0 else 0

X = np.array([
            [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 0 ,1, 1, 1, 1, 0, 0, 1, 0, 0, 1]
        ])
   
Y = np. array([

        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 1]
        ])

# weights and bias (init)
n_inputs  = X.shape[1] # 15
n_outputs = Y.shape[1] # 4
weights = np.zeros((n_outputs, n_inputs))
biases = np.zeros(n_outputs)
learning_rate = .1

# loop
for epoch in range(100):
    print(f"Epoch {epoch}")

    # loop through samples
    for i in range(len(X)):
        x_i = X[i]
        y_true = Y[i]

        # 
        for j in range(n_outputs):
            z = np.dot(weights[j], x_i) + biases[j]
            y_pred = step(z)
            error = y_true[j] - y_pred

            weights[j] += learning_rate * error * x_i
            biases[j] += learning_rate * error


# prediction function
def predict(x):
    z = np.dot(weights, x) + biases
    return [step(val) for val in z]

# test the perceptron
print("\nTesting:")
for i in range(len(X)):
    pred = predict(X[i])
    true = Y[i].tolist()
    print(f"Digit {i}: predicted = {pred}, expected = {true}")


# Post-training =======================================================

def add_noise(x, flips=1):
    x_noisy = x.copy()
    zero_indices = np.where(x == 0)[0]
    
    if len(zero_indices) == 0:
        return x_noisy, []  # no 0s to flip

    flip_indices = np.random.choice(zero_indices, size=min(flips, len(zero_indices)), replace=False)
    x_noisy[flip_indices] = 1
    return x_noisy, flip_indices.tolist()


print("\nNoisy Testing (1 random 0 flipped to 1):")
for i in range(len(X)):
    noisy_input, flipped = add_noise(X[i], flips=1)
    pred = predict(noisy_input)
    true = Y[i].tolist()
    print(f"Digit {i}: Predicted = {pred}, Expected = {true}, Flipped positions: {flipped}")

