class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n

        l, cur_sum = 0, 0
        for r in range(n + abs(k)):
            
            cur_sum += code[r % n]
            
            if r - l + 1 > abs(k):
                cur_sum -= code[l % n]
                l = (l + 1) % n
                
            if r - l + 1 == abs(k):
                if k < 0:
                    res[(r + 1) % n] = cur_sum
                elif k > 0:
                    res[(l - 1) % n] = cur_sum
            
        return res