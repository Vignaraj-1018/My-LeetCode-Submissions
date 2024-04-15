class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, res = 0, len(nums)-1, nums[0]

        while l <= r:
            if nums[l]<nums[r]:
                res = min(res,nums[l])
                break
            mid = (r+l)//2
            res = min(res,nums[mid])
            if nums[mid]>=nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res