class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        
        res = float("inf")
        bits = [0] * 32
        
        def bits_update(n, diff):
            for i in range(32):
                if n & (1 << i):
                    bits[i] += diff
                    
        def bits_to_int():
            res = 0
            for i in range(32):
                if bits[i]:
                    res += (1 << i)
            return res
        
        l = 0
        for r in range(len(nums)):
            bits_update(nums[r], 1)
            cur_or = bits_to_int()
            
            while l <= r and cur_or >= k:
                res = min(res, r - l + 1)
                bits_update(nums[l], -1)
                cur_or = bits_to_int()
                l += 1
            
        return -1 if res == float("inf") else res