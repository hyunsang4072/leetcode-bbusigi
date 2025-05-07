class KthLargest:

    def __init__(self, k: int, nums: List[int]) -> None:
        # TC: O(mlogk), m = # of add() calls made
        # SC: O(k)
        self.my_heap = nums
        self.k = k
        heapq.heapify(self.my_heap)
        while len(self.my_heap) > k: # keep k elements
            heapq.heappop(self.my_heap)

    def add(self, val: int) -> int: # TC: O(logk)
        # self.my_heap[0] = smallest
        # since we maintain only k elements in our minHeap
        # smallest in our minHeap will be k-th largest element
        heapq.heappush(self.my_heap, val)
        if len(self.my_heap) > self.k: # don't pop if less than k elements
            heapq.heappop(self.my_heap)
        
        # return self.my_heap[-self.k]
        return self.my_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)