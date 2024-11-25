def twoSum(self, numbers: list[int], target: int) -> list[int]:
    '''
    use two pointers: one at the beginning, the other one at the end
    each iteration, if sum is too big, decrement right ptr; else, increment left ptr
    add one to each index for the return value due to problem specification
    '''
    l, r = 0, len(numbers) - 1

    while l != r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        elif s < target:
            l += 1
        elif s > target:
            r -= 1