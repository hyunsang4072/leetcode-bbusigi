def majorityElement(self, nums: list[int]) -> int:
    # hashMap approach
    # seen = {}

    # for i in range(len(nums)):
    #     val = nums[i]
    #     # if val not in seen:
    #     #     seen[val] = 1
    #     # seen[val] += 1
    #     seen[val] = seen.setdefault(val, 0) + 1
    
    # th = len(nums) // 2

    # for el in seen:
    #     if seen[el] > th:
    #         return el

    # optimal approach --> Moore's voting algorithm
    # iterate through array once
    # when iterating, keep track of val that has not been counted out yet
    # c is to keep track of whether this current val is not outnumbered by other elements or not
    # once c has reached for current val, it has to be replaced by next element in the array
    val, c = 0, 0
    
    for i in range(len(nums)):
        if c == 0:
            val = nums[i]
            c += 1
        elif val != nums[i]:
            c -= 1
        else:
            c += 1
    
    return val