def digit(num: int):
    numbers = [int(x) for x in str(num)]
    while sum(numbers) > 9:
        numbers = [int(x) for x in str(sum(numbers))]
    return sum(numbers)
    
print(digit(123123))