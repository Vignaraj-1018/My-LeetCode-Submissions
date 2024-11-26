class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n
        
        for s, d in edges:
            incoming[d] += 1
        
        res = []
        cnt = 0
        for i, c in enumerate(incoming):
            if c == 0: 
                res.append(i)
                cnt += 1
                if cnt > 1:
                    return -1
    
        return res[0]