class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n == 0:
                return 1
            
            return n * factorial(n-1)
        
        fact = factorial(n)
        
        cnt = 0
        while fact % 10 == 0:
            cnt+=1
            fact //=10
            
        return cnt