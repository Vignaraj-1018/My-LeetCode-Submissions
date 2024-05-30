class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]        
        pathVisited = [[False] * cols for _ in range(rows)]
        
        def dfs(r, c, fr, fc, char):
            
            visited[r][c] = True
            pathVisited[r][c] = True
            
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                
                if nr in range(rows) and nc in range(cols) and grid[nr][nc]==char:
                    if not visited[nr][nc]:
                        if dfs(nr, nc, r, c, char):
                            return True
                    elif pathVisited[nr][nc] and (nr != fr or nc != fc):
                        return True
            
            pathVisited[r][c] = False
            return False
        
        
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    if dfs(i,j,-1,-1,grid[i][j]):
                        return True
        
        return False