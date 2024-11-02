def maxSubArray(nums: list[int]) -> int:
    # use Kadane's Algorithm
    # don't carry negative currSum forward
    # only add to results if after adding, still positive value
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