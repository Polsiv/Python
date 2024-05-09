from random import randint
import time

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
    return num_list, len(num_list)

def write_sorted_data(filename, list):
    file = open(filename, "w") 
    for i in list:  
        file.write(f'{i} \n')
    file.close()


def shellSort(array, n):

    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2
    return array


def main():
    low_limit, sup_limit, max_numbers = 0, 12, 10000000
    write_data("numbers.txt", generate_random(low_limit, sup_limit, max_numbers))
    num_list, len = read_data("numbers.txt")

    start = time.time()
    sorted_list = shellSort(num_list, len)
    end = time.time()
    write_sorted_data("sortednumbers.txt", sorted_list)

    print((end - start), "s")
    print((end - start) * 1000, "ms." )

main()