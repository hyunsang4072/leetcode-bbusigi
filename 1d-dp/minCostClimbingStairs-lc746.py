def minCostClimbingStairs(self, cost: List[int]) -> int:
    # DP w/ space optimization (by using the given arr)
    # TC: O(n)
    # SC: O(1)
    # cost: [10, 15, 20]
    # add dummy value to the cost arr
    # to deal w/ IndexOutOfBounds err
    cost.append(0) # cost: [10, 15, 20] 0

    # iterate through arr in reverse order
    # len(cost) - 3: because, we can take one or two steps + extra 0 at the end
    # each iteration add the current cost value to the minimum of
    # next two costs(emulate taking one or two steps)
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])
    
    # print(cost)
    
    # return whether we take start from index 0 or
    # start from index 1
    return min(cost[0], cost[1])


    ####### brute force w/ memoization #######
    # TC: O(n)
    # SC: O(n)
    # res = 0
    # seen = {}

    # def dfs(i):
    #     if i >= len(cost):
    #         return 0

    #     if (i + 1) in seen and (i + 2) in seen:
    #         one, two = seen[i + 1], seen[i + 2]
    #         return cost[i] + min(one, two)
        
    #     one, two = dfs(i + 1), dfs(i + 2)
    #     seen[i + 1] = one
    #     seen[i + 2] = two

    #     return cost[i] + min(one, two)
    
    # return min(dfs(0), dfs(1))