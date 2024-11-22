def  extendshortest_paths_memo_matrix(L, W):
    n = len(L) #number of nodes
    
    L_prime = [[float('inf')] * n for _ in range(n)]
    
    
    def shortest_path(i, j):
        """
        calculate the shortest distance form node i to node j, using memo recursion
        """
        
        #if valueis not inf (means its calculated) return the value!
        if L_prime[i][j] != float('inf'):
            return L_prime[i][j]
        
        #base case, no intermediate nodes between
        L_prime[i][j] = L[i][j]
        
        #re-calculate the minimun distance considering the intermediate k nodes.
        for k in range(n):
            L_prime[i][j] = min(L_prime[i][j], shortest_path(i, k) + W[k][j])
            
        return L_prime[i][j]
        
    #calculate the shortest distances between all (i, j) pairs
    for i in range(n):
        for j in range(n):
            shortest_path(i, j)
            
    return L_prime

W = [[0, 4, 2], [5, 0, 1], [3, 2, 0]]
L = W


L_prime = extendshortest_paths_memo_matrix(L, W)
for row in L_prime:
    print(row)