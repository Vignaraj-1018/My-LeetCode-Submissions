class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        a_count_right = 0
        for i in range(n):
            if s[i] == 'a':
                a_count_right += 1
        
        b_count_left = 0
        res = n
        for i, ch in enumerate(s):
            if ch == 'a':
                a_count_right -= 1
            res = min(res, b_count_left + a_count_right)
            if ch == 'b':
                b_count_left += 1

        return res