class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDig = set()
        negDig = set()

        res = []
        board = [['.'] * n for _ in range(n)]

        def backTrack(r):

            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            
            for c in range(n):
                if c in col or (r-c) in negDig or (r+c) in posDig:
                    continue
                
                col.add(c)
                posDig.add(r+c)
                negDig.add(r-c)
                board[r][c] = 'Q'

                backTrack(r+1)

                col.remove(c)
                posDig.remove(r+c)
                negDig.remove(r-c)
                board[r][c] = '.'

                
        backTrack(0)

        return res