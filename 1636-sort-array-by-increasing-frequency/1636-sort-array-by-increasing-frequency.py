class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        nums.sort(key = lambda i: [freq[i], -i])
        
        return nums