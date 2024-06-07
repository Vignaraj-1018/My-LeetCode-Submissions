class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        path = []
        
        def dfs(i):
            if len(path) == k:
                res.append(path.copy())
                return
            
            for j in range(i, n+1):
                path.append(j)
                dfs(j+1)
                path.pop()
        
        dfs(1)
        return res