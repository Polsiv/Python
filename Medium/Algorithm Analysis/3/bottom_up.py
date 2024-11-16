from math import inf

def bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)  #max revenue
    s = [0] * (n + 1)  #cuts

    for j in range(1, n + 1):
        q = -inf
        for i in range(1, j + 1):
            if q < p[i - 1] + r[j - i]:
                q = p[i - 1] + r[j - i]
                s[j] = i  #stpre length of the first piece to cut
        r[j] = q
    
    return r[n], s

def get_cut_rod_solution(s, n):
    sol = []
    while n > 0:
        sol.append(s[n])
        n -= s[n]  #reduce n by the length of the first piece
    return sol

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 4
cost, cuts = bottom_up_cut_rod(p, n)
#print(cuts)
solution_pieces = get_cut_rod_solution(cuts, n)
print(cost)
print(solution_pieces)



    
