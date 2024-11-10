def setMismatch(self, nums: list[int]) -> list[int]:
    minVal = float("inf") # inf
    maxVal = float("-inf") # -inf
    
    seen = {}
    res = []

    nums.sort()
    
    for i in nums:
        if i < minVal:
            minVal = i
        
        if i > maxVal:
            maxVal = i
        
        if i in seen:
            seen[i] += 1
            res.append(i)
        else:
            seen[i] = 1
    
    # seen = {1:2}
    
    for j in range(maxVal): # 0 -> 1
        if (j+1) not in seen:
            res.append(j+1)
            return res
    
    res.append(nums[-1]+1)

    return res