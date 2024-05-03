class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        isCount = True
        for i in s:
            if i == '|':
                isCount = not isCount
            if i == "*" and isCount:
                count +=1
        
        return count