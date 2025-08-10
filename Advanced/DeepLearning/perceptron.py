import numpy as np
from functions import step
import matplotlib.pyplot as plt

# data for AND
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([
        [0, 0], 
        [0, 1],
        [0, 1],
        [1, 1]])

# weights and bias (initialization)
weights = np.zeros((2, 2))  # shape: (neurons, inputs)
biases = np.zeros(2)
learning_rate = 0.05


# train
for epoch in range(12):
    print(f"Epoch: {epoch}")

    for i in range(len(X)):
        x_i = X[i]
        y_true = y[i]

        # for each neuron
        for j in range(2):
            z = np.dot(weights[j], x_i) + biases[j]
            y_pred = step(z)
            error = y_true[j] - y_pred

            # update weights and bias
            weights[j] += learning_rate * error * x_i
            biases[j] += learning_rate * error

            print(f"  Neuron {j} | Input: {x_i} | Pred: {y_pred} | True: {y_true[j]} | W: {weights[j]} | B: {biases[j]}")

def predict(x):
    z = np.dot(weights, x) + biases
    return [step(val) for val in z]  # [and_output, or_output   ]

for x in X:
    and_out, or_out = predict(x)
    print(f"Input: {x} -> AND: {and_out}, OR: {or_out}")



def plot_decision_boundaries(X, Y, weights, biases, neuron_labels=["Neuron 1", "Neuron 2"]):
    colors = ['red', 'blue']
    x_vals = np.linspace(-0.1, 1.1, 100)

    # Plot data points
    for x, label in zip(X, Y):
        plt.scatter(x[0], x[1], color='black')
        plt.text(x[0]+0.05, x[1], f"{label}", fontsize=10)

    # Plot decision boundaries
    for i in range(len(weights)):
        w = weights[i]
        b = biases[i]
        label = neuron_labels[i] if i < len(neuron_labels) else f"Neuron {i}"
        
        if w[1] != 0:
            y_vals = -(w[0] / w[1]) * x_vals - b / w[1]
            plt.plot(x_vals, y_vals, label=f"{label} boundary", color=colors[i])
        else:
            x_const = -b / w[0]
            plt.axvline(x_const, color=colors[i], linestyle='--', label=f"{label} boundary")

    plt.xlim(-0.2, 1.2)
    plt.ylim(-0.2, 1.2)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Decision Boundaries')
    plt.grid(True)
    plt.legend()
    plt.show()

plot_decision_boundaries(X, y, weights, biases, neuron_labels=["AND", "OR"])
