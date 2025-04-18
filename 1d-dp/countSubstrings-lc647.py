def countSubstrings(self, s: str) -> int:
    # visit lc5-longestPalindrome question before this one
    # TC: O(n^2)
    # SC: O(1)
    res = 0
    
    for i in range(len(s)):
        res += self.countPalindromes(s, i, i)
        res += self.countPalindromes(s, i, i + 1)
    
    return res

def countPalindromes(self, s, l, r) -> int:
    count = 0

    while l >= 0 and r < len(s) and s[l] == s[r]:
        count += 1
        l -= 1
        r += 1
    
    return count

    ####### same approach, but redundant #######
    # res = 0

    # for i in range(len(s)):
    #     # odd
    #     l, r = i, i
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         res += 1
    #         l -= 1
    #         r += 1
        
    #     # even
    #     l, r = i, i + 1
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         res += 1
    #         l -= 1
    #         r += 1

    # return res