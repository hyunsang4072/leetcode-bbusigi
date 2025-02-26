def minWindow(s: str, t: str) -> str:
    # strings: s, t
    # m = len(s), n = len(t)
    if not t: return ""

    # countT: hashMap containing counts of each char in string t
    # window: hashMap containing counts of each char within current window
    countT, window = {}, {}
    
    # initialize countT; it won't be changed
    for c in t:
        countT[c] = countT.get(c, 0) + 1
    
    # need -> countT
    # have -> window
    need, have = len(countT), 0

    # res: the indices of left and right pointer;
    # res will be used to get the characters in s at the end
    # resLen will keep track of the minimum window size that satisfies the problem
    res, resLen = [-1, -1], float('infinity')
    
    # initialize left pointer; allows us to dynamically change the size of our window
    l = 0
    for r in range(len(s)):
        c = s[r] # for each new char, update the count on window map
        window[c] = window.get(c, 0) + 1

        # we don't really care about c that's not in string t
        if c in countT and window[c] == countT[c]:
            have += 1 # counts of c are equal so we satisfied one of the characters in t
        
        while have == need:
            # whenever we met the requirement, we update the result
            # current window size = r - l + 1
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = r - l + 1
            # since we want to minimize our window size
            # while having met the problem constraint,
            # we shift our left pointer to decrement the window size
            window[s[l]] -= 1 # decrement count
            # if removing leftmost char affected our condition, update have
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1 # because now, we are missing that character
            l += 1

    # extract l and r values from res array
    l, r = res # unzipping in Python

    return s[l:r+1] if resLen != float('infinity') else ""