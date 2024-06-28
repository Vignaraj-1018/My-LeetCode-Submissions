class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edge_cnt = [0] * n
        
        for n1, n2 in roads:
            edge_cnt[n1] += 1
            edge_cnt[n2] += 1
        
        l = 1
        res = 0
        for c in sorted(edge_cnt):
            res += l * c
            l += 1
            
        return res
        
        