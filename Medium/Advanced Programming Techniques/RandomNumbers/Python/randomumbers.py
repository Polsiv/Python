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
    return num_list, max(num_list)

def write_sorted_data(filename, list):
    file = open(filename, "w") 
    for i in list:  
        file.write(f'{i} \n')
    file.close()

def count_sort(odd_list, maxi):
    list_count = [0] * (maxi + 1)
    list_sorted = [None] * len(odd_list)
    
    for i in odd_list:
        list_count[i] += 1
        
    total = 0
    for i in range(len(list_count)):
        list_count[i], total = total, total + list_count[i]
    
    for index in odd_list:
        list_sorted[list_count[index]] = index
        list_count[index] +=1
    return list_sorted

def main():
    #low_limit, sup_limit, max_numbers = 0, 256, 1048576
    #write_data("numbers.txt", generate_random(low_limit, sup_limit, max_numbers))
    num_list, maxi = read_data("numbers.txt")
    sorted_list = count_sort(num_list, maxi)

    write_sorted_data("sortednumbers.txt", sorted_list)
   
main()