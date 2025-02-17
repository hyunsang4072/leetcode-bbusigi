def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    # brute force --> TLE == bad!!!
    # res = [0] * len(temperatures)
    # for i in range(len(temperatures)):
    #     j = i + 1
    #     c = 1
    #     while j < len(temperatures):
    #         if temperatures[i] < temperatures[j]:
    #             res[i] = c
    #             break
    #         else:
    #             j += 1
    #             c += 1
    
    # return res


    # optimal soln. using stack
    # TC: O(n)
    # SC: O(n)
    stack = []
    res = [0] * len(temperatures)

    for i, t in enumerate(temperatures): # [index, temperature]
        while stack and t > stack[-1][1]: # compare temps
            stackInd, stackT = stack.pop() # unZipping
            res[stackInd] = i - stackInd
        # continue adding temps that are less than
        # temp that's on top of our stack
        stack.append([i, t])

    return res