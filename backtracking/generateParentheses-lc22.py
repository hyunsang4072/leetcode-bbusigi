def generateParenthesis(self, n: int) -> list[str]:
    # 1. keep track of two variables: open, close
    # 2. valid combination if close < open
    # use backtracking to get valid parentheses combination
    # Algorithm:
    # - only add open parenthesis if open < n
    # - only add closing parenthesis if close < open
    # - stop when open == close == n
    
    # approach1 using string --> not optimal, but easier to comprehend
    res = []

    def backTrack(openN, closedN, path):
        if openN == closedN == n: # base case --> found a valid combination
            res.append(path)
            return
        
        if closedN < openN: # add a closing parenthesis
            # path += ")" <-- this doesn't work!!!
            backTrack(openN, closedN + 1, path + ")")
        
        if openN < n: # add a open parenthesis
            # path += "(" <-- this doesn't work!!!
            backTrack(openN + 1, closedN, path + "(")
    
    backTrack(0, 0, "")

    return res

    # approach2 using stack --> better soln.
    # stack = []
    # res = []

    # def backtrack(openN, closedN):
    #     if openN == closedN == n:
    #         res.append("".join(stack))
    #         return

    #     if openN < n:
    #         stack.append("(")
    #         backtrack(openN + 1, closedN)
    #         stack.pop()
    #     if closedN < openN:
    #         stack.append(")")
    #         backtrack(openN, closedN + 1)
    #         stack.pop()

    # backtrack(0, 0)
    # return res