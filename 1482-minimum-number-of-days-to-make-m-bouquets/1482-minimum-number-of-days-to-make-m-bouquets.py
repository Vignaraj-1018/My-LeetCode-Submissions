class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1
        
        def isPossible(day):
            cnt, res = 0, 0
            for i in range(n):
                if bloomDay[i] <= day:
                    cnt+=1
                else:
                    res += cnt//k
                    cnt=0
            
            res += cnt//k
            if res >= m:
                return True
            return False
                    
        res = 0
        minDay, maxDay = min(bloomDay), max(bloomDay)
        res= 0
        while minDay < maxDay:
            mid = (minDay + maxDay)//2
            if isPossible(mid):
                maxDay = mid
            else:
                minDay = mid + 1
        
        return minDay
        