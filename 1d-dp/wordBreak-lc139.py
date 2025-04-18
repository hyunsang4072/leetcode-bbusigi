def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    # DP approach
    # TC: O(n * m * t), where n = len(s), m = len(wordDict), and
    # t = maximum length of any string in wordDict
    # SC: O(n)
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True # base case

    # iterate the index in reverse order
    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            # first, check whether this string has a length that's within
            # the len(s); this check is needed to avoid indexOutOfBounds error
            # next, check for matching word
            if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            # if already checked, move to next iteration
            if dp[i]:
                break
    
    return dp[0]

    ####### attempt 2: wrong
    # l = 0

    # for w in wordDict:
    #     if l > len(s): return True
    #     wLen = len(w)
    #     if s[l : l + wLen] != w:
    #         return False
    #     l = l + wLen
    
    # return True
    
    ####### attempt 1: TLE
    # l = 0
    # count = 0

    # while l < len(s):
    #     r = l
    #     while r <= len(s):
    #         subStr = s[l:r]
    #         if subStr in wordDict:
    #             count += 1
    #             break
    #         r += 1
    #     l = r
    
    # return count == len(wordDict)