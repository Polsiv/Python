harv = []
counterharv = 0
best = 0
worst = 0

for i in range(12):
    x = int(input(f'Enter the harvesting for the {i + 1}° Month: '))
    harv.append(x)
    counterharv += harv[i]
    
avg = counterharv / 12

for i in range(12):
    if avg > harv[i]:
        best += 1
    else:
        worst += 1
        
print(f'The average is: {avg} \n Months above average: {best} \n Months below average: {worst}')

