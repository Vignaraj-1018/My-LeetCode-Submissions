class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        
        def canPlace(mid):
            cnt = 1
            lst = position[0]
            for i in range(len(position)):
                if position[i] - lst >= mid:
                    cnt += 1
                    lst = position[i]
                if cnt >= m:
                    return True
            
            return False
                    
                
        lo, hi = 1, (position[-1] - position[0]) // (m - 1)
        ans = 1
        while lo <= hi:
            
            mid = (lo + hi) // 2
            
            if canPlace(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans