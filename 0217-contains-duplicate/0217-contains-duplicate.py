class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        numsSet = set(nums)
        return len(nums)!=len(numsSet)