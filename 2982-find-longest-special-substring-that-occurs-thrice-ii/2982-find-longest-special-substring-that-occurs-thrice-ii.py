class Solution:
    def maximumLength(self, s: str) -> int:
        top3freq = [[-1, -1, -1] for _ in range(26)]

        last_seen = '*'
        win_len = 0

        for curr in s:
            idx = ord(curr) - ord('a')
            win_len = win_len + 1 if curr == last_seen else 1
            last_seen = curr

            min_index = top3freq[idx].index(min(top3freq[idx]))
            if win_len > top3freq[idx][min_index]:
                top3freq[idx][min_index] = win_len

        max_len = -1
        for freq in top3freq:
            max_len = max(max_len, min(freq))

        return max_len