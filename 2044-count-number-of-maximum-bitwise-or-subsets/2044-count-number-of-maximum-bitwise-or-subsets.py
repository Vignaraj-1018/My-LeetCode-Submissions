class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        
        for i in nums:
            max_or |= i
        
        def dfs(i, cur_or):
            nonlocal max_or
            
            if i == len(nums):
                return 1 if cur_or == max_or else 0
            
            return dfs(i + 1, cur_or) + dfs(i + 1, cur_or | nums[i])
            
        return dfs(0, 0)
        