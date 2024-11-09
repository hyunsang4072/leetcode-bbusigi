def findDuplicate(self, nums: list[int]) -> int:
    '''
    two different approaches
    1. use hashSet - extra space required
    2. use Floyd's algorithm - no extra space used
    '''
    # use hashSet
    # dupSet = {}

    # for i in nums:
    #     # dictionary.setdefault(key, default)
    #     # return value for the given key if it exists
    #     # else, insert new {key: default} pair
    #     dupSet[i] = dupSet.setdefault(i, 0) + 1

    
    # for k in dupSet.keys():
    #     if dupSet[k] > 1:
    #         return k

    # use Floyd's algo to detect cycle in LL - 2 steps
    # 1. use slow, fast ptrs to detect a cycle
    # 2. start another slow2 ptr from beginning and find the intersecting point where slow = slow2
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow