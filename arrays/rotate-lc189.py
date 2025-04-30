def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # TC: O(n)
    # SC: O(1) -> in-place
    if len(nums) == 1 or k == 0:
        return
    
    k %= len(nums)
    
    def reverse(i, j, arr):
        while i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1

    reverse(0, len(nums) - 1, nums)
    reverse(0, k - 1, nums)
    reverse(k, len(nums) - 1, nums)
