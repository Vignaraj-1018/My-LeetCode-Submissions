class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def getMappedValue(num):
            temp = str(num)
            res = 0
            for n in temp:
                res = res * 10 + mapping[int(n)]
            return res
            
        mappedValues = defaultdict(list)
        for num in nums:
            mappedValues[getMappedValue(num)].append(num)

        res = []
        for num in sorted(mappedValues):
            res.extend(mappedValues[num])
        return res