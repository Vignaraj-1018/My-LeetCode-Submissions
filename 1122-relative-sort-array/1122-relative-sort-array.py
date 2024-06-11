class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {}
        for i in arr1:
            count[i] = count.get(i,0) + 1
            
        # print(count)
        
        res = []
        
        for i in arr2:
            res.extend([i]*count[i])
            count[i]=0
        
        for i in sorted(count):
            if count[i]:
                res.extend([i]*count[i])
        
        return res