class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        R1, C1 = len(grid), len(grid[0])
        R2, C2 = 3 * R1, 3 * C1
        
        grid2 = [[0] * C2 for _ in range(R2)]
        
        for r in range(R1):
            for c in range(C1):
                r2, c2 = 3 * r, 3 * c
                if grid[r][c] == '/':
                    grid2[r2][c2 + 2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2] = 1
                elif grid[r][c] == "\\":
                    grid2[r2][c2] = 1
                    grid2[r2 + 1][c2 + 1] = 1
                    grid2[r2 + 2][c2 + 2] = 1
                    
        def dfs(r, c, visit):
            if r < 0 or c < 0 or r == R2 or c == C2 or (r, c) in visit or grid2[r][c] == 1:
                return
            
            visit.add((r, c))
            directions = [[r, c + 1], [r + 1, c], [r - 1, c], [r, c - 1]]
            for dr, dc in directions:
                dfs(dr, dc, visit)
        
        res = 0
        visit = set()
        for r in range(R2):
            for c in range(C2):
                if grid2[r][c] != 1 and (r, c) not in visit:
                    dfs(r, c, visit)
                    res += 1
        return res