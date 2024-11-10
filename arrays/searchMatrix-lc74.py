def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    l, r = 0, len(matrix) - 1
    row = 0 # // --> floor div
    
    while l <= r:
        m = (l+r) // 2
        
        if matrix[m][0] > target:
            r = m - 1
        elif matrix[m][0] <= target and matrix[m][-1] >= target:
            row = m
            break
        else:
            l = m + 1
    
    # m should contain the row index of list that contains the target

    l, r = 0, len(matrix[row]) - 1

    while l <= r:
        mi = (l+r) // 2 # 1
        val = matrix[row][mi]
        print(val)

        if val > target:
            r = mi - 1
        elif val < target:
            l = mi + 1
        else:
            return True

    return False