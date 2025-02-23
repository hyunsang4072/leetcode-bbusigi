def lengthOfLongestSubstring(self, s: str) -> int:
    seen = set()
    l, r = 0, 0 # we need r to start at r because of line 9
    # if we start r at 1, our set will throw a keyNotFound Error!!!
    res = 0

    while r < len(s):
        while s[r] in seen:
            # sliding window technique
            seen.remove(s[l]) # remove left until no more duplicates
            l += 1 # we need to adjust left pointer
        
        # otherwise, we keep adding a new character to our set
        seen.add(s[r])
        res = max(res, r - l + 1) # + 1 for edge cases when r == l
        # e.g., if we don't add 1 for 'a', it will return 0 (BAD!!!)
        r += 1 # update r since we are doing a while loop
    
    return res
