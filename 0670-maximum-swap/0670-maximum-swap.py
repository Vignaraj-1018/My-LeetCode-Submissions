class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        
        max_d = "0"
        max_i = -1
        swap_i, swap_j = -1, -1
        
        for i in reversed(range(len(num))):
            
            if num[i] > max_d:
                max_d = num[i]
                max_i = i
                
            if num[i] < max_d:
                swap_i, swap_j = i, max_i
        
        if swap_i != -1:
            num[swap_i], num[swap_j] = num[swap_j], num[swap_i]
        
        return int("".join(num))