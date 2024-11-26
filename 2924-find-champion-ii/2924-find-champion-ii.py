class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0] * n
        
        for s, d in edges:
            incoming[d] += 1
        
        res = []
        for i, c in enumerate(incoming):
            if c == 0: 
                res.append(i)
    
        return -1 if len(res) > 1 else res[0]