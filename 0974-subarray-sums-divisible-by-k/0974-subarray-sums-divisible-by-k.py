class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = [0]*k
        _sum = 0
        
        for i in nums:
            _sum += i%k
            counts[_sum % k] +=1
        
        res = counts[0]
        for c in counts:
            res+= (c*(c-1)) // 2
            
        return res