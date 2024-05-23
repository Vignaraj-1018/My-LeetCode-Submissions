class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        i = 0
        res = [[] for i in range(numRows)]
        cnt = 0
        hit = False
        while i<len(s):
            res[cnt].append(s[i])
            i+=1
            if cnt+1 == numRows:
                hit = True
            elif cnt-1 == -1:
                hit = False
            if hit:
                cnt-=1
            else:
                cnt+=1
        
        final = []
        for i in range(numRows):
            final.append("".join(res[i]))
        return "".join(final)