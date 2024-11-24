def twoSum(self, nums: list[int], target: int) -> list[int]:
    # sums = {}

    # sums = {
    #   3: 0
    #   2: 1
    #   4: 2
    # }

    # for i in range(len(nums)):
    #     diff = target - nums[i]
    #     if diff in sums:
    #         return [sums[diff], i]
    #     sums[nums[i]] = i
    
    # optimal: TC = O(nlogn)
    # SC = O(1)
    # 1. sort the array

    for i in range(len(nums)):
        nums[i] = (nums[i], i)
    nums.sort()

    # 2. greedy approach to find two indices
    # two ptrs: left at the beginning; right at the end
    #[(2, 1), (3, 0), (4, 2)]

    l, r = 0, len(nums) - 1
    while l != r:
        currSum = nums[l][0] + nums[r][0]
        if currSum == target:
            return [nums[l][1], nums[r][1]]
        elif currSum < target:
            l += 1
        elif currSum > target:
            r -= 1