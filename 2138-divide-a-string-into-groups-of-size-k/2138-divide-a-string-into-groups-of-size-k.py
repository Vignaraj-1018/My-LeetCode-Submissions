class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        c = 0
        cur = []
        for i in range(len(s)):
            cur.append(s[i])
            c+=1
            if c==k:
                res.append("".join(cur))
                c=0
                cur=[]
        if cur:
            cur.append(fill*(k-c))
            res.append("".join(cur))

        return res