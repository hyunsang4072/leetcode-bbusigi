def rob(self, nums: List[int]) -> int:
    # optimal approach w/ space optimization
    # TC: O(n)
    # SC: O(n) due to list slicing in Python
    return max(nums[0], self.helpRob(nums[1:]), self.helpRob(nums[:-1]))

def helpRob(self, street): # lc198 House Robber I problem
    rob1, rob2 = 0, 0

    # [rob1, rob2, street[i], street[i+1], ...]
    for i in range(len(street)):
        temp = max(street[i] + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    
    return rob2

####### my approach #######
# TC: O(n)
# SC: O(n)
#     if len(nums) < 2:
#         return nums[0]
    
#     first, second = self.helpRob(nums[:-1]), self.helpRob(nums[1:])
#     return max(first, second)

# def helpRob(self, street):
#     street.append(0)
#     # street = [2, 3, 2] 0

#     for i in range(len(street) - 3, -1, -1):
#         street[i] = max(street[i] + street[i + 2], street[i + 1])

#     return street[0]