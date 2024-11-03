class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)

        for _ in range(n):

            if s == goal:
                return True

            s = s[-1] + s[:-1]

        return False