def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2 # used for indexing

    # let A, B = shortArr, longArr
    if len(nums1) > len(nums2):
        A, B = nums2, nums1
    
    # run binary search on A(short)
    l, r = 0, len(A) - 1
    while True: # i'm not sure why we don't use l <= r
        i = (l + r) // 2 # m for A
        j = half - (i + 1) - 1 # m for B

        # retrieve element at each index
        ALeft = A[i] if i >= 0 else float("-inf")
        BLeft = B[j] if j >= 0 else float("-inf")
        ARight = A[i + 1] if (i + 1) < len(A) else float("inf")
        BRight = B[j + 1] if (j + 1) < len(B) else float("inf")

        if BLeft <= ARight and ALeft <= BRight:
            # we found the correct left,right partitions
            # total length is odd
            if total % 2:
                return min(ARight, BRight)
            return (min(ARight, BRight) + max(ALeft, BLeft)) / 2
        elif ALeft > BRight:
            r = i - 1
        else:
            l = i + 1

    # we don't have to return anything ourselves
    # since we are guaranteed to find the median value