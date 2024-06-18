class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        maxProfit = 0
        best = 0
        j = 0
        for w in worker:
            while j < len(jobs) and w >= jobs[j][0]:
                best = max(best, jobs[j][1])
                j += 1
            maxProfit += best
        
        return maxProfit