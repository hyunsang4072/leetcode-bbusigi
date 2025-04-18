def uniquePaths(self, m: int, n: int) -> int:
    # TC: O(m*n), where m = # of rows, n = # of cols
    # SC: O(m*n), where m = # of rows, n = # of cols
    # [[0, 0, 0, 0, 0, 0, 0, 0], 
    #  [0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 1, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0]]
    # 1 extra layer of 0 around the edge of dp
    # hard to solve this type of problem w/o visualization
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[m-1][n-1] = 1

    for r in range(m - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            dp[r][c] += dp[r + 1][c] + dp[r][c + 1]
    
    return dp[0][0]

    # recursion using dfs with memoization -> works!
    # TC: O(m*n), where m = # of rows, n = # of cols
    # SC: O(m*n), where m = # of rows, n = # of cols
    # path = {}

    # def dfs(r, c):
    #     if r >= m or c >= n:
    #         return 0
    #     if r == m - 1 and c == n - 1:
    #         return 1

    #     if (r, c) in path:
    #         return path[(r, c)] # cache

    #     res = dfs(r + 1, c) + dfs(r, c + 1) # move either down or right

    #     path[(r, c)] = res

    #     return res
    
    # return dfs(0, 0)