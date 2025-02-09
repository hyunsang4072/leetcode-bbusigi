def productExceptSelf(nums: list[int]) -> list[int]:
    # TC = O(n)
    # SC = O(1); using output arr doesn't count as an extra memory usage for this problem
    res = [0] * len(nums)

    prev, nxt = 1, 1

    # nums = [1, 2, 3, 4] --> [24, 12, 8, 6]
    # preFix = res = [1, 1, 2, 6]
    for i in range(len(nums)):
        res[i] = prev
        prev *= nums[i]

    # postFix = [24, 12, 4, 1]
    # res = [24, 12, 8, 6]
    for j in range(len(nums)-1, -1, -1):
        res[j] *= nxt
        nxt *= nums[j]

    return res