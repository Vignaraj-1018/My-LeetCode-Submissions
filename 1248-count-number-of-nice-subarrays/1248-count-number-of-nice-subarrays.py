class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count_map = defaultdict(int)
        odd_count_map[0] = 1

        odd_count = 0
        res = 0

        for num in nums:
            if num % 2:
                odd_count += 1
            
            if odd_count >= k:
                res += odd_count_map[odd_count - k]
            
            odd_count_map[odd_count] += 1
        
        return res