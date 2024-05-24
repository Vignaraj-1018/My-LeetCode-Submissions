class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumOfSquares(n):
            res = 0
            
            while n>0:
                digit  = n % 10
                digit = digit ** 2
                res += digit
                n //= 10
            
            return res
        
        s, f = n, n
        
        while True:
            
            s = sumOfSquares(s)
            f = sumOfSquares(sumOfSquares(f))
            
            
            
            if s == 1 or f == 1:
                return True
            
            if s == f:
                return False