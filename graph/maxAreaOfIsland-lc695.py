def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    if not grid:
        return 0
    
    ROW, COL = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)] # right, left, up, down
    visited = set()
    maxArea = 0

    def bfs(r, c):
        area = 1
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
                    grid[ro + i][co + j] == 1):
                    q.append((ro + i, co + j))
                    visited.add((ro + i, co + j))
                    area += 1
        
        return area

    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == 1 and (r, c) not in visited:
                maxArea = max(maxArea, bfs(r, c))
    
    return maxArea