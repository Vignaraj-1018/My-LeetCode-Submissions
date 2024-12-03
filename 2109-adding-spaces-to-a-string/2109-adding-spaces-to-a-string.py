class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        
        cur = 0
        for n in spaces:
            res.append(s[cur:n])
            cur = n
        res.append(s[cur:])
        return " ".join(res)