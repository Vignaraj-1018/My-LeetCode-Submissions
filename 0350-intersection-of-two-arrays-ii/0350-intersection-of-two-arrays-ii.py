class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        
        for i in nums1:
            freq[i] = 1 + freq.get(i, 0)
        
        # print(freq)
        res = []
        for i in nums2:
            if i in freq and freq[i] > 0:
                res.append(i)
                freq[i] -= 1
        
        return res