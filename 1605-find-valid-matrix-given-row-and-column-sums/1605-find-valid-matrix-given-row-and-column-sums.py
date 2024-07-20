class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)

        res = [[0] * m for _ in range(n)]

        for r in range(n):
            res[r][0] = rowSum[r]

        for c in range(m):
            cur = 0
            for r in range(n):
                cur += res[r][c]
            
            r = 0
            while cur > colSum[c]:
                diff = cur - colSum[c]
                maxShift = min(res[r][c], diff)

                res[r][c] -= maxShift
                res[r][c+1] += maxShift
                cur -= maxShift
                r += 1
            
        return res