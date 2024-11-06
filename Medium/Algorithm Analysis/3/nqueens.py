def solve_n_queens(n: int):
    col = set()
    pos_diag = set()  # (r + c)
    neg_diag = set()  # (r - c)
    
    res = []
    board = [["0"] * n for _ in range(n)]
    
    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return 
        
        for c in range(n):  # columns
            if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                continue
            
            col.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = "1"
            
            backtrack(r + 1)
            
            
            # backtrack (remove the queens that dont fit the solution)
            col.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = "0"
            
    backtrack(0)
    return res

results = solve_n_queens(4)

for i in range(len(results)):
    print("\n")
    for j in range(len(results[i])):
        print(" ".join(results[i][j]))
    
