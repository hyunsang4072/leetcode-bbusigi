def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    # TC: O(m * n)
    # SC: O(m * n)
    ROW, COL = len(board), len(board[0])
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)] # right, left, up, down

    # start dfs on edge 'O's
    def dfs(r, c):
        # mark 'O's that are edge 'O's AND
        # mark the 'O's that are connected to edge 'O's
        if (r < 0 or r >= ROW or
            c < 0 or c >= COL or
            board[r][c] != 'O'):
            return
        
        board[r][c] = 'S'

        for i, j in directions:
            dfs(r + i, c + j)
    
    for r in range(ROW):
        dfs(r, 0)
        dfs(r, COL - 1)
    for c in range(COL):
        dfs(0, c)
        dfs(ROW - 1, c)
    
    # post processing
    # TODO: go through each cell
    for r in range(ROW):
        for c in range(COL):
            # change marked cell to 'X'
            if board[r][c] == 'S':
                board[r][c] = 'O'
            # change 'O's to 'X'
            elif board[r][c] == 'O':
                board[r][c] = 'X'


    ########## not working ##########
    # edge = set() # (r, c): coordinates that are on edge of the board
    # ROW, COL = len(board), len(board[0])

    # for r in range(ROW):
    #     edge.add((r, 0)) # left-most edge
    #     edge.add((r, COL - 1)) # right-most edge
    
    # for c in range(COL):
    #     edge.add((0, c)) # top edge
    #     edge.add((ROW - 1, c)) # bottom edge
    
    # visited = set()
    # directions = [(0, 1), (0, -1), (-1, 0), (1, 0)] # right, left, up, down

    # def dfs(r, c):
    #     if ((r, c) in edge or
    #         board[r][c] == 'X' or
    #         (r, c) in visited):
    #         return
        
    #     visited.add((r, c))
    #     if (board[r + 1][c] == 'X' or
    #         board[r - 1][c] == 'X' or
    #         board[r][c + 1] == 'X' or
    #         board[r][c - 1] == 'X'): # if captured by 'X' cells
    #         board[r][c] = 'X'

    #     for i, j in directions:
    #         dfs(r + i, c + j)
    
    # # post processing
    # for r in range(ROW):
    #     for c in range(COL):
    #         if (r, c) not in edge:
    #             dfs(r, c)
