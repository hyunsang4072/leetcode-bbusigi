def maxSubArray(nums: list[int]) -> int:
    maxSum = -float("inf") # -inf
    currSum = 0
    # currElem = []

    for i in range(len(nums)):
        currSum += nums[i]

        if maxSum < currSum:
            maxSum = currSum
        
        if currSum < 0:
            currSum = 0
    
    # print(currElem)

    return maxSum