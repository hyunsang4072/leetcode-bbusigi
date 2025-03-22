def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    subset = []
    # you MUST sort the array first
    # b/c you want to skip the elements that are used already
    candidates.sort()

    def helper(s, i):
        if s == target:
            res.append(subset.copy())
            return
        if s > target or i >= len(candidates):
            return
        
        # decision1: add current element
        curr = candidates[i]
        subset.append(curr)
        helper(s + curr, i + 1) # (i + 1) because we don't want to use same element more than once

        # decision2: NOT add current element
        subset.pop()
        # increment i until we reach some new element we haven't seen yet
        while (i + 1) < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        helper(s, i + 1)
    
    helper(0, 0)
    
    return res