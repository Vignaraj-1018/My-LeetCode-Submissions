class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -(1 << 31) and divisor == -1:
            return (1 << 31) - 1
        
        sign = (dividend >= 0) == (divisor >= 0)
        a = abs(dividend)
        b = abs(divisor)
        
        res = 0
        while a - b >= 0:
            cnt = 0
            while a - (b << 1 << cnt) >= 0:
                cnt += 1
            res += 1 << cnt
            a -= b << cnt
        
        return res if sign else -res