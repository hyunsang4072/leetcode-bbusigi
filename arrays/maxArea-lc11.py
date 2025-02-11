def maxArea(self, height: list[int]) -> int:
    # two pointers to find max area
    area = 0

    l, r = 0, len(height) - 1

    while l < r:
        w = r - l
        h = min(height[l], height[r])
        area = max(area, w*h)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    
    return area