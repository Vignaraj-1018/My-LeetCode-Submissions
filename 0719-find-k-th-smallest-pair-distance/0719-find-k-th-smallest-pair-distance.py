class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        l, r = 0, max(nums)

        def helper(dist):
            l, res = 0, 0

            for r in range(len(nums)):
                while nums[r] - nums[l] > dist:
                    l += 1
                res += r - l
            return res
            

        while l < r:
            mid = l + ((r - l) // 2)
            pairs = helper(mid)
            if pairs >= k:
                r = mid
            else:
                l = mid + 1
        
        return l