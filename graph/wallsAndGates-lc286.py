def wallsAndGates(self, rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    if not rooms:
        return
    
    ROW, COL = len(rooms), len(rooms[0])
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)] # right, left, up, down
    q = deque() # (r, c, dist)

    for r in range(ROW):
        for c in range(COL):
            if rooms[r][c] == 0: # we only want to run bfs from the gate
                q.append((r, c, 0))

    # run bfs simultaneously!!!
    while q:
        r, c, dist = q.popleft()
        for i, j in directions:
            if (0 <= r + i < ROW and
                0 <= c + j < COL and
                rooms[r + i][c + j] == 2147483647): # hasn't been reached yet!
                rooms[r + i][c + j] = dist + 1
                q.append((r + i, c + j, dist + 1))
