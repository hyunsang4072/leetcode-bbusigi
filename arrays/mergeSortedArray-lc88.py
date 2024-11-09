def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    n = len(nums2)

    for i in range(n):
        nums1[i+m] = nums2[i]
    
    nums1.sort()