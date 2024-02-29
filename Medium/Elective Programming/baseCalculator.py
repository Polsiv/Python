import math

def base_to_base():
    return 0

def decimal_to_base(number, base):
    above_decimal, coc, result ="ABCDEF", 1, ""
    float_part = float("{:.2f}".format(number % 1))
    int_part = int(number // 1)

   #converting the int_part
    while coc != 0:
        coc = int_part // base
        reminder = int_part % base
        if reminder > 9:
            reminder = above_decimal[reminder - 10]
        result += str(reminder)
        int_part = coc
        
    #converting the float_part
    float_part_complete = ""
    for _ in range(4):
        target = float_part * base
        float_part_complete += str(int(target))
        float_part = target - int(target)
    
    return result[::-1] + "." + float_part_complete

def base_to_decimal(number, base):
    above_decimal = {"A": 10, "B":  11, "C": 12, "D": 13, "E": 14, "F": 15}
    
    for i in range (len(number)):
        if number[i] in above_decimal.keys(): number = number.replace(str(number[i]), str(above_decimal[number[i]]))
    
    
    int_part, float_part = number.split(".")

    return 0



def main():

    option = int(input(f'==Welcome to the number base calculator, enter the option you desire!== \n 1) From base N to base M. \n 2) From base Decimal to N. \n 3) From base N to Decimal. \n {"="*30} \n Enter your option:'))
    if option == 1:
        print("xd")

    if option == 2:
        number = float(input("Enter the decimal number to covert: "))
        base = int(input("Enter the target base: "))
        print(f'Your number {number} is written as: {decimal_to_base(number, base)} in {base} base.')
    if option == 3: 
        base = int(input("Enter the base: "))
        number = (input("Enter the number to covert to decimal: "))
        base_to_decimal(number, base)
        # print(f'Your number {number} is written as: {base(number, base)} in decimal.')


main()