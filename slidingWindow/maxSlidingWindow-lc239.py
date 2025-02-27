import collections

def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
    # brute force --> TC: O(n*k)
    # this soln TLE on leetCode

    # if len(nums) == 1: return nums

    # res = [0] * (len(nums) - k + 1)

    # l = 0
    # for r in range(k-1, len(nums)):
    #     res[l] = max(nums[l:r+1])
    #     l += 1
    
    # return res

    ############################################################
    # optimal soln.
    # TC = SC = O(n)
    res = []
    # keep indices of elements in deque in decreasing order
    q = collections.deque() # contains indices, not elements!!!
    # l: left bound of window
    # r: right bound of window
    l = r = 0

    while r < len(nums):
        # before inserting nums[r], we remove all indices from q
        # whose corresponding values are smaller than nums[r]
        while q and nums[q[-1]] < nums[r]: # ensures decreasing order
            q.pop()
        q.append(r)

        # q[0] should have the index of the maximum value for current window
        if l > q[0]: # if left bound of window passed index at q[0], remove it from q
            q.popleft() # elements outside window is removed
        
        # since r starts at index 0, the first window of size k is formed when r reaches k - 1.
        # from this point onward, every time r increases, new sliding window is calculated
        # this ensures that we don't add anything to the res array unless we have a window of size k
        if (r + 1) >= k: # we will add 1 element each time after we met this condition
            res.append(nums[q[0]])
            # since we've just found a window of size k, we want to increment l
            # so that our window is moving
            l += 1
        
        # increment right pointer
        r += 1
    
    return res