def maxProfit(self, prices: list[int]) -> int:
    # we have to move forward so we can't just find min/max and find the difference between the two.
    # we use a loop to look at each day's price
    maxProf = 0
    minPrice = prices[0]

    for i in range(len(prices)):
        minPrice = min(minPrice, prices[i]) # update minPrice
        maxProf = max(maxProf, prices[i] - minPrice) # update maxProf if possible
    
    return maxProf