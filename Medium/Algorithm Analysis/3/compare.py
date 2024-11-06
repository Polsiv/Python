import matplotlib.pyplot as plt
from time import time
import numpy as np
from branch_and_bound import solve_n_queens_bnb
from n_queens import solve_n_queens

def get_data():
    
    x = np.array([4, 5, 6, 7, 8, 9, 10, 11, 12])
    backtracking, branch_and_bound = [], []

    for i in x: 
        
        #backtracking
        start_normal = time()
        solve_n_queens(i)
        end_normal = time()
        backtracking.append(end_normal - start_normal)
        
        #branch and bound     
        start_divide = time()
        solve_n_queens_bnb(i)
        end_divide = time()
        branch_and_bound.append(end_divide - start_divide)
        
    return x, backtracking, branch_and_bound
        
        
def plot_data(x, backtracking, branch_and_bound):
    
    x, backtracking, branch_and_bound = get_data()
    plt.plot(x, backtracking, label='Backtracking',)
    plt.plot(x, branch_and_bound, label='Branch & Bound')
    plt.xlabel('Queens num')
    plt.ylabel('Time (s)')
    plt.title('Compare Time complexity')
    plt.legend()
    plt.show()


def main():
    x, backtracking, branch_and_bound = get_data()
    plot_data(x, backtracking, branch_and_bound)
    
    
main()