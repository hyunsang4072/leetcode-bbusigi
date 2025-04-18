def longestPalindrome(self, s: str) -> str:
    # Optimal approach
    # TC: O(n^2)
    # SC: O(1) extra space; except for out string, which is O(n)
    resInd = 0
    resLen = 0

    for i in range(len(s)):
        # odd
        l, r = i, i
        oddStr = ""
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                resInd = l
                resLen = r - l + 1
            l -= 1
            r += 1
        
        # even
        l, r = i, i + 1
        evenStr = ""
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                resInd = l
                resLen = r - l + 1
            l -= 1
            r += 1

    return s[resInd : resInd + resLen]

    ######## two pointer approach #######
    # still not optimal since we are doing slicing to update res
    # res = ""
    # resLen = 0

    # for i in range(len(s)):
    #     # odd
    #     l, r = i, i
    #     oddStr = ""
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         if (r - l + 1) > resLen:
    #             resLen = r - l + 1
    #             res = s[l:r+1]
    #         l -= 1
    #         r += 1
        
    #     # even
    #     l, r = i, i + 1
    #     evenStr = ""
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         if (r - l + 1) > resLen:
    #             resLen = r - l + 1
    #             res = s[l:r+1]
    #         l -= 1
    #         r += 1

    # return res