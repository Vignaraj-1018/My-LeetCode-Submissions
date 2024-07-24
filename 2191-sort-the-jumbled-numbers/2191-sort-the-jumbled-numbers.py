class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def getMappedValue(num):
            temp = str(num)
            res = []
            for n in temp:
                res.append(str(mapping[int(n)]))
            
            return int("".join(res))
            
        mappedValues = defaultdict(list)
        for num in nums:
            mappedValues[getMappedValue(num)].append(num)

        res = []
        for num in sorted(mappedValues):
            res.extend(mappedValues[num])
        return res