class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        merged = []
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        
        prev = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged.append(prev)
                prev = interval
        
        merged.append(prev)
        return merged