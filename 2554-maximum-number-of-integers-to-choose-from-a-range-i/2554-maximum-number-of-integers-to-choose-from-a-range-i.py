class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        res = 0
        cur = 0
        _banned = set(banned)
        for i in range(1, n + 1):
            
            if i in _banned:
                continue
            
            if cur + i <= maxSum:
                cur += i
                res += 1
            else:
                break
        
        return res