class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        for _ in range(k):
            res = str(sum(int(digit) for digit in res))
        
        return int(res)