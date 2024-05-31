class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        
        visit = set()
        
        def bfs(r, c):
            
            q = []
            visit.add((r,c))
            q.append((r,c))
            fish = grid[r][c]
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            
            while q:
                r, c = q.pop(0)
                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    if row in range(rows) and col in range(cols) and (row, col) not in visit and grid[row][col] > 0:
                        visit.add((row, col))
                        q.append((row, col))
                        fish += grid[row][col]

            return fish
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visit and grid[i][j] > 0:
                    res = max(res, bfs(i,j))
                    
        return res