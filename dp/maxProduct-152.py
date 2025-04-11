def maxProduct(self, nums: List[int]) -> int:
    # Kadane's Algo
    # keep the curMax, curMin to update future max values
    # e.g., nums = [2, 3, -2, 4] 
    # (2, 2), (6, 3), (-2, -12), (4, -48)
    # TC: O(n)
    # SC: O(1)
    res = nums[0]
    curMin, curMax = 1, 1

    for i in range(len(nums)):
        temp = curMax * nums[i]
        curMax = max(nums[i] * curMax, nums[i] * curMin, nums[i])
        # temp is needed to store the old curMax * nums[i] value
        curMin = min(temp, nums[i] * curMin, nums[i])
        # we don't want to consider curMin when calculating res
        res = max(res, curMax)
    
    return res

    ####### brute force -> TLE #######
    # if len(nums) == 1:
    #     return nums[0]
    # res = 0

    # def dfs(i, j):
    #     nonlocal res

    #     if j == len(nums):
    #         return
        
    #     prod = 1
    #     for ind in range(i, j + 1):
    #         prod *= nums[ind]
    #     res = max(res, prod)

    #     dfs(i + 1, j + 1)
    #     dfs(i, j + 1)
    
    # dfs(0, 0)

    # return res