from math import inf

def bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -inf
        for i in range(1, j + 1):
            q  = max(q, p[i - 1] + r[j - i])
        r[j] = q
    return r[n]
      


# def ext_bottom_up_cut_rod(p, n):
#   r = [0] * n
#   s = [0] * n  
#   for j in range (1, n + 1): 
#     q = -inf
#     for i in range(1, j + 1):
#       if q < p[i - 1] + r[j - i - 1]:
#         q = p[i - 1] + r[j - i - 1]
#         s[j - 1] = i - 1
#     r[j - 1] = q
#   return r, s

# def print_cut_rod_solution(p, n):
#   r, s = ext_bottom_up_cut_rod(p, n)
#   while n > 0:
#     print(" ", s[n - 1])
#     n = n - s[n - 1]
    
    
#p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
#n = 10
#r = bottom_up_cut_rod(p, n)
#print(r)