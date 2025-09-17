import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def step(z):
    return 1 if z >= 0 else 0

X = np.array([
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1 ,0],
    [1, 1, 1]
])

y = np.array([0, 0, 0, 0, 0, 0, 0, 1])

# initialize weights and bias
weight = np.zeros(3)
bias = 0.0
learning_rate = 0.1


# loop
for epoch in range(10):
    print(f"Epoch {epoch}")
    
    for i in range(len(X)):
        x_i = X[i]
        y_true = y[i]

        # prediction
        z = np.dot(weight, x_i) + bias
        y_pred = step(z)

        #  update rule
        error = y_true - y_pred
        weight += learning_rate * error * x_i
        bias += learning_rate * error

        print(f"Input: {x_i} | Pred: {y_pred} | True: {y_true} | W: {weight} | B: {bias}")

def predict(x):
    return step(np.dot(weight, x) + bias)

print("\nTesting:")
for x in X:
    print(f"Input: {x} → Output: {predict(x)}") 


# graph
def plot_3d_decision_plane(X, y, weights, bias):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X0 = X[y == 0]
    X1 = X[y == 1]

    ax.scatter(X0[:, 0], X0[:, 1], X0[:, 2], color='red', label='Class 0')
    ax.scatter(X1[:, 0], X1[:, 1], X1[:, 2], color='blue', label='Class 1')

    # mesh grid to plot decision plane
    xx, yy = np.meshgrid(np.linspace(0, 1.2, 10), np.linspace(0, 1.2, 10))

    if weights[2] != 0:
        zz = -(weights[0] * xx + weights[1] * yy + bias) / weights[2]
        ax.plot_surface(xx, yy, zz, alpha=0.5, color='green', label='Decision plane')
    else:
        print("Cannot plot decision plane: w3 (z weight) is 0")

    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('x3')
    ax.set_title('3D Perceptron Decision Plane')
    ax.legend()
    plt.show()

plot_3d_decision_plane(X, y, weight, bias)
