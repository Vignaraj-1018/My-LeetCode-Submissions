class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = (10 ** 9) + 7
        sub_array = []
        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += nums[j]
                sub_array.append(cur_sum)
        sub_array.sort()
        return sum(sub_array[left - 1 : right]) % MOD