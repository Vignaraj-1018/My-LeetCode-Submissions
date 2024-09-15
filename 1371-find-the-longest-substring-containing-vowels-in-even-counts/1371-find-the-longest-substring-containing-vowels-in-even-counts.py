class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        res = 0
        mask = 0
        mask_to_idx = {0:-1}
        
        vowels = "aeiou"
        
        for i, c in enumerate(s):
            
            if c in vowels:
                mask = mask ^ (1 + ord(c) - ord('a'))
            
            if mask in mask_to_idx:
                res = max(res, i - mask_to_idx[mask])
            
            else:
                mask_to_idx[mask] = i
        
        return res