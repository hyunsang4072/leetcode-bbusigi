def maxProfit(self, prices: list[int]) -> int:
    res = 0

    l, r = 0, 1
    while r < len(prices):
        if prices[r] > prices[l]: # profitable
            profit = prices[r] - prices[l]
            res = max(res, profit)
        else: # not profitable and since we checked all values up to where right pointer is
        # we can just skip those values by moving left pointer to where right pointer is
            l = r
        r += 1
    
    return res