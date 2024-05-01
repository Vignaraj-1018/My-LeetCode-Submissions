class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        res = []
        countS = defaultdict(int)
        countT = defaultdict(int)
        
        for i in s:
            countS[i]+=1
        
        for i in t:
            countT[i]+=1
            
        for i in countT:
            n = countT[i]-countS[i]
            res.append(i*n)
        
        return ''.join(res)