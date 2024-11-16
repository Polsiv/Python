def cut_rod(p, n):
    if n == 0:
        return 0, []
    q = 0
    best_cut = 0
    for i in range(n):
        current_revenue, _ = cut_rod(p, n - i - 1)
        if q < p[i] + current_revenue:
            q = p[i] + current_revenue
            best_cut = i + 1 
    max_revenue, cuts = cut_rod(p, n - best_cut)
    return q, [best_cut] + cuts

p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 4
cost, cuts = cut_rod(p, n)
print(cost)
print(cuts)
