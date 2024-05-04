class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_n = bin(n)
        ans = []
        for i in str(bin_n[2:]):
            if i == '1':
                ans.append('0')
            else:
                ans.append('1')
        
        return int(''.join(ans),2)