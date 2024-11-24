class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        abs_min = float('inf')
        cnt = 0
        
        for row in matrix:
            for n in row:
                abs_min = min(abs(n), abs_min)
                res += abs(n)
                if n < 0:
                    cnt += 1
        
        if cnt % 2:
            res -= 2 * abs_min
        
        return res
                    