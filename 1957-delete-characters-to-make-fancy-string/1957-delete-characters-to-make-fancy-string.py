class Solution:
    def makeFancyString(self, s: str) -> str:
        streak, res = 0, ""
        
        for i in range(len(s)):
            
            if s[max(0, i - 1)] == s[i]:
                streak += 1
            else:
                streak = 1
            
            if streak < 3:
                res += s[i]
        
        return res