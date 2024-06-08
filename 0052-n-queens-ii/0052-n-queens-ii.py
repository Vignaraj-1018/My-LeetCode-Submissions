class Solution:
    def totalNQueens(self, n: int) -> int:
        res = [0]
        board = [['.'] * n for _ in range(n)]

        col =set()
        posDig = set()
        negDig = set()

        def dfs(r):

            if r == n:
                res[0]+=1
                return

            for c in range(n):

                if c in col or (r+c) in posDig or (r-c) in negDig:
                    continue

                col.add(c)
                posDig.add(r+c)
                negDig.add(r-c)

                board[r][c] = 'Q'
                dfs(r+1)

                col.remove(c)
                posDig.remove(r+c)
                negDig.remove(r-c)

        dfs(0)
        return res[0]

