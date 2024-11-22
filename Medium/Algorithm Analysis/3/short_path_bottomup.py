def extend_shortest_paths(L, W):
    n = len(L)  # nodes in the graph

    # new matrix L' to store the extended shortest paths
    L_prime = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        
        for j in range(n):
            # iterate over each intermediate node k
            for k in range(n):
                # update the shortest path from i to j through k
                L_prime[i][j] = min(L_prime[i][j], L[i][k] + W[k][j])

    return L_prime


L = [[0, 4, 2], [5, 0, 1], [3, 2, 0]]
W = [[0, 4, 2], [5, 0, 1], [3, 2, 0]]

L_prime = extend_shortest_paths(L, W)
for row in L_prime:
    print(row)