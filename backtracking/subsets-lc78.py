def subsets(self, nums: List[int]) -> List[List[int]]:
    # TC: O(n * 2^n)
    # SC: O(n)
    res = []

    subset = []
    def dfs(i):
        # base case
        # i is the index of current element
        if i >= len(nums):
            res.append(subset.copy())
            return

        # split in to two different cases
        # 1. we add the current element
        subset.append(nums[i])
        dfs(i + 1)

        # 2. we don't add the current element
        subset.pop()
        dfs(i + 1)
    
    dfs(0)

    return res