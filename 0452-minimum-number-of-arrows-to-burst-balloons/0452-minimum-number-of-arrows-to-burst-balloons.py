class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        res = len(points)
        
        points.sort()
        
        prev = points[0]
        
        for i in range(1, len(points)):
            
            cur = points[i]
            
            if cur[0] <= prev[1]:
                res -= 1
                prev = [cur[0], min(cur[1], prev[1])]
            
            else:
                prev = cur
        
        return res