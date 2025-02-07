def isAnagram(self, s: str, t: str) -> bool:
    # length should be equal
    if len(s) != len(t):
        return False

    # sortedS = ''.join(sorted(s))
    # sortedT = ''.join(sorted(t))

    # for i in range(len(s)):
    #     if sortedS[i] != sortedT[i]:
    #         return False
    
    # return True

    s1 = {}
    s2 = {}

    for i in range(len(s)): # time: O(n)
        sc = s[i]
        tc = t[i]

        s1[sc] = s1.get(sc, 0) + 1
        s2[tc] = s2.get(tc, 0) + 1
    
    for c in 'abcdefghijklmnopqrstuvwxyz': # time: O(1) since 26 characters
        if c in s1 and c in s2:
            if s1[c] == s2[c]:
                continue
            else:
                return False
        elif c not in s1 and c not in s2:
            continue
        else:
            return False
    
    return True