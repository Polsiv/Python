from math import floor
from time import time
import matplotlib.pyplot as plt
from random import randint


def merge(A, p, q, r):

    L = A[p:q + 1] + [float('inf')]  
    R = A[q + 1:r + 1] + [float('inf')] 

    i = 0
    j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, p, r):
    if p < r:
        q = floor((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def generate_random(lowlimit, sup_limit, max_numbers):
    num_list = []
    for _ in range(max_numbers):
        num_list.append(randint(lowlimit, sup_limit))
    return num_list

def save_data():
    x_axis = []
    y_axis = []

    numbers = [10, 100, 1000, 10000]
    for i in numbers:
        x_axis.append(i)
        my_list = generate_random(1, 100, i)
        start = time()
        merge_sort(my_list, 0, len(my_list) - 1)
        end = time()
        total_time = (end - start)
        print(total_time)
        y_axis.append(total_time) 
    
    return x_axis, y_axis

def plot_data(x, y):
    plt.plot(x, y)
    plt.ylabel("time (s)")
    plt.grid(True)
    plt.show()

def main():
    x, y = save_data()

    plot_data(x, y)

main()


