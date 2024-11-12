def majorityElement(self, nums: List[int]) -> List[int]:
    # res = []

    # th = len(nums) // 3

    # seen = {}

    # for i in range(len(nums)):
    #     val = nums[i]
    #     seen[val] = seen.setdefault(val, 0) + 1

    # for el in seen:
    #     count = seen[el]
    #     if count > th:
    #         res.append(el)

    # return res


    # optimal
    # use Boyer-Moore Majority Voting Algorithm
    # arr = [3, 2, 3] --> n = 3 && n // 3 = 1
    # if n = 9999 --> n // 3 = 3333

    res = []

    th = len(nums) // 3

    val1, val2 = 0, 0
    c1, c2 = 0, 0

    for i in range(len(nums)):
        if c1 == 0 and val2 != nums[i]:
            val1 = nums[i]
            c1 += 1
        elif c2 == 0 and val1 != nums[i]:
            val2 = nums[i]
            c2 += 1
        elif val1 == nums[i]:
            c1 += 1
        elif val2 == nums[i]:
            c2 += 1
        else:
            c1 -= 1
            c2 -= 1
    
    count1 = count2 = 0
    for num in nums:
        if val1 == num:
            count1 += 1
        elif val2 == num:
            count2 += 1        
    
    if count1 > th:
        res.append(val1)
    if count2 > th:
        res.append(val2)

    return res