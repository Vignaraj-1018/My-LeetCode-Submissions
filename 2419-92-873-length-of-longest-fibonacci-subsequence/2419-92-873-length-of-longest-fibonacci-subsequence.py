class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        longest = 0

        for sum_idx in range(2, n):
            a, b = 0, sum_idx - 1
            while a < b:
                if arr[a] + arr[b] < arr[sum_idx]:
                    a += 1
                elif arr[a] + arr[b] > arr[sum_idx]:
                    b -= 1
                else:
                    dp[b][sum_idx] = 1 + dp[a][b]
                    longest = max(longest, dp[b][sum_idx])
                    a += 1
                    b -= 1
        return 2 + longest if longest > 0 else 0