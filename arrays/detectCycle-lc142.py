def findDuplicate(self, nums: list[int]) -> int:
    # Optimal Soln. using LL + Floyd's algo... (very unintuitive)
    # TC: O(n)
    # SC: O(1)

    slow, fast = 0, 0

    # detect a cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast: # they are at some intersection within a cycle
            break
    
    # initialize another slow ptr that starts at the beginning
    # by Floyd's algo, we know for sure that the slow and slow2 ptrs will
    # meet at the beginning of the cycle as long as there's a cycle
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow