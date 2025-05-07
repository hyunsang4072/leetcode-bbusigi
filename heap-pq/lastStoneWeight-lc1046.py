def lastStoneWeight(self, stones: List[int]) -> int:
    # heapq.heapify(list): Transforms a list into a heap, in-place.
    # heapq.heappush(heap, item): Adds an element to the heap.
    # heapq.heappop(heap): Removes and returns the smallest element from the heap.
    # heapq.nlargest(n, iterable, key=None): Returns a list with the n largest elements from the dataset.
    # heapq.nsmallest(n, iterable, key=None): Returns a list with the n smallest elements from the dataset.
    for i in range(len(stones)):
        stones[i] = -stones[i]
    
    # python's default heap == minHeap
    # negate each elem --> maxHeap
    heapq.heapify(stones) # maxHeap = [-8, -7, -4, -2, -1, -1]
    
    while len(stones) >= 2:
        y = heapq.heappop(stones) # -8
        x = heapq.heappop(stones) # -7
        if x == y:
            continue
        else:
            y -= x
            heapq.heappush(stones, y)
    
    # if input arr is empty, or we destroyed all stones
    return -stones[0] if stones else 0