
names = []
weights = []

winner = ""
highest = 0

for _ in range(5):
    x = input("Enter your name: ")
    names.append(x)
    y = float(input("Enter your weight: "))
    weights.append(y)
    
for i in range(5):
    if(weights[i] > highest):
        highest = weights[i]
        winner = names[i]
        
print(f'The winner is {winner}')


