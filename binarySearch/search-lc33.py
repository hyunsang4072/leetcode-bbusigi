def search(self, nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] == target: return m

        # think of all possible cases
        # break down to two cases: left sorted arr, right sorted arr
        # within each sorted portion, decide whether we look at current portion
        # or we look at another portion of arr by eliminating all elements inside current portion
        if nums[l] <= nums[m]: # left portion of arr
            if target > nums[m] or target < nums[l]: # target not in between l, m
                l = m + 1
            else:
                r = m - 1
        else: # right portion of arr
            if target > nums[r] or target < nums[m]:
                r = m - 1
            else:
                l = m + 1
    
    return -1