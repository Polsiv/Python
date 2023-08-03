def rabbits (n):
    population = [1, 1]
    for i in range(2, n):
        population.append(population[i - 1] + population[i -2])
    return population
    
x = int(input("Enter the x month you want to know: "))
result = rabbits(x)
print(result[-1])

