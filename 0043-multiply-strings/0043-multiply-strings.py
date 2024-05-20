class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        
        def getNumber(num):
            val = 0
            for i in num:
                val = val*10 + int(i)
            
            return val
        
        num1 = getNumber(num1)
        num2 = getNumber(num2)
        
        res = num1 * num2
        
        return str(res)