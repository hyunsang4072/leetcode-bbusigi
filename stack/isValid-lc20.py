def isValid(self, s: str) -> bool:
    # use stack to get a list of opening parentheses
    # when we encounter a closing parenthesis,
    # check last element
    if (len(s) % 2) != 0: # more optimizations, i guess
        return False
    
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for i in s:
        if i in pairs:
            last = stack[-1] if stack else None
            if pairs[i] != last:
                return False
            stack.pop()
        else:
            stack.append(i)
    
    if stack:
        return False
    
    return True