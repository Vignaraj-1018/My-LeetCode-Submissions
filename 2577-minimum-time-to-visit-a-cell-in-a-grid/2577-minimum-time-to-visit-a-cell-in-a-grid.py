class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1], grid[1][0]) > 1:
            return -1
        
        minheap = [(0, 0, 0)]
        m, n = len(grid), len(grid[0])
        visit = set()
        
        while minheap:
            t, r, c = heapq.heappop(minheap)
            
            if (r, c) == (m - 1, n - 1):
                return t
            
            directions = [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]
            for nr, nc in directions:
                if nr < 0 or nr == m or nc < 0 or nc == n or (nr, nc) in visit:
                    continue
                wait = 0
                if abs(grid[nr][nc] - t) % 2 == 0:
                    wait = 1
                
                new_t = max(grid[nr][nc] + wait, t + 1)
                heapq.heappush(minheap, (new_t, nr, nc))
                visit.add((nr, nc))