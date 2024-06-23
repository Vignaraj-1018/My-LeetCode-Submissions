class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxDeque = deque()
        minDeque = deque()
        l = 0
        max_length = 0

        for r in range(len(nums)):
            while maxDeque and nums[maxDeque[-1]] <= nums[r]:
                maxDeque.pop()
            maxDeque.append(r)

            while minDeque and nums[minDeque[-1]] >= nums[r]:
                minDeque.pop()
            minDeque.append(r)

            while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
                l += 1
                if maxDeque[0] < l:
                    maxDeque.popleft()
                if minDeque[0] < l:
                    minDeque.popleft()

            max_length = max(max_length, r - l + 1)

        return max_length