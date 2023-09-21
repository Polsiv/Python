from stack import *
import random
import sys


month_temp = MyStack()
temperatures = []

try:
    days = 1
    while days != 0:
        days = int(input("Enter the amount of days of the month:"))
        if days >= 28 and days <=31: 
            for i in range(days):
                x = round(random.uniform(-40, 40), 2)
                temperatures.append(x)
                stacking(month_temp, x)
                days = 0
        else:
            print("There are not months such amount of days is equal to the amount of given days.")

except Exception as e: 
    print(f"An error occurred!: {e}")
    sys.exit(0)
    
try:
    option = 1
    while option != 5:
        option = int(input(f'{"-" * 10}Choose the option you want!{"-" * 10}\n1)Find The range, max and min temp.\n2)Find the average.\n3)Find the values above and below average.\n4)Print all temperatures (ascending order).\n5)Exit the program.\n{"-" * 25}\n'))

        if option == 1: find_range(month_temp)
        elif option == 2: print(f'The average is: {round(find_average(month_temp), 2)}°C\n')
        elif option == 3: below_and_above_temperatures(month_temp)
        elif option == 4: print(sorted(temperatures))
        elif option == 5: print("Done.")
        else: 
            print("The given input is not valid.")
            break
except: print("The given input is not valid.")
    


