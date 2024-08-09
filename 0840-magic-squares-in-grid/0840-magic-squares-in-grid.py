class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        pat1 = '438167294381672'
        pat2 = '927618349276183'
        
        def helper(r, c):
            
            if grid[r][c] != 5:
                return 0
            
            neighbours = [
                [r - 1, c], [r - 1, c + 1],
                [r, c + 1], [r + 1, c + 1],
                [r + 1, c], [r + 1, c - 1],
                [r, c - 1], [r - 1, c - 1]
            ]
            s = ''
            for nr, nc in neighbours:
                s = s + str(grid[nr][nc])
            
            if s in pat1 or s in pat2:
                return 1
            
            return 0
                
            
        
        res = 0
        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                res += helper(r, c)
                                                    
        return res