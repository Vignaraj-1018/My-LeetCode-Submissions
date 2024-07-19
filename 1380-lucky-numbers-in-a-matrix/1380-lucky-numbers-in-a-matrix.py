class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        maxCols, res = [], []
        for i in range(n):
            maxCols.append(max(matrix[j][i] for j in range(m)))
        for i in range(m):
            minRow, colIndex = matrix[i][0], 0
            for j in range(1, n):
                if matrix[i][j] < minRow:
                    minRow, colIndex = matrix[i][j], j
            if minRow == maxCols[colIndex]:
                res.append(minRow)
        return res