class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS, COLS = len(grid1), len(grid1[0])
        visit = set()
        
        def dfs(r, c):
            
            if r not in range(ROWS) or c not in range(COLS) or grid2[r][c] == 0 or (r, c) in visit:
                return True
            
            visit.add((r, c))
            res = True
            if grid1[r][c] == 0:
                res = False
            
            res = dfs(r + 1, c) and res
            res = dfs(r - 1, c) and res
            res = dfs(r, c + 1) and res
            res = dfs(r, c - 1) and res
            
            return res
            
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid2[i][j] and (i, j) not in visit and dfs(i, j):
                    res += 1
        return res