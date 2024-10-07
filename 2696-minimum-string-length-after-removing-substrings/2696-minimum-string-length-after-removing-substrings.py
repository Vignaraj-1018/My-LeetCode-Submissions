class Solution:
    def minLength(self, s: str) -> int:
        
        def removeSubString(s):
            
            if "AB" not in s and "CD" not in s:
                return s
            
            if 'AB' in s:
                index = s.find("AB")
                s = s[:index] + s[index + 2:]
            
            elif 'CD' in s:
                index = s.find("CD")
                s = s[:index] + s[index + 2:]
            
            return removeSubString(s)
        
        return len(removeSubString(s))