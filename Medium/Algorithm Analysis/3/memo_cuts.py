from math import inf

def memo_cut_rod(p, n):
    r = [-inf] * n  # memorization array to store the optimal revenues
    s = [0] * n # array to store the first cut for each length
    memo_cut_rod_aux(p, n, r, s)
    return r[n - 1], reconstruct_solution(s, n)

def memo_cut_rod_aux(p, n, r, s):
    if r[n - 1] >= 0:  # of already computedeturn the value
        return r[n - 1]
    if n == 0:
        q = 0
    else:
        q = -inf
        for i in range(1, n + 1):
            val = p[i - 1] + memo_cut_rod_aux(p, n - i, r, s)
            if val > q:
                q = val
                s[n - 1] = i #store the size of the first piece to cut
    r[n - 1] = q
    return q

def reconstruct_solution(s, n):
    pieces = []
    while n > 0:
        pieces.append(s[n - 1])
        n -= s[n - 1]
    return pieces

n = 10
price_list = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(memo_cut_rod(price_list, n))