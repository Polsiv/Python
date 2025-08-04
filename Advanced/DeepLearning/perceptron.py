import numpy as np
from functions import step

# data for AND
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 0, 0, 1])

# weights and bias (initialization)
weights = np.zeros(2)
bias = 0.0
learning_rate = 0.1


# train
for epoch in range(10):
    print(f"Epoch: {epoch}")

    for i in range(len(X)):
        x_i = X[i]
        y_true = y[i]

        # weighted sum
        z = np.dot(weights, x_i) + bias
        y_pred = step(z)

        # update weights if wrong
        error = y_true - y_pred
        weights += learning_rate * error * x_i
        bias += learning_rate *error

        print(f"  Input: {x_i}, Prediction: {y_pred}, True: {y_true}, Weights: {weights}, Bias: {bias}")



print("\nFinal weights:", weights)
print("Final bias:", bias)

def predict(x):
    return step(np.dot(weights, x) + bias)

print("\nTesting:")
print("predict([1, 1]) =", predict([1, 1]))  # should be 1
print("predict([0, 1]) =", predict([0, 1]))  # should be 0
