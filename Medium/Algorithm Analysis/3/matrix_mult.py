def matrix_chain_order(p):
    n = len(p) - 1  # number of matrices

    # create tables m and s
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]

    # fill the tables m and s in a bottom-up manner
    for l in range(2, n + 1):
        for i in range(n - l + 1): # l is the chain length
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s  


def print_optimal_parens(s, i, j):

    # prints the optimal parenthesization of a matrix chain multiplication.
    if i == j:
        print("A" + str(i + 1), end="")  
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

p = [10, 20, 30, 40]

m, s = matrix_chain_order(p)

# Print the optimal parenthesization
print_optimal_parens(s, 0, len(p) - 2)

# Print the minimum number of scalar multiplications
print("\nminimum number of scalar multiplications:", m[0][len(p) - 2])
