def threeSum(self, nums: list[int]) -> list[list[int]]:
    '''
    1. fix one of them --> then, it becomes a twoSum problem
    2. repeat for all elements
    '''
    res = []

    nums.sort()
    # [-4, -1, -1, 0, 1, 2]

    for i in range(len(nums)):
        # since the array is sorted, left ptr value must be either zero or negative
        # otherwise, it's not possible to find any combination that satisfies the problem cond.
        if nums[i] > 0: break # optimization
        if i > 0 and nums[i] == nums[i-1]: # skip duplicate elem
            # i > 0 must be true
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0: # sum too small
                l += 1
            elif s > 0: # sum too big
                r -= 1
            else: # sum == 0
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    # l < r cond. for out-of-bounds err
                    l += 1 # skip already seen elem
    
    return res