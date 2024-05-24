from random import randint

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


low_limit, sup_limit, max_numbers = 0, 12, 1000
write_data("numbers.txt", generate_random(low_limit, sup_limit, max_numbers))