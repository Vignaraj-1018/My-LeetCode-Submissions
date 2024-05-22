class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float('inf')
        sum_subarray = 0
        for r in range(len(nums)):
            sum_subarray += nums[r]
            while sum_subarray>=target:
                res = min(res, r-l+1)
                sum_subarray -= nums[l]
                l+=1
        
        if res == float("inf"):
            return 0
        
        return res
