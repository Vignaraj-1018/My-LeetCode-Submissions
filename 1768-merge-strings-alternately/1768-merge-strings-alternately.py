class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i,j = 0,0
        n, m = len(word1), len(word2)
        while i < n and j < m:
            res.append(word1[i])            
            res.append(word2[j])
            i+=1
            j+=1
        
        res = ''.join(res)
        
        if i < n:
            res = res + word1[i:]
        
        if j < m:
            res = res + word2[j:]
            
        return res