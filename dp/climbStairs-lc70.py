def climbStairs(self, n: int) -> int:
    # recursion w/ memoization
    # time: O(n)
    # space: O(n)
    # memo = {}

    # def helper(i, n, m):
    #     if i > n:
    #         return 0
    #     if n == i:
    #         return 1
        
    #     if (i, n) in m:
    #         return m[(i, n)]
        
    #     dp = helper(i + 1, n, m) + helper(i + 2, n, m)

    #     m[(i, n)] = dp

    #     return dp

    # return helper(0, n, memo)

    ################################################
    # DP w/o space optimization
    # time: O(n)
    # space: O(n)
    if n <= 2: # 1 way at n=1; 2 ways at n=2
        return n
    
    # initialize dp array(1-D) bottom-up approach
    dp = [0] * (n) # [0, ... , 0]
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n): # i = 3, ..., n
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n-1]

    ################################################
    # DP w/ space optimization == optimal soln.
    # time: O(n)
    # space: O(1)
    # one, two = 1, 1

    # for i in range(n-1):
    #     temp = two
    #     two = one + two
    #     one = temp
    
    # return two