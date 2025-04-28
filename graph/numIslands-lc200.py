def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0
    
    ROW, COL = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)] # right, left, up, down
    visited = set()
    island = 0

    def bfs(r, c):
        q = deque() # [] <- [] -> []
        # update queue and visited set
        q.append((r, c))
        visited.add((r, c))

        while q:
            ro, co = q.popleft()
            for i, j in directions:
                if (0 <= (ro + i) < ROW and
                    0 <= (co + j) < COL and
                    (ro+i, co+j) not in visited and
                    grid[ro + i][co + j] == "1"):
                    q.append((ro + i, co + j))
                    visited.add((ro + i, co + j))


    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                island += 1
    
    return island