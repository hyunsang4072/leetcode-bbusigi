def coinChange(self, coins: List[int], amount: int) -> int:
    # TC: O(n * t); n = len(coins), t = amount
    # SC: O(t)
    dp = [amount + 1] * (amount + 1) # initialize arr -> [0, ..., amount + 1]
    dp[0] = 0 # base case: only one(no) way to satisfy the amount 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                # coin(c) = 4
                # amount(a) = 7
                # dp[7] = 1 + dp[7 - 4]; since we used up 4
                #       = 1 + dp[3]; find a way to make amount 3
                dp[a] = min(dp[a], 1 + dp[a - c])
    
    # it's possible that we don't find the right combination to make the amount
    return dp[amount] if dp[amount] != amount + 1 else -1