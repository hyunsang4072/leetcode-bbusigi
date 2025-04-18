def lengthOfLIS(self, nums: List[int]) -> int:
    # TC: O(n^2)
    # SC: O(n)
    # for each num in nums, check with every element that comes after current num
    # use dp list to cache and make it more efficient
    LIS = [1] * len(nums) # base case

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)): # O(n^2)
            if nums[i] < nums[j]: # strictly less than
                # since LIS[j] should contain the longest inc. subsequence
                # just add one to it and compare with current index in LIS
                LIS[i] = max(LIS[i], 1 + LIS[j])
    
    # this line is equivalent to...
    # max(1, 1 + LIS[0], 1 + LIS[1], ..., 1 + LIS[len(nums)-1])
    return max(LIS)