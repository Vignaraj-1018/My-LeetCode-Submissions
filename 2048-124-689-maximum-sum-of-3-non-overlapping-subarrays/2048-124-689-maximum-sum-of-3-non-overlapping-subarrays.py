class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        k_sums = [sum(nums[:k])]
        for i in range(k, n):
            k_sums.append(k_sums[-1] + nums[i] - nums[i - k])

        dp = {}

        def get_max_sum(i, cnt):
            if cnt == 3 or i > n - k:
                return 0

            if (i, cnt) in dp:
                return dp[(i, cnt)]

            include = k_sums[i] + get_max_sum(i + k, cnt + 1)
            skip = get_max_sum(i + 1, cnt)

            dp[(i, cnt)] = max(include, skip)
            return dp[(i, cnt)]
        

        i = 0
        indices = []
        cnt = 0

        while i <= n - k and cnt < 3:
            include = k_sums[i] + get_max_sum(i + k, cnt + 1)
            skip = get_max_sum(i + 1, cnt)

            if include >= skip:
                indices.append(i)
                cnt += 1
                i += k
            else:
                i += 1

        return indices
        
