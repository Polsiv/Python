import math

def decimal_to_base(number, base):
    above_decimal, coc, result ="ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1, ""
    int_part = int(number)
    float_part = number - int(int_part)

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
        if target > 9: float_part_complete += str(above_decimal[int(target) - 10])
        else:float_part_complete += str(int(target))
        float_part = target - int(target)
    return result[::-1] + "." + float_part_complete

def base_to_decimal(number, base):
    above_decimal = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15,
    "G": 16, "H": 17, "I": 18, "J": 19, "K": 20, "L": 21, "M": 22,
    "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27, "S": 28, "T": 29,
    "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35
    }
    float_part = 0
    if "." in number: int_part, float_part = number.split(".") 
    else: int_part  = number
    int_result, float_result = 0, 0
    
    #converting int_part
    for i in range(len(int_part)):
        int_result += above_decimal[int_part[i]] * math.pow(base, len(int_part) - i - 1)

    #converting float_part
    if float_part != 0:
        for i in range(len(float_part)):
            float_result += above_decimal[float_part[i]] * math.pow(base, (-i - 1))

    print(int_result + float_result if float_part else int(int_result))
    return int_result + float_result if float_part else int(int_result)

