def trap(self, height: list[int]) -> int:
    # TC = O(n)
    # SC = O(n) <-- not optimal; can be optimized further
    # res = 0

    # maxL = [0] * len(height)
    # maxR = [0] * len(height)

    # l = 0
    # for i in range(len(height)):
    #     h = height[i]
    #     l = max(l, h)
    #     maxL[i] = l
    # r = 0
    # for j in range(len(height)-1, -1, -1):
    #     h = height[j]
    #     r = max(r, h)
    #     maxR[j] = r
    
    # for i in range(len(height)):
    #     curr = min(maxL[i], maxR[i]) - height[i]
    #     res += curr
    
    # return res

    # TC = O(n)
    # SC = O(1) <-- optimal soln.
    # formula used for this question is: min(height[l], height[r]) - height[i]
    res = 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    
    return res