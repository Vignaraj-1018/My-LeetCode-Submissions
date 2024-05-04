class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)
        ans = 0
        for i in str(bin_n):
            if i == '1':
                ans+=1
        
        return ans