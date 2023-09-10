def rabbits (n):
    if (n <= 1): return 1
    return rabbits(n - 1) + rabbits(n - 2)
print(rabbits(10))

#This algorithm is 0(n^2) time complexity, which is really bad


def optimized_rabbits(x, dir = {}):
    if (x in dir): return dir[x]
    if(x <= 1): return 1
    dir[x] = optimized_rabbits(x - 1, dir) + optimized_rabbits(x - 2, dir)
    return dir[x]

print(optimized_rabbits(10))