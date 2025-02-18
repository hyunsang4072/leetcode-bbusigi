def search(self, nums: list[int], target: int) -> int:
    # given array is sorted
    # TC: O(logn)
    # SC: O(1)
    l, r = 0, len(nums) - 1

    while l <= r:
        # m = (l + r) // 2 # might lead to overflow
        m = l + (r - l) // 2
        if target > nums[m]:
            l = m + 1
        elif target < nums[m]:
            r = m - 1
        else:
            return m
    
    return -1