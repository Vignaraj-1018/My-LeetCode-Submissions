class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = []
        n = len(code)
        for i in range(n):
            if k > 0:
                cur, j = 0, (i + 1) % n
                for _ in range(k):
                    cur += code[j]
                    j = (j + 1) % n
                res.append(cur)
            elif k < 0:
                cur, j = 0, (i - 1) % n
                for _ in range(abs(k)):
                    cur += code[j]
                    j = (j - 1) % n
                res.append(cur)
            else:
                res.append(0)
        return res