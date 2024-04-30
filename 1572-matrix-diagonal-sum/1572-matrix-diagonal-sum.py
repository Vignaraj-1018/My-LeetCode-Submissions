class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        n = len(mat)
        for i in range(n):
            res += mat[i][i]
            if i != n-i-1:
                res += mat[i][n-i-1]
        
        return res