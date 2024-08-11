class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c, visit):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0 or (r, c) in visit:
                return
            
            visit.add((r, c))
            neighbors = [[r + 1, c], [r, c + 1], [r - 1, c], [r, c - 1]]
            for nr, nc in neighbors:
                dfs(nr, nc, visit)
                
            
        def helper():
            visit = set()
            count = 0
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] and (r, c) not in visit:
                        dfs(r, c, visit)
                        count += 1
            
            return count
        
        if helper() != 1:
            return 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    grid[r][c] = 0
                    if helper() != 1:
                        return 1
                    grid[r][c] = 1
        
        return 2
