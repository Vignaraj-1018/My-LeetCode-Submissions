class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = set()
        res = 0
        
        for i in s:
            if i in cnt:
                cnt.remove(i)
                res+=2
            else:
                cnt.add(i)
        if cnt:
            res+=1
        
        return res
            