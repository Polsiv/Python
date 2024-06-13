import numpy as np
import random
import matplotlib.pyplot as plt

N = 9

# Generate random initial individuals
def create_individual():
    individual = np.zeros((N, N), dtype=int)
    for i in range(N):
        individual[i, :] = np.random.permutation(range(1, N + 1))
    return individual

# Detailed fitness function
def fitness(individual):
    fitness = 0
    # Penalize duplicates in rows
    for i in range(N):
        row = individual[i, :]
        fitness += N - len(np.unique(row))
    # Penalize duplicates in columns
    for j in range(N):
        col = individual[:, j]
        fitness += N - len(np.unique(col))
    # Penalize duplicates in 3x3 blocks
    for i in range(0, N, 3):
        for j in range(0, N, 3):
            block = individual[i:i+3, j:j+3].flatten()
            fitness += N - len(np.unique(block))
    return fitness

# Parent selection (tournament)
def select_parents(population, fitnesses):
    parents = []
    for _ in range(len(population)):
        participants = random.sample(range(len(population)), 3)
        participants_fitnesses = [fitnesses[p] for p in participants]
        winner = participants[np.argmin(participants_fitnesses)]
        parents.append(population[winner])
    return parents

# Crossover with more control
def crossover(parent1, parent2):
    crossover_point = random.randint(0, N-1)
    child1 = np.vstack((parent1[:crossover_point, :], parent2[crossover_point:, :]))
    child2 = np.vstack((parent2[:crossover_point, :], parent1[crossover_point:, :]))
    return child1, child2

# Controlled mutation
def mutate(individual):
    row = random.randint(0, N-1)
    col1, col2 = random.sample(range(N), 2)
    individual[row, col1], individual[row, col2] = individual[row, col2], individual[row, col1]

# Genetic Algorithm with random initial population
def genetic_algorithm(pop_size, max_generations):
    population = [create_individual() for _ in range(pop_size)]
    for generation in range(max_generations):
        fitnesses = [fitness(ind) for ind in population]
        print(f"Generation {generation} - Best fitness: {min(fitnesses)}")
        if min(fitnesses) == 0:
            break
        parents = select_parents(population, fitnesses)
        next_population = []
        for i in range(0, len(parents), 2):
            parent1 = parents[i]
            parent2 = parents[i + 1 if i + 1 < len(parents) else 0]
            child1, child2 = crossover(parent1, parent2)
            if random.random() < 0.1:
                mutate(child1)
            if random.random() < 0.1:
                mutate(child2)
            next_population.extend([child1, child2])
        population = next_population[:pop_size]
    return population[np.argmin(fitnesses)]

# Function to plot the Sudoku
def plot_sudoku(sudoku):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, N)
    ax.set_ylim(0, N)
    
    for i in range(N+1):
        lw = 2 if i % 3 == 0 else 1
        ax.plot([i, i], [0, N], 'k', lw=lw)
        ax.plot([0, N], [i, i], 'k', lw=lw)
        
    for i in range(N):
        for j in range(N):
            if sudoku[i, j] != 0:
                ax.text(j + 0.5, N - i - 0.5, sudoku[i, j], 
                        ha='center', va='center', fontsize=16)
                
    plt.gca().invert_yaxis()
    plt.axis('off')
    plt.show()

# Run the algorithm
best_solution = genetic_algorithm(pop_size=100, max_generations=1000)
print("Best solution found:")
print(best_solution)

# Plot the best solution found
plot_sudoku(best_solution)
