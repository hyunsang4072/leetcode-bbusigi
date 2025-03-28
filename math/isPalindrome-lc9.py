def isPalindrome(self, x: int) -> bool:
    if x < 0: return False
    n = x
    reversed_n = 0

    while n != 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n //= 10
    
    return reversed_n == x

    ####### String Approach #######
    # s = str(x)

    # l, r = 0, len(s) - 1

    # while l <= r:
    #     if s[l] != s[r]:
    #         return False
    #     l += 1
    #     r -= 1
    
    # return True