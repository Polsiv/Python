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
                num_list.append(int(i))
        return num_list
    except FileNotFoundError:
        return None

def check_numbers(num):
    """
    returns fizz, buzz, fizzbuzz or the number it self depending on the number.
    """
    competedstring = ""
    competedstring += "Fizz" * int(num % 3 == 0)
    competedstring += "Buzz" * int(num % 5 == 0)
    return competedstring or num


