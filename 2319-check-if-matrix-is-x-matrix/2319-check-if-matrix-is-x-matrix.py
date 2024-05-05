class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if i==j and grid[i][j] == 0:
                    return False
                elif j == n-i-1 and grid[i][j] == 0:
                    return False
                elif i!=j and j != n-i-1 and grid[i][j]!=0:
                    return False
        
            
        
        return True