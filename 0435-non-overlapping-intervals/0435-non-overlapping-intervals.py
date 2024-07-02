class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        cur = intervals[0][1]
        for st, ed in intervals[1:]:
            if st >= cur:
                cur = ed
            else:
                res += 1
                cur = min(cur, ed)
        
        return res