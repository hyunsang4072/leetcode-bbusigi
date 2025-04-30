def orangesRotting(self, grid: List[List[int]]) -> int:
    time = -1
    fresh = 0
    ROW, COL = len(grid), len(grid[0]) # m * n
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)] # right, left, up, down
    q = deque() # (r, c)

    # pre-processing
    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == 1: # fresh
                fresh += 1
            elif grid[r][c] == 2: # rotten
                q.append((r, c)) # (r, c)
    
    # check if any fresh oranges exist
    if fresh == 0:
        return 0
    
    while q:
        for _ in range(len(q)):
            r, c = q.popleft() # (r, c)
            for i, j in directions:
                if (0 <= r + i < ROW and
                    0 <= c + j < COL and
                    grid[r + i][c + j] == 1): # if fresh orange nearby, make rotten
                    grid[r + i][c + j] = 2 # make rotten
                    q.append((r + i, c + j))
                    fresh -= 1 # decrement the fresh count by one
        time += 1
    
    return time if fresh == 0 else -1
