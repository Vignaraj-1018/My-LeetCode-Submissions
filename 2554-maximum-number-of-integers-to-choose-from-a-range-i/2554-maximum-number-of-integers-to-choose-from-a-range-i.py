class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        res = 0
        cur = 0
        _banned = set(banned)
        for i in range(1, n + 1):
            
            if i not in _banned:
                cur += i
                if cur > maxSum:
                    break
                res += 1
        
        return res