def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1) > len(s2): return False
    
    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        # increment each character's frequency in each of the string's array
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1
    
    # we need this matches variable to be 26 in order for us
    # to conclude that there exists such a permutation of s1 in s2
    matches = 0
    # we need to go through each index of both arrays at least once
    # to figure out the 'initial' matches value
    for i in range(26):
        matches += (1 if s1Count[i] == s2Count[i] else 0)
    
    # sliding technique
    # we move forward our sliding window without changing the window size
    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26: return True

        # right ptr
        # this is equivalent of doing hashMap[s[r]] if we used hashMap approach
        index = ord(s2[r]) - ord('a')
        s2Count[index] += 1 # increment frequency of right most character
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]: # has to be this specific condition
            matches -= 1
        
        # left ptr
        # this is equivalent of doing hashMap[s[l]] if we used hashMap approach
        index = ord(s2[l]) - ord('a')
        s2Count[index] -= 1 # decrement frequency of left most character
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]: # has to be this specific condition
            matches -= 1
        l += 1 # we need to keep moving the left ptr each iteration
    
    return matches == 26