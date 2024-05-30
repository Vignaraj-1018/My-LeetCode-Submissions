class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(mat), len(mat[0])
        visited = [[0] * cols for _ in range(rows)]
        dist = [[0] * cols for _ in range(rows)]
        
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i,j,0))
                    visited[i][j] = 1
                else:
                    visited[i][j] = 0
        
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        
        
        while q:
            
            r, c, st = q.popleft()
            dist[r][c] = st
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr,nc,st+1))
            
        
        return dist