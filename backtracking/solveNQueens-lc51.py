def solveNQueens(self, n: int) -> List[List[str]]:
    # TC: O(n!)
    # SC: O(n^2)
    res = []
    board = [["."] * n for _ in range(n)]
    # e.g., for n=4,
    # [["...."],
    #  ["...."],
    #  ["...."],
    #  ["...."]]

    col = set()
    posDiag = set() # (r + c); from left to right, diagonal pointing upwards
    negDiag = set() # (r - c); from left to right, diagonal pointing downwards

    def backtrack(r):
        if r == n: # found a combination
            # make a copy of a board
            # since it's a list of lists, you can't call copy()
            copy = ["".join(r) for r in board]
            res.append(copy)
            return
        
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            
            # decision1: add Queen(Q) at position (r, c)
            # this means we add the following values to corresponding sets
            # to ensure that we don't have any of two queens attacking each other
            col.add(c)
            posDiag.add((r + c))
            negDiag.add((r - c))
            board[r][c] = "Q" # e.g., [["...."]] -> [["..Q."]]

            backtrack(r + 1)

            # decision2: NOT add Queen(Q) at position (r, c)
            # since we added Queen for decision1, we have to remove it before
            # considering the next backtracking iteration(i.e., undo what we did)
            col.remove(c)
            posDiag.remove((r + c))
            negDiag.remove((r - c))
            board[r][c] = "." # e.g., [["..Q."]] -> [["...."]]
    
    backtrack(0)

    return res