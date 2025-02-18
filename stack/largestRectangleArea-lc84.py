def largestRectangleArea(self, heights: list[int]) -> int:
    maxArea = 0
    stack = [] # pair: [index, height]

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h: # compare heights
            # if next bar shorter than current bar, pop it from stack
            index, height = stack.pop()
            area = height * (i - index) # height * width
            maxArea = max(maxArea, area)
            # we don't want to keep the current index
            # we want to extend the starting point for current bar
            # until we get to the last popped element (go backwards)
            # this is so that when we iterate through the stack later
            # we can compute the areas for rectangles that are laying down |_____|
            start = index # last popped index
        stack.append((start, h))
    
    # iterate through leftover elements in stack
    for i, h in stack:
        area = h * (len(heights) - i)
        maxArea = max(maxArea, area)
    
    return maxArea