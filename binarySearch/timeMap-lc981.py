class TimeMap:
    from collections import defaultdict

    def __init__(self):
        self.timeStore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, pairs = "", self.timeStore[key]
        # pairs: [[v1, t1], ..., [vn, tn]]
        
        l, r = 0, len(pairs) - 1
        while l <= r:
            m = (l + r) // 2

            # pairs: [val, time]
            # if case can achieve two things:
            # 1) find the exact match if it exists
            # 2) get closer to the target as much as possible(think range)
            if pairs[m][1] <= timestamp:
                res = pairs[m][0]
                l = m + 1
            else: # if not found search left until we eliminate all elements or find the target
                r = m - 1
        
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)