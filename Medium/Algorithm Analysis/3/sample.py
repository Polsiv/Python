import random


#1000 vertices, 2000 edges
edges13 = [(random.randint(0, 999), random.randint(0, 999), random.randint(1, 200)) for _ in range(2000)]
edges13 = list(set(edges13))

#1000 vertices, ~499500 edges
edges14 = [(i, j, random.randint(1, 200)) for i in range(1000) for j in range(i + 1, 1000)]

#10,000 vertices, 15,000 edges
edges15 = [(random.randint(0, 9999), random.randint(0, 9999), random.randint(1, 500)) for _ in range(15000)]
edges15 = list(set(edges15))

#10,000 vertices, ~49,995,000 edges
edges16 = [(i, j, random.randint(1, 500)) for i in range(10000) for j in range(i + 1, 10000)]

graphs = [edges13, edges14, edges15, edges16]