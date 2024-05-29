class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh_oranges = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        if fresh_oranges == 0:
            return 0

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        time_units = 0

        while q:
            time_units += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh_oranges -= 1

        return time_units - 1 if fresh_oranges == 0 else -1