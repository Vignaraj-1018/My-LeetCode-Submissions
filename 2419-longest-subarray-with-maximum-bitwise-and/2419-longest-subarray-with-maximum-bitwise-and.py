class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        size = 0
        big = max(nums)
        for i in nums:
            if i == big:
                size += 1
            else:
                size = 0
            
            res = max(size, res)
        
        return res