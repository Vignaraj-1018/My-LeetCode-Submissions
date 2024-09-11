class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        n = start ^ goal
        
        while n:
            n = (n - 1) & n
            res += 1
            
        return res