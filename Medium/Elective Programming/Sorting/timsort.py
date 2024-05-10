from random import randint
import time
import matplotlib.pyplot as plt

def generate_random(lowlimit, suplimit, max_numbers):
    num_list = []
    for _ in range(max_numbers):
        num_list.append(randint(lowlimit, suplimit))
    return num_list 

def write_data(filename, numbers):
    file = open(filename, "w") 
    for i in numbers:
        file.write(f'{str(i)}\n')
    file.close()

def read_data(filename):
    num_list = []
    with open(filename, encoding = 'utf-8') as f:
        for i in f:
            num_list.append(int(i))
    return num_list

def write_sorted_data(filename, list):
    file = open(filename, "w") 
    for i in list:  
        file.write(f'{i} \n')
    file.close()

MINIMUM= 32
  
def find_minrun(n): 
  
    r = 0
    while n >= MINIMUM: 
        r |= n & 1
        n >>= 1
    return n + r 
  
def insertion_sort(array, left, right): 
    for i in range(left+1,right+1):
        element = array[i]
        j = i-1
        while element<array[j] and j>=left :
            array[j+1] = array[j]
            j -= 1
        array[j+1] = element
    return array
              
def merge(array, l, m, r): 
  
    array_length1= m - l + 1
    array_length2 = r - m 
    left = []
    right = []
    for i in range(0, array_length1): 
        left.append(array[l + i]) 
    for i in range(0, array_length2): 
        right.append(array[m + 1 + i]) 
  
    i=0
    j=0
    k=l
   
    while j < array_length2 and  i < array_length1: 
        if left[i] <= right[j]: 
            array[k] = left[i] 
            i += 1
  
        else: 
            array[k] = right[j] 
            j += 1
  
        k += 1
  
    while i < array_length1: 
        array[k] = left[i] 
        k += 1
        i += 1
  
    while j < array_length2: 
        array[k] = right[j] 
        k += 1
        j += 1
  
def tim_sort(array): 
    n = len(array) 
    minrun = find_minrun(n) 
  
    for start in range(0, n, minrun): 
        end = min(start + minrun - 1, n - 1) 
        insertion_sort(array, start, end) 
   
    size = minrun 
    while size < n: 
  
        for left in range(0, n, 2 * size): 
  
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
            merge(array, left, mid, right) 
  
        size = 2 * size 

    return array


def plot_graph(data):

    x = range(len(data))
    fig, ax = plt.subplots()

    ax.bar(x, data)
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title('Graph of the List')

    plt.show()


def maintim():

    plot_graphs = False

    #low_limit, sup_limit, max_numbers = 0, 12, 1000
    #write_data("numbers.txt", generate_random(low_limit, sup_limit, max_numbers))
    num_list = read_data("numbers.txt")

    start = time.time()
    sorted_list = tim_sort(num_list)
    end = time.time()
    write_sorted_data("sortednumbers.txt", sorted_list)

    if plot_graphs:
        plot_graph(sorted_list)

    return end - start

