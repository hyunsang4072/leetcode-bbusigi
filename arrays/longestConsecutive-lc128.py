def longestConsecutive(self, nums: list[int]) -> int:
    hashSet = set(nums)

    longest = 0
    for n in hashSet: # DO NOT use original list since we want to skip duplicates!!!
        if (n-1) not in hashSet: # n is starting point of a sequence
            count = 1
            while (n + count) in hashSet: # O(1)
                count += 1
            longest = max(longest, count)
    
    return longest