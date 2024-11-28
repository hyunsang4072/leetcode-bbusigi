def longestConsecutive(self, nums: list[int]) -> int:
    # can't use sorting --> O(nlogn)
    
    seen = set() # unordered

    for i in range(len(nums)):
        seen.add(nums[i])
    
    longest = 0

    # find starting point
    # find longest from start
    for j in seen:
        if j-1 not in seen: # start point found; else ignore current
            c = 1
            while j+1 in seen: # count how long our consecutive sequence is from start
                c += 1
                j += 1
            if c > longest: # update if needed
                longest = c
    
    return longest