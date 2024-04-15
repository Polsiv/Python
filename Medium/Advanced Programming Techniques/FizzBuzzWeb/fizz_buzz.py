def check_numbers(num):
    """
    returns fizz, buzz, fizzbuzz or the number it self depending on the number.
    """
    competedstring = ""
    competedstring += "Fizz" * int(num % 3 == 0)
    competedstring += "Buzz" * int(num % 5 == 0)
    return competedstring or str(num)
