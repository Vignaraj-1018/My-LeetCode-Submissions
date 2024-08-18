class Solution:
    def isUgly(self, n: int) -> bool:
        
        factors = [2, 3, 5]
        i = 0
        while i < 3 and n:
            if not n % factors[i]:
                n /= factors[i]
            else:
                i += 1
        
        if n != 1:
            return False
        return True