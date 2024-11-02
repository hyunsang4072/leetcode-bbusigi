# def sortColors(self, nums: list[int]) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     # better solution --> O(2N) == O(N); ignore constants
#     count = [0]*3 # [count0, count1, count2]

#     for i in range(len(nums)):
#         curr = nums[i]
#         if curr == 0:
#             count[0] += 1
#         elif curr == 1:
#             count[1] += 1
#         else:
#             count[2] += 1
    
#     for i in range(count[0]):
#         nums[i] = 0
    
#     for i in range(count[1]):
#         nums[i+count[0]] = 1
    
#     for i in range(count[2]):
#         nums[i+count[0]+count[1]] = 2

def sortColors(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # optimal solution --> O(N)
    # Dutch National Flag(DNF) Algorithm
    # assume before low and after high are sorted properly
    # (sorted) ...low | mid (unsorted) ... | high... (sorted)
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0: # send to low
            temp = nums[low]
            nums[low] = nums[mid]
            nums[mid] = temp
            low += 1
            mid += 1
        elif nums[mid] == 1: # sorted so move to next
            mid += 1
        elif nums[mid] == 2: # send to high
            temp = nums[mid]
            nums[mid] = nums[high]
            nums[high] = temp
            high -= 1