class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = len(digits) - 1
        cur = 1
        
        while i >= 0 and cur:
            cur += digits[i]
            digits[i] = cur % 10
            cur //= 10
            i-=1

        if cur:
            digits = [cur] + digits
        
        return digits