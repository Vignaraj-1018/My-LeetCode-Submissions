class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0

        while n>=2:
            if n%2==0:
                res += n/2
                n = n/2
            else:
                res += (n-1)/2
                n = ((n-1)/2)+1
        
        return int(res)