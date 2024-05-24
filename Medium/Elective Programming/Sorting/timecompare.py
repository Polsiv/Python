import matplotlib.pyplot as plt
from counting import maincounting
from shell import mainshell
from timsort import maintim

def plot_times(n):
    algorithms = ['Shell Sort', 'Counting Sort', 'Timsort']
    times = [mainshell(), maincounting(), maintim()]
    
    plt.bar(algorithms, times, color=['blue', 'green', 'red'])
    plt.xlabel('Algorithm')
    plt.ylabel('Time (seconds)')
    plt.title(f'Execution Time of Algorithms for n = {n}')
    plt.show()

plot_times(1000)

