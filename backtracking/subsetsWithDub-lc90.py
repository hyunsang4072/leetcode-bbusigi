def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    # this problem is pretty similar to lc40-combinationSum2
    # TC: O(n * 2^n)
    # SC: O(n)
    res = []
    subset = []
    
    # sort the array beforehand
    # this is to prevent using the same element more than once
    nums.sort()

    def helper(i):
        if i == len(nums):
            res.append(subset.copy())
            return
        
        # decision1: add the current element
        curr = nums[i]
        subset.append(curr)
        helper(i + 1)

        # decision2: NOT add the current element
        subset.pop()
        while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        helper(i + 1)
    
    helper(0)

    return res