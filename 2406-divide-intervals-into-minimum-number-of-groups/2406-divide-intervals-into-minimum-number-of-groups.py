class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        
        for l, r in intervals:
            start.append(l)
            end.append(r)
        
        start.sort()
        end.sort()
        
        i, j = 0, 0
        res = 0
        grps = 0
        
        while i < len(intervals):
            if start[i] <= end[j]:
                grps += 1
                i += 1
            else:
                grps -= 1
                j += 1
            
            res = max(res, grps)
        
        return res