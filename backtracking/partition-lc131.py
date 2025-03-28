def partition(self, s: str) -> List[List[str]]:
    # TC: O(n * 2^n)
    # SC: O(n * 2^n) space for the output list
    res = []
    subset = []

    def helper(i):
        # TODO: recursively generate all panlidromes
        # Base case: we've reached the end of the string
        if i >= len(s): 
            res.append(subset.copy())
            return
        
        # Try every possible end index j from i to end of string
        for j in range(i, len(s)):
            if self.isPalindrome(s, i, j):    # If s[i:j+1] is a palindrome
                subset.append(s[i:j+1])       # Choose (add to path)
                helper(j + 1)                 # Explore further with next index
                subset.pop()                  # Backtrack (remove last choice)

    # call helper function
    helper(0)

    return res

def isPalindrome(self, s, i, j) -> bool:
    if not s: return False
    
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    
    return True