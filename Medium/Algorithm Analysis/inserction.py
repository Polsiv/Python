from random import randint
from time import time
import matplotlib.pyplot as plt

def inserction(list):
    for i in range(1, len(list)):

        key = list[i]
        j = i - 1

        while j >= 0 and list[j] > key:
            
            list[j + 1] = list[j]
            j = j - 1

        list[j + 1] = key

def generate_random(lowlimit, suplimit, max_numbers):
    num_list = []
    for _ in range(max_numbers):
        num_list.append(randint(lowlimit, suplimit))
    return num_list 


def save_data():
    x_axis = []
    y_axis = []

    numbers = [10, 100, 1000, 10000, 100000]
    for i in numbers:
        x_axis.append(i)
        my_list = generate_random(1, 100, i)
        start = time()
        inserction(my_list)
        end = time()
        total_time = (end - start)
        y_axis.append(total_time) 
    
    return x_axis, y_axis

def plot_data(x, y):
    plt.plot(x, y)
    plt.xlabel("num lenght")
    plt.ylabel("time (ms)")
    plt.grid(True)
    plt.show()


def main():
    x, y = save_data()

    plot_data(x, y)


main()
   
    


