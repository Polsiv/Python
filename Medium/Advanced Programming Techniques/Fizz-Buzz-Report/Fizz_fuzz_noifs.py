"""
Author: Juan Pablo Silvestre
"""
def read_from_file(filename):
    """
    Reads the input file and returns a list of numbers.
    """
    num_list = []
    try:
        with open(filename, encoding='utf-8') as f:
            for i in f:
                num_list.append(i)
        return num_list
    except FileNotFoundError:
        return None

def casting_to_int(num_list):
    """
    Casts the list of strings to integers.
    """
    int_num_list = []
    for i in num_list:
        int_num_list.append(int(i))
    int_num_list.remove(100)
    return int_num_list

def check_numbers(num):
    """
    returns fizz, buzz, fizzbuzz or the number it self depending on the number.
    """
    competedstring = ""
    competedstring += "Fizz" * int(num % 3 == 0)
    competedstring += "Buzz" * int(num % 5 == 0)
    return competedstring or num

def print_result(numbers):
    """
    prints the number and the evaluation of the number.
    """
    for i in numbers:
        print(i, check_numbers(i))

def main():
    """
    Calls the essential functions.
    """
    num_list = read_from_file("input.txt")
    int_num_list = casting_to_int(num_list)
    print_result(int_num_list)

main()
