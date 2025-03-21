def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    subset = []

    def helper(s, i):
        # base case1: we found a subset we want
        if s == target:
            res.append(subset.copy())
            return
        # base case2: subset not add up to target or index out of bounds
        if s > target or i >= len(candidates):
            return
        
        # add current element
        curr = candidates[i]
        subset.append(curr)
        helper(s + curr, i)

        # NOT add current element
        # note that if we decided to add i-th element above,
        # we don't consider it anymore for later recursive calls
        # this is to avoid having any duplicates
        subset.pop()
        helper(s, i + 1)
    
    helper(0, 0)

    return res