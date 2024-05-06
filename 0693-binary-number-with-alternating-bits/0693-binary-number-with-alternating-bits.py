class Solution:
    def hasAlternatingBits(self, num: int) -> bool:
        bin_num = bin(num)
        bin_num = bin_num[2:]
        n = len(bin_num)
        print(bin_num)
        for i in range(n):
            if i%2==0 and bin_num[i]!='1':
                return False
            elif i%2!=0 and bin_num[i]=='1':
                return False
        
        return True