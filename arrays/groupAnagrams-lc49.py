def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    # Sorting method --> O(m*nlogn), m=len(strs) & n=avglen(each str)
    # res = []
    from collections import defaultdict
    # hashMap = defaultdict(list) # {k: [v1, ..., vn]}

    # for s in strs:
    #     sortedS = ''.join(sorted(s))
    #     hashMap[sortedS].append(s)

    # for k in hashMap:
    #     res.append(hashMap[k])
    
    # return res

    # Count frequency(Optimal) --> O(m*n)
    # m is the number of strings and n is the length of the longest string.
    # the idea is that for two strings to be anagrams of each other,
    # they must have the same frequences of each character
    res = defaultdict(list) # {k: []}
    
    for s in strs:
        count = [0]*26 # frequency for 'abcd...xyz'

        for c in s: # 'eat'
            freq = ord(c) - ord('a') # let 'a'=80, 'e'=84 --> 80-84=4
            count[freq] += 1 # increment each time a char is seen
            # print(freq, count)
        
        res[tuple(count)].append(s) # {[0,1,...,0]: ['eat']}
    
    return list(res.values())