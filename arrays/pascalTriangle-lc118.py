def generate(self, numRows: int) -> list[list[int]]:
    '''
    1 = [[1]]
    2 = [[1], [1,1]]
    3 = [[1], [1,1], [1, 2, 1]]
    '''
    res = [[numRows]]
    
    if numRows == 1:
        return res
    elif numRows == 2:
        res = [[1]] + [[1, 1]]
        return res
    
    res = [[1]] + [[1, 1]]
    numIter = numRows - 2
    for i in range(numIter):
        prev = res[i+1]
        curr = [1]
        for j in range(i+1):
            curr += [prev[j] + prev[j+1]]
        curr += [1]
        res += [curr]
    
    return res