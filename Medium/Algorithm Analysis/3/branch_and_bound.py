def solve_n_queens_bnb(n: int):
    col = [False] * n  # column constraints
    pos_diag = [False] * (2 * n - 1)  # positive diagonal constraints
    neg_diag = [False] * (2 * n - 1)  # negative diagonal constraints
    
    res = []
    board = [["0"] * n for _ in range(n)]
    
    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return 
        
        #pruning
        for c in range(n):
            if col[c] or pos_diag[r + c] or neg_diag[r - c + n - 1]:
                continue
            
            # place the queen
            col[c] = pos_diag[r + c] = neg_diag[r - c + n - 1] = True
            board[r][c] = "1"
            
            backtrack(r + 1)
            
            # remove the queen 
            col[c] = pos_diag[r + c] = neg_diag[r - c + n - 1] = False
            board[r][c] = "0"
    
    backtrack(0)
    return res

solve_n_queens_bnb(4)
