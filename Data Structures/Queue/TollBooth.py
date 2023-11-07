from Queue import *
import random
from tabulate import tabulate
import sys

tollbooth1 = Kiwi()
tollbooth2 = Kiwi()
tollbooth3 = Kiwi()
tollbooths = [tollbooth1, tollbooth2, tollbooth3]
fees_tb = { "Tollboth 1": 0, "Tollboth 2": 0, "Tollboth 3": 0}
vehicles_tb1 = {"Car": 0, "Van": 0, "Truck": 0, "Bus": 0}
vehicles_tb2 = {"Car": 0, "Van": 0, "Truck": 0, "Bus": 0}
vehicles_tb3 = {"Car": 0, "Van": 0, "Truck": 0, "Bus": 0}

def creating_vehicles():
    for i in range(30):
        x = random.randint(1, 4)
        chosen_one = random.choice(tollbooths)
        appending(chosen_one, x)

a = 2
while a != 5:
    try:
        a =  int(input(f'\n{"-"*6}Choose whatever option you want!{"-"*6}\n1)Create 30 new random vehicles\n2)Check the queue status of every tollbooth\n3)Find which tollbooth earned the most fees\n4)Find how many vehicles of each type where checked in each toolbooth\nExit\n{"-"*50}\n'))
    except Exception as e:
        print(f"An error occurred!: {e}")
        sys.exit(0)

    if a == 1:
       creating_vehicles()
    
    if a == 2:
        print("Checking vehicles: ")
        if(not empty_kiwi(tollbooth1)):
            vehicle_type(tollbooth1)
            vehicles_tb1[vehicle_type(tollbooth1)] += 1
            fees_tb["Tollboth 1"] += checking(tollbooth1)
            print("Tollbooth 1:", fees_tb["Tollboth 1"] )
        else: print("T1 has no vehicles to check!")

        if(not empty_kiwi(tollbooth2)):
            vehicle_type(tollbooth2)
            vehicles_tb2[vehicle_type(tollbooth2)] += 1 
            fees_tb["Tollboth 2"] += checking(tollbooth2)
            print("Tollbooth 2:", fees_tb["Tollboth 2"])
        else: print("T2 has no vehicles to check!")

        if(not empty_kiwi(tollbooth3)):
            vehicle_type(tollbooth3)
            vehicles_tb3[vehicle_type(tollbooth3)] += 1
            fees_tb["Tollboth 3"] += checking(tollbooth3)
            print("Tollbooth 3:", fees_tb["Tollboth 3"])
        else: print("T3 has no vehicles to check!")

    if a == 3:
       if fees_tb["Tollboth 1"] == 0 and fees_tb["Tollboth 2"] == 0 and fees_tb["Tollboth 3"] == 0: print("None of the tollboths has collected any fees.")
       else:
           print("The Tollboth that collected the most is:", max(fees_tb, key=fees_tb.get), " with a total amount of: ", max(fees_tb.values()))
        
    if a == 4:
        
        if(vehicles_tb1["Bus"] == 0 and vehicles_tb1["Car"] == 0 and vehicles_tb1["Truck"] == 0 and vehicles_tb1["Van"] == 0): print("T1 has no vehicles to check!")
        else:  
            print(f'{"="*6}Tollbooth 1{"="*6}')
            table = []
            for key, value in vehicles_tb1.items():
                table.append([key, value])
            print(tabulate(table, headers=["Vehicle", "Count"], tablefmt="plain"))

        if(vehicles_tb2["Bus"] == 0 and vehicles_tb2["Car"] == 0 and vehicles_tb2["Truck"] == 0 and vehicles_tb2["Van"] == 0): print("T2 has no vehicles to check!")
        else:  
            print(f'{"="*6}Tollbooth 2{"="*6}')
            table1 = []
            for key, value in vehicles_tb2.items():
                table1.append([key, value])
            print(tabulate(table1, headers=["Vehicle", "Count"], tablefmt="plain"))
        
        if(vehicles_tb3["Bus"] == 0 and vehicles_tb3["Car"] == 0 and vehicles_tb3["Truck"] == 0 and vehicles_tb3["Van"] == 0): print("T3 has no vehicles to check!")
        else:  
            print(f'{"="*6}Tollbooth 3{"="*6}')
            table2 = []
            for key, value in vehicles_tb3.items():
                table2.append([key, value])
            print(tabulate(table2, headers=["Vehicle", "Count"], tablefmt="plain"))