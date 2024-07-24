class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def getMappedValue(num):
            temp = str(num)
            res = 0
            for n in temp:
                res = res * 10 + mapping[int(n)]
            return res
        
        pairs = []
        for i, num in enumerate(nums):
            pairs.append((getMappedValue(num), i))

        pairs.sort()
        return [nums[i] for n,i in pairs]