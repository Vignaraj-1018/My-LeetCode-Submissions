class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        
        for i in nums:
            max_or |= i
            
        cache = [[-1] * (max_or + 1) for _ in range(len(nums))]
        
        def dfs(i, cur_or):
            nonlocal max_or
            
            if i == len(nums):
                return 1 if cur_or == max_or else 0
            
            if cache[i][cur_or] != -1:
                return cache[i][cur_or]
            
            cache[i][cur_or] = dfs(i + 1, cur_or) + dfs(i + 1, cur_or | nums[i])
            return cache[i][cur_or]
            
        return dfs(0, 0)
        