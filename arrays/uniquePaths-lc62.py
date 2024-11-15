def uniquePaths(self, m: int, n: int) -> int:
    # still not optimal solution
    # memoization
    seen = {}

    def helper(r, c):
        # has access to m and n --> grid = m x n dimension
        ans = 0

        if r == m - 1 and c == n - 1: # destination reached
            return 1
        elif r == m or c == n:
            return 0
        elif r < 0 or c < 0:
            return 0
        
        if (r, c) in seen:
            ans = seen[(r, c)]
        else:
            ans = helper(r, c + 1) + helper(r + 1, c)
            seen[(r, c)] = ans
        
        return ans
    
    res = helper(0, 0)

    return res