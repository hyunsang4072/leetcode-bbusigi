def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
    res = []

    nums.sort()
    # [-2, -1, 0, 0, 1, 2]
    #   ^               ^
    #   i               j

    # fix two elems
    # optimize further by skipping duplicate values
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]: continue
        for j in range(len(nums)-1, 0, -1): # range(start, stop, step)
            if i == j: break
            l, r = i + 1, j - 1
            if j < len(nums)-1 and nums[j] == nums[j+1]: continue
            while l < r:
                s = nums[i] + nums[l] + nums[r] + nums[j]
                if s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r], nums[j]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
    
    return res