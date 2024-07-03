class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        res = float('inf')
        for l in range(4):
            r = n - 4 + l
            res = min(res, nums[r] - nums[l])
        return res