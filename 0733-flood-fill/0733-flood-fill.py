class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return image
        
        q = deque()
        rows, cols = len(image), len(image[0])
        q.append((sr, sc))
        srColor = image[sr][sc]
        
        if srColor == color:
            return image
        
        direction = [[1,0], [0,1], [-1, 0], [0,-1]]
        image[sr][sc] = color
        while q:
            
            for _ in range(len(q)):
                
                r, c = q.popleft()
                for dr, dc in direction:
                    row, col = dr + r, dc + c
                    
                    if row in range(rows) and col in range(cols) and image[row][col] == srColor:
                        image[row][col] = color
                        q.append((row, col))
        
        return image
            