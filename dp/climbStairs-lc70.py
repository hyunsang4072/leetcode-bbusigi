def climbStairs(self, n: int) -> int:
    # at least for this problem, where the maximum step
    # we can take is 2, the first and second will always have
    # default value of two
    first, second = 1, 1
    
    # e.g., n = 5
    # visualize an arr like this: [0, 0, 0, 0, 0, 0] since 0 up to 5
    # we need to think about our base cases so we start from the end of an arr
    # i.e., [0, 0, 0, 0, 1, 1] where last two indices contain second and first
    # start building up the arr woking towards the beginning of our arr
    # i.e., [0, 0, 0, 2, 1, 1]
    # i.e., [0, 0, 3, 2, 1, 1]
    # i.e., [0, 5, 3, 2, 1, 1]
    # i.e., [8, 5, 3, 2, 1, 1]
    # notice how we don't really need the last step where we computed 8
    # so we can just do this in (n - 1) iterations!
    for i in range(n - 1):
        temp = second
        second = first + second
        first = temp
        # or w/o using temp variable can be done as follows:
        # second = first + second
        # first = second - first
    
    return second

    ####### dp w/ bottom-up #######
    # TC: O(n)
    # SC: O(n)
    # if n <= 2:
    #     return n
    
    # dp = [0] * (n + 1) # e.g., [0, 0, 0, 0]
    # dp[1], dp[2] = 1, 2 # e.g., [0, 1, 2, 0]

    # for i in range(3, n + 1):
    #     dp[i] = dp[i - 2] + dp[i - 1] # e.g., if n==4: [0, 1, 2, 3, 5]
    
    # return dp[n]