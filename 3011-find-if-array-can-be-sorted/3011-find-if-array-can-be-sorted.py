class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        def set_count(n):
            return bin(n).count("1")
        
        cur_min, cur_max, prev_max = nums[0], nums[0], float("-inf")
        
        for n in nums:
            if set_count(n) == set_count(cur_min):
                cur_min = min(cur_min, n)
                cur_max = max(cur_max, n)
                
            else:
                if cur_min < prev_max:
                    return False
                
                prev_max = cur_max
                cur_min = cur_max = n
        
        if cur_min < prev_max:
            return False
        return True
        