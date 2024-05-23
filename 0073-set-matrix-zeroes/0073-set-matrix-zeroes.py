class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = {'rows':[], 'cols':[]}
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    res['rows'].append(i)
                    res['cols'].append(j)
        for i in range(rows):
            for j in range(cols):
                if i in res['rows'] or j in res['cols']:
                    matrix[i][j] = 0
