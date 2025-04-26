def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # the idea is that we treat this matrix as a single array
    # this only works if the given matrix is sorted in order
    # [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

    # find 11
    # we know rowNum, colNum = 3, 4
    # l, r = 0, (rowNum * colNum) - 1; -1 to avoid indexOutOfBounds err
    # m = (l + r) // 2 = 5
    # r, c = m // 4=colNum, m % 4=colNum
    #      = 1, 1

    row, col = len(matrix), len(matrix[0]) # row x col matrix
    l, r = 0, (row * col) - 1 # treat this matrix like 1d-arr

    # normal binary search -> O(logn)
    while l <= r:
        m = (l + r) // 2
        el = matrix[m // col][m % col]

        if el > target:
            r = m - 1
        elif el < target:
            l = m + 1
        else:
            return True
    
    return False