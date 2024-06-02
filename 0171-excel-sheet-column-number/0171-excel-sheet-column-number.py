class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        n =len(columnTitle) - 1
        i = 0

        while n >= 0:
            res += (ord(columnTitle[n]) - ord('A') + 1) * (26 ** i)
            n-=1
            i+=1

        return res