def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    # bottom-up DP approach
    # TC: O(n * m), where n=len(text1), m=len(text2)
    # SC: O(n * m)
    r, c = len(text1), len(text2)
    # create a 2d-dp list with an extra layer of 0's surrounding the actual dp
    dp = [[0] * (c + 1) for _ in range(r + 1)]
    # row=text1, col=text2
    # dp = [
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 0]
    # ]
    
    # break original problem into smaller subproblems
    for i in range(r - 1, -1, -1):
        for j in range(c - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    
    # e.g., text1 = "abcde", text2 = "ace" 
    # dp = [
    #     [3, 2, 1, 0],
    #     [2, 2, 1, 0],
    #     [2, 2, 1, 0],
    #     [1, 1, 1, 0],
    #     [1, 1, 1, 0],
    #     [0, 0, 0, 0]
    # ]

    return dp[0][0]