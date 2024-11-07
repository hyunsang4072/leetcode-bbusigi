def merge(self, intervals: list[list[int]]) -> list[list[int]]:
    # res = []
    # used = [0] * len(intervals)

    # # print(sorted([[15,18],[1,3],[2,6],[8,10]]))
    # # >>> [[1, 3], [2, 6], [8, 10], [15, 18]]
    # optimal solution --> TC = O(NlogN) + O(N)
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    res = []

    intervals = sorted(intervals) # returns a sorted list
    # intervals = [[1,3],[2,6],[8,10],[15,18]]
    n = len(intervals)

    for i in range(n):
        if len(res) == 0 or intervals[i][0] > res[-1][1]:
            res.append(intervals[i])
        else:
            res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]

    return res