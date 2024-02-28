def base_to_base():
    return 0

def decimal_to_base(number, base):
    return 0

def base_to_decimal():
    return 0

option = input(f'==Welcome to the number base calculator, enter the option you desire!== \n 1) From base N to base M. \n 2) From base Decimal to N. \n 3) From base N to Decimal. \n {"="*30} \n Enter your option:')


if option == 1:base_to_base()
if option == 2:
    number = input("Enter the decimal number to covert: ")
    base = int(input("Enter the target base: "))
    decimal_to_base(number, base)
if option == 3: base_to_decimal()