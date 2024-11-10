from math import inf

def ext_bottom_up_cut_rod(p, n):
    r = [0] * (n + 1)  # Extend r to include n itself
    s = [0] * (n + 1)  # Extend s to include n itself
    for j in range(1, n + 1):
        q = -inf
        for i in range(1, j + 1):
            if q < p[i - 1] + r[j - i]:
                q = p[i - 1] + r[j - i]
                s[j] = i  # Store the cut length that gives the best revenue
        r[j] = q
    return r, s

def get_cut_rod_solution(p, n):
    r, s = ext_bottom_up_cut_rod(p, n)
    cuts = []
    while n > 0:
        cuts.append(s[n])  # Add the optimal cut length for the current rod length
        n -= s[n]  # Reduce n by the size of the cut
    return cuts  # Return the list of cuts

# Example usage:
p = [10, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 10
cuts = get_cut_rod_solution(p, n)
print("Optimal cuts to maximize revenue:", cuts)
