class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        subset = []
        
        def dfs():
            
            if len(subset)== len(nums):
                res.append(subset.copy())
                return
            
            for c in range(len(nums)):
                if nums[c] not in subset:
                    subset.append(nums[c])
                    dfs()
                    subset.pop()
        
        dfs()
        
        return res