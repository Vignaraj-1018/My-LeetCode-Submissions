class Solution:
    def skip_spaces(self, s, n, pos):
        while pos < n and s[pos] == '_':
            pos += 1
        return pos

    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        first = second = 0
        limit_idx = -1

        while first < n:

            first = self.skip_spaces(start, n, first)
            second = self.skip_spaces(target, n, second)

            if first == n and second == n:
                return True
            if first == n or second == n or start[first] != target[second]:
                return False

            if start[first] == 'L' and (second <= limit_idx or second > first):
                return False
            elif start[first] == 'R' and first > second:
                return False

            limit_idx = second
            first += 1
            second += 1

        first = self.skip_spaces(start, n, first)
        second = self.skip_spaces(target, n, second)

        return first == n and second == n