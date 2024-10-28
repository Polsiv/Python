def f(x):
    match x:
        case 0:
            return 0
        case 10:
            return 227
        case 15:
            return 362

def lagrange(a, b, f, x):
    A = [0, 227, 362]
    B=[0,10,15]
    sum = 0
    for i in range(len(A)):
        L = 1
        for j in range(len(A)):
            if i == j:
                continue
            
            else:
                L *= (x - B[j]) / (B[i] - B[j])

        sum += L * A[i]
    return sum


a = 0
b = 15
n = 3
x = 12

print(lagrange(a, b, f, x))