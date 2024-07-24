class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def getMappedValue(num):
            
            res = 0
            base = 1
            if num == 0:
                res = mapping[0]
            while num:
                res += base * mapping[num%10]
                num //= 10
                base *= 10
            return res
        
        pairs = []
        for i, num in enumerate(nums):
            pairs.append((getMappedValue(num), i))

        pairs.sort()
        return [nums[i] for n,i in pairs]