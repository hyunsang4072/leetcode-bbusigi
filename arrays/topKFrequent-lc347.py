def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    # Sorting method --> O(nlogn)
    # res = []
    # seen = {}

    # for n in nums:
    #     seen[n] = seen.get(n, 0) + 1

    # seen = sorted(seen.items(), key=lambda x: x[1])

    # c = -1

    # while k != 0:
    #     res.append(seen[c][0])
    #     c -= 1
    #     k -= 1
    
    # return res

    # modified Bucket Sort(original uses indices as actual vals)
    # time: O(n)
    res = []
    arr = [[] for i in range(len(nums))] # arr where ind=count, vals=num
    # arr = [[]] * len(nums) <-- DO NOT DO THIS!!!
    seen = {}

    # create frequency map
    for n in nums:
        seen[n] = seen.get(n, 0) + 1
    
    # arr needed for modified bucket sort
    for i in seen:
        arr[seen[i]-1].append(i)
    
    for subArr in arr[::-1]: # reversing the arr since largest to smallest freq.
        if not subArr:
            continue
        for el in subArr:
            res.append(el)
            k -= 1
            if k == 0: # stop when k elemnts found
                return res