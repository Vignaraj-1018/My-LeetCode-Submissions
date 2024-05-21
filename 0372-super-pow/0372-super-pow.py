class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        num = 0
        for i in b:
            num = num*10 + i
        
        return pow(a,num,1337)