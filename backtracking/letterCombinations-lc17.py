def letterCombinations(self, digits: str) -> List[str]:
    # TC: O(n * 4^n)
    # SC: O(n * 4^n)
    res = []
    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    if not digits: return res

    # store current index and string that we've built so far
    def backtrack(i, curr):
        # base case
        if len(curr) == len(digits):
            res.append(curr)
            return
        
        for c in mapping[digits[i]]:
            # we want to always increment i by one
            # add each character in mapping to current string
            backtrack(i + 1, curr + c)
    
    backtrack(0, "")

    return res

    ####### brute-force soln. #######
    # res = []
    # mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    # if not digits: return res
    # if len(digits) == 1:
    #     num = int(digits[0])
    #     return list(mapping[num])

    # def helper2(n1, n2):
    #     n1, n2 = int(n1), int(n2)
    #     for i in range(len(mapping[n1])):
    #         for j in range(len(mapping[n2])):
    #             s = mapping[n1][i] + mapping[n2][j]
    #             res.append(s)
    
    # def helper3(n1, n2, n3):
    #     n1, n2, n3 = int(n1), int(n2), int(n3)
    #     for i in range(len(mapping[n1])):
    #         for j in range(len(mapping[n2])):
    #             for k in range(len(mapping[n3])):
    #                 s = mapping[n1][i] + mapping[n2][j] + mapping[n3][k]
    #                 res.append(s)
    
    # def helper4(n1, n2, n3, n4):
    #     n1, n2, n3, n4 = int(n1), int(n2), int(n3), int(n4)
    #     for i in range(len(mapping[n1])):
    #         for j in range(len(mapping[n2])):
    #             for k in range(len(mapping[n3])):
    #                 for l in range(len(mapping[n4])):
    #                     s = mapping[n1][i] + mapping[n2][j] + mapping[n3][k] + mapping[n4][l]
    #                     res.append(s)

    # if len(digits) == 2:
    #     for i in range(len(digits)):
    #         for j in range(i+1, len(digits)):
    #             helper2(digits[i], digits[j])
    
    # if len(digits) == 3:
    #     for i in range(len(digits)):
    #         for j in range(i+1, len(digits)):
    #             for k in range(j+1, len(digits)):
    #                 helper3(digits[i], digits[j], digits[k])
    
    # if len(digits) == 4:
    #     for i in range(len(digits)):
    #         for j in range(i+1, len(digits)):
    #             for k in range(j+1, len(digits)):
    #                 for l in range(k+1, len(digits)):
    #                     helper4(digits[i], digits[j], digits[k], digits[l])
    
    # return res