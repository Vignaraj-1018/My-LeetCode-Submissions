class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s,2)
        print(n)
        cnt = 0
        while n != 1:
            if n & 1:
                n += 1
            else:
                n = n // 2
            cnt += 1
        return cnt