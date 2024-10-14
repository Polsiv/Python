def f(x):
    match x:
        case 1:
            return 2
        case 2:
            return 3
        case 3:
            return 5

def lagrange(a, b, f, x):

    sum = 0
    for i in range(a, b + 1):
        L = 1
        for j in range(a, b + 1):
            if i == j:
                continue
            
            else:
                L *= (x - j) / (i - j)

        sum += L * f(i)
    return sum


a = 1
b = 3
n = 3
x = 2.6

print(lagrange(a, b, f, x))