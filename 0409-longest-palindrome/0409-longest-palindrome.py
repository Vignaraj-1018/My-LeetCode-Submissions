class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = {}
        res = 0
        
        for i in s:
            if i in cnt:
                cnt[i]+=1
                if cnt[i]%2 == 0:
                    res+=2
            else:
                cnt[i]=1
        for c in cnt:
            if cnt[c]%2:
                res+=1
                return res
        
        return res
            