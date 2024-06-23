class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i in range(len(s)):
            lastIndex[s[i]] = i

        size, end = 0, 0
        res = []

        for i in range(len(s)):
            end = max(end, lastIndex[s[i]])
            size += 1
            if i == end:
                res.append(size)
                size = 0
                end  = 0

        return res