def rob(self, nums: List[int]) -> int:
    # TC: O(n)
    # SC: O(1)
    # using two variables
    rob1, rob2 = 0, 0

    # [rob1, rob2, nums[i], nums[i+1], ...]
    # to compute current value, we look at
    # past best results so far(in this case, it's max profit)
    for i in range(len(nums)):
        temp = max(rob1 + nums[i], rob2)
        rob1 = rob2
        rob2 = temp

    return rob2

    ####### my soln. #######
    # TC: O(n)
    # SC: O(1) since we use the given arr
    # nums.append(0)

    # for i in range(len(nums) - 3, -1, -1):
    #     nums[i] = max(nums[i + 1], nums[i] + nums[i + 2])

    # return max(nums)