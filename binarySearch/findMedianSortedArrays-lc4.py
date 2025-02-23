def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    # TC: O(log(min(n, m)))
    # SC: O(1)
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2 # integer division

    # we want A to be smaller than B
    if len(B) < len(A):
        A, B = B, A
    
    l, r = 0, len(A) - 1
    while True: # finding a median is guaranteed
        i = (l + r) // 2 # middle point of A
        j = half - i - 2 # middle point of B

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i+1] if (i+1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j+1] if (j+1) < len(B) else float("infinity")

        # partition is correct
        if Aleft <= Bright and Bleft <= Aright:
            # odd of elements
            if total % 2: # 1 is True in Python
                return min(Aright, Bright)
            # even
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else: # Bleft <= Aright is False
            l = i + 1