def isPalindrome(self, s: str) -> bool:
    combined = (''.join(x for x in s if x.isalnum())).lower()

    l, r = 0, len(combined) - 1

    while l < r:
        if combined[l] != combined[r]:
            return False
        l += 1
        r -= 1

    return True