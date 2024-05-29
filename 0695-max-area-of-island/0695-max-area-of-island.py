class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0
        
        def bfs(r, c):
            q = []
            visit.add((r,c))
            q.append((r,c))
            count = 1
            
            while q:
                row, col = q.pop(0)
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c]==1 and (r,c) not in visit):
                        visit.add((r,c))
                        q.append((r,c))
                        count+=1
            # print(count)
            return count
            
        max_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    max_count = max(max_count, bfs(r,c))
                    
        return max_count