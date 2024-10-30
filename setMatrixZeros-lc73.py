def setZeroes(self, matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    Input: matrix = 
        [[1,1,1],
         [1,0,1],
         [1,1,1]]
    Output: 
        [[1,0,1],
         [0,0,0],
         [1,0,1]]
    """

    # brute force solution(bad!!!)
    # def setZeroes(self, matrix: list[list[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     rows = len(matrix)
    #     cols = len(matrix[0])

    #     # memo = {}
    #     for i in range(rows):
    #         for j in range(cols):
    #             curr_cell = matrix[i][j]
    #             if curr_cell == 0:
    #                 # memo[i] = (i, j)
    #                 indexRow = 0
    #                 while indexRow < rows: # rather than 0, set it to 0.5 so that it won't be reused for later iterations
    #                     matrix[indexRow][j] = 0.5 if matrix[indexRow][j] != 0 else 0
    #                     indexRow += 1
    #                 indexCol = 0
    #                 while indexCol < cols: # rather than 0, set it to 0.5 so that it won't be reused for later iterations
    #                     matrix[i][indexCol] = 0.5 if matrix[i][indexCol] != 0 else 0
    #                     indexCol += 1
                    
    #     for i in range(rows):
    #         for j in range(cols):
    #             if matrix[i][j] == 0.5:
    #                 matrix[i][j] = 0


    # better solution(not optimal)
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        basically, this time we have two extra arrays to mark all rows and cols that contain at least one zero.
        on the second iteration, we fill those "marked" rows and cols with all zeros.
        """
        rows = len(matrix)
        # mark rows that contain zero
        arr_rows = [0] * rows
        cols = len(matrix[0])
        arr_cols = [0] * cols

        # memo = {}
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    # mark each index
                    arr_rows[i] = 1
                    arr_cols[j] = 1
        
        # fill with zeros
        for i in range(len(arr_rows)):
            for j in range(len(arr_cols)):
                if arr_rows[i] == 1 or arr_cols[j] == 1:
                    matrix[i][j] = 0