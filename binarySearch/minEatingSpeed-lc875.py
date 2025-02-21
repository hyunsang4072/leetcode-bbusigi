import math

def minEatingSpeed(self, piles: list[int], h: int) -> int:
    # binary search on [1, max(piles)]
    # TC: O(n*logm)
    # SC: O(1)
    l, r = 1, max(piles)
    res = 0

    while l <= r:
        m = (l + r) // 2

        # for each rate, find how many hours in total
        # it takes koko to eat all of the bananas
        total = 0
        for p in piles:
            total += math.ceil(p / m) # we want integer values since we are dealing w/ hours
        
        if total > h: # this happens if the rate is too slow
            l = m + 1
        else:
            res = m
            r = m - 1 # guarantees that the res will always be minimal if updated
    
    return res # optimal res