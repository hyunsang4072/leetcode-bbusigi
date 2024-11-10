def myPow(self, x: float, n: int) -> float:
    # find x^n
    # use recursion
    def helper(b, e):
        # base cases
        if e == 0: return 1 # anything raised to 0 is 1
        if b == 0: return 0 # 0^e is always 0

        # we want to recurse towards our base case
        ans = helper(b * b, e // 2)

        return ans * b if e % 2 else ans

    # since n can be a negative value
    # we avoid such edge cases by taking the absolute value of n
    # account for negative n when we return
    res = helper(x, abs(n))

    # x^-n = 1/(x^n)
    return res if n >= 0 else 1 / res