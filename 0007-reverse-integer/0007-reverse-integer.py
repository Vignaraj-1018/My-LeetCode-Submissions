class Solution:
    def reverse(self, x: int) -> int:
        
        ans = 0
        negativeFlag = False
        if x<0:
            negativeFlag = True
            x*=-1
        while x>0:
            ans = ans*10 + x%10
            x//=10
            
        if ans>(2**31)-1 or ans<(-2**31):
            return 0
        return ans if not negativeFlag else ans*-1