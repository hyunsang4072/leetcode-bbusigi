# def rotate(self, matrix: List[List[int]]) -> None:
#     """
#     Do not return anything, modify matrix in-place instead.
#     [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
#     rotate(...)
#     [
#         [7, 4, 1],
#         [8, 5, 2],
#         [9, 6, 3]
#     ]
#     """
#     temp = matrix[-1]

#     for i in range(len(matrix[0])):
#         matrix.append([temp[i]])

#     # print(matrix)

#     # reversed
#     for i in reversed(matrix[:len(matrix[0])]):
#         for j in range(len(matrix[0])):
#             if i[j] not in matrix[len(matrix[0])+j]:
#                 matrix[len(matrix[0])+j].append(i[j])

#     # print(matrix)

#     # cut front
#     count = 0
#     for i in matrix[len(matrix[0]):]:
#         matrix[count] = i
#         matrix.pop()
#         count += 1

def rotate(self, matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate(...)
    [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    """
    # strategy:
    # 1. transpose: two different ways; either works
    # 2. reverse each row
    n = len(matrix[0])

    # 1st way of transposing the matrix, using seen list
    # seen = []
        # for i in range(n):
        #     for j in range(n):
        #         if (i,j) not in seen:
        #             seen.append((j,i))
        #             temp = matrix[i][j]
        #             matrix[i][j] = matrix[j][i]
        #             matrix[j][i] = temp
        #         else:
        #             continue

    # 2nd way of transposing the matrix; faster than 1st approach
    for i in range(n):
        for j in range(n - i):
            temp = matrix[i][j+i]
            matrix[i][j+i] = matrix[j+i][i]
            matrix[j+i][i] = temp
    
    # reverse each row
    for i in matrix:
        i.reverse()
