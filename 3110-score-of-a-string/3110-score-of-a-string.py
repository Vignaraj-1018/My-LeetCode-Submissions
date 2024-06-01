class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i, j in zip(s[:-1], s[1:]):
            res += abs(ord(i)-ord(j))

        return res
