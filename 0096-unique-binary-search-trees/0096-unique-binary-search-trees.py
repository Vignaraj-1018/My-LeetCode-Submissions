class Solution:
    def numTrees(self, n: int) -> int:
        
        def fact(n):
            if n == 0:
                return 1
            else:
                return n*fact(n-1)

        res = (fact(2*n)/(fact(n)**2))//(n+1)

        return int(res)