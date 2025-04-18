def canPartition(self, nums: List[int]) -> bool:
    # TC: O(n*t), where n=len(nums), t=sum of array elements divided by 2
    # SC: O(t), where t=sum of array elements divided by 2
    # in order for two subsets to have sums equal to one another,
    # they should have a sum that's equal to half of total sum
    total = sum(nums)
    if total % 2 == 1:
        return False
    
    half = total // 2
    combs = set()
    combs.add(0) # we can always form a sum of 0 using the empty subset.

    for i in range(len(nums) - 1, -1, -1):
        n = nums[i]
        copy = set() # modifying the set while iterating it is NOT allowed
        for c in combs: # create all possible sum's
            if n + c == half: # optimization; not needed for completion
                return True
            copy.add(n + c)
        combs.update(copy)
    
    if half in combs:
        return True
    
    return False