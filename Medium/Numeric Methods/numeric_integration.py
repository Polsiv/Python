

def f(x):
    return x**2

def rieman(a, b, n):

    dx = (b - a)/n
    total_area_left = 0
    total_area_right = 0

    x1 = a + dx
    for i in range(0, n):

        
        x0 = a + i * dx
        total_area_left += dx * f(x0)
        total_area_right += dx * f(x1)
        x1 = a + i * dx


    return total_area_left, total_area_right

a = 0
b = 3
n = 100

print(rieman(a, b, n))