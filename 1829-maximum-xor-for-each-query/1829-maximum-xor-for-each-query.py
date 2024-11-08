class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        
        res = []
        mask = (1 << maximumBit) - 1
        
        for n in reversed(nums):
            res.append(xor ^ mask)
            xor ^= n
            
        return res