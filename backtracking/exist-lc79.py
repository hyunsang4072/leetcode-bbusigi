def exist(self, board: List[List[str]], word: str) -> bool:
    # [["A","B","C","E"],
    #  ["S","F","C","S"],
    #  ["A","D","E","E"]]
    seen = set()

    def dfs(r, c, i):
        if i == len(word):
            return True

        # out of bounds/board
        if r >= len(board) or r < 0:
            return False
        if c >= len(board[r]) or c < 0:
            return False
        if word[i] != board[r][c]:
            return False
        
        # this check MUST be placed after out of bounds checks!!!
        if (r, c) in seen:
            return False
        seen.add((r, c))
        
        # up, down, left, right
        res = (dfs(r - 1, c, i + 1) or
                dfs(r + 1, c, i + 1) or 
                dfs(r, c - 1, i + 1) or 
                dfs(r, c + 1, i + 1))
        
        seen.remove((r, c))

        return res
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if dfs(i, j, 0):
                return True
    
    return False