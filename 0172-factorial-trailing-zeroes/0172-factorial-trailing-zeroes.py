class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        ans = 0
        i = 5
        
        while n / i > 0:
            cur = n // i
            ans += cur
            i *= 5
        
        return ans