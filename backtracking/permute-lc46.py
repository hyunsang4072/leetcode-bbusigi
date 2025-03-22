def permute(self, nums: List[int]) -> List[List[int]]:
    # TC: O(n! * n^2) = O(n!)
    # SC: O(n! * n) = O(n!)
    res = []

    # base case
    # since we broke down our problems into smaller subProblems
    # we need to build up the permutations
    if not nums:
        return [[]]

    # for each recursive call, take off the first element
    perms = self.permute(nums[1:])

    for p in perms:
        for i in range(len(p) + 1):
            copy_p = p.copy()
            # insert the missing first element that we got rid of earlier
            # at every possible position i
            copy_p.insert(i, nums[0])
            res.append(copy_p)
    
    return res