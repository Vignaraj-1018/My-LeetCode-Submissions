class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        cur = 0
        l = 0
        unique = set()
        
        for r in range(len(nums)):
            
            while nums[r] in unique or len(unique) == k:
                unique.remove(nums[l])
                cur -= nums[l]
                l += 1
            
            cur += nums[r]
            unique.add(nums[r])
            
            if len(unique) == k:
                res = max(res, cur)
        
        return res