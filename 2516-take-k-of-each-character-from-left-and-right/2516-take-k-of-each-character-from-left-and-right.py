class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = [0, 0, 0]
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        if min(count) < k:
            return -1
        
        res = float('inf')
        l = 0
        n = len(s)
        for r in range(n):
            count[ord(s[r]) - ord('a')] -= 1
            
            while min(count) < k:
                count[ord(s[l]) - ord('a')] += 1
                l += 1
            
            res = min(res, n - (r - l + 1))
        
        return res