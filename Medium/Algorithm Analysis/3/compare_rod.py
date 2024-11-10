import matplotlib.pyplot as plt
from time import time
from random import randint
from cut_rod import cut_rod
from memorized_cut_rod import memo_cut_rod
from bottom_up import bottom_up_cut_rod

def get_data():
    
    old = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    min_value = max(old) + 1
    new = sorted(randint(min_value, min_value + 100) for _ in range(90))
    price_list = sorted(old + new)
    recursive, memorized, bottom_up = [], [], []
    n = range(4, 100, 4)

    for i in n: 
        
        #recursive cut rod
        start_normal = time()
        cut_rod(price_list, i)
        end_normal = time()
        recursive.append(end_normal - start_normal)
        
        #memorized  
        start_divide = time()
        memo_cut_rod(price_list, i)
        end_divide = time()
        memorized.append(end_divide - start_divide)
        
        #bottom up  
        start_divide = time()
        bottom_up_cut_rod(price_list, i)
        end_divide = time()
        bottom_up.append(end_divide - start_divide)
        
        
    return n, recursive, memorized, bottom_up
        
        
def plot_data(n, recursive, memorized, bottom_up):
    plt.plot(n, recursive, label = 'Recursive')
    plt.plot(n, memorized, label = 'Memorized')
    plt.plot(n, bottom_up, label = 'Bottom_up')
    plt.xlabel('Rod length')
    plt.ylabel('Time (s)')
    plt.title('Compare Time complexity')
    plt.legend()
    plt.show()


def main():

    n, recursive, memorized, bottom_up = get_data()
    plot_data(n, recursive, memorized, bottom_up)
    
main()