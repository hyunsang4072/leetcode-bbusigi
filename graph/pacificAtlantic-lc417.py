def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    # square grid
    # find (r, c) where the rain water can flow
    # from (r, c) to both the Pacific and Atalantic oceans
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)] # right, left, up, down
    ROW, COL = len(heights), len(heights[0])
    pacific, atlantic = set(), set() # (r, c)

    # dfs
    def dfs(r, c, visited, prevH):
        # instead of starting from middle and going outwards
        # we start from each ocean, and move towards the middle
        # think going up the hills
        if (r < 0 or c < 0 or
            r >= ROW or c >= COL or
            (r, c) in visited or
            heights[r][c] < prevH): # think opposite conditions
            return
        
        # otherwise, add coordinate to the set
        visited.add((r, c)) # avoids visiting the same cell twice
        for i, j in directions: # look each direction
            dfs(r + i, c + j, visited, heights[r][c])

    # how to check whether (r, c) in pacific ocean or atlantic ocean?
    # get pacific, atlantic (r, c) that meet the requirements
    for c in range(COL): # top row, bottom row
        dfs(0, c, pacific, heights[0][c])
        dfs(ROW - 1, c, atlantic, heights[ROW - 1][c])
    
    for r in range(ROW): # left-most col, right-most col
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, COL - 1, atlantic, heights[r][COL - 1])

    # post processing
    # pacific, atlantic should now have all the coordinates
    # that meet the problem requirements
    res = []
    for r in range(ROW):
        for c in range(COL):
            if (r, c) in pacific and (r, c) in atlantic:
                res.append([r, c])

    return res
