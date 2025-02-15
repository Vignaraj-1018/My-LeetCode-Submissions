class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def partition(i, cur, target, string, l):
            if i == l  and cur == target:
                return True
            
            for j in range(i, l):
                if partition(j + 1, cur + int(string[i:j + 1]), target, string, l):
                    return True
                
            return False

        res = 0
        for i in range(1, n + 1):
            num_str = str(i * i)
            if partition(0, 0, i , num_str, len(num_str)):
                res += i * i
        
        return res