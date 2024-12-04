class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m, n = len(str1), len(str2)
        if n > m:
            return False

        first, second = -1, -1
        while first < m and second < n:
            first += 1
            second += 1
            # Find matching char with diff <= 1
            while first < m and second < n:
                next_char = chr(((ord(str1[first]) - ord('a') + 1) % 26) + ord('a'))
                if str2[second] == str1[first] or str2[second] == next_char:
                    break
                first += 1

        if first == m and second < n:
            return False
        return True